/**
 * Stores data required by the next page.
 * Currently only used when loading the map screen from an address field - the address data is stored in this object
 */
var linkParams = {};

/**
 * Central controller/configurer for the app. Handles AJAX defaults and the loading of some core data on application load
 */
var OCA = {
    $header: null,
    IncidentManager: false,
    Risk           : false,
	FeaturesLoaded : false,
	ACTION_CREATE  :'POST',
	ACTION_READ    :'GET',
	ACTION_UPDATE  :'PUT',
	ACTION_DELETE  :'DELETE',
    currentAjaxConfig: null,
    VERSION: '10.0.9',
    Locale:{},
    Settings: {},
	nameCache: {},
	typeQueue: [],

    taskTimer: null,
    taskPollInterval: 1000 * 60 * 1, //every 1 minute;
	pushTimer: null,
	pushPollInterval: 1000 * 60 * 1, //every 1 minute;

    config:           function () {
        console.log('OCA app version ' + OCA.VERSION);
        $.mobile.defaultPageTransition = "none";
        $.mobile.defaultDialogTransition = "none";
		if (device.platform === "iOS" && parseInt(device.version) >= 9){
			$.mobile.hashListeningEnabled = false;
		}

        var ajaxConfig = {
            contentType: 'application/json',
            dataType: 'json',
            processData: false,
            headers: {"X-OCA-AppVer": OCA.VERSION}
        };
        if (OCASession && OCASession.get('id')) {
//			console.log('setting header ' + OCASession.get('id') + ' for ' + OCASession.getUser());
        	ajaxConfig['headers']["X-Session-ID"] = OCASession.get('id');
        }

        if (JSON.stringify(this.currentAjaxConfig) === JSON.stringify(ajaxConfig)) return; //dont
        $.ajaxSetup(ajaxConfig);
        this.currentAjaxConfig = ajaxConfig;
    },
    initted: false,
    init: function () {
        $('#menu .home-icon-grid').removeClass('hidden');
        this.setupLanguage();
        if (this.initted) return;
        this.initted = true;

        OCA.$header = $('#header');
        this.config();

        if (OCASession.getSessionId()) { //whether contact or user
			this.getCoreData();
			if (Session.shouldCheckPIN()){
				Session.checkPIN();
			} else {
				dbStore.init();
			}
		}

        if (OCASession.isLoggedIn()) { //only applies to users
			this.initUserData();
           	this.startTaskPolling();
            this.applyBranding();

			if (OCASession.getDataRetentionDefaultLength()){
            	dbStore.purge();
			}
		}

		GopherQueue.init();

		$(window).on('loggedIn', $.proxy(this.initUserData, this));
        $(window).on('loggedIn', $.proxy(this.startTaskPolling, this));
        $(window).on('loggedIn', $.proxy(this.translate, this));

		homeController.loadDashboard();
    },

    setupLanguage: function(gotLocale){
        if (!gotLocale) OCALocale.getDeviceLocale();

        var activeLanguage = OCALocale.selectLanguage();
        if (!this.hasOwnProperty('currentLanguage') || activeLanguage != OCA.currentLanguage){
            if (this.hasOwnProperty('i18n')){
                delete OCA.i18n;
            }
            OCA.currentLanguage=activeLanguage;
        }
        OCA.translate();
    },

    getI18n: function(){
        if (!this.hasOwnProperty('currentLanguage')){
            this.setupLanguage();
        }
        if (!this.hasOwnProperty('i18n')){
            this.i18n = new Jed({
                "domain" : "oca",
                "locale_data" : locale_data[OCA.currentLanguage]
            });
//            console.log('setting up Jed with : '+OCA.currentLanguage);
        }
        return this.i18n;

    },
    translate: function(){
        $('[data-translate]').not('.transspecial,#locationInterval option,#locationDuration option,[data-role="popup"] *').each(this.translateStandard);
        $('#locationInterval option,#locationDuration option').each(function(){
            var textarr = $(this).data('translate').trim().split(' ');
            if (textarr.length > 1){
                $(this).text(OCA.getI18n().translate("%d "+textarr[1]).fetch(parseInt(textarr[0])));
            } else {
                $(this).text(OCA.getI18n().gettext($(this).data('translate')));
            }
        });

        $('.transspecial').each(this.translateSpecial);
    },
    translateStandard: function(){
        if ($(this).data('translate')){
            $(this).text(OCA.getI18n().gettext($(this).data('translate').trim()));
            $(this).addClass('translated');
		}
    },
    translateSpecial: function(){
        var child = $(this).children().first();
            child.detach();
            $(this).text(OCA.getI18n().gettext($(this).data('translate')));
            $(this).html($(this).text().replace('%s',$('<div>').append(child.clone()).html()));
            $(this).addClass('translated');
    },
    getCoreData: function (giveUp) {
		if (!dbStore.DB){
//			console.log('no cache, lets try later');
			$(window).one('databaseReady', $.proxy(this.getCoreData, this));
			return;
		}
		// console.log('get core data with ' + OcaSession.getSessionId());
        //fetch common records like the policy list
        if (OCASession.isLoggedIn()) {
            if (OCA.versionAtLeast('1.6.7')){
                new Gopher({url: '/menu', backgroundMode: true},    $.proxy(this.gotQAB,     this)).run();
                new Gopher({url: '/locale', backgroundMode: true},  $.proxy(this.gotLocale,  this)).run();
                if (!giveUp) { //already know the version; dont get stuck in an infinite loop because gotVersion calls this func
                    new Gopher({url: '/version', backgroundMode: true}, $.proxy(this.gotVersion, this)).run();
                }
                //user might not have access to this endpoint. Use background mode to prevent ugly messages
                //note that the features may not have loaded, so we cannot reliably use OCA.checkFeature
                new Gopher({url: '/outboundcomms/addresses', backgroundMode: true}, $.proxy(message.gotFromAddresses, message)).run();
            }
            if (OCA.versionAtLeast('1.6.12')){
                //as above, using background mode
                new Gopher({url: '/outboundcomms/statuses', backgroundMode: true}, $.proxy(comms.gotStatuses, comms)).run();
                new Gopher({url: '/settings', backgroundMode: true}, $.proxy(this.gotSettings, this)).run();
            }

			if (OCA.versionAtLeast('1.7.0')){
				Teamroles.migrateLabels(); //1.7.0 had the IRM changes converting teamroles to resource assignments. Update labels accordingly
			}

			this.initPush();

			new Gopher("/policies",    $.proxy(this.gotPolicies,this)).run();
            if (giveUp && this.FeaturesLoaded){
                return; //already got features so lets give up easily
            }
			this.FeaturesLoaded = false;
			new Gopher('/me/access',   $.proxy(this.gotFeatures,this)).run();
        } else if (OCASession.getSessionId()){  //if logged in as a contact, show the inbox submissions
            OCA.gotFeatures([{
                Features: [{
                    FeatureName: "INBOUNDCOMMS_SUBMIT",
                    Endpoints: {
                        "/inboxitems": ["POST"]
                    }
                }]
            }]);
            Session.showMenu();
			this.initPush();
        }
    },
	/**
	 * For each set of types which the user has access to and is required for offline behaviour to function,
	 * fetch the listing endpoint and then add each type to a processing queue.
	 */
	getTypeData: function(){
		if (localStorage['noTypes']) return;
		this.typeQueue = [];
		for (var key in OCA.Features){
			if (key == 'RESOURCEASSIGNMENTS') continue; //currently no support for resource assignments in the app
			for (var url in OCA.Features[key]){
				if (url.indexOf('types') !== -1) {
					new Gopher({url: url, backgroundMode: true, dontCheckCache: true}, function(typeSummaries){
						for (var t = 0; t < typeSummaries.length; t++) {
							OCA.name(typeSummaries[t].URL, typeSummaries[t].Name);
							this.typeQueue.push(typeSummaries[t].URL);
						}
						this.processTypeQueue(); //n.b. this will create a 'thread' for each set of types - potentially 10 at once for high access user on a risk system
					}.bind(this)).run();
				}
			}
		}
	},
	/** Update the offline sync badge with the count of pending items to fetch, then get the next item */
	processTypeQueue: function(){
		storage.updateBadge(this.typeQueue.length);
		if (this.typeQueue.length === 0){
			return;
		}
		var typeURL	= this.typeQueue.pop();
		new Gopher({url: typeURL, backgroundMode: true, dontCheckCache: true}, function(typeData){
			this.processTypeQueue(); //dont need to do anything with typeData, it has already been cached by Gopher
		}.bind(this), function(){
			this.typeQueue.push(typeURL);
		}.bind(this)).run();
	},
	/** return a list of the names of types to be fetched */
	getTypeQueue: function(){
		return this.typeQueue.map(function(url){ return OCA.name(url); });
	},
	/**
	 * When logged in to a system, set up the OCA.systemData storage
	 * This is data which belongs to a particular user on a particular system, like their primary EME
	 */
	initUserData: function(){
		console.log('init user data');
		var key = Configuration.get('clientUrl') + OCASession.getUser();
		this.userData = new LocalNoSQL(key);
        this.displayCurrentUserData();
	},
    /**
     * After logging in, display an infobar message saying what the current primary EME and primary role is, if set.
     */
    displayCurrentUserData: function(){
        var pe = this.getPrimaryEME();
        var msg = []
        if (pe){
            msg.push('Primary event: ' + pe.label);
        }
        var pr = this.getPrimaryRole();
        if (pr){
            msg.push('Primary role: ' + pr.label);
        }
        msg = msg.join("<br />");
        if (msg){
            util.infobar(msg, "#settings", 15);
        }
    },
    /**
     * Start regular polling of the tasks/assigned/me endpoint. Display an infobar message if a new task is assigned to the current user
     */
    startTaskPolling: function(){
		if (localStorage['stopPolling']) return;
		if (!OCA.userData) {
			log.e("No user data")
			return;
		}
		//poll for assigned tasks
        var checkTasks = function(){
            new Gopher({url: '/tasks/assigned/me?status=ANY', dontCheckCache: true, backgroundMode: true}, function(data){
                var taskCount = OCA.userData.get('myTaskCount') || 0;
                if (taskCount !== data.length){
                    if (data.length > taskCount){
                        var msg = (taskCount + 1 === data.length)
                            ? OCA.getI18n().gettext("New task assigned")
                            : OCA.getI18n().gettext("New tasks assigned");
                        util.infobar(msg, "#taskIndex?assigned=me", 30);
                    }
                    OCA.userData.set('myTaskCount', data.length);
                }
                TaskController.myTaskCount = data.length;
            }).run();
        }
        checkTasks();
        if (this.taskTimer){
            clearInterval(this.taskTimer);
        }
        this.taskTimer = setInterval(checkTasks, this.taskPollInterval);
        $(window).on('loggedOut', $.proxy(this.stopTaskPolling, this));
    },
    stopTaskPolling:  function(){
        if (this.taskTimer){
            clearInterval(this.taskTimer);
            this.taskTimer = null;
        }
    },
	stopPushPolling:  function(){
		if (this.pushTimer){
			clearInterval(this.pushTimer);
			this.pushTimer = null;
		}
	},
	/**
	 * Processes the policy options and makes them available at
	 * OCA.policies (full response data)
	 * OCA.policyOptions (array of [URL, Name] arrays)
	 */
    gotPolicies:      function (data) {
        this.policies = data;
        this.policyOptions = [];
        for (var p = 0; p < this.policies.length; p++) {
            var policy = this.policies[p];
            this.policyOptions.push([policy.URL,policy.Name]);
        }
        Session.refresh();
    },
	/**
	 * Loads the features from /me/access
	 */
	gotFeatures: function(data){
		this.FeaturesLoaded = true;

		var df = data[0].Features;
        this.Visibility = {};
        if (data[0].Visibility){
            this.Visibility = data[0].Visibility;
        }

		this.Features = {};

		for (var i = 0; i < df.length; i++){
			this.Features[df[i].FeatureName] = df[i].Endpoints;
		}

        if (data[0].Packs){
            this.IncidentManager = ($.inArray('OCA_EMERGENCY', data[0].Packs) !== -1);
            this.Risk = ($.inArray('OCA_RISK', data[0].Packs) !== -1);
            for (var p = 0; p < data[0].Packs.length; p++){
                $(window).trigger('init-' + data[0].Packs[p]); //set up events for packs to hook into and init.
            }
        }

		this.policyDefaults = {
			Read:		data[0].DefaultReadPolicyURL,
			Write:		data[0].DefaultWritePolicyURL,
			Send:		data[0].DefaultSendPolicyURL,
			TaskUpdate: data[0].DefaultTaskUpdatePolicyURL
		};

		//Reset the home page menu
		Session.refresh();
        $(window).trigger('gotFeatures');
	},
    gotQAB: function(data){
        $('#menu .home-block.qab').remove();
        var targetDiv = $('#menu .home-icon-grid > div').first();

        for (var i in data) {
        	var $button = ViewUtil.getQuickAccessButton(data[i]);
            if ($button) {
            	$button.insertBefore(targetDiv);
			}
        }
        ViewUtil.addQuickAccessButtonListeners($('#menu .home-icon-grid'));
        Session.refresh();
    },
    gotVersion: function(data){
        var ocaVersion = null;
		var apiVersion = null;
        if (data[0] && data[0].OCAVersion){
            ocaVersion = data[0].OCAVersion;
			apiVersion = data[0].APIVersion || 1;
            //handle dev systems
            if (ocaVersion.indexOf('current') !== -1)       ocaVersion = '1.12.0.0';
            else if (ocaVersion.indexOf('beta') !== -1)     ocaVersion = '1.11.0.0';
			else if (ocaVersion.indexOf('longterm') !== -1) ocaVersion = '1.6.26.0';
            else if (ocaVersion.indexOf('stable') !== -1)   ocaVersion = '1.10.0.0';

            OCA.Packs = [{Label: 'OCA', Prefix: 'oca', Version: ocaVersion}];
            if (data[0].Packs) {
                for (var p = 0; p < data[0].Packs.length; p++){
                    data[0].Packs[p].Label = data[0].Packs[p].Label.replace('OCA ', ''); //remove OCA from pack names
                    OCA.Packs.push(data[0].Packs[p]);
                }
            }
        }
        Configuration.setOCAVersion(ocaVersion);
		Configuration.setAPIVersion(apiVersion);
    },
    gotBranding: function(data){
        data = data[0];
        if (data.HeaderColour){
            Configuration.setHeaderColour(data.HeaderColour);
        }
        if (data.HeaderLogo){
            Configuration.setHeaderLogo(data.HeaderLogo);
        }
        this.applyBranding();
    },
    gotLocale:function(data){
        OCALocale.init(data[0]);
    },
    applyBranding: function(){
        OCA.$header.css('background-color', Configuration.getHeaderColour());
        OCA.$header.find('a.oca').html(     Configuration.getHeaderLogo());
    },
    gotSettings: function(data){
        if (!data || !data[0]) return;

        this.Settings = $.extend({}, data[0]);
        if (this.Settings.GeocodeURL){
            theSilentCartographer.ARCGIS_GEOCODE = this.Settings.GeocodeURL;
            if (this.Settings.GeocodeURLexpiry){
                var timeoutdate = new Date(this.Settings.GeocodeURLexpiry);
                var timesecs = Math.round((timeoutdate.getTime() - (new Date()).getTime())/1000);
                if (timesecs < 24*60*60){
                    setTimeout(function(){
                        new Gopher({url: '/settings', backgroundMode: true}, $.proxy(this.gotSettings, this)).run();
                    },timesecs);
                }
            }
        }
    },
	/**
	 * @param {string} feature The name of the feature eg 'REPORTS'
	 *
	 * @returns boolean TRUE if the user has access to the specified feature
	 */
	checkFeature: function(feature){
		if (this.FeaturesLoaded){
			if (this.Features[feature] !== undefined){
				return true;
			}
		}
		return false;
	},

    checkMenuVisibility: function(feature){
        if (this.FeaturesLoaded){
            if (feature in this.Visibility){
                return this.Visibility[feature];
            }
            return true;
        }
        return false;
    },
	/**
	 * Checks that the end point is allowed for the current user
	 *
	 * @param {string} feature  The feature eg "LOGS" or "LOGS_ADDLOG"
	 * @param {string} endpoint The endpoint eg "/logtype/{logtypeid:id}"
	 * @param {string} action   The action, see OCA.ACTION_* eg OCA.ACTION_CREATE
	 *
	 * @returns {boolean} TRUE if the current user has access to the specified action
	 */
	checkEndPoint: function(feature,endpoint,action){
		if (this.FeaturesLoaded){
			var fspec = this.Features[feature];
			if (fspec){
				var mspec = fspec[endpoint];
				if (mspec){
					return $.inArray(action,mspec) !== -1;
				}

			}
		}

		return false;
	},
	getPrimaryEME: function(){
        if (!this.userData) return null;
		var p = this.userData.get('emePrimary');
		if (! p || ! p['url']){
			return null;
		}
		return p;
	},
	setPrimaryEME: function(url,label){
		if (url) {
			this.userData.set('emePrimary',{url:url, label:label});
            util.infobar(OCA.getI18n().gettext('Primary event')+': ' + label, null, 15);
		} else {
            util.infobar(OCA.getI18n().gettext('Primary event cleared'), null, 15);
			this.userData.set('emePrimary',null);
		}
	},
    getPrimaryRole: function(){
        if (!this.userData) return null;
        var p = this.userData.get('rolePrimary');
        if (! p || ! p['url']){
            return null;
        }
        return p;
    },
    /**
     * set the primary role for this session
     * @param {string} url the URL of the teamrole to set. Set null when clearing primary role.
     * @param {string} label the name of the teamrole. Set null when clearing primary role.
     * @param {boolean} [sendToOCA] used when clearing the primary role.
     * If true, an API call will be made to clear the primary team role. Used when clearing primary role from the settings page
     * If false, the API call is not required. Used when allocating out of roles from the allocate page. (allocating out automatically clears the primary role)
     */
    setPrimaryRole: function(url, label, sendToOCA){
        if (url) {
			var id = ViewUtil.getID(url);
            new Gopher({url: Teamroles.migrate('/me/currentteamrole/') + id, data: {Primary: true}}, function(){
				OCA.userData.set('rolePrimary',{url:url, label:label});
				util.infobar(OCA.getI18n().gettext('Primary role')+': ' + label, null, 15);
            }, function(){
				util.infobar(OCA.getI18n().gettext('Error setting primary role'));
			}).put(false);
        } else {
            if (sendToOCA){
                new Gopher({url: Teamroles.migrate('/me/currentteamroles'), data: {Primary: false}}, function(){
					util.infobar(OCA.getI18n().gettext('Primary role cleared'), null, 15);
					OCA.userData.set('rolePrimary',null);
                    util.log('primary role cleared on server')
                }, function(){
					util.infobar(OCA.getI18n().gettext('Error clearing primary role'));
				}).put(false);
            }
        }
    },
    versionAtLeast: function(compareVersion){
        var ocaVersion = Configuration.getOCAVersion();
        if (!ocaVersion){
            return false; //dont know anything about the version, so it's 1.6.0 or earlier.
        } else if (ocaVersion.indexOf('current') != -1){
            return true; //dev system, so definitely up to date
        } else if (ocaVersion.match(/[0-9\.]*/)){ //version is digits and periods, parse it
            compareVersion = util.getIntVersion(compareVersion);
            ocaVersion     = util.getIntVersion(ocaVersion);
            return ocaVersion >= compareVersion;
        } else {
            return false;
        }
    },

	/**
	 * Lookup or set the name of an OCA object
	 * - if url is provided, this function returns the name from the cache if set, else an empty string
	 * - if url AND name are provided, the cached name for that url is set
	 * @param url the url to lookup or set
	 * @param name optional, the name to remember for the url
	 */
	name: function(url, name){
		url = url.replace(Configuration.getAPIUrl(), '');  //full URL was specified, reduce it to the api path
		url = url.replace(Configuration.getAPIPath(), ''); //endpoint is in the base URL, dont need it twice
		if (name){
			this.nameCache[url] = name;
		} else {
			return this.nameCache[url] ? this.nameCache[url] : '';
		}
	},

	initPush: function(){
		var pushwoosh = cordova.require("pushwoosh-cordova-plugin.PushNotification");
		var checkAppMessages = function(){
			new Gopher({url: '/appmessages', dontCheckCache: true, backgroundMode: true}, function(data){
				appMessagesController.currentCount = data.length;
				appMessagesController.unreadCount = data.filter(function(m){ return m.IsRead == '0'}).length;
                if (appMessagesController.checkNew(data)) {
                    util.infobar(T("New message(s) received"), "#appMessages?dismissed=0&search=", 30);
                }
				appMessagesController.updateBadge();
			}).run();
		}

		if (OCASession.getSessionId()){
			checkAppMessages();

			if (!pushwoosh) {
				//no push plugin available (mobile interface or dev env)
				//set up polling of the /appmessages API

				if (this.pushTimer) {
					clearInterval(this.pushTimer);
				}
				if (!localStorage['stopPolling']) {
					this.pushTimer = setInterval(checkAppMessages, this.pushPollInterval);
				}
				$(window).on('loggedOut', $.proxy(this.stopPushPolling, this));
				return;
			}
		}

		var push = Configuration.get('pushSetting');
		if (push === null || push === undefined && OCA.versionAtLeast('1.9.1')){
			var interval = null;
			interval = setInterval(function() {
				push = Configuration.get('pushSetting');
				if (push !== null && push !== undefined){
					clearInterval(interval);
					return;
				}

				util.confirmDialog(
					T("OCA now supports sending 'App Messages' to your device as notifications.")
					+ "<br />"
					+ T("Would you like to enable this feature?"),
					$.proxy(settings.togglePush, settings),
					T("Notifications"),
					[T('Yes'), T("No")]
				);
			}, 1000); //wait a second to show the dialog so its not interrupted by the dashboard loading or navigating to the menu, recur to avoid interrupting popups
		}

		// Should be called before pushwoosh.onDeviceReady
		document.addEventListener('push-notification', function(event) {
			if (device.platform == 'iOS') {
				//on iOS this is a launch event that means the user has clicked on the notification - whether from background or foreground, just go to the app message index
				$("body").pagecontainer("change", '#appMessages?dismissed=0&search=');
			} else {
				util.infobar(T("New message(s) received"), "#appMessages?dismissed=0&search=", 30);
				checkAppMessages();
			}
		});

		// Initialize Pushwoosh. This will trigger all pending push notifications on start.
		pushwoosh.onDeviceReady({
			appid: "341B5-72855",
			projectid: "781252180898",
//			serviceName: "MPNS_SERVICE_NAME"
		});

		if (OCASession.getSessionId() && push == '1') {
			var devicePayload = {
				Name: device.model,
				Model: device.model,
				Platform: device.platform,
				OSVersion: device.version
			};
			var uuid = util.getDeviceId();
			pushwoosh.registerDevice(
				function(status) {
					devicePayload.PushToken = status.pushToken;
					new Gopher({url: '/me/device/' + uuid, data: devicePayload, backgroundMode: true}, function() {
						console.log("Successfully sent device!", devicePayload, arguments);
					}, log.e).put(false);
				},
				function(status) {
					util.alertDialog(T("There was a problem registering your device for push notifications"));
					console.log(status);
				}
			);
		}

		function testPushLaunch(){
		    if (device.platform !== 'Android' && device.platform !== 'iOS'){ //getLaunchNotification only exists on these platforms
		        checkAppMessages(); //if on windows, just check the messages. We can't tell if the app was launched by Push or not.
		        return;
            }

			pushwoosh.getLaunchNotification(function(result){
				if (result){
					pushwoosh.clearLaunchNotification();
					$("body").pagecontainer("change", '#appMessages?dismissed=0&search=');
				} else if (OCASession.getSessionId()){
					//not launched from notification, but at least check for new messages
					checkAppMessages();
				}
			});
		}

		testPushLaunch();
		$(document).on('resume', testPushLaunch);
	}
};



