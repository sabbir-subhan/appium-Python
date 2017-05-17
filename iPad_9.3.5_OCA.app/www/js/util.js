/**
 * Set of utility data and functions
 */
var util = {
    infobarTimer: null,
    shortDays: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],

    isEmulator: function () {
        var emulator = false;
        if (!window.device) return false;
        var platform = window.device.platform;
        if (platform !== "iOS" && platform !== "Android" && platform !== "Win32NT") {
            emulator = true;
        }
        return emulator;
    },

    getDeviceId: function () {
        var uuid = '1234567890123456789012345678901234567890';
        if ((typeof window.device != 'undefined') && (!util.isEmulator())) {
            uuid = window.device.uuid.replace(/-/g, '').toLowerCase();
            if (window.device.platform.indexOf('Android') == -1) {
                uuid += '12345678'; //required padding for comms schema(?)
            }
        }

        return uuid;
    },
    isActivated: function () {
        if (Configuration.get('isActivated') && Configuration.get('pin')) {
            return true; // logged in using pin
        }
        return OCASession.isLoggedIn();
    },
    handleResponseExtras: function (response, backgroundMode) {
		if (!response) return;

		var errorMessage = null;
        if (response.errors && response.errors.length) {
            errorMessage = response.errors.join("<br />");
        } else if (response.errors){
			var errors = [];
			for (var k in response.errors){
				errors.push(k + ": " + response.errors[k]);
			}
			if (errors.length){
				errorMessage = errors.join("<br />");
			}
		}
		if (errorMessage && errorMessage.indexOf("_APIPayload") != -1){
			log.e('API Error: ' + errorMessage);	//log error but dont display a technical error message to user
			errorMessage = OCA.getI18n().gettext("An error was received from the server");
		}
		if (errorMessage && backgroundMode !== true){
			util.alertDialog(errorMessage, jQuery.noop, 'Error', 'Ok');
		}

        var notificationMessage = null;
        if (response.notices && response.notices.length) {
            notificationMessage = response.notices.join("<br />");
        } else if (response.notices){
            var notices = [];
            for (var k in response.notices){
                notices.push(k + ": " + response.notices[k]);
            }
            if (notices.length){
                notificationMessage = notices.join("<br />");
            }
        }
        if (notificationMessage && backgroundMode !== true){
            util.alertDialog(notificationMessage, jQuery.noop, 'Notice', 'Ok');
        }

		if (response.extraPayloads && response.extraPayloads.length){
			for (var e = 0; e < response.extraPayloads.length; e++){
				util.handleExtraPayload(response.extraPayloads[e])
			}
		}
        //response.notices
    },
	handleExtraPayload: function(extra){

		var sURL = extra.sourceURL.replace(/^\/api\/v\d+\//,'/');

		switch (sURL){
			case '/session':
				//TODO - Needs to change for contents
				Session.handleExtraPayload(extra);
				return; //return so the request is not cached
            case '/policies':
                OCA.gotPolicies(extra.payloads);
                break;
            case '/me/access':
                OCA.gotFeatures(extra.payloads);
                break;
            case '/version':
                OCA.gotVersion(extra.payloads);
                break;
            case '/branding':
                OCA.gotBranding(extra.payloads);
                break;
            case '/locale':
                OCA.gotLocale(extra.payloads);
                break;
            case '/menu':
                OCA.gotQAB(extra.payloads);
                break;
            case '/riskterminology':
                RiskController.gotTerminology(extra.payloads);
                break;
        }

        //cache the request
        var data = {
            responsePayloads:extra.payloads,
            errors:[],
            extraPayloads:null,
            notices:[],
            nextPageURL:null,
            prevPageURL:null
        };

        if (extra.expiryTime){
            data.expiry = new Date(extra.expiryTime).toISOString();
        }
        var g = new Gopher(extra.sourceURL);

        //extraPayloads will ALWAYS be returning data for GET endpoints
        g.method = 'GET';

        g.saveCache(data);
	},
    infobar: function(message, callback, timeout, btnIcon, btnCallback){
        var $active = $("body").pagecontainer("getActivePage");
        if ($active.prop('id') == 'sessionPIN'){
            util.infobarClear();
            return;
        }
        callback    = callback      || $.noop;
        btnCallback = btnCallback   || $.noop;
        if (typeof callback == 'string' && callback[0] == '#'){
            var pageRoute = callback;
            callback = function(){ $("body").pagecontainer( "change", pageRoute, {})};
        }

        this.infobarClear();
        var $header = $('#header');

        var $bar;
        var pagePad = window.device.platform === "iOS" ? 62 : 42;
        $header.data('oldPagePad', pagePad);

        var clearBar = function(){
            $bar.remove();
            $('div[data-role="page"]').css('padding-top', pagePad + 'px');
        }

        if (btnIcon){
            //button bar

            $bar = $('<div data-role="navbar" class="ui-navbar infobar ui-bar-a"><ul class="ui-grid-a"/></div>');
            var $ul = $bar.find('ul');

            $ul.append($("<li class='ui-block-a'><a href='#' class='ui-btn'><h3>" + message + "</h3></a></li>")
                .click(function(){
                    if (timeout !== false) clearBar();
                    callback();
                }));
            $ul.append($("<li class='ui-block-b'><a href='#' class='ui-btn'><span class='icon white " + btnIcon + "'></span></a></li>")
                .click(function(){
					if (timeout !== false) clearBar();
                    btnCallback();
                }));
        } else {
            //infobar

            $bar = $("<div class='ui-bar ui-bar-a infobar'></div>");
            $bar.append("<h3 />").html(message).click(function(){
                clearBar();
                callback();
            });
        }

        $header.append($bar);

        $('div[data-role="page"]').css('padding-top', ($header.height() + 2) + 'px');
        $(window).trigger('infobarResize');

		//close infobar after timeout, or else after navigation.
        if (timeout){
            this.infobarTimer = setTimeout(function(){
                util.infobarClear()
            }, timeout * 1000)
        } else {
			$(window).on('pagebeforechange', function(e, data){
				if (data && data.options && data.options.role != 'popup'){ //close the infobar on navigation, unless its just a popup (e.g. menu loading)
					util.infobarClear();
				}
			});
		}
    },
    infobarClear: function(){
        var $header = $('#header');
        var $bar = $header.find('.infobar');
        if ($bar.length){
            var pagePad = $header.data('oldPagePad');
            $bar.remove();
            $('div[data-role="page"]').css('padding-top', pagePad + 'px');
            $(window).trigger('infobarResize');
        }
        clearTimeout(this.infobarTimer);
        this.infobarTimer = null;
    },
	goBack: function(number){
		if (this.goingBack || number === 0) return;
		this.goingBack = true;

		if (number && $.mobile.navigate && $.mobile.navigate.history && ($.mobile.navigate.history.activeIndex < Math.abs(number))){
			//protect against trying to go back twice when only one page deep, etc.
			number = -$.mobile.navigate.history.activeIndex;
		}

		if (device.platform === "iOS" && parseInt(device.version) >= 9){
			if (number){
				$("body").pagecontainer("go", number);
			} else {
				$("body").pagecontainer("back");
			}
		} else {
			if (number){
				history.go(number);
			} else {
				history.go(-1);
			}
		}
		//prevent accidental double clicks from going
		setTimeout(function(){
			util.goingBack = false;
		}, 300);
	},
    reload: function(){
		//iOS9+ has a bug/behaviour where the window.location.href doesn't update as the app navigates.
		//fetch the current page location from $.mobile.navigate.history instead
		var currentPage = $.mobile.navigate.history.stack[$.mobile.navigate.history.activeIndex];
		var url = currentPage.url || currentPage.hash || window.location.href;
        $("body").pagecontainer("change", url, {
            allowSamePageTransition: true
        });
    },
	dump: function(obj){
		try {
			return JSON.stringify(obj);
		} catch (e){
			var bits = [];
			for (var k in obj){
				try {
					bits.push(k + ": " + JSON.stringify(obj));
				} catch (ee){
					bits.push(k + ": circular");
				}
			}
			return bits.join("----");
		}
	},
	log: function(){
		try {
            if (arguments.length === 1 && typeof arguments[0] == 'string'){
                console.log(arguments[0]);
            } else {
			    console.log(JSON.stringify(arguments, null, '\t'));
            }
		} catch (e){
			console.log('couldnt util log')
		}
	},
    /**
     * Convert a 4 dot point version string into a numeric representation
     * 1st * 1000000 +
     * 2nd * 10000 +
     * 3rd * 100 +
     * 4th
     * @param versionString
     */
    getIntVersion: function(versionString){
        var bits = versionString.split('.');
        var intver = 0;
        var multiplier = 1000000;
        for (var i = 0; i < 4; i++){ //max 4 dot points
            if (bits[i]){
                intver += multiplier * parseInt(bits[i],10);
            }
            multiplier /= 100;
        }
        return intver;
    },
	alertDialog: function(message, callback, title, buttonLabel){
		var templateOptions = {
			message: message,
			title: title || T("Alert"),
			buttonLabel: buttonLabel || T("Ok")
		};

		var $active = $("body").pagecontainer("getActivePage");
		var $pop = $('<div data-role="popup"  data-overlay-theme="a" data-dismissible="false" class="ui-corner-all dynamic-popup"/>');
		ViewUtil.applyTemplate($pop, templateOptions, 'alertDialog');
		$active.append($pop);
		$pop.popup({history: false});
		$pop.popup('open');
		$pop.one('click', 'a.ok-button', function(){
			$pop.popup('close');
			if (callback) {
				callback();
			}
			$pop.remove();
		});
	},
	confirmDialog: function(message, callback, title, buttonLabels){
		var templateOptions = {
			message: message,
			title: title || T("Confirm"),
			buttonLabels: buttonLabels || T(["Ok", "Cancel"])
		};

		var $active = $("body").pagecontainer("getActivePage");
		var $pop = $('<div data-role="popup"  data-overlay-theme="a" data-dismissible="false" class="ui-corner-all dynamic-popup"/>');
		ViewUtil.applyTemplate($pop, templateOptions, 'confirmDialog');
		$active.append($pop);
		$pop.popup({history: false});
		$pop.popup('open');
		$pop.one('click', 'a.button', function(e){
			$pop.popup('close');
			if (callback) {
				callback($(e.target).data('button-index'));
			}
			$pop.remove();
		})
	},
	promptDialog: function(message, callback, title, buttonLabels, initialValue){
		var templateOptions = {
			message: message,
			title: title || T("Confirm"),
			buttonLabels: buttonLabels || T(["Ok", "Cancel"]),
			initialValue: initialValue
		};

		var $active = $("body").pagecontainer("getActivePage");
		var $pop = $('<div data-role="popup"  data-overlay-theme="a" data-dismissible="false" class="ui-corner-all dynamic-popup"/>');
		ViewUtil.applyTemplate($pop, templateOptions, 'promptDialog');
		$active.append($pop);
		$pop.popup({history: false});
		$pop.popup('open');
		$pop.one('click', 'a.button', function(e){
			$pop.popup('close');
			if (callback) {
				callback({
					input1: 	 $pop.find('.prompt-input').val(),
					buttonIndex: $(e.target).data('button-index')
				});
			}
			$pop.remove();
		});
	},
	getHash: function(){
		var currentRoute = $.mobile.navigate.history.stack[$.mobile.navigate.history.activeIndex];
		if (currentRoute.url[0] == '#') {
			return currentRoute.url; //start page usually is a file:// .... index.html , other pages are just #route
		} else if (currentRoute.hash) {
			return currentRoute.hash;
		} else if (currentRoute.pageUrl){ //not always set
			if (currentRoute.pageUrl[0] == '#') {
				return currentRoute.pageUrl;
			} else {
				return '#' + currentRoute.pageUrl;
			}
		} else {
			return '#'; //fallback. if we get here, assume we're at the start page
		}
	}
};
//console.log = function(){};

