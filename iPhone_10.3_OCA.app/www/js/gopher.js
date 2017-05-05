/**
 * The Gopher class handles almost all of the requests to the server. 
 * It essentially provides a wrapper around the jQuery AJAX requests which adds the ability to returned cached responses for GETs or resubmit failed requests for POST/PUT/DELETEs.
 * @constructor
 */
function Gopher(param, callbackOK, callbackFail){
    if (OCA.currentAjaxConfig === null) OCA.config();

	//init defaults
	this.base = Configuration.getAPIUrl();
    this.mode = "json";
	this.data = {};
	this.cleanupFiles = this.desc = this.name = this.oldTimestamp = this.resubmitter = this.typeURL = this.mime = null;
	this.dontCache = this.dontCheckCache = this.dontProcessError = this.backgroundMode = this.noExtras = false;

	if (typeof param == 'string'){
		this.url = param;
		param = {url: param};
	}
	//apply parameters
	$.extend(this, param);

	if (this.data.CleanupFiles) {
		this.cleanupFiles = this.data.CleanupFiles;
		delete this.data.CleanupFiles;
	}

    this.url = this.url.replace(Configuration.getAPIUrl(), '');  //full URL was specified, reduce it to the api path
	this.url = this.url.replace(Configuration.getAPIPath(), ''); //endpoint is in the base URL, dont need it twice
	this.callbackOK = callbackOK || log.d;
	this.callbackFail = callbackFail || log.e;

	this.cacheName = this.getCacheName(this.url);
	this.method = null;
	this.status = 0;
}

//counter of the number of currently active requests. Used to display the loading widget.
Gopher.activeRequests = 0;
Gopher.reqLog = [];
Gopher.recentDownloads = {};
Gopher.log = function(n) {
	var c = Gopher.reqLog.length;
	console.log("There are " + c + " items in the log");
	n = n || 20;
	var logs = Gopher.reqLog;
	var start = Math.max(0, c-n);
	for (var l = start; l < logs.length; l++){
		console.log(l + ": " + logs[l]);
	}
};
//occasionally we have to fake an API response
Gopher.emptyResponse = {
	errors: [],
	notices: [],
	responsePayloads: [],
	extraPayloads: [],
	nextPageURL: null,
	prevPageURL: null
}

/**
 * Converts a URL into a valid filename for the cache by stripping invalid characters
 * @param {string} path URL
 * @return {string} valid cache file name
 */
Gopher.prototype.getCacheName = function(path){
	return path.replace(new RegExp("[^a-zA-Z0-9=]", "g"), "-");
};

/**
 * Executes after every successful request made by the Gopher class 
 * 'Success' refers to whether the request was submitted and recieved by the server, not to the returned HTTP status code. 
 * i.e. a form validation error or 500 error would still be a successful request
 * Decrements the active request counter
 */
Gopher.prototype.successfulRequest = function(xhr){
	if (!this.backgroundMode){
		Gopher.activeRequests--;
		Gopher.reqLog.push("inactive : " + this.method + " - " + this.url);
		if (this.backgroundTimeout){
			clearTimeout(this.backgroundTimeout);
			this.backgroundTimeout = null;
		}
	}
}

/**
 * Executes after every unsuccessful request made by the Gopher class. 
 * 'Success' refers to whether the request was submitted and recieved by the server, not to the returned HTTP status code.
 * Decrements the active request counter if not in background mode, and displays a message telling the 
 */
Gopher.prototype.unsuccessfulRequest = function(xhr, status, doCallback){
	if (!this.backgroundMode){
		Gopher.activeRequests--;
		Gopher.reqLog.push("inactive : " + this.method + " - " + this.url);
		if (!this.dontProcessError && ((xhr && (xhr.status == 0 || xhr.http_status === null)) || status == 'timeout') && (this.method == 'PUT' || this.method == 'POST')){
			var callback = doCallback ? $.proxy(this.callbackOK, this) : $.noop;
			util.alertDialog(
				T("Connection timed out or unavailable. This record will be saved locally and resubmitted later"),
				callback,
				T('Offline mode'),
				T('Ok'));
		} else {
			if (doCallback){
				this.callbackOK();
			}
		}
		if (this.backgroundTimeout){
			clearTimeout(this.backgroundTimeout);
			this.backgroundTimeout = null;
		}
	}
	if (xhr && xhr.status) this.status = xhr.status;
}

/**
 * Executes when a request is submitted
 * Increments the active request counter if not in background mode
 */
Gopher.prototype.activatedRequest = function(){
	if (!this.backgroundMode){
		Gopher.activeRequests++;
		Gopher.reqLog.push("  active : " + this.method + " - " + this.url);
	}
}

/**
 * Starts a GET request by first checking if there is a cached version of the response
 * @param {object} [params] optionally, parameters which can be used to set values within the class.
 */