var OCALocale = new LocalNoSQL('ocaLocale');

/*
    translations from native plugins
    OCA.getI18n().gettext("Contact your OCA administrator to send you a contact identifier if you don't have one.");
    OCA.getI18n().gettext("There are no location providers available.")
    OCA.getI18n().gettext("There are no location providers enabled.")
    OCA.getI18n().gettext("There are no location providers available. Your position could not be determined");
    OCA.getI18n().gettext("There are no location providers enabled. Your position could not be determined");
    OCA.getI18n().gettext("Your OCA version requires a contact identifier for location submission");
    OCA.getI18n().gettext("Location data could not be sent due to connectivity issues");
    OCA.getI18n().gettext("Location services are disabled. Enable them in settings to use OCA location tracking");
    OCA.getI18n().gettext("Connection error, please try again later");
*/
OCALocale.deviceOnlyLanguages=['fr_ca','fr_fr']; //ideally this wouldn't be used... any languages supported by the app should be supported by OCA.. locales listed here are usable by the app when not in OCA
OCALocale.init = function(data){
    delete OCA.i18n;

	locale_data['fr_fr'] = locale_data['fr_ca'];

    for (var i in data){
        this.set(i,data[i]); //n.b. null is an acceptable value
    }
    var supportedLanguages = this.getDeviceSupportedLanguages();
    if (data.hasOwnProperty('Language') && data.Language){
        if ($.inArray(data.Language.toLowerCase(),supportedLanguages)){
            this.set('OCALanguage',data.Language.toLowerCase());
        } else {
            log.d('OCA Language not supported in app: '+data.Language.toLowerCase());
        }

    }
    OCA.setupLanguage();
};
OCALocale.getDeviceSupportedLanguages = function(){
	return Object.keys(locale_data);
};
OCALocale.getDeviceLocale = function(){
    if (navigator && navigator.globalization){
        navigator.globalization.getLocaleName(function(devicelocale){
            var deviceLanguage = devicelocale.value.replace('-','_').toLowerCase();
            deviceLanguage = deviceLanguage.toLowerCase();
            var supportedLanguages = OCALocale.getDeviceSupportedLanguages();
            supportedLanguages = supportedLanguages.map(function(value){ return value.toLowerCase(); });

            if ($.inArray(deviceLanguage, supportedLanguages) != -1){
                OCALocale.set('DeviceLanguage',deviceLanguage);
				OCA.setupLanguage(true); //in case the device language should be applied, check setupLanguage again.
            } else {
                log.d('Device Language not supported: '+ deviceLanguage, supportedLanguages);
                OCALocale.set('DeviceLanguage',false);
            }
        },function(){
//            log.d('failed to get device language');
        });
    } else {
//        log.d('no locale plugin available');
    }
};
OCALocale.selectLanguage = function(){
	if (this.get('SettingsLanguage')){ 			//user has set language choice in OCA mobile settings
		return this.get('SettingsLanguage');
	} else if (this.get('OCALanguage')){ 		//user preference
        return this.get('OCALanguage').toLowerCase();
    } else if (this.get('DeviceLanguage')){ 	//detected device settings
        return this.get('DeviceLanguage');
    } else if (this.get('DefaultLanguage')){	//OCA default settings
        return this.get('DefaultLanguage').toLowerCase();
    } else {
        return 'en_au'; 						//fallback
    }
};
OCALocale.setLanguage = function(language){
	this.set('SettingsLanguage', language);
	OCA.setupLanguage();
}
OCALocale.getLanguageSetting = function(){
	return this.get('SettingsLanguage') || null;
}
/**
 *
 * @returns string valid language identifier for use as the locale argument to Date.toLocale(Date|Time)String
 * Must use BCP 47 format
 * Returns current language, or falls back to en-au
 * @see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleDateString
 */
