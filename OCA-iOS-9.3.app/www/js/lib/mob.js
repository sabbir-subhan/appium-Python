var device = {
	platform: "Mobile Interface"
};
var cordova = {
	exec: function(){},
	require: function(){}
};
var LocalFileSystem = {
	PERSISTENT: window.PERSISTENT || 1,
	TEMPORARY:  window.TEMPORARY  || 0
};
navigator.notification = {
	alert: function(message){
		alert(message);
	},
	prompt: function(message, callback, title, buttons, defaultText){
		var value = prompt(message, defaultText);
		var result = {
			input1: value,
			buttonIndex: (value === null) ? 0 : 1
		};
		callback(result);
	},
	confirm: function(message, callback, title, buttons){
		var value = confirm(message);
		var button = value === null ? 0 : value === true ? 1 : 2; //dismissed without choosing, ok, cancel = 0,1,2
		callback(button);
	}
};
if (!location.origin){
    //IE does not have location.origin
    location.origin = location.protocol + "//" + location.hostname + (location.port ? ':' + location.port : '');
}
var noggin = {
    getStatus: function(){
        //do nothing.
    }
}

var encryption = {
	isRooted: function(success, error) {
		return success(0); //not rooted
	},
	createSecretKey: function(alias, password, success, error){
		return success(alias + password);	//should never be reached
	},
	getSecretKey: function(alias, password, success, error){
		return success(alias + password);
	},
};


function storageEnabled() {
    try {
        localStorage.setItem("__test", "data");
    } catch (e) {
        return false;
    }
    return true;
}