Gopher.prototype.run = function(params){
	this.method = 'GET';
	if (params) $.extend(this, params);
	this.activatedRequest();
    if (this.dontCheckCache){
        this.noCache();
    } else {
	    this.checkCache();
    }
	app.checkLoaded();
};

/**
 * Sends a PUT request.
 * Sets up parameters to send to this.sendData();
 * @param {boolean} [retry] can be set as false to stop the submission being retried in the GopherQueue, but defaults to true
 */
Gopher.prototype.put = function(retry){
	this.method = 'PUT';
	if (retry !== false) retry = true;
	this.sendData({
		url: this.base + this.url,
		data: JSON.stringify(this.data),
		method: 'PUT',
		success: $.proxy(this.putOK, this),
		error: $.proxy(this.requestError, this)
	}, retry);
	this.uncache(); //mark the current cache as expired now to avoid a race condition later.
};

/**
 * Sends a POST request.
 * Sets up parameters to send to this.sendData();
 * If this is an update to something in the offline queue, this.oldTimestamp will be set and used to remove the existing item from the GopherQueue
 * @param {boolean} [retry] can be set as false to stop the submission being retried in the GopherQueue, but defaults to true
 */
Gopher.prototype.post = function(retry){
	this.method = 'POST';
	if (this.oldTimestamp){
		console.log('removing ' + this.oldTimestamp);
		GopherQueue.remove('POST', this.base + this.url, this.oldTimestamp);
	}
	if (retry !== false) retry = true;

	if (this.url.indexOf('/pending') === 0){ //this is a child of an item created offline. lets check to see if it has been resolved to a parent URL
		var bits = this.url.split("/");
		var key = ['', bits[1], bits[3]].join('/');
		if (GopherQueue.createdCache[key]){
			var parentURL = GopherQueue.createdCache[key];
			parentURL = parentURL.replace(Configuration.getAPIPath(), ''); //prevent /api/v2/ being added twice by stripping it out of the cached path
			this.url = parentURL + '/' + bits[4];
		}
	}

	this.sendData({
		url: this.base + this.url,
		data: JSON.stringify(this.data),
		method: 'POST',
		success: $.proxy(this.postOK, this),
		error: $.proxy(this.requestError, this)
	}, retry);
};

/**
 * Sends a DELETE request.
 * Sets up parameters to send to this.sendData();
 * @param {boolean} [retry] can be set as false to stop the submission being retried in the GopherQueue, but defaults to true
 */
Gopher.prototype.sendDelete = function(retry){
	this.method = 'DELETE';
	if (retry !== false) retry = true;
	this.sendData({
		url: this.base + this.url,
		method: 'DELETE',
		success: $.proxy(this.deleteOK, this),
		error: $.proxy(this.requestError, this)
	}, retry)
}

/**
 * Sends a HEAD request
 */
Gopher.prototype.head = function(){
	this.cacheName = 'HEAD' + this.cacheName; //make sure it doesnt collide with any GET caches
	this.run({method: 'HEAD'});
}

/**
 * Extract headers and pass it to the success callback when a HEAD request returns
 */
Gopher.prototype.headOK = function(data, status, xhr){
	var raw = xhr.getAllResponseHeaders();
	var lines = raw.split("\n");
	var headers = {};
	for (var l = 0; l < lines.length; l++){
		var line = lines[l];
		var bits = line.split(":");
		var key = bits.shift();
		var value = $.trim(bits.join(":"));
		headers[key] = value;
	}
	if (xhr && xhr.status) data.status = xhr.status;
	this.successfulRequest();
	this.callbackOK(headers);

	if (this.dontCache) return;

	//convert to API response format for saving in the cache
	var expiry = new Date(Date.now() + 24 * 60 * 60 * 1000); //24 hour expiry for HEAD requests
	var headerExpiry = Date.parse(headers['Expires']);
	if (!isNaN(headerExpiry) && headerExpiry > Date.now()){ //valid date and in the future
		expiry = new Date(headers['Expires']); //but allow the API headers to supercede if valid
	}

	var cacheData = {
		errors: [],
		responsePayloads: headers,
		expiry: expiry.toISOString()
	};
	this.saveCache(cacheData);
}

/**
 * Return MIME type from a given extension
 * @param {string} ext file extension
 * @return {string} MIME type
 */
Gopher.prototype.getMIMEfromExtension = function(ext){
	switch (ext){
		case 'jpg':
		case 'jpeg':
			return 'image/jpg';
		case 'png':
			return 'image/png';
		case 'gif':
			return 'image/gif';
		case 'amr':
			return 'audio/AMR';
		case 'mp3':
			return 'audio/mp3';
		case 'mp4':
			return 'video/mp4';
		case 'pdf':
			return 'application/pdf';
		default: 
			return 'text/plain';
	}
}

/**
 * Uploads a file (filename specified by this.data) to the server
 */