OCALocale.getDateTimeLocale = function(){
	var locale = OCALocale.selectLanguage().replace("_", "-"); //get current language, convert to BCP which seems to be en-au not en_au
	try {
		new Date().toLocaleDateString(locale);
	} catch (e) {
		console.log(e);
		console.log(e.name)
		console.log(e.name == 'RangeError');
		if (true){}
		if (e.name === 'RangeError') {
			//test
			//bad locale name, fall through
		} else {
			return locale;
		}
	}
	return 'en-au'; //fallback to a valid DT
}

/**
	Parent controller for all 'apps' or sections within OCA Mobile
*/
var app = {
	page:    null,
	content: null,
	$mainLV: null,
	pullToRefresh: false,

	parentItem: {
		ID: null, Name: null, URL: null
	},
	currentItem: {
		ID: null, Name: null, URL: null, Singleton: null
	},
	pendingItem: {
		ID: null, Name: null, URL: null, ParentID: null
	},

	indexFilters: {},
	queryParams: ['search', 'status'],	// index filters which are converted to individual parameters

	init:        function() {},
	checkLoaded: function() {
		if (Gopher.activeRequests <= 0) {
			$.mobile.loading('hide');
			Gopher.activeRequests = 0;
		} else {
			$.mobile.loading('show');
			if (app.loadTimer) {
				clearTimeout(app.loadTimer);
			}
			app.loadTimer = setTimeout(app.checkLoaded, 500);
		}
	},

	setCurrentItem: function(type, ID){
		this.currentItem = {
			ID: ID,
			Name: type ? OCA.name('/' + type + '/' + ID) : null,
			URL: type ? '/' + type + '/' + ID : null,
			Singleton: null //reset to null. It is the responsibility of the child controller to maintain
		};
	},

	setPendingItem: function(type, ID, parentID){
		this.pendingItem = {
			ID: ID,
			Name: type ? OCA.name('/' + type + '/' + ID) : null,
			URL: type ? '/' + type + '/' + ID : null,
			ParentID: parentID ? parentID : null
		};
	},

	setParentItem: function(type, ID){
		this.parentItem = {
			ID: ID,
			Name: type ? OCA.name('/' + type + '/' + ID) : null,
			URL: type ? '/' + type + '/' + ID : null
		};
	},

	renderListing: function(){
		//will be implemented by each inheriting section controller
	},

	getListingQuery: function() {
		var query  = {};
		var filter = {};
		for (var k in this.indexFilters) {
			if (this.indexFilters[k] === null || this.indexFilters[k] === undefined || this.indexFilters[k] === '') continue;

			if (this.queryParams.indexOf(k) !== -1) { //handle these keys specially
				query[k]  = this.indexFilters[k];
			} else {
				filter[k] = this.indexFilters[k];
			}
		}
		if (!$.isEmptyObject(filter)) {
			query.filter = filter;
		}

		return query;
	},
	/**
	 * * Utility method to handle the display of an index listing page
	 * - splits data between local and server items
	 * - renders 'pending' section and 'main' section
	 * @param $listview
	 * @param $heading translated string
	 */
	getListing: function(listingURL, heading, callbackOK, renderProperties) {
		var $main     = this.page.find('.main');
		var $pending  = this.page.find('.pending').hide(); //start hidden

		$main.find('.listview').empty();	//start clean
		$main.find('.extra-data').remove(); //remove previous pagination results
		$(window).off('scroll.listview'); 	//remove pagination handlers

		//do heading
		$main.find('h2').text(heading);
		new Gopher(
			{url: listingURL, offlineError: 'inline'},
			$.proxy(this.gotListing, this, $main, $pending, callbackOK, renderProperties),
			log.e
		).run({dontCheckCache: this.forceRefresh});
		this.forceRefresh = false;
		this.checkLoaded();

		if (!app.pullToRefresh){
			app.pullToRefresh = true;
			ViewUtil.pullToRefresh(this.page.find('.ui-content'), function() {
				this.forceRefresh = true;
				this.renderListing();
			}.bind(this));
		}
	},
	/**
	 * Utility method to render a 'secondary' listview - e.g. documents (folders are the 'main' listview)
	 * @param listingURL
	 * @param callbackOK
	 * @param renderProperties
	 */
	getSecondaryListing: function(listingURL, callbackOK, renderProperties){
		var $secondary = this.page.find('.secondary');
		var $pending  = this.page.find('.pending-secondary').hide(); //start hidden
		$secondary.find('.listview').empty();
		$secondary.find('.extra-data').remove();
		this.checkLoaded();

		if (listingURL) {
			new Gopher(
				{url: listingURL, offlineError: 'inline'},
				$.proxy(this.gotListing, this, $secondary, $pending, callbackOK, renderProperties),
				log.e
			).run();
			this.checkLoaded();
		}
	},
	/**
	 * Utility method to handle the display of an index listing page
	 * - splits data between local and server items
	 * - renders 'pending' section and 'main' section
	 * @param {JQuery} $main           DIV containing the listview for the server data
	 * @param {JQuery} $pending        DIV containing the listview for any local pending data
	 * @param {Function} callbackOK
	 * @param {Object} renderProperties
	 * @param {Array} data
	 * @param {Object} extra
	 * @param {string} extra.nextPageURL
	 */
	gotListing: function($main, $pending, callbackOK, renderProperties, data, extra) {
		//set up the render properties
		var defaults = {
			type: 'type',
			icon: 'folder',
			selectorMode: false,
			noItemsMsg:   T("There are no items to display")
		};

		var r = $.extend(defaults, renderProperties);

		//split up the data
		var pendingData = [];
		var mainData    = [];
		for (var i = 0; i < data.length; i++) {
			if (data[i].Name && data[i].URL){
				OCA.name(data[i].URL, data[i].Name);
			}
			if (data[i].local) {
				pendingData.push(data[i]);
			} else {
				mainData.push(data[i]);
			}
		}

		//render the listviews
		var showPending = pendingData.length && !r.selectorMode && $pending;
		if (showPending) {
			var $pLV = $pending.find('ul').empty();
			$pending.show();
			ViewUtil.populateLV($pLV, pendingData, r.type, r.icon);
		}

		if (mainData.length == 0) { 	// if there are no main items,
			if (showPending && 0) {			// but there are pending items, hide the main section (simpler UI)
//				$main.hide();
			} else if (r.noItemsMsg) {	// if there are no main items or pending items, show the 'no items to display' message
				$main.show();
				$main.find('.listview').append("<li data-theme='e'>" + r.noItemsMsg + "</li>").listview('refresh');
			}
		} else {						// if there are main items, render them
			if (r.template){
				ViewUtil.applyTemplate($main.show().find('.listview'), mainData, r.template, extra.nextPageURL);
			} else {
				ViewUtil.populateLV($main.show().find('.listview'), mainData, r.type, r.icon, r.selectorMode, extra.nextPageURL);
			}
		}

		//return to the controller for any extra processing
		if (callbackOK) {
			callbackOK(data, extra);
		}
		this.checkLoaded();
	}
};

