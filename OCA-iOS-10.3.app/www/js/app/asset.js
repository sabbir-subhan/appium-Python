router.add({
    "#assetTreeView[?]id=(\\d+)$": function (type, match, ui, page, e) {
        if (match[1] !== 0 && AssetController.currentItem.Singleton === match[1]){
            //if the current Asset is childless and already displayed, go to the single view mode
            $("body").pagecontainer("change", '#assetView?id=' + match[1], {changeHash: false});
        } else {
            AssetController.renderListing(match[1], false);
        }
    },
	"#assetTreeView[?]id=0&query=(.*)": function(type, match){
		AssetController.indexFilters.search = match[1];
		AssetController.renderListing();
	},
	"#assetTreeView[?]selector=true&id=(\\d+)": function(type, match, ui, page, e){
		AssetController.renderListing(match[1], true);
	},
	"#assetView[?]id=(\\d+)": function(type, match, ui, page, e){
		new AssetView(match[1], page).getData();
	},
	"#assetEdit[?]id=(\\d+)": function(type, match, ui, page, e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
		new AssetEdit(match[1], page).getData();
	},
	"#assetNew[?]parent=(\\d+)&timestamp=(\\d+)": function(type, match, ui, page, e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
		new AssetNew(match[1], page).getNewCacheData(match[2]);
	},
	"#assetNew[?]parent=(\\d+)$": function(type, match, ui, page, e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
		new AssetNew(match[1], page).getTypes();
	},
    "#assetNew[?]type=(\\d+)$": function(type, match, ui, page, e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
        new AssetNew(0, page).getType(match[1]);
    },
    "#assetNew[?]parent=(\\d+)&type=(\\d+)$": function(type, match, ui, page, e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
        new AssetNew(match[1], page).getType(match[2]);
    },
    "#assetNew[?]parent=(\\d+)&type=(\\d+)&timestamp=(\\d+)": function(type, match, ui, page, e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
        new AssetNew(match[1], page).getNewCacheData(match[2]);
    },

   //routes to support pending items
   "#assetTreeView[?]pending=true&parent=(\\d+)&timestamp=(\\d+)$": function(type, match, ui, page, e) {
	   var pendingKey = 'pending-' + match[2] + '-' + match[1];
	   if (AssetController.currentItem.Singleton === pendingKey) { //if the current Asset is childless and already displayed, go to the single view mode
		   $("body").pagecontainer("change", '#assetView?pending=true&parent=' + match[1] + '&timestamp=' + match[2], {changeHash: false});
	   } else {
		   AssetController.renderListing(pendingKey, false);
	   }
   },

   "#assetTreeView[?]pending=true&timestamp=(\\d+)$": function(type, match, ui, page, e) {
	   var pendingKey = 'pending-' + match[1] + '-' + 0;
	   if (AssetController.currentItem.Singleton === pendingKey) { //if the current Asset is childless and already displayed, go to the single view mode
		   $("body").pagecontainer("change", '#assetView?pending=true&timestamp=' + match[1], {changeHash: false});
	   } else {
		   AssetController.renderListing(pendingKey, false);
	   }
   },

   "#assetView[?]pending=true&parent=(\\d+)&timestamp=(\\d+)$": function(type, match, ui, page, e) {
	   new AssetPendingView(match[1], page).getNewCacheData(match[2])
   },
   "#assetView[?]pending=true&timestamp=(\\d+)$": function(type, match, ui, page, e) {
	   new AssetPendingView(0, page).getNewCacheData(match[1])
   },

   "#assetNew[?]pending=true&parent=(\\d+)$": function(type, match, ui, page, e) {
	   if (ViewUtil.selector.previousObject) {
		   ViewUtil.selector.previousObject = null;
		   app.checkLoaded();
		   return;
	   }
	   new AssetPendingNew(match[1], page).getTypes();
   },

   "#assetNew[?]pending=true&parent=(\\d+)&timestamp=(\\d+)$": function(type, match, ui, page, e) {
	   if (ViewUtil.selector.previousObject) {
		   ViewUtil.selector.previousObject = null;
		   app.checkLoaded();
		   return;
	   }
	   new AssetPendingNew(match[1], page).getNewCacheData(match[2]);
   },

   "#assetNew[?]pending=true&timestamp=(\\d+)$": function(type, match, ui, page, e) {
	   if (ViewUtil.selector.previousObject) {
		   ViewUtil.selector.previousObject = null;
		   app.checkLoaded();
		   return;
	   }
	   new AssetPendingNew(0, page).getNewCacheData(match[1]);
   },
});