Gopher.prototype.uploadFile = function(retry){
	//expecting this.data to be a fileUri
	var options = {
		fileName: this.data.substr(this.data.lastIndexOf('/') + 1),
		mimeType: 'text/plain'
	};
	var ext = options.fileName.split(".").pop();
	options.mimeType = this.getMIMEfromExtension(ext);

    this.submitFile(options, retry);
}

/**
 * Inbox submit is a special kind of file upload. Additional data is passed with the request - a description of the media and potentially some coordinates
 * 
 */
Gopher.prototype.inboxSubmit = function (mimeType, body, lat, lng, accuracy) {
    this.method = 'POST';
	var options = {
		fileName: this.data.substr(this.data.lastIndexOf('/') + 1),
		mimeType: mimeType,
		params: {Body: body}
	};
	
	if (lat && lng) {
		options.params.Lat = lat;
		options.params.Lng = lng;
		options.params.AccuracyMetres = accuracy;
	}

    this.submitFile(options, true);
}

/**
 * Submits a file to OCA using the FileTransfer function.
 * Called from inboxSubmit for media inbox submissions or from uploadFile for file attachments.
 * @param options ajax options. May include data.
 * @param retry whether the request should be retried on failure.
 */
Gopher.prototype.submitFile = function(options, retry){
    options.headers = {
        'X-Session-ID': OCASession.get('id'),
        'Accept':       'application/json'
    };
    //prevent error on mobile interface
    if (device.platform != "Mobile Interface"){
    	options.headers['User-Agent'] = navigator.userAgent;
    }
    options.chunkedMode = false;
    options.fileKey = 'file';

    var ft = new FileTransfer();
    if (this.onProgress) {
        this.progressMessage = OCA.getI18n().gettext("Uploading file - sent");
        ft.onprogress = $.proxy(this.onProgress, this);
    }

    var failure = $.proxy(this.requestError, this);
    if (retry !== false){
        //set up options for retry if required
        failure = $.proxy(this.retryAJAX, this,
            {
                url:    this.base + this.url,
                data:   this.data,
                options: options,
                method: 'POST'
            }, {
            	url: 	 this.url,
				name:	 options.fileName,
                desc:    'File upload',
                upload:  true,
                timestamp:	 new Date().getTime(),
                pageHash: '#',
				cleanupFiles: [this.data]
            });
    }

    util.log('sending to ', this.base + this.url, options);
	this.activatedRequest();
	ft.upload(this.data, this.base + this.url, $.proxy(this.uploadOK, this), failure, options, true);
	app.checkLoaded();
}

/**
 * Downloads a file from a location specified by this.url to a filename specified by this.data
 * If running Android, this will call the noggin addDownload plugin to actually download the file
 * Otherwise, it will use FileTransfer.download from the PhoneGap framework after checking the cache
 * @param {function} [androidCallback] if present, executed after the download plugin is called
 * @param {string} [mime] if present, the mime type is passed to the download plugin
 */
Gopher.prototype.downloadFile = function(androidCallback, mime){
    var filename = this.data.replace(/ /g, "_");

    var path = fileStore.downloadDir.toURL ? fileStore.downloadDir.toURL() : fileStore.downloadDir.fullPath;
    path += "/" + filename;    

	fileStore.downloadDir.getFile(
		filename, {create: false},
		$.proxy(this.gotDownloadCache, this),
		$.proxy(this.gotDownloadCache, this, false)
	);

}

/**
 * Callback function after checking the cache for the requested file
 * @param fileEntry|false If the file is in the cache, a FileEntry. If not, the boolean false
 */
Gopher.prototype.gotDownloadCache = function(fileEntry){
    var filename = this.data.replace(/ /g, "_");
    
    var path = fileStore.downloadDir.toURL ? fileStore.downloadDir.toURL() : fileStore.downloadDir.fullPath;
    path += "/" + filename;

	if (fileEntry && Gopher.recentDownloads[fileEntry.name]){
//		console.log('file has been downloaded this session. Just return it without fetching.');
		this.downloadOK(fileEntry);
		return;
	}

	var ft = new FileTransfer();
	if (this.onProgress){
		this.progressMessage = OCA.getI18n().gettext("Downloading file - got");
		ft.onprogress = $.proxy(this.onProgress, this);
	}
	var options = this.getFileTransferOptions();
	this.activatedRequest();
	ft.download(this.base + this.url, path, $.proxy(this.downloadOK, this), $.proxy(this.downloadError, this, fileEntry), true, options);
	app.checkLoaded();
}

Gopher.prototype.downloadError = function(fileEntry, xhr, status, error){
	if (fileEntry) {
//		console.log("Error downloading " + fileEntry.name + ". Returning from cache");
		this.downloadOK(fileEntry);
	} else {
//		console.log("Error downloading " + fileEntry.name + ". No cache to return");
		this.requestError(xhr, status, error);
	}
}

