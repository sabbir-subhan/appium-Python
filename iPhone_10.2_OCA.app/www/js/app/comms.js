router.add({
	"#sentcommView[?]id=(\\d+)": function(type, match, ui, page, e){
		comms.sentView(match[1], page);
	},
	"#sentitemView[?]method=(\\w+)": function(type, match, ui, page, e){
		comms.sentitemView(match[1], page);
	},
	'#sentStatus[?]status=(\\w+)': function(type, match, ui, page, e){
		console.log('sentstatus');
		comms.sentStatusView(match[1], page);
	},
    '#sentComms': function(){
        comms.getMessages();
    }
});
$(document).on("pageinit", "#sentComms", function(e){
    comms.init($(this));
});
var comms = $.extend({}, app, {
	init: function(page){
		this.page = page;
        this.content = this.page.find('.ui-content');
		this.$messages = this.content.find('ul');
		
		this.content.find('#sentSearch').keypress(function(e){
			if (e.which == 13){
				comms.getMessages($(this).val());
			}
		}).on('change', function(e){
			if ($(this).val() == ''){
				comms.getMessages();
			}
		});
		
		this.buildStatusList();
	},
	getMessages: function(query){
		var url = '/outboundcomms/sent';
		if (query){
			url += '?search=' + encodeURIComponent(query);
		}
        this.content.find('.ui-listview.extra-data').remove();
        $(window).off('scroll.listview'); //remove pagination handlers
		new Gopher(url, $.proxy(this.gotMessages, this)).run();
	},
	gotMessages: function(data, extra){
		ViewUtil.applyTemplate(this.$messages, data, 'sentLV', extra.nextPageURL);
		this.checkLoaded();
	},
	sentView: function(id, page){
		
		if (!this.$sentView) {
			this.$sentView = $(page);
		}
		if (!this.currentOutboundID || this.currentOutboundID != id){
			//fetch stuff, if we are loading a new message
			this.$sentView.find('ul.methods li').hide();
//			this.$sentView.find('ul.statuses span.ui-li-count');
			this.currentOutboundID = id;
			this.getOutboundComm();
		}
		this.checkLoaded();
	},
	getOutboundComm: function(){
		this.$sentView.find('.overrideshow').removeClass('overrideshow');
		new Gopher('/outboundcomm/' + this.currentOutboundID, $.proxy(this.gotOutboundComm, this)).run();
	},
	gotStatuses: function(data){
		if (data){
			this.commStatuses = data;
		}
	},
	buildStatusList: function(){
		if (!OCA.versionAtLeast('1.6.12')){

            //if connecting to old version, without statuses endpoint, translate the existing statuses
            for (var i in this.commStatuses){
            	this.commStatuses[i].Name=OCA.getI18n().gettext(this.commStatuses[i].Name);
            }
        }
		var statuslist = $("#sentcommView ul.statuses");
		var alwaysShow = ['ACKNOWLEDGED','DELIVERED','DISPATCHED','FAILURE_PERM'];
		statuslist.empty();
		for (var i in this.commStatuses){
			statuslist.append($('<li data-key="'+this.commStatuses[i].DefineSymbol+'"'+
				(alwaysShow.indexOf(this.commStatuses[i].DefineSymbol) == -1 ? ' class="hidden"' : '')+'>'+
				'<a href="#sentStatus?status='+this.commStatuses[i].DefineSymbol+'">'+
				'<span data-translate="'+this.commStatuses[i].Name+'"></span>'+
				'<span class="ui-li-count">0</span></a></li>'));
		}
		
	},
	gotOutboundComm: function(data){
		data = data[0];
		this.currentOutboundData = data;
		
		this.currentOutboundData.ContentPart = {};
		for (var c=0; c < data.ContentParts.length; c++){
			var type = data.ContentParts[c].Type;
			this.currentOutboundData.ContentPart[type] = data.ContentParts[c];
			
			this.$sentView.find("ul.methods li[data-key='"+type+"']").show();
		}
		this.stats = {};
		for (var i in this.commStatuses){
			this.stats[this.commStatuses[i].DefineSymbol] = [];
		}
		
		var status;
		for (var s=0; s < data.RecipientStatuses.length; s++){
			status = data.RecipientStatuses[s];
			if (!this.stats[status.BestStatus]) {
				this.stats[status.BestStatus] = [];
			}
			this.stats[status.BestStatus].push(status);
		}
		
		for (status in this.stats){
			var temp = this.$sentView.find("ul.statuses li[data-key='"+status+"']");
			temp.find('span.ui-li-count').text(this.stats[status].length);
			if (this.stats[status].length){
				temp.addClass('overrideshow');
			}
		}
		
		this.$sentView.find('#sendFollowup').off('click').on('click', $.proxy(message.setRecipients, message, data));
		this.$sentView.find('#sendAgain').off('click').on('click', $.proxy(message.loadFromData, message, data));
		this.checkLoaded();
	},
	builtStatusList: false,
	//including existing data, in case app connects to older OCA without API endpoint. this will be replaced by API call
	commStatuses: [
		{
          Name: "Acknowledged",
          DefineSymbol: "ACKNOWLEDGED"
        },
        {
          Name: "Confirmed Delivered",
          DefineSymbol: "DELIVERED"
        },
        {
          Name: "Sent",
          DefineSymbol: "DISPATCHED"
        },
        {
          Name: "Queued",
          DefineSymbol: "QUEUED"
        },
        {
          Name: "Cancelled by the user",
          DefineSymbol: "CANCELLED_CLIENT"
        },
        {
          Name: "Failed - Temporary",
          DefineSymbol: "FAILED_TEMP"
        },
        {
          Name: "Failed - Permanent",
          DefineSymbol: "FAILURE_PERM"
        },
        {
          Name: "Escalated",
          DefineSymbol: "ESCALATED"
        },
        {
          Name: "Processing",
          DefineSymbol: "PROCESSING"
        },
        {
          Name: "Unresolved",
          DefineSymbol: "UNRESOLVED"
        },
        {
          Name: "Deferred",
          DefineSymbol: "DEFERRED"
        },
        {
          Name: "Unsubscribed",
          DefineSymbol: "UNSUBSCRIBED"
        },
        {
          Name: "Not sent - insufficient credits",
          DefineSymbol: "INSUFFICIENT_CREDIT"
        },
        {
          Name: "Replied",
          DefineSymbol: "REPLIED"
        },
        {
          Name: "Not sent - empty address",
          DefineSymbol: "FAILED_EMPTYADDR"
        }
	],
	getStatusLabel: function(define){
		for (var i in this.commStatuses){
			if (this.commStatuses[i].DefineSymbol == define){
				return this.commStatuses[i].Name;
			}
		}
	},
	sentStatusView: function(status, page){
		page = $(page);
		page.find('h3').text(this.getStatusLabel(status));
		page.find('p').text(OCA.getI18n().translate("Recipients whose best status was '%s'").fetch(this.getStatusLabel(status)));
		var recipients = this.stats[status];
		ViewUtil.populateLV(page.find('ul.recipients'), recipients, 'contact', 'contacts', false)
		if (recipients.length == 0){
			page.find('ul.recipients').append("<li data-theme='e'>"+OCA.getI18n().gettext('There are no items to display')+"</li>").listview('refresh');
		}
		if (status == "FAILURE_PERM"){
			page.find('.ui-footer').show();
		} else {
			page.find('.ui-footer').hide();
		}
		this.checkLoaded();
	},
	sentitemView: function(type, page){
		page = $(page);
		var data = this.currentOutboundData.ContentPart[type];
		
		var listview = page.find('ul.ui-listview');
		listview.empty();
		listview.append("<li>"+ type + "</li>");
		if (this.currentOutboundData.Name) {
            listview.append("<li>"+ this.currentOutboundData.Name + "</li>");
        }
        if (data.Subject){
            listview.append("<li>"+ data.Subject + "</li>");
        }
		if (data.HTMLContent){
			
			var iframe = $("<div class='iframe'><iframe /></div>");
	        listview.append(iframe);
	        var htmlcontent = data.HTMLContent;
	        setTimeout(function(){ //populate the iframe, but wrap it in a timeout to make sure the iframe document is accessible
	            ViewUtil.populateIFrame(iframe.find('iframe'), htmlcontent);
	        }, 0);
		} else if (data.TextContent){
			listview.append("<li class='description'><pre>" + data.TextContent + "</pre></li>");
		}
		if (data.Attachments){
			for (var a = 0; a < data.Attachments.length; a++){
				var att = data.Attachments[a];
				var icon = 'file'; 
				switch (att.MIMEType.split("/").shift()){
					case 'video':
						icon = 'camcorder';
						break;
					case 'audio':
						icon = 'microphone';
						break;
					case 'image':
						icon = 'camera';
						break;
				}
				var $li = $("<li><a href='#'>" + ViewUtil.ocaicon(icon + " inline") + att.Name + "</a></li>");
				$li.on('click', function(){
					DocumentController.downloadFile(att.URL, att.Name, att.MIMEType, function(){
						console.log('android callback');
					});
				})
				listview.append($li);
			}
		}
		listview.listview('refresh');
		this.checkLoaded();
	}
});