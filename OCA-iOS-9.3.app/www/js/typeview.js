/**
 * Generic 'type' view class - type being anything in OCA which supports the creation of different types and has field data
 * This class is abstract and is extended by each type individually 
 * @see ContactView
 * @see TaskView
 * @see LogView
 * etc
 */ 
function TypeView(id, page){
	this.initTypeView(id, page);
}
TypeView.prototype = new View;
TypeView.prototype.constructor = TypeView;
/**
 * Initialises the basic properties of the type view
 */
TypeView.prototype.initTypeView = function(id, page, type){
	this.initView(page);		//call parent init
	
	this.ID = id;				//properties of a Type View
	this.typeID = null;
	this.type = type;
	this.typeLabel = type; 		//optionally overridden by child classes
	this.endpoint = "/"+type+"/";
	this.typeEndpoint = "/"+type+"type";
	this.data = null;
	this.typeData = null;
	this.externalHandlers = true;
    this.supportsLocation = OCA.checkEndPoint('MAPPING', '/symbology/features', OCA.ACTION_READ); //if mapping is not available to the user, do not add the mapping fields
	this.policies = ["Read", "Write"];
	this.deleteLevels = -2;
	this.moreMenu = this.page.find('#' + type + 'ViewMoreMenu');
    this.lockURL = Configuration.getAPIPath() + this.endpoint + this.ID  + '/lock';
    this.mode = 'view';

    this.expressions = {};

	this.forceRefresh = false;
}
/**
 * Fetches the data for this object. The URL is generated from the endpoint set up in the init, and the ID of this object
 */
TypeView.prototype.getData = function(){
	new Gopher({url:this.endpoint + this.ID}, $.proxy(this.gotData, this), log.e).run({dontCheckCache: this.forceRefresh});
	if (!app.pullToRefresh){
		app.pullToRefresh = true;
		ViewUtil.pullToRefresh(this.content, function() {
			this.forceRefresh = true;
			this.content.empty();
			this.getData();
		}.bind(this));
	}
}
/**
 * Success callback when data has been retrieved. 
 * Data is stored and the type data is fetched
 */
TypeView.prototype.gotData = function(data, payload){
	this.data = $.extend(true, {}, data[0]);	//so we can muck about with the data without altering the cache.
    if (payload.extraPayloads.length){
        this.handleExtraPayloads(payload.extraPayloads);
    }

	this.getType();
}
/**
 * When re-editing a new item which has yet to be submitted because the device is offline,
 * the previous submission has to be fetched from the cache and then loaded as if it had come
 * directly from the server
 * @param {number} timestamp of previous submission
 */
TypeView.prototype.getNewCacheData = function(timestamp){
	this.timestamp = parseInt(timestamp, 10); //force int so that it can be used in the Date constructor
	this.cache = new Gopher(this.createURL).getPOSTCache(timestamp);
	if (!this.cache) {	//try loading from an offline parent
		this.cache = new Gopher('/pending' + this.createURL).getPOSTCache(timestamp);
	}
	if (!this.cache && GopherQueue.createdCache['/pending/' + timestamp]) {
		//this used to be a cached item but it was just saved. This route shouldn't be reached but the code is here as a fallback
		this.ID = ViewUtil.getID(GopherQueue.createdCache['/pending/' + timestamp]);
		return this.getData();
	}
	this.cache.info.currentlyEditing = true;
	this.data = JSON.parse(this.cache.ajax.data);
	var bits = this.data.TypeURL.split("/");
	this.typeID = bits.pop();
	this.getType();
};
/**
 * Default implementation. Look for lock objects
 *
 */
TypeView.prototype.handleExtraPayloads = function(payloads){
    this.extraPayloads = payloads;
    for (var e = 0; e < payloads.length; e++){
        if (payloads[e].sourceURL == this.lockURL){
            this.lock = payloads[e].payloads[0];
        }
    }
}
/**
 * Fetches the data for the type of this object, after reading the data to find what that type is
 */
TypeView.prototype.getType = function(id){
    if (id){
        this.typeID = id;
    } else if (!this.typeID){
		var bits = this.data.TypeURL.split("/");
		this.typeID = bits[bits.length-1];
	}
	new Gopher(this.typeEndpoint + "/" + this.typeID, $.proxy(this.gotType, this), log.e).run({dontCheckCache: this.forceRefresh});
	this.forceRefresh = false;
}
/**
 * Success callback when the type data has been retrieved. 
 * Calls the render function after saving the type data
 */
