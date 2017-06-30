router.add({
	"#reportIndex[?]id=0&query=(.*)": function(type, match){
		ReportController.indexFilters.search = match[1];
		ReportController.renderListing();
	},
	"#reportIndex$": function(type, match, ui, page, e){
		ReportController.renderListing();
	},
	"#reportView[?]id=(\\d+)$": function(type, match, ui, page, e){
		new ReportView(match[1], page).getData();
	},
	"#reportView[?]id=(\\d+)&version=draft$": function(type, match, ui, page, e){
		new ReportView(match[1], page).getDraft();
	},
	"#reportView[?]id=(\\d+)&version=draftFallback": function(type, match, ui, page, e){
		new ReportView(match[1], page).getDraftFallback();
	},
	"#reportEdit[?]id=(\\d+)": function(type, match, ui, page, e){
		if (ViewUtil.selector.previousObject){
			ViewUtil.selector.previousObject = null;
			app.checkLoaded();
            return;
        }
        new ReportEdit(match[1], page).getData();
	},
    "#reportNew[?]timestamp=(\\d+)": function(type, match, ui, page, e){
		if (ViewUtil.selector.previousObject){
			ViewUtil.selector.previousObject = null;
			app.checkLoaded();
			return;
		}
		new ReportNew(page).getNewCacheData(match[1]);
	},
	"#reportNew$": function(type, match, ui, page, e){
		if (ViewUtil.selector.previousObject){
			ViewUtil.selector.previousObject = null;
			app.checkLoaded();
			return;
		}
		new ReportNew(page).getTypes();
	},
    "#reportNew[?]type=(\\d+)": function(type, match, ui, page, e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
        new ReportNew(page).getType(match[1]);
    },

   //routes to support pending items
   "#reportView[?]pending=true&timestamp=(\\d+)$": function(type, match, ui, page, e) {
	   new ReportPendingView(page).getNewCacheData(match[1])
   },
});

$(document).on("pageinit", "#reportIndex", function(e){ 
	ReportController.init($(this));
});
var ReportController = $.extend({}, app, {
	init:           function(page) {
		this.indexFilters = {
			typeurl: null,
			status:  null,
			search:  null
		};
		this.queryParams  = ['search'];

		this.page    = page;
		this.content = this.page.find('.ui-content');
		this.footer  = this.page.find('.ui-footer');
		this.$mainLV = this.content.find(".main ul.reports.listview");

		app.init.call(this);
		this.content.find('#reportSearch').keypress(function(e) {
			if (e.which == 13) {
				ReportController.indexFilters.search = $(this).val();
				ReportController.renderListing();
			}
		}).on('change', function(e) {
			if ($(this).val() == '') {
				ReportController.indexFilters.search = null;
				ReportController.renderListing();
			}
		});

		this.$collapsible    = this.content.find('div.ui-collapsible');
		this.indexTypeList   = this.content.find('ul.reporttypes');
		this.indexStatusList = this.content.find('ul.reportstatus');
		this.typeHeading     = this.content.find("h2.reporttype span.label");
		this.statusHeading   = this.content.find("h2.reportstatus span.label");

		this.indexStatusList.on('click', 'a', function() {
			ReportController.$mainLV.empty();
			ReportController.indexFilters.status = $(this).attr('data-status');
			ReportController.statusHeading.text($(this).text());
			ReportController.renderListing();
			ReportController.$collapsible.collapsible('collapse');
		});
		new Gopher('/reporttypes', $.proxy(this.gotReportTypes, this)).run();
	},
	gotReportTypes: function(data) {
		this.indexTypeList.empty();

		var li = $("<li><a class='translated' data-translate='All Reports'>" + OCA.getI18n().gettext('All Reports') + "</a></li>").data('id', null);
		this.indexTypeList.append(li);

		for (var d = 0; d < data.length; d++) {
			var reporttype = data[d];
			li             = $("<li><a>" + reporttype.Name + "</a></li>").data('id', ViewUtil.stripAPI(reporttype.URL));
			this.indexTypeList.append(li);
		}
		this.indexTypeList.on('click', 'li', function() {
			ReportController.typeHeading.text($(this).text());
			ReportController.$collapsible.collapsible('collapse');
			ReportController.indexFilters.typeurl = $(this).data('id');
			ReportController.renderListing();
		});
		this.indexTypeList.listview('refresh');
		this.indexTypeList.children().first().click();
	},
	renderListing:  function() {
		this.checkLoaded();

		this.footer.find('li a.new.report').showIf(OCA.checkEndPoint('REPORTS_ADDREPORT', '/reports', OCA.ACTION_CREATE));

		var query     = this.getListingQuery();
		var heading   = $.isEmptyObject(query) ? "Reports" : "Reports search";
		query.orderby = 'DateCreated';
		var url       = '/reports?' + $.param(query);

		var renderProps = {
			type:         'report',
			selectorMode: this.selectorMode ? {parent: true} : false,
			icon:         'reports'
		};
		this.getListing(url, T(heading), null, renderProps);
	}
});

