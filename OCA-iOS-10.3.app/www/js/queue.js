/**
 * The GopherQueue handles the processing of queued requests when the device is in offline mode.
 */
var GopherQueue = {
	PUT:{},
	POST:{},
	DELETE:{},
	currentRetry: 5000,
	currentTimer: null,
	createdCache: {},

	/**
	 * Add a pending request to the queue.
	 * 
	 * @param {object} ajax the request data
	 * @param {object} info the meta data, including the timestamp, originating page, etc
	 */
	add: function(ajax, info){
		var obj = {
			ID: null,
			ajax: ajax,
			info: info,
			name: ajax.method + ' to ' + ajax.url
		};
		obj.info.pageHash = obj.info.pageHash.replace('ui-state=dialog&', ''); //strip cruft (especially for comms)
		if (ajax.method == 'POST'){
			obj.info.pageHash += "&timestamp=" + obj.info.timestamp;
			if (obj.info.pageHash.indexOf('?') == -1) {
				obj.info.pageHash = obj.info.pageHash.replace('&', '?'); //if there is not currently a query string
			}
			obj.info.currentlyEditing = false;
			
			if (!this.POST[ajax.url]) this.POST[ajax.url] = {};
			this.POST[ajax.url][obj.info.timestamp] = obj; //could be a queue of new items to add to this endpoint, so index by the time the request was made
		} else {
			this[ajax.method][ajax.url] = obj;
		}

		this.storeItem(ajax.method, ajax.url, obj.info.timestamp, obj);
		storage.updateBadge();
		if (!this.currentTimer) this.flush(); //try to submit straight away
	},
	/**
	 * Remove a pending request from the queue
	 * 
	 * @param {string} method POST, PUT or DELETE
	 * @param {string} url URL the request was being sent to 
	 * @param {timestamp} [timestamp] POST requests are keyed on timestamp in addition to URL, so the timestamp must be provided to delete a pending POST
	 */
	remove: function(method, url, timestamp){
		if (method == 'POST'){
			if (this.POST[url] && this.POST[url][timestamp]) {
				delete this.POST[url][timestamp];
				if (Object.keys(this.POST[url]).length == 0){
					delete this.POST[url];
				}
			}
		}
		else if (this[method][url]) delete this[method][url];
		this.removeItem(method, url, timestamp);
		storage.updateBadge();
	},
	/**
	 * Function to check if a particular URL has pending requests. Used to indicate that a particular result (e.g. index listing) may be incomplete or out of date due to unsubmitted requests
	 * @param {string} url URL of the request
	 * @param {timestamp} [timestamp] POST requests are keyed against timestamp as well. Required if a specific POST request is being requested for editing
	 * @return {object} Depending on parameters, an object containing a message and possibly data to display, or a cached POST request.
	 */
	has: function(url, timestamp){
		if (url.indexOf('?') !== -1){
			var bits = url.split('?');
			url = bits[0];
		}
		var response = false;
		if (this.PUT[url]){
			var item = this.PUT[url];
			response = {
				data: JSON.parse(item.ajax.data),
				method: 'PUT',
				message: "This record has unsubmitted local changes"
			}
		} else if (this.DELETE[url]){
			response = {
				data: false,
				method: 'DELETE',
				message: "This record has a pending delete request"
			}
		} else if (this.POST[url]){
			if (timestamp){
				response = this.POST[url][timestamp]; //a specific item has been requested for editing
			} else {
				//this is a listing endpoint, return all offline children
				response = [];
				for (var k in this.POST[url]){
					var item = this.POST[url][k];
					var route = item.info.pageHash.replace("New?", "Pending?"); //'Pending' is a special keyword that will be translated by ViewUtil.getRoute
					route = route.replace('pending=true&', ''); 				//this will be re-added later, and might be present if we are in a offline-child-of-offline-item situation
					route = route.replace(/type=\d+&/, ''); 					//dont need type, can be found in object data

					//pending items might be the parent of the tree, so make sure the name can be looked up by /pending/... URL
					if (!item.info.type){
						var data = JSON.parse(item.ajax.data);
						item.info.type = data.TypeURL;
					}
					if (item.info.name && item.info.type){
						var typeURL = item.info.type.replace(Configuration.getAPIUrl(), ''); //exampleoca.com/api/v2/assettype/123
						typeURL = typeURL.replace(Configuration.getAPIPath(), ''); 			 //api/v2/assettype/123
						var bits = typeURL.split('/'); 										 ///assettype/123 -> [, assettype, 123]
						bits.pop(); //ID
						var typeName = bits.pop().replace('type', '');						 // assettype -> asset
						OCA.name('/pending/' + typeName + '/' + item.info.timestamp, item.info.name);
					}

					response.push({
						Name: item.info.name || item.info.desc,
						URL: route,
						OtherFields: {},
						DynamicFields: [],
					});
				}
			}
		}
		//dirty hack for report drafts which could exist at either endpoint without an easy way to tell which is correct
		if (this.POST[url + '/drafts']){
			var drafts = this.has(url + '/drafts', timestamp);
			if (response && $.isArray(response) && drafts && $.isArray(drafts)) {
				response = response.concat(drafts);
			} else if (!response && drafts){
				response = drafts;
			}
		}
		return response;
	},
	/**
	 * Get the list of items currently pending
	 */
	get: function(callback){
		var queue = [];
		var k;
		for (k in this.PUT)		queue.push(this.PUT[k]);
		for (k in this.DELETE)	queue.push(this.DELETE[k]);
		for (k in this.POST)	for (var p in this.POST[k]) queue.push(this.POST[k][p]);

		//return queue in order of the times, most recent to oldest
		queue.sort(function(a, b){
			return b.info.timestamp - a.info.timestamp;
		});

		if (callback) {
			callback(queue);
			return null;
		} else {
			return queue;
		}
	},
	/**
	 * Attempt to flush the queue by sending a 'canary' request to check for connectivity
	 * If successful, call this.processQueue()
	 * If unsuccessful, call this.noFlush()
	 */
	flush: function(){
		if (localStorage['offline'] == 1){
			console.log("No flush - fake offline");
			return;
		}

//		console.log('flushing ' + OcaSession.getSessionId());
		if (this.currentTimer) clearTimeout(this.currentTimer);
		this.currentTimer = null;
		
		var count = Object.keys(this.PUT).length + Object.keys(this.POST).length + Object.keys(this.DELETE).length;
		if (count == 0) {
			return; //nothing to flush
		}
		console.log(count + " items in queue");
		
		if (!OCASession.isLoggedIn()){	//dont submit if not logged in
			this.stepOff();
			return;
		}
		
		console.log('sending canary down the mine');
		new Gopher({
			url: "/session",
			backgroundMode: true,
			dontCache: true
		}, $.proxy(this.processQueue, this), $.proxy(this.stepOff, this)).run();
	},
	/**
	 * Process the queue of pending items, one at a time. Loops through the PUT, POST and DELETE queues to find the first request, then processes it.
	 * If the found request is being currently edited (applies to POSTs only), it is skipped.
	 */
	processQueue: function(){
		if (this.submitting) return; //something is already trying to process the queue, back off
		this.submitting = true;

		//trying to only submit one thing at one time, but if somehow the submitting flag was never turned off, clear it in a timeout.
		if (this.submitTimer) {
			clearTimeout(this.submitTimer);
			this.submitTimer = null;
		}
		this.submitTimer = setTimeout(function(){
			this.submitting = false;
			this.flush();
		}.bind(this), 30000);

		var count = Object.keys(this.PUT).length + Object.keys(this.POST).length + Object.keys(this.DELETE).length;
		if (count == 0) {
			this.submitting = false;
			return; //nothing to flush
		}

		//TODO what happens if an invalid item is blocking ?
		var k, item;
		for (k in this.PUT){
			item = this.PUT[k];
            if (item.info.invalid) {
                item = null;
                continue;
            }
			break;
		}
		if (!item){
			for (k in this.POST){
				if (item) break;
				for (var p in this.POST[k]){
					item = this.POST[k][p];
					if (item.info.currentlyEditing || item.info.invalid) {
                        item = null;
						continue;
					}
					if (item.info.url && item.info.url.indexOf("/pending") === 0){
						//this item depends on a parent which is/was also in the queue.
						// convert /pending/parenttype/parentID/children URL like /pending/eme/123123/emes into the pendingCache key /pending/123123
						var bits = item.info.url.split("/");
						var key = ['', bits[1], bits[3]].join('/');
						if (this.createdCache[key]){
							var parentURL = this.createdCache[key];
							parentURL = parentURL.replace(Configuration.getAPIPath(), ''); //prevent /api/v2/ being added twice by stripping it out of the cached path
							var newURL = parentURL + '/' + bits[4];

							item.info.keyURL = item.ajax.url;
							item.ajax.url = item.ajax.url.replace(item.info.url, newURL);
							item.info.url = newURL;
						} else {
							//this is a child of a pending item. don't process it.
							item = null;
							continue;
						}
					}
					if (item) break;
				}
			}
		}
		if (!item){
			for (k in this.DELETE){
				item = this.DELETE[k];
                if (item.info.invalid) {
                    item = null;
                    continue;
                }
				break;
			}
		}
		
		//dont submit no item found or if not logged in. 
		// no item found means that there is one POST item in the whole queue but it is currently being edited
        // or the only remaining items have lock conflicts
		if (!item || !OCASession.isLoggedIn()){
			this.stepOff();
		} else {
			this.submitItem(item);
		}
	},
	/**
	 * Handle the resubmission of an item
	 * The item may specify a function to be called to handle resubmission (e.g. Outbound communications). 
	 * Otherwise, the cached ajax request is resent
	 * @param {object} item cached item. item.ajax is the ajax request to resubmit, item.info contains metadata
	 */
	submitItem: function(item){
		this.currentRetry = 5000; //alles gut, reset timer
		if (item.info.upload){
			new FileTransfer().upload(item.ajax.data, item.ajax.url, $.proxy(this.submittedItemOK, this, item), $.proxy(this.noFlush, this, item), item.ajax.options, true);
		} else if (item.info.resubmitter){
			var resubmitter = new window[item.info.resubmitter](item);
		} else {
			item.ajax.success = $.proxy(this.submittedItemOK, this, item);
			item.ajax.error = $.proxy(this.noFlush, this, item);
			item.ajax.timeout = 120000;
			$.ajax(item.ajax);
		}
	},
	/**
	 * Callback for queue processing success.
	 * Get the URL of the new object if applicable, then flush the queue
	 * @param item 		queue item passed in the $.proxy call
	 * @param data		data from ajax response
	 * @param status	status from ajax response
	 * @param xhr		xhr from ajax response
	 */
	submittedItemOK: function(item, data, status, xhr){
		var createdURL = null;
		if (item.ajax.method == 'POST' && xhr && xhr.getResponseHeader){
			createdURL = xhr.getResponseHeader('Location');
		}
		this.flushOut(item, data, createdURL);
	},
	/**
	 * When the queue processing succeeds, remove the item from the queue, update the storage page and then process the next item in the queue.
	 * @param {object} item cached item
	 * @param {object} data ajax data response
	 * @param {string} createdURL URL of submitted item, for object creation requests
	 */
	flushOut: function(item, data, createdURL){
		this.submitting = false;
		util.handleResponseExtras(data);
		//if there were temporary file copies associated with this request, clear them now that it's been submitted
		if (item.info.cleanupFiles && item.info.cleanupFiles.length){
			fileStore.clearFiles(item.info.cleanupFiles);
		}
		if (item.info.keyURL) {	//a child of an offline-created item gets its URL changed, so remove it using the keyURL
			this.remove(item.ajax.method, item.info.keyURL, item.info.timestamp);
		} else {
			this.remove(item.ajax.method, item.ajax.url, item.info.timestamp);
		}
		if (item.ajax.method == 'POST' && createdURL){
			this.createdCache["/pending/" + item.info.timestamp] = createdURL;
		}
		storage.getQueue(); //update storage page
		this.processQueue(); //everything went nicely so lets call the flush function again!
	},
	/**
	 * If the queue processing fails due to no connection, increase the time between retries.
	 * If the submission was made but was somehow invalid or returned with errors, handle the response
	 */
	noFlush: function(item, xhr, status, error){
		this.submitting = false;
		console.log('no flush', xhr, status, error);
//		console.log(JSON.stringify(arguments, null, '\t'));
		if (status == 'timeout' || xhr.status == 0 || xhr.http_status === null || xhr.code == FileTransferError.CONNECTION_ERR){
			this.stepOff();
		} else {
			console.log('queue retry: not timeout, ' + status + ' , ' + error);
			try {
				var response = JSON.parse(xhr.responseText);
				util.handleResponseExtras(response, true);
                item.info.invalid = true;
                var msg = '';
                if (response.errors && response.errors.length) {
                    item.info.errors = response.errors;
                    msg = OCA.getI18n().gettext('Validation error while attempting to sync offline items. Please review the queued submissions.');
                }
                if (xhr.status == 423){
                    item.info.locked = true;
                }
                if (msg) {
                    util.infobar(msg, '#storage', 30);
                }
            } catch (e){

			}
            this.processQueue(); //this item failed, but the device is online. continue processing queue
		}
	},
	/**
	 * Increase the current retry delay by 50%, but do not exceed 5 minutes
	 */
	stepOff: function(){
		this.submitting = false;
		this.currentRetry *= 1.5;
		this.currentRetry = Math.min(this.currentRetry, 1000 * 60 * 5); //try at least once every 5 minutes
		this.currentTimer = setTimeout($.proxy(this.flush, this), this.currentRetry);
		console.log('trying again in ' + this.currentRetry + " ms");
	},
	/**
	 * Wipe the pending queues
	 */
	wipe: function(deferred){
		this.PUT = {};
		this.POST = {};
		this.DELETE = {};
		this.currentRetry = 5000;
		this.createdCache = {};

		var d = deferred ? deferred.resolve : dbStore.d;
		var e = deferred ? deferred.resolve : dbStore.e;
		if (dbStore.isReady()) {
			dbStore.DB.transaction(function(tx) {
				tx.executeSql("DELETE FROM offlinesync WHERE 1=1", [], d, e);
			}, e, d);
		} else {
			if (deferred) { deferred.resolve(); }
		}
		storage.updateBadge(0);
	},
	/**
	 * Initialise the queues by loading the persistant storage and loading any data from it, then call flush to check if anything can be submitted.
	 */
	init: function(done){

		if (!dbStore.DB){
			$(window).one('databaseReady', GopherQueue.init.bind(this, done));
			return;
		}

		dbStore.DB.transaction(function(tx){
			var query = "SELECT ID, method, url, timestamp, data FROM offlinesync";
			tx.executeSql(query, [], function(tx, results){
				for (var i = 0; i < results.rows.length; i++){
					var row = results.rows.item(i);
					this.restoreItem(row.method, row.url, row.timestamp, JSON.parse(row.data), row.id);
				}
				this.flush();
				if (results.rows.length == 0){ //nothing in the queue, which means any old files are unrelated to queue items.
					fileStore.removeOldFiles();
				}
				if (done) done();
			}.bind(this), dbStore.e);
		}.bind(this), dbStore.e, dbStore.n);

		$(window).on('loggedIn', function(){    //clear queue when changing systems
			GopherQueue.wipe();
		});
	},
	restoreItem: function(method, url, timestamp, item, id){
		item.ID = id;

		if (item.info.cleanupFiles && item.info.cleanupFiles.length){
			item.info.currentlyEditing = true;
			item.info.filesToGo = item.info.cleanupFiles.length;
			item.ajax.data = JSON.parse(item.ajax.data); //will be re-stringified after all files are loaded
			this.restoreDataURIs(item.ajax.data, item);
		}

		if (method == 'POST'){
			if (!this.POST[url]) {
				this.POST[url] = {};
			}
			this.POST[url][timestamp] = item;
		} else {
			this[method][url] = item;
		}
	},
	/** Save a single item in the persistent storage. */
	storeItem: function(method, url, timestamp, data){
		if (!dbStore.DB){
			//should only occur if things are added before full-initialisation which means its not an explicit user action, just a mistake
			console.error("Where's the database ?!");
		}

		var item = $.extend(true, {}, data);
		if (item.info.cleanupFiles && item.info.cleanupFiles.length){
			item.ajax.data = JSON.stringify(this.stripDataURIs(JSON.parse(item.ajax.data)));
		}

		dbStore.DB.transaction(function(tx){
			tx.executeSql("INSERT INTO offlinesync (method, url, timestamp, data) VALUES (?,?,?,?)",
			[method, url, timestamp, JSON.stringify(item)], function(tx, result){
				if (result.insertId){
					data.ID = result.insertId;
				}
			}, dbStore.e)
		}, dbStore.e);
	},
	updateItem: function(ID, data){
		if (!dbStore.DB){
			//should only occur if things are added before full-initialisation which means its not an explicit user action, just a mistake
			console.error("Where's the database ?!");
		}

		dbStore.DB.transaction(function(tx){
			tx.executeSql("UPDATE offlinesync SET data = ? WHERE ID = ?",
						  [ID, data], dbStore.n, dbStore.e)
		}, dbStore.e);
	},
	removeItem: function(method, url, timestamp){
		if (!dbStore.DB){
			//should only occur if things are added before full-initialisation which means its not an explicit user action, just a mistake
			console.error("Where's the database ?!");
		}

		dbStore.DB.transaction(function(tx){
			var params = [method, url];
			var sql = "DELETE FROM offlinesync WHERE method = ? AND url = ?";
			if (timestamp) {
				params.push(timestamp);
				sql += " AND timestamp = ?";
			}
			tx.executeSql(sql, params, dbStore.n, dbStore.e)
		}, dbStore.e);
	},
	/**
	 * recursively seek out any dataURIs and remove them from the database payload as long as there is a file:// url equivalent
	 * @param data
	 * @returns {*}
	 */
	stripDataURIs: function(data){
		if (data.dataURI && data.filepath && data.filepath.substr(0, 7) == 'file://'){
			data.dataURI = null; //keep key present
			return data;
		}
		for (var k in data){
			if ($.isPlainObject(data[k])) {
				data[k] = this.stripDataURIs(data[k]);
			} else if ($.isArray(data[k])){
				for (var i = 0; i < data[k].length; i++){
					if ($.isPlainObject(data[k][i])) {
						data[k][i] = this.stripDataURIs(data[k][i]);
					}
				}
			}
		}
		return data;
	},
	/**
	 * recursively seek out any null'd dataURIs and load the sibling URL as a restored dataURI.
	 * once loaded, the callback will determine if all files have been restored
	 * @param data AJAX data object
	 * @param item GopherQueue item
	 * @returns {*}
	 */
	restoreDataURIs: function(data, item){
		//find any objects with stripped dataURI and a file path reference
		if (data.dataURI === null && data.filepath && data.filepath.substr(0, 7) == 'file://'){
			//start file load
			var filename = data.filepath.split('/').pop();
			var filepath = cordova.file.dataDirectory + filename; //absolute path might change due to iOS sandbox - frequently in dev, but also when app updates etc. reconstruct as dir + name
			new Gopher({url: filepath, mode: 'data', mime: data.mime, dontCheckCache: true, backgroundMode: true}, $.proxy(this.gotDataUri, this, data, item), function(){
				//console.log('couldnt get file!', url, arguments)
			}).run();
		}
		for (var k in data){
			if ($.isPlainObject(data[k])) {
				data[k] = this.restoreDataURIs(data[k], item);
			} else if ($.isArray(data[k])){
				for (var i = 0; i < data[k].length; i++){
					if ($.isPlainObject(data[k][i])) {
						data[k][i] = this.restoreDataURIs(data[k][i], item);
					}
				}
			}
		}
		return data;
	},
	gotDataUri: function(fileUploadData, item, dataURI){
		fileUploadData.dataURI = dataURI;
		item.info.filesToGo--;
		if (item.info.filesToGo === 0){
			item.info.currentlyEditing = false;
			item.ajax.data = JSON.stringify(item.ajax.data); //all files restored so restore the payload to the stringified version
		}
	}
};