window.onerror = function(msg, url, line, x){
    console.log('JAVASCRIPT ERROR: ' + msg + " in file: " + url + " , line " + line);
    util.log(arguments);
}

function handleOpenURL(url){
    util.log('handleOpenURL ' + url);
    url = url.replace('oca://', '');
    var bits = url.split('?');
    var path = bits[0];
    var query = bits[1];
    var paramSplit = query.split('&');
    var params = {};
    for (var p = 0; p < paramSplit.length; p++){
        var parts = paramSplit[p].split('=');
        params[parts[0]] = parts[1];
    }

    switch (path){
        case 'login':
        case 'login/':
            Session.loginSAML(params);
            break;
        case 'redirect':
        case 'redirect/':
            var currentDomain = Configuration.getClientUrl();
            var linkDomain = params.protocol + "//" + params.domain;
            if (currentDomain && OCASession.isLoggedIn()){
                if (currentDomain != linkDomain && currentDomain != params.domain){ //check client url against http://domain and just domain - can login with either format
                    util.alertDialog(OCA.getI18n().gettext('Unable to load link from a different OCA instance'), jQuery.noop, 'Error', 'Ok');
                    return;
                }
            } else {
                Configuration.setClientUrl(linkDomain);
            }
            homeController.redirectLink(params.type, params.id);
            break;
        default:
            util.log('switch default');
    }
}