Gopher.prototype.downloadMedia = function(onProgress){
    var filename = this.url.split().pop().replace(/\W/g, '_');
    filename = fileStore.cacheDir.toURL() + "/" + filename;

    var ft = new FileTransfer();
    if (onProgress) ft.onprogress = onProgress;

    var options = this.getFileTransferOptions();
    ft.download(this.base + this.url, filename, $.proxy(this.mediaOK, this), $.proxy(this.requestError, this), true, options);
}

Gopher.prototype.mediaOK = function(fileEntry){
    this.callbackOK(fileEntry.toURL());
}

Gopher.prototype.getFileTransferOptions = function(){
	var headers = {
            'X-Session-ID':          OCASession.get('id'),
                'HTTP-X-Session-ID': OCASession.get('id'),
        'Accept':                    'application/json'
        }
    //prevent error on mobile interface
    if (device.platform != "Mobile Interface"){
    	headers['User-Agent'] = navigator.userAgent;
    }
    return {
        headers: headers
    };
}

/**
 * Set the browser location to the specified URL
 * In the mobile interface, this will cause the file to be downloaded because the API sends it as a file
 * In the app, this should not be used
 * In the dev environment, this won't work because it pretends to be the mobile interface,
 * 		but does not have the cookies set on the server
 */
Gopher.prototype.openFile = function(){
	location.href = this.base + this.url; //cookie has been set from the login API call and will authenticate the document opening
}

/**
 * Callback for progress events when uploading or downloading
 * If the app is not in background mode, display a progress message and update it approximately every two seconds
 */
Gopher.prototype.onProgress = function(progress){
	var percent = Math.round(progress.loaded / progress.total * 100);
	var kb = Math.round(progress.loaded / 1024);
	var s = new Date().getSeconds();
	if (this.backgroundMode){
		return;
	}
	if (!this.lastShown || this.lastShown != s || percent === 100){ //update every second, but only once each second
		this.lastShown = s;
		$.mobile.loading('show', {
			theme: 'a',
			text: this.progressMessage + " " + kb + "kB",
			textonly: true,
			textVisible: true
		});
	}
}

/**
 * Internal function used to submit requests which alter data (PUT, POST, DELETE)
 * 
 * If the request fails due to connection problems, it will be queued for retry by default
 * @param {object} ajaxParams parameters to send to the $.ajax function
 * @param {boolean} retry whether the request should be retried if it is unable to be submitted instantly. Defaults to true
 */
Gopher.prototype.sendData = function(ajaxParams, retry){
	if (retry){
		var hash = util.getHash();
		if (hash.indexOf('timestamp') != -1) hash = hash.substr(0, hash.indexOf('timestamp') - 1); //if this is re-editing something in the post cache, remove old timestamp

		var retryData = {
			pageHash: hash,
			url: this.url,
            type: this.typeURL || this.data && this.data.TypeURL,
			name: this.name,
			desc: this.desc,
			timestamp: this.oldTimestamp || new Date().getTime(), //preserve old timestamp if set, otherwise use the current time
			resubmitter: this.resubmitter,
			cleanupFiles: this.cleanupFiles
		};

		ajaxParams.error = $.proxy(this.retryAJAX, this, ajaxParams, retryData);
        
        this.backgroundTimeout = setTimeout($.proxy(this.moveToBackground, this), 10000);   //only move to background if this is a request which may be retried
	}
	ajaxParams.timeout = 120000;

	ajaxParams.beforeSend = function(xhr, settings){
		if (settings.url.indexOf('/session') !== -1) {
			return true; //always allow logins
		} else if (settings.url.indexOf('/pending') !== -1){ //child of pending item. fail so it goes back to the queue
			settings.error(xhr, 'timeout', 'Fake offline status');
			return false;
		}
		if (window.localStorage['offline'] == 1){
			console.log('offline dont send', xhr, settings);
			settings.error(xhr, 'timeout', 'Fake offline status');
			return false;
		}
	}

	this.activatedRequest();
	$.ajax(ajaxParams);
	app.checkLoaded();
};

/**
 * If a request is taking a long time, call the success callback (we're optimists here) and then clear the success callback so it can't be run again
 * The timeout will eventually cause retryAJAX to run and have the item added to the queue, but for now we will just redirect the user so they can go on their 
 * merry way
 */
Gopher.prototype.moveToBackground = function(){
	this.callbackOK();
	this.callbackOK = $.noop;
    Gopher.activeRequests--;
	Gopher.reqLog.push("backgrnd : " + this.method + " - " + this.url);
    this.backgroundMode = true; //so the fail/success callbacks dont interrupt us or decrement the request count again
}

/**
 * Callback function to handle failures from this.sendData()
 * If the failure was due to a connection issue, the data will be added to the GopherQueue for later retry
 * @param {object} ajaxParams the parameters of the AJAX request
 * @param {object} retryData the request metadata
 * @param {xhr} xhr jqXHR OR the fileUpload xhr equivalent
 * @param {string} status text
 * @param {string} error message
 */
