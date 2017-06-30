router.add(
	{
		"#documentfolderTreeView[?]id=0&query=(.*)":       function(type, match) {
			DocumentController.indexFilters.search = match[1];
			DocumentController.renderListing();
		},
		"#documentfolderTreeView[?]selector=true&id=(.+)": function(type, match, ui, page, e) {
			DocumentController.renderListing(match[1], true);
		},
		"#documentView[?]id=(\\d+)":                       function(type, match, ui, page, e) {
			DocumentController.view(match[1]);
		},
		"#documentfolderTreeView[?]id=(.+)$":              function(type, match, ui, page, e) {
			DocumentController.indexFilters.search = '';
			DocumentController.content.find('#docSearch').val(''); //reset search when browsing tree
			DocumentController.renderListing(match[1], false);
		}
	});

$(document).on("pageinit", "#documentfolderTreeView", function(e){ 
	DocumentController.init($(this));
});
var DocumentController = $.extend({}, app, {
	returnedLists: 0, //counter to detemine if the list of folders AND the list of files has returned
	init: function(page){
		this.indexFilters = {
			search: null
		};
		this.page = page;
		this.content = this.page.find('.ui-content');
		this.footer = this.page.find('.ui-footer');
		app.init.call(this);
		this.$mainLV = this.content.find("ul.folders.listview");
		this.$secondLV = this.content.find("ul.documents.listview");
		this.content.find('#docSearch').keypress(function(e){
			if (e.which == 13){
				DocumentController.indexFilters.search = $(this).val();
				DocumentController.renderListing(0, DocumentController.selectorMode);
			}
		}).on('change', function(e){
			if ($(this).val() == ''){
				DocumentController.indexFilters.search = $(this).val();
				DocumentController.renderListing(0, DocumentController.selectorMode);
			}
		});

		OCA.name('/documentfolder/0', 'Documents'); //special name for document root
	},
	renderListing: function(id, selectorMode){
		if (!id) {
			id = 0;
		}
		this.setCurrentItem('documentfolder', id);

		this.selectorMode = selectorMode || false;
		this.page.find('.selector-mode').visibleIf(this.selectorMode);
		this.content.find('div.heading-row a.level-up').visibleIf(id != 0);
		this.returnedLists = 0;

		var heading, foldersURL, documentsURL, showDocuments = true;
		var query = this.getListingQuery();

		if ($.isEmptyObject(query)) {	//normal tree browsing mode
			heading      = this.currentItem.Name;
			foldersURL   = this.currentItem.URL + '/documentfolders';
			documentsURL = this.currentItem.URL + '/documents';
			if (isNaN(id) || id == 0){ //only 'real' folders with a normal (numeric) ID can have child documents
				showDocuments = false;
			}
		} else {						//search mode
			heading      = 'Document search';
			foldersURL   = '/documentfolders?' + $.param(query);
			documentsURL = '/documents?' + $.param(query);
		}

		var selectProps = {
			unselectable: true,	//you dont choose a document folder
			parent:       true	//but you might navigate into it to find documents
		};
		this.getListing(foldersURL, heading, $.proxy(this.gotDocumentFolders, this), {
			type:         'documentfolderTree',
			selectorMode: this.selectorMode ? selectProps : false,
			noItemsMsg: false	//need to consider both listviews together - handled in checkLoaded
		});

		if (showDocuments){
			this.getSecondaryListing(documentsURL, $.proxy(this.gotDocuments, this), {
				type:         'document',
				icon:         'file',
				selectorMode: this.selectorMode,
				noItemsMsg: false
			});
		} else {
			this.returnedLists = 1; //pretend we already have 1 list because documents arent being fetched
			this.$secondLV.empty();
		}
	},
	gotDocumentFolders: function(data, extra){
		this.returnedLists++;
		this.checkLoaded();
	},
	gotDocuments: function(data, extra){
		this.returnedLists++;
		this.checkLoaded();
	},
	checkLoaded: function(){
		app.checkLoaded();
		if (this.returnedLists == 2 && this.$secondLV.children().length === 0 && this.$mainLV.children().length === 0) {
			this.$mainLV.append($("<li />").data('theme','e').text(OCA.getI18n().gettext('There are no items to display'))).listview('refresh');
		}
	},
	view: function(id){
		var url = '/document/' + id;
		new Gopher(url, $.proxy(this.gotHeaders, this, url), $.proxy(this.documentError, this)).head();
	},
	documentError: function(){
		util.infobar('Unable to load document', null, 10);
		util.goBack();
	},
	gotHeaders: function(url, headers){
		console.log('got headers');
		console.log(JSON.stringify(headers));
		var filename = this.getFilename(headers['Content-Disposition'] || headers['content-disposition']);
		this.downloadFile(url, filename, headers['Content-Type']);
	},
	getFilename: function(disposition){
		return disposition.split("filename=").pop().replace('"', '').replace('"', ''); //should have begining and trailing quotation marks
	},
	downloadFile: function(url, filename, mime, androidCallback, dontGoBack){

		androidCallback = androidCallback || function(){
			console.log('success callback from download for android');
			if (!dontGoBack) util.goBack();
		};
		if (device.platform != "Mobile Interface"){
			if (device.platform != "Android") $.mobile.loading('show');  //android uses system downloads, has a separate progress indication.

			new Gopher({url: url, data: filename}, function(fileEntry){
				DocumentController.displayFile(fileEntry, filename, dontGoBack);
			}, $.proxy(this.documentError, this)).downloadFile(androidCallback, mime);
		} else {
			//goback causes openfile to fail on mobile browser interface.. adding delay and running openFile after goback() seems to fix.
			setTimeout(function(){
				new Gopher(url).openFile();
			},100);

			if (!dontGoBack){util.goBack();} //back to file list
			
		}
	},
	displayFile: function(fileEntry, filename, dontGoBack){
		this.checkLoaded();
		console.log('displaying file ' + filename);
		console.log(JSON.stringify(arguments));
		var target = '_blank';
		if (window.device.platform == "Win32NT"){
			target = '_launcher';
		} else if (window.device.platform == "Android"){
			target = '_system';
		}
		setTimeout(function(){
			var ref = window.open(fileEntry.toURL(), target, 'location=no,EnableViewPortScale=yes');
			ref.addEventListener('loadstart', 	function(){console.log("LOADSTART")});
			ref.addEventListener('loadstop',  	function(){console.log("LOADSTOP") });
			ref.addEventListener('loadexit',  	function(){console.log("LOADEXIT") });
			ref.addEventListener('loaderror', 	$.proxy(this.documentError, this));
		},100);
		if (!dontGoBack) util.goBack();
	}
});