/**
 * Utilty object to provide generic logging functionality
 * log.d and log.e accept any number of arguments and attempt to output them all to the console
 */
var log = {
    d: function () {
        if (util.isEmulator()) {
            console.debug(arguments);
        } else {
            console.debug("Debug Msg with " + arguments.length + " parts");
            for (var a = 0; a < arguments.length; a++) {
                console.debug(JSON.stringify(arguments[a]));
            }
        }
    },
    e: function () {
        if (util.isEmulator()) {
            console.debug(arguments);
            var err = new Error('dummy');
            console.debug(err, err.stack);
        } else {
            console.debug("Error Msg with " + arguments.length + " parts");
            for (var a = 0; a < arguments.length; a++) {
                console.error(JSON.stringify(arguments[a]));
            }
            var err = new Error('dummy');
            console.error(JSON.stringify(err.stack));
        }
    }
};

/**
 * Create the router for OCApp. This uses the jQuery Mobile Router plugin.
 */
if (!router) {
    var router = new $.mobile.Router({
		"#fakeRouteToEnableDefaultHandler": {
			handler: function(){},
			events: "s,bC,bc,c,i,bs,bh,h,rm,bl,l" //the default handler will only work if the event is handled at least once somewhere else
		},
		'#not-available': {
			handler: function(){
				app.checkLoaded();
			},
			events: "s"
		}
	},{},{
		/**
		 * display the loading widget when loading a page
		 * when showing a page, remove any active button classes and check if the loading widget may be hidden
		 */
		defaultHandler: function (type, ui, page) {
//            console.log(type, ui, page);
			if (type === "pagebeforechange" && !ui.options.role && !ui.options.fromHashChange) { //dont show loading when opening or closing a popup
//                console.log(type, ui, page, 'handler show loading');
                if (typeof ui.toPage == 'string'){  //pagebeforechange will fire twice. only handle this the first time.
                    Gopher.activeRequests = 0;      //reset active request count if navigating. all current requests are now irrelevant
                }
				$.mobile.loading('show');
//				$('#header').off();
//				$('#header').removeData('pulltorefresh');
				app.pullToRefresh = false;
			} else if (type === 'pageshow'){
                var $active = $("body").pagecontainer("getActivePage");
                $active.find('.ui-btn-active').removeClass('ui-btn-active');

                ViewUtil.resizeForScrolling();
				app.checkLoaded();

				var to = ui.toPage && ui.toPage[0] && ui.toPage[0].id;
				if (Session.shouldCheckPIN() && to !== 'sessionPIN'){ //the PIN should be checked but this is an event for some other page. change to the PIN page instead
					Session.checkPIN();
				}
			}
		},
		defaultHandlerEvents: "s,bC,bc,c,i,bs,bh,h,rm,bl,l"
	});
}

