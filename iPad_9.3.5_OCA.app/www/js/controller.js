$(document).bind('deviceready', function () {
	Session.init($('#session'));
	fileStore.init();
	OCA.init();
	if (parseFloat(window.device.version) >= 7 && window.device.platform === "iOS") {
		OCA.$header.find('.iOS7').css('margin-top', '20px');
		$('div[data-role="page"]').css('padding-top', '62px');
		var $active = $("body").pagecontainer("getActivePage");
		if ($active.prop('id') === 'home'){
			var minH = $active.css('min-height').replace('px', '');
			minH -= 20; //extra padding
			$active.css('min-height', minH + 'px');
		}
	}
});
$(document).on("resume", function(){
	if (OCASession.isLoggedIn()){
		OCA.startTaskPolling();
		dbStore.purge();
		if (Session.shouldCheckPIN()) {
			Session.checkPIN();
		}
	}
	Session.preserveDB = false;
});
$(document).on('pause', function(){
	OCA.stopTaskPolling();
	if (!Session.preserveDB && OCASession.mustUseAppEncryption()){ //only clear database instance when encryption is required
		dbStore.purge();
		dbStore.DB = null;
		dbStore.decrypted = false;
	}
});

$(function(){
	FastClick.attach($('div[data-role=page]').not('.fastclickdisabled'));
});

$.mobile.hidePageLoadingMsg = function(){}; //deprecated, but hide it so all loading messages are controlled in the app and not the framework
$.mobile.changePage.defaults.allowSamePageTransition = true;

//extend mobile history to add a method to expose the current history index. used to jump back to the caller of a selector
$.extend($.mobile.History.prototype, {
	getIndex: function () {
		return this.activeIndex;
	}
});