Gopher.prototype.retryAJAX = function(ajaxParams, retryData, xhr, status, error){
	if (status == 'timeout' || xhr.status == 0 || xhr.http_status === null){
		GopherQueue.add(ajaxParams, retryData);
		this.unsuccessfulRequest(xhr, status, true);
		app.checkLoaded();
	} else {
		this.requestError(xhr, status, error);
	}
};

/**
 * Start the process of checking whether this request has an existing cache
 */
Gopher.prototype.checkCache = function(){
	if (Gopher.forceUncache) {
		//in case there are a few simultaneous requests, uncache them all by putting a timeout on forceuncache.
		//e.g. contact group list gets the group, the group's groups and the group's contacts
		setTimeout(function() { Gopher.forceUncache = false; }, 1000);
		this.noCache();
	} else if (fileStore && this.mode == "image" && fileStore.documentsDir){
		fileStore.documentsDir.getFile(this.cacheName, {create: false}, $.proxy(this.gotCache, this), $.proxy(this.noCache, this));
	} else if (dbStore.isReady()) {
		var url = this.url;
		dbStore.sql(
			"SELECT id, url, data, cache_expiry, data_expiry FROM responses WHERE URL = ?",
			[url],
			function(tx, results) {
				if (results.rows.length == 0){ //nothing in the queue, which means any old files are unrelated to queue items.
					this.noCache();
				} else {
					var row = results.rows.item(0);
					this.checkJSONCache(row.data, row.cache_expiry);
				}
			}.bind(this),
			this.noCache.bind(this) //error = no cache
		);
//	} else if (dbStore) {
//		$(window).on('databaseReady', $.proxy(this.checkCache, this));
	} else {
		this.noCache();
	}
};

/**
 * File exists, get it.
 */
Gopher.prototype.gotCache = function(fileEntry){
	fileEntry.file($.proxy(this.gotFile, this), $.proxy(this.noCache, this));
};

/**
 * File found, read it
 */
Gopher.prototype.gotFile = function(file){
	this.file = file;
	var reader = new FileReader();
    reader.onerror = $.proxy(this.noCache, this);

    if (this.mode === "data"){
        reader.onloadend = $.proxy(this.gotFileData, this, file);
        reader.readAsDataURL(file);
    } else {
	    reader.onloadend = $.proxy(this.gotFileText, this, file);
        reader.readAsText(file);
    }
};

Gopher.prototype.gotFileData = function(file, event){
//    console.log('gotfiledata', file, event);
    this.callbackOK(event.target.result);
    this.successfulRequest();
}

/**
 * A cached file has been found for this request. 
 * If it can be parsed and represents a cached response, check the expiry time.
 * If it's valid, pass it to the success callback.
 * 
 * If the cache doesn't exist or is expired, call this.noCache() to send a request to the server
 * @param {FileEntry} file cache file entry
 * @param {Event} event onloadend event. Contains the file contents at event.target.result
 */
Gopher.prototype.gotFileText = function(file, event){
	var result = event.target.result;

	if (this.mode !== "json"){
		this.callbackOK(result);
		this.successfulRequest();
		return;
	}
	this.checkJSONCache(result);
};

/**
 * Check whether this data string is a cached JSON response:
 * - if valid and unexpired, return as the success callback
 * - else if valid, keep as the offline fallback and try to fetch from server
 * - else try to fetch from server
 * @param jsonString
 * @param expires string in ISO date format. Present when database storage is used
 */
Gopher.prototype.checkJSONCache = function(jsonString, expires){
	try {
		this.cachedResponse = (jsonString && jsonString.constructor === String) ? JSON.parse(jsonString) : jsonString;
	} catch (err){
		this.cachedResponse = false;
		console.log('Invalid stored JSON for ' + this.url, err);
		console.log(file, jsonString, event);
		log.e(err);
	}

	if (this.cachedResponse && this.cachedResponse.errors.length === 0){
		var now = new Date();
		expires = new Date(expires); //string to Date
		if (now < expires && !Gopher.forceUncache){
			this.successfulRequest();
			var response = this.checkLocalChanges(this.cachedResponse.responsePayloads);
			this.callbackOK(response, this.cachedResponse);
			return;
		}
	}

	//cache expired or otherwise invalid
	this.noCache();
}

/**
 * Submit a GET request if the cache has not been found or is expired
 */