function ReportView(id, page){
	this.initReportView(id, page);
}
ReportView.prototype = new TypeView;
ReportView.prototype.constructor = ReportView;
ReportView.prototype.initReportView = function(id, page){
	this.initTypeView(id, page, "report");
};
ReportView.prototype.beforeRender = function(){
	TypeView.prototype.beforeRender.call(this);
	if (this.data.Status == 'Draft'){
		for (var i in this.typeData.Fields){
			if (this.typeData.Fields[i].Define == 'STATUS'){
				this.data.FieldData[i] = '99';
				this.typeData.Fields[i].Options.push(['99', 'Draft']);
				break;
			}
		}
	}
}
ReportView.prototype.afterRender = function(){
	TypeView.prototype.afterRender.call(this);

    var mm = this.moreMenu;
    var $deletePopup = this.page.find('#confirmDeleteReport');
    var $deleteDraftPopup = this.page.find('#confirmDeleteReportDraft');
	
	ViewUtil.applyTemplate($deletePopup,{item:'report'},'confirmDelete');

	$deletePopup.find('a.delete').off().on('click', $.proxy(this.deleteItem, this));
	$deleteDraftPopup.find('a.delete').off().on('click', $.proxy(this.discardDraft, this));
	this.hasDraft = (this.data.LatestVersionURL && this.data.LatestVersionURL.split("/").pop() == "draft");
	this.isDraft = (this.data.Status == "Draft");

    mm.find('li.report.delete').on('click', function(){
        mm.popup('close');
        $deletePopup.popup('open');
    });
    mm.find('li.report.discard.draft').on('click', function(){
        mm.popup('close');
        $deleteDraftPopup.popup('open');
    });

    var canEdit = this.data.WritePolicyURL != -1;
	if (this.hasDraft) {
		if (!this.isDraft){
			canEdit = false;
		} else {
			canEdit = canEdit && this.data.IsDraftEditable === true;
		}
	}
    if (this.lock && this.lock.IsLocked && !this.lock.MyLock){ //if object has a lock, but not held by the current user
        canEdit = false;
    }
	this.footer.find('li.edit a').showIf(canEdit);
	mm.find('li.view.draft')
		.showIf(this.hasDraft && !this.isDraft)
		.off().on('click', $.proxy(this.showDraft, this));
	mm.find('li.discard.draft')
		.showIf(this.hasDraft && canEdit);
	mm.find('li.delete')
		.showIf(canEdit);
	this.showInfobar();

}

ReportView.prototype.showInfobar = function(){
	if (this.hasDraft && !this.isDraft){
		util.infobar(
			OCA.getI18n().gettext('A new draft version of this report exists'), null, false,
			'chevron-right', $.proxy(this.showDraft, this)
		);
	} else if (this.hasDraft && this.isDraft && this.data.IsDraftEditable !== true){
        util.infobar(OCA.getI18n().gettext('This report is the subject of a workflow, so it cannot be edited'));
    } else {
        TypeView.prototype.showInfobar.call(this);
    }
}

ReportView.prototype.showDraft = function(){
    $("body").pagecontainer("change", '#reportView?id=' + this.ID + '&version=draft', {allowSamePageTransition: true});
}

ReportView.prototype.getDraft = function(){
	new Gopher(this.endpoint + this.ID + "/draft", $.proxy(this.gotData, this)).run();
}

//report approval tasks attempt to show the draft, but it may not exist. Don't show the error if so, and just fall back to getting the normal report
ReportView.prototype.getDraftFallback = function(){
	new Gopher({url: this.endpoint + this.ID + "/draft", dontProcessError: true}, $.proxy(this.gotData, this),$.proxy(this.getData,this)).run();
}

ReportView.prototype.discardDraft = function(){
	var url = this.endpoint + this.ID
	new Gopher(url + "/draft", function(){
		util.goBack();
		new Gopher(url).uncache();
	}).sendDelete();
}

