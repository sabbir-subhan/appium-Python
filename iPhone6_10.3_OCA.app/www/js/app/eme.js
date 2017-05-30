router.add(
	{
		"#emeTreeView[?]id=0&query=(.*)": function(type, match) {
			EmeController.indexFilters.search = match[1];
			EmeController.renderListing();
		},

		"#emeTreeView[?]selector=true&id=(\\d+)": function(type, match, ui, page, e) {
			EmeController.renderListing(match[1], true);
		},

		"#emeView[?]id=(\\d+)": function(type, match, ui, page, e) {
			new EmeView(match[1], page).getData();
		},

		"#emeTreeView[?]id=(\\d+)$": function(type, match, ui, page, e) {
			if (match[1] !== 0 && EmeController.currentItem.Singleton === match[1]) {				//if the current EME is childless and already displayed, go to the single view mode
				$("body").pagecontainer("change", '#emeView?id=' + match[1], {changeHash: false});
			} else {
				EmeController.renderListing(match[1], false);
			}
		},

		"#emeEdit[?]id=(\\d+)$": function(type, match, ui, page, e) {
			if (ViewUtil.selector.previousObject) {
				ViewUtil.selector.previousObject = null;
				app.checkLoaded();
				return;
			}
			new EmeEdit(match[1], page).getData();
		},

		"#emeNew[?]parent=(\\d+)$": function(type, match, ui, page, e) {
			if (ViewUtil.selector.previousObject) {
				ViewUtil.selector.previousObject = null;
				app.checkLoaded();
				return;
			}
			new EmeNew(match[1], page).getTypes();
		},

		"#emeNew[?]parent=(\\d+)&timestamp=(\\d+)$": function(type, match, ui, page, e) {
			if (ViewUtil.selector.previousObject) {
				ViewUtil.selector.previousObject = null;
				app.checkLoaded();
				return;
			}
			new EmeNew(match[1], page).getNewCacheData(match[2]);
		},

		"#emeNew[?]type=(\\d+)$": function(type, match, ui, page) {
			if (ViewUtil.selector.previousObject) {
				ViewUtil.selector.previousObject = null;
				app.checkLoaded();
				return;
			}
			new EmeNew(0, page).getType(match[1]);
		},

		"#emeNew[?]parent=(\\d+)&type=(\\d+)&timestamp=(\\d+)$": function(type, match, ui, page, e) {
			if (ViewUtil.selector.previousObject) {
				ViewUtil.selector.previousObject = null;
				app.checkLoaded();
				return;
			}
			new EmeNew(match[1], page).getNewCacheData(match[3]);
		},

		"#emeNew[?]parent=(\\d+)&type=(\\d+)$": function(type, match, ui, page) {
			if (ViewUtil.selector.previousObject) {
				ViewUtil.selector.previousObject = null;
				app.checkLoaded();
				return;
			}
			new EmeNew(match[1], page).getType(match[2]);
		},

		//routes to support pending items

		"#emeTreeView[?]pending=true&parent=(\\d+)&timestamp=(\\d+)$": function(type, match, ui, page, e) {
			var pendingKey = 'pending-' + match[2] + '-' + match[1];
			if (EmeController.currentItem.Singleton === pendingKey) { //if the current EME is childless and already displayed, go to the single view mode
				$("body").pagecontainer("change", '#emeView?pending=true&parent=' + match[1] + '&timestamp=' + match[2], {changeHash: false});
			} else {
				EmeController.renderListing(pendingKey, false);
			}
		},

		"#emeView[?]pending=true&parent=(\\d+)&timestamp=(\\d+)$": function(type, match, ui, page, e) {
			new EmePendingView(match[1], page).getNewCacheData(match[2])
		},

		"#emeTreeView[?]pending=true&timestamp=(\\d+)$": function(type, match, ui, page, e) {
			var pendingKey = 'pending-' + match[1] + '-' + 0;
			if (EmeController.currentItem.Singleton === pendingKey) { //if the current EME is childless and already displayed, go to the single view mode
				$("body").pagecontainer("change", '#emeView?pending=true&timestamp=' + match[1], {changeHash: false});
			} else {
				EmeController.renderListing(pendingKey, false);
			}
		},

		"#emeView[?]pending=true&timestamp=(\\d+)$": function(type, match, ui, page, e) {
			new EmePendingView(0, page).getNewCacheData(match[1])
		},

		"#emeNew[?]pending=true&parent=(\\d+)$": function(type, match, ui, page, e) {
			if (ViewUtil.selector.previousObject) {
				ViewUtil.selector.previousObject = null;
				app.checkLoaded();
				return;
			}
			new EmePendingNew(match[1], page).getTypes();
		},

		"#emeNew[?]pending=true&parent=(\\d+)&timestamp=(\\d+)$": function(type, match, ui, page, e) {
			if (ViewUtil.selector.previousObject) {
				ViewUtil.selector.previousObject = null;
				app.checkLoaded();
				return;
			}
			new EmePendingNew(match[1], page).getNewCacheData(match[2]);
		},
		"#emeNew[?]pending=true&timestamp=(\\d+)$": function(type, match, ui, page) {
			if (ViewUtil.selector.previousObject) {
				ViewUtil.selector.previousObject = null;
				app.checkLoaded();
				return;
			}
			new EmeNew(0, page).getNewCacheData(match[1]);
		},
	}
);

