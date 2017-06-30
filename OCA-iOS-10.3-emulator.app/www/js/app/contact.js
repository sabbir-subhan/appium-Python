router.add({
	"#contactgroupTreeView[?]id=(\\d+)$": function(type, match){
		ContactController.renderListing(match[1], false);
	},
	"#contactgroupTreeView[?]id=0&query=(.*)": function(type, match){
		ContactController.indexFilters.search = match[2];
		ContactController.renderListing(match[1]);
	},
	"#contactgroupTreeView[?]selector=true&id=(\\d+)": function(type, match, ui, page, e){
		ContactController.renderListing(match[1], true);
	},
	"#contactgroupTreeView[?]mode=contacts&selector=true&id=(\\d+)": function(type, match, ui, page, e){
		ContactController.renderListing(match[1], 'contacts');
	},
	"#contactgroupTreeView[?]mode=groups&selector=true&id=(\\d+)": function(type, match, ui, page, e){
		ContactController.renderListing(match[1], 'groups');
	},
	"#contactgroupView[?]id=(\\d+)": function(type, match, ui, page, e){
		new ContactGroupView(match[1], page).getData();
	},
	"#contactgroupEdit[?]id=(\\d+)": function(type, match, ui, page, e){
		if (ViewUtil.selector.previousObject){
			ViewUtil.selector.previousObject = null;
			app.checkLoaded();
			return;
		}
		new ContactGroupEdit(match[1], page).getData();
	},
	"#contactgroupNew[?]parent=(\\d+)&timestamp=(\\d+)$": function(type, match, ui, page, e){
		if (ViewUtil.selector.previousObject){
			ViewUtil.selector.previousObject = null;
			app.checkLoaded();
			return;
		}
		new ContactGroupNew(match[1], page).getNewCacheData(match[2]);
	},
	"#contactgroupNew[?]parent=(\\d+)$": function(type, match, ui, page, e){
		if (ViewUtil.selector.previousObject){
			ViewUtil.selector.previousObject = null;
			app.checkLoaded();
			return;
		}
		new ContactGroupNew(match[1], page).getTypes();
	},
	"#contactView[?]id=(\\d+)": function(type, match, ui, page, e){
		new ContactView(match[1], page).getData();
	},
	"#contactEdit[?]id=(\\d+)": function(type, match, ui, page, e){
		if (ViewUtil.selector.previousObject){
			ViewUtil.selector.previousObject = null;
			app.checkLoaded();
			return;
		}
		new ContactEdit(match[1], page).getData();
	},
	"#contactNew[?]parent=(\\d+)$": function(type, match, ui, page, e){
		if (ViewUtil.selector.previousObject){
			ViewUtil.selector.previousObject = null;
			app.checkLoaded();
			return;
		}
		new ContactNew(match[1], page).getTypes();
	},
	"#contactNew[?]parent=(\\d+)&timestamp=(\\d+)$": function(type, match, ui, page, e){
		if (ViewUtil.selector.previousObject){
			ViewUtil.selector.previousObject = null;
			app.checkLoaded();
			return;
		}
		new ContactNew(match[1], page).getNewCacheData(match[2]);
	},
	"#contactNew[?]parent=(\\d+)&type=(\\d+)$": function(type, match, ui, page, e){
		if (ViewUtil.selector.previousObject){
			ViewUtil.selector.previousObject = null;
			app.checkLoaded();
			return;
		}
		new ContactNew(match[1], page).getType(match[2]);
	},
	"#contactNew[?]parent=(\\d+)&type=(\\d+)&timestamp=(\\d+)": function(type, match, ui, page, e){
		if (ViewUtil.selector.previousObject){
			ViewUtil.selector.previousObject = null;
			app.checkLoaded();
			return;
		}
		new ContactNew(match[1], page).getNewCacheData(match[3]);
	},
	"#contactImport[?]parent=(\\d+)": function(type, match, ui, page, e){
		ContactImport.load(match[1], page);
	},

   //routes to support pending items
   "#contactgroupTreeView[?]pending=true&parent=(\\d+)&timestamp=(\\d+)$": function(type, match, ui, page, e) {
	   var pendingKey = 'pending-' + match[2] + '-' + match[1];
	   ContactController.renderListing(pendingKey, false);
   },

   "#contactgroupView[?]pending=true&parent=(\\d+)&timestamp=(\\d+)$": function(type, match, ui, page, e) {
	   new ContactGroupPendingView(match[1], page).getNewCacheData(match[2])
   },

   "#contactgroupNew[?]pending=true&parent=(\\d+)$": function(type, match, ui, page, e) {
	   if (ViewUtil.selector.previousObject) {
		   ViewUtil.selector.previousObject = null;
		   app.checkLoaded();
		   return;
	   }
	   new ContactGroupPendingNew(match[1], page).getTypes();
   },

   "#contactgroupNew[?]pending=true&parent=(\\d+)&timestamp=(\\d+)$": function(type, match, ui, page, e) {
	   if (ViewUtil.selector.previousObject) {
		   ViewUtil.selector.previousObject = null;
		   app.checkLoaded();
		   return;
	   }
	   new ContactGroupPendingNew(match[1], page).getNewCacheData(match[2]);
   },
   "#contactView[?]pending=true&parent=(\\d+)&timestamp=(\\d+)$": function(type, match, ui, page, e) {
	   new ContactPendingView(match[1], page).getNewCacheData(match[2])
   },

   "#contactNew[?]pending=true&parent=(\\d+)$": function(type, match, ui, page, e) {
	   if (ViewUtil.selector.previousObject) {
		   ViewUtil.selector.previousObject = null;
		   app.checkLoaded();
		   return;
	   }
	   new ContactPendingNew(match[1], page).getTypes();
   },

   "#contactNew[?]pending=true&parent=(\\d+)&timestamp=(\\d+)$": function(type, match, ui, page, e) {
	   if (ViewUtil.selector.previousObject) {
		   ViewUtil.selector.previousObject = null;
		   app.checkLoaded();
		   return;
	   }
	   new ContactPendingNew(match[1], page).getNewCacheData(match[2]);
   },
});

