router.add({
	"#messageTracking": function(type, match, ui, page, e){
		ViewUtil.selector.previousObject = message;
		message.loadTracking();
	},
	"#messageRecipients": function(type, match, ui, page, e){
		ViewUtil.selector.previousObject = message;
		message.listRecipients($(page));
	},
	"#messagePage$": function(type, match, ui, page, e){
		message.updateAll();
	},
	"#messagePage[?]timestamp=(\\d+)": function(type, match, ui, page, e){
		if (ViewUtil.selector.previousObject) {
			ViewUtil.selector.previousObject = null;
			app.checkLoaded();
			return;
		}
		message.getCacheData(match[1]);
	},
	"#messageEmailAttachments": function(type, match, ui, page, e){
		message.updateEmailAttachments($(page));
	},
	"#messageDrafts": function(type, match, ui, page, e){
		ViewUtil.selector.previousObject = message;
		message.getDrafts(page);
		app.checkLoaded();
	},
	"#messageTemplates": function(type, match, ui, page, e){
		ViewUtil.selector.previousObject = message;
		message.getTemplates(page);
		app.checkLoaded();
	},
	"#message": function(){
		app.checkLoaded();
	},
    "#messagePage[?]templateID=(\\d+)": function(type, match, ui, page, e){
		message.updateAll();
		if (ViewUtil.selector.previousObject) {
			ViewUtil.selector.previousObject = null;
			app.checkLoaded();
			return;
		}
		message.getTemplate(match[1]);
    },
	"#messageAcknowledgement": 	function(){ ViewUtil.selector.previousObject = message; }, //preserve context when going into sub-pages of the compose screen
    "#messageSMS": 				function(){ ViewUtil.selector.previousObject = message; },
    "#messageEmail": 			function(){ ViewUtil.selector.previousObject = message; },
    "#messageVoice":			function(){ ViewUtil.selector.previousObject = message; },
    "#messageFax": 				function(){ ViewUtil.selector.previousObject = message; },
});
$(document).on("pageinit", "#messagePage", function (e) {
    message.init($(this));
});
$(document).on("pageinit", "#messageAddRecipients", function (e) {
    message.initAddRecipients($(this));
});
$(document).on("pageinit", "#messageAcknowledgement", function (e) {
    message.initAcknowledgement($(this));
});
$(document).on("pageinit", "#messageTracking", function (e) {
    message.initTracking($(this));
});
$(document).on("pageinit", "#messageSMS", function (e) {
    message.initSMS($(this));
});
$(document).on("pageinit", "#messageEmail", function (e) {
    message.initEmail($(this));
});
$(document).on("pageinit", "#messageEmailAttachments", function (e) {
    message.initEmailAttachments($(this));
});
$(document).on("pageinit", "#messageVoice", function (e) {
    message.initVoice($(this));
});
$(document).on("pageinit", "#messageFax", function (e) {
    message.initFax($(this));
});
$(document).on("pageinit", "#messageVoiceRecording", function (e) {
	console.log('init message voice recording');
    message.initVoiceRecording($(this));
});

