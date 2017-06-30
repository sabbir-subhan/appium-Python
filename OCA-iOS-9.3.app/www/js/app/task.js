router.add({
	"#taskIndex[?]id=0&query=(.*)": function(type, match){
		TaskController.query = encodeURI(match[1]);
		TaskController.renderListing();
	},
	"#taskIndex$": function(type, match, ui, page, e){
		TaskController.renderListing();
	},
    "#taskIndex[?]assigned=me": function(){
        TaskController.status = "MY";
        TaskController.renderListing();
    },
	"#taskView[?]id=(\\d+)": function(type, match, ui, page, e){
		new TaskView(match[1], page).getData();
	},
	"#taskEdit[?]id=(\\d+)": function(type, match, ui, page, e){
		if (ViewUtil.selector.previousObject){
			ViewUtil.selector.previousObject = null;
			app.checkLoaded();
			return;
		}
		new TaskEdit(match[1], page).getData();
	},
	"#taskNew[?]timestamp=(\\d+)": function(type, match, ui, page, e){
		if (ViewUtil.selector.previousObject){
			ViewUtil.selector.previousObject = null;
			app.checkLoaded();
			return;
		}
		new TaskNew(page).getNewCacheData(match[1]);
	},
	"#taskNew$": function(type, match, ui, page, e){
		if (ViewUtil.selector.previousObject){
			ViewUtil.selector.previousObject = null;
			app.checkLoaded();
			return;
		}
		new TaskNew(page).getTypes();
	},
	//routes to support pending items
   	"#taskView[?]pending=true&timestamp=(\\d+)$": function(type, match, ui, page, e) {
		new TaskPendingView(page).getNewCacheData(match[1])
   	}
});

$(document).on("pageinit", "#taskIndex", function(e){ 
	TaskController.init($(this));
});
$(document).on("pageinit", "#taskAssignType", function (e) {
    TaskController.initAssignType($(this));
});
var TaskController = $.extend({}, app, {
	status:         'MY',
	query:          null,
	init:           function(page){
		var self = this;
		this.page = page;
		this.content = this.page.find('.ui-content');
		this.footer = this.page.find('.ui-footer');
		app.init.call(this);
		this.$mainLV = this.content.find("ul.tasks.listview");
		this.content.find('#taskSearch').keypress(function(e){
			if (e.which == 13){
				self.query = encodeURI($(this).val());
				self.renderListing();
			}
		}).on('change', function(e){
			if ($(this).val() == ''){
				self.query = null;
				self.renderListing();
			}
		});
		var $collapsible = this.content.find('div.ui-collapsible');
		var $statuses = $collapsible.find('ul.statuses');
        if (OCA.versionAtLeast('1.6.2')){
            $statuses.find('li:last-child').before("<li><a href='#' data-status='IN_REVIEW' data-translate='In Review' class='ui-btn translated'>"+OCA.getI18n().gettext('In Review')+"</a></li>");
        }

		this.$heading = $collapsible.find('h2 span.label');
		$statuses.on('click', 'a', function(){
			self.status = $(this).attr('data-status');
			self.$mainLV.empty();
			self.renderListing();
			self.$heading.text($(this).text());
			$collapsible.collapsible('collapse');
		});
	},
    initAssignType: function($page){
        $page.find('div.team').showIf(OCA.versionAtLeast('1.6.19'));
    },
	renderListing:  function(){
		this.footer.find('li a.taskNew').showIf(OCA.checkEndPoint('TASKS_ADDTASK', '/tasks', OCA.ACTION_CREATE));

		//easier to not use this.getListingQuery
		var heading = 'Tasks', url;
		if (this.status == 'MY'){
			heading = 'My ' + heading;
			url = "/tasks/assigned/me?status=ANY";
		} else {
			url = "/tasks?status=" + this.status;
		}
		if (this.query){
			url += "&search=" + this.query;
			heading += " search";
		}
		url += "&orderby=StartDate";

		var renderProps = {
			type:         'task',
			selectorMode: false,
			icon:         'tasks'
		};
		this.getListing(url, T(heading), $.proxy(this.gotTasks, this), renderProps);
	},
	gotTasks: function(data, extra){
        if (this.status == 'MY'){
            OCA.userData.set('myTaskCount', data.length); //if loading assigned tasks, update the user's task count.
        }
	}
});

function TaskView(id, page){
	this.initTaskView(id, page);
}
TaskView.prototype = new TypeView;
TaskView.prototype.constructor = TaskView;
TaskView.prototype.initTaskView = function(id, page){
	this.initTypeView(id, page, "task");
};