function LocalNoSQL(entity){
	this.entity = entity;
    if (window.location.pathname.indexOf('tests') !== -1) this.entity = 'test_' + this.entity; //make sure tests don't interrupt the dev environment
}

/**
 * Store a value v with key k. If key already exists, it will be overwritten.
 * The value will be serialized and stored in persistent storage
 * @param k
 * @param v any object
 * @returns {*}
 */
LocalNoSQL.prototype.set = function(k,v){
	try {
		v = JSON.stringify(v);
	} catch (err) {
		console.log(err);
		return false;
	}

	window.localStorage.setItem(this.entity + '_' + k, v);
};


/**
 * Get the stored value v from key k
 * @param k
 * @returns {*} (unsterilized object) or empty string
 */
LocalNoSQL.prototype.get = function (k) {
	var v = window.localStorage.getItem(this.entity + '_' + k);
	if (typeof v === 'string' && v.length) {
		try {
			v = $.parseJSON(v);
		} catch (err) {
			v = '';
		}
	}
	return v;
};

/**
 * Remove a key k from storage
 * @param k
 */
LocalNoSQL.prototype.remove = function (k) {
	window.localStorage.removeItem(this.entity + '_' + k);
	return true;
};

/**
 * Remove all keys from storage.
 */
LocalNoSQL.prototype.removeAll = function () {
	var keys = Object.keys(window.localStorage);
	for (var i = 0; i < keys.length; i++){
		var k = keys[i];

		if (k.indexOf(this.entity + '_') === 0){
			window.localStorage.removeItem(k);
		}
	}
};

