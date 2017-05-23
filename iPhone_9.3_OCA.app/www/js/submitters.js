function Resubmitter(cache){
	this.init(cache);
	this.run();
}
Resubmitter.prototype.init = function(cache){
	if (!cache) return;
	
	this.cache = cache;
	this.data  = JSON.parse(cache.ajax.data);
	this.url   = cache.info.url;
}
Resubmitter.prototype.run = function(){}
Resubmitter.prototype.success = function(response, data, createdURL){
	GopherQueue.flushOut(this.cache, data, createdURL);
}
Resubmitter.prototype.failure = function(xhr, error){
	if (error){
        //OCA validation request response
        if (error.errors && error.errors.length){
            if (this.cache.info.invalid){
                //do nothing. This item is already known to be invalid
            } else {
                util.infobar(OCA.getI18n().gettext('Validation error while attempting to sync offline items. Please review the queued submissions.'), '#storage', 30);
                this.cache.info.invalid = true;
                this.cache.info.errors = error.errors;
            }
        }
        GopherQueue.submitting = false;
		GopherQueue.flush(); //this item failed but did reach the server,so continue to process items.
	} else {
		GopherQueue.stepOff();
	}
}

function EMEResubmitter(cache){
	this.init(cache);
	this.run();
}
EMEResubmitter.prototype = new Resubmitter;
EMEResubmitter.prototype.constructor = EMEResubmitter;
EMEResubmitter.prototype.run = function(){
	new Gopher({url: this.url, data: this.data, backgroundMode: true}, $.proxy(this.success, this),$.proxy(this.failure, this)).post(false);
}
EMEResubmitter.prototype.success =  function(responsePayloads, data, createdURL){
	Resubmitter.prototype.success.call(this, responsePayloads, data, createdURL);
	if (this.data.Attachments && createdURL){
		TypeEdit.prototype.addRelatedDocuments.call({ID: createdURL.split("/").pop(), endpoint: '/eme/'}, this.data.Attachments);
	}
}


function ReportResubmitter(cache){
	this.init(cache);
	this.run();
}
ReportResubmitter.prototype = new Resubmitter;
ReportResubmitter.prototype.constructor = ReportResubmitter;
ReportResubmitter.prototype.run = function(){
	new Gopher({url: this.url, data: this.data, backgroundMode: true}, $.proxy(this.success, this),$.proxy(this.failure, this)).post(false);
}
ReportResubmitter.prototype.success = function(responsePayloads, data, createdURL){
	Resubmitter.prototype.success.call(this, responsePayloads);
	if (this.data.Attachments && createdURL){
		if (createdURL && createdURL.indexOf('/draft') != -1) createdURL = createdURL.substr(0, createdURL.indexOf('/draft'));
		TypeEdit.prototype.addRelatedDocuments.call({}, this.data.Attachments, createdURL);
	}
}

function ReportDraftResubmitter(cache){
	this.init(cache);
	this.run();
}
ReportDraftResubmitter.prototype = new Resubmitter;
ReportDraftResubmitter.prototype.constructor = ReportDraftResubmitter;
ReportDraftResubmitter.prototype.run = function(){
	new Gopher({url: this.url, data: this.data, backgroundMode: true}, $.proxy(this.success, this),$.proxy(this.failure, this)).post(false);
}
ReportDraftResubmitter.prototype.success = function(responsePayloads, data, createdURL){
	Resubmitter.prototype.success.call(this, responsePayloads);
	if (this.data.Attachments && createdURL){
		if (createdURL && createdURL.indexOf('/draft') != -1) createdURL = createdURL.substr(0, createdURL.indexOf('/draft'));

		if (this.data.PublishAfterUpload){ //if the report needs to upload files and then publish the report
			ReportNew.prototype.addRelatedDocuments.call({}, this.data.Attachments, createdURL, true);
		} else {
			TypeEdit.prototype.addRelatedDocuments.call({}, this.data.Attachments, createdURL);
		}
	}
}

function LogResubmitter(cache){
	this.init(cache);
	this.run();
}
LogResubmitter.prototype = new Resubmitter;
LogResubmitter.prototype.constructor = LogResubmitter;
LogResubmitter.prototype.run = function(){
	new Gopher({url: this.url, data: this.data, backgroundMode: true}, $.proxy(this.success, this),$.proxy(this.failure, this)).post(false);
}
LogResubmitter.prototype.success = function(responsePayloads, data, createdURL){
	Resubmitter.prototype.success.call(this, responsePayloads);
	if (this.data.Attachments && createdURL){
		TypeEdit.prototype.addRelatedDocuments.call({ID: createdURL.split("/").pop(), endpoint: '/log/'}, this.data.Attachments);
	}
}

function TaskResubmitter(cache){
	this.init(cache);
	this.run();
}
TaskResubmitter.prototype = new Resubmitter;
TaskResubmitter.prototype.constructor = TaskResubmitter;
TaskResubmitter.prototype.run = function(){
	new Gopher({url: this.url, data: this.data, backgroundMode: true}, $.proxy(this.success, this),$.proxy(this.failure, this)).post(false);
}
TaskResubmitter.prototype.success = function(responsePayloads, data, createdURL){
	Resubmitter.prototype.success.call(this, responsePayloads);
	if (this.data.Attachments && createdURL){
		TypeEdit.prototype.addRelatedDocuments.call({ID: createdURL.split("/").pop(), endpoint: '/task/'}, this.data.Attachments);
	}
}

function AssetResubmitter(cache){
	this.init(cache);
	this.run();
}
AssetResubmitter.prototype = new Resubmitter;
AssetResubmitter.prototype.constructor = AssetResubmitter;
AssetResubmitter.prototype.run = function(){
	new Gopher({url: this.url, data: this.data, backgroundMode: true}, $.proxy(this.success, this),$.proxy(this.failure, this)).post(false);
}
AssetResubmitter.prototype.success = function(responsePayloads, data, createdURL){
	Resubmitter.prototype.success.call(this, responsePayloads, data, createdURL);
	if (this.data.Attachments && createdURL){
		TypeEdit.prototype.addRelatedDocuments.call({ID: createdURL.split("/").pop(), endpoint: '/asset/'}, this.data.Attachments);
	}
}