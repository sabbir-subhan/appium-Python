router.add({
	"#inboxitemView[?]id=(\\d+)": function(type, match, ui, page, e){
		new InboxItemView(match[1], page).getData();
	},
	'#inbox$': function(){
		inbox.checkLoaded();
	}
});
$(document).on("pageinit", "#inbox", function(e){
    inbox.init($(this));
});
var inbox = $.extend({}, app, {
	init: function(page){
		this.page = page;
        this.content = this.page.find('.ui-content');
		this.$collapsible = this.content.find('div.ui-collapsible');
		this.$folderHeading = this.content.find('h2 span.label');
		this.$folderList = this.content.find('ul.folders');
		this.$messages = this.content.find('ul.messages');
		
		this.content.find('#inboxSearch').keypress(function(e){
			if (e.which == 13){
				inbox.getMessages(inbox.currentFolderID, $(this).val());
			}
		}).on('change', function(e){
			if ($(this).val() == ''){
				inbox.getMessages(inbox.currentFolderID);
			}
		});
        $(window).on('loggedIn', function(){    //clear folder list when changing systems
			inbox.$folderList.empty();
		});
	},
	checkLoaded: function(){
		app.checkLoaded();
		if (this.$folderList.children().length === 0){	//if initially accessed in offline mode, folders might not be populated. check on each load
			new Gopher('/inboxfolders', $.proxy(this.gotFolders, this)).run();
		}
	},
	gotFolders: function(data){
		this.$folderList.empty();
		for (var d=0; d < data.length; d++){
			var folder = data[d];
			var li = $("<li><a>"+folder.Name+"</a></li>").data('id', ViewUtil.getID(folder.URL)).on('click', function(){
				inbox.$folderHeading.text($(this).text());
				inbox.$messages.empty();
				inbox.getMessages($(this).data('id'));
				inbox.$collapsible.collapsible('collapse');
			});
			this.$folderList.append(li);
		}
		this.$folderList.listview('refresh');
		this.$folderList.children().first().click();
	},
	getMessages: function(id, query){
		this.currentFolderID = id;
		var url = '/inboxfolder/'+id+'/inboxitems';
		if (query) {
			url += "?search=" + encodeURIComponent(query);
		}
		new Gopher(url, $.proxy(this.gotMessages, this)).run();
		this.checkLoaded();
	},
	gotMessages: function(data, extra){
		ViewUtil.applyTemplate(this.$messages, data, 'inboxLV', extra.nextPageURL);
		this.checkLoaded();
	}
});