TypeView.prototype.gotType = function(data){
	this.typeData = $.extend(true, {}, data[0]);  //so we can muck about with the data without altering the cache.
	if (this.typeData.HideMap){
		this.supportsLocation = false;
	}
    if (this.mode == 'edit' && this.typeData.AllowLocks){
        if (this.lock && this.lock.IsLocked && this.lock.MyLock){
            //editing something you already own
            this.render();
        } else {
            this.getLock();
        }
    } else {
	    this.render();
    }
}
/**
 * Get the list of available types
 */
TypeView.prototype.getTypes = function(){
	new Gopher(this.typeEndpoint + "s", $.proxy(this.gotTypes, this), log.e).run();
}
/**
 * Success callback for the list of types.
 * If there is only one type, auto select it
 * If not, present the types in a listview for selection
 */
TypeView.prototype.gotTypes = function(data){
	if (data.length == 1){	//only one type. select it and move on.
		this.typeID = data[0].URL.split("/").pop();
		this.getType();
		return;
	}
	this.listview = $("<ul />");

	data = data.filter(this.typeFilter, this);

	for (var i=0; i < data.length; i++){
		var type = data[i];
		var bits = type.URL.split("/");
		var row = $("<li />").append($("<a href='#'>").text(type.Name).data("type-id", bits.pop())).click($.proxy(this.chooseType, this));
		this.listview.append(row)
	}
	this.content.append(this.listview);
	this.listview.listview();
	this.footer.css('visibility', 'hidden');
	$.mobile.loading('hide');
};

/**
 * Array filter callback which removes types the user has no permission to create
 * @param type type summary payload
 * @returns {boolean}
 */
TypeView.prototype.typeFilter = function(type){
	if (type.OtherFields && type.OtherFields.AllowNewPolicyURL == -1){	//A type that the user is not allowed to create new records of
		return false;
	}
	return true;
}
/**
 * Set the type ID and fetch the type data
 */
TypeView.prototype.chooseType = function(e){
	$.mobile.loading('show');
	var a = $(e.target);
	this.typeID = a.data("type-id");
	this.content.empty();
	this.data = {};
	this.getType();
	this.footer.css('visibility', 'visible');
}

/**
 * Render the fields for this object into a listview, then refresh the listview to make jQuery Mobile prettify it
 */
TypeView.prototype.render = function(){
    this.listview = $("<ul />");
    this.beforeRender();
	this.renderFields();
	this.renderRelations();
	this.renderOptions();
    this.renderMapping();
	this.renderPolicies();
	this.content.append(this.listview);
	this.afterRender();
	this.listview.listview();
	$.mobile.loading('hide');
	this.finalise();
}
/**
 * Called after renderFields
 * Displays any related items
 */
TypeView.prototype.renderRelations = function(){
	//offline mode. render the attachments using the editor but remove all edit-mode controls
	if (this.data.Attachments && !$.isEmptyObject(this.data.Attachments)){
		TypeEdit.prototype.renderRelations.call(this);
		this.listview.find('.edit-mode').remove();
		return;
	}

	if (!this.data.RelatedObjects || Object.keys(this.data.RelatedObjects).length == 0) return;
	
	this.listview.append($("<li class='relatedSection' data-role='list-divider'/>").text(OCA.getI18n().gettext("Related")));
	for (var direction in this.data.RelatedObjects){
		var relations = this.data.RelatedObjects[direction];
		for (var relation in relations){
			for (var url in relations[relation]){
				var label = relations[relation][url];
				if (url.indexOf('/api/v') !== 0){
					url = Configuration.getAPIPath() + url;
				}
				var match = url.match(/\/api\/v\d\/(\w+)\/(\d+)/);
				var type = match[1];
				//EMEs are displayed in the Events field. Unless this itself is an eme being displayed
				if (type === 'eme' && this.type !== 'eme') {
					continue;
				}
				var id = match[2];
				var content = label;
				// provide a link to all valid and viewable types
				if ($.inArray(type, ['contact', 'contactgroup', 'document', 'report', 'task', 'log']) !== -1){	
					content = "<a href='#" + type + "View?id=" + id + "'>" + label + "</a>";
				}
				this.listview.append("<li>" + content + "</li>");
			}
		}
	}
	//if no relations were rendered, hide section
	var lastRow = this.listview.children().last()
	if (lastRow.is('.relatedSection')){
		lastRow.remove();
	}
}

/**
 * Called after renderFields
 * Implemented by subclasses to display inputs which do not come from dynamic field data in a particular type
 */