$(document).on("pageinit", "#emeTreeView", function(e) {
	EmeController.init($(this));
});
var EmeController = $.extend({}, app, {
	init: function(page) {
		this.page    = page;
		this.content = this.page.find('.ui-content');
		this.footer  = this.page.find('.ui-footer');
		this.$mainLV = this.content.find(".main ul.emes.listview");

		this.indexFilters = {
			search: null,
			status: null
		};
		this.content.find('#emeSearch').keypress($.proxy(function(e) {
			if (e.which == 13) {
				this.indexFilters.search = $(e.currentTarget).val();
				this.renderListing(this.currentItem.ID, this.selectorMode);
			}
		}, this)).on('change', $.proxy(function(e) {
			if ($(e.target).val() == '') {
				this.indexFilters.search = null;
				this.renderListing(this.currentItem.ID, this.selectorMode);
			}
		}, this));

		this.page.find('#emeTreeMore li.eme.set.primary a').on('click', $.proxy(this.setPrimaryEME, this));
		this.page.find('#emeTreeMore li.eme.clear.primary a').on('click', $.proxy(this.clearPrimaryEME, this));

		this.$collapsible    = this.content.find('div.ui-collapsible');
		this.indexTypeList   = this.content.find('ul.emetypes');
		this.indexStatusList = this.content.find('ul.emestatus');
		this.typeHeading     = this.content.find("h2.emetype span.label");
		this.statusHeading   = this.content.find("h2.emestatus span.label");

		this.indexStatusList.on('click', 'a', $.proxy(function(e) {
			var $status              = $(e.currentTarget);
			this.indexFilters.status = $status.attr('data-status');
			this.statusHeading.text($status.text());
			this.$collapsible.collapsible('collapse');
			this.renderListing(this.currentItem.ID, this.selectorMode);
		}, this));

		if (OCA.versionAtLeast('1.6.7')) {
			this.indexTypeList.empty();
			new Gopher('/emetypes', $.proxy(this.gotEMETypes, this)).run();
		} else {
			this.indexTypeList.empty().parents('.emetype.collapsible').hide();
		}
		$("body").on("reset-#emeTreeView?selector=true&id=0", $.proxy(function() {
			this.indexFilters.status  = "";
			this.indexFilters.typeurl = "";
			this.statusHeading.text("Any Status");
			this.typeHeading.text("Any Type");
		}, this));

		app.init.call(this);
	},

	gotEMETypes: function(data) {
		this.indexTypeList.empty();

		var li = $("<li><a class='translated' data-translate='Any Type'>" + OCA.getI18n().gettext('Any Type') + "</a></li>").data('id', null);
		this.indexTypeList.append(li);

		for (var d = 0; d < data.length; d++) {
			var type = data[d];
			li       = $("<li><a>" + type.Name + "</a></li>").data('id', ViewUtil.stripAPI(type.URL));
			this.indexTypeList.append(li);
		}
		this.indexTypeList.on('click', 'li', $.proxy(function(e) {
			var $type = $(e.currentTarget);
			this.typeHeading.text($type.text());
			this.$collapsible.collapsible('collapse');
			this.indexFilters.typeurl = $type.data('id');
			this.renderListing(this.currentItem.ID, this.selectorMode);
			e.preventDefault();
		}, this));
		this.indexTypeList.listview('refresh');
	},

	setPrimaryEME: function() {
		OCA.setPrimaryEME(this.currentItemURL, this.currentItemName);
		this.checkLoaded();
		util.goBack(); //close the context menu
		this.page.find('#emeTreeMore li.primary.eme.clear').show();
	},

	clearPrimaryEME: function() {
		OCA.setPrimaryEME(null, null);
		this.checkLoaded();
		util.goBack(); //close the context menu
		this.page.find('#emeTreeMore li.primary.eme.clear').hide();
	},

	renderListing: function(id, selectorMode) {
		if (!id) {
			id = 0;
		}
		this.selectorMode   = selectorMode || false;

		var newArg  = 'parent=' + id;
		var viewArg = 'id=' + id;
		if (isNaN(id) && id.indexOf('pending-') === 0) {
			var bits = id.split("-"); // pending-itemID-parentID
			this.setPendingItem('pending/eme', bits[1], bits[2]);
			this.setCurrentItem('pending/eme', bits[1]);
			newArg  = 'pending=true&parent=' + bits[1]; //create child of this item
			viewArg = 'pending=true&parent=' + bits[2] + '&timestamp=' + bits[1]; //view this item
		} else {
			this.setPendingItem(null);
			this.setCurrentItem('eme', id);
		}

		var atRoot = id == 0;
		this.page.find('.selector-mode').visibleIf(this.selectorMode)
		this.footer.find('.emeView').visibleIf(!atRoot);
		this.content.find('div.heading-row a.level-up').visibleIf(!atRoot);
		this.content.find('.filters').showIf(!this.pendingItem.ID); //in the tree view of a pending item, don't show any filter options because we cant handle it

		var newEME       = OCA.checkEndPoint('EMES_ADDEME', '/eme/{emeid:int}/emes', OCA.ACTION_CREATE);
		var clearPrimary = OCA.getPrimaryEME();
		var $more        = this.page.find('#emeTreeMore');
		$more.find('li.eme.new').showIf(newEME);
		$more.find('li.eme.clear').showIf(clearPrimary);
		$more.find('li.eme.set').showIf(!atRoot);
		$more.find('li.new.eme a').prop('href', '#emeNew?' + newArg);
		this.page.find('#openEmeTreeMore').showIf(newEME || clearPrimary || !atRoot);
		this.footer.find('a.emeView').prop('href', '#emeView?' + viewArg);

		var query     = this.getListingQuery();
		var heading   = this.currentItem.Name
			? this.currentItem.Name
			: $.isEmptyObject(query) ? "Events" : "Events search";
		query.orderby = 'StartDate';

		var url         = this.currentItem.URL + "/emes?" + $.param(query);
		var renderProps = {
			type:         'emeTree',
			selectorMode: this.selectorMode ? {parent: true} : false
		};
		this.getListing(url, T(heading), $.proxy(this.gotEmes, this), renderProps);
	},

	gotEmes: function(data, extra) {
		if (!data.length && this.currentItem.ID && this.currentItem.ID != "0") {
			// there are no items in the eme list
			// go to eme view, do not update the history.

			var route = '#emeView?id=' + this.currentItem.ID;
			if (this.pendingItem.ID) {
				route = '#emeView?pending=true&parent=' + this.pendingItem.ParentID + '&timestamp=' + this.pendingItem.ID;
			}
			$("body").pagecontainer("change", route, {changeHash: false});
			this.currentItem.Singleton = this.currentItem.ID;
		} else {
			this.setParentItem('eme', this.currentItem.ID); //this is a parent eme
			this.checkLoaded();
			this.currentItem.Singleton = null;
		}
	},
});