$(document).ready(function(){
    if (!storageEnabled()) {
        alert('You must turn off private browsing to use OCA');
        return false;
    }
    if (!navigator.cookieEnabled){
        alert('You must turn on cookies to use OCA');
        return false;
    }
	$(document).trigger('deviceready');

    if (location.protocol.indexOf("http") === 0){ //mobile interface is being hosted over HTTP, so set the ClientUrl based on the domain
        Configuration.setClientUrl(location.origin);
    }

    if (Configuration.hasBranding()){ //branding might already be in local storage
        OCA.applyBranding();
    }

    if (!window.openDatabase || OCASession.get('UseAppEncryption')) {
    	window.openDatabase = dbStore.shimOpenDatabase;
		OCA.getTypeData = function(){}; //no caching, so don't bother fetching all of that stuff.
	}
    //if encrypted storage is mandated, use the shim so that nothing is cached
	OCASession.mustUseAppEncryption = function(){
		if (OCASession.get('id') && OCASession.get('UseAppEncryption')){
			window.openDatabase = dbStore.shimOpenDatabase;
			OCA.getTypeData = function(){}; //no caching, so don't bother fetching all of that stuff.
		}
		return false;
	}

	//load ESRI files, extra geo libraries and the map app controller
	var esriCSS = $("<link rel='stylesheet' type='text/css' href='https://js.arcgis.com/3.20/esri/css/esri.css'>");
	$("head").append(esriCSS);

	jQuery.getJS = function(url){
		return jQuery.ajax({url: url, dataType: 'script', cache: true});
	}

	function addScript(url, loadEvent){
		var el = document.createElement('script');
		document.body.appendChild(el);
		el.onload = loadEvent;
		el.src = url;
	}

    function addTrackingIframe(){
        $('<iframe id="tracking" src="/tracking.html" />').appendTo('body');
    }

	addScript("https://js.arcgis.com/3.20/init.js", function(){
		addScript("js/lib/terraformer.min.js", function(){
			addScript("js/lib/terraformer-arcgis-parser.min.js"); //terraformer libraries must be loaded in the correct order for happiness
		});
		addScript("js/map.js"); //must be loaded after ESRI SDK, function()
        addTrackingIframe();
    
	});
	addScript("https://cdn.ckeditor.com/4.5.10/standard/ckeditor.js");
	addScript("https://code.highcharts.com/3.0.5/highcharts.js");

	OCASession.setSession('', '', '');
    if (Configuration.getAPIUrl()){

        //the branding API was made public in 1.6.22. Since the interface has a known domain, fetch it straight away
        new Gopher({url: '/branding', backgroundMode: true}, $.proxy(OCA.gotBranding, OCA)).run();

        //determine if we are already logged in
        new Gopher({url: '/session', dontProcessError: true}, function(){
            //GET /session worked, therefore we have an active and valid session based on cookie authentication
			OCASession.setSession('cookie', 'cookie', Session.state.PASS);
            OCA.getCoreData(true);
            $(window).trigger('loggedIn');
			
            setTimeout(function(){
                $(window).trigger('linkCheck');
            }, 100);
        }, function(){
            //we don't have a current session, but maybe we can SAML
            new Gopher({url: '/session/saml', dontProcessError: true}, function(){
                Session.SAMLAvailable = true;
                new Gopher({url: '/session/saml', data:{}, dontProcessError: true},
                    function(response){
                        Session.user = 'samlUser'; //exact username not important, it just distinguishes from a contact
                        Session.loginOK(response);
                        $(window).trigger('linkCheck');
                    }, function(){
                        $(window).trigger('linkCheck');
                        $('#sessionMenu a').prop('href', '#sessionSSO'); //saml is available but not logged in. present it to the user before the normal login
//						$(window).trigger('loggedOut');
						Session.refresh();
                    }).post(false);
            }, function(){
                $(window).trigger('linkCheck');
                Session.SAMLAvailable = false;
                $('a#sessionSSO').parent().hide(); //SAML not available, hide the button
//				$(window).trigger('loggedOut');
				Session.refresh();
            }).run();
        }).run();
    }

    menuController.handleRedirectRoute = function(type, ID, model, forceSAML){
        var appRedirect = '://redirect?type=' + type + "&id=" + ID + "&protocol=" + window.location.protocol + "&domain=" + window.location.host;
        if (model === 'android'){
            appRedirect = 'intent' + appRedirect + "#Intent;package=com.noggin.oca;scheme=oca;launchFlags=268435456;end;";
        } else {
            appRedirect = 'oca' + appRedirect;
        }

        var $popup = $('#redirectLinkPopup');
        $popup.find('a.app').prop('href', appRedirect);

        $popup.on('click', 'a.interface', function(){
            $popup.popup('close');
            setTimeout(function(){
				menuController.redirectLink(type, ID);
			}, 500);
        });

        $(window).on('linkCheck', function(){
            //other platforms do not need the option of launching the app
            if (!(model === 'android' || model === 'iphone' || model === 'iemobile' || model === 'ipad')){
                menuController.redirectLink(type, ID, forceSAML);
                return;
            }
            $popup.popup('open');
        });
    }

    router.add({
		"#file": {
			handler: function (type, match, ui, page, e) {
				if (!util.isActivated()) {
					mediaFile.$content.hide(); //TODO cant hide when coming via the menu
					settings.redirect = '#file';
                    $("body").pagecontainer("change", $('#settings'), {reverse: false, changeHash: false});
				} else if (!OCA.checkFeature("INBOUNDCOMMS_SUBMIT")){	//logged in but old version
                    $("body").pagecontainer("change", '#not-available', {changeHash: false});
				} else {
					mediaFile.$content.show();
					app.checkLoaded();
				}
				e.preventDefault();
			},
			events: "bs"
		},
        "#home[?]linkobject=(\\w+)&pk(?:.*)?=(\\d+)&model=(\\w+)$": function(t, match){
            var type  = match[1];
            var ID    = match[2];
            var model = match[3];

            menuController.handleRedirectRoute(type, ID, model);
        },
        "#home[?]linkobject=(\\w+)&pk(?:.*)?=(\\d+)&model=(\\w+)&forcesaml=(\\d+)": function(t, match){
            var type  = match[1];
            var ID    = match[2];
            var model = match[3];
            var forceSAML = match[4];

            menuController.handleRedirectRoute(type, ID, model, forceSAML);
        },
        "#home[?]linkobject=(\\w+)&dashboardid=(\\d+)&model=(\\w+)$": function(t, match){
            var type  = match[1];
            var ID    = match[2];
            var model = match[3];

            menuController.handleRedirectRoute(type, ID, model);
        },
        "#home[?]linkobject=(\\w+)&dashboardid=(\\d+)&model=(\\w+)&forcesaml=(\\d+)": function(t, match){
            var type  = match[1];
            var ID    = match[2];
            var model = match[3];
            var forceSAML = match[4];

            menuController.handleRedirectRoute(type, ID, model, forceSAML);
        },
        "#home[?]forcesaml=(\\d+)": function(t, match){
            var forceSAML = match[1];
            if (forceSAML){
                new Gopher({url: '/version', dontProcessError: true, dontCheckCache:true}, function(){
//                    console.log('got version, must be logged in already');
                }, function(){
//                    console.log('failed to get /version, not logged in!')
                    Session.redirectSAML();
                }).run();

            }
        },
		"#error[?]msg=(.+)": function(t,match,u, page, e){
			$(page).find('p.error').text(decodeURI(match[1]));
		}
	});
	$(document).on("pageinit", "#file", function (e) {
		mediaFile.init($(this));
	});
	router.add({
		"#locationLitePage": {
			handler: function(type, match, ui, page, e){
				//if not allowed, redirect to settings page
                if ((!Configuration.get('isActivated') || !Configuration.get('pin')) && !OCASession.isLoggedIn()) {
					locationLite.$content.hide(); //TODO cant hide when coming via the menu
					settings.redirect = '#locationLitePage';
                    $("body").pagecontainer("change", $('#settings'), {reverse: false, changeHash: false});
				} else {
					locationLite.$content.show();
					app.checkLoaded();
				}
				e.preventDefault();
			},
			events: "bs"
		}
	});
	$(document).on("pageinit", "#locationLitePage", function(e){
		locationLite.init($(this));
	});
	$(document).on("pagehide", "#locationLitePage", function(){
		clearTimeout(locationLite.updateLastSentTimer);
	});

	window.locationLite = $.extend({}, loc, {
		init: function(page){
			this.$page = page;
			this.$content = this.$page.find('.ui-content');

			this.$lastSent = this.$content.find('#locationLiteLastSent');
			this.$sendNow = this.$content.find('#locationLiteSendNow').button();
			this.$sendNow.on('click', $.proxy(this.sendNow, this));
			this.updateLastSent();
		},
		sendNow: function(){
			this.$sendNow.find('.label').text('Sending now');
			this.$sendNow.button('disable').button('refresh');
			navigator.geolocation.getCurrentPosition($.proxy(this.gotPosition, this), $.proxy(this.noPosition, this));
		},
		gotPosition: function(position){
            new Gopher({
                url: "/locations",
                data: {
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude,
                    accuracy: position.coords.accuracy,
                    device_uuid: "1234567890123456789012345678901234567890",
                    device_model: navigator.vendor,
                    device_name: device.platform,
                    device_version: navigator.userAgent
                },
                backgroundMode: true,
                dontProcessError: true
            }, $.proxy(this.sentPosition, this), $.proxy(this.unsentPosition, this)).post(false);
		},
		noPosition: function(){
			alert(OCA.getI18n().gettext('Unable to determine position'));
			this.refresh();
		},
		sentPosition: function(){
			this.lastSentTime = new Date();
			Configuration.set('locationLastSentTime', new Date().toISOString());
			this.refresh();
		},
		unsentPosition: function(){
			alert("Could not submit location");
			this.refresh();
		},
		refresh: function(){
			this.updateLastSent();
			this.$sendNow.find('.label').text('Send once now');
			this.$sendNow.button('enable').button('refresh');
		}		
	});

	var mediaFile = $.extend({}, app, {
		init: function($page){
			this.$page = $page;
			this.$content = this.$page.find('.ui-content');
			this.$page.find('#fileBtnSend').on('click', $.proxy(this.getLocation, this));
			this.$page.find('#fileBtnReset').on('click', $.proxy(this.reset, this));
		},
		getLocation: function(){
			$.mobile.loading('show');
			navigator.geolocation.getCurrentPosition(
				function (pos) {
					mediaFile.sendFile(pos.coords);
				},
				function (error) {
					mediaFile.sendFile(null);
				},
				{timeout: 5000}
			);
		},
		sendFile: function(coords){
			var form = this.$content.find('form');
			var file = form.find('input')[0].files[0];
			var data = new FormData();
			data.append('file', file);
			data.append('Body', form.find('textarea').val());
			if (coords){
				data.append('Lat', coords.latitude);
				data.append('Lng', coords.longitude);
				data.append('AccuracyMetres', coords.accuracy);
			}
			$.ajax({
				url: Configuration.getAPIUrl() + "/inboxitems",
				type: 'POST',
				success: $.proxy(this.sendOK, this),
				error: $.proxy(this.sendFail, this),
				cache: false,
				data: data,
				contentType: false, 
				processData: false
			});
		},
		sendOK: function(data, status, xhr){
			util.goBack();
			$.mobile.loading('hide');
		},
		sendFail: function(){
			alert(OCA.getI18n().gettext("Could not submit media"));
			$.mobile.loading('hide');
		},
		reset: function(){
			this.$content.find('input, textarea').val(null);
			var self = this;
			setTimeout(function(){
				self.$page.find('.ui-btn-active').removeClass('ui-btn-active');
			}, 100);
		}

	});
});