function ReportEdit(id, page){
	this.initReportEdit(id, page);
}
ReportEdit.prototype = new TypeEdit;
ReportEdit.prototype.constructor = ReportEdit;
ReportEdit.prototype.initReportEdit = function(id, page){
	this.initTypeEdit(id, page, "report");
};
/**
 * Overwrite gotData to autofetch the draft version for editing if it exists
 */
ReportEdit.prototype.gotData = function(data, payload){
	this.data = $.extend(true, {}, data[0]);	//so we can muck about with the data without altering the cache.
    if (payload.extraPayloads.length){
        this.handleExtraPayloads(payload.extraPayloads);
    }
    this.hasDraft = (this.data.LatestVersionURL.split("/").pop() == "draft");
	if (this.hasDraft && this.data.Status != "Draft"){	//if the draft exists but it is not this record, get the draft
		ReportView.prototype.getDraft.call(this);
	} else {
		this.getType();
	}
}
ReportEdit.prototype.afterRender = function(){
	TypeEdit.prototype.afterRender.call(this);
	this.hasDraft = (this.data && this.data.LatestVersionURL && this.data.LatestVersionURL.split("/").pop() == "draft");
	this.isDraft = (this.data.Status == "Draft");
	var self = this;
	this.footer.find('li.draft')
		.showIf(this.typeData.DraftsAllowed||this.hasDraft)
		.find("a").off().on('tap', function(e){
			self.saveDraft();
			e.preventDefault();
			return false;
		});
	ReportView.prototype.showInfobar.call(this);

	if (this.hasDraft && !this.typeData.DraftsAllowed){
		this.footer.find('li.mainsave').hide();
	} else {
		this.footer.find('li.mainsave').show();
	}
}
ReportEdit.prototype.getSLMCType = function(field){
	switch (field.Define){
		case 'EMES':		
			return "emeTreeView";
	}
}
ReportEdit.prototype.saveDraft = function(){
	this.savingDraft = true;
	var submission = this.getSubmission();
	
	if (!submission) {
		if (this.processed) return;
		this.processed = true;
		util.goBack();
	} else if (this.valid(submission)) {
		if (this.hasDraft){
			this.updateDraft(submission);
		} else {
			this.createDraft(submission);
		}
		if (this.ID){	//report has already been published, uncache it
			new Gopher(this.endpoint + this.ID).uncache();
		}
	}
}
/**
 * If the user has clicked publish, overwrite the normal hasChanged method to submit all field values
 * This ensures that a draft can be published with full data, not just whatever has recently changed
 */
ReportEdit.prototype.hasChanged = function(field){
	if (!this.savingDraft || !this.hasDraft){ //this is a publish submission, or creating a draft where none exists
		return TypeNew.prototype.hasChanged.call(this, field);
	} else {
		return TypeEdit.prototype.hasChanged.call(this, field);
	}	
}
ReportEdit.prototype.updateDraft = function(submission){
	if (this.submitted) return;
	this.submitted = true;
	var desc = "Edited " + (this.data.FullName || this.data.Name || 'draft report');
	var url = this.endpoint + this.ID;
	new Gopher({url: url + '/draft', data: submission, desc: desc}, function(){
		util.goBack();
	}, $.proxy(this.dataError, this)).put();

	if (submission.Attachments) {
		this.addRelatedDocuments(submission.Attachments, url);
	}
	if (submission.Detachments){
		this.removeRelatedDocuments(submission.Detachments, url);
	}
}
ReportEdit.prototype.createDraft = function(submission){
	if (this.submitted) return;
	this.submitted = true;
	submission['TypeURL'] = Configuration.getAPIPath() + this.typeEndpoint + '/' + this.typeID;
	var desc = "Created new " + this.typeData.Name + " draft report";
	var url = this.endpoint + this.ID;
	new Gopher({
			url: url + '/draft', 
			data: submission, 
			desc: desc, 
			oldTimestamp: this.timestamp,
			resubmitter: 'ReportDraftResubmitter'
		}, 
		function(){
			util.goBack();
		},
		$.proxy(this.dataError, this)
	).post();
	new Gopher(url).uncache();	//a draft is being created, so the published cache needs to be expired
        fileStore.clearCache('reports', true);	//a draft is being created, so the published cache needs to be expired for all reports, not just reports/drafts
	if (submission.Attachments) {
		this.addRelatedDocuments(submission.Attachments, url);
	}
	if (submission.Detachments){
		this.removeRelatedDocuments(submission.Detachments, url);
	}
}