Gopher.prototype.noCache = function(){
//	console.log('fetching '+ this.url + " mode " + this.mode);
    if (this.mode === "image"){
        var req = new XMLHttpRequest();
        req.open("GET", this.url, false);
        req.overrideMimeType("text/plain; charset=x-user-defined");
        req.send(null);

        if (req.status === 200){
            this.gotRequest(req.responseText, req.statusText, req);
        } else {
            this.requestError(req, req.status, req.statusText)
        }
	} else if (this.mode === "data"){
		var req = new XMLHttpRequest();
		req.open("GET", this.url, true);
        req.responseType = 'arraybuffer';

        var self = this;
		var mime = self.mime || "image/jpeg"; //default to image
		req.onload = function(e)
        {
			try {
				var arr = new Uint8Array(req.response);
				var raw = '';
				var i, j, subArray, chunk = 50000;
				for (i = 0, j = arr.length; i < j; i += chunk) {
					subArray = arr.subarray(i, i + chunk);
					raw += String.fromCharCode.apply(null, subArray);
				}
				var b64 = btoa(raw);
				var dataURL="data:" + mime + ";base64," + b64;
				if (req.readyState === 4 && b64.length){
					self.gotRequest(dataURL, req.statusText, req);
				} else {
					self.requestError(req, req.status, req.statusText)
				}
			} catch (e){
				console.log('data uri error', e);
			}
        };
        req.send();
	} else if (this.method == 'HEAD') {
		$.ajax({
				   url:      this.base + this.url,
				   dataType: 'text',
				   success:  $.proxy(this.headOK, this),
				   error:    $.proxy(this.requestError, this),
				   method:   'HEAD'
			   })
	} else if (this.url.indexOf('/pending') === 0){
		//pending urls are fake routes - go straight to gotRequest so any local items can be added
		this.gotRequest(Gopher.emptyResponse, "Ok");
    } else {
		var cache = '';
		if (this.dontCheckCache) {
			if (this.url.indexOf('?') === -1) {
				cache = '?1=1';
			}
			cache += '&' + Date.now() + "=cachebust";
		}
        $.ajax({
            url: this.base + this.url + cache,
            dataType: this.mode,
            success: $.proxy(this.gotRequest, this),
            error: $.proxy(this.requestError, this)
        });
    }
};

/**
 * Success callback after a GET request has been sent
 * Process the response, return it to the Gopher success callback and then save it in the cache.
 * When saving, the expiry header (and data retention header) is processed and added to the record
 * 
 * @param {object} data JSON response data
 * @param {string} status
 * @param {jqXHR|XMLHttpRequest} [xhr]
 */
Gopher.prototype.gotRequest = function(data, status, xhr){
	this.successfulRequest();
	var saveData = data;
	var expiry = new Date();
	var dataExpiry = null;

    if (this.mode === "json"){
		if (xhr && xhr.status) data.status = xhr.status;
		saveData = $.extend({}, data);
        var response = this.checkLocalChanges(data.responsePayloads);
        this.callbackOK(response, data);
        if (!this.noExtras) util.handleResponseExtras(data, this.backgroundMode);

        //store the expiry header with the data for cache invalidation
        try {
            if (xhr) {
            	expiry = new Date(xhr.getResponseHeader('expires')).toISOString();
            	var dataHeader = xhr.getResponseHeader('x-data-retention');
            	if (dataHeader) {
            		dataExpiry = new Date(dataHeader).toISOString();
				}
			}
        } catch (invalidDate){
            log.e(invalidDate);
        }
    } else {
        this.callbackOK(data);
    }
	
	if (this.dontCache) return;
    if (data.errors && data.errors.length) return; //dont cache if it has errors

	this.saveCache(saveData, expiry, dataExpiry);
};

/**
 * Check if there are unsubmitted local changes that should be added to this response
 * For example, an index listing might have an item indicating there are unsubmitted new items which belong to the listing
 */
Gopher.prototype.checkLocalChanges = function(response){
	var local = GopherQueue.has(this.base + this.url)
	if (local){
		//clone item if we are going to muck with it so the changes are not written to the cache
		response = JSON.parse(JSON.stringify(response));

		if ($.isArray(local)){
			for (var l = 0; l < local.length; l++){
				local[l].local = true;
				response.unshift(local[l]);
			}
		} else {
			if (local.message){
				util.infobar(local.message);
				$(document).one('pagebeforechange', util.infobarClear);
			}
			if (local.data){
				$.extend(true, response[0], local.data);
			} 	
		}
	}
	return response;
};

/**
 * Given a timestamp, fetch the corresponding POST request from the offline queue and return the data
 * @param {timestamp} timestamp time of previous request creation
 * @return cached submission
 */
Gopher.prototype.getPOSTCache = function(timestamp){
	var local = GopherQueue.has(this.base + this.url, timestamp);
	return local;
};

/**
 * Failure callback for HTTP requests
 * For GET requests, the cached response will be returned if available
 * For inline GET requests (i.e. pagination), an item of dummy data indicating offline mode will be returned
 * 
 * If dontProcessError is true, all arguments to this function will be passed to the failure callback
 * 
 * Failing these conditions, attempt to parse the response. If valid, handle the response (display errors, save extra payloads, etc). 
 * Execute the Gopher failure callback, passing the error message and the response (if parsed)
 * 
 * If this was a GET request and there is no cache to fall back upon, change to the page which shows the offline error message
 */