//FileTransfer cordova
//implemented from file:///Users/tom/app/branches/current/platforms/web/index.html

function getParentPath(filePath) {
    var pos = filePath.lastIndexOf('/');
    return filePath.substring(0, pos + 1);
}

function getFileName(filePath) {
    var pos = filePath.lastIndexOf('/');
    return filePath.substring(pos + 1);
}

function getUrlCredentials(urlString) {
    var credentialsPattern = /^https?\:\/\/(?:(?:(([^:@\/]*)(?::([^@\/]*))?)?@)?([^:\/?#]*)(?::(\d*))?).*$/,
        credentials = credentialsPattern.exec(urlString);

    return credentials && credentials[1];
}

function getBasicAuthHeader(urlString) {
    var header =  null;


    // This is changed due to MS Windows doesn't support credentials in http uris
    // so we detect them by regexp and strip off from result url
    // Proof: http://social.msdn.microsoft.com/Forums/windowsapps/en-US/a327cf3c-f033-4a54-8b7f-03c56ba3203f/windows-foundation-uri-security-problem

    if (window.btoa) {
        var credentials = getUrlCredentials(urlString);
        if (credentials) {
            var authHeader = "Authorization";
            var authHeaderValue = "Basic " + window.btoa(credentials);

            header = {
                name : authHeader,
                value : authHeaderValue
            };
        }
    }

    return header;
}

function checkURL(url) {
    return url.indexOf(' ') === -1 ?  true : false;
}


var idCounter = 0;

var transfers = {};

var FileTransfer = function() {
    this._id = ++idCounter;
    this.onprogress = null; // optional callback
};

resolveLocalFileSystemURL = function(target, callbackWithDir){
    callbackWithDir(fileStore.cacheDir);
}

FileTransfer.prototype.download = function(source, target, successCallback, errorCallback, trustAllHosts, options) {

    // Check if target URL doesn't contain spaces. If contains, it should be escaped first
    // (see https://github.com/apache/cordova-plugin-file-transfer/blob/master/doc/index.md#download)
    if (!checkURL(source)) {
        errorCallback && errorCallback(new FileTransferError(FileTransferError.INVALID_URL_ERR, source, target));
        return;
    }

    options = options || {};

    var headers = options.headers || {};

    var basicAuthHeader = getBasicAuthHeader(source);
    if (basicAuthHeader) {
        source = source.replace(getUrlCredentials(source) + '@', '');
        headers[basicAuthHeader.name] = basicAuthHeader.value;
    }

    var that = this;
    var xhr = transfers[this._id] = new XMLHttpRequest();

    var fail = errorCallback && function(code, status, response) {
        transfers[that._id] && delete transfers[that._id];
        // In XHR GET reqests we're setting response type to Blob
        // but in case of error we need to raise event with plain text response
        if (response instanceof Blob) {
            var reader = new FileReader();
            reader.readAsText(response);
            reader.onloadend = function(e) {
                var error = new FileTransferError(code, source, target, status, e.target.result);
                errorCallback(error);
            };
        } else {
            var error = new FileTransferError(code, source, target, status, response);
            errorCallback(error);
        }
    };

    xhr.onload = function (e) {

        var fileNotFound = function () {
            fail(FileTransferError.FILE_NOT_FOUND_ERR);
        };

        var req = e.target;
        // req.status === 0 is special case for local files with file:// URI scheme
        if ((req.status === 200 || req.status === 0) && req.response) {
            window.resolveLocalFileSystemURL(getParentPath(target), function (dir) {
                //prevent javascript error on mobile interface
				if (!dir) dir = fileStore.cacheDir; //hacky fallback - target should already be a fileStore.cacheDir derived URL, but there are contradicting ways of specifying the schemes and things get messy
                if (!dir){							//but if it doesn't work, don't proceed
                dir.getFile(getFileName(target), {create: true}, function writeFile(entry) {
                    entry.createWriter(function (fileWriter) {
                        fileWriter.onwriteend = function (evt) {
                            console.log('file transfer onwrite end', evt, entry, successCallback);
                            if (!evt.target.error) {
                                entry.filesystemName = entry.filesystem.name;
                                delete transfers[that._id];
                                successCallback && successCallback(entry);
                            } else {
                                fail(FileTransferError.FILE_NOT_FOUND_ERR);
                            }
                        };
                        fileWriter.onerror = function () {
                            fail(FileTransferError.FILE_NOT_FOUND_ERR);
                        };
                        fileWriter.write(req.response);
                    }, fileNotFound);
                }, fileNotFound);
                }
            }, fileNotFound);
        } else if (req.status === 404) {
            fail(FileTransferError.INVALID_URL_ERR, req.status, req.response);
        } else {
            fail(FileTransferError.CONNECTION_ERR, req.status, req.response);
        }
    };

    xhr.onprogress = function (e) {
        that.onprogress && that.onprogress(e);
    };

    xhr.onerror = function () {
        fail(FileTransferError.CONNECTION_ERR, this.status, this.response);
    };

    xhr.onabort = function () {
        fail(FileTransferError.ABORT_ERR, this.status, this.response);
    };

    xhr.open("GET", source, true);

    for (var header in headers) {
        if (headers.hasOwnProperty(header)) {
            xhr.setRequestHeader(header, headers[header]);
        }
    }

    xhr.responseType = "blob";

    xhr.send();
}

/**
 * Aborts the ongoing file transfer on this object. The original error
 * callback for the file transfer will be called if necessary.
 */
FileTransfer.prototype.abort = function() {
    if (this instanceof FileTransfer) {
        if (transfers[this._id]) {
            transfers[this._id].abort();
            delete transfers[this._id];
        }
    }
};

/**
 * FileTransferError
 * @constructor
 */
var FileTransferError = function(code, source, target, status, body, exception) {
    this.code = code || null;
    this.source = source || null;
    this.target = target || null;
    this.http_status = status || null;
    this.body = body || null;
    this.exception = exception || null;
};

FileTransferError.FILE_NOT_FOUND_ERR = 1;
FileTransferError.INVALID_URL_ERR = 2;
FileTransferError.CONNECTION_ERR = 3;
FileTransferError.ABORT_ERR = 4;
FileTransferError.NOT_MODIFIED_ERR = 5;