TaskView.prototype.outcomeRender = function(field,data){
	if (!data||!data.options||!data.options.length || this.data.CompletedDate){ //if completed, don't show outcomes.
		return null;
	}
	var html='';
	if (data.subject.type=='ReportVersion'){
		html += '<h6>Task Report</h6>'+
		'<ul class="ui-grid-a">'+
			'<li class="ui-block-a"><a href="#reportView?id='+data.subject.id+'&version=draftFallback" class="ui-btn ui-btn-b">View</a></li>'+
			'<li class="ui-block-b"><a href="#reportEdit?id='+data.subject.id+'" class="ui-btn ui-btn-b">Edit</a></li>'+
		'</ul>';
	}
	html += '<h6>'+ field.Label + '</h6>'+
		'<ul class="ui-grid-a outcomeOptions">';
	for (var i in data.options){
		var opt = data.options[i];
		html+='<li class="ui-block-'+(i%2?'b':'a')+'">'+
			'<a href="#confirmOutcomeTask" data-rel="popup" data-position-to="window" area-haspopup="true" area-owns="confirmOutcomeTask" area-expandable="false" class="ui-btn ui-btn-b" data-id="'+opt.id+'">'+opt.name+'</a></li>';

	}
	html+='</ul>';
	var row = $("<li />")
		.html(html)
		.data('icon', false)
		.attr('data-enhance', false);
	this.listview.append(row);
	
	return row;
}

TaskView.prototype.afterRender = function () {
	var $self = this;
    TypeView.prototype.afterRender.call(this);
    var mm = this.moreMenu;
    var $deletePopup = this.page.find('#confirmDeleteTask');
    var $outcomePopup = this.page.find('#confirmOutcomeTask');
	ViewUtil.applyTemplate($deletePopup,{item:'task'},'confirmDelete');
	$deletePopup.find('a.delete').off().on('click',$.proxy(this.deleteItem,this));
    mm.find('li.delete').on('click', function(){
        mm.popup('close');
        $outcomePopup.popup('close');
        $deletePopup.popup('open');
    });
    
    if (this.data.Workflow && this.data.Workflow.options)
    {
    	var $workflowData = this.data.Workflow;
    	var $oopts = $('.outcomeOptions a');
    	$oopts.click(function(){
    		for (var i in $workflowData.options)
    		{
    			if ($workflowData.options[i].id==$(this).data('id'))
    			{
    				ViewUtil.applyTemplate($outcomePopup,$workflowData.options[i],'confirmOutcome');
    			}
    		}
			$outcomePopup.find('a.complete').off().on('click',function(){
				var submitdata={outcome:$(this).data('outcomeid')}
				if ($('input#comment-'+$(this).data('outcomeid')).length)
				{
					if ($('input#comment-'+$(this).data('outcomeid')).val().trim())
					{
						submitdata.comment=$('input#comment-'+$(this).data('outcomeid')).val();
					}
					else if ($(this).hasClass('commentRequired1'))
					{
						$('input#comment-'+$(this).data('outcomeid')).addClass('error');
						util.alertDialog(T('You must supply a comment for this response'));
						return;
					}
				}
				$.proxy($self.outcomeItem,$self,submitdata)();
			});
    		mm.popup('close');
	        $deletePopup.popup('close');
	        $outcomePopup.popup('open');
	        //$outcomePopup.find('input').focus();
    	});
    }
	
	//There is only one item in the more menu - to delete a task so hide the entire item, the delete item is removed by TypeView
	this.footer.find('li.more a').showIf(this.data.WritePolicyURL != -1);
};

TaskView.prototype.outcomeItem = function(data){
	if (this.submitted){
		return;
	}
	
	this.submitted = true;
	var desc = "Edited " + (this.data.FullName || this.data.Name || this.type);

    fileStore.clearCache('tasks'); //task status changed, index must refresh. Triggering before the PUT action (although it might fail) to avoid race conditions
	var subject = this.data.Workflow.subject;
	new Gopher({url:this.endpoint + this.ID, data:data, desc: desc}, function(){
        if (subject && subject.type && subject.id){
            switch (subject.type){
                case 'ReportVersion':
                    fileStore.clearCache('reports');                //report changed, index must refresh. New reports will appear
                    new Gopher('/report/' + subject.id).uncache();  //report has been altered, draft removed
                    break;
            }
        }
		$("body").pagecontainer("change", '#taskIndex');
	},$.proxy(this.dataError, this)).put();
}