$(document).on("pageinit", "#assetTreeView", function(e){ 
	AssetController.init($(this));
});
var AssetController = $.extend({}, app, {
    parentAssetID: null,
    currentAssetID: null,
    currentAssetURL: null,
    currentAssetName: null,

	init:          function(page){
		this.page = page;
		this.content = this.page.find('.ui-content');
		this.footer = this.page.find('.ui-footer');
		app.init.call(this);
		this.$mainLV = this.content.find(".main ul.assets.listview");

		this.indexFilters.search = null;
		this.content.find('#assetSearch').keypress(function(e){
			if (e.which == 13){
				this.indexFilters.search = $(e.target).val();
				this.renderListing(this.currentItem.ID, this.selectorMode);
			}
		}.bind(this)).on('change', function(e){
			if ($(e.target).val() == ''){
				this.indexFilters.search = null;
				this.renderListing(this.currentItem.ID, this.selectorMode);
			}
		}.bind(this));
	},
	renderListing: function(id, selectorMode){
		if (!id) {
			id = 0;
		}
		this.selectorMode   = selectorMode || false;

		var newArg  = 'parent=' + id;
		var viewArg = 'id=' + id;
		if (isNaN(id) && id.indexOf('pending-') === 0) {
			var bits = id.split("-"); // pending-itemID-parentID
			this.setPendingItem('pending/asset', bits[1], bits[2]);
			this.setCurrentItem('pending/asset', bits[1]);
			newArg  = 'pending=true&parent=' + bits[1]; //create child of this item
			viewArg = 'pending=true&parent=' + bits[2] + '&timestamp=' + bits[1]; //view this item
		} else {
			this.setPendingItem(null);
			this.setCurrentItem('asset', id);
		}

        var atRoot = id == 0;
		this.page.find('.selector-mode').visibleIf(this.selectorMode);
        this.footer.find('.assetView').visibleIf(!atRoot);
		this.content.find('div.heading-row a.level-up').visibleIf(!atRoot);
		this.content.find('.filters').showIf(!this.pendingItem.ID); //in the tree view of a pending item, don't show any filter options because we cant handle it
        this.$mainLV.empty();

        var newAsset = OCA.checkEndPoint('ASSETS_ADDASSET', '/asset/{assetid:int}/assets', OCA.ACTION_CREATE);
        var $more = this.page.find('#assetTreeMore');
        $more.find('li.asset.new').showIf(newAsset);
        this.page.find('#openAssetTreeMore').showIf(newAsset);
		this.footer.find('a.assetView').prop('href', '#assetView?' + viewArg);
		$more.find('li.new.asset a').prop('href', '#assetNew?' + newArg);

		var query     = this.getListingQuery();
		var heading   = this.currentItem.Name
			? this.currentItem.Name
			: $.isEmptyObject(query) ? "Assets" : "Assets search";
		query.orderby = 'Date';

		var url         = this.currentItem.URL + "/assets?" + $.param(query);
		var renderProps = {
			type:         'assetTree',
			selectorMode: this.selectorMode ? {parent: true} : false,
			icon:		  'apartment'
		};
		this.getListing(url, T(heading), $.proxy(this.gotAssets, this), renderProps);
	},
	gotAssets: function(data, extra){
        if (!data.length && this.currentItem.ID && this.currentItem.ID != "0") {
            // there are no items in the asset list
            // go to asset view, do not update the history.
			var route = '#assetView?id=' + this.currentItem.ID;
			if (this.pendingItem.ID) {
				route = '#assetView?pending=true&parent=' + this.pendingItem.ParentID + '&timestamp=' + this.pendingItem.ID;
			}
            $("body").pagecontainer("change", route, {changeHash: false});
            this.currentItem.Singleton = this.currentItem.ID;
		} else {
			this.setParentItem('asset', this.currentItem.ID); //this is a parent asset
            this.checkLoaded();
            this.currentItem.Singleton = null;
        }
	}
});

