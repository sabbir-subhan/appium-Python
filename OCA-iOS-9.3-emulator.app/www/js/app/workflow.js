router.add({
	"#workflowActivation": function(){
        Workflow.checkLoaded();
    }
});
$(document).on("pageinit", "#workflowActivation", function(e){
	Workflow.init($(this));
});
var Workflow = $.extend({}, app, {
	init: function(page){
		this.page = page;
		this.content = this.page.find('.ui-content');
		this.$lv = this.content.find('ul');
		this.$confirm = this.page.find('#confirmWorkflowActivation');
        app.init.call(this);
        $(window).on('loggedIn', function(){    //clear folder list when changing systems
            Workflow.$lv.empty();
        });
    },
    checkLoaded: function(){
        app.checkLoaded();
		if (this.$lv.children().length === 0){	//if initially accessed in offline mode, workflows might not be populated. check on each load
			this.getWorkflows();
		}
    },
    getWorkflows: function(){
		new Gopher('/workflows/nosubject?filter[trigger]=manual', $.proxy(this.gotWorkflows, this)).run();
		this.$lv.on('click', 'a', $.proxy(this.confirmActivation, this));
	},
	gotWorkflows: function(workflows, extra){
		ViewUtil.populateLV(this.$lv, workflows, 'workflow', 'switch', false, extra.NextPageURL);
        if (this.$lv.children().length === 0){
            this.$lv.append($("<li />").data('theme','e').text(OCA.getI18n().gettext('There are no workflows available for activation'))).listview('refresh');
        }
		this.checkLoaded();
	},
	confirmActivation: function(e){
        var self = Workflow;
        setTimeout(function(){      //fix active/hover styles after clicking an item
        	if (self.page){
	            self.page.find('.ui-btn-active').removeClass('ui-btn-active');
	            self.page.find('.ui-btn-hover-undefined').removeClass('ui-btn-hover-undefined');
	        }
	    }, 30);
		

		var a = $(e.currentTarget);
		var href = a.prop('href');
		var id = href.substr(href.indexOf('id=')+3);
		
		var interval = a.data('mobiletrackingintervalminutes');
		var duration = a.data('mobiletrackingdurationhours');
		
		util.confirmDialog(
			T("Are you sure you want to activate this workflow?"),
			function(buttonIndex) {
				if (buttonIndex == 1) { //activate
					Workflow.activateWorkflow(id, interval, duration);
				}
			}.bind(Workflow),
			T('Activate'),
			[T('Activate'), T('Cancel')]
		);
		
		e.preventDefault();
		return false;
	},
	activateWorkflow: function(id, interval, duration){
		new Gopher({url: "/workflow/" + id + "/instances", desc: "Workflow activation"}, $.proxy(this.workflowActivated, this, parseInt(interval), parseInt(duration))).post();

	},
	workflowActivated: function(interval, duration){
        if (interval && duration && device.platform !== "Mobile Interface"){
            util.alertDialog(T('Workflow activated - Tracking Location'));
            loc.startTracking(interval, duration);
        } else if (util.getHash() == '#') { //home page, dont go back
			util.alertDialog(T('Workflow activated'));
        } else {
			util.alertDialog(T('Workflow activated'));
			util.goBack();
        }
	}
});