TaskView.TYPE_NORMAL = 1;
TaskView.TYPE_CHECKLIST = 2;
TaskView.DEFINE_NAME = 'NAME';
TaskView.DEFINE_ASSIGNEE = 'ASSIGNEE';
TaskView.DEFINE_EME = 'EME';
TaskView.CHECKED = 'checkbox_tick';
TaskView.UNCHECKED = 'checkbox';
TaskView.prototype.getType = function(){
	this.typeData = {
		Name: "Task",
		Fields: {
			Name: {Type: 'sgltxt', Label: OCA.getI18n().gettext('Title'), Y: 0, X: 0, Define: TaskView.DEFINE_NAME, Required: true},
			Assignees: {Type: 'slmc', Label: OCA.getI18n().gettext('Assigned'), Y: 1, X: 0, Define: TaskView.DEFINE_ASSIGNEE, Required: true},
			Detail: {Type: 'multitxt', Label: OCA.getI18n().gettext('Detail'), Y: 2, X: 0},
			Workflow: {Type: 'outcome',Label:OCA.getI18n().gettext('Action Required'),Y:2,X:0},
			StartDate: {Type: 'datetime', Label: OCA.getI18n().gettext('Start Date'), Y: 4, X: 0, Required: true},
			DueDate: {Type: 'datetime', Label: OCA.getI18n().gettext('Due Date'), Y: 5, X: 0},
			CompletedDate: {Type: 'datetime', Label: OCA.getI18n().gettext('Completed Date'), Y: 6, X: 0},
			Status: {Type:'opt', Label:OCA.getI18n().gettext('Status'), Y:7, X:0, Options:[
				['Action required',OCA.getI18n().gettext('Action required')],
				['In progress',OCA.getI18n().gettext('In progress')],
				['Completed',OCA.getI18n().gettext('Completed')],
				['Cancelled',OCA.getI18n().gettext('Cancelled')]], Required: true, DefaultValue: 'Action required'},
			RemindMinsBeforeDue: {Type: 'opt', Label: OCA.getI18n().gettext('Remind before due'), Y: 8, X: 0, Options: [
				[0,OCA.getI18n().gettext('No')],
				[15,OCA.getI18n().gettext('15 minutes')],
				[30,OCA.getI18n().gettext('30 minutes')],
				[60,OCA.getI18n().gettext('1 hour')],
				[120,OCA.getI18n().gettext('2 hours')]]},
			RemindWhenOverdue: {Type: 'opt', Label: OCA.getI18n().gettext('Remind when overdue'), Y: 9, X: 0, Options: [
				[0,OCA.getI18n().gettext('No')],
				[1,OCA.getI18n().gettext('Yes')]]}
		}
	};
    
	if (OCA.IncidentManager){
		this.typeData.Fields.RelatedObjects = {Type: 'slmc', Label: OCA.getI18n().gettext('Events'), Y: 10, X: 0, Define: TaskView.DEFINE_EME};
	}
    if (OCA.versionAtLeast('1.6.2')){
        this.typeData.Fields.Status.Options.push(['In review', OCA.getI18n().gettext('In review')]);
    }
	if (this.data && this.data.ChecklistItems){
		this.typeData.Name = 'Checklist';
		this.typeID = TaskView.TYPE_CHECKLIST;
		
		this.typeData.Fields.ChecklistItems = {Type: 'checklist', Label: OCA.getI18n().gettext('Check list'), Y: 11, X:0};
	} else {
		this.typeID = TaskView.TYPE_NORMAL;
	}
	this.forceRefresh = false;
	this.render();
}
TaskView.prototype.beforeRender = function(){
	if (this.data.RemindMinsBeforeDue){
		var min = this.data.RemindMinsBeforeDue;
		if (min != 0 && min != 15 && min != 30 && min != 60 && min != 120){
			var field = this.typeData.Fields.RemindMinsBeforeDue;
			field.Options.push([min, min + ' minutes']);
		}
	}
}
TaskView.prototype.checklistRender = function(){
	this.listview.append($("<li data-role='list-divider'/>").text(OCA.getI18n().gettext("Checklist")));
	for (var i = 0; i < this.data.ChecklistItems.length; i++){
		var item = this.data.ChecklistItems[i];
		var checked = parseInt(this.data.ChecklistStatuses[item.ID], 10);
		var icon = ViewUtil.ocaicon((checked ? TaskView.CHECKED : TaskView.UNCHECKED) + ' inline');
		var row = $("<li class='checklist'><h6>" + icon + "<span class='text' /></h6></li>");
		row.find('span.text').text(item.Label);
		if (checked){
			row.append("<p>"+OCA.getI18n().translate('Checked by %s').fetch(item.CheckedByContactName + " - " + ViewUtil.relativeDate(new Date(item.DateChecked))) + "</p>");
		}
		row.data('item', item);
		item.Row = row;
		this.listview.append(row);
	}
}
TaskView.prototype.slmcRender = function(field, data){
	data = this.convertSLMCData(field, data);
	return TypeView.prototype.slmcRender.call(this, field, data);
}
//Task data is in a different format than normal SLMCs. Convert it so it can be reused.
TaskView.prototype.convertSLMCData = function(field, data){
	if (field.Define == TaskView.DEFINE_EME){ 
		//extract EMEs only out of the related objects
		if (!data || !data['From'] || !data['From']['related to']) {
			data = {};
		} else {
			var EMEs = {}
			for (var url in data['From']['related to']){
				if (url.indexOf('/eme/') != -1){
					EMEs[url] = data['From']['related to'][url];
				}
			}
			data = EMEs;
		}
	}
	var slmc = [];
	for (var url in data){
		slmc.push({
			url: url,
			label: data[url]
		});
	}
	return slmc;
}

