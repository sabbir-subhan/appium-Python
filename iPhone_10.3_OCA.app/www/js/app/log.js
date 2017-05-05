router.add({
	"#logIndex[?]id=0&query=(.*)": function(type, match){
		LogController.indexFilters.search = match[1];
		LogController.renderListing();
	},
	"#logIndex[?]selector=true&id=0": function(type, match){
		LogController.indexFilters = {typeurl: null, search: null};
		LogController.renderListing(true);
	},
	"#logIndex$": function(type, match, ui, page, e){
		LogController.indexFilters = {typeurl: null, search: null};
		LogController.renderListing();
	},
	"#logView[?]id=(\\d+)": function(type, match, ui, page, e){
		new LogView(match[1], page).getData();
	},
	"#logEdit[?]id=(\\d+)": function(type, match, ui, page, e){
		if (ViewUtil.selector.previousObject){
			ViewUtil.selector.previousObject = null;
			app.checkLoaded();
			return;
		}
		new LogEdit(match[1], page).getData();
	},
	"#logNew[?]timestamp=(\\d+)": function(type, match, ui, page, e){
		if (ViewUtil.selector.previousObject){
			ViewUtil.selector.previousObject = null;
			app.checkLoaded();
			return;
		}
		new LogNew(page).getNewCacheData(match[1]);
	},
	"#logNew$": function(type, match, ui, page, e){
		if (ViewUtil.selector.previousObject){
			ViewUtil.selector.previousObject = null;
			app.checkLoaded();
			return;
		}
		new LogNew(page).getTypes();
	},
    "#logNew[?]type=(\\d+)": function(type, match, ui, page, e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
        new LogNew(page).getType(match[1]);
    },
   //routes to support pending items
   "#logView[?]pending=true&timestamp=(\\d+)$": function(type, match, ui, page, e) {
	   new LogPendingView(page).getNewCacheData(match[1])
   },
});

$(document).on("pageinit", "#logIndex", function(e){
	LogController.init($(this));
});
var LogController = $.extend({}, app, {
	init: function(page){
		this.indexFilters = {
			typeurl:null,
			search:null
		};

		this.page = page;
		this.content = this.page.find('.ui-content');
		this.footer = this.page.find('.ui-footer');
		app.init.call(this);
		this.$mainLV = this.content.find(".main ul.logs.listview");
		this.typeHeading = this.content.find("h2 span.label");
		this.$collapsible = this.content.find('div.ui-collapsible');
		this.content.find('#logSearch').keypress(function(e){
			if (e.which == 13){
				LogController.indexFilters.search = $(this).val();
				LogController.renderListing();
			}
		}).on('change', function(e){
			if ($(this).val() == ''){
				LogController.indexFilters.search = null;
				LogController.renderListing();
			}
		});
		this.indexTypeList = this.content.find('ul.logtypes');
		new Gopher('/logtypes',$.proxy(this.gotLogTypes,this)).run();

		$("body").on("reset-#logIndex?selector=true&id=0", function(){
			LogController.indexFilters.typeurl = "";
			LogController.typeHeading.text(T("All Logs"));
		});
	},
	gotLogTypes:   function(data){
		this.indexTypeList.empty();

		var li = $("<li><a class='translated' data-translate='All Logs'>"+OCA.getI18n().gettext('All Logs')+"</a></li>").data('id',null);
		this.indexTypeList.append(li);

		for (var d = 0; d < data.length; d++){
			var logtype = data[d];
			li = $("<li><a>"+logtype.Name+"</a></li>").data('id',ViewUtil.stripAPI(logtype.URL));
			this.indexTypeList.append(li);
		}
		this.indexTypeList.on('click', 'li', function(){
			LogController.typeHeading.text($(this).text());
			LogController.$collapsible.collapsible('collapse');
			if (LogController.indexFilters.typeurl != $(this).data('id')){
				LogController.indexFilters.typeurl = $(this).data('id');
				LogController.renderListing();
			}
		});
		this.indexTypeList.listview('refresh');
		this.indexTypeList.children().first().click();
	},
	renderListing: function(selectorMode){
		this.selectorMode = selectorMode || false;

		this.footer.find('li a.logNew').showIf(OCA.checkEndPoint('LOGS_ADDLOG','/logs',OCA.ACTION_CREATE));
		this.page.find('.selector-mode').visibleIf(this.selectorMode);

		var query     = this.getListingQuery();
		var heading   = $.isEmptyObject(query) ? "Logs" : "Log search";
		query.orderby = 'Date';
		var url       = '/logs?' + $.param(query);

		var renderProps = {
			type:         'log',
			selectorMode: this.selectorMode,
			icon:         'logs'
		};
		this.getListing(url, T(heading), null, renderProps);
	}
});

