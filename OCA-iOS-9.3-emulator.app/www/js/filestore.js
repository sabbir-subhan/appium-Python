/**
 * The fileStore object handles access to the device's file system.
 * 
 * It sets up the cache and download directories, as well as providing methods to clear the cache.
 */
var fileStore = {
	fileSystem: null,
	cacheDir: null,
	downloadDir: null,

	/**
	 * Initialise the file store:
	 * - request access to the local file system
	 * - create or find the cache directory
	 * - create or find the Downloads directory
	 */
	init: function(){
		if (!cordova.file) { //wp8 patch
			cordova.file = {
				cacheDirectory: '.cache',
				dataDirectory: 'Downloads'
			};
		}
//		console.log('init filestore');
		if (util.isEmulator() && window.webkitStorageInfo){		//emulator mode
//            console.log('emulator wsi');
			if (window.webkitFileReader) FileReader = window.webkitFileReader;	//dont use cordova file reader when we are in the emulator because Ripple doesnt fully implement it
			window.webkitStorageInfo.requestQuota(LocalFileSystem.PERSISTENT, 100*1024*1024, function(grantedBytes){
				window.webkitRequestFileSystem(LocalFileSystem.PERSISTENT, grantedBytes, function(fs){
//					console.log('got file system');
					fileStore.fileSystem = fs;
					fileStore.fileSystem.root.getDirectory(".cache", {create:true},  function(dir){
//						console.log('got cache dir');
						fileStore.cacheDir = dir
						$(window).trigger('cacheReady');
					}, log.e);
					fileStore.fileSystem.root.getDirectory("Downloads", {create:true},  function(dir){
//						console.log('got download dir');
						fileStore.downloadDir = dir
					}, log.e);
				}, log.e);
			}, log.e);
		} else if (window.requestFileSystem) {
//            console.log('window request file system');
			var grantedBytes = 1024 * 1024;
			grantedBytes = 0;
			window.requestFileSystem(LocalFileSystem.PERSISTENT, grantedBytes, function(fs){
				console.log('got file system');
				fileStore.fileSystem = fs;
				if (device.platform === "windows" && window.resolveLocalFileSystemURI) window.resolveLocalFileSystemURL = window.resolveLocalFileSystemURI; //despite ..URI telling you to use ..URL, URI is the one that actually works.
                window.resolveLocalFileSystemURL(cordova.file.cacheDirectory, function(dir){
                    console.log('got cache dir');
                    fileStore.cacheDir = dir
                    $(window).trigger('cacheReady');
                }, function(){ //fallback if resolveLocalFileSystemURL doesnt work
					fs.root.getDirectory('.cache', {create: true}, function(dir){
						console.log('got cache dir 2');
						fileStore.cacheDir = dir
						$(window).trigger('cacheReady');
					}, log.e)
				});
                if (device.platform === "Android" && cordova.file.externalDataDirectory){
                    window.resolveLocalFileSystemURL(cordova.file.externalDataDirectory,  function(dir){
                        console.log('got external download dir');
                        fileStore.downloadDir = dir
                    }, log.e);
                } else {
                    window.resolveLocalFileSystemURL(cordova.file.dataDirectory,  function(dir){
                        console.log('got download dir');
                        fileStore.downloadDir = dir
                    }, function(){ //fallback if resolveLocalFileSystemURL doesnt work
						fs.root.getDirectory('Downloads', {create: true}, function(dir){
							console.log('got download dir 2');
							fileStore.downloadDir = dir
						}, log.e)
					});
                }
			}, function(code){
//				console.log("No file system " + code + code.code)
			});
		} else {
//            console.log('no file system!?');
        }
		setTimeout(function(){
			// sometimes after a logout and reload, the filestore doesn't init properly.
			// just in case, wait 5 seconds and check it was set up
			if (!fileStore.fileSystem || !fileStore.downloadDir || !fileStore.cacheDir){
				console.log("5 second reboot of filestore");
				fileStore.init();
			}
		}, 5000);
	},
    canCache: function(){
        if ((util.isEmulator() && window.webkitStorageInfo) || window.requestFileSystem){
            return true;
        }
        return false;
    },
	/**
	 * List all files in a directory
	 * @param {function} callback function passed the list of files on success
	 * @param {DirectoryEntry} [directory] Files will be listed from this directory. If null, defaults to the file system root.
	 */
	getFiles: function(callback, directory){
		directory = directory || this.fileSystem.root;
		var reader = directory.createReader();
		reader.readEntries(callback, log.e);
	},
	/**
	 * Saves data to a filename within the cache directory. It must first get the file entry and then pass that to this.gotSaveFile()
	 * @param {string} filename name of file entry to retrieve
	 * @param {string} data data to be saved. Passed to gotSaveFile
	 * @param {function} callbackOK function called if the file is saved successfully. Passed to gotSaveFile
	 */
	saveFile: function(filename, data, callbackOK){
		fileStore.cacheDir.getFile(filename, {create: true}, $.proxy(this.gotSaveFile, this, data, callbackOK), log.e);
	},
	/**
	 * Writes data to a file entry. 
	 * This function is called from this.saveFile() and calls this.writeFile() if the file entry can be turned into a file writer
	 * @param {string} data to be written to the file entry
	 * @param {function} callbackOK function called if the data is written successfully
	 * @param {FileEntry} file file entry which creates the writer which is passed to writeFile
	 */	
	gotSaveFile: function(data, callbackOK, file){
		file.createWriter($.proxy(this.writeFile, this, data, file, callbackOK), log.e);
	},
	/**
	 * Writes data using a file writer
	 * This function is called from this.gotSaveFile()
	 * The data is converted to a Blob when run in a web browser.
	 * 
	 * @param {string} data to be written 
	 * @param {FileEntry} file to be saved
	 * @param {function} callbackOK function called with the full path of the file if the write completes successfully
	 * @param {File} writer object to write to a file
	 */
	writeFile: function(data, file, callbackOK, writer){
		writer.onwriteend = function(){		//after truncate
			writer.onwriteend = function(){	//after write
				callbackOK(file.fullPath);
			}
			if (util.isEmulator()){ //emulator mode, data must be a blob
				data = new Blob([data], {});
			}
			writer.write(data);
		}
		writer.truncate(0);
	},
	/**
	 * Function to clear the cache files. 
	 * Called with no paramters to completely remove all files on login/logout.
	 * Called otherwise to expire multiple files at once - e.g. after a new log has been created and log caches for all the filters must be expired
	 * 
	 * @param {string} [match] string to match file names against. If present, only those files which match this parameter will be cleared
	 * @param {boolean} [shallowDelete] If true, cache files will be marked as expired instead of deleted. Defaults to false.
	 */
	clearCache: function(match, shallowDelete){
		if (!fileStore.cacheDir) return;
		
		var reader = fileStore.cacheDir.createReader();
		reader.readEntries($.proxy(this.clearCacheEntries, this, match, shallowDelete));
	},
    rebootCache: function(deferred){
        if (!fileStore.cacheDir) {
			if (deferred) { deferred.resolve(); }
			return;
		}

        fileStore.cacheDir.removeRecursively(function(){
            fileStore.init();
			if (deferred) { deferred.resolve(); }
        }, function(e){
        	console.error(e)
			if (deferred) { deferred.resolve(); }
		});
    },
	/**
	 * Processing callback of this.clearCache(). For each file, handle delete/expiry/ignoring as per the parameters.
	 * 
	 * @param {string} [match] string to match file names against. If present, only those files which match this parameter will be cleared
	 * @param {boolean} [shallowDelete] If true, cache files will be marked as expired instead of deleted. Defaults to false.
	 * @param {array} cache Array of FileEntry objects representing files in the cache
	 */
	clearCacheEntries: function(match, shallowDelete, cache){
		for (var i = 0; i < cache.length; i++){
			var entry = cache[i];
			if (match){
				if (entry.name.indexOf(match) == -1){
					continue;
				}
			}
			if (shallowDelete){
				//just mark the file as out of date instead of physically removing the file
				Gopher.prototype.clearCache(entry);
			} else {
				if (entry.isDirectory){
					entry.removeRecursively($.noop);
				} else {
					entry.remove($.noop);
				}
			}
		}
	},
	clearFiles: function(files){
		console.log('filestore clearfiles', files);
		for (var i = 0; i < files.length; i++){
			var url = files[i];
			window.resolveLocalFileSystemURL(url, function(fileEntry){
				fileEntry.remove();
			})
		}
	},
	removeOldFiles: function(){
		if (!fileStore.downloadDir) {
			setTimeout($.proxy(fileStore.removeOldFiles, fileStore), 10000);
			return;
		}

		var reader = fileStore.downloadDir.createReader();
		reader.readEntries(function(entries){
			var yesterday = Date.now() - 1000*60*60*24;

			for (var i = 0; i < entries.length; i++){
				var file = entries[i];
				if (file.name.indexOf('__file__') !== -1){
					var bits = file.name.split('__');
					var timestamp = parseInt(bits[0], 10);

					if (timestamp < yesterday){
						console.log('clearing out old file ', file.name);
						file.remove();
					}
				}
			}
		}, log.e);
	}
};