Gopher.prototype.requestError = function(xhr, status, error){
//    util.log('request error', this.method, this.url, this.base, this.data && JSON.stringify(this.data).length > 10000 ? 'large data' : this.data, arguments);
	this.unsuccessfulRequest(xhr, status);
	app.checkLoaded();

    if (xhr.status === 401) util.log(401 + ": session - " + OCASession.getSessionId());

	if (xhr.status === 401 && this.method === "GET" && (this.url === "/policies" || this.url === "/me/access")){ //not authorised when loading page
		OCASession.kill();
		Session.refresh();
		return;
	}
	
	if (this.method == 'GET' && !this.dontCache && this.cachedResponse && xhr.status !== 404 && xhr.status !== 401){ //404 probably means object was deleted. dont return cache! //401 means bad login
		var response = this.checkLocalChanges(this.cachedResponse.responsePayloads);
		this.cachedResponse.expired = true;
		this.callbackOK(response, this.cachedResponse);
		return;
	}

	if (this.method == 'GET' && this.dontCheckCache && !this.backgroundMode && (xhr.status == 0 || status == "timeout")){ //device is offline but was told not to check the cache. Probably pull-to-refresh or some other forced update.
		util.infobar("Unable to refresh data", null, 5);
		this.callbackFail(xhr, status, error);
		return;
	}
	
	if (this.method == 'GET' && this.offlineError && this.offlineError == 'inline' && (xhr.status == 0 || status == "timeout")){
		var data = {"errors": [], "notices": [], "responsePayloads": [], "extraPayloads": [], "nextPageURL": null, "prevPageURL": null};
		data.responsePayloads.push({
			local:		false, //is from local, but should appear in the main listview
			offline:	true,
			Name:		OCA.getI18n().gettext("Offline mode - can't get data"),
			URL:		'#'
		});
		var response = this.checkLocalChanges(data.responsePayloads); //add any pending items from the cache
		this.callbackOK(response, data);
		return;
	}
	
	if (this.dontProcessError){
		this.callbackFail(xhr, status, error);
		return;
	}
	
	try {
		var response = JSON.parse(xhr.responseText);
		if (!this.noExtras) util.handleResponseExtras(response, this.backgroundMode);
		this.callbackFail(error, response);
	} catch (e){
		if (xhr && !error) error = xhr;
		this.callbackFail(error); //response might not be parseable
	}
	
	if (this.method == 'GET' && !this.backgroundMode && (xhr.status == 0 || status == "timeout")){
		console.log("ATTEMPTING OFFLINE MODE " + this.url);
		console.log(JSON.stringify(arguments));
		if (Gopher.offlineTimer) clearTimeout(Gopher.offlineTimer);
		Gopher.offlineTimer = setTimeout(function(){
            $( "body" ).pagecontainer( "change", $('#offline'));
		}, 1000 * Gopher.activeRequests);
	}
};

/**
 * Success callback after a PUT request. Handle the request and call the Gopher success callback
 * Set the cache for the equivalent GET request and for the parent listing GET request to be expired, as the data has changed for this child item
 */
Gopher.prototype.putOK = function(data, status, xhr){
	if (xhr && xhr.status) data.status = xhr.status;
	this.successfulRequest();
	this.callbackOK(data.responsePayloads ? data.responsePayloads : data);
    this.uncache();
	this.recache(); //recache after the data is returned because it removes the callbacks
	if (!this.noExtras) util.handleResponseExtras(data, this.backgroundMode);
	
	//make the bold assumption that if we are putting to /type/ID then we should uncache /types
	var parent = this.url.substr(1, this.url.indexOf("/",1)-1)+"s";
	this.uncache(parent);
	if (this.cleanupFiles){
		console.log('gopher put clearfiles');
		fileStore.clearFiles(this.cleanupFiles);
	}
};

/**
 * Success callback after a POST request. Handle the request and call the Gopher success callback
 * Clear the GET request caches which correspond to this POST URL, since the data has now changed
 * @callback {array} response payloads from the API request
 * @callback {string} Location response header. When the POST creates a new object, this will be the URL that identifies it
 */
Gopher.prototype.postOK = function(data, status, xhr){
	if (xhr && xhr.status) data.status = xhr.status;
	this.successfulRequest();
	this.uncache();
	this.callbackOK(data.responsePayloads ? data.responsePayloads : data, data, xhr.getResponseHeader('Location'));
	if (!this.noExtras) util.handleResponseExtras(data, this.backgroundMode);
    Gopher.forceUncache = true;
	if (this.cleanupFiles){
		console.log('gopher post clearfiles');
		fileStore.clearFiles(this.cleanupFiles);
	}
	if (this.oldTimestamp){ //this was probably a fix for an object with validation errors. Make sure it's added to the created cache in case it had children.
		GopherQueue.createdCache['/pending/' + this.oldTimestamp] = xhr.getResponseHeader('Location');
	}
};

