var sessionRoutes = {
	"#session$":            function() {
		Session.domainChecked = false;
		Session.refresh();
	},
	'#sessionTerms':       function(type, match, ui, page) {
		Session.showTerms($(page));
	},
	'#sessionCustomTerms': function(type, match, ui, page) {
		Session.showCustomTerms($(page));
	},
	'#sessionPIN':         function(type, match, ui, page) {
		if (dbStore.decrypted){
			util.goBack();
		}
	}
};
router.add(sessionRoutes);
$(document).on("pageinit", "#sessionTwoFactor", function(){
	Session.init2FA($(this));
});
$(document).on("pageinit", "#sessionSSO", function(){
	Session.initSSO($(this));
});
$(document).on("pageinit", "#sessionPIN", function(){
	Session.initPIN($(this));
	Session.noescape();
});

$(document).on("pagehide", "#sessionPIN", function(){
	Session.clearNoescape();
});

/**
 * The Session application handles login and logout.
 * It also changes the main menu to reflect the current authentication status (i.e. hiding menu icons the user has no access to)
 */
var Session = $.extend({}, app, {
	LOGIN_PATH: Configuration.getAPIPath() + '/session',
	state: {
		FAIL: 'UNAUTHORISED',
		W2FA: 'WAIT_2_FACTOR',
		WTNC: 'WAIT_TERMS_AND_CONDITIONS',
		PASS: 'AUTHENTICATED',
		RNEW: 'RENEW_SESSION',
        SAML: 'RENEW_SAML',
		LOCK: 'LOCKED_OUT',
		RSET: 'RESET_PASSWORD'
	},
	terms: {},
    SAMLAvailable: false,
	initted: false,
	refreshable: true,

	PIN_MIN_LENGTH: 4,
	PIN_MAX_TRIES: 3,
	PINAttempts: 0,
	PINSuccess: $.noop,
	PINFail: $.noop,

	preserveDB: false,

	/**
	 * Initialise the session page on first load:
	 * - find the key containers
	 * - add click handler for the submit button
	 */
    init: function (page) {
        this.$page = page;
        this.$content = this.$page.find('.ui-content');
		this.$menu = $('#sessionMenu');

		var subHandler = function(e){
			Session.submit();
			e.stopPropagation();
			e.preventDefault();
			return false;
		};
        this.$page.on('tap', '#sessionSubmit', subHandler);
        this.$content.find('form').on('submit', subHandler);
		
		if (location.protocol.indexOf("http") === 0){
			this.$content.find('.sessionDomain').hide();
			this.$content.find('#sessionDomain').val(location.origin);
        }

		this.initted = true;
		this.domainChecked = false;
        this.refresh();
    },
	/** 
	 * Displays an input for the second factor authentication (PIN sent via SMS)
	 * Includes the ability to request a new PIN via the 'Resend' button
	 * 
	 * @param {JQuery} $page The two factor authentication page
	 */
	init2FA: function ($page){
		$page.on('tap', '#sessionTwoFactorSubmit', $.proxy(this.submit2FA, this, $page));
		$page.on('tap', '#sessionTwoFactorResend', $.proxy(this.resend2FA, this, $page));
		//handling the submit event will intercept submissions from hitting the enter key, 'Go', etc
		$page.find('form').on('submit', function (e) {
			Session.submit2FA($page);
			e.preventDefault();
			return false;
		});
	},
	/**
	 * Set up SSO listeners
	 * @param {JQuery} $page The SSO page
	 */
	initSSO: function($page){
		var $dom = $page.find('#sessionSSODomain');
        var domain = Configuration.get('clientUrl');
		if (location.protocol.indexOf("http") === 0){
			$dom.val(location.origin);
		} else if (domain && domain.length){
            $dom.val(domain);
        }

		$page.find('form').on('submit', function (e) {
			Session.submitSSO($dom);
			e.preventDefault();
			return false;
		});
		$page.find('#sessionSSOSubmit').on('click', $.proxy(this.submitSSO, this, $dom));
	},

	initPIN: function($page){
		var $PINput = $page.find('#sessionPINput');

		$page.find('.PIN-grid .num a').on('tap', function(e){ //input number
			$PINput.val($PINput.val() + e.target.innerText);
		});
		$page.find('.PIN-grid .clr a').on('tap', function(){ //clear PIN
			$PINput.val('');
		});
		$page.find('.PIN-grid .del a').on('tap', function(){  //delete last number
			$PINput.val($PINput.val().slice(0, -1));
		});

		$page.find('#sessionPINSubmit').on('tap', function(e){
			this.validatePINput($PINput.val());
			$PINput.val('');
			//make sure event doesnt fall through
			e.stopPropagation();
			e.preventDefault();
			return false;
		}.bind(this));
	},


	/**
	 * Displays the terms and conditions.
	 * If accepted, and there is a second set of terms, it redirects to the custom terms page.
	 * If the only set of terms has been accepted, the acknowledgement code is sent to the server
	 * If the terms are declined, the session is cleared and the decline code is sent
	 * 
	 * @param {JQuery} $page The first terms page
	 */
	showTerms: function($page){
		$page.find('.ui-footer').show();
		var $content = $page.find('.ui-content').empty();
		$content.append('<h2>' + this.terms.title + '</h2>');
		$content.append(this.terms.content);
		
		$page.find('#sessionTermsAccept').off().on('click', function(){
			if (Session.terms.customTitle){
                $("body").pagecontainer("change", '#sessionCustomTerms', {changeHash: false});
			} else {
				new Gopher({
						url: "/session",
						data: {TermsAccept: [Session.terms.ackCode]},
						dontCache: true
					},
					$.proxy(Session.loginOK, Session),
					$.proxy(Session.loginFail, Session)
				).put(false);
			}
			$content.empty();
			$page.find('.ui-footer').hide();
		});
		$page.find('#sessionTermsReject').off().on('click', function(){
			new Gopher({
				url: "/session",
				data: {TermsDecline: [Session.terms.ackCode]},
				dontCache: true
			}).put(false);
			OCASession.kill();
			$content.empty();
			$page.find('.ui-footer').hide();
			$("body").pagecontainer("change", '#home', {changeHash: false});
		});
	},
	/**
	 * Displays the second set of terms and conditions, if required. 
	 * This page is reached after the first set of terms and conditions has been accepted.
	 * If these terms are accepted, both acknowledgement codes are sent to the server.
	 * If these terms are declined, the first set is sent as accepted and the second set is declined
	 * 
	 * @param {JQuery} $page The custom terms page
	 */
	showCustomTerms: function($page){
		var $content = $page.find('.ui-content').empty();
		$page.find('.ui-footer').show();
		$content.append('<h2>' + this.terms.customTitle + '</h2>');
		$content.append(this.terms.customContent);
		$page.find('#sessionCustomTermsAccept').off().on('click', function(){
			new Gopher({
					url: "/session",
					data: {
						TermsAccept: [Session.terms.ackCode, Session.terms.customAckCode]
					},
					dontCache: true
				},
				$.proxy(Session.loginOK, Session),
				$.proxy(Session.loginFail, Session)
			).put(false);
			$content.empty();
			$page.find('.ui-footer').hide();
		});
		$page.find('#sessionCustomTermsReject').off().on('click', function(){
			new Gopher({
				url: "/session",
				data: {
					TermsAccept: [Session.terms.ackCode],
					TermsDecline: [Session.terms.customAckCode]
				},
				dontCache: true
			}).put(false);
			OCASession.kill();
			$content.empty();
			$page.find('.ui-footer').hide();
			$("body").pagecontainer("change", '#home', {changeHash: false});
		});
	},
    submit: function(e){
    	if (this.loggedIn){
    		this.logout();
    	} else if (this.domainChecked) {
    		this.login();
    	} else {
    		this.checkDomain();
		}
    },
	/**
	 * Submit the two factor authentication code
	 * @param $2FApage
	 */
	submit2FA: function($2FApage){
		var $pin = $2FApage.find('#session2FA');
		if (!$pin.val()) return;

		new Gopher({
					url: "/session",
					data: {SMSAuthPIN: $pin.val()},
					dontCache: true
				},
				$.proxy(this.loginOK,   this),
				$.proxy(this.loginFail, this)
		).put(false);
		$pin.val(null);
		$2FApage.find('.ui-btn-active').removeClass('ui-btn-active');
	},
	/**
	 * Request the two factor authentication code to be resent
	 * @param $2FApage
	 */
	resend2FA: function($2FApage){
		new Gopher({url: "/session/smsauthpin", dontCache: true}, function(){
			util.alertDialog(OCA.getI18n().gettext("Your PIN has been resent"), jQuery.noop, 'Mobile PIN', 'Ok');
		}, function(){
			util.alertDialog(OCA.getI18n().gettext("Unable to resend PIN"), jQuery.noop, 'Mobile PIN', 'Ok');
		}).post(false);
		$2FApage.find('#sessionPIN').val(null);
		$2FApage.find('.ui-btn-active').removeClass('ui-btn-active');
	},
	submitSSO: function($domainInput){
		var domain = $domainInput.val();
		Configuration.setClientUrl(domain);
		this.redirectSAML();
	},

	checkDomain: function(){
		var domain = this.$content.find('#sessionDomain').val();
		if (domain && domain.length) {
			//strip login.html from the input domain if present
			domain = domain.replace("m/login.html", "");
			domain = domain.replace("login.html", "");
			domain = domain.replace("directlogin.html", "");

			//user has entered the domain incorrectly
			if (domain.indexOf('.html') !== -1){
				util.alertDialog(OCA.getI18n().gettext("The OCA domain is not in the expected format"), $.noop, 'Error', 'Ok');
				return false;
			}

			Configuration.setClientUrl(domain);
		} else { //fail if domain not supplied
			util.alertDialog(OCA.getI18n().gettext("You must enter an OCA domain"), $.noop, 'Error', 'Ok');
			app.checkLoaded();
			return false;
		}

		new Gopher(
			{url: "/version", dontProcessError: true, dontCheckCache: true},
			$.proxy(this.versionCheckOK, this),
			$.proxy(this.versionCheckFail, this)
		).run();
	},

	domainCheckOK: function(){
		this.domainChecked = true; //domain is valid, but if the version check failed it must be super old. Ignore SAML and policy checks; continue to login interface
		Session.refresh();
	},

	domainCheckFail: function(){
		util.alertDialog(T("Unable to connect. Please check the OCA domain"));
	},

	versionCheckOK: function(versionData){
		OCA.gotVersion(versionData);
		new Gopher('/session/saml', this.samlCheckOK.bind(this), this.samlCheckFail.bind(this)).run();
	},

	versionCheckFail: function(xhr, error, message){
		//make sure version info is cleared
		Configuration.setOCAVersion(false);
		Configuration.setAPIVersion(false);

		if (xhr && xhr.status == 401){
			//version check failed because of authentication, which means it's at least 1.6 (/version exists) but less than 1.7.10 (approximately when /version became public)
			//check SAML because that might exist
			new Gopher('/session/saml', this.samlCheckOK.bind(this), this.samlCheckFail.bind(this)).run();
		} else {
			//it's either really old or a wrong domain, so check just the root of the API (domain.com/api/v1)
			new Gopher({url:      '',
				dontProcessError: true,
				mode:             'text',
				dontCheckCache:   true
			}, this.domainCheckOK.bind(this), this.domainCheckFail.bind(this)).run();
		}
	},

	samlCheckOK: function(){
		this.$page.find('li.sso').show();
		this.checkPolicy();
	},

	samlCheckFail: function(){
		//OCA does not support SAML login. Hide the button.
		this.$page.find('li.sso').hide();
		this.checkPolicy();
	},

	checkPolicy: function(){
		if (OCA.versionAtLeast('1.10.0.20')){ //exact fourth point that #49059 passed QA
			new Gopher('/clientpolicies', this.policyCheckOK.bind(this), this.policyCheckFail.bind(this)).run();
		} else {
			OCASession.setPolicy({});
			OCASession.setEncryptionPIN(null);
			this.domainChecked = true;
			Session.refresh();
		}
	},

	policyCheckOK: function(clientPolicy){
		OCASession.setPolicy(clientPolicy[0]);
		OCASession.setEncryptionPIN(null);
		if (OCASession.shouldBlockRootedDevices()){
			this.checkRoot();
		} else {
			this.domainChecked = true;
			Session.refresh();
		}
	},

	policyCheckFail: function(){
		//OCA valid but unable to fetch the clientpolicy for some reason. ??
	},

	checkRoot: function(){
		encryption.isRooted(function(isRooted){
			if (isRooted) {
				this.rootCheckFail();
			} else {
				this.rootCheckOK();
			}
		}.bind(this), function(errorMsg){
			console.error(errorMsg);
			this.rootCheckOK();  //unable to determine definitively whether the device is rooted due to some error, so assume its okay
		}.bind(this))
	},

	rootCheckOK: function(){
		//success callback: this device was not detected to be rooted or jailbroken
		this.domainChecked = true;
		Session.refresh();
	},

	rootCheckFail: function(){
		//fail callback: this device was detected to be rooted
		util.alertDialog(T("Unable to proceed. This OCA domain does not allow rooted or jailbroken devices"));
	},

	/**
	 * function which submits a login request with username and password 
	 */
    login: function() {
        this.user = this.$content.find('#sessionUsername').val();

		new Gopher({
			url: "/session",
			data: {
				"Username": this.user,
				"Password": this.$content.find('#sessionPassword').val()
			},
			dontProcessError: true
		}, $.proxy(this.loginOK, this), $.proxy(this.loginFail, this)).post(false);
    },
	/**
	 * the callback for all successful login related requests
	 * The user is routed to the appropriate page depending on the authentication state - success, requiring two factor authentication or requiring terms and conditions acceptance
	 * @param {SessionResponse_APIPayload} response
	 */
	loginOK: function(response){
		OCASession.setSession(response[0].SessionID, this.user, response[0].StateCode);

		var $body = $('body');
		switch (response[0].StateCode){
			case this.state.PASS:
				if (response[0].Message){
					Session.refreshable = false; //make sure alert is not displayed against backdrop asking if you want to log out
					return util.alertDialog(response[0].Message, this.finaliseLogin.bind(this), 'Notice', 'Ok');
				} else {
					return this.finaliseLogin();
				}
				break;
			case this.state.W2FA:
                $body.pagecontainer("change", '#sessionTwoFactor', {changeHash: false});
				break;
			case this.state.WTNC:
				//NOTE: Issue #48515 changed this so that the OCA terms were displayed second, but it's not worth changing every property name purely for the sake of internal consistency
				//Functionally, the two sets of terms and conditions are interchangeable. It doesn't even matter which order the acknowledgement codes are sent in.
				Session.terms = {
					title  : response[0].TermsTitle,
					content: response[0].TermsContent,
					ackCode: response[0].TermsAckCode
				};
				if (response[1]){
					Session.terms.customTitle   = response[1].TermsTitle;
					Session.terms.customContent = response[1].TermsContent;
					Session.terms.customAckCode = response[1].TermsAckCode;
				}
                $body.pagecontainer("change", '#sessionTerms', {changeHash: false});
				break;
			case this.RNEW:
				//should not occur
				break;
			case this.state.FAIL:
				//should not occur - failed logins go to the loginFail callback
				util.alertDialog(OCA.getI18n().gettext("Invalid login, please retry"), $.noop, 'Error', 'Ok');
				break;
		}
		Session.refresh();
	},
	finaliseLogin: function(){
		if (OCASession.mustUseAppEncryption()){
			if (!OCASession.getEncryptionPIN()){
				return this.setPIN();
			}
		} else {
			dbStore.init();
		}

		//Core data was returned in the extraPayload of the login response, unless there were terms or 2fa
		setTimeout(function() {
			OCA.getCoreData(true);
		}, 500);

		$(window).trigger('loggedIn');

		if (OCA.FeaturesLoaded){ //features might be already loaded if the user had to set up a PIN
			OCA.getTypeData();
		} else {
			$(window).one('gotFeatures', function() {
				OCA.getTypeData();
			});
		}

		Session.refreshable = false; //make sure alert is not displayed against backdrop asking if you want to log out
		this.$page.find('.login').hide();

		$("body").pagecontainer("change", '#home');
		Session.refreshable = true;
		Session.refresh();
	},

	setPIN: function(){
		$('#sessionPIN').find('h2').text(T("Set up PIN lock"));
		$("body").pagecontainer("change", '#sessionPIN');
	},

	shouldCheckPIN: function(){
		return OCASession.mustUseAppEncryption() 	//system wants clients to encrypt data
			&& OCASession.getEncryptionPIN() 		//encryption has been set up for this device
			&& !Session.preserveDB 					//this was not a temporary out-of-app experience (e.g. taking photo) which allows the PIN to be skipped
			&& !dbStore.isDecrypted(); 				//database is not already decrypted
	},

	checkPIN: function(){
		util.infobarClear();
		$('#sessionPIN').find('h2').text(T("Enter PIN to unlock"));
		$("body").pagecontainer("change", '#sessionPIN');
		Session.PINAttempts = 0;
		Session.noescape();
	},
	noescape: function(){

		$(document).on('backbutton',function(){
			return false;
		});
		$(document).on('click','#header a',function(){
			return false;
		});
	},
	clearNoescape: function(){
		$(document).off('backbutton');
		$(document).off('click','#header a');
	},

	PINSetOK: function(pin){
		$(window).on('databaseReady.pin', this.finaliseLogin.bind(this));
		dbStore.create(pin);
	},

	PINCheckOK: function(pin){
		var history = $.mobile.navigate.history;
		var prev = history.stack[history.getIndex() - 1];
		var nav = this.goHome; //by default after unlocking, go to the home page (fresh launch)
		if (prev && (!prev.url || ((prev.url.indexOf('sessionPIN') === -1) && (prev.url.indexOf('#') !== -1)))){ //if there is a previous page to return to, go there after unlocking (resume)
			nav = util.goBack.bind(util, -1);
		}

		$(window).off('databaseReady.pin').on('databaseReady.pin', nav);
		dbStore.decrypt(pin);
	},

	PINCheckFail: function(){
		util.alertDialog(T("Too many invalid PINs. You will be logged out."), this.logout.bind(this));
	},

	goHome: function(){
		$("body").pagecontainer("change", '#home');
	},

	validatePINput: function(input){
		this.PINAttempts++;

		var setPIN = OCASession.getEncryptionPIN();
		if (!setPIN){
			if (input.length < this.PIN_MIN_LENGTH){
				return util.alertDialog(T("PIN too short"));
			}

			OCASession.setEncryptionPIN(input);
			this.PINSetOK(input);
		} else if (input === setPIN){
			this.PINCheckOK(input);
		} else if (this.PINAttempts >= this.PIN_MAX_TRIES){
			this.PINCheckFail();
		} else {
			util.alertDialog(T("PIN does not match"));
		}
	},

    /**
     * Called from noggin.js handleOpenURL when redirecting from SAML auth.
     * POST credentials to /session/saml
	 * @param {string} credentials.sessionID
	 * @param {string} credentials.username
     */
    loginSAML: function(credentials){
		$.mobile.loading('show');
        util.log('loginSAML', credentials);
        if (credentials.username && credentials.sessionID){
            this.user = credentials.username;
            OCASession.setSession(credentials.sessionID, this.user, this.state.SAML);
            new Gopher({
                url: "/session/saml",
                data: {},
                dontProcessError: true
            }, $.proxy(this.loginOK, this), $.proxy(this.loginFail, this)).post(false);
        }
    },
    redirectSAML: function(){
        this.showingSAML = false;
        var path = Configuration.getClientUrl();
		if (path.indexOf('http') !== 0) {
			path = 'https://' + path;
		}
		path = path.replace('http://', 'https://'); //SAML must always use https, even if the OCA doesn't (i.e. dev)
		path += "/login.html?op=op_samllogin&type=";
        if (device.platform === 'Android') {
            path += 'android';   //android is redirected differently on the server side
        } else if (device.platform === 'Mobile Interface'){
            path += 'interface';
        } else {
            path += 'app';
        }
        if (menuController.redirectAfterLogin){
            path += "&linkobject=" + menuController.redirectAfterLogin[0];
            path += "&pk=" + menuController.redirectAfterLogin[1];
        }

        var target = '_system';
        if (device.platform === 'Mobile Interface') target = '_self';

        window.open(path, target, 'location=no');
    },
	/**
	 * If the login fails with a 404 status, it means the OCA domain does not have the REST API endpoints (i.e. is on an old version)
	 * @param {XMLHttpRequest} xhr response object
	 * @param {string} status 
	 * @param {string} error
	 */
	loginFail: function(xhr, status, error){
		var response;
		if (xhr.status === 404){
            $("body").pagecontainer("change", '#not-available', {changeHash:false});
		} else if (xhr.status === 401){
			var msg = T('Invalid username and/or password');	//default assumption for this response code

			//there might be errors set by the API response to display
			if (xhr.responseText){
				try {
					response = JSON.parse(xhr.responseText);
					if (response && response.errors && response.errors.length){
						msg = response.errors.join('<br />');
					}
				} catch (error){
					//oh well
				}
			}
			util.alertDialog(msg, $.noop, 'Error', 'Ok');
		} else if (xhr.status === 302 || status === "parsererror"){
			util.alertDialog(OCA.getI18n().gettext('Authentication error. Please check your OCA domain is in the correct format'), $.noop, 'Error', 'Ok');
		} else if (xhr.status === 0){
			util.alertDialog(OCA.getI18n().gettext('Connection error. Unable to login'), $.noop, 'Error', 'Ok');
		} else {
			try {
				response = JSON.parse(xhr.responseText);
				util.handleResponseExtras(response);
			} catch (error){
                util.alertDialog(OCA.getI18n().gettext('Authentication error:')+' '+xhr.status, $.noop, 'Error', 'Ok');
            }
		}
		Session.refresh();
	},
	/**
	 * Log out - send the logout API call
	 */
    logout: function() {
		if (Configuration.get('pushSetting') == '1') {
			settings.deregisterPush();
		}
		new Gopher("/session", $.proxy(this.logoutResponse, this, true), $.proxy(this.logoutResponse, this, false)).sendDelete(false);
    },
	/**
	 * Log out  - clear the cache, kill the session and refresh the login page and menu
     * @param success if this is reached as a result of a successful logout or failed (db error - session not found, timeout, etc)
     * @param data any data returned by the DELETE request. should be null
     * @param logoutRedirect if the server is configured to redirect on logout, this value will be set
	 */
	logoutResponse: function(success, data, logoutRedirect){
		OCASession.kill();
		Configuration.setOCAVersion(false);
		Configuration.setAPIVersion(false);
		Configuration.setHeaderColour(false);
		Configuration.setHeaderLogo(false);

		var clearedFiles     = $.Deferred(); clearedFiles.done(function(){ console.log('cleared files done');});
		var clearedResponses = $.Deferred(); clearedResponses.done(function(){ console.log(' clearedResponses done');});
		var clearedQueue     = $.Deferred(); clearedQueue.done(function(){ console.log(' clearedQueue done');});

		fileStore.rebootCache(clearedFiles);
		dbStore.wipe(clearedResponses);
		GopherQueue.wipe(clearedQueue);

		appMessagesController.updateBadge(0);
        if (success && Configuration.get('pin')){
            //if logging out but the contact identifier still exists, get a new session for contact level access
            settings.getSession(Configuration.get('pin'));
		}
		this.terms = {};

        var redir = function(){
			if (logoutRedirect && device.platform == 'Mobile Interface'){
				window.location = logoutRedirect;
			} else {
				$('#home', '#menu').empty(); 			//clear screen, and...
				window.location.hash = '#home'; //...make sure that the app reloads at the start
				window.location.reload(true);
			}
		};
		$.when(clearedFiles, clearedQueue, clearedResponses).done([redir]);
//		setTimeout(redir, 5000); //if some kind of error prevents the logout from completely finishing, reload after 5 seconds
	},
	/**
	 * Check if the user is currently logged in. 
	 * If so, the main menu button says 'Log out' and the logout text is shown
	 * If not, 'Log in' and the login form is shown
	 * Finally, the menu is refreshed to only show the icons available to the user at their current level of authentication.
	 */
    refresh: function(){
		if (!this.initted || !this.refreshable) return; //avoid race conditions and dont bother calling this page until Session.init has run. This should be on window load anyway, and this function will be called at that time.

    	var domain = Configuration.get('clientUrl');
        if (domain && domain.length){
    		this.$content.find('.sessionDomain').val(domain);
    	}
    	if (OCASession.isLoggedIn()) {
    		this.loggedIn = true;
    		this.$menu.find('a').prop('href', '#session').find('.label').text(OCA.getI18n().gettext('Logout')).data('translate', 'Logout');
    		this.$page.find('.login').hide();
    		this.$page.find('.logout').show();
    	} else {
    		this.loggedIn = false;
    		this.$menu.find('.label').text(OCA.getI18n().gettext('Login')).data('translate', 'Login');
    		this.$page.find('.logout, .user, .domain').hide();
    		if (this.domainChecked){
    			this.$page.find('.user').show();
			} else {
				this.$page.find('.domain').show();
				this.$page.find('.sso').hide();
				if (location.protocol.indexOf("http") === 0){
					this.checkDomain(); //mobile interface so the domain is known - check it straight away
				}
			}
    	}
		this.showMenu();
		app.checkLoaded();
    },
	initMenu: function($grid){
		this.$grid = $grid;
		this.showMenu();
	},
	/**
	 * Show menu icons that the user has access to at their current level of authentication (none || mobile pin ('contact') || username and password ('user'))
	 * 
	 * Then filter the menu icons to only show the features they have access to according to the OCA Access Permission settings
	 * Then filter any items not available on this version of OCA Server
	 */
	showMenu: function(){
		var checkAccess;
        if (!this.$grid) return;

		if (OCASession.isLoggedIn()){
			this.$grid.find('.contactVisible').show();

			checkAccess = this.$grid.find('.userVisible, .userAuthVisible').hide();
		} else if (OCASession.getSessionId()){
			this.$grid.find('.contactVisible').show();
			this.$grid.find('.userVisible').hide();

			checkAccess = this.$grid.find('.userAuthVisible').hide();
		} else {
			this.$grid.find('.contactVisible').hide();
			this.$grid.find('.userVisible').hide();
			this.$grid.find('.userAuthVisible').show();
		}

		if (checkAccess){
			checkAccess.each(function(){
				var feature = $(this).attr('data-ng-feature');
				
				var visfeature = feature ? feature.split('_').shift() : null;
				$(this).showIf(!feature || (OCA.checkMenuVisibility(visfeature) && OCA.checkFeature(feature)));
			});
			checkAccess.find('div[data-min-ver]').each(function(i,e){
				$(e).showIf(OCA.versionAtLeast($(e).data('min-ver')));
			});
		}
	},
	/**
	 * If an extra payload comes in for the /session URL, it will be handled here
	 * @param {SessionResponse_APIPayload} extra.payloads[0] The session payload object
	 */
	handleExtraPayload: function(extra){
		if (extra.payloads[0] && extra.payloads[0].StateCode){
            switch (extra.payloads[0].StateCode) {
                case Session.state.RNEW:
                    var id = extra.payloads[0].SessionID;
                    util.log('RNEW SESSION', id);
                    new Gopher({url: '/me/access', dontCheckCache: true, noExtras: true}, function(){
                        console.log('got me access now renew with ' + id);
                        OCASession.renewSession(id);
                    }).run();
                    break;
                case Session.state.SAML:
                    util.log('SAML Reval', extra);
                    if (this.showingSAML || !OCASession.isLoggedIn()) return;

                    this.showingSAML = true;
                    util.infobar(extra.payloads[0].Message, $.proxy(Session.redirectSAML, Session));
                    break;
            }
		}
	}
});