LocalNoSQL.prototype.debug = function () {
	for (var i = 0; i < window.localStorage.length; i++) {
		console.log(window.localStorage.key(i) + ": " + JSON.stringify(window.localStorage.getItem(window.localStorage.key(i))));
	}
};

var Configuration = new LocalNoSQL('config');

Configuration.MAX_KNOWN_API_VERSION = 2; // TO DO: perhaps move in to a config file?


/**
 * Client URL as comes from Comms GW. Typically with protocol://domain but no API end-point
 * @param url
 */
Configuration.setClientUrl = function (url) {
    url = $.trim(url);
    if (url.charAt(url.length - 1) === '/') { // remove a trailing slash
        url = url.substr(0, url.length - 1);
    }
    Configuration.set('clientUrl', url);
};

Configuration.getClientUrl = function(){
    return Configuration.get('clientUrl');
}

Configuration.setOCAVersion = function(ver){
    Configuration.set('OCAVersion', ver);
}

Configuration.getOCAVersion = function(){ return Configuration.get('OCAVersion'); }

Configuration.setAPIVersion = function(ver){
	Configuration.set('APIVersion', ver);
	if (ver > Configuration.MAX_KNOWN_API_VERSION){
		//the APIVersion from the server is higher than this client knows about
		//warn the user
		util.infobar("Warning: this app may be out of date. Please check for updates.")
	}
}