$(document).on("pageinit", "#contactgroupTreeView", function(e){ 
	ContactController.init($(this));
});
var ContactController = $.extend({}, app, {
	returnedLists: 0, //counter to detemine if the list of groups AND the list of contacts has returned
	init: function(page){
		this.page = page;
		this.content = this.page.find('.ui-content');
		this.footer = this.page.find('.ui-footer');
		app.init.call(this);
		this.$mainLV   = this.content.find(".main ul.groups.listview");
		this.$secondLV = this.content.find(".secondary ul.contacts.listview");
		this.content.find('#contactSearch').keypress(function(e){
			if (e.which == 13){
				ContactController.indexFilters.search = $(this).val();
				ContactController.renderListing(0, ContactController.selectorMode);
			}
		}).on('change', function(e){
			if ($(this).val() == ''){
				ContactController.indexFilters.search = $(this).val();
				ContactController.renderListing(0, ContactController.selectorMode);
			}
		});

		OCA.name('/contactgroup/0', 'Contact Directory'); //special name for contactgroup root
	},
	renderListing: function(id, selectorMode){
		if (!id) {
			id = 0;
		}
		this.selectorMode = selectorMode || false;

		var newArg  = 'parent=' + id;
		var viewArg = 'id=' + id;
		if (isNaN(id) && id.indexOf('pending-') === 0) {
			var bits            = id.split("-");
			this.setPendingItem('pending/contactgroup', bits[1], bits[2]);
			this.setCurrentItem('pending/contactgroup', bits[1]);
			newArg  = 'pending=true&parent=' + bits[1];
			viewArg = 'pending=true&parent=' + bits[2] + '&timestamp=' + bits[1];
			this.pendingItem.ID  = bits[1];
			this.currentItem.URL = "/pending/contactgroup/" + this.pendingItem.ID;
		} else {
			this.setPendingItem(null);
			this.setCurrentItem('contactgroup', id);
		}

		//set visibilty of elements depending on whether or not we are in the contact directory root
		var atRoot = (id == 0);
		this.footer.find('.groupView').visibleIf(!atRoot);
		this.page.find('#contactgroupTreeMore .ingroup').showIf(!atRoot);
		this.content.find('div.heading-row a.level-up').visibleIf(!atRoot);
		
		this.page.find('.selector-mode').showIf(this.selectorMode);
		this.page.find('.normal-mode').showIf(!this.selectorMode);

		//check permissions
		var newGroup = OCA.checkEndPoint('CONTACTSGROUPS_ADDGROUP','/contactgroup/{groupid:int}/contactgroups',OCA.ACTION_CREATE);
		var newContact = OCA.checkEndPoint('CONTACTSGROUPS_ADDCONTACT','/contactgroup/{groupid:id}/contacts',OCA.ACTION_CREATE) && !atRoot;
		this.page.find('#openContactGroupTreeMore').showIf(newGroup || newContact);

		//set routes based on the current group
		this.footer.find('a.groupView').prop('href', '#contactgroupView?' + viewArg);
		var $more = this.page.find('#contactgroupTreeMore');
		$more.find('a.new.contactgroup').prop('href', '#contactgroupNew?' + newArg);
		$more.find('li.new.contactgroup').showIf(newGroup);
		$more.find('a.new.contact').prop('href', '#contactNew?' + newArg);
		$more.find('li.new.contact').showIf(newContact);
		$more.find('a.import.contact').prop('href', '#contactImport?parent=' + id);
		$more.find('li.import.contact').showIf(newContact && device.platform != "Mobile Interface");

		this.returnedLists = 0;

		var heading, groupsURL, contactsURL, showContacts = true;
		var query = this.getListingQuery();

		if ($.isEmptyObject(query)) {	//normal tree browsing mode
			heading      = this.currentItem.Name;
			groupsURL   = this.currentItem.URL + '/contactgroups';
			contactsURL = this.currentItem.URL + '/contacts';
			if (id == 0 || this.selectorMode == 'groups'){ //no contacts at root or in group only selector mode
				showContacts = false;
			}
		} else {						//search mode
			heading      = 'Contact search';
			groupsURL   = '/contactgroups?' + $.param(query);
			contactsURL = '/contacts?' + $.param(query);
		}

		var selectProps = this.selectorMode
			? {parent: true}	//contact groups may contain other groups or contacts
			: false;
		if (this.selectorMode === "contacts") {
			selectProps.mode = this.selectorMode;
			selectProps.unselectable = true;
		} else if (this.selectorMode === 'groups'){
			selectProps.mode = 'groups';
		}
		this.getListing(groupsURL, heading, $.proxy(this.gotContactGroups, this), {
			type:         'contactgroupTree',
			selectorMode: selectProps,
			noItemsMsg: false	//need to consider both listviews together - handled in checkLoaded
		});

		if (showContacts){
			this.getSecondaryListing(contactsURL, $.proxy(this.gotContacts, this), {
				type:         'contact',
				icon:         'contacts',
				selectorMode: this.selectorMode,
				noItemsMsg: false
			});
		} else {
			this.returnedLists = 1; //pretend we already have 1 list because contacts arent being fetched
			this.getSecondaryListing(false); //just clean/hide up any existing data
		}
	},
	gotContactGroups: function(data, extra){
		this.returnedLists++;
		this.checkLoaded();
	},
	gotContacts: function(data, extra){
		this.returnedLists++;
		this.checkLoaded();
	},
	checkLoaded: function(){
		app.checkLoaded.call(this);
		if (this.returnedLists == 2 && this.$secondLV.children().length === 0 && this.$mainLV.children().length === 0) {
			this.$mainLV.append($("<li />").data('theme', 'e').text(OCA.getI18n().gettext('There are no items to display'))).listview('refresh');
		}
	}
});