var message = $.extend({}, app, {
	MAX_RECIPIENTLIST: 3,
	tmp: {},
	values: {
		Recipients: {},
		SMS: null,
		Email: null,
		Voice: null,
		Fax: null,
		Acknowledgement: 'none',
		Tracking: 'disabled',
		TrackingTimeframe: 120
	},
	labels: {
		Acknowledgement: {
			'none': 'No',
			'ack': 'Yes',
			'ackesc': 'Escalate'
		},
		Tracking: {
			'disabled': 'No',
			'enabled': 'Yes',
			'pollingonly': 'Polling'
		}
	},
    SMSFromAddresses: [],
    EmailFromAddresses: [],
    gotFromAddresses: function(data, extra){
        if (data && data[0]){
            this.SMSFromAddresses = data[0].SMS;
            this.EmailFromAddresses = data[0].Email;
        }
    },
	initAcknowledgement: function(page){
		this.$acknowledgement = page.find('.ui-content .ui-listview');
		this.$acknowledgement.on('click', 'a', function(){
			message.values.Acknowledgement = $(this).data('value');
			message.updateAcknowledgement();
			util.goBack();
		});
		this.updateAcknowledgement();
	},
	updateAcknowledgement: function(){
		message.$acknowledgement.find('span.icon').remove();
		message.$acknowledgement.find("a[data-value='"+message.values.Acknowledgement +"']").prepend(ViewUtil.ocaicon('checkmark'));
		this.updateOptions();
	},
	initTracking: function(page){
		this.$tracking = page.find('.ui-content .ui-listview');
		this.$tracking.on('click', 'a', function(){
			message.values.Tracking = $(this).data('value');
			message.updateTracking();
		});
		
		this.$trackingTimeframe = page.find('#trackingTimeframe');
		this.$trackingTimeframe.on('change', function(e){
			message.values.TrackingTimeframe = $(this).val();
		});
		
		this.$trackingCancel = page.find('#trackingCancel');
		
		this.updateTracking();
	},
	updateTracking: function(){
		message.$tracking.find('span.icon').remove();
		message.$tracking.find("a[data-value='"+message.values.Tracking +"']").prepend(ViewUtil.ocaicon('checkmark'));
		message.$trackingTimeframe.val(message.values.TrackingTimeframe).change();
		this.updateOptions();
	},
	loadTracking: function(){
		var current = JSON.parse(JSON.stringify({
			Tracking: message.values.Tracking,
			TrackingTimeframe: message.values.TrackingTimeframe
		}));
		this.$trackingCancel.off('click').on('click', function(){
			message.values.Tracking = current.Tracking;
			message.values.TrackingTimeframe = current.TrackingTimeframe;
			message.updateTracking();
			util.goBack();
		});
	},
	recipientsSelected: function(data){
		var key, item;
		for (key in data){
			item = data[key];
			if (!item.checked){
				if (this.values.Recipients[key]) {
					if (this.values.Recipients[key].li) this.values.Recipients[key].li.remove();
					delete this.values.Recipients[key];
				}
				delete data[key];
			}
		}
		$.extend(this.values.Recipients, data);
		this.updateRecipients();
	},
	updateRecipients: function(){
		if (!this.$recipients) return;
		var key, item;
		var len = Object.keys(this.values.Recipients).length;
		if (len){
			this.$recipients.find('li.none').hide();
			for (key in this.values.Recipients){
				if (this.$recipients.children('li.recipient').length < message.MAX_RECIPIENTLIST){
					item = this.values.Recipients[key];
					if (!item.li){
						item.li = $("<li class='recipient'/>").text(item.label);
						this.$recipients.prepend(item.li);
					}
				} else {
					break;
				}
			}
			this.$recipients.find('li.more').show().find('span.ui-li-count').text(len + ' total');
		} else {
			this.$recipients.find('li.more').hide();
			this.$recipients.find('li.none').show();
		}
		this.$recipients.listview('refresh');
	},
	listRecipients: function($page){
		var $lv = $page.find('ul');
		$lv.empty();
		var html = "";
		var key;
		for (key in this.values.Recipients){
			html += "<li><a href='#'>" + this.values.Recipients[key].label + "</a><a href='#' class='delete' data-key='"+key+"'>X</a></li>";
		}
		$lv.html(html).listview('refresh');
		var self = this;
		$lv.on('click', 'a.delete', function(){
			var a = $(this);
			var key = a.attr('data-key');
			var item = self.values.Recipients[key];
			if (item && item.li) item.li.remove();
			delete self.values.Recipients[key];
			a.parents('li').remove();
		});
	},	
	updateMethods: function(){
		this.$methods.children().each(function(i, el){
			el = $(el);
			var key = el.attr('data-key');
			if (message.values[key]){
				el.find('span.ui-li-count').replaceWith(ViewUtil.ocaicon('checkmark right'));
			} else {
				el.find('span.icon').replaceWith("<span class='ui-li-count ui-body-inherit'>" + OCA.getI18n().gettext('not set') + "</span>");
			}
		});
	},
	updateOptions: function(){
		message.$options.find('a.tracking span.ui-li-count').text(message.labels.Tracking[message.values.Tracking]);
		message.$options.find('a.acknowledgement span.ui-li-count').text(message.labels.Acknowledgement[message.values.Acknowledgement]);
	},
	updateVoice: function(){
		if (!this.$Voice) return;
		if (this.values.Voice && this.values.Voice.text){
			this.$Voice.find('#voiceText').val(this.values.Voice.text);
		} else {
			this.$Voice.find('#voiceText').val(null);
		}
		this.$Voice.find('li').each(function(i, el){
			el = $(el);
			el.find('span.icon').remove();
			var key = el.attr('data-key');
			if (message.values.Voice && message.values.Voice.method == key){
				el.find('a').prepend(ViewUtil.ocaicon('checkmark'));
			}
		});
	},
	updateFax: function(){
		if (!this.$Fax) return;
		this.$Fax.find('li').each(function(i, el){
			el = $(el);
			el.find('span.icon').remove();
			var key = el.attr('data-key');
			if (message.values.Fax && message.values.Fax.method == key){
				el.find('a').prepend(ViewUtil.ocaicon('checkmark'));
			}
		});
	},
	initSMS: function(page){
		this.$SMS = page.find('.ui-content');
        var $from = page.find('#SMSFrom').empty();
        for (var f = 0; f < this.SMSFromAddresses.length; f++){
            $from.append($("<option value='" + this.SMSFromAddresses[f].URL + "' />").text(this.SMSFromAddresses[f].Name));
        }
        $from.selectmenu("refresh", true);
        if ($from.children().length === 0) $from.parent().parent().hide(); //double nested div

        this.updateSMS();
		page.find('#SMSDiscard').on('click', function(){
			message.values.SMS = null;
			message.updateMethods();
			util.goBack();
		});
		page.find('#SMSOK').on('click', function(){
			message.values.SMS = {
				From: message.$SMS.find('#SMSFrom').val(),
				Body: message.$SMS.find('#SMSBody').val(),
				Flash: parseInt(message.$SMS.find('#SMSFlash').val(), 10)
			};
			if (!message.values.SMS.Body) message.values.SMS = null; //dont set a blank sms as valid
			message.updateMethods();
			util.goBack();
		});
		page.find('#SMSCancel').on('click', function(){
			if (message.values.SMS){
				message.$SMS.find('#SMSFrom').val(message.values.SMS.From).change();
				message.$SMS.find('#SMSBody').val(message.values.SMS.Body);
				message.$SMS.find('#SMSFlash').val(message.values.SMS.Flash).change();
			} else {
				message.$SMS.find('#SMSBody').val(null);
			}
			message.updateMethods();
			util.goBack();
		});
	},
	updateSMS: function(){
		if (message.$SMS) {
			if(message.values.SMS){
				message.$SMS.find('#SMSBody').val(message.values.SMS.Body);
                message.$SMS.find('#SMSFrom').val(message.values.SMS.From);
			} else {
				message.$SMS.find('#SMSBody').val(null);
                message.$SMS.find('#SMSFrom').val(null);
			}
            message.$SMS.find('#SMSFrom').selectmenu('refresh');
		}
	},
	initEmail: function(page){
		this.$Email = page.find('.ui-content');
		var useCKEditor = (device.platform != 'Win32NT'); //disable for WP8 devices

		if (useCKEditor) {
			message.emailInput = new CKEditorInput({});
			if (device.platform == 'iOS') {
				//iOS has a weird and drastic rendering bug when the page height is less than the window height
				//increase the email body input size to fill the page
				message.emailInput.config.height = 200 + $(window).height() - 570; //570 is approx height of all elements normally, including header and footer
			}
			message.emailInput.enhance(message.$Email.find('#emailBody')[0]);
		} else {
			message.emailInput = message.$Email.find('#emailBody');
		}
        var $from = page.find('#emailFrom').empty();
        for (var f = 0; f < this.EmailFromAddresses.length; f++){
            $from.append($("<option value='" + this.EmailFromAddresses[f].URL + "' />").text(this.EmailFromAddresses[f].Name));
        }
        $from.selectmenu("refresh", true);
        if ($from.children().length === 0) $from.parent().parent().hide(); //double nested div

		this.tmp.EmailAttachments = {};
		this.updateEmail();
		
		page.find('#EmailDiscard').on('click', function(){
			message.values.Email = null;
			message.updateMethods();
			message.emailInput.val(null);
			message.$Email.find('#emailSubject').val(null);
			message.tmp.EmailAttachments = {};
			message.updateEmailAttachments();
			util.goBack();
		});
		page.find('#EmailOK').on('click', function(){
			message.values.Email = {
				From: message.$Email.find('#emailFrom').val(),
				Body: message.emailInput.val(),
				Subject: message.$Email.find('#emailSubject').val(),
				Attachments: message.tmp.EmailAttachments
			};
			message.updateMethods();
			util.goBack();
		});
		page.find('#EmailCancel').on('click', function(){
			message.updateEmail();
			message.updateMethods();
			util.goBack();
		});
	},
	updateEmail: function(){
		if (message.$Email) {
			if (message.values.Email){
                message.$Email.find('#emailFrom').val(message.values.Email.From);
				message.emailInput.val(message.values.Email.Body);
				message.$Email.find('#emailSubject').val(message.values.Email.Subject);
				message.tmp.EmailAttachments = message.values.Email.Attachments;
			} else {
                message.$Email.find('#emailFrom').val(null);
				message.emailInput.val(null);
				message.$Email.find('#emailSubject').val(null);
			}
            message.$Email.find('#emailFrom').selectmenu('refresh');
		}
		message.updateEmailAttachments();
	},
	initEmailAttachments: function($page){
		$page.find('#emailAttachDoc').on('click', function(){
			ViewUtil.selector.start({
				callbackOK: $.proxy(message.addEmailAttachmentDoc, message),
				data: message.tmp.EmailAttachments
			});
		});
		$page.find('#emailAttachMedia').on('click', function(){
			FileApp.mediaSelectCallback = $.proxy(message.addEmailAttachmentMedia, message);
		});
		var self = this;
		$page.find('ul.ui-listview').on('click', 'a.delete', function(){
			var a = $(this);
			var key = a.attr('data-key');
			var item = self.tmp.EmailAttachments[key];
			item.li.remove();
			delete self.tmp.EmailAttachments[key];
			self.updateEmailAttachments();
		});
		$page.find('li.attach').showIf(device.platform != "Mobile Interface");
	},
	updateEmailAttachments: function($page){
		if ($page){
			message.$EmailAttachments = $page;
		}
		if (message.$Email){
			var count = message.$Email.find('ul.attachments span.ui-li-count');
			var len = message.tmp.EmailAttachments ? Object.keys(message.tmp.EmailAttachments).length : 0;
			if (len){
				count.text(len);
			} else {
				count.text('none');
			}
		}
		if (message.$EmailAttachments){
			var $lv = message.$EmailAttachments.find('ul.ui-listview');
			if (len){
				for (var key in this.tmp.EmailAttachments){
					var item = this.tmp.EmailAttachments[key];
					if (!item.li){
						item.li = $("<li class='attachment'><a href='#'>" + item.label + "</a><a href='#' class='delete' data-key='"+key+"'>X</a></li>");
						$lv.prepend(item.li);
					}
				}
				$lv.find('li.none').hide();
			} else {
				$lv.find('li.attachment').remove();
				$lv.find('li.none').show();
			}
			$lv.listview('refresh');
		}
	},
	addEmailAttachmentMedia: function(url, name){
		var key = encodeURI(url);
		if (!this.tmp.EmailAttachments) this.tmp.EmailAttachments = {};
		this.tmp.EmailAttachments[key] = {
			path: url,
			label: name,
			checked: true
		}
	},
	addEmailAttachmentDoc: function(data){
		var key, item;
		if (!this.tmp.EmailAttachments) this.tmp.EmailAttachments = {};
		for (key in data){
			item = data[key];
			if (!item.checked){
				if (this.tmp.EmailAttachments[key]) {
					if (this.tmp.EmailAttachments[key].li) this.tmp.EmailAttachments[key].li.remove();
					delete this.tmp.EmailAttachments[key];
				}
			} else {
				this.tmp.EmailAttachments[key] = item;
			}
		}
//		this.updateEmailAttachments();
	},
	chooseVoiceDocument: function(data){
		if (!message.values.Voice) message.values.Voice = {};
		message.values.Voice.method = 'document';
		console.log(message.values.Voice);
		for (var key in data){ //should only be one, actually
			message.values.Voice.document = data[key]
		}
		this.updateVoice();
	},
	initVoice: function(page){
		this.$Voice = page.find('.ui-content');
		page.find('#voiceTextMethod').on('click', function(){
			if (!message.values.Voice) message.values.Voice = {};
			message.values.Voice.method = 'text';
			message.updateVoice();
		});
		page.find('#voiceDocumentMethod').on('click', function(){
			ViewUtil.selector.start({
				callbackOK: $.proxy(message.chooseVoiceDocument, message),
				single: true
			});
		});
		page.find('#voiceDiscard').on('click', function(){
			message.values.Voice = null;
			message.updateMethods();
			util.goBack();
		});
		page.find('#voiceOK').on('click', function(){
			var text = message.$Voice.find('#voiceText').val();
			if (text){
				if (!message.values.Voice) message.values.Voice = {};
				message.values.Voice.text = text;
			}
			
			message.updateMethods();
			util.goBack();
		});
		page.find('#voiceCancel').on('click', function(){
			message.updateVoice();
			message.updateMethods();
			util.goBack();
		});
		page.find('.recording').showIf(device.platform != 'Mobile Interface' && device.platform != 'Android');
	},
	chooseFaxDocument: function(data){
		if (!message.values.Fax) message.values.Fax = {};
		message.values.Fax.method = 'document';
		console.log(message.values.Fax);
		for (var key in data){ //should only be one, actually
			message.values.Fax.document = data[key]
		}
		this.updateFax();
	},
	initFax: function(page){
		this.$Fax = page.find('.ui-content');
		page.find('#faxDocumentMethod').on('click', function(){
			ViewUtil.selector.start({
				callbackOK: $.proxy(message.chooseFaxDocument, message),
				single: true
			});
		});
		page.find('#faxDiscard').on('click', function(){
			message.values.Fax = null;
			message.updateMethods();
			util.goBack();
		});
		page.find('#faxOK').on('click', function(){
			message.updateMethods();
			util.goBack();
		});
		page.find('#faxCancel').on('click', function(){
			message.updateMethods();
			util.goBack();
		});
	},
	initVoiceRecording: function(page){
		this.$VoiceRecording = page;
		var replay = page.find('#voiceRecordReplay').button();
		page.find("#voiceRecordStart").button().button('enable').on('click', function(){
			replay.button('disable');
			Session.preserveDB = true;
			navigator.device.capture.captureAudio(
				function (mediaFiles) {
					var i, path, len, type;
					for (i = 0, len = mediaFiles.length; i < len; i += 1) {
						path = mediaFiles[i].localURL;
						// do something interesting with the file
                        if (path){
                            message.gotVoice(path);
                        }
					}

				}, 
				log.e, 
				{limit: 1}
			);
		});

		replay.on('click', function(e){
			var media = new Media(message.tmp.voiceRecording, function(){
				media.release(); //play completed, release the media
			});
			media.play();
		});
		if (message.values.Voice && message.values.Voice.recording){
			replay.button('enable');
		} else {
			replay.button('disable');
		}
		
		page.find('#voiceRecordOK').on('click', function(){
			if (message.tmp.voiceRecording){
				if (!message.values.Voice) message.values.Voice = {};
				
				message.values.Voice.method = 'recording';
				message.values.Voice.recording = message.tmp.voiceRecording;
				message.tmp.voiceRecording = null;
			}
			message.updateVoice();
			message.updateMethods();
			util.goBack();
		});
		page.find('#voiceRecordCancel').on('click', function(){
			message.tmp.voiceRecording = null;
			message.updateVoice();
			message.updateMethods();
			util.goBack();
		});
	},
	gotVoice: function(path){
		message.tmp.voiceRecording = path;
		this.$VoiceRecording.find('#voiceRecordReplay').button('enable');
	},
    init: function(page) {
        this.page = page;
        this.content = this.page.find('.ui-content');
		
		this.$recipients = this.content.find('ul.recipients');
		
		this.$methods = this.content.find('ul.methods');
		this.updateMethods();
		
		this.$options = this.content.find('.options');
		var fake = {listview: this.$options};
		this.values.ReadPolicyURL = {
			Options: OCA.policyOptions, 
			Label: OCA.getI18n().gettext("Read Access Level")
		};
		this.values.WritePolicyURL = {
			Options: OCA.policyOptions, 
			Label: OCA.getI18n().gettext("Write Access Level")
		};
		TypeEdit.prototype.optRender.call(fake, this.values.ReadPolicyURL, null);
		TypeEdit.prototype.optRender.call(fake, this.values.WritePolicyURL, null);

		if (OCA.IncidentManager){
			this.addEventsSLMC(false);
		}
		
		this.$options.enhanceWithin().listview('refresh');
		
		this.page.find('#messageSend').on('click', $.proxy(this.sendMessage, this));
		this.page.find('#saveDraft').on('click', $.proxy(this.savePrompt, this));
//		this.page.find('#messageSave').on('click', $.proxy(this.saveMessage, this));
		this.page.find('#messageDiscard').on('click', $.proxy(this.discardMessage, this));

		var $confirmClearRecipients = this.page.find('#confirmClearRecipients');
		var $confirmClearMessage = this.page.find('#confirmClearMessage');
		this.page.find('#messageClearRecipients').on('click', $.proxy(this.clearRecipients, this, $confirmClearRecipients));
		this.page.find('#messageClearMethods').on('click', $.proxy(this.clearMethods, this, $confirmClearMessage));
		
		$(window).on('loggedIn', function(){
			message.clearMessage();
			message.reset();	//This is here really just to reset the read / write access level options and show / hide the Events SLMC
		});

        var $mm = this.page.find('#messageMore');
        var $confirmDiscard = this.page.find('#confirmDiscard');
        $mm.find('a.discard').on('click', function(){
            $mm.popup('close');
            $confirmDiscard.popup('open');
        });

        $mm.find('a.clear.recipients').on('click', function(){
            $mm.popup('close');
            $confirmClearRecipients.popup('open');
        });
        $mm.find('a.clear.message').on('click', function(){
            $mm.popup('close');
            $confirmClearMessage.popup('open');
        });
    },
	addEventsSLMC: function(refreshListView){
		var relfake = {listview:this.$options,prepend:true};

		this.values.Events = {
			Label:OCA.getI18n().gettext('Events')
		};

		var Events = [];
		var pe = OCA.getPrimaryEME();
		if (pe){
			Events.push({url:pe.url,label:pe.label});
		}

		TypeEdit.prototype.slmcRender.call(relfake,this.values.Events,Events,'emeTreeView');

		if (refreshListView === undefined || refreshListView){
			this.$options.enhanceWithin().listview('refresh');
		}
	},
	reset: function(){
		if (this.values.ReadPolicyURL && this.values.ReadPolicyURL.Input){
			this.values.ReadPolicyURL.Options = OCA.policyOptions;
			TypeEdit.renderOptions(this.values.ReadPolicyURL,this.values.ReadPolicyURL.Input);
			this.values.ReadPolicyURL.Input.val(OCA.policyOptions[0][0]).change();
		}
		if (this.values.WritePolicyURL && this.values.WritePolicyURL.Input){
			this.values.WritePolicyURL.Options = OCA.policyOptions;
			TypeEdit.renderOptions(this.values.WritePolicyURL,this.values.WritePolicyURL.Input);
			this.values.WritePolicyURL.Input.val(OCA.policyOptions[0][0]).change();
		}

		if (OCA.IncidentManager){
			//Logged in from a non IM system to an IM system, add the Events SLMC
			if (! this.values.Events){
				this.addEventsSLMC();
			}
		}else{
			//Logged in from an IM system to a non IM system, remove the Events SLMC
			if (this.values.Events){
				this.values.Events.Input.detach();
				delete this.values.Events;
			}
		}

	},
	initAddRecipients: function(page){
		var $page = $(page);
		$page.find('a').on('click', function(){
			ViewUtil.selector.start({
				callbackOK: $.proxy(message.recipientsSelected, message),
				data: message.values.Recipients || {},
				extraBack: 1,
				previousObject: this
			});
		});
	},
	sendTo: function(type, id, label){
		this.clearMessage();
		this.values.Recipients[type + "-" + id] = {
			checked: true,
			id: id,
			label: label
		};
		this.updateRecipients();
	},
	sendToMany: function(recipients){
		this.clearMessage();
		for (var r = 0; r < recipients.length; r++){
			var recipient = recipients[r];
			this.values.Recipients[recipient.key] = {
				checked: true,
				id: recipient.id,
				label: recipient.label
			};
		}
		this.updateRecipients();
	},
	setSMS: function(body, flash, from){
		this.values.SMS = {Body: body};
		if (flash) this.values.SMS.Flash = "1";
        if (from) this.values.SMS.From = from;
	},
	setEmail: function(subject, body, attachments, from){
		this.values.Email = {
			Subject: subject
		};
		if (body) {
			this.values.Email.Body = body;
		}
		if (attachments){
			this.values.Email.Attachments = {};
			for (var a = 0; a < attachments.length; a++){
				var att = attachments[a];
				this.values.Email.Attachments['url-' + att.URL] = {
					label: att.Name,
					checked: true,
					id: 'url' + a
				};
			}
		}
        if (from){
            this.values.Email.From = from;
        }
	},
	setVoice: function(text, url){
		if (text){
			this.values.Voice = {
				method: 'text',
				text: text
			};
		} else if (url) {
			this.values.Voice = {
				method: 'document',
				document: url
			};
		}
	},
	setFax: function(url){
		if (url){
			this.values.Fax.method = 'document';
			this.values.Fax.document = url;
		}
	},
	getCacheData: function(timestamp){
		if (this.timestamp == timestamp){
			//this has already been loaded, so dont load it again
			return;
		}
		//try 'sent' first
		var cache = new Gopher('/outboundcomms/sent').getPOSTCache(timestamp);
		if (!cache){
			cache = new Gopher('/outboundcomms/drafts').getPOSTCache(timestamp);
		}
		var data = JSON.parse(cache.ajax.data);
		this.loadFromData(data);
		cache.info.currentlyEditing = true;
		this.timestamp = timestamp;
	},
	sendMessage: function(){
		if (this.submitting) return;	//stop double clicks double submitting
		this.submitting = true;
		setTimeout(function(){ message.submitting = false}, 1000);

		var comm = this.getComm();
		if (JSON.stringify(comm.Recipients) == JSON.stringify({})){
			$('#confirmSendMessage').popup('close');
			setTimeout(function(){
				util.alertDialog(OCA.getI18n().gettext('Message not sent. No recipients have been selected'));
			}, 100);
			message.submitting = false;
			return;
		}
		if (!comm.ContentParts.length){
			$('#confirmSendMessage').popup('close');
			setTimeout(function(){
				util.alertDialog(OCA.getI18n().gettext('Message not sent. No communication methods have been selected'));
			}, 100);
			message.submitting = false;
			return;
		}
        var url = '/outboundcomms/sent';
		this.postMessage(url, comm);
        new Gopher(url).clearCache();
	},
	saveMessage: function(){
		if (this.submitting) return;	//stop double clicks double submitting
		this.submitting = true;
		setTimeout(function(){ message.submitting = false}, 1000);
		var comm = this.getComm();
		if (JSON.stringify(comm.Recipients) == JSON.stringify({}) && !comm.ContentParts.length){
			util.alertDialog(OCA.getI18n().gettext('There is no content to save as a draft message'));
			message.submitting = false;
			return;
		}
		comm.Name = this.currentDraftName;
		var url = this.currentDraftURL 
			? this.currentDraftURL
			: '/outboundcomms/drafts';
		this.postMessage(url, comm);
	},
	postMessage: function(url, comm){
		$('#confirmSendMessage').popup('close');
		setTimeout(function(){
			new MessageSubmitter(url, comm, this.timestamp, $.proxy(this.postedMessage, this), $.proxy(this.postedFail, this));
			message.page.find('.ui-btn-active').removeClass('ui-btn-active');
		}.bind(this), 50);
	},
	savePrompt: function(){
		util.promptDialog(
			OCA.getI18n().gettext('Enter a name for your message'),
			$.proxy(this.savedPrompt, this),
			'Save Draft',
			['Save', 'Cancel'],
			this.currentDraftName || ''
		);
	},
	savedPrompt: function(results){
		if (results.buttonIndex === 1){
			this.currentDraftName = results.input1;
			this.saveMessage();
		}
	},
	postedMessage: function(payloads, data, messageURL){
		if (data && data.status == 202 && data.notices.length && messageURL){
			var message = data.notices.join("<br />");
			util.confirmDialog(message, $.proxy(this.messageWarningCallback, this, messageURL), OCA.getI18n().gettext('Validating communication'));
		} else {
			//assume happiest of cases
			this.discardMessage();
		}
		app.checkLoaded();
	},
	messageWarningCallback: function(messageURL, button){
		if (button === 1) {
			new Gopher({url: messageURL}, $.proxy(this.postedMessage, this), $.proxy(this.postedFail, this)).put();
		} else {
			util.infobar(OCA.getI18n().gettext('Your communication was cancelled and did not send'));
			new Gopher({url: messageURL, backgroundMode: true}).sendDelete(false);
		}
	},
    postedFail: function(status, response){
		util.infobar(OCA.getI18n().gettext('Your communication had errors and did not send'));
		util.handleResponseExtras(response); //MessageSubmitter has told Gopher not to auto-process extras, so do it here.
    },
	clearMessage: function(){
		this.clearRecipients();
		this.clearMethods();
		this.timestamp = null;
		this.currentDraftURL = null;
		this.currentDraftName = null;

		if (OCA.IncidentManager && this.values.Events){
			var pe = OCA.getPrimaryEME();
			if (pe){
				var Events = [];
				Events.push({url:pe.url,label:pe.label});
				this.values.Events.Input.val(Events).change();
			} else {
				this.values.Events.Input.val([]).change();
			}
		}
	},
	
	clearRecipients: function($popup){
		this.values.Recipients = {};
		if (this.$recipients) this.$recipients.find('li.recipient').remove();
		this.updateRecipients();
		if ($popup) $popup.popup('close');
	},
	clearMethods: function($popup){
		this.values.SMS = null;
		this.values.Email = null;
		this.tmp.EmailAttachments = {};
		this.values.Voice = null;
		this.tmp.voiceRecording = null;
		this.values.Fax = null;
		this.values.Acknowledgement = 'none';
		this.values.Tracking = 'disabled';
		this.values.TrackingTimeframe = 120;
		this.updateAll();
		if ($popup) $popup.popup('close');
	},
	discardMessage: function(){
		this.clearMessage();
		$("body").pagecontainer("change", '#home');
	},
	updateAll: function(){
		if (!this.content) return;
		this.updateRecipients();
		this.updateMethods();
		this.updateOptions();
		this.updateSMS();
		this.updateEmail();
		this.updateVoice();
		this.updateFax();
	},
	getComm: function(){
		var comm = {}, key, bits;
		comm.Recipients = {};
		for (key in this.values.Recipients){
			var recipient = this.values.Recipients[key];
			bits = key.split("-");	//0 type (contact/contactgroupTree) 1 ID
			var url;
			switch (bits[0]){
				case 'contact':
					url = Configuration.getAPIPath() + '/contact/' + bits[1];
					break;
				case 'contactgroup':
					url = Configuration.getAPIPath() + '/contactgroup/' + bits[1] + '/contacts';
					break;
				case 'teamrole':
				case 'resourcestructurenode':
					url = Configuration.getAPIPath() + '/' + bits[0] + '/' + bits[1] + '/currentallocatees';
					break;
				case 'adhoc':
					url = key.replace('adhoc-', ''); //the email might actually contain hyphens, so use the full key as the address
					break;
				default:
					console.error('INVALID RECIPIENT KEY: ' + key);
					continue;
			}
			comm.Recipients[url] = recipient.label;
		}
		comm.AckMode = this.values.Acknowledgement;
		comm.PollMode = this.values.Tracking;
		comm.PollWindowMins = this.values.TrackingTime;
		comm.ReadPolicyURL = this.values.ReadPolicyURL.Input.val();
		comm.WritePolicyURL = this.values.WritePolicyURL.Input.val();

		if (OCA.IncidentManager && this.values.Events){
			comm.EventURLs = [];
			var ev = this.values.Events.Input.val();
			for (var i = 0; i < ev.length; i++){
				comm.EventURLs.push(ev[i].url);
			}
		}
		
		comm.ContentParts = [];
		if (this.values.SMS){
			var sms = {
				Type: 'SMS',
				TextContent: this.values.SMS.Body,
				IsFlash: this.values.SMS.Flash,
                FromAddressURL: this.values.SMS.From
			};
			comm.ContentParts.push(sms);
		}
		if (this.values.Email){
			var email = {
				Type: 'Email',
				Subject: this.values.Email.Subject,
				HTMLContent: this.values.Email.Body,
                FromAddressURL: this.values.Email.From,
				Format: 'both',
				AttachmentURLs: [],
				AttachmentData: []
			};
			for (key in this.values.Email.Attachments){
				bits = key.split("-");	//0 type (contact/contactgroupTree) 1 ID
				if (bits[0] == 'document'){
					email.AttachmentURLs.push(Configuration.getAPIPath() + '/document/' + bits[1]);
					email.AttachmentData.push({
						key: key,
						label: this.values.Email.Attachments[key].label
					});
				} else if (bits[0] == 'url'){
					email.AttachmentURLs.push(bits[1]);
					email.AttachmentData.push({
						key: key,
						label: this.values.Email.Attachments[key].label
					});
				} else {
					//FILE UPLOAD
					var file = this.values.Email.Attachments[key];
					email.AttachmentData.push({
						key: key,
						label: file.label,
						path: file.path
					});
				}
			}
			comm.ContentParts.push(email);
		}
		if (this.values.Voice){
			var voice = {Type: 'Voice'};
			if (this.values.Voice.method == 'text'){
				voice.TextContent = this.values.Voice.text;
			} else if (this.values.Voice.method == 'document'){
				if (this.values.Voice.document.id){
					voice.ContentURL = Configuration.getAPIPath() + '/document/' + this.values.Voice.document.id;
				} else {
					voice.ContentURL = this.values.Voice.document; //if this is an option populated directly with an URL
				}
			} else {
				voice.ContentFile = this.values.Voice.recording;
			}
			comm.ContentParts.push(voice);
		}
		if (this.values.Fax){
			var fax = {Type: 'Fax'};
			if (this.values.Fax.method == 'document'){
				if (this.values.Fax.document.id){
					fax.ContentURL = Configuration.getAPIPath() + '/document/' + this.values.Fax.document.id;
				} else {
					fax.ContentURL = this.values.Fax.document; //if this is an option populated directly with an URL
				}
			}
			comm.ContentParts.push(fax);
		}
		return comm;
	},
	getDrafts: function(page){
		var lv = $(page).find('ul').empty();
		new Gopher('/outboundcomms/drafts', $.proxy(this.gotTemplates, this, lv, true)).run();
	},
	getTemplates: function(page){
		var lv = $(page).find('ul').empty();
		new Gopher('/outboundcomms/templates', $.proxy(this.gotTemplates, this, lv, false)).run();
	},
	gotTemplates: function(lv, draftMode, data){
		for (var d = 0; d < data.length; d++){
			var name = data[d].Name ? data[d].Name : 'Untitled';
			lv.append("<li><a href='#' data-url='" + data[d].URL+ "'>" + name + "</a></li>");
		}
		lv.off('click').on('click', 'a', function(){
			var url = $(this).attr('data-url');
			new Gopher(url, $.proxy(message.loadFromTemplate, message, draftMode ? url : null)).run();
			ViewUtil.selector.previousObject = null;
			util.goBack();
		});
		lv.listview('refresh');
		app.checkLoaded();
	},
	getTemplate: function(templateID){
		var templateURL = "/outboundcomm/" + templateID;
		new Gopher(templateURL, $.proxy(message.loadFromTemplate, message, null)).run();
	},
	loadFromTemplate: function(url, data){
		this.loadFromData(data);
		if (url){
			this.currentDraftURL = url;
		}
	},
	setRecipients: function(data){
		this.clearMessage();
		this.loadRecipientData(data);
		this.updateRecipients();
	},
	loadRecipientData: function(data){
		var recipient;
		
		if (data.RecipientStatuses && data.RecipientStatuses.length){
			for (var s = 0; s < data.RecipientStatuses.length; s++){
				recipient = data.RecipientStatuses[s];
				var bits = recipient.URL.split("/");
				var id = bits.pop();
				var type = bits.pop();
				this.values.Recipients[type + "-" + id] = {
					checked: true,
					id: id,
					label: recipient.Name
				};
			}
		} else if (data.Recipients){
			for (var url in data.Recipients){
				var match = url.match(/\/api\/v\d\/(\w+)\/(\d+)/);	//match 1 = type, match 2 = ID
				if (match){
					this.values.Recipients[match[1] + "-" + match[2]] = {
						checked: true,
						id: match[2],
						label: data.Recipients[url]
					};
				} else if (url.indexOf('@') !== -1 || url.indexOf('+') !== -1){ //ad hoc address
					this.values.Recipients["adhoc-" + url] = {
						checked: true,
						id: url,
						label: data.Recipients[url]
					};
				}

			}
		}
	},
	loadFromData: function(data){
		this.clearMessage();
		if (data && data[0]) data = data[0];
		this.loadRecipientData(data);
		this.loadMessageData(data);
		this.updateAll();
	}, 
	loadMessageData: function(data){
		var p, a, att;
		for (p = 0; p < data.ContentParts.length; p++){
			var part = data.ContentParts[p];
			switch (part.Type){
				case "Email":
					var useCKEditor = (device.platform != 'Win32NT'); //disable for WP8 devices
					var content = useCKEditor ? part.HTMLContent : part.TextContent;
					this.setEmail(part.Subject, content, null, part.FromAddressURL);
					if (part.AttachmentData){
						this.values.Email.Attachments = {};
						for (a = 0; a < part.AttachmentData.length; a++){
							att = part.AttachmentData[a];
							this.values.Email.Attachments[att.key] = att;
						}
					} else if (part.Attachments && part.Attachments.length){
						this.values.Email.Attachments = {};
						for (a = 0; a < part.Attachments.length; a++){
							att = part.Attachments[a];
							this.values.Email.Attachments['url-' + att.URL] = {
								label: att.Name,
								checked: true,
								id: 'url' + a
							};
						}
					}
					break;
				case "SMS":
					this.setSMS(part.TextContent, part.IsFlash, part.FromAddressURL);
					break;
				case 'Voice':
					this.setVoice(part.TextContent, part.ContentURL, part.ContentFile);
					break;
				case 'Fax':
					this.setFax(part.ContentURL);
					break;
			}
		}
		this.values.Acknowledgement = data.AckMode;
		this.values.Tracking = data.PollMode;
		this.values.TrackingTime = data.PollWindowMins;
		if (this.values.ReadPolicyURL.Input)  this.values.ReadPolicyURL.Input.val(data.ReadPolicyURL).change();
		if (this.values.WritePolicyURL.Input) this.values.WritePolicyURL.Input.val(data.WritePolicyURL).change();
		
		if (OCA.IncidentManager && this.values.Events && this.values.Events.Input){
			var Events = [];

			if (data.Events){
				for (var url in data.Events){
					Events.push({url:url,label:data.Events[url]});
				}
			}

			this.values.Events.Input.val(Events).change();
		}
		if (data.Name){
			this.currentDraftName = data.Name;
		}
	}
});
function MessageSubmitter(url, comm, timestamp, callbackOK, callbackFail, resubmission){
	this.ATTACH_URL = '/outboundcomms/tempattachments';
	this.requests = 0;
	this.url = url;
	this.comm = comm;
	this.timestamp = timestamp;
	this.callbackOK = callbackOK;
	this.callbackFail = callbackFail;
	this.resubmission = resubmission;
	
	this.processComm();
	this.submit();
}
MessageSubmitter.prototype.processComm = function(){
	for (var p = 0; p < this.comm.ContentParts.length; p++){
		switch (this.comm.ContentParts[p].Type){
			case "Email":
				var email = this.comm.ContentParts[p]
				for (var a = 0; a < email.AttachmentData.length; a++){
					var att = email.AttachmentData[a];
					if (att.path){
						this.requests++;
						new Gopher(
							{url: this.ATTACH_URL, data: att.path, backgroundMode: this.resubmission},
							$.proxy(this.addEmailAttachment, this, email, att.path),
							$.proxy(this.requestError, this)
						).uploadFile(false);
					}
				}
				break;
			case "Voice":
				var voice = this.comm.ContentParts[p];
				if (voice.ContentFile){
					this.requests++;
					new Gopher(
						{url: this.ATTACH_URL, data: voice.ContentFile, backgroundMode: this.resubmission},
						$.proxy(this.addVoice, this, voice, voice.ContentFile),
						$.proxy(this.requestError, this)
					).uploadFile(false);
				}
				break;
			case "Fax":
				var fax   = this.comm.ContentParts[p];
				break;
		}
	}
}
MessageSubmitter.prototype.requestError = function(xhr, error){
	this.requests--;
	if (this.discarded)		return;
	this.discarded = true;
	
	if (xhr == "timeout" || error == "timeout" || (xhr && xhr.http_status === null)) {
		if (!this.resubmission){
			if (this.timestamp){
				GopherQueue.remove('POST', Configuration.getAPIUrl() + this.url, this.timestamp);
			}
			
			var hash = util.getHash();
			if (hash.indexOf('timestamp') != -1) hash = hash.substr(0, hash.indexOf('timestamp') - 1); //if this is re-editing something in the post cache, remove old timestamp

			var retryData = {
				pageHash: hash,
				url: this.url,
				desc: 'Outbound communication',
				date: new Date(),
				resubmitter: 'MessageResubmitter'
			};

			var ajaxParams = {
				url: Configuration.getAPIUrl() + this.url,
				data: JSON.stringify(this.comm),
				method: 'POST'
			};

			console.log('adding to GopherQ')
			GopherQueue.add(ajaxParams, retryData);
			
			this.callbackOK();	//comm has been added to GopherQ. Pretend everything is okay.
			return;
		}
	}
	this.callbackFail(xhr);
}