function LogView(id, page){
	this.initLogView(id, page);
}
LogView.prototype = new TypeView;
LogView.prototype.constructor = LogView;
LogView.prototype.initLogView = function(id, page){
	this.initTypeView(id, page, "log");
};
LogView.prototype.afterRender = function(){
	TypeView.prototype.afterRender.call(this);

    var $mm = this.moreMenu;
    var $deletePopup = this.page.find('#confirmDeleteLog');

	ViewUtil.applyTemplate($deletePopup,{item:'log'},'confirmDelete');
	$deletePopup.find('a.delete').off().on('click', $.proxy(this.deleteItem, this));
	$mm.find('li.log.new').showIf(OCA.checkEndPoint('LOGS_ADDLOG', '/logs', OCA.ACTION_CREATE));

    $mm.find('li.log.delete').on('click', function(){
        $mm.popup('close');
        $deletePopup.popup('open');
    });
}

function LogEdit(id, page){
	this.initLogEdit(id, page);
}
LogEdit.prototype = new TypeEdit;
LogEdit.prototype.constructor = LogEdit;
LogEdit.prototype.initLogEdit = function(id, page){
	this.initTypeEdit(id, page, "log");
    this.supportsLocation = false;
};
LogEdit.prototype.getSLMCType = function(field){
	switch (field.Define){
		case "EMES":
			return "emeTreeView";
			break;
		case "ASSETS":
			return "assetTreeView";
			break;
	}
};
/**
 * Override TypeEdit.getName so that the log entry can be truncated and
 * @returns {*}
 */
LogEdit.prototype.getName = function(){
	if (!this.typeData || !this.typeData.Fields) return '';

	for (var fID in this.typeData.Fields){
		var field = this.typeData.Fields[fID];
		if (field.Define == 'ENTRY' && field.Input && field.Input.val()) {
			var entry = field.Input.val();
			var tmp = document.createElement("DIV");
			tmp.innerHTML = entry;
			entry = tmp.textContent || tmp.innerText || '';
			return entry.substr(0, 50);
		}
	}
	//failing that, give the type name
	return this.typeData.Name;
}

function LogNew(page){
	this.initLogNew(page);
}
LogNew.prototype = new LogEdit;
LogNew.prototype.constructor = LogNew;
LogNew.prototype.initLogNew = function(page){
	this.parentID = null;
	this.initLogEdit(null, page, "log");
	this.createURL = '/logs';
}
LogNew.prototype.hasChanged = TypeNew.prototype.hasChanged;
LogNew.prototype.submission = function(submission){
	if (this.submitted) return;
	this.submitted = true;
	submission['TypeURL'] = Configuration.getAPIPath() + this.typeEndpoint + '/' + this.typeID;
	var desc = "Created new " + this.typeData.Name;
	new Gopher({
			url: this.createURL,
			data: submission,
			desc: desc,
			oldTimestamp: this.timestamp,
			resubmitter: 'LogResubmitter',
			name: this.getName(),
			type: this.type
		},
		$.proxy(this.attachAfterSubmit, this, submission.Attachments),
		$.proxy(this.dataError, this)
	).post();
}

LogNew.prototype.beforeRender = function(){
	TypeView.prototype.beforeRender.call(this);

	if (! this.data){
		this.data = {};
	}
	if (!this.data.FieldData){
		this.data.FieldData = {};
	}
	//Set the primary eme as the event
	var emeFieldID = null;
	for (var i in this.typeData.Fields){
		if (this.typeData.Fields[i].Define == 'EMES'){
			emeFieldID = i;
			break;
		}
	}

	if (emeFieldID && !this.data.FieldData[emeFieldID]){
		var pe = OCA.getPrimaryEME();
		if (pe !== null){
			this.data.FieldData[emeFieldID] = [pe];
		}
	}
}

function LogPendingView(page) {
	this.initLogPending(page);
}
LogPendingView.prototype                = new LogView;
LogPendingView.prototype.constructor    = LogPendingView;
LogPendingView.prototype.initLogPending = function(page) {
	this.initLogView(null, page);
	this.createURL = '/logs';

};
LogPendingView.prototype.afterRender    = function() {
	LogView.prototype.afterRender.call(this);

	var $deletePopup = this.page.find('#confirmDeleteLog');
	$deletePopup.find('a.delete').off().on('click', $.proxy(this.deleteCacheItem, this, this.createURL, this.timestamp));
	this.footer.find('li.edit a').prop('href', '#logNew?timestamp=' + this.timestamp);
};