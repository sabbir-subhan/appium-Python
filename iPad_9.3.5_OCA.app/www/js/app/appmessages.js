router.add(
	{
		"#appMessageView[?]id=(\\d+)": function(type, match, ui, page, e) {
			new AppMessageView(match[1], page).getData();
		},
		'#appMessages$':                function() {
			appMessagesController.renderListing();
		},
		"#appMessages[?]dismissed=0&search=": function(){
			appMessagesController.forceRefresh = true;
			appMessagesController.indexFilters = {
				dismissed: 0,
				search: null,
			}
			appMessagesController.content.find('#appMsgSearch').val('');
			appMessagesController.statusHeading.text(T('Active'));
			appMessagesController.renderListing();
			
		}
	});
$(document).on("pageinit", "#appMessages", function(e) {
	appMessagesController.init($(this));
});
var appMessagesController = $.extend({}, app, {
	currentCount: undefined,
	unreadCount: undefined,
	existingMessageIDs : undefined,

	init: function(page) {

		this.page    = page;
		this.content = this.page.find('.ui-content');
		this.$mainLV = this.content.find('ul');

		this.indexFilters = {
			search: null,
			dismissed: 0,
		};
		this.queryParams.push('dismissed');

		this.content.find('#appMsgSearch').keypress(function(e) {
			if (e.which == 13) {
				this.indexFilters.search = $(e.currentTarget).val();
				this.renderListing();
			}
		}.bind(this)).on('change', function(e) {
			if ($(e.target).val() == '') {
				this.renderListing();
			}
		}.bind(this));

		this.$collapsible    = this.content.find('div.ui-collapsible');
		this.indexDismissedList = this.content.find('ul.msgdismissed');
		this.statusHeading   = this.content.find("h2.msgdismissed span.label");
		this.indexDismissedList.on('click', 'a', $.proxy(function(e) {
			var $status              = $(e.currentTarget);
			this.indexFilters.dismissed = $status.attr('data-dismissed');
			this.statusHeading.text($status.text());
			this.$collapsible.collapsible('collapse');
			this.renderListing();
		}, this));
	},

	renderListing: function() {
		var query     = this.getListingQuery();
		var heading   = $.isEmptyObject(query) ? "My Messages" : "My Messages search";
		query.orderby = 'TimeCreated DESC';

		var url         = "/appmessages?" + $.param(query);
		var renderProps = {
			type:     'appMessage',
			template: 'appMessagesLV'
		};
		this.getListing(url, T(heading), $.proxy(this.gotMessages, this, query), renderProps, true);
	},

	gotMessages: function(query, data, extra){
		if (this.existingMessageIDs === undefined){
			this.existingMessageIDs = [];
		}
		for (var i = 0; i < data.length; i++){
			this.existingMessageIDs[data[i].URL] = true;
		}
		if (!query.search){
			this.currentCount = data.length;
			this.unreadCount = data.filter(function(m){ return m.IsRead == '0'}).length;
			this.updateBadge();
		}
	},

	checkNew: function(data){
		if (this.existingMessageIDs !== undefined){
			for (var i = 0; i < data.length; i++){
				if(!this.existingMessageIDs[data[i].URL]){
					if (data[i].IsRead == '0'){
						return true;
					}
				}
			}
		}
		return false;
	},

	updateBadge: function(count){
		count = count || this.unreadCount;

		$("a[href='#appMessages'] .badge").text(count).showIf(count);
		var pushwoosh = cordova.require("pushwoosh-cordova-plugin.PushNotification");
		if (pushwoosh){
			pushwoosh.setApplicationIconBadgeNumber(this.unreadCount);
		}
	}
});
/**
 * @property {Array} data.Actions
 * @property {string} data.TimeCreated ISO8601 datetime string
 * @property {string} data.Status enum , status
 * @property {string} data.Notification subject for notification, safe for insecure display
 * @property {string} data.Message message content, potentially sensitive
 * @property {string} data.MenuChoice
 */