TypeView.prototype.renderOptions = function(){}

/**
 * Called after renderOptions
 * Renders geometry data for this object, if applicable for the type and data
 */
TypeView.prototype.renderMapping = function(){
    if (!this.supportsLocation){
    	return;
    }
    if ((this.data.Geometry && this.data.Geometry.WKT) || this.data.HasMapData){
        this.listview.append($("<li data-role='list-divider'/>").text(OCA.getI18n().gettext("Mapping")));
        linkParams.geometry = {
            type: this.type,
            ID: this.ID
        }
        this.listview.append("<li><a href='#mapPage?geometry=true'>" + OCA.getI18n().gettext("View on map") + "</a></li>");
    }
};

/**
 * Display all policies which belong to this object
 *
 * @translation OCA.getI18n().gettext('Read Access Level')
 * @translation OCA.getI18n().gettext('Write Access Level')
 * @translation OCA.getI18n().gettext('Send Access Level')
 */
TypeView.prototype.renderPolicies = function(){
    if (!this.policies.length) return;

	this.listview.append($("<li data-role='list-divider'/>").text(OCA.getI18n().gettext("Access Levels")));
	for (var p=0; p < this.policies.length; p++){
		var policyName = this.policies[p];
		this.typeData[policyName+"PolicyURL"] = {
            Options: OCA.policyOptions, 
            Label: OCA.getI18n().gettext(policyName + " Access Level"), 
            ID: policyName
        };
		var data = this.data ? this.data[policyName+"PolicyURL"] : null;
		if (!data){
			data = OCA.policyDefaults ? OCA.policyDefaults[policyName] : null;
		}
		this.optRender(this.typeData[policyName+"PolicyURL"], data);
	}
}
/**
 * Called before the render function.
 * Used to set data values before the fields are rendered.
 */
TypeView.prototype.beforeRender = function() {
	this.typeData.Fields = this.applyFieldAccessLevels(this.typeData.Fields);
}

TypeView.prototype.applyFieldAccessLevels = function(fields){
	for (var id in fields){
		var field = fields[id];
		if (field.ReadPolicyURL === -1){
			delete fields[id]; //dont have read access to this field
		}
		if (field.WritePolicyURL === -1){
			if (!this.ID && field.CreatePolicyAllowAll){
				//CreatePolicyAllowAll overrides the write policy in create mode
			} else {
				field.Readonly = true;	//set readonly because we dont have write access
			}
		}
		if (field.CreatePolicyURL === -1 && !this.ID){
			delete fields[id]; //dont have create access to this field, so remove it completely in create mode
		}
		if (field.SubFields) {
			field.SubFields = this.applyFieldAccessLevels(field.SubFields);
			if ($.isEmptyObject(field.SubFields)){
				delete fields[id];
			}
		}
	}
	return fields;
}

/**
 * After the fields have been rendered, finish the page rendering by updating URLs for action buttons or hiding them due to access levels
 */
TypeView.prototype.afterRender = function(){
	var canEdit = this.data.WritePolicyURL != -1;
    if (this.lock && this.lock.IsLocked && !this.lock.MyLock){ //if object has a lock, but not held by the current user
        canEdit = false;
    }
	this.moreMenu.find('li.delete').showIf(canEdit);
    this.footer.find('li.edit a').showIf(canEdit);
	this.footer.find('li.edit a').prop('href', '#' + this.type + 'Edit?id='+this.ID);
}

TypeView.prototype.showInfobar = function(){
    //handle the infobar for any locks
    var msg = '';
    var btnIcon = null;
    var btnCallback = null;
    if (this.lock) {
        if (this.lock.IsLocked){
            if (this.lock.MyLock){
                this.lock.LockedByName = 'you';
            } else if (this.lock.CanSteal){
                btnIcon = 'lock';
                btnCallback = $.proxy(this.stealLock, this);
            }
            msg = OCA.getI18n().gettext('Lock held by') + ' ' + this.lock.LockedByName;
        }
    }
    if (msg){
        util.infobar(msg, null, null, btnIcon, btnCallback);
    }
}

TypeView.prototype.stealLock = function(){
    console.log('stealing the lock yeah!');
    new Gopher(this.lockURL, $.proxy(this.stoleLock, this), $.proxy(this.cantLock, this)).put(false);
}

TypeView.prototype.getLock = function(){
    console.log('getting the lock');
    new Gopher({url: this.lockURL, backgroundMode: true}, $.proxy(this.gotLock, this), $.proxy(this.cantLock, this)).post(false);
}