MessageSubmitter.prototype.addEmailAttachment = function(email, cleanupPath, data){
	if (!data || !data[0] || !data[0].URL) return; //if offline, might be called with no data - dont process
	email.AttachmentURLs.push(data[0].URL);
	this.requests--;
	this.submit();
	fileStore.clearFiles([cleanupPath]);
}

MessageSubmitter.prototype.addVoice = function(voice, cleanupPath, data){
	if (!data || !data[0] || !data[0].URL) return; //if offline, might be called with no data - dont process
	voice.ContentURL = data[0].URL;
	this.requests--;
	this.submit();
	fileStore.clearFiles([cleanupPath]);
}

MessageSubmitter.prototype.addFax = function(fax, data){
	fax.ContentURL = data[0].URL;
	this.requests--;
	this.submit();
}

MessageSubmitter.prototype.submit = function(){
	if (this.requests != 0) return;
	if (this.submitting)	return;
	if (this.discarded)		return;
	this.submitting = true;
	var gopher = new Gopher({
			url:			this.url, 
			data:			this.comm,
			resubmitter:	'MessageResubmitter',
			desc:			'Outbound communication',
			backgroundMode: this.resubmission,
			oldTimestamp:	this.timestamp,
			noExtras:		true
		},
		this.callbackOK,
		this.callbackFail
	);
	if (this.url.match(/\/api\/v\d\/outboundcomm\/\d+/)){
		gopher.put(this.resubmission != true);
	} else {
		gopher.post(this.resubmission != true);
	}
	app.checkLoaded();
}

/**
 * Extend Resubmitter for use with messages
 * @see Resubmitter
 */
function MessageResubmitter(cache){
	this.init(cache);
	this.run();
}
MessageResubmitter.prototype = new Resubmitter;
MessageResubmitter.prototype.constructor = MessageResubmitter;
MessageResubmitter.prototype.run = function(){
	new MessageSubmitter(this.url, this.data, null, $.proxy(this.success, this), $.proxy(this.failure, this), true);
}