/**
 * Success callback after a DELETE request. Handle the request and call the Gopher success callback
 * Set the cache of the parent listing as expired
 */
Gopher.prototype.deleteOK = function(data, status, xhr){
	if (xhr && xhr.status) data.status = xhr.status;
	this.successfulRequest();
	this.uncache();
	this.callbackOK(data.responsePayloads ? data.responsePayloads : data, xhr.getResponseHeader('Location'), data);
	if (!this.noExtras) util.handleResponseExtras(data, this.backgroundMode);
	//make the bold assumption that if we are putting to /type/ID then we should uncache /types
	var parent = this.url.substr(1, this.url.indexOf("/",1))+"s";
	this.uncache(parent);
	Gopher.forceUncache = true; //dont know which parent this deleted object belonged to, but theres a good chance the next thing it tries to display will be the parent tree/index. force gopher to fetch the next request again
}

/**
 * Success callback after file upload request
 */
Gopher.prototype.uploadOK = function(r){
	this.successfulRequest();
	var data = r.response ? JSON.parse(r.response) : r;
	if (r && r.status) data.status = r.status;
	this.callbackOK(data.responsePayloads ? data.responsePayloads : data);
	if (!this.noExtras) util.handleResponseExtras(data, this.backgroundMode);
};

/**
 * Success callback after file download request
 */
Gopher.prototype.downloadOK = function(fileEntry){
	this.successfulRequest();
//	console.log('downloadOK ' + fileEntry.name);
	$.mobile.loading('hide');
	this.callbackOK(fileEntry);
	Gopher.recentDownloads[fileEntry.name] = true;
}

/**
 * Mark any cached response for this item as out-of-date
 * @param url - specify an URL to uncache, otherwise assume its the URL of the current item
 */
Gopher.prototype.uncache = function(url){
	url = url || this.url

	if (dbStore.isReady()) {
		var url = this.url;
		dbStore.sql(
			"UPDATE responses SET cache_expiry = ? WHERE url LIKE ?", //use like to catch querystring searches
			[new Date().toISOString(), '%' + url + '%'],
			function(tx, result) {
//				console.log('set ' + url + ' to be expired');
			});
	} //if the DB doesnt exist, this is probably a startup/login task that doesn't need invalidation
};

/**
 * 'recache' something by sending the GET request again. 
 * Overwrites the callbacks since this request doesn't have to do anything except save.
 */
Gopher.prototype.recache = function(){
	if (this.dontCache) return;
	
	this.callbackOK   = function(){} //reGOT since the data has been updated
	this.callbackFail = function(){} //TODO remove cache if this failed? e.g.
	this.noCache();
}

/**
 * Save data to the cache
 */
Gopher.prototype.saveCache = function(data, cacheExpiry, dataExpiry){
    if (this.mode == 'image'){
        if (!fileStore.documentsDir) return;
        fileStore.documentsDir.getFile(this.cacheName, {create: true}, $.proxy(this.gotSaveCache, this, data), log.e);
    }
    if (dbStore.isReady()) {
    	dbStore.nextPurge(dataExpiry);
		dbStore.sql(
			"INSERT OR REPLACE INTO responses (id, url, data, cache_expiry, data_expiry) VALUES ((SELECT id FROM responses WHERE URL = ?),?,?,?,?)",
			[this.url, this.url, JSON.stringify(data), cacheExpiry, dataExpiry],
			function(tx, result) {
				if (result.insertId) {
					data.ID = result.insertId;
				}
			});
	} else {
    	$(window).on('databaseReady', $.proxy(this.saveCache, this, data, cacheExpiry, dataExpiry));
	}
};

/**
 * Internal callback - create file writer to save data to the cache
 */
Gopher.prototype.gotSaveCache = function(data, entry){ //data param passed via $.proxy
	entry.createWriter($.proxy(this.writeSaveCache, this, data), log.e);
};

/**
 * Internal callback - write data to a file in the cache
 */
Gopher.prototype.writeSaveCache = function(data, writer){
    var type = 'text';
	if (this.mode === "json"){
		try {
			data = JSON.stringify(data);
			type = 'text/json'
		} catch (e){ //can't stringify circular data - usually indicates that the app is editing the response directly instead of taking a copy
			console.error(e);
			console.error(data);
			console.error(this.url, this);
			return;
		}
    }
	writer.onwriteend = function(){
		writer.onwriteend = function(){};
		if (util.isEmulator()){ //emulator mode, data must be a blob
			data = new Blob([data], {type: type});
		}
		writer.write(data);
	};
	writer.truncate(0);
};