TypeView.prototype.cancelLock = function(){
    new Gopher(this.endpoint + this.ID).uncache();
    new Gopher(this.lockURL, function(){
        console.log('lock cancelled!');
    }, function(){
        console.log('lock not cancelled');
    }).sendDelete();
    util.goBack();
}

TypeView.prototype.stoleLock = function(){
    console.log('got lock, change lock properties');
    this.lock = {
        MyLock: true,
        IsLocked: true
    };
    new Gopher(this.endpoint + this.ID).uncache();
    this.showInfobar();
    this.afterRender();
}

TypeView.prototype.gotLock = function(){
    this.lock = {
        MyLock: true,
        IsLocked: true
    };
    new Gopher(this.endpoint + this.ID).uncache();
    this.render();
}

TypeView.prototype.cantLock = function(e, response){
    response.errors.unshift(OCA.getI18n().gettext("Unable to obtain lock"));
    util.handleResponseExtras(response);

    if (this.ID) new Gopher(this.endpoint + this.ID).uncache();
    util.goBack(); //cant lock, return and the lock should appear because we have uncached the object
}


/** render a datetime field */
TypeView.prototype.datetimeRender = function(field, data){
	if (data && !isNaN(Date.parse(data))){ 		//data is set and parses as a valid date
		var date = new Date(data);
		data = ViewUtil.displayDateTime(date); 	//format as per the OCA server settings.
	}
	return this.fieldRender(field, data);
}
/** render a datetimeopt field */
TypeView.prototype.datetimeoptRender = function(field, data){
	if (data && data.indexOf("T")){
        return this.datetimeRender(field, data);
	} else {
        return this.dateRender(field, data);
	}
}
/** render a date field */
TypeView.prototype.dateRender = function(field, data){
	if (data && !isNaN(Date.parse(data))){
        var date = new Date(data);
        data = ViewUtil.displayDate(date);
	}
    return this.fieldRender(field, data);
}