function InboxItemView(id, page){
	this.initInboxItemView(id, page);
}
InboxItemView.prototype = new TypeView;
InboxItemView.prototype.constructor = InboxItemView;
InboxItemView.prototype.initInboxItemView = function(id, page){
	this.initTypeView(id, page, "inboxitem");
	this.footer.find('#inboxitemReply').off('click').on('click', $.proxy(this.reply, this));
	this.footer.find('#inboxitemForward').off('click').on('click', $.proxy(this.forward, this));
};
InboxItemView.prototype.getType = function(){
	this.render(); //inbox items dont have types with endpoints, skip right to the render function
	this.forceRefresh = false;
}
InboxItemView.prototype.render = function(){
	this.listview = $("<ul />");
	this.listview.empty();
	var from = $("<li><h4>"+OCA.getI18n().translate('%s from').fetch(this.data.Type)+"</h4><p>" + this.data.FromName + "</p></li>");
	if (this.data.FromContactURL){
		var id = ViewUtil.getID(this.data.FromContactURL);
		from.wrapInner("<a href='#contactView?id="+id+"' />");
	}
	this.listview.append(from);
	this.listview.append("<li>" + ViewUtil.displayDateTime(this.data.ReceivedDate) + "</li>");
	if (this.data.HTMLContent){
		var iframe = $("<div class='iframe'><iframe /></div>");
		this.listview.append(iframe);
		var htmlcontent = this.data.HTMLContent;
		setTimeout(function(){ //populate the iframe, but wrap it in a timeout to make sure the iframe document is accessible
            ViewUtil.populateIFrame(iframe.find('iframe'), htmlcontent);
        }, 0);

	} else if (this.data.TextContent){
		this.listview.append("<li class='description'><pre>" + this.data.TextContent + "</pre></li>");
	} else {
		this.listview.append("<li class='description'>("+OCA.getI18n().gettext('empty message')+")</li>");
	}
	if (this.data.Attachments){
		for (var a = 0; a < this.data.Attachments.length; a++){
			var att = this.data.Attachments[a];
			var icon = 'file'; 
			switch (att.MIMEType.split("/").shift()){
				case 'video':
					icon = 'film';
					break;
				case 'audio':
					icon = 'microphone';
					break;
				case 'image':
					icon = 'camera';
					break;
			}
			var $li = $("<li><a href='#'>" + ViewUtil.ocaicon(icon + " inline") + att.Name + "</a></li>");
			$li.on('click', function(att){
				DocumentController.downloadFile(att.URL, att.Name, att.MIMEType, $.noop, true);
			}.bind(this, att));
			this.listview.append($li);
		}
	}
	this.content.append(this.listview);
	this.listview.listview();
	$.mobile.loading('hide');
}
InboxItemView.prototype.reply = function(){
	if (!this.data.FromContactURL) return;
	var bits = this.data.FromContactURL.split("/");
	var id = bits.pop();
	var type = bits.pop();
	message.sendTo(type, id, this.data.FromName);
	if (this.data.Type == "SMS"){
		message.setSMS('');
	} else {
		message.setEmail("Re: " + this.data.Subject)
	}
};
InboxItemView.prototype.forward = function(){
	message.clearMessage();
	if (this.data.Type == "SMS"){
		message.setSMS(this.data.TextContent);
	} else {
		var content;
		var useCKEditor = (device.platform != 'Win32NT'); //disable for WP8 devices
		if (useCKEditor) {
			content = this.data.HTMLContent;
			if (OCA.Settings.IncludeMetadataWhenForwarding) {
				//content _might_ be a full HTML document.
				// Use $.parseHTML to break it down into individual nodes and append them to a temporary parent container
				var $tmp = $('<div />').append(this.getMetadataHTML(), $.parseHTML(content));

				content = $tmp.html();
			}
		} else {
			content = this.data.TextContent;
			if (OCA.Settings.IncludeMetadataWhenForwarding) {
				content = this.getMetadataText() + '\n' + content;
			}
		}
		message.setEmail("Fwd: " + this.data.Subject, content, this.data.Attachments)
	}
};
InboxItemView.prototype.getMetadataHTML = function(){
	var metadata = ["", "---- Forwarded Message ----"];

	if (this.data.FromAddress){
		metadata.push("<b>From:</b> " + ViewUtil.escape(this.data.FromAddress));
	} else if (this.data.FromName){
		metadata.push("<b>From:</b> " + ViewUtil.escape(this.data.FromName));
	}
	if (this.data.ReceivedDate){
		metadata.push("<b>Date:</b> " + ViewUtil.displayDateTime(this.data.ReceivedDate));
	}
	if (this.data.Subject){
		metadata.push("<b>Subject:</b> " + ViewUtil.escape(this.data.Subject));
	}
	if (this.data.HeaderTo){
		metadata.push("<b>To:</b> " + ViewUtil.escape(this.data.HeaderTo));
	} else if (this.data.ToAddress){
		metadata.push("<b>To:</b> " + ViewUtil.escape(this.data.ToAddress));
	}
	if (this.data.HeaderCC){
		metadata.push("<b>CC:</b> " + ViewUtil.escape(this.data.HeaderCC));
	}
	metadata.push("");

	return metadata.join("<br />");
}

InboxItemView.prototype.getMetadataText = function(){
	var metadata = ["", "---- Forwarded Message ----"];

	if (this.data.FromAddress){
		metadata.push("From: " + this.data.FromAddress);
	} else if (this.data.FromName){
		metadata.push("From: " + this.data.FromName);
	}
	if (this.data.ReceivedDate){
		metadata.push("Date: " + ViewUtil.displayDateTime(this.data.ReceivedDate));
	}
	if (this.data.Subject){
		metadata.push("Subject: " + this.data.Subject);
	}
	if (this.data.HeaderTo){
		metadata.push("To: " + this.data.HeaderTo);
	} else if (this.data.ToAddress){
		metadata.push("To: " + this.data.ToAddress);
	}
	if (this.data.HeaderCC){
		metadata.push("CC: " + this.data.HeaderCC);
	}
	metadata.push("");

	return metadata.join("\n");
}