function EmeView(id, page) {
	this.initEmeView(id, page);
}
EmeView.prototype             = new TypeView;
EmeView.prototype.constructor = EmeView;
EmeView.prototype.initEmeView = function(id, page) {
	this.initTypeView(id, page, "eme");
	if (id == EmeController.parentItem.ID) {
		//we are in the eme view of an eme with children. Go back an extra level on delete rather than just returning to the tree view for this eme
		this.deleteLevels--;
	}
};

EmeView.prototype.afterRender = function() {
	TypeView.prototype.afterRender.call(this);

	var $mm = this.moreMenu;
	$mm.find('li.new.subeme a').prop('href', '#emeNew?parent=' + this.ID);
	$mm.find('li.new.subeme').showIf(this.data.WritePolicyURL != -1 && OCA.checkEndPoint('EMES_ADDEME', '/eme/{emeid:int}/emes', OCA.ACTION_CREATE))

	$mm.find('li.eme.set.primary').off().on('click', $.proxy(this.setPrimaryEME, this));

	var $deletePopup = this.page.find('#confirmDeleteEME');
	ViewUtil.applyTemplate($deletePopup, {item: 'eme', 'label': 'event'}, 'confirmDelete');
	$deletePopup.find('a.delete').off().on('click', $.proxy(this.deleteItem, this));

	$mm.find('li.eme.delete').showIf(this.data.WritePolicyURL != -1).on('click', function() {
		$mm.popup('close');
		$deletePopup.popup('open');
	});
};

EmeView.prototype.setPrimaryEME = function() {
	OCA.setPrimaryEME(this.endpoint + this.ID, this.data.Name);
	util.goBack(); // causes a load of the emeTreeView and then directs back to the eme itself but just closing the popup causes the same problem
};

function EmeEdit(id, page) {
	this.initEmeEdit(id, page);
}

EmeEdit.prototype             = new TypeEdit;
EmeEdit.prototype.constructor = EmeEdit;
EmeEdit.prototype.initEmeEdit = function(id, page) {
	this.initTypeEdit(id, page, "eme");
	this.typeLabel = 'event';
};

EmeEdit.prototype.getSLMCType = function(field) {
	switch (field.Define) {
		case "OTHERAGENCIES":
			return "contactgroupTreeView";
			break;
	}
	return false;
};

function EmeNew(parentID, page) {
	this.initEmeNew(parentID, page);
}
EmeNew.prototype             = new EmeEdit;
EmeNew.prototype.constructor = EmeNew;
EmeNew.prototype.initEmeNew  = function(parentID, page) {
	this.parentID = parentID;
	this.initEmeEdit(null, page);
	this.createURL = '/eme/' + this.parentID + '/emes';

};
EmeNew.prototype.hasChanged  = TypeNew.prototype.hasChanged;
EmeNew.prototype.submission  = function(submission) {
	if (this.submitted) return;
	this.submitted        = true;
	submission['TypeURL'] = Configuration.getAPIPath() + this.typeEndpoint + '/' + this.typeID;
	var desc              = "Created new " + this.typeData.Name;
	window.linkParams     = {createdObject: 'eme', message: desc};
	new Gopher({
		url:          this.createURL,
		data:         submission,
		desc:         desc,
		name:         this.getName(),
		type:         this.type,
		oldTimestamp: this.timestamp,
		resubmitter:  'EMEResubmitter'
	}, $.proxy(this.attachAfterSubmit, this, submission.Attachments), $.proxy(this.dataError, this)).post();
};

/**
 * Array filter callback which removes types the user has no permission to create,
 * or types invalid at this level - some events can only be created as children, some only at the root
 * @param type type summary payload
 * @returns {boolean}
 */
EmeNew.prototype.typeFilter = function(type) {
	if (type.OtherFields) {
		if (type.OtherFields.AllowNewPolicyURL == -1) {	//A type that the user is not allowed to create new records of
			return false;
		}
		if (type.OtherFields.IsSubEvent && this.parentID == 0) { //sub event at the root
			return false;
		} else if (type.OtherFields.IsSubEvent === false && this.parentID != 0) { //full event as a child
			return false;
		} //else when IsSubEvent is null, it can be used as either
	}
	return true;
}

function EmePendingView(parentID, page) {
	this.initEmePending(parentID, page);
}
EmePendingView.prototype                = new EmeView;
EmePendingView.prototype.constructor    = EmePendingView;
EmePendingView.prototype.initEmePending = function(parentID, page) {
	this.parentID = parentID;
	this.initEmeView(null, page);
	this.createURL = '/eme/' + this.parentID + '/emes';

};
EmePendingView.prototype.afterRender    = function() {
	EmeView.prototype.afterRender.call(this);

	var $mm = this.moreMenu;
	$mm.find('li.new.subeme a').prop('href', '#emeNew?pending=true&parent=' + this.timestamp);
	$mm.find('li.eme.set.primary').hide(); //cant set pending EME as primary

	var $deletePopup = this.page.find('#confirmDeleteEME');
	$deletePopup.find('a.delete').off().on('click', $.proxy(this.deleteCacheItem, this, this.createURL, this.timestamp));
	//link edit to the pending new route
	var editRoute = '#emeNew?pending=true&parent=' + this.parentID + '&timestamp=' + this.timestamp;
	if (this.cache.info.url.indexOf('/pending') === -1){ //if this is a child of a normal item, adjust the edit route
		editRoute = editRoute.replace('pending=true&', '');
	}
	this.footer.find('li.edit a').prop('href', editRoute);
};

//for creating a new item as the child of a pending item
function EmePendingNew(parentID, page) {
	this.initEmePendingNew(parentID, page);
}
EmePendingNew.prototype                   = new EmeNew;
EmePendingNew.prototype.constructor       = EmePendingNew;
EmePendingNew.prototype.initEmePendingNew = function(parentID, page) {
	this.initEmeNew(parentID, page);
	this.createURL = '/pending' + this.createURL;

};