function ContactGroupView(id, page){
	this.initContactGroupView(id, page);
}
ContactGroupView.prototype = new TypeView;
ContactGroupView.prototype.constructor = ContactGroupView;
ContactGroupView.prototype.initContactGroupView = function(id, page){
	this.initTypeView(id, page, "contactgroup");
	this.policies.push("Send");
	this.deleteLevels--; //groups have to go back one extra level
    this.supportsLocation = false;
};
ContactGroupView.prototype.renderRelations = $.noop;
ContactGroupView.prototype.renderOptions = function(){
	this.listview.append($("<li data-role='list-divider'/>").text(OCA.getI18n().gettext("Options")));
	this.typeData["IsMailingList"] = {
		Options: [["0",OCA.getI18n().gettext("None")],["1",OCA.getI18n().gettext("Mailing list")]], 
		Label: OCA.getI18n().gettext("Compliance mode")
	};
	this.typeData["IsOrganisation"] = {
		Options: [["0",OCA.getI18n().gettext("No")],["1",OCA.getI18n().gettext("Yes")]], 
		Label: OCA.getI18n().gettext("Organisation")
	};
	this.typeData["IsAgency"] = {
		Options: [["0",OCA.getI18n().gettext("No")],["1",OCA.getI18n().gettext("Yes")]], 
		Label: OCA.getI18n().gettext("Agency")
	};
	this.optRender(this.typeData["IsMailingList"],	this.data ? this.data["IsMailingList"]	? "1" : "0" : null);
	this.optRender(this.typeData["IsOrganisation"], this.data ? this.data["IsOrganisation"] ? "1" : "0" : null);
	this.optRender(this.typeData["IsAgency"],		this.data ? this.data["IsAgency"]		? "1" : "0" : null);
}
ContactGroupView.prototype.afterRender = function(){
	TypeView.prototype.afterRender.call(this);

	var canEdit    = (this.data.WritePolicyURL != -1)
	var sendComm    = (this.data.SendPolicyURL  != -1 && OCA.checkFeature('OUTBOUNDCOMMS_SEND'));
	var newGroup = (this.data.WritePolicyURL != -1 && OCA.checkEndPoint('CONTACTSGROUPS_ADDGROUP','/contactgroup/{groupid:int}/contactgroups',OCA.ACTION_CREATE));
	var newContact  = (this.data.WritePolicyURL != -1 && OCA.checkEndPoint('CONTACTSGROUPS_ADDCONTACT','/contactgroup/{groupid:id}/contacts',OCA.ACTION_CREATE));

    var $mm = this.moreMenu;
	$mm.find('li.delete.contactgroup').showIf(canEdit);
    $mm.find('li.send').showIf(sendComm);
    $mm.find('li.new.contactgroup').showIf(newGroup);
    $mm.find('li.new.contact').showIf(newContact);
	this.page.find('#openContactGroupViewMore').showIf(canEdit || sendComm || newGroup || newContact);

    $mm.find('li.new.contactgroup a').prop('href', '#contactgroupNew?parent=' + this.ID);
    $mm.find('li.new.contact a').prop('href', '#contactNew?parent=' + this.ID);
    $mm.find('li.import.contact a').prop('href', '#contactImport?parent=' + this.ID).showIf(device.platform != "Mobile Interface");
    $mm.find('li.send a').off().on('click', $.proxy(this.sendComm, this));

    var $deletePopup = this.page.find('#confirmDeleteContactGroup');
	ViewUtil.applyTemplate($deletePopup,{item:'contactgroup',label:OCA.getI18n().gettext('contact group')},'confirmDelete');
	$deletePopup.find('a.delete').off().on('click', $.proxy(this.deleteItem, this));
    $mm.find('li.delete.contactgroup').on('click', function(){
        $mm.popup('close');
        $deletePopup.popup('open');
    });
	
}
ContactGroupView.prototype.sendComm = function(){
	message.sendTo('contactgroup', this.ID, this.data.Name);
}