function TaskEdit(id, page){
	this.initTaskEdit(id, page);
}
TaskEdit.prototype = new TypeEdit;
TaskEdit.prototype.constructor = TaskEdit;
TaskEdit.prototype.initTaskEdit = function(id, page){
	this.initTypeEdit(id, page, "task");
};
TaskEdit.prototype.getSLMCType = function(field){
	switch (field.Define){
		case TaskView.DEFINE_ASSIGNEE:
			return "taskAssignType";
			break;
		case TaskView.DEFINE_EME:
			return "emeTreeView";
			break;
	}
}
TaskEdit.prototype.getType = TaskView.prototype.getType;
TaskEdit.prototype.checklistRender = function(){
	var self = this;
	self.data.ChecklistChanged = false;
	TaskView.prototype.checklistRender.call(this);
	this.listview.on('click', 'li.checklist', function(){
		var item = $(this).data('item');
		var ID = item.ID;
		var current = self.data.ChecklistStatuses[ID];
		if (current == "1"){
			item.Row.find('.icon').removeClass(TaskView.CHECKED).addClass(TaskView.UNCHECKED);
			self.data.ChecklistStatuses[ID] = "0";
		} else {
			item.Row.find('.icon').removeClass(TaskView.UNCHECKED).addClass(TaskView.CHECKED);
			self.data.ChecklistStatuses[ID] = "1";
		}
		self.data.ChecklistChanged = true;
	});
}

TaskEdit.prototype.slmcRender = function(field, data){
	data = TaskView.prototype.convertSLMCData(field, data);
	return TypeEdit.prototype.slmcRender.call(this, field, data);
}

TaskEdit.prototype.getSubmission = function(){
	var submission = {};
	var submit = false, field = null;
	for (var id in this.typeData.Fields){
		field = this.typeData.Fields[id];
		if (this.hasChanged(field)) {
			submission[id] = field.Input.val();
            if (field.Input.getAPIValue){ //overwrite the val() output if there's a specialised function to get the submission value
                submission[id] = field.Input.getAPIValue();
            }
			submit = true;
		}
	}
	
	//handle policies and other options
	for (var k in this.typeData){
		field = this.typeData[k];
		if (field && field.Input){	//there is an input field for this item
			if (this.hasChanged(field)){
				submission[k] = field.Input.val();
				submit = true;
			}
		}
	}
	if (submission.Assignees){	//convert SLMC data into assignee data
		submission.AssigneeURLs = [];	//task assignees needs to be PUT or POSTed to assigneeURLs
		var assignees = {};
		for (var a = 0; a < submission.Assignees.length; a++){
			var assignee = submission.Assignees[a];
			assignees[assignee.url] = assignee.label;
			submission.AssigneeURLs.push(assignee.url);
		}
        submission.Assignees = assignees;
	}
	if (submission.RelatedObjects){
		var relatedEMEs = submission.RelatedObjects;
		submission.RelatedObjects = {
			'From': {
				'related to': {}
			}
		};
		for (var e = 0; e < relatedEMEs.length; e++){
			var eme = relatedEMEs[e];
			submission.RelatedObjects.From['related to'][eme.url] = eme.label;
		}
	}
	if (this.data) {
		if (this.data.ChecklistChanged){
			submit = true;
			submission.ChecklistItems = this.data.ChecklistItems;
			for (var i = 0; i < submission.ChecklistItems.length; i++){
                //remove readonly properties and DOM nodes
                delete submission.ChecklistItems[i].DateChecked;
                delete submission.ChecklistItems[i].CheckedByContactURL;
                delete submission.ChecklistItems[i].CheckedByContactName;
				delete submission.ChecklistItems[i].Row;
			}
			submission.ChecklistStatuses = this.data.ChecklistStatuses; //changes are made directly to the data object
		}
		if (this.data.RelatedObjects && submission.hasOwnProperty('RelatedObjects')){ //related (eme) objects have been edited AND they have existing data
			submit = true;
			//User can only edit the EME relations, so add all of the existing, non-EME related objects back to the submission
			for (var direction in this.data.RelatedObjects){
				if (!submission.RelatedObjects.hasOwnProperty(direction)){
					submission.RelatedObjects[direction] = {};
				}
				for (var relation in this.data.RelatedObjects[direction]){
					if (!submission.RelatedObjects[direction].hasOwnProperty(relation)){
						submission.RelatedObjects[direction][relation] = {};
					}
					for (var url in this.data.RelatedObjects[direction][relation]){
						if (url.indexOf("eme") == -1){
							submission.RelatedObjects[direction][relation][url] = this.data.RelatedObjects[direction][relation][url];
						}
					}
				}
			}
		}
	}
	return submit ? submission : null;
}
TaskEdit.prototype.beforeRender = function(){
	if (this.data.RemindMinsBeforeDue){
		var min = this.data.RemindMinsBeforeDue;
		if (min != 0 && min != 15 && min != 30 && min != 60 && min != 120){
			var field = this.typeData.Fields.RemindMinsBeforeDue;
			field.Options.push([min, min + ' minutes']);
		}
	}
	this.data.RemindWhenOverdue = this.data.RemindWhenOverdue ? 1 : 0;
}