Configuration.getAPIPath = function(){
	var path = '/api/v';
	var version = Configuration.get('APIVersion') || 1;
	return path + version;
}

/**
 * Add API end-point to the url and return it
 * @returns {*}
 */
Configuration.getAPIUrl = function () {
    var url = Configuration.get('clientUrl');
    if (url) {
        if (url.charAt(url.length - 1) === '/') { // remove a trailing slash
            url = url.substr(0, url.length - 1);
        }
        url = url + Configuration.getAPIPath();
        if (url.indexOf('http') !== 0) {
            // normally it's assumed that we would have protocol on the clientUrl
            // this is to fix it up if it does not.
            url = 'https://' + url;
        }
    }
    return url;
};

/**
 * Only get the domain for the OCA Api. No protocol or end point
 * @returns {*}
 */
Configuration.getAPIDomain = function () {
    var url = Configuration.getAPIUrl();
    if (!url) return false;
    var m = url.match(/(https?:\/\/.+?)\//);
    if (m) {
        return m[1];
    } else {
        if (url) {
            return url;
        }
    }
    return false;
};

Configuration.setHeaderColour = function(value){
    Configuration.set('HeaderColour', value);
}

Configuration.setHeaderLogo = function(value){
    Configuration.set('HeaderLogoUri', value);
}

Configuration.hasBranding = function(){
    return (Configuration.get('HeaderColour') || Configuration.get('HeaderLogo'));
}
Configuration.getHeaderColour = function(){
    var v = Configuration.get('HeaderColour');
    return v ? v : '';
}
Configuration.getHeaderLogo = function(){
    var uri = Configuration.get('HeaderLogoUri');
    return uri
        ? ("<img src='" + uri + "' />")
        : "<span class='icon oca_header white' />";
}

var OCASession = new LocalNoSQL('session');

/**
 * Store session values.
 *
 * @param {string} sessionId The Session Id token
 * @param {string} user username (leave blank if using pin only session)
 * @param {string} state the authentication state (blank if pin only)
 */
OCASession.setSession = function (sessionId, user, state) {
    user  = user  || '';
	state = state || '';
    OCASession.set('id', sessionId);
    OCASession.set('timestamp', new Date().getTime());
    OCASession.set('user', user);
	OCASession.set('state', state);

    OCA.config();
};

OCASession.renewSession = function(sessionID){
	OCASession.set('id', sessionID);
	OCA.config();
};

OCASession.isLoggedIn = function(){
	return (OCASession.getSessionId() && OCASession.getUser() && OCASession.get('state') === Session.state.PASS);
};
/**
 * Gets user name that we're currently logged in user. Useful for checking if the user is logged in
 * @returns string
 */
OCASession.getUser = function () {
    return OCASession.get('user');
};

/**
 * Useful to see if we are logged in with the pin
 * @returns {*}
 */
OCASession.getSessionId = function () {
    return OCASession.get('id');
};

/**
 * Log out as the user, however, the session still remains for pin only auth
 * @returns {*}
 */
OCASession.logout = function () {
    return OCASession.set('user', '');
};

OCASession.setPolicy = function(policyPayload){
	OCASession.set('BlockRootedDevices', policyPayload.BlockRootedDevices);
	OCASession.set('UseAppEncryption', policyPayload.UseAppEncryption);
	OCASession.set('DataRetentionDefaultMins', policyPayload.DataRetentionDefaultMins);
}

OCASession.shouldBlockRootedDevices = function(){
	return OCASession.get('BlockRootedDevices');
}

OCASession.mustUseAppEncryption = function(){
	return OCASession.isLoggedIn() && OCASession.get('UseAppEncryption');
}

OCASession.getDataRetentionDefaultLength = function(){
	return OCASession.get('DataRetentionDefaultMins');
}

OCASession.getEncryptionPIN = function(){
	return OCASession.get('EncryptionPIN');
}

OCASession.setEncryptionPIN = function(pin){
	return OCASession.set('EncryptionPIN', pin);
}

/**
 * Use when logging out
 */
OCASession.kill = function () {
    OCASession.removeAll();
    OCASession.setSession('', '', '');
    OCASession.setPolicy({});
    $.ajaxSettings.headers = {};
	$(window).trigger('loggedOut');
};

OCALocale.remove('OCALanguage');
OCALocale.remove('DefaultLanguage');
OCALocale.remove('DeviceLanguage');
delete OCA.i18n;