TypeView.prototype.sectionheaderRender = function(field, data){
	var row = $('<li class="sectionHeader'+(field.Collapsible ? ' ui-btn-icon-right ui-icon-arrow-u' : '')+'" data-role="list-divider" />').text(field.Label);
	this.listview.append(row);
	return row;
}
TypeView.prototype.toggleSection = function(fields,header,event){
	if (header.sectionVisible){
		header.sectionVisible = false;
		header.addClass('ui-icon-arrow-d');
		header.removeClass('ui-icon-arrow-u');
		for (var i in fields){
			if (fields[i].$row){
				fields[i].$row.addClass('sectionHidden');
			}
		}
	} else {
		header.sectionVisible = true;
		header.removeClass('ui-icon-arrow-d');
		header.addClass('ui-icon-arrow-u');
		for (var i in fields){
			if (fields[i].$row){
				fields[i].$row.removeClass('sectionHidden');
			}
		}
	}
}
/** render an url field */
TypeView.prototype.urlRender = function(field, data){
	var row = this.fieldRender(field, data);
	if (data && this.externalHandlers){
		row.wrapInner("<a href='"+data+"' />").data('icon', 'home');
	}
    return row;
}
/** render a opt field */
TypeView.prototype.optRender = function(field, data){
	var value = '';
	if (data === false) data = 0;
	if (data === true)  data = 1;
	if (data != null){
		if (field.Options && field.Options.length){

			value = [];

			//Loop through in the options rank
			for (var i = 0; i < field.Options.length; i++){
				if ($.isArray(data)){
					for (var d=0; d < data.length; d++){
						if (data[d] == field.Options[i][0]){
							value.push(field.Options[i][1]);
							break;
						}
					}

				}else{
					if (field.Options[i][0] == data){
						value.push(field.Options[i][1]);
						break;
					}
				}
			}

			value = value.join(", ");

		}

	}
	return this.fieldRender(field, value);
}
/** render a fileupload field */
TypeView.prototype.fileuploadRender = function(field, data){
    var value;
    if (data && data.dataURI) {
		if (field.ShowCanvas == '1') {
			value = '<img style="width: 100%;" src="' + data.dataURI + '">';
		} else if (data.dataURI.substr(0, 10) == "data:image"){ //probably showing a pending item
			var row = $('<li class="fileupload field"><h6>' + field.Label + '</h6><img src="' + data.dataURI + '" class="listview thumbnail" />' + data.name + '</li>');
			this.listview.append(row);
			return row;
		}
    } else if (data && data.URL){
		value = data.name || data.label;
		var row = this.fieldRender(field, value);
		row.append(ViewUtil.ocaicon('file inline-right'));
		row.on('click', function(){
			DocumentController.downloadFile(data.URL, value, data.type, null, true);
		});
		return row;
    }
	return this.fieldRender(field, value);
}
/** render a number field */
TypeView.prototype.numberRender = function(field, data){
	//TODO correct formatting
	return this.fieldRender(field, data);
}
TypeView.prototype.subformRender = function(field, data){
    if (!data) return;

    var row = TypeView.prototype.fieldRender.call(this, field, "<div class='subform'><hr /></div>");
    field.SubFieldInputs = [];
    var subContainer = row.find('div.subform');
    for (var d=0; d < data.length; d++){
        subContainer.append(this.createSubformRow(field, data[d]));
    }
    field.Input = new SubformInput(field);
    field.InitialValue = data;
    return row;
};
TypeView.prototype.createSubformRow = function(field, data){
    data = data || {};
    var $container = $("<div class='subform-row'/>");
    var $subLV = $("<ul class='subform-row'>").data('inset', true);
    $container.append($subLV);
	//operate on a copy of the subfields to leave the 'master' unaffected
	var subfields = {};//$.extend(true, {}, field.SubFields);
	if (!this.subRows) this.subRows = 0;
	var sfidmap = {};
	for (var fid in field.SubFields) {
		subfields[fid + '-' + this.subRows] = $.extend(true, {}, field.SubFields[fid]);
		var newVF = {};
		for (var vfid in field.SubFields[fid].VisibilityFields) {
			newVF[vfid + '-' + this.subRows] = field.SubFields[fid].VisibilityFields[vfid];
		}
		subfields[fid + '-' + this.subRows].VisibilityFields = newVF;
		sfidmap[fid + '-' + this.subRows] = fid;
	}
	var rowData = {};
	for (var did in data) {
		rowData[did + '-' + this.subRows] = data[did];
	}
	this.subRows++;
    this.renderFields(subfields, rowData, $subLV);

    //get the inputs
    var inputs = {};
    for (var sfid in subfields){
		subfields[sfid].IsSubField = true;		//some inputs need to know whether they are in a subform
		subfields[sfid].ParentSubFormField = field;
		if (subfields[sfid].Input){
			subfields[sfid].Input.Field = subfields[sfid];
			inputs[sfidmap[sfid]] = subfields[sfid].Input;
	    }
    }
    field.SubFieldInputs.push(inputs);
    $container.append("<hr />");
    return $container;
}
/** 
 * render a phone field 
 * Display the data and wrap it in a tel: link if externalHandlers are enabled
 */
TypeView.prototype.phoneRender = function(field, data){
	var row = this.fieldRender(field, data);
	if (data && this.externalHandlers) {
        row.wrapInner("<a href='tel:"+data.split(' ').join('') +"' />").attr('data-icon', 'phone');
    }
    return row;
}
TypeView.prototype.faxRender = TypeView.prototype.mobileRender = TypeView.prototype.phoneRender;
TypeView.prototype.emailRender = function(field, data){
	var row = this.fieldRender(field, data);
    return row;
}
/** 
 * render a location field
 * Wrap it in a link to display the address on a map if there is data and external handlers are available
 */
TypeView.prototype.locationRender = function(field, data){
	var value = "";
	if (data){
		value = ViewUtil.formatLocationData(data);
	}
	var row = this.fieldRender(field, value); //even when
	var w = window;
	var label = this.data.Name || this.data.FullName;
	if (value && this.externalHandlers){
		row.wrapInner("<a href='#mapPage?address=true'/>").click(function(e){
			w.linkParams['mapFromAddress'] = {
				content: "<b>"+label+"</b><br />"+value,
				data: data
			};
		}).attr('data-icon', 'world_map');
	}
    return row;
}
/**
 * Render a chart field. 
 * Table fields are not currently supported. 
 * The chart data is saved to the file system. The actual rendered output is a link to view the chart in a new window
 */
