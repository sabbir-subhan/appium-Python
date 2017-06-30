router.add({
    "#settings": function() {
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
        if (!OCASession.isLoggedIn()){
            $('#settingContactPin').focus().select().click();
        }
		app.checkLoaded();
		settings.render();
    }
});
$(document).on("pageinit", "#settings", function (e) {
    settings.init($(this));
});

var settings = $.extend({}, app, {
	saveSettingsInterval: null,
	sending: false,
	
    init: function (page) {
        this.$page = page;
        this.$content = this.$page.find('.ui-content .contact.settings');
		this.$pin  = this.$content.find('#settingContactPin');
		this.$save = this.$page.find('#settingsBtnSave');
		
		this.$save.on('click', $.proxy(this.saveSettings, this));
		this.$content.find('form').on('submit', function(e){
			settings.saveSettings();
			e.preventDefault();
			return false;
		});

        this.$lv = this.$page.find('.ui-content .settings ul.ui-listview');

		this.render();
    },
	saveSettings:function () {
        var pin = this.$pin.val();
        if (pin) {
            this.$save.find('span span').text('Saving');
			this.sendPIN(pin);
        } else {
			this.deregisterPush();
            if (!OCASession.isLoggedIn()){  //if clearing the pin and only logged in as a contact, clear the session
                OCASession.kill();
            }
			Configuration.set('pin', null);
			Configuration.set('isActivated', false);
            $.mobile.loading('hide');
			//Init the menu regardless to potentially enable / disable the INBOUNDCOMMS_SUBMIT items
			Session.showMenu();
        }
		this.render();
    },
	/**
     * Get a session token from an activated mobile PIN to enable inbox submission
     * @param {string} pin mobile activation PIN
     */
    getSession:function (pin) {
		new Gopher({
			url: "/session",
			data: {"MobilePIN": pin, "DeviceID": util.getDeviceId()},
			backgroundMode: true,
			dontProcessError: true
		}, $.proxy(this.gotSession, this), $.proxy(this.sessionFail, this, pin)).post(false);
    },
	gotSession: function(response){
		OCA.gotFeatures([{
			Features: [{
				FeatureName: "INBOUNDCOMMS_SUBMIT",
				Endpoints: {
					"/inboxitems": ["POST"]
				}
			}]
		}]);
		OCASession.setSession(response[0].SessionID);
		Session.showMenu();
		new Gopher({url: "/version", dontProcessError: true}, $.proxy(this.gotVersion, this)).run();
	},
	gotVersion: function(versionData){
		OCA.gotVersion(versionData);
		OCA.initPush();
		Session.showMenu();
		this.render();
	},
	sessionFail: function(pin, xhr, status, error){
		if (xhr.status == 404){
			OCA.gotFeatures([{Features: []}]); //session API endpoint does not exist. OCA is too old
        } else if (xhr.status == 401){
            //do nothing, unauthorised status says that this pin is no good
		} else {
			setTimeout($.proxy(this.getSession, this, pin), 5000);	//try again in 5 seconds. 
		}
	},
	/**
	 * Send the activation PIN to comms
	 */
    sendPIN: function (pin) {
        var data = {
            METHOD:			'ACTIVATEPIN',
            PIN:			pin,
            DEVICEID:		'1234567890123456789012345678901234567890',
            APPNAME:		'oca',
            DATA_OS:		'Cordova',
            PUSHTOKEN:		'1234567890123456789012345678901234567890123456789012345678901234',
            DATA_APP:		'OCA ' + OCA.VERSION,
            DATA_DTYPE:		'Ripple',
            DATA_DNAME:		'Emulator',
            PUSHSERVERURL:	'gateway.push.apple.com'
        };
		if (window.device && !util.isEmulator()){
			data.DEVICEID	= util.getDeviceId();
			data.DATA_OS	= device.version;
			data.DATA_DTYPE = device.platform;
			data.DATA_DNAME = device.model;
			if (device.platform == "Android") data.PUSHSERVERURL = 'android.pushapi.noggin.com.au';
		}
		
		this.sending = true;
		$.ajax({
			url: 'https://mob.ngcomms.net',
			success: $.proxy(this.sentPINOK, this, pin),
			error: $.proxy(this.sentPINFail, this),
			data: data,
			dataType: 'xml',
			contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
			type: 'POST',
			processData: true
		});
    },
	/** 
	 * Success callback for sending the mobile PIN to comms.
	 */
	sentPINOK: function(pin, result, status, xhr){
		this.$save.find('span span').text('Save').removeClass('ui-btn-active');
		this.sending = false;
		$.mobile.loading('hide');
		
		var error;
		if ($(result).find('accept').text() === 'true') {
			Configuration.set('pin', pin);
			Configuration.set('isActivated', true);
			var clientUrl = $(result).find('clientsystemurl').text();
			if (clientUrl.length) {
				Configuration.setClientUrl(clientUrl); // Note: clientURL comes out with protocol://domain but no path (api endpoint)
			} else {
				error = OCA.getI18n().gettext("Error, please contact your Admin. (Client URL not received in the response)");
			}
		} else {
			error = OCA.getI18n().gettext("Invalid code. Please contact your OCA Admin");
		}
		this.render();
		
		if (error) {
			util.alertDialog(error, jQuery.noop, 'Error', 'Ok');
		} else {
			// Now get the session from the pin, unless the user is already logged in
			// OCA may take a few minutes to get the pin activation from Comms.
			if (!OCASession.getSessionId()) {
				this.getSession(pin);
			}
			if (this.redirect) {
                $("body").pagecontainer("change", settings.redirect, {reverse:false, changeHash:false});
				this.redirect = null;
			} else {
				util.alertDialog(OCA.getI18n().gettext("App has been activated."), $.noop);
			}
		}
	},
	/**
	 * Failure callback for submitting the mobile PIN to comms
	 */
	sentPINFail: function(xhr, status, error){
		this.$save.find('span span').text('Save').removeClass('ui-btn-active');
		var msg;
		try {
			var xml = $.parseXML(xhr.responseText);
			msg = $(xml).find('error').text();
		} catch (e){
			log.e(e);
		}
		if (!msg) msg = OCA.getI18n().gettext("Unable to connect to server");
		util.alertDialog(msg, $.noop, 'Error', 'Ok');
		this.sending = false;
		$.mobile.loading('hide');
		this.render();
	},
	/**
	 * Update the settings page depending on whether or not the app has been activated with a mobile PIN (if not a user)
     * or various current system settings like primary event (if a user)
	 */
    render: function() {
		this.$lv.empty();
		var fakeType = {listview: this.$lv};
		var fakeData = [];
		TypeEdit.prototype.sectionheaderRender.call(fakeType, {Label: OCA.getI18n().gettext('Settings')});

        this.$page.find('.contact.settings').showIf(!OCASession.isLoggedIn());

        if (OCA.IncidentManager){
            //primary eme
            var fakeFieldPE = {Label: OCA.getI18n().gettext('Primary event')};
            var pe = OCA.getPrimaryEME();
            fakeData = pe ? [pe] : [];
            TypeEdit.prototype.slmcRender.call(fakeType, fakeFieldPE, fakeData, 'emeTreeView');
            fakeFieldPE.Input.singleMode = true;
            fakeFieldPE.Input.change(function(){
                var val = fakeFieldPE.Input.val();
                if (val && val.length){
                    OCA.setPrimaryEME(val[0].url, val[0].label);
                } else {
                    OCA.setPrimaryEME(null,null);
                }
            });
            if (OCA.versionAtLeast('1.6.2.28')){
                //primary role
                var fakeFieldPR = {Label: OCA.getI18n().gettext('Primary role')};
                var pr = OCA.getPrimaryRole();
                fakeData = pr ? [pr] : [];
                TypeEdit.prototype.slmcRender.call(fakeType, fakeFieldPR, fakeData, 'teamrolePrimary');
                fakeFieldPR.Input.singleMode = true;
                fakeFieldPR.Input.change(function(){
                    var val = fakeFieldPR.Input.val();
                    if (val && val.length){
                        OCA.setPrimaryRole(val[0].url, val[0].label);
                    } else {
                        OCA.setPrimaryRole(null, null, true);
                    }
                });
            }
        }
		if (!OCASession.isLoggedIn()) {
            if (this.sending){
                this.$save.addClass('ui-disabled');
            } else {
                this.$save.removeClass('ui-disabled');
            }

            this.$content.find('.show-if-pin-active').showIf(Configuration.get('isActivated'));
            this.$content.find('.show-if-pin-inactive').showIf(!Configuration.get('isActivated'));
            this.$pin.val(Configuration.get('pin'));
        }

		var fakeFieldLang = {
			ID: 'Language',
			Label: OCA.getI18n().gettext('Language'),
			Minimum: "0",
			Maximum: "1",
			DefaultValue: 'auto',
			Options: [['', "("+OCA.getI18n().gettext('automatic')+")"]]
		}
		for (var langCode in locale_data){
			if (langCode == 'fr_fr') continue; //just an alias, skip it as an option
			var langLabel = locale_data[langCode].meta.label;
			fakeFieldLang.Options.push([langCode, langLabel])
		}
		fakeData = OCALocale.getLanguageSetting();
		TypeEdit.prototype.optRender.call(fakeType, fakeFieldLang, fakeData);
		fakeFieldLang.Input.change(function(){
			var val = fakeFieldLang.Input.val();
			OCALocale.setLanguage(val);
			settings.render();
		});

		if (util.isActivated() && OCA.versionAtLeast('1.9.1') && device.platform != 'Mobile Interface') { //no push plugin available for mobile interface
			var fakeFieldPush = {
				ID:           'Push',
				Label:        T('Notifications'),
				Minimum:      "0",
				Maximum:      "1",
				DefaultValue: 'auto',
				Options:      [
					[0, T('Disable notifications from OCA')],
					[1, T('Enable notifications from OCA')]
				]
			};
			fakeData          = Configuration.get('pushSetting') || 0;
			TypeEdit.prototype.optRender.call(fakeType, fakeFieldPush, fakeData);
			fakeFieldPush.Input.change(function() {
				this.togglePush(fakeFieldPush.Input.val());
			}.bind(this));
		}

//		var $push = this.$page.find('.pushToggle');
//		this.$lv.append($push.replaceWith("<li class='ui-field-contain pushToggle'>" + $push.html() + "</li>"));
//		console.log($push);
//		$push.showIf(OCA.versionAtLeast('1.9') && OcaSession.isLoggedIn());
//		if (OCA.versionAtLeast('1.9')) {
//			var pushSetting = Configuration.get('pushSetting') || 0;
//			var $pushToggle = this.$page.find('#pushToggle').flipswitch();
//
//			$pushToggle.val(pushSetting).flipswitch('refresh').off('change.push').on('change.push', function(e) {
//				this.togglePush($pushToggle.val());
//			}.bind(this));
//		}

        var $ios = this.$page.find('.ios');
        $ios.showIf(device.platform === 'iOS');
        if (device.platform === 'iOS'){
            var accuracySetting = Configuration.get('iosAccuracySetting') || 'high';
            var $accuracy = $ios.find('select');

            var explain = function(){ //TODO i18n
                $ios.find('.explanation').text(Configuration.get('iosAccuracySetting') !== 'low'
                    ? 'Background tracking will use more power and operate at regular intervals'
                    : 'Background tracking will only trigger on significant location changes - at least 500m'
                );
            };
            explain();
            $accuracy.val(accuracySetting).selectmenu('refresh').off('change.acc').on('change.acc', function(e){
                Configuration.set('iosAccuracySetting', $accuracy.val());
                explain();
            });
        }
		this.$lv.enhanceWithin().listview('refresh');
    },
	togglePush: function(pushSetting){
    	if (pushSetting == '2') { 	//when called from the initial prompt in OCA.initPush, 1 = Ok, 2 = Dont Allow
    		pushSetting = '0'; 		//every other time 0 = Disable, 1 = Enable
		}

		Configuration.set('pushSetting', pushSetting);
		var devicePayload = {
			Name: device.model,
			Model: device.model,
			Platform: device.platform,
			OSVersion: device.version
		};
		var uuid = util.getDeviceId();

		var pushwoosh = cordova.require("pushwoosh-cordova-plugin.PushNotification");
		if (pushSetting == '1' && pushwoosh){
			pushwoosh.registerDevice(
				function(status) {
					devicePayload.PushToken = status.pushToken;
					new Gopher({url: '/me/device/' + uuid, data: devicePayload, backgroundMode: true}, function(){
//						util.alertDialog("Push token sent to OCA");
						console.log("Successfully sent device!", devicePayload, arguments);
						if ($('body').pagecontainer('getActivePage').prop('id') === 'settings'){
							settings.render();
						}
					}, log.e).put(false);
				},
				function(status) {
					util.alertDialog(T("There was a problem registering your device for push notifications"));
					console.log(status);
					Configuration.set('pushSetting', 0);
				}
			);
		} else {
			devicePayload.PushToken = null;
			new Gopher({url: '/me/device/' + uuid, data: devicePayload, backgroundMode: true}, function(){
				console.log("Successfully de-registered for push!", devicePayload, arguments);
			}, log.e).put(false);
		}
	},
	deregisterPush: function(){
		var devicePayload = {
			Name: device.model,
			Model: device.model,
			Platform: device.platform,
			OSVersion: device.version,
			PushToken: null
		};
		var uuid = util.getDeviceId();
		new Gopher({url: '/me/device/' + uuid, data: devicePayload, backgroundMode: true}, log.d, log.e).put(false);
	}
});