function ContactGroupEdit(id, page){
	this.initContactGroupEdit(id, page);
}
ContactGroupEdit.prototype = new TypeEdit;
ContactGroupEdit.prototype.constructor = ContactGroupEdit;
ContactGroupEdit.prototype.initContactGroupEdit = function(id, page){
	this.initTypeEdit(id, page, "contactgroup");
	this.policies.push("Send");
    this.supportsLocation = false;
};
ContactGroupEdit.prototype.renderRelations = $.noop;
ContactGroupEdit.prototype.renderOptions = function(){
	ContactGroupView.prototype.renderOptions.call(this);
}

function ContactGroupNew(parentID, page){
	this.initContactGroupNew(parentID, page);
}
ContactGroupNew.prototype = new ContactGroupEdit;
ContactGroupNew.prototype.constructor = ContactGroupNew;
ContactGroupNew.prototype.initContactGroupNew = function(parentID, page){
	this.parentID = parentID;
	this.initContactGroupEdit(null, page, "contactgroup");
	this.createURL = '/contactgroup/' + this.parentID + '/contactgroups';
}
ContactGroupNew.prototype.hasChanged = TypeNew.prototype.hasChanged;
ContactGroupNew.prototype.submission = function(submission){
	if (this.submitted) return;
	this.submitted = true;
	submission['TypeURL'] = Configuration.getAPIPath() + this.typeEndpoint + '/' + this.typeID;
	var desc = "Created new " + this.typeData.Name;
	new Gopher({url: this.createURL, data: submission, desc: desc, oldTimestamp: this.timestamp, name: this.getName(), type: this.type}, function(){
		util.goBack();
	}, $.proxy(this.dataError, this)).post();
};

function ContactGroupPendingView(parentID, page) {
	this.initContactGroupPending(parentID, page);
}
ContactGroupPendingView.prototype                         = new ContactGroupView;
ContactGroupPendingView.prototype.constructor             = ContactGroupPendingView;
ContactGroupPendingView.prototype.initContactGroupPending = function(parentID, page) {
	this.parentID = parentID;
	this.initContactGroupView(null, page);
	this.createURL = '/contactgroup/' + this.parentID + '/contactgroups';

};
ContactGroupPendingView.prototype.afterRender             = function() {
	ContactGroupView.prototype.afterRender.call(this);

	var $mm = this.moreMenu;
	$mm.find('li.new.contactgroup a').prop('href', '#contactgroupNew?pending=true&parent=' + this.timestamp);
	$mm.find('li.new.contact a').prop('href', '#contactNew?pending=true&parent=' + this.timestamp);
	$mm.find('li.send.contactgroup a').hide(); //cant send pending group
	$mm.find('li.import.contact a').hide();

	var $deletePopup = this.page.find('#confirmDeleteContactGroup');
	$deletePopup.find('a.delete').off().on('click', $.proxy(this.deleteCacheItem, this, this.createURL, this.timestamp));
	//link edit to the pending new route
	var editRoute = '#contactgroupNew?pending=true&parent=' + this.parentID + '&timestamp=' + this.timestamp;
	if (this.cache.info.url.indexOf('/pending') === -1){ //if this is a child of a normal item, adjust the edit route
		editRoute = editRoute.replace('pending=true&', '');
	}
	this.footer.find('li.edit a').prop('href', editRoute);
};

//for creating a new item as the child of a pending item
function ContactGroupPendingNew(parentID, page) {
	this.initContactGroupPendingNew(parentID, page);
}
ContactGroupPendingNew.prototype                            = new ContactGroupNew;
ContactGroupPendingNew.prototype.constructor                = ContactGroupPendingNew;
ContactGroupPendingNew.prototype.initContactGroupPendingNew = function(parentID, page) {
	this.initContactGroupNew(parentID, page);
	this.createURL = '/pending' + this.createURL;

};