/**
 * Convenience function for translation
 * makes the code more readable by reducing the number of characters used to wrap every string
 * accepts a string - returns translated string
 * or an array - translates each item in the array and returns the array
 * or an object - translates each value (but not each key) and returns the object
 * Operates recursively - i.e. arrays of arrays would be fine
 * @param toTranslate
 * @returns translations in the same type they were recieved
 */
function T(toTranslate){
	if (typeof toTranslate == 'string') {
		return OCA.getI18n().gettext(toTranslate);
	} else if ($.isArray(toTranslate)){
		for (var i = 0; i < toTranslate.length; i++){
			toTranslate[i] = T(toTranslate[i]);
		}
		return toTranslate;
	} else if (typeof toTranslate == 'object'){
		for (var key in toTranslate){
			toTranslate[key] = T(toTranslate[key]);
		}
		return toTranslate;
	}
}
//overwrite the default console output functions so that the published app doesnt talk too much

function isNogginEnvironment() {
	var domain = Configuration.getAPIDomain();
	if (!domain) {	//not logged in
		return true;
	}
	domain = domain.replace('https://', '');
	if (domain.substr(0, 4) == 'demo' && domain.indexOf('nogginoca.com') !== -1) {	//demo sites
		return true;
	} else if (domain.indexOf('el7.clients') !== -1) {	//dev environments
		return true;
	} else if (domain.indexOf('lan.noggin.com.au') !== -1) {	//internal UATs
		return true;
	} else if (location.pathname.indexOf('oca-mobile') !== -1) { //dev environment rather than deployed app
		return true;
	} else if (domain.indexOf('10.1.1') !== -1) { //app using proxy
		return true;
	}

	if (cordova && cordova.logger){
		cordova.logger.useLogger(false); //disable iOS device logs if not on Noggin environment
	}

	return false;
}

var _log      = console.log;
console.log   = function() { if (isNogginEnvironment()) _log.apply(this, arguments); }
var _debug    = console.debug;
console.debug = function() { if (isNogginEnvironment()) _debug.apply(this, arguments); }
var _error    = console.error;
console.error = function() { if (isNogginEnvironment()) _error.apply(this, arguments); }
var _info     = console.info;
console.info  = function() { if (isNogginEnvironment()) _info.apply(this, arguments); }
var _warn     = console.warn;
console.warn  = function() { if (isNogginEnvironment()) _warn.apply(this, arguments); }