ReportEdit.prototype.attachAfterSubmit = function(attachments, responsePayloads, data, createdURL){
	if (createdURL && createdURL.indexOf('/draft') != -1) createdURL = createdURL.substr(0, createdURL.indexOf('/draft'));
	TypeEdit.prototype.attachAfterSubmit.call(this, attachments, responsePayloads, data, createdURL);
}

function ReportNew(page){
	this.initReportNew(page);
}
ReportNew.prototype = new ReportEdit;
ReportNew.prototype.constructor = ReportNew;
ReportNew.prototype.initReportNew = function(page){
	this.initReportEdit(null, page);
	this.createURL = '/reports';
}
ReportNew.prototype.hasChanged = TypeNew.prototype.hasChanged;
ReportNew.prototype.submission = function(submission){
	if (this.submitted) return;
    if (submission.Attachments){
		submission.PublishAfterUpload = true; //set flag on submission for processing in offline sync queue
        this.publishSubmissionAfterUpload = submission;
        return this.createDraft(submission);
    }

	this.submitted = true;
	submission['TypeURL'] = Configuration.getAPIPath() + this.typeEndpoint + '/' + this.typeID;
	var desc = "Created new " + this.typeData.Name;
    window.linkParams = {createdObject: 'report', message: desc};
	new Gopher({
			url: this.createURL,
			data: submission, 
			desc: desc, 
			oldTimestamp: this.timestamp,
			resubmitter: 'ReportResubmitter',
			name: this.getName(),
			type: this.type
		}, 
		$.proxy(this.attachAfterSubmit, this, submission.Attachments),
		$.proxy(this.dataError, this)
	).post();
}
ReportNew.prototype.createDraft = function(submission){
	if (this.submitted) return;
	this.submitted = true;
	submission['TypeURL'] = Configuration.getAPIPath() + this.typeEndpoint + '/' + this.typeID;
	var desc = "Created new " + this.typeData.Name + " draft";
    window.linkParams = {createdObject: 'report', message: desc};
	new Gopher({
			url: this.createURL + '/drafts',
			data: submission, 
			desc: desc, 
			oldTimestamp: this.timestamp,
			resubmitter: 'ReportDraftResubmitter',
			name: this.getName(),
			type: this.type
		}, 
		$.proxy(this.attachAfterSubmit, this, submission.Attachments),
		$.proxy(this.dataError, this)
	).post();
    fileStore.clearCache('reports', true);	//a draft is being created, so the published cache needs to be expired for all reports, not just reports/drafts
}

ReportNew.prototype.beforeRender = function(){
	TypeView.prototype.beforeRender.call(this);

	//Set the primary eme as the event
    if (!this.data) this.data = {};
	if (!this.data.FieldData){
		this.data.FieldData = {};
	}
	var pe = OCA.getPrimaryEME();
	if (pe !== null){
		for (var i in this.typeData.Fields){
			if (this.typeData.Fields[i].Define === 'EMES'){
				this.data.FieldData[i] = [pe];
				break;
			}
		}
	}
}

ReportNew.prototype.addRelatedDocuments = function(files, url, publishAfterUpload){
    url = url || this.endpoint + this.ID;
    var docURL = url + '/related/documents';
    this.pendingUploadCount = 0;
    var self = this;
    for (var file in files){
        this.pendingUploadCount++;
        new Gopher({
            url: docURL,
            data: file,
            backgroundMode: true
        }, function(){
            self.pendingUploadCount--;
            if (self.pendingUploadCount === 0){
                var submission = self.publishSubmissionAfterUpload;
				if (submission || publishAfterUpload){
					var data = {"FieldData": {}}; //dont need to change any values, just submit to /report/123 and not /report/123/draft
					url = url.replace('/drafts', '');
					new Gopher({url: url, data: data, desc: "Publishing report", backgroundMode: true}, function(){
					}).put();
				}
            } else {
                //still waiting for uploads to finish
            }
        }).uploadFile();
    }
}

function ReportPendingView(page) {
	this.initReportPending(page);
}
ReportPendingView.prototype                = new ReportView;
ReportPendingView.prototype.constructor    = ReportPendingView;
ReportPendingView.prototype.initReportPending = function(page) {
	this.initReportView(null, page);
	this.createURL = '/reports';

};
ReportPendingView.prototype.afterRender    = function() {
	ReportView.prototype.afterRender.call(this);

	var $deletePopup = this.page.find('#confirmDeleteReport');
	$deletePopup.find('a.delete').off().on('click', $.proxy(this.deleteCacheItem, this, this.cache.info.url, this.timestamp));
	this.footer.find('li.edit a').prop('href', '#reportNew?timestamp=' + this.timestamp);
};