function ContactView(id, page){
	this.initContactView(id, page);
}
ContactView.prototype = new TypeView;
ContactView.prototype.constructor = ContactView;
ContactView.prototype.initContactView = function(id, page){
	this.initTypeView(id, page, "contact");
	this.policies.push("Send");

	var more = this.page.find('#moreMenu');
	more.find('li.send').showIf(OCA.checkFeature('OUTBOUNDCOMMS_SEND'));
};
ContactView.prototype.beforeRender = function() {
	for (var t in this.typeData.Tabs) {
		if (this.typeData.TabFields) {
			this.typeData.TabFields[t] = this.applyFieldAccessLevels(this.typeData.TabFields[t]);
		}
	}

	var profileFields = $.extend(true, {}, this.typeData.ProfileFields);
	this.typeData.ProfileFields = {};
	for (var p in this.typeData.Profiles){
		//so that the edit view can do a delta for each profile, hack it into this format where there is a copy of the profile fields for each profile
		this.typeData.ProfileFields[p] = ContactView.prototype.createProfileFields(profileFields, p);
		this.typeData.ProfileFields[p] = this.applyFieldAccessLevels(this.typeData.ProfileFields[p]);
	}

	this.typeData.Fields = this.typeData.TabFields
}
ContactView.prototype.render = function(){
	this.content.empty();
	this.listview = $("<ul />");
	this.beforeRender();
	
	var lastRow;
	this.typeData.Fields = {};
	for(var t in this.typeData.Tabs){
		if (!this.typeData.TabFields) continue;

		this.listview.append($("<li data-role='list-divider'/>").text(this.typeData.Tabs[t].Name + " " + OCA.getI18n().gettext("Tab")));
		this.renderFields(this.typeData.TabFields[t], this.data.BaseFieldData);
		lastRow = this.listview.children().last()
		if (lastRow.data('role') == 'list-divider') lastRow.remove(); //last row added no fields

		this.typeData.Fields = $.extend(this.typeData.Fields, this.typeData.TabFields[t]); //certain shared code needs to be able to look up fields by ID, so copy them over
	}
	for(var p in this.typeData.Profiles){
		this.profileSection(this.typeData.Profiles[p]);
		this.renderFields(this.typeData.ProfileFields[p], this.data.ProfileFieldData[p]);
		lastRow = this.listview.children().last()
		if (lastRow.data('role') == 'list-divider') lastRow.remove(); //last row added no fields

		this.typeData.Fields = $.extend(this.typeData.Fields, this.typeData.ProfileFields[t]); //certain shared code needs to be able to look up fields by ID, so copy them over
	}

	this.renderOptions();
	this.renderPolicies();
	this.content.append(this.listview);
	this.listview.listview();
	this.afterRender();
	$.mobile.loading('hide');
};
/**
 * Create a copy of the provided profile fields and apply any profile-specific settings
 * @param profileFields
 * @param profileID
 */
ContactView.prototype.createProfileFields = function(profileFields, profileID){
	var copy = $.extend(true, {}, profileFields);	//make a fresh copy so that each profile can be handled independently

	for (var fID in profileFields){
		if (profileFields[fID].RequiredOnProfiles && profileFields[fID].RequiredOnProfiles.length){
			if (profileFields[fID].RequiredOnProfiles.indexOf(profileID) !== -1){
				copy[fID].Required = true;	//this field is required on this profile, so mark it as such for this copy
			} else {
				copy[fID].Required = false;
			}
		}
	}
	return copy;

};

ContactView.prototype.sortFields = function(fieldObj){
	var fields = [];
	for (var id in fieldObj){
		var field = fieldObj[id];
		field["ID"] = id;
		//hack so that surname is next to first name
		if (field.Define == "SURNAME"){
			field.X = "1"; 
			field.Y = "0";
		} else if (field.X == "1" && field.Y == "0"){
			field.X = "0";
			field.Y = "1";
		}
		fields.push(field);
	}
	fields.sort(function(a, b){
		var aIdx = a.Y * 2 + a.X;
		var bIdx = b.Y * 2 + b.X;
		return aIdx - bIdx;
	});
	return fields;
};
ContactView.prototype.renderRelations = $.noop;
ContactView.prototype.renderOptions = function(){
	this.listview.append($("<li data-role='list-divider'/>").text(OCA.getI18n().gettext("Options")));
	this.typeData["IsUnsubscribed"] = {
		Options: [["0",OCA.getI18n().gettext("Active")], ["1",OCA.getI18n().gettext("Unsubscribed")]], 
		Label: OCA.getI18n().gettext("Communication Status"),
		ID: 'IsUnsubscribed'
	};
	this.optRender(this.typeData["IsUnsubscribed"], this.data ? this.data["IsUnsubscribed"] ? "1" : "0" : null);
}
ContactView.prototype.profileSection = function(profile){
//	this.listview.append($("<li />").data('role', 'list-divider').text(profile.label + " Profile"));
	var schedule = [];
	for (var s=0; s < profile.schedule.length; s++){
		schedule[s] = this.formatSchedule(profile.schedule[s]);
	}
	schedule = schedule.join(", ");
	this.listview.append($("<li data-role='list-divider'/>").text(profile.label + " " + OCA.getI18n().gettext("Profile") + " : " + schedule));
};
ContactView.prototype.formatSchedule = function(schedule){
	var str = util.shortDays[schedule.sday];					//e.g. Mon
	if (schedule.sday != schedule.eday) {
		str += "-"  + util.shortDays[schedule.eday];			//-Fri
	}
	
	var start = this.formatTime(schedule.stime);
	var end = this.formatTime(schedule.etime);
	if (start != "12am" || end != "12am"){
		str += " " + start + "-" + end;
	}
	return str;
};
ContactView.prototype.formatTime = function(time){
	var bits = time.split(":");
	bits[2] = "am";												//ignore seconds, display meridian
	if (bits[0] == 0 || bits[0] == 24){							//0am = 24am
		bits[0] = 12;
	} else if (bits[0] > 12){
		bits[0] -= 12;
		bits[2] = "pm";
	} else {
		bits[0] *= 1;											//convert to number to lose leading zeroes
	}
	var str = bits[0];
	if (bits[1] != "00") str += ":" + bits[1];					// minutes not empty, so display
	str += bits[2];
	return str;
};
ContactView.prototype.emailRender = function(field, data){
	var row = this.fieldRender(field, data);
	var self = this;
	if (data && this.externalHandlers) {
		row .wrapInner("<a href='#messagePage' />")
			.on('click', function(){
				message.sendTo('contact', self.ID, self.data.FullName);
			})
            .attr('data-icon', 'inbox');
	}
};
ContactView.prototype.afterRender = function(){
	this.footer.find('li.edit a').showIf(this.data.WritePolicyURL != -1);
    var $mm = this.moreMenu;
    $mm.find('li.delete').showIf(this.data.WritePolicyURL != -1);
    $mm.find('li.send').showIf(this.data.SendPolicyURL != -1);
    $mm.showIf(this.data.WritePolicyURL != -1 || this.data.SendPolicyURL != -1);
	
	this.page.find('.ui-footer a.edit').prop('href', '#contactEdit?id='+this.ID);
    $mm.find('a.send').off().on('click', $.proxy(this.sendComm, this));
    $mm.find('a.save').off().on('click', $.proxy(this.saveToDevice, this));
    $mm.find('li.save.contact').showIf(device.platform != "Mobile Interface");

    var $deletePopup = this.page.find('#confirmDeleteContact');
	ViewUtil.applyTemplate($deletePopup,{item:'contact'},'confirmDelete');
    $deletePopup.find('a.delete').off().on('click', $.proxy(this.deleteItem, this));
    $mm.find('li.delete').on('click', function(){
        $mm.popup('close');
        $deletePopup.popup('open');
    });
}
ContactView.prototype.sendComm = function(){
	message.sendTo('contact', this.ID, this.data.FullName);
}
ContactView.prototype.saveToDevice = function(){
	ContactExport.save(this);
}

