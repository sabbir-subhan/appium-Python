router.add({
	"#storage": function(type, match, ui, page, e){
		storage.getIncoming();
		storage.getQueue();
	}
});
$(document).on("pageinit", "#storage", function(e){ 
	storage.init($(this));
});
var storage = $.extend({}, app, {
	init: function(page){
		this.page = page;
		this.content = page.find('.ui-content');
		this.listview = this.content.find('.ui-listview.outgoing');
		this.footer = page.find('.ui-footer');
		this.footer.find('#storageFlush').click(function(){
			util.infobar("Retrying offline sync", null, 10);
			GopherQueue.flush();
			util.goBack();
		});
		this.footer.find('#storageWipe').click(function(){
			GopherQueue.wipe();
			storage.getQueue();
		});
	},
	getQueue: function(){
		if (this.listview){
			GopherQueue.get($.proxy(this.gotQueue, this), log.e);
		} else {
			//console.log('cant update storage page');
		}
	},
	gotQueue: function(queue){
		this.listview.empty();
		if (queue.length == 0) {
			this.content.find('.status').text('There are no items awaiting submission');
		} else {
            this.content.find('.status').text('The following items were changed whilst offline and have not been sent to OCA');
			for (var q=0; q < queue.length; q++){
				var item = queue[q];
				var label = item.info.name || item.info.desc;
                var $li = $('<li><h5>' + label + '</h5><p>' + ViewUtil.relativeDate(new Date(parseInt(item.info.timestamp,10))) + '</p></li>');
                var route = this.getRoute(item.info.pageHash);
                $li.wrapInner("<a href='" + route + "' class='resumeQueue' />");

                if (item.info.invalid){
                    $li.attr('data-theme', 'e');
                    var $a = $li.find('a.resumeQueue');
                    $a.append('<h5>' + OCA.getI18n().gettext('Validation errors') + ':</h5>');
                    for (var e = 0; e < item.info.errors.length; e++) $a.append("<p class='desc'>- " + item.info.errors[e] + '</p>');

                    if (item.info.locked){
                        this.addLockedOptions(item, $a);
                    }
                } else {
                    $li.append($("<a />").prop('href', '#').data('queueItem', item).click($.proxy(this.deleteItem, this)));
                }
                this.listview.append($li);
				item.info.currentlyEditing = false; //if a user cancels an edit and goes back to this page, they are no longer editing
			}
		}
		this.listview.listview('refresh');
        this.listview.enhanceWithin();
		app.checkLoaded();
	},
	deleteItem: function(e){
		var item = $(e.currentTarget).data('queueItem');
		GopherQueue.remove(item.ajax.method, item.ajax.url, item.info.timestamp);
		this.getQueue();
	},
	scanCache: function(){
		var reader = fileStore.cacheDir.createReader();
		reader.readEntries($.proxy(this.writeCache, this), log.e);
	},
	writeCache: function(entries){
		this.listview.empty().data('split-icon', 'delete');
		for (var i=0; i < entries.length; i++){
			var entry = entries[i];
			if (entry.isFile){
				var row = $("<li />");
				row.append("<h5>"+ entry.name+ "</h5>");
//				entry.file(function(file){
//					row .append("<p class='ul-li-desc'>"+ file.fullPath+ "</p>")
//						.append("<p>Date: "+ file.lastModifiedDate+ "</p>")
//						.append("<p>Type: "+ file.type+ "</p>")
//						.append("<p>Size: "+ file.size+ "</p>")
//						.append("<a href='#'>Del</a>")
//						.append("<a href='#'>Two</a>")
//				}, log.e);
				this.listview.append(row);
			}
		}
		this.listview.listview('refresh');
	},
    addLockedOptions: function(queueItem, $a){
        if (!queueItem || !$a) return;

        //options: if editing report and the status code was locked, give the user options to save as a new report or discard
        var bits = queueItem.info.url.split('/');
        if (bits.length == 3 && bits[1] == 'report'){ //TODO if/when more object types are supported, refactor this
            var save = $("<a href='#' data-role='button' data-inline='true' class='add' data-theme='b'>" + OCA.getI18n().gettext('Save as new report') + "</a>");
            save.click($.proxy(this.newReport, this, queueItem));
            $a.append(save);
            var discard = $("<a href='#' data-role='button' data-inline='true' class='add' data-theme='b'>" + OCA.getI18n().gettext('Discard') + "</a>");
            discard.data('queueItem', queueItem);
            discard.click($.proxy(this.deleteItem, this));
            $a.append(discard);
        }
    },
    newReport: function(queueItem){
        var data = JSON.parse(queueItem.ajax.data);
        data.TypeURL = queueItem.info.type;
        new Gopher({url: '/reports', data: data}, function(){
            util.infobar(OCA.getI18n().gettext('Report saved successfully'));
            GopherQueue.remove(queueItem.ajax.method, queueItem.ajax.url, queueItem.info.timestamp);
            storage.getQueue(); //update storage page
        }, function(){
            console.log('not saved as new report !', queueItem, arguments);
        }).post(false);
    },
	getIncoming: function(){
		var incoming = OCA.getTypeQueue();

		var $lv = this.content.find('.ui-listview.incoming').empty();
		if (incoming.length == 0) {
			this.content.find('.incoming').hide();
		} else {
			this.content.find('.incoming').show();
			this.content.find('.status-incoming').text('Fetching type data:');
			for (var i=0; i < incoming.length; i++){
				$lv.append('<li>' + incoming[i] + '</li>');
			}
		}
		$lv.listview('refresh');
		$lv.enhanceWithin();
		app.checkLoaded();
	},
	updateBadge: function(count) {
		count = count || OCA.getTypeQueue().length + GopherQueue.get().length;
		$("a[href='#storage'] .badge").text(count).showIf(count);
	},
	/**
	 * Convert an item.info.pageHash into the correct route for viewing the pending item
	 * eme, asse
 	 * @param pageHash
	 * @returns string
	 */
	getRoute: function(pageHash){
		var type = pageHash.split('?')[0].replace('#', '').replace('New', '').replace('Edit', '');
		if (['eme', 'asset', 'contactgroup'].indexOf(type) !== -1) {
			type += 'Tree'; 									//show pending trees for hierarchical types.
			pageHash = pageHash.replace('Edit?', 'TreeView?'); 	//if edit, link to object tree
		} else {
			pageHash = pageHash.replace('Edit?', 'View?'); 		//or just to normal view
		}

		var route = pageHash.replace("New?", "Pending?");
		route     = route.replace('pending=true&', '');
		route     = route.replace(/type=\d+&/, '');
		route     = '#' + ViewUtil.getRoute(type, route);

		return route;
	}
});