TypeView.prototype.chartRender = function(field, data){
	if (!data){
		return this.fieldRender(field, OCA.getI18n().gettext("No data to display"));
	}
	if (data.length < 100) {
		return this.fieldRender(field, OCA.getI18n().gettext("Unable to display table data"));
	} else {
		var $row;
		try {
			//data is OCA Chart JSON
			data = JSON.parse(data);
			if (!data.highchart){
				return this.fieldRender(field, OCA.getI18n().gettext("No data to display"));
			} else {
				var card = new AnalyticsChartCard({
					Type: "ANALYTICS-CHART",
					Title: field.Label,
					Content: data
				});

				card.renderField(this.listview);
			}
		} catch(e) {
			//old system still providing SVG
			if (device.platform != "Mobile Interface") {
				$row = this.fieldRender(field, "<a href='#'>" + OCA.getI18n().gettext('Click to view chart') + "</a>");
				fileStore.saveFile('chart-' + this.ID + '-' + field.ID + '.svg', data, $.proxy(this.chartSVG, this, $row));
			} else {
				$row  = $("<li />").html("<h6>" + field.Label + "</h6>").data('icon', false);
				var $svg = $(data);
				$row.append($svg);
				$svg.wrap($("<div />").width(this.content.width()).height(this.content.width() / 2));
			}
			this.listview.append($row);
		}
		return $row;
	}
}
/**
 * Success callback for saving the chart SVG file
 * Add a click listener to open the file in a new window which can be zoomed and moved.
 */
TypeView.prototype.chartSVG = function(row, path){
	row.on('click', function(){
		window.open(path, '_blank', 'location=no');
	});
};
/**
 * render a field. This handles sgltxt fields, but is also the base field render function used by many other methods
 */
TypeView.prototype.fieldRender = function(field, value){
	if (!value && value !== 0){
		return null;
	}
//	value = value || "-";
	var row = $("<li />")
		.html("<h6>"+ field.Label + "</h6><p>" + value + "</p>")
		.data('icon', false);

	if (this.prepend){
		this.listview.prepend(row);
	}else{
		this.listview.append(row);
	}
	
	return row;
};
/** 
 * Render sgltxt field.
 */
TypeView.prototype.sgltxtRender = function(field, value){
	return this.fieldRender(field, value);
};
/**
 * Render multitxt field. Converts line break characters into XHTML BR tags
 */
TypeView.prototype.multitxtRender = function(field, value){
	if (value) value = value.replace(/\n/g, "<br />");
	var $row = this.fieldRender(field, value);
	if ($row){
		$row.addClass('multitxt'); //make sure multi line text doesnt get cut-off
		$row.children('p').find('a').on('click', ViewUtil.linkClickHandler);
	}
	return $row;
};
/**
 * Render rich text fields. 
 * If the data includes HTML markup, wrap it in a DIV to protect it from jQuery mobile 'improvements'
 * Else, wrap it in a P tag for display
 */
TypeView.prototype.richtextRender = function(field, value){
    if (!value) return null;

    var iframeContents = false;
    if (value.indexOf('<') == -1){
        value = "<p class='richtextcontent'>" + value + "</p>";
    } else {
        iframeContents = value;
        value = "<div class='iframe'><iframe /></div>";
    }

	var html = "<h6>"+ field.Label + "</h6>" + value;
	var row = $("<li />")
		.html(html)
		.data('icon', false)
		.attr('data-enhance', false);
	this.listview.append(row);
    if (iframeContents !== false){
        setTimeout(function(){ //populate the iframe, but wrap it in a timeout to make sure the iframe document is accessible
            ViewUtil.populateIFrame(row.find('iframe'), iframeContents);
        }, 0);
    }
	return row;
}

/**
 * render SLMC field as a list of values, optionally with a link to the item
 * @param {object} field
 * @param {array} data
 * @param {boolean} [link] whether the SLMC should be rendered with links to the selected values. Defaults to true
 */