function ContactEdit(id, page){
	this.initContactEdit(id, page);
}
ContactEdit.prototype = new TypeEdit;
ContactEdit.prototype.constructor = ContactEdit;
ContactEdit.prototype.initContactEdit = function(id, page){
	this.initTypeEdit(id, page, "contact");
	this.policies.push("Send");
    this.supportsLocation = false;
};
//copy functions from ContactView
ContactEdit.prototype.beforeRender = ContactView.prototype.beforeRender;
ContactEdit.prototype.render = ContactView.prototype.render;
ContactEdit.prototype.renderRelations = $.noop;
ContactEdit.prototype.renderOptions = ContactView.prototype.renderOptions;
ContactEdit.prototype.sortFields = ContactView.prototype.sortFields;
ContactEdit.prototype.submit = function(){
	var submission = {
		BaseFieldData: {},
		ProfileFieldData: {}
	};
	var submit = false, field = null, id;
	
	for (var t in this.typeData.Tabs){
		for (id in this.typeData.TabFields[t]){
			field = this.typeData.TabFields[t][id];
			if (this.hasChanged(field)) {
				submission.BaseFieldData[id] = field.Input.val();
				if (field.Input.getAPIValue){ //overwrite the val() output if there's a specialised function to get the submission value
					submission.BaseFieldData[id] = field.Input.getAPIValue();
				}
				submit = true;
			}
		}
	}
	for (var p in this.typeData.Profiles){
		submission.ProfileFieldData[p] = {};
		for (id in this.typeData.ProfileFields[p]){
			field = this.typeData.ProfileFields[p][id];
			if (this.hasChanged(field)) {
				submission.ProfileFieldData[p][id] = field.Input.val();
				if (field.Input.getAPIValue){ //overwrite the val() output if there's a specialised function to get the submission value
					submission.ProfileFieldData[p][id] = field.Input.getAPIValue();
				}
				submit = true;
			}
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
	
	if (!submit) {
		if (this.processed) return;
		this.processed = true;
		util.goBack();
		return;
	}

	if (this.valid()) {
		this.submission(submission);
	}
};
ContactEdit.prototype.valid = function(){
	var valid = true, id, field, val;
	var errors = [];
	for (var t in this.typeData.Tabs){
		for (id in this.typeData.TabFields[t]){
			field = this.typeData.TabFields[t][id];
			if (field.Required && field.Input){
				val = field.Input.val()
				if (!val || JSON.stringify(val) === JSON.stringify([]) || JSON.stringify(val) === JSON.stringify({})){
					valid = false;
					errors.push(field.Label);
				}
			}
		}
	}
	for (var p in this.typeData.Profiles){
		for (id in this.typeData.ProfileFields[p]){
			field = this.typeData.ProfileFields[p][id];
			if (field.Required && field.Input){
				val = field.Input.val()
				if (!val || JSON.stringify(val) === JSON.stringify([]) || JSON.stringify(val) === JSON.stringify({})){
					valid = false;
					errors.push(field.Label);
				}
			}
		}
	}
	
	if (!valid){
		util.alertDialog(OCA.getI18n().translate("Required fields are not filled in: %s").fetch(errors.join(", ")), $.noop, OCA.getI18n().gettext("Validation error"));
		app.checkLoaded();
	}
	return valid;
}
ContactEdit.prototype.profileSection = ContactView.prototype.profileSection;
ContactEdit.prototype.formatSchedule = ContactView.prototype.formatSchedule;
ContactEdit.prototype.formatTime = ContactView.prototype.formatTime;
ContactEdit.prototype.getName = function(){
	if (!this.typeData || !this.typeData.TabFields) return '';

	var first = '', last = '';

	for (var tID in this.typeData.TabFields) {
		for (var fID in this.typeData.TabFields[tID]) {
			var field = this.typeData.TabFields[tID][fID];
			if (field.Define == 'FIRSTNAME') {
				first = field.Input.val();
			} else if (field.Define == 'SURNAME') {
				last = field.Input.val();
			}
		}
	}
	if (first || last) {
		return first + ' ' + last;
	}

	//failing that, give the type name
	return this.typeData.Name;
}

ContactNew = function(parentID, page){
	this.initContactNew(parentID, page);
}
ContactNew.prototype= new ContactEdit;
ContactNew.prototype.constructor = ContactNew;
ContactNew.prototype.initContactNew = function(parentID, page){
	this.parentID = parentID;
	this.initContactEdit(null, page);
	this.createURL = '/contactgroup/' + this.parentID + '/contacts';
}
ContactNew.prototype.render = function(){
	if (!this.data) this.data = {};
	if (!this.data['ProfileFieldData']) this.data['ProfileFieldData'] = {};
	if (!this.data['BaseFieldData']) this.data['BaseFieldData'] = {};
	for(var pID in this.typeData.Profiles){
		if (!this.data.ProfileFieldData[pID]) this.data.ProfileFieldData[pID] = {};	
	}
	
	//if this is an import from the device, loop through all of the fields to try and prefill values
	if (ContactImport.hasData()){
		var importData = ContactImport.getData();
		var field = null, f=null;
		for(var t in this.typeData.Tabs){
			for(f in this.typeData.TabFields[t]){
				field = this.typeData.TabFields[t][f];
				if (importData.Define[field.Define]) {
					this.data.BaseFieldData[f] = importData.Define[field.Define];
				}
				if (importData.Type[field.Type] && importData.Type[field.Type].length > 0){
					this.data.BaseFieldData[f] = importData.Type[field.Type].shift();
				}
			}
		}
		for(var p in this.typeData.Profiles){
			this.data.ProfileFieldData[p] = {};	
			for(f in this.typeData.ProfileFields){
				field = this.typeData.ProfileFields[f];
				if (importData.Type[field.Type] && importData.Type[field.Type].length > 0){
					this.data.ProfileFieldData[p][f] = importData.Type[field.Type].shift();
				}
			}
		}
	}
	ContactEdit.prototype.render.call(this);
}
ContactNew.prototype.hasChanged = TypeNew.prototype.hasChanged;
ContactNew.prototype.submission = function(submission){
	if (this.submitted) return;
	this.submitted = true;
	submission['TypeURL'] = Configuration.getAPIPath() + this.typeEndpoint + '/' + this.typeID;
	var desc = "Created new " + this.typeData.Name;
	new Gopher({url: this.createURL, data:submission, desc: desc, oldTimestamp: this.timestamp, name: this.getName(), type: this.type}, function(){
		util.goBack();
	}, $.proxy(this.dataError, this)).post();
};

function ContactPendingView(parentID, page) {
	this.initContactPending(parentID, page);
}
ContactPendingView.prototype                = new ContactView;
ContactPendingView.prototype.constructor    = ContactPendingView;
ContactPendingView.prototype.initContactPending = function(parentID, page) {
	this.parentID = parentID;
	this.initContactView(null, page);
	this.createURL = '/contactgroup/' + this.parentID + '/contacts';

};
ContactPendingView.prototype.afterRender    = function() {
	ContactView.prototype.afterRender.call(this);

	var $mm = this.moreMenu;
	$mm.find('li.send').hide(); //cant send to pending contact
	$mm.find('li.save.contact').hide(); //cant save pending contact

	var $deletePopup = this.page.find('#confirmDeleteContact');
	$deletePopup.find('a.delete').off().on('click', $.proxy(this.deleteCacheItem, this, this.createURL, this.timestamp));
	//link edit to the pending new route
	var editRoute = '#contactNew?pending=true&parent=' + this.parentID + '&timestamp=' + this.timestamp;
	if (this.cache.info.url.indexOf('/pending') === -1){ //if this is a child of a normal item, adjust the edit route
		editRoute = editRoute.replace('pending=true&', '');
	}
	this.footer.find('li.edit a').prop('href', editRoute);
};

//for creating a new item as the child of a pending item
function ContactPendingNew(parentID, page) {
	this.initContactPendingNew(parentID, page);
}
ContactPendingNew.prototype                   = new ContactNew;
ContactPendingNew.prototype.constructor       = ContactPendingNew;
ContactPendingNew.prototype.initContactPendingNew = function(parentID, page) {
	this.initContactNew(parentID, page);
	this.createURL = '/pending' + this.createURL;

};
//static controller for contact importing
var ContactImport = {
	load: function(parentID, page){
		this.parentID = parentID;
		this.$page = $(page);
		this.$page.find('#contactImportSearch').keypress(function(e){
			if (e.which == 13){
				ContactImport.search($(this).val());
			}
		}).on('change', function(e){
			if ($(this).val() == ''){
				ContactImport.search(false);
			}
		});
		this.$lv = this.$page.find('ul').empty();
		this.$lv.on('click', 'a', $.proxy(this.chooseContact, this));
		ContactImport.search(false);
	},
	search: function(query){
		var options = {multiple: true};
		if (query) options['filter'] = query;
		navigator.contacts.find(["*"], $.proxy(this.gotContacts, this), log.e, options);
	},
	gotContacts: function(contacts){
		this.$lv.empty();
		this.contacts = contacts;
		ViewUtil.applyTemplate(this.$lv, this.contacts, 'contactImportLV');
		$.mobile.loading('hide');
	},
	chooseContact: function(e){
		this.contact = this.contacts[$(e.target).attr('data-contact-index')];
        $("body").pagecontainer("change", '#contactNew?parent='+this.parentID, {changeHash: false});
	},
	hasData: function(){
		return this.contact != null;
	},
	getData: function(){
		var data = {
			Define: {},
			Type: {
				email:		[],
				location:	[],
				phone:		[],
				mobile:		[]
			}
		};
		
		if (this.contact.displayName){
			var name = this.contact.displayName.split(" ");
			if (!this.contact.name.givenName  && name.length > 0) this.contact.name.givenName  = name.shift();
			if (!this.contact.name.familyName && name.length > 0) this.contact.name.familyName = name.pop();
		}
		
		if (this.contact.name){
			data.Define['FIRSTNAME'] = this.contact.name.givenName+"";
			data.Define['SURNAME'] = this.contact.name.familyName+"";
		}
		
		if (this.contact.organizations && this.contact.organizations.length > 0){
			var org = this.contact.organizations.shift();
			if (org.title) data.Define['POS'] = org.title;
			if (org.name)  data.Define['ORG'] = org.name;
		}
		
		if (this.contact.emails){
			for (var e = 0; e < this.contact.emails.length; e++){
				data.Type.email.push(this.contact.emails[e].value);
			}
		}
		
		if (this.contact.address){
			for (var a = 0; a < this.contact.addresses.length; a++){
				data.Type.location.push(this.contact.addresses[a].formatted);
			}
		}
		
		if (this.contact.phoneNumbers){
			for (var p = 0; p < this.contact.phoneNumbers.length; p++){
				var num = this.contact.phoneNumbers[p];
				if (num.type && num.type == 'mobile'){
					data.Type.mobile.push(num.value);
				} else {
					data.Type.phone.push(num.value);
				}
			}
		}
		
		this.contact = null;
		return data
	}
}
var ContactExport = {
	save: function(contactView){
		//TODO
		this.contact = navigator.contacts.create({"displayName": contactView.data.FullName});
		this.contact.name = {};
		this.contact.phoneNumbers = [];
		this.contact.emails = [];
		this.contact.organizations = [];
		this.contact.urls = [];
		var f;
		for(var t in contactView.typeData.Tabs){
			for(f in contactView.typeData.TabFields[t]){
				this.processField(contactView.typeData.TabFields[t][f], contactView.data.BaseFieldData[f]);
			}
		}
		for(var p in contactView.typeData.Profiles){
			for(f in contactView.typeData.ProfileFields[p]){
				this.processField(contactView.typeData.ProfileFields[p][f], contactView.data.ProfileFieldData[p][f])
			}
		}
		this.contact.save();
	},
	processField: function(field, data){
		if (!data) return;
		if (field.Define){
			switch (field.Define){
				case "FIRSTNAME":
					this.contact.name.givenName = data;
					break;
				case "SURNAME":
					this.contact.name.familyName = data;
					break;
				case "TITLE":
					this.contact.name.honorificPrefix = data;
					break;
				case "POS":
					if (!this.contact.organizations.length) this.contact.organizations.push({});
					this.contact.organizations[0]['title'] = data;
					break;
				case "DEPT":
					if (!this.contact.organizations.length) this.contact.organizations.push({});
					this.contact.organizations[0]['department'] = data;
					break;
				case "ORG":
					if (!this.contact.organizations.length) this.contact.organizations.push({});
					this.contact.organizations[0]['name'] = data;
					break;
					
			}
		} else {
			switch (field.Type){
				case 'email':
					this.contact.emails.push({value: data});
					break;
				case 'phone':
				case 'mobile':
					this.contact.phoneNumbers.push({value: data});
					break;
				case 'url':
					this.contact.urls.push({value: data});
					break;
			}
		}
	}
}