function TaskNew(page){
	this.initTaskNew(page);
}
TaskNew.prototype = new TaskEdit;
TaskNew.prototype.constructor = TaskNew;
TaskNew.prototype.initTaskNew = function(page){
	this.parentID = null;
	this.initTaskEdit(null, page, "task");
	this.createURL = '/tasks';
}
TaskNew.prototype.hasChanged = TypeNew.prototype.hasChanged;
TaskNew.prototype.submission = function(submission){
	if (this.submitted) return;
	this.submitted = true;
    
    submission['TypeURL'] = Configuration.getAPIPath() + '/task/' + this.typeID;  //not processed by the API, just setting this for the app's benefit
	var desc = "Created new " + this.typeData.Name;
    window.linkParams = {createdObject: 'task', message: desc};
	new Gopher({
		url: this.createURL,
		data: submission, 
		desc: desc, 
		oldTimestamp: this.timestamp,
		resubmitter: 'TaskResubmitter'
	}, $.proxy(this.attachAfterSubmit, this, submission.Attachments), $.proxy(this.dataError, this)).post();
}
TaskNew.prototype.getTypes = function(){
	var types = [{URL: 'task/' + TaskView.TYPE_NORMAL,	 Name: 'Normal Task'}];
//	types.push({URL: 'task/' + TaskView.TYPE_CHECKLIST, Name: 'Checklist Task'});	//creating a new checklist task can wait for another release
	this.gotTypes(types);
}
TaskNew.prototype.beforeRender = function(){
	if (OCA.IncidentManager){
		var pe = OCA.getPrimaryEME();
		if (pe !== null){
			if (! this.data){
				this.data = {};
			}
			if (! this.data.RelatedObjects){
				this.data.RelatedObjects = {};
			}
			if (! this.data.RelatedObjects.From){
				this.data.RelatedObjects.From = {};
			}
			if (! this.data.RelatedObjects.From['related to']){
				this.data.RelatedObjects.From['related to'] = {};
			}
			this.data.RelatedObjects.From['related to'][pe.url] = pe.label;
		}
	}
}

function TaskPendingView(page) {
	this.initTaskPending(page);
}
TaskPendingView.prototype                = new TaskView;
TaskPendingView.prototype.constructor    = TaskPendingView;
TaskPendingView.prototype.initTaskPending = function(page) {
	this.initTaskView(null, page);
	this.createURL = '/tasks';

};
TaskPendingView.prototype.afterRender    = function() {
	TaskView.prototype.afterRender.call(this);

	var $deletePopup = this.page.find('#confirmDeleteTask');
	$deletePopup.find('a.delete').off().on('click', $.proxy(this.deleteCacheItem, this, this.createURL, this.timestamp));
	this.footer.find('li.edit a').prop('href', '#taskNew?timestamp=' + this.timestamp);
};