TypeView.prototype.slmcRender = function(field, data, link){
	if (link !== false){
		link = true;
	}
	var values = [];
	for (var i = 0; data && i < data.length; i++){
		var item = data[i];
		if (link && item.url){
            var bits = item.url.split("/");
            var id = bits.pop();
            var type = bits.pop();
			var url = "#" + type + "View?id=" + id;
			if ($('#' + type + 'View').length) {	//only render the link if there's a route to receive it
				values.push("<a href='" + url + "'>" + item.label + "</a>");
			} else {
				values.push(item.label);
			}
		} else {
			values.push(item.label);
		}
	}
	return this.fieldRender(field, values.join(", "));
}
/** render asset chooser field as an slmc with links to the items */
TypeView.prototype.assetchooserRender = function(field, data){
	return this.slmcRender(field, data, true);
};
/** render teamrole chooser field as an slmc without links to the items*/
TypeView.prototype.teamrolechooserRender = function(field, data){
	return this.slmcRender(field, data, false);
};
/** render resourcestructurenode chooser field as an slmc without links to the items*/
TypeView.prototype.resourcestructurenodechooserRender = function(field, data){
	return this.slmcRender(field, data, false);
};
/** render contact chooser field as an slmc with links to the items*/
TypeView.prototype.contactchooserRender = function(field, data){
	return this.slmcRender(field, data, true);
};
/** render document chooser field as an slmc with links to the items*/
TypeView.prototype.documentchooserRender = function(field, data){
    return this.slmcRender(field, data, true);
};
/** render eme chooser field as an slmc with links to the items*/
TypeView.prototype.emechooserRender = function(field, data){
    return this.slmcRender(field, data, true);
};
/** render log chooser field as an slmc with links to the items */
TypeView.prototype.logentrychooserRender = function(field, data){
	return this.slmcRender(field, data, true);
}
/** render contact grop chooser field as an slmc with links to the items */
TypeView.prototype.contactgroupchooserRender = function(field, data){
	return this.slmcRender(field, data, true);
}
TypeView.prototype.derivedfieldRender = function(field,data){
    return this.fieldRender(field,data);
}
TypeView.prototype.calcfieldRender = function(field,data){
    return this.derivedfieldRender(field, data);
}
/** datediff fields are just derived fields as far as the app cares */
TypeView.prototype.datediffRender = function(field, data){
    return this.derivedfieldRender(field, data);
};

TypeView.prototype.checkVisibility = function(field, dataObj) {
	var show = true;
	for (var id in field.VisibilityFields) {
		var val = dataObj[id];
		if (!$.isArray(val)) val = [val];
		var showField = false;
		for (var v = 0; v < val.length; v++){
			if (val[v] && val[v].indexOf('/api/') === 0){ //convert from an API endpoint (/api/v1/contactgroup/22) to the ID (22)
				var bits = val[v].split('/');
				val[v] = bits.pop();
			}
			if ($.inArray(val[v], field.VisibilityFields[id]) !== -1) {
				showField = true;
			}
		}
		show = show && showField;
	}
	return show;
}

/** 
 * render a set of fields.
 * Sort the fields by order of their position, then render them in sections
 * @param {object} [fieldObj] set of fields, in associative array keyed by field ID. Defaults to this.typeData.Fields
 * @param {object} [dataObj] set of field data, in associative array keyed by field ID. Defaults to this.data.FieldData, then to this.data
 * @param {jQuery} [lv] listview object to populate with fields. Defaults to this.listview
 */