function AppMessageView(id, page) {
	this.initAppMessageView(id, page);
}
AppMessageView.prototype             = new TypeView;
AppMessageView.prototype.constructor = AppMessageView;
AppMessageView.prototype.initAppMessageView = function(id, page) {
	this.initTypeView(id, page, "appmessage");

	this.footer.find('a#appMessageOk').text('Ok').off();
	this.footer.find('a#appMessageDismiss').off().on('click', $.proxy(this.dismissMessage, this));
};
AppMessageView.prototype.getType = function() {
	this.render(); //app message dont have types with endpoints, skip right to the render function
	this.forceRefresh = false;
	if (this.data.IsRead == '0'){
		this.readMessage();
	}
}
AppMessageView.prototype.render  = function() {
	this.listview = $("<ul />");
	this.listview.empty();
	
	var message = ViewUtil.handleObjectLinks(this.data.Message);

	this.multitxtRender({Label: T('Message'), type: 'multitxt'}, message);
	this.fieldRender({Label: T('Sent'), type: 'datetime'}, ViewUtil.displayDateTime(this.data.TimeCreated));
	this.fieldRender({Label: T('Status'), type: 'sgltxt'}, this.data.Status);

	if (this.data.Actions) {
		for (var a = 0; a < this.data.Actions.length; a++) {
			/**
			 * @var {Object} action
			 * @property {string} action.Label
			 * @property {string} action.Colour
			 * @property {string} action.Intent
			 * @property {string} action.URL
			 * @property {string} action.Properties.MenuChoice
			 */
			var action   = this.data.Actions[a];
			action.Label = action.Label || action.label;
			var row      = "<li class='ui-field-contain ui-li-static'><div class='app-message-action'>"
				+ "<a href='#' data-role='button' data-theme='b'>" + action.Label + "</a></div></li>";
			action.$row  = $(row).on('click', $.proxy(this.selectAction, this, action)).appendTo(this.listview);

			if (action.Properties.MenuChoice && action.Properties.MenuChoice == this.data.MenuChoice || $.inArray(action.Properties.MenuChoice, this.data.MenuChoice) !== -1){
				action.$row.find('a').addClass('selected').prepend(ViewUtil.ocaicon('checkmark white inline-left'));
				this.listview.addClass('selection-made');
			}
		}
	}
	this.content.append(this.listview);
	this.listview.listview();
	this.content.enhanceWithin();
	$.mobile.loading('hide');
};

AppMessageView.prototype.selectAction = function(action) {
	this.selectedAction = action;
	this.listview.addClass('selection-made');
	this.content.find('.app-message-action a.selected .icon.checkmark').remove();
	this.content.find('.app-message-action a.selected').removeClass('selected');

	action.$row.find('a').addClass('selected').prepend(ViewUtil.ocaicon('checkmark white inline-left'));
	this.footer.find('a#appMessageOk').text('Send').off('click').on('click', $.proxy(this.sendAction, this));
}

AppMessageView.prototype.dismissMessage = function() {
	new Gopher({
		url:  '/appmessage/' + this.ID,
		data: {
			IsDismissed: true
		}
	}, function() {
		util.goBack();
	}).put(false);
	new Gopher('/appmessages').uncache();
}

AppMessageView.prototype.readMessage = function() {
	new Gopher({
		url:  '/appmessage/' + this.ID,
		data: {
			IsRead: true
		}
	}, function() {
//		util.goBack();
	}).put(false);
	new Gopher('/appmessages').uncache();
}

AppMessageView.prototype.sendAction = function(e){
	//TODO switch on this.selectedAction.Intent when there are multiple button types to support
	new Gopher({
		url: this.selectedAction.URL,
		data: this.selectedAction.Properties
	}, function(){
		//success
		util.goBack();
	}).put(false);

	//normally would go back. wait for response first.
	e.stopPropagation();
	e.preventDefault();
	return false;
}