function AssetView(id, page){
	this.initAssetView(id, page);
}
AssetView.prototype = new TypeView;
AssetView.prototype.constructor = AssetView;
AssetView.prototype.initAssetView = function(id, page){
	this.initTypeView(id, page, "asset");
    if (id == AssetController.parentItem.ID){
        //we are in the asset view of an asset with children. Go back an extra level on delete rather than just returning to the tree view for this asset
        this.deleteLevels--;
    }
};
AssetView.prototype.renderOptions = function(){
    this.listview.append($("<li class='optionHeading' data-role='list-divider'/>").text(OCA.getI18n().gettext("Options")));
    this.typeData["CostPerUnit"] = {
        Type: 'number',
        Label: OCA.getI18n().gettext("Cost per unit")
    };
    this.typeData["CostPerUnitPerHour"] = {
        Type: 'number',
        Label: OCA.getI18n().gettext("Cost per unit per hour")
    };
    this.fieldRender(this.typeData["CostPerUnit"],          this.data ? this.data["CostPerUnit"] : null);
    this.fieldRender(this.typeData["CostPerUnitPerHour"],	this.data ? this.data["CostPerUnitPerHour"] : null);

    //remove header if no fields were added (i.e. view mode, no data)
    var lastRow = this.listview.children().last();
    if (lastRow.is('.optionHeading')) lastRow.remove();
}
AssetView.prototype.afterRender = function(){
    TypeView.prototype.afterRender.call(this);

    var canEdit    = (this.data.WritePolicyURL != -1)

    var $deletePopup = this.page.find('#confirmDeleteAsset');
    ViewUtil.applyTemplate($deletePopup,{item:OCA.getI18n().gettext('asset')},'confirmDelete');
    $deletePopup.find('a.delete').off().on('click', $.proxy(this.deleteItem, this));
    var $mm = this.moreMenu;
    $mm.find('li.asset.delete').showIf(canEdit).on('click', function(){
        $mm.popup('close');
        $deletePopup.popup('open');
    });
    $mm.find('li.asset.new')
        .showIf(OCA.checkEndPoint('ASSETS_ADDASSET', '/asset/{assetid:int}/assets', OCA.ACTION_CREATE))
        .find('a').prop('href', '#assetNew?parent=' + this.ID);
}

function AssetEdit(id, page){
	this.initAssetEdit(id, page);
}
AssetEdit.prototype = new TypeEdit;
AssetEdit.prototype.constructor = AssetEdit;
AssetEdit.prototype.initAssetEdit = function(id, page){
	this.initTypeEdit(id, page, "asset");
};
AssetEdit.prototype.renderOptions = AssetView.prototype.renderOptions;

function AssetNew(parentID, page){
	this.initAssetNew(parentID, page);
}
AssetNew.prototype = new AssetEdit;
AssetNew.prototype.constructor = AssetNew;
AssetNew.prototype.initAssetNew = function(parentID, page){
	this.parentID = parentID;
	this.initAssetEdit(null, page);
	this.createURL = '/asset/' + this.parentID + '/assets';
	this.parentURL = '/asset/' + this.parentID;
}
AssetNew.prototype.hasChanged = TypeNew.prototype.hasChanged;
AssetNew.prototype.submission = function(submission){
	if (this.submitted) return;
	this.submitted = true;
	submission['TypeURL'] = Configuration.getAPIPath() + this.typeEndpoint + '/' + this.typeID;
	var desc = "Created new " + this.typeData.Name;
    window.linkParams = {createdObject: 'asset', message: desc};
	new Gopher(
		{url: this.createURL, data: submission, desc: desc, oldTimestamp: this.timestamp, name: this.getName(), type: this.type, resubmitter:  'AssetResubmitter'},
		$.proxy(this.attachAfterSubmit, this, submission.Attachments),
		$.proxy(this.dataError, this)
	).post();
}

function AssetPendingView(parentID, page) {
	this.initAssetPending(parentID, page);
}
AssetPendingView.prototype                = new AssetView;
AssetPendingView.prototype.constructor    = AssetPendingView;
AssetPendingView.prototype.initAssetPending = function(parentID, page) {
	this.parentID = parentID;
	this.initAssetView(null, page);
	this.createURL = '/asset/' + this.parentID + '/assets';
	this.parentURL = '/asset/' + this.parentID;

};
AssetPendingView.prototype.afterRender    = function() {
	AssetView.prototype.afterRender.call(this);

	var $mm = this.moreMenu;
	$mm.find('li.new.asset a').prop('href', '#assetNew?pending=true&parent=' + this.timestamp);

	var $deletePopup = this.page.find('#confirmDeleteAsset');
	$deletePopup.find('a.delete').off().on('click', $.proxy(this.deleteCacheItem, this, this.createURL, this.timestamp));
	var editRoute = '#assetNew?pending=true&parent=' + this.parentID + '&timestamp=' + this.timestamp;
	if (this.cache.info.url.indexOf('/pending') === -1){ //if this is a child of a normal item, adjust the edit route
		editRoute = editRoute.replace('pending=true&', '');
	}
	this.footer.find('li.edit a').prop('href', editRoute);
};

//for creating a new item as the child of a pending item
function AssetPendingNew(parentID, page) {
	this.initAssetPendingNew(parentID, page);
}
AssetPendingNew.prototype                   = new AssetNew;
AssetPendingNew.prototype.constructor       = AssetPendingNew;
AssetPendingNew.prototype.initAssetPendingNew = function(parentID, page) {
	this.initAssetNew(parentID, page);
	this.createURL = '/pending' + this.createURL;

};