TypeView.prototype.renderFields = function(fieldObj, dataObj, lv){
	fieldObj = fieldObj || this.typeData.Fields;					//allow override of the fields
	dataObj = dataObj;												//allow override of the data
	if (!dataObj && this.data && this.data.FieldData){
		dataObj = this.data.FieldData
	}
	if (!dataObj && this.data){
		dataObj = this.data;
	}
	this.fullLV = this.listview;
	this.listview = lv || this.listview;						//if the LV is being overridden 
	
	var fields = this.sortFields(fieldObj);						//sort fields in order of their position (2Y+X)
	
	var sections = {"__core": []};								//then put all fields into a 'section'
	var sectionOrder = ["__core"];								//the first section is a core section. __core so it doesnt clash with any subsequent names
	var currLeftSection = "__core";
	var currRightSection = "__core";
	
	var field, isLeft, data;
	for (var f=0; f < fields.length; f++){						
		field = fields[f];
		isLeft = field.X == 0;

		if (!(this instanceof TypeEdit || this.checkVisibility(field, dataObj))) continue;

		if (field.Type == "sectionheader"){						//this field is a sectionheader, so a new section is started
			if ( isLeft){
				currLeftSection = field.Label;
			}
			if (!isLeft || field.Width == 2){
				currRightSection = field.Label;
			}
			sections[field.Label] = [field];
			sectionOrder.push(field.Label);
		} else {
			if (isLeft){
				sections[currLeftSection].push(field);
			} else {
				sections[currRightSection].push(field);
			}
		}
	}
	var lastRow;
	var tobeClicked = [];
	for (var s=0; s < sectionOrder.length; s++){				//for each section
		var section = sectionOrder[s];
		var sectionFields = sections[section];
		lastRow = this.listview.children().last();
		if (lastRow.is('.sectionHeader')){
			lastRow.remove();		//if the last row is a section header, no fields were added in that last section. So remove it.
		}
		
		for (var sf=0; sf < sectionFields.length; sf++){		//render all fields in that section
			field = sectionFields[sf];
			data = (dataObj && (dataObj[field.ID] || dataObj[field.ID] === 0))
				? dataObj[field.ID]
				: null;


			//if the default value has an expression to evaluate on load, add it to this.expressions for resolution
			if (! this.ID && ! data && field.DefaultValue && field.ApplyDefaultOnSave != '1'){
				data = field.DefaultValue;

				//Strip out any replacements
				if (data.replace) { //data might not be a string
					data = data.replace(/\$\{((?:\\\\|\\\}|[^\}])+)\}/g,'');
				}
                if (data !== field.DefaultValue){
                    this.expressions[field.ID] = field.DefaultValue;
                }
			}
            if (field.Type === 'number' && field.DerivedField){
                field.Type = 'derivedfield';
            }
			var renderFunc = field.Type + "Render";

			if (this[renderFunc]){
				field.InitialValue = data;
				var row = this[renderFunc].call(this, field, data);
                field.$row = row;
				this.enhanceRow(row, field);
			} else {
				//this.fieldRender(field, data); //if the field type is not recognised, don't render it
			}
		}
		if (section != '__core'){
			sectionFields[0].$row.sectionVisible = true;
			if (sectionFields[0].Collapsible){
				var increment = 1;
				var collapseFields = sectionFields.slice(1);
				while (sectionOrder[s+increment] && !sections[sectionOrder[s+increment]][0].Collapsible){
					collapseFields = collapseFields.concat(sections[sectionOrder[s+increment]]);
					increment++;
				}
				sectionFields[0].$row.click($.proxy(this.toggleSection, this, collapseFields,sectionFields[0].$row));
			}
			if (sectionFields[0].Collapsible == "default_collapsed"){
				tobeClicked.push(sectionFields[0].$row);
			}
		}
	}
	for (var c = 0;c<tobeClicked.length;c++){
		tobeClicked[c].click();
	}
	lastRow = this.listview.children().last();
	if (lastRow.is('.sectionHeader')){
		lastRow.remove();
	}
	this.listview = this.fullLV;
}
/**
 * Order fields by their position. 
 * The calculation is 2Y + X - i.e. for each row (Y), first the left (X=0)then the right (X=1)
 * This function also sets the ID property of the field to the field ID
 * @param {object} fieldObj associative array of fields, keyed by field ID
 */
TypeView.prototype.sortFields = function(fieldObj){
	var fields = [];
	for (var id in fieldObj){
		fieldObj[id]["ID"] = id;
		fields.push(fieldObj[id]);
	}
	fields.sort(function(a, b){
		var aIdx = a.Y * 2 + a.X;
		var bIdx = b.Y * 2 + b.X;
		return aIdx - bIdx;
	});
	return fields;
}
/**
 * Send the DELETE request for this item
 */
TypeView.prototype.deleteItem = function(){
	var go = this.deleteLevels;
	if (device.platform === "iOS" && parseInt(device.version) >= 9){
		go++; //go back one less level for iOS9. stupid iOS9
	}
	new Gopher(this.endpoint + this.ID, function(){
		util.goBack(go); //back would just reload the view. since this is launched from a popup.
	}).sendDelete();
};

TypeView.prototype.deleteCacheItem = function(url, timestamp){
	var go = this.deleteLevels;
	if (device.platform === "iOS" && parseInt(device.version) >= 9){
		go++; //go back one less level for iOS9. stupid iOS9
	}
	if (GopherQueue.has(Configuration.getAPIUrl() + url, timestamp)) {							//pending item might be unparented or child of a server item
		GopherQueue.remove('POST', Configuration.getAPIUrl() + url, timestamp);
	} else if (GopherQueue.has(Configuration.getAPIUrl() + '/pending' + url, timestamp)) {		//or a child of another pending item
		GopherQueue.remove('POST', Configuration.getAPIUrl() + '/pending' + url, timestamp);
	}
	util.goBack(go);
}

TypeView.prototype.dataError = function(){
	this.submitted = false;
}

/** Only applies to edit mode */
TypeView.prototype.enhanceRow = function(row, field){}

/** This function is called at the very end of a TypeView's render method. For very patient hooks */
TypeView.prototype.finalise = function(){
	if (device.platform != 'iOS') return; //at the moment, we only need to worry about iOS
	
	//force redraw by hiding and re-showing a field after a short break. This fixes an absurd bug on iOS
	var $lv = this.listview;
	setTimeout(function(){
		$lv.find('li:last-child').hide();
		setTimeout(function(){
			$lv.find('li:last-child').show();
		}, 100);
	}, 100);
}