router.add({
	"#filesystemTreeView$": function(type, match, ui, page, e){
		FileApp.index();
	},
	"#filesystemTreeView[?]selector=true&id=(\\d+)": function(type, match, ui, page, e){
		if (parseInt(match[1], 10)){
			FileApp.view(match[1]);
		} else {
			FileApp.index();
		}
	},
	'#filesystemMediaSelect': function(){
		app.checkLoaded();
	}
});

$(document).on("pageinit", "#filesystemTreeView", function(e){ 
	FileApp.init($(this));
});
$(document).on("pageinit", "#filesystemMediaSelect", function(e){ 
	FileApp.initMedia($(this));
});
var FileApp = $.extend({}, app, {
	pathCache: ['root'],
	init: function(page){
		this.page = page;
		this.content = this.page.find('.ui-content');
		this.footer = this.page.find('.ui-footer');
		app.init.call(this);
		this.fListview = this.content.find("ul.folders.listview");
		this.dListview = this.content.find("ul.documents.listview");
	},
	initMedia: function($page){
		$page.find('#filePhotoGallery').on('click', $.proxy(this.selectMedia, this, 'photo', false));
		$page.find('#fileVideoGallery').on('click', $.proxy(this.selectMedia, this, 'video', false));
		$page.find('#filePhotoCapture').on('click', $.proxy(this.selectMedia, this, 'photo', true));
		$page.find('#fileVideoCapture').on('click', $.proxy(this.recordVideo, this));
		$page.find('#fileAudioCapture').on('click', $.proxy(this.recordAudio, this));
	},
	selectMedia: function(type, capture){
		var cam = navigator.camera;
		var options = {
			quality: 50,
			sourceType: capture 
				? cam.PictureSourceType.CAMERA
				: cam.PictureSourceType.SAVEDPHOTOALBUM,
			destinationType: cam.DestinationType.FILE_URI,
			saveToPhotoAlbum: capture
		}
		if (type == 'video'){
			options.mediaType = cam.MediaType.VIDEO;
		} else {
			options.mediaType = cam.MediaType.PICTURE;
			options.encodingType = cam.EncodingType.JPEG;
			options.correctOrientation = true;
		}
		Session.preserveDB = true;
		cam.getPicture($.proxy(this.gotMedia, this, type, type == 'video' ? 'video/mpeg' : 'image/jpeg'), log.e, options);
		// returns something like
		// content://media/external/video/media/32
	},
	recordVideo: function(){
		var mime = 'video/mpeg'; //default guess
		if (device.platform == 'iOS') mime = 'video/quicktime'; //iOS = .mov
		Session.preserveDB = true;
		navigator.device.capture.captureVideo($.proxy(this.recordedMedia, this, mime), log.e);
	},
	recordAudio: function(){
		var mime = 'audio/mpeg'; //default guess
		if (device.platform == 'iOS') mime = 'audio/wav'; //iOS = .wav files
		Session.preserveDB = true;
		navigator.device.capture.captureAudio($.proxy(this.recordedMedia, this, mime), log.e);
	},
	recordedMedia: function(mime, mediaFiles){
		var file = mediaFiles.shift();
		if (file){
			if (file.type) mime = file.type;
			this.gotMedia('', mime, file.fullPath);
		}
	},
	gotMedia: function(prefix, mime, url){
		//android - (file://)?/storage/emulated/android.../com.noggin.oca/cache/12312312.jpg
		//ios - file://varmobile.... Application/uuids--asd-asda-sasd/tmp/cdv_photo_...

		if (url.indexOf('content://') != -1) {
			window.FilePath.resolveNativePath(url, function(filePath){
				if (filePath.indexOf('file://') === -1){
					filePath = 'file://' + filePath;
				}
				FileApp.gotMedia(prefix, mime, filePath);
			}, function(){
				util.alertDialog("Unable to load file", $.noop, T("Error"));
				util.goBack();
			});
		} else if (this.mediaSelectCallback){
			if (url.substr(0,13) == 'file:/storage') url = url.replace('file:/storage', 'file:///storage'); //fix stupid Android bug
			if (url.substr(0,7) !== 'file://') url = 'file://' + url;

			//copy the returned media to a directory the system won't clear so we have full control.
			window.resolveLocalFileSystemURL(url, function(fileEntry){
				if (fileStore.downloadDir) {
					//put timestamp in the copied file's name to guarantee no collisions.
					var filename = url.split("/").pop();
					var newName  = Date.now() + '__file__' + filename;
					fileEntry.copyTo(fileStore.downloadDir, newName, function(copiedFile){ //copy rather than move so that iOS keeps incrementing the filename
						FileApp.gotMediaCopy(prefix, mime, copiedFile.toURL(), filename);
					}, function(error){
						log.e(error);
						FileApp.gotMediaCopy(prefix, mime, url);
					});
				} else { //no download dir to copy , just do the selection callback
					FileApp.gotMediaCopy(prefix, mime, url);
				}
			}, function(error){
				log.e(error);
				FileApp.gotMediaCopy(prefix, mime, url);
			})
		}
	},
	gotMediaCopy: function(prefix, mime, url, filename){
		filename = filename || url.split("/").pop();
		if (filename.indexOf(prefix) !== -1) prefix = ''; //dont do photo_cdv_photo
		var name = prefix + filename;
		this.mediaSelectCallback(url, name, mime);
		this.mediaSelectCallback = null;
		util.goBack();
	},
	index: function(){
		fileStore.getFiles($.proxy(this.gotFiles, this));
	},
	view: function(id){
		var path = this.pathCache[id];
		resolveLocalFileSystemURL(path, $.proxy(this.gotEntry, this));
	},
	gotEntry: function(entry){
		fileStore.getFiles($.proxy(this.gotFiles, this), entry);
	},
	gotFiles: function(entries){
		this.fListview.empty();
		this.dListview.empty();
		var folders = [];
		var docs = [];
		for (var e = 0; e < entries.length; e++){
			var entry = entries[e];
			if (entry.name[0] == '.') continue; //convention is that these files should be hidden
			var id = this.pathCache.length;
			this.pathCache.push(entry.fullPath);
			if (util.isEmulator()){
				entryCache[entry.fullPath] = entry;
			}
			if (entry.isDirectory){
				folders.push({
					Name: entry.name,
					URL: 'pretendURL/'+id
				});
			} else {
				docs.push({
					Name: entry.name,
					URL: 'pretendURL/'+id
				});
			}
		}
		ViewUtil.populateLV(this.fListview, folders, 'filesystemTree', 'folder', {unselectable: true, parent: true});
		ViewUtil.populateLV(this.dListview, docs, 'file', 'file', true);
		this.checkLoaded();
	}
});
if (util.isEmulator()){
	var entryCache = {};
	window.resolveLocalFileSystemURL = function(path, callback){
		callback(entryCache[path]);
	}
}