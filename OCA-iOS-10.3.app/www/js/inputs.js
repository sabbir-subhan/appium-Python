router.add({
	"#optionList$": function(type, match, ui, page, e){
		var enhancedOptionList = ViewUtil.selector.previousObject;

		if (!enhancedOptionList || enhancedOptionList.constructor.name != 'EnhancedOptionList'){	//this route renders the options for an enhanced optlist in selector mode. if it isnt set, abort.
			util.goBack();
			console.error("Error: Unenhanced option list");
			return;
		}

		enhancedOptionList.renderListview($(page));
	}
});

/** abstract class for input classes to extend. Allow use of these objects as jQuery selectors - parent, is, prop, val, etc - as if they were actual input fields. */
function jQueryInterface(field, value){
	this.field = field;
	if (this.field && !this.field.InitialValue) this.field.InitialValue = value;
	this.value = value || null;
	this.$row = false;
	this.changeCallbacks = [];
}
/**
 * Implement the jQuery val function for this input.
 * Note this does NOT support the data argument being a function callback. see JQuery docs for .val()
 * @see jQuery.val()
 */
jQueryInterface.prototype.val = function(data){
	if (arguments.length > 0){
		this.setValue(data);
		return this;
	}
	return this.value;
}

/**
 * Implement jQuery.parent by returning the row parent
 */
jQueryInterface.prototype.parent = function(){
	return !this.$row ? false : this.$row.parent();
}

/**
 * Implement jQuery.detach by detaching the row
 */
jQueryInterface.prototype.detach = function(){
	return !this.$row ? false : this.$row.detach();
}

/**
 * Implement jQuery.prop by calling the row
 */
jQueryInterface.prototype.prop = function(){
	return !this.$row ? false : this.$row.prop.apply(this, arguments);
}

/**
 * Implement jQuery.change by setting the change callback or calling it
 * @param {function} [callback] if specified, this will save the callback for future use. If omitted but a changeCallback has been set, it will be called
 */
jQueryInterface.prototype.change = function(callback){
	if (arguments.length > 0){
		this.changeCallbacks.push(callback);
	} else if(this.changeCallbacks.length){
		for (var c = 0; c < this.changeCallbacks.length; c++) this.changeCallbacks[c]();
	}
}

/**
 * Implement jQuery.find by operating on the row
 * @param selector css selector to find
 * @returns jQuery object
 */
jQueryInterface.prototype.find = function(selector){
	return !this.$row ? false : this.$row.find(selector);
};

/**
 * Implement jQuery.is by operating on the row
 * @param selector css selector to find
 * @returns jQuery object
 */
jQueryInterface.prototype.is = function(selector){
	return !this.$row ? false : this.$row.is(selector);
};

jQueryInterface.prototype.kill = function(){
	if (this.$row) {
		this.$row.off();
	}
}
/**
 * This class acts as the input for any SLMC fields.
 * In order to act as the input, it must handle the same jQuery methods that normal input fields provide, such as val and change
 * Note that only some of the use cases of these functions are implemented
 */
function SLMC(field, row, slmcRoute, typeEditObject){
	jQueryInterface.call(this, field);
	this.value = field.InitialValue;
	this.$row = row;
    this.singleMode = field.Maximum == "1"; //make the 'M' in SLMC optionally a lie.
    this.extraBack = 0;
	this.slmcRoute = slmcRoute;
	this.resolveFilterURL = field.ResolveFilterURL;
	this.typeEditObject = typeEditObject;
}
SLMC.prototype = new jQueryInterface;
SLMC.prototype.constructor = SLMC;

SLMC.prototype.loadSelector = function(typeEditObject){
	if (this.resolveFilterURL){
		var context = typeEditObject.getContext();
		delete context.Data[this.field.ID]; //remove this SLMC's values from the context so changes dont require the filter to be re-resolved

		var currentContext = JSON.stringify(context)
		if (!this.previousContext || currentContext != this.previousContext){
			//context has changed. fetch new data.
			this.previousContext = currentContext;
			new Gopher({
				url: this.resolveFilterURL,
				data: context,
				backgroundMode: false
			}, $.proxy(this.gotFilter, this), $.proxy(this.filterError, this, typeEditObject)).post(false);
		} else {
			//go straight to the chooser
			this.gotFilter();
		}
	} else {
		this.loadUnfilteredSelector(typeEditObject);
	}
}

SLMC.prototype.gotFilter = function(options){
	if (options) {
		//convert array of {Name: name, URL: url} options to [url, name] in the format expected for option lists
		this.field.Options = options.map(function (o) {
			return [o.URL, o.Name]
		});
	}

	var enhancedOptionList = new EnhancedOptionList(this.field);

	ViewUtil.selector.start({
		callbackOK: $.proxy(this.selectorCallback, this),
		data: this.field.Maximum > 1 ? this.selectorData(enhancedOptionList) : [],
		previousObject: enhancedOptionList,
		goBack: true,
		makeBackup: false,
		single: !(this.field.Maximum > 1),
		extraBack: false,
		field: this.field
	});
	$("body").pagecontainer( "change", '#optionList', {});
}
SLMC.prototype.addClickHandler = function(){
	if (!this.clickHandlerActive){
		this.$row.on('click',function(){
			this.loadSelector(this.typeEditObject);
		}.bind(this));
		this.clickHandlerActive = true;
	}
}
SLMC.prototype.removeClickHandler = function(){
	this.$row.off('click');
	this.clickHandlerActive = false;
}

SLMC.prototype.filterError = function(typeEditObject){
	this.loadUnfilteredSelector(typeEditObject)
}
SLMC.prototype.setReadOnly = function(readonly){
	this.$row.toggleClass('slmcreadonly', !!readonly);
	if (readonly){
		this.removeClickHandler();
	} else {
		this.addClickHandler();
	}
}
SLMC.prototype.loadUnfilteredSelector = function(typeEditObject){
	ViewUtil.selector.start({
		callbackOK: $.proxy(this.selectorCallback, this),
		data: this.singleMode ? [] : this.selectorData(),
		previousObject: typeEditObject,
        goBack: true,
        single: this.singleMode,
        extraBack: this.extraBack,
		field: this.field
	});
	$("body").trigger("reset-" + this.slmcRoute); //set up an event for index pages to reset their filters
    $("body").pagecontainer( "change", this.slmcRoute, {});
}
/** set the value of this SLMC and update the field content to show the data labels */
SLMC.prototype.setValue = function(data){
	this.value = data;

	var labels = [];
	for (var i = 0; data && i < data.length; i++){
		var item = data[i];
		var bits = item.url.split("/");
		var id = bits.pop();
		labels.push(item.label);
	}
	var label = labels.length ? labels.join(", ") : "-";
	this.$row.find('p').text(label);
}

/**
 * @param data Hash, keyed by URL, Object is itself a hash of {label:<string>}
 */
SLMC.prototype.selectorCallback = function(data){
	this.value = [];
	var labels = [];
	for (var key in data){
        if (data[key].checked ==  false) {
            continue;
        }
		var bits = key.split("-");
		var type = bits.shift();
		var id = bits.pop();
		this.value.push({
			url: Configuration.getAPIPath() + "/" + type + "/" + id,
			label: data[key].label
		});
		labels.push(data[key].label);
	}

	var label = labels.length ? labels.join(", ") : "";
	this.$row.find('span.valueLabel').text(label);
	this.change();
}
/**
 * Convert the SLMC data into the format expected by the selector mode controller
 * @param EnhancedOptionList eol if set, validate that all current values are in the current set of options
 */
SLMC.prototype.selectorData = function(eol){
	var allowedValues = [];
	if (eol) {
		allowedValues = eol.optionList.map(function (option) {
			return ViewUtil.getID(option.URL);
		});
	}

	var data = {};
	for (var i = 0; this.value && i < this.value.length; i++){
		var item = this.value[i];
		var bits = item.url.split("/");
		var id = bits.pop();
		var type = bits.pop();

		if (!eol || $.inArray(id, allowedValues) !== -1) { //if the eol is set, check that each ID is an available option
			data[type + "-" + id] = {
				id: id,
				label: item.label,
				checked: true
			};
		}
	}
	return data;
};

SLMC.prototype.render = function(data){
	if (data && !$.isArray(data)) { //if data was set from default value it might be a string
		data = [data];
	}

	this.value = this.currentValue = data;
	var currentLabel  = [];
	this.InitialValue = data;

	for (var i = 0; data && i < data.length; i++){
		var item = data[i];
		currentLabel.push(item.label);
	}

	var text = currentLabel.join(', ') || "";
	this.$row = $("<li name='" + this.field.Label.toLowerCase() + "' class='ui-field-contain'/>")
	.append($("<label />").prop("for", this.field.Label.toLowerCase()).text(this.field.Label))

	var choose = $("<div class='ui-select'><div class='ui-btn ui-shadow ui-btn-corner-all ui-btn-icon-right ui-btn-down-c ui-icon-arrow-r'>" +
				   "<span class='valueLabel'>" + text + "</span></div></div>");
	this.$row.append(choose);
	this.setReadOnly(this.field.IsReadOnly == 1);
	this.$row.data('input', this);
	return this.$row;
}

/**
 * Render a set of options as a group of checkboxes
 */
function EnhancedOptionList(field){
	jQueryInterface.call(this, field);
	this.optionList  = [];
	this.fullList    = [];
	this.optionIndex = {};
	this.valueIndex  = {};
	this.nestedMapIndex	 = {};

	for (var o = 0; field.Options && o < field.Options.length; o++){
		var url = String(field.Options[o][0]);
		if (url.indexOf('/') == -1) url = '/option/' + url;
		var id = ViewUtil.getID(url);

		var opt = {
			URL:  url,
			Name: field.Options[o][1]
		};
		this.optionList.push(opt);
		this.valueIndex[id]  = field.Options[o][0];
		this.optionIndex[id] = field.Options[o][1];
		this.nestedMapIndex[opt.Name.toLowerCase()] = opt;
	}
	this.fullList = this.optionList;
	this.constructor.name = "EnhancedOptionList"; //IEMobile doesnt set this value and the #optionList route checks it
}
EnhancedOptionList.prototype = new jQueryInterface;
EnhancedOptionList.prototype.constructor = EnhancedOptionList;

EnhancedOptionList.COUNT_THRESHOLD  = 10;
EnhancedOptionList.LENGTH_THRESHOLD = 30;

/** 
 * render the checkbox group.
 * The set of options will only be shown if the user clicks on the field
 * If shown, event listeners are added to change styles and record data when options are (de)/selected
 */
EnhancedOptionList.prototype.render = function(data){
	if (data && !$.isArray(data)) { //if data was set from default value it might be a string
		data = [data];
	}

	this.currentValue = data;
	var currentLabel  = [];
	
	this.InitialValue = data;

	//display initial values as label
	for (var d=0; data && d < data.length && this.field.Options && this.field.Options.length; d++){
		var id = String(data[d]).indexOf('/') != -1 //lookup labels by ID. convert URLs to IDs for lookup - e.g. for policies
				? ViewUtil.getID(data[d])
				: data[d];
		currentLabel.push(this.optionIndex[id]);
	}
	var text = currentLabel.join(', ') || "(none)";
	var row = $("<li name='" + this.field.Label.toLowerCase() + "' class='ui-field-contain'/>")
		.append($("<label />").prop("for", this.field.Label.toLowerCase()).text(this.field.Label))

	var choose = $("<div class='ui-select'><div class='ui-btn ui-shadow ui-btn-corner-all ui-btn-icon-right ui-btn-down-c ui-icon-arrow-r'>" +
		"<span class='valueLabel'>" + text + "</span></div></div>");
	row.append(choose);
	this.$row = row;
	this.setReadOnly(this.field.IsReadOnly == 1);
	row.data('input', this);
	return row;
};
EnhancedOptionList.prototype.setReadOnly = function(readonly){
	this.$row.find('div.ui-select').toggleClass('ui-state-disabled',readonly);
	if (readonly){
		this.removeClickHandler();
	} else {
		this.addClickHandler();
	}
};

EnhancedOptionList.prototype.addClickHandler = function(){
	if (!this.clickHandlerActive){
		this.$row.click($.proxy(this.loadSelector, this));
		this.clickHandlerActive = true;
	}
}
EnhancedOptionList.prototype.removeClickHandler = function(){
	this.$row.off('click');
	this.clickHandlerActive = false;
}

/** 
 * for no good reason, nested list mapping works on the basis of the parent field's option labels (as opposed to say... a numerically unique identifier
 * convert the currently selected ID values to the option labels they represent
 * @returns {Array} of object labels that act as keys for nested list mapping
 */
EnhancedOptionList.prototype.getNestedListParentKeys = function(){
	var values = this.val();
	values = values || [];
	if (!$.isArray(values)) values = [values];
	
	var keys = [];
	for (var v = 0; v < values.length; v++){
		if (this.optionIndex[values[v]]) keys.push(this.optionIndex[values[v]]);
	}
	return keys;
}

/**
 * If this is a nested list, restrict the options to those specified by the provided keys and the nested list mapping
 * @param keys array of strings
 */
EnhancedOptionList.prototype.applyNestedListMapping = function(keys){
	keys = keys || [];
	var showAll = (keys.length === 0); //no parent value = show all child options
	for (var k = 0; k < keys.length; k++){
		if (this.field.NestedListMap[keys[k].toLowerCase()] === null){	//null = allow all
			showAll = true;
		}
	}
	
	if (showAll){
		this.optionList = this.fullList;
	} else {
		this.optionList = [];
		for (var k = 0; k < keys.length; k++){
			var currentValue = keys[k].toLowerCase();
			var allowedOptions = this.field.NestedListMap[currentValue];		//check if there are options for this key
			for (var a = 0; allowedOptions && a < allowedOptions.length; a++){
				var allowed = allowedOptions[a].toLowerCase(); 					//should already be lowercase, but the API has been known to make mistakes... from time to time
				if (this.nestedMapIndex[allowed]){								//look up the allowed option and add it for display
					this.optionList.push(this.nestedMapIndex[allowed]);
				}
			}
		}

		if (this.currentValue) { //allowed values might not include the current values
			var allowedValues = this.optionList.map(function (option) {
				return ViewUtil.getID(option.URL);
			});
			this.currentValue = this.currentValue.filter(function (val) {
				return $.inArray(val, allowedValues) !== -1;
			});
		}
		this.updateLabel();
	}
}

EnhancedOptionList.prototype.renderListview = function($page){
	$page.find('h2').text(this.field.Label);
	var $lv = $page.find('.optionLV').empty();
	ViewUtil.populateLV($lv, this.optionList, this.field.Label, null, true);
	$lv.filterable({
		defaults: true,
		input:    $('#optionSearch'),
		enhanced: true
	});
	setTimeout(function(){
		$lv.filterable('refresh');
	}, 0); //make sure any filtering from previous loads is reset

	$page.find('#optionSearch').val('').parent().showIf(this.optionList && this.optionList.length > EnhancedOptionList.COUNT_THRESHOLD);
}

/**
 * Implement the jQuery val function to allow this to act as an input field
 */
EnhancedOptionList.prototype.val = function(setValue){
	if (arguments.length > 0){
		this.currentValue = setValue;
		return this;
	}

	if (this.opened){  //field may have been edited
		var value = this.currentValue;
		if (this.field.Maximum > 1){
			return value;	//return array of values because this is multi select
		} else {
			return ($.isArray(value) && value.length) ? value[0]  : null; //return the first value if set, or null
		}
	} else {
		return this.field.Maximum > 1
			? this.InitialValue
			: ($.isArray(this.InitialValue) && this.InitialValue.length
				? this.InitialValue[0]
				: null);
	}
}

/**
 * Implement jQuery.is
 * @return boolean
 */
EnhancedOptionList.prototype.is = function(selector){
	if (selector.toLowerCase() === "enhancedoptionlist") return true;

	return this.$row.is(selector);
};

EnhancedOptionList.prototype.loadSelector = function(){
	this.opened = true;

	ViewUtil.selector.start({
		callbackOK: $.proxy(this.selectorCallback, this),
		callbackCancel: $.proxy(this.cancelCallback, this),
		data: this.field.Maximum > 1 ? this.selectorData() : [],
		previousObject: this,
        goBack: true,
        makeBackup: false,
        single: !(this.field.Maximum > 1),
        extraBack: false,
		field: this.field
	});
    $("body").pagecontainer( "change", '#optionList', {});
};

EnhancedOptionList.prototype.selectorData = function(){
	var data = {};
	for (var i = 0; this.currentValue && i < this.currentValue.length; i++){
		var item = this.currentValue[i];
		if (String(item).indexOf('/') == -1){ //id only. convert to url
			item = "/option/" + item;
		}
		var bits = item.split("/");
		var id   = bits.pop();
		var type = bits.pop();
		if (this.optionIndex[id]) { //make sure all values are still valid options
			var label = this.optionIndex[id];
			data[type + "-" + id] = {
				id: id,
				label: label,
				checked: true
			};
		}
	}
	return data;
}

EnhancedOptionList.prototype.selectorCallback = function(data){
	this.currentValue = [];
	
	for (var key in data){
		if (data[key].checked == false){
			delete data[key];
			continue;
		}

		var bits = key.split('-');
		var id = parseInt(bits[1], 10);
		this.currentValue.push(this.valueIndex[id]);
	}
	this.updateLabel();
	this.change();
}
EnhancedOptionList.prototype.updateLabel = function(){
	var labels = [];
	for (var v = 0; this.currentValue && v < this.currentValue.length; v++){
		var key = this.currentValue[v]+'';
		if (key.indexOf('/') !== -1) 	key = ViewUtil.getID(key);
		if (this.optionIndex[key]) 		labels.push(this.optionIndex[key]);
	}
	var label = labels.length ? labels.join(", ") : "(none)";
	this.$row.find('span.valueLabel').text(label);
}
EnhancedOptionList.prototype.cancelCallback = function(){
	//do nothing
}


/**
 * An input to edit the location field parts
 */
function LocationInput(){
	jQueryInterface.call(this);
    this.fields = [];
    var onebox = OCA.Settings.LocationFieldSingleBox;
    var suburbLabel = onebox ? OCA.getI18n().gettext("Location") : OCA.getI18n().gettext("Suburb");
    var latlng = OCA.Settings.LocationFieldShowLatLng !== false;
    var subType = onebox ? 'textarea' : null;

	this.fields = [
		{Label: OCA.getI18n().gettext("Level/unit etc"),dataKey: "InternalAddress", hidden: onebox},
		{Label: OCA.getI18n().gettext("Building name"),	dataKey: "BuildingName",    hidden: onebox},
		{Label: OCA.getI18n().gettext("Number"),		dataKey: "StreetNumber",    hidden: onebox},
		{Label: OCA.getI18n().gettext("Street"),		dataKey: "StreetName",      hidden: onebox},
		{Label: suburbLabel,                    		dataKey: "Suburb",          type:  subType},
		{Label: OCA.getI18n().gettext("State"),			dataKey: "State"},
		{Label: OCA.getI18n().gettext("Post Code"),		dataKey: "Postcode",        hidden: onebox},
		{Label: OCA.getI18n().gettext("Country"),		dataKey: "Country"},
        {Label: OCA.getI18n().gettext("Latitude"),		dataKey: "Lat",             hidden: !latlng},
        {Label: OCA.getI18n().gettext("Longitude"),		dataKey: "Lng",             hidden: !latlng},
        {Label: '',	hidden: true, type: 'boolean',      dataKey: "IsTiedMarker"}
	];
	this.listview = $("<ul data-inset='true'>");
    this.expanded = false;
}
LocationInput.prototype = new jQueryInterface;
LocationInput.prototype.constructor = LocationInput;

/** 
 * Render the location field input.
 * The individual parts are only shown if the user selects the field.
 */
LocationInput.prototype.render = function(field, data){

	var value = (data && typeof data == 'object') //protect against API sending a locationID
		? ViewUtil.formatLocationData(data, "\n")
		: "";
		
	field.InitialValue = (data) 
		? JSON.parse(JSON.stringify(data))
		: {};
	this.data = typeof data == "object" ? data : {};
	this.field = field;

    this.$textarea = $("<textarea />").addClass('ui-body-c ui-input-text').text(value).attr('readonly', 'readonly');
    
	var row = $("<li class='ui-field-contain'/>")
		.append($("<label />").prop("for", field.Label).text(field.Label))
		.append(this.$textarea);
		
	this.$row = row;
	this.setReadOnly(field.IsReadOnly == 1);
	return row;
}
LocationInput.prototype.addClickHandler = function(){
	if (!this.clickHandlerActive && !this.expanded){
		this.$row.one('click', function(e){
			for (var f=0; f < this.fields.length; f++){
				var locField = this.fields[f];
				var value = (this.data) ? this.data[locField.dataKey]: null;
	            if (value && (locField.dataKey == 'Lat' || locField.dataKey == 'Lng')) {
	                value = parseFloat(value).toFixed(5);
	            }
	            var input;

	            if (locField.type == 'boolean'){
	                input = $("<input />").prop('type', 'hidden').prop('checked', value);
	            } else if (locField.type == 'textarea'){
	                input = $('<textarea />')
	            } else {
				    input = $("<input />").prop("type", 'text');
	            }
	            input.prop("name", locField.Label.toLowerCase()).prop("id", locField.Label.toLowerCase()).prop("value", value);
				locField.Input = input;
				locField.InitialValue = value;
	            if (!locField.hidden){
	                var locrow = $("<li class='ui-field-contain'/>")
	                    .append($("<label />").prop("for", locField.Label.toLowerCase()).text(locField.Label))
	                    .append(input);
	                this.listview.append(locrow);
	                input.on('blur', $.proxy(this.changeHandler, this));
	            }
			}

			this.$textarea.remove();
	        this.$textarea = null;
	        $(e.currentTarget).append(this.listview);
			this.listview.listview();
			this.listview.enhanceWithin();
			this.listview.addClass('edit-view');
	        this.expanded = true;
		}.bind(this));
		this.clickHandlerActive = true;
	}
}
LocationInput.prototype.removeClickHandler = function(){
	this.$row.off('click');
	this.clickHandlerActive = false;
}

LocationInput.prototype.changeHandler = function(){
	if(this.changeCallbacks.length){
		for (var c = 0; c < this.changeCallbacks.length; c++) this.changeCallbacks[c]();
	}

    if (OCA.Settings.LocationFieldGeocodeDefault === false){
        return; //dont need to geocode according to the settings
    }

    var data = this.val();
    delete data.InternalAddress; //these values tend to just confuse the geocoder
    delete data.BuildingName;
    var addrString = ViewUtil.formatLocationData(data, ' ');

    if (addrString != this.currentGeocodeAddress){ //only geocode if address has changed
        this.currentGeocodeAddress = addrString;
        theSilentCartographer.externalGeocode(addrString, $.proxy(this.geocodeCallback, this));
    }
};

LocationInput.prototype.geocodeCallback = function(geocoded){
    if (geocoded){
        for (var f=0; f < this.fields.length; f++){
            var field = this.fields[f];
            if (field.dataKey == 'Lat') field.Input.val(geocoded.location.getLatitude().toFixed(5));
            if (field.dataKey == 'Lng') field.Input.val(geocoded.location.getLongitude().toFixed(5));
            if (field.dataKey == 'IsTiedMarker') field.Input.val(true);
        }
    }
}

/**
 * Implement jQuery.prop by calling the listview
 */
LocationInput.prototype.prop = function(){
    if (arguments.length && arguments[0] == 'disabled'){
    	this.setReadOnly(arguments[1]);
    } else {
    	return this.listview.prop.apply(this, arguments);
    }
}

/** 
 * Implement the jQuery val function so this can act as an input
 */
LocationInput.prototype.val = function(value){
	if (!this.data) this.data = {};

    //set
    if (value){
        for (var k in value) { //overwrite any data keys specified in value
            this.data[k] = value[k];
        }
        this.update();
        return this;
    }

    //get
	for (var f=0; f < this.fields.length; f++){
		var field = this.fields[f];
		if (field.Input) {
			this.data[field.dataKey] = field.Input.val();
		}
	}
	if (!$.isEmptyObject(this.data)) { //only set tied marker if there are some location values
	this.data.IsTiedMarker = (this.data.Lat && this.data.Lng && !this.field.IsSubField)  //sub-location-fields do not contribute geometry
	}

	return this.data;
}

LocationInput.prototype.update = function(){
    if (this.expanded){
        for (var f=0; f < this.fields.length; f++){
            var field = this.fields[f];
            var val = this.data[field.dataKey];
            if (field.dataKey == 'Lat' || field.dataKey == 'Lng') val = val.toFixed(5);
            field.Input.val(val);
        }
    } else {
        var value = (this.data)
            ? ViewUtil.formatLocationData(this.data, "\n")
            : "";
        this.$textarea.val(value);
    }
}
LocationInput.prototype.setReadOnly = function(readonly){
	if (readonly){
		this.removeClickHandler();
	} else {
		this.addClickHandler();
	}
	if (this.$textarea){
		this.$textarea.toggleClass('ui-state-disabled',readonly);
		this.$textarea.prop('disabled',readonly);
	} else {
		this.listview.find('input').each(function(){
			$(this).parent('div').toggleClass('ui-state-disabled',readonly);
			$(this).prop('disabled',readonly);
		});
	}
}

/** old 'rich' text input - used by wp8 only */
function RichTextInput(field){
	jQueryInterface.call(this, field);
	this.field = field;
	this.textarea = field.Input;
	field.InitialValue = this.val();
	field.Input = this;
}
RichTextInput.prototype = new jQueryInterface;
RichTextInput.prototype.constructor = RichTextInput;

RichTextInput.prototype.val = function(){
	var text = this.textarea.val();
	text = this.entitise(text);
	text = this.nl2br(text);
	return text;
}

/**
 * Convert new lines to br tags.
 * @see OCA_CKEditor_BasisWgt::plainToHtml
 */
RichTextInput.prototype.nl2br = function(text){
	//remove the last new line
	text = text.replace(/(\r\n|\n)$/g, '');

	var paras = text.split(/\n\n/);
	var value = "";
	for (var p = 0; p < paras.length; p++){
		var bits = paras[p].split(/(\r\n|\n)/);
		value += "<p>" + bits.join("<br />\n") + "</p>\n";
	}
	if (value == "<p></p>\n") {
		value = ""; //empty p tags are not a value. set it back to an empty string so it evaluates to false
	}
	return value;
}

RichTextInput.prototype.entitise = function(text){
	return text.replace(/\&/g, "&amp;").replace(/\</g, "&lt;").replace(/\>/g, "&gt;");
}

RichTextInput.prototype.prop = function(){
    return this.field.input.prop.apply(this, arguments);
}
RichTextInput.prototype.setReadOnly = function(readonly){
	if (readonly){
		this.textarea.addClass('ui-state-disabled');
		this.textarea.prop('disabled','disabled');
	} else {
		this.textarea.removeClass('ui-state-disabled');
		this.textarea.removeProp('disabled');
	}
}

function MediaDeselectorInput(view, field){
	this.view = view;
	this.field = field;
	this.data = {};
}

MediaDeselectorInput.prototype.add = function(url){
	this.data[url] = true;
}
MediaDeselectorInput.prototype.val = function(){
	return this.data;
}

function MediaSelectorInput(view, field){
	jQueryInterface.call(this, field);
	this.view  = view;
	this.data  = {};
}
MediaSelectorInput.prototype = new jQueryInterface;
MediaSelectorInput.prototype.constructor = MediaSelectorInput;

MediaSelectorInput.prototype.render = function(){
	this.$row = $("<li />").appendTo(this.view.listview);
	this.$div = $("<div class='addmedia edit-mode' />").appendTo(this.$row);
	this.$add = $("<a href='#' data-role='button' data-inline='true' class='add media' data-theme='b'>" + OCA.getI18n().gettext('Add media') + "</a>").appendTo(this.$div);
	this.$add.on('click', $.proxy(this.loadSelector, this));
	if (device.platform == "Mobile Interface") this.$add.hide();	//the plugin showIf() function doesnt play nice with this button
	return this;
}

MediaSelectorInput.prototype.loadSelector = function(){
    ViewUtil.selector.start({
        previousObject: this
    });
	FileApp.mediaSelectCallback = $.proxy(this.selectorCallback, this);
    $("body").pagecontainer( "change", "#filesystemMediaSelect", {});
}

MediaSelectorInput.prototype.selectorCallback = function(url, name, noRefresh){
	this.data[url] = name;
	var self = this;
	var $photo = $("<li class='ui-li-static ui-body-inherit'><img src='" + url + "' class='listview thumbnail' />" + this.data[url] + ViewUtil.ocaicon('close2 medium inline-right edit-mode') + "</li>")
	this.$row.before($photo);
	$photo.find('span.icon').on('click', function(){
		$photo.remove();
		delete self.data[url];
	});
	if (!noRefresh) {
		this.view.listview.listview('refresh');
	}
}

MediaSelectorInput.prototype.val = function(){
	return $.isEmptyObject(this.data) ? null : this.data;
}

function FileInput(view, field, data){
	jQueryInterface.call(this, field, data);
	this.view  = view;
	this.data  = data;
}
FileInput.prototype = new jQueryInterface;
FileInput.prototype.constructor = FileInput;

FileInput.prototype.render = function(){
	this.$row = $("<li class='ui-field-contain ui-li-static field' />")
			.append($("<label />").prop("for", this.field.Label.toLowerCase()).text(this.field.Label))
			.appendTo(this.view.listview);

	this.$div  = $("<div class='addmedia' />").appendTo(this.$row);
	this.$file = $("<input type='file' data-enhanced='true'/>").appendTo(this.$div).hide();
	this.$add  = $("<a href='#' data-role='button' data-inline='true' class='add media' data-theme='b'>" + OCA.getI18n().gettext('Add media') + "</a>").appendTo(this.$div);
	this.$clear  = $("<a href='#' data-role='button' data-inline='true' class='clear'  data-theme='b'>" + OCA.getI18n().gettext('Clear')  + "</a>").appendTo(this.$div);

	if (this.data && this.data.name) { 	//existing data - show label, hide add button
		var isImage = this.data.dataURI && this.data.dataURI.substr(0,10) == 'data:image';
		var $photo = isImage
			? $("<li class='initialValue'><img src='" + this.data.dataURI + "' class='listview thumbnail' />" + this.data.name + "</li>")
			: $("<p class='initialValue'>" + this.data.name + "</p>");

		this.$div.before($photo);
		this.$add.hide();
		//revert button is only available if there is an initial value to revert to.
		this.$revert = $("<a href='#' data-role='button' data-inline='true' class='revert' data-theme='b'>" + OCA.getI18n().gettext('Revert') + "</a>").appendTo(this.$div);
		this.$revert.hide(); 			//revert is hidden until user clears field
	} else {							//no data - hide clear
		this.$clear.hide();

	}

	this.setReadOnly(this.field.IsReadOnly == 1);

	return this;
}
FileInput.prototype.setReadOnly = function(readonly){
	if (readonly){
		this.removeClickHandler();
		this.$div.addClass('ui-state-disabled');
		this.$file.prop('disabled','disabled');
	} else {
		this.addClickHandler();
		this.$div.removeClass('ui-state-disabled');
		this.$file.removeProp('disabled');
	}
}
FileInput.prototype.addClickHandler = function(){
	if (!this.clickHandlerActive){
		this.$add.on('click', $.proxy(this.loadSelector, this));

		this.$clear.on('click', function(){
			if (this.data && this.data.filepath){
				fileStore.clearFiles([this.data.filepath]);
			}
			this.data = null;
			this.$row.find('.selectedValue').remove();
			this.$add.show();
			this.$clear.hide();
			this.$row.find('.initialValue').hide();
			if (this.$revert){
				this.$revert.show();
			}
			this.change();
		}.bind(this));

		if (this.$revert){
			this.$revert.on('click', function(){
				this.$clear.show();
				this.$revert.hide();
				this.$add.hide();
				this.data = this.field.InitialValue;
				this.$row.find('.initialValue').show();
				this.$row.find('.selectedValue').remove();
			}.bind(this));
		}
		this.clickHandlerActive = true;
	}
}
FileInput.prototype.removeClickHandler = function(){
	this.$add.off('click');
	this.$clear.off('click');
	if (this.$revert){
		this.$revert.off('click');
	}
	this.clickHandlerActive = false;
}

FileInput.prototype.loadSelector = function(){
	var self = this;
	if (device.platform == "Mobile Interface"){
		this.$file.click();
		this.$file.one('change', function(e){
			var files = e.target.files;
			if (files.length){
				self.data = files[0];

				var isImage = self.data.type && self.data.type.substr(0,5) == 'image';
				var $photo = isImage
					? $("<li class='selectedValue'><img src='' class='listview thumbnail' />" + self.data.name + "</li>")
					: $("<p class='selectedValue'>" + self.data.name + "</p>");

				self.$row.find('.selectedValue').remove();
				self.$div.before($photo);
				self.$clear.show();
				self.$add.hide();
				var reader = new FileReader();
				reader.onloadend = function(){
					if (isImage){
						$photo.find('.thumbnail').attr('src', reader.result);
					}
					self.data.dataURI = reader.result;
				}
				reader.readAsDataURL(files[0]);
				self.change();
			}
		})
	} else {
		ViewUtil.selector.start({
			previousObject: this
		});
		FileApp.mediaSelectCallback = $.proxy(this.selectorCallback, this);
		$("body").pagecontainer( "change", "#filesystemMediaSelect", {});
	}
}

FileInput.prototype.selectorCallback = function(filepath, name, mime){
	this.data = {filepath: filepath, name: name, mime: mime};
	this.$row.find('.selectedValue').remove();

	var isImage = mime && mime.substr(0,5) == 'image';;
	var $photo = isImage
		? $("<li class='selectedValue'><img src='' class='listview thumbnail' />" + name + "</li>")
		: $("<p class='selectedValue'>" + name + "</p>");
	this.$clear.show();
	this.$add.hide();
	this.$div.before($photo);
	this.view.listview.listview('refresh');
	new Gopher({url: filepath, mode: 'data', mime: mime, dontCheckCache: true}, $.proxy(this.gotDataUri, this, isImage), function(){
//		console.log('couldnt get file!', url, arguments)
	}).run();
}

FileInput.prototype.gotDataUri = function(isImage, dataURI){
	if (isImage){
		this.$row.find('.thumbnail').attr('src', dataURI);
	}
	this.data.dataURI = dataURI;
	this.change();
}

FileInput.prototype.val = function(setValue){
	if (arguments.length > 0){
		this.data = setValue;
		return this;
	}
	return $.isEmptyObject(this.data) ? null : this.data;
}

FileInput.prototype.getAPIValue = function(){
	if (this.data && this.data.dataURI) {
		return {
			dataURI: this.data.dataURI, //data is the base64 val of the selected file
			name: this.data.name,
			filepath: this.data.filepath //pass filepath in for offline sync data storage only
		};
	} else if (this.data){ //existing data unchanged
		return this.data;
	} else {
		return null;
	}
};

FileInput.prototype.getFilesToClean = function(){
	if (this.data && this.data.filepath){
		return [this.data.filepath];
	}
	return [];
}


function GeometryInput(view, field, restrictedFeatureSymbologies){
	jQueryInterface.call(this, field);
    this.view = view;
	this.restrictedFeatureSymbologies = restrictedFeatureSymbologies;

    if (!$.isEmptyObject(field.InitialValue) && field.InitialValue.restorableGeometry){
        this.data = field.InitialValue.data;
        this.restorableGeometry = field.InitialValue.restorableGeometry;
        field.InitialValue = this.data; //for has changed comparison
    } else {
        this.data = field.InitialValue;
        this.restorableGeometry = false;
    }
}
GeometryInput.prototype = new jQueryInterface;
GeometryInput.prototype.constructor = GeometryInput;

GeometryInput.prototype.render = function(){
    var label = (this.data && !$.isEmptyObject(this.data)) ? OCA.getI18n().gettext('Edit mapping data') : OCA.getI18n().gettext('Create mapping data');
    this.$btn = $("<li class='geometryinput'><a href='#'>" + label + "</a></li>").appendTo(this.view.listview);
    this.$btn.on('click', $.proxy(this.loadSelector, this));
    return this;
}
GeometryInput.prototype.loadSelector = function(){
    linkParams.geometry = {
        type: this.view.type,
        ID: this.view.ID,
        restorableGeometry: this.restorableGeometry,
        locationFields: {}
    };
    for (var fieldID in this.view.typeData.Fields){
        if (this.view.typeData.Fields[fieldID].Input instanceof LocationInput){
            linkParams.geometry.locationFields[fieldID] = this.view.typeData.Fields[fieldID].Input.val();
        }
    }

	linkParams.restrictedFeatureSymbologies = this.restrictedFeatureSymbologies;

    ViewUtil.selector.start({
        callbackOK: $.proxy(this.selectorCallback, this),
        data: this.data,
        previousObject: this
    });
    $("body").pagecontainer( "change", "#mapPage?selector=true", {});

};
GeometryInput.prototype.selectorCallback = function(response){
    if (response === null) response = {data:null, restorableGeometry:null, locationFields: null};

    this.data = response.data;
    this.restorableGeometry = response.restorableGeometry;
    this.locationFields = response.locationFields;

    if (this.data && !$.isEmptyObject(this.data)){
    	this.$btn.find('a').text(OCA.getI18n().gettext("Edit mapping data"));
    } else {
    	this.$btn.find('a').text(OCA.getI18n().gettext("Create mapping data"));
    }

    if (this.locationFields && !$.isEmptyObject(this.locationFields) && this.view.typeData.Fields){
        for (var fieldID in this.locationFields){
            if (this.view.typeData.Fields[fieldID] &&  this.view.typeData.Fields[fieldID].Input instanceof LocationInput){
                this.view.typeData.Fields[fieldID].Input.val(this.locationFields[fieldID]);
            }
        }
    }
}
GeometryInput.prototype.val = function(){ return this.data; };

router.add({
    "#locationEdit": function(type, match, ui, page, e){
        new LocationEdit(page);
    }
});
function LocationEdit(page){
    this.$page = $(page);
    this.$content = this.$page.find('.ui-content');
    this.fields = [
        {Label: "Level/unit etc",	dataKey: "InternalAddress"},
        {Label: "Building name",	dataKey: "BuildingName"},
        {Label: "Number",			dataKey: "StreetNumber"},
        {Label: "Street",			dataKey: "StreetName"},
        {Label: "Suburb",			dataKey: "Suburb"},
        {Label: "State",			dataKey: "State"},
        {Label: "Post Code",		dataKey: "Postcode"},
        {Label: "Country",			dataKey: "Country"}
    ];
    this.data =			linkParams["locationEdit"].data;
    this.parentField =	linkParams["locationEdit"].field;
    this.parentLI =		linkParams["locationEdit"].li;
    this.render();
}
LocationEdit.prototype = new TypeEdit;
LocationEdit.prototype.constructor = LocationEdit;
LocationEdit.prototype.render = function(){
    this.listview = $("<ul>");
    for (var f=0; f < this.fields.length; f++){
        var field = this.fields[f];
        this.fieldRender(field, this.data[field.dataKey]);
    }
    this.$content.empty().append(this.listview);
    this.listview.listview();
    this.listview.addClass('edit-view');
    this.$content.enhanceWithin();
}


SubformInput = function(field){
	jQueryInterface.call(this);
    this.field = field;
}
SubformInput.prototype = new jQueryInterface;
SubformInput.prototype.constructor = SubformInput;
/*
 * Calculate the value of this subform by looping through all inputs in all rows
 * Returns an array of objects. Each object represents one row and is keyed by subfieldID (sfid).
 */
SubformInput.prototype.val = function(){
    var value = [];
    for (var r = 0; r < this.field.SubFieldInputs.length; r++){
        if (!this.field.SubFieldInputs[r]) continue;	//rows may be removed,
        var inputs = this.field.SubFieldInputs[r];
        var row = {};
        for (var sfid in inputs){
			row[sfid] = inputs[sfid] ? inputs[sfid].val() : null;
			if (inputs[sfid] && inputs[sfid].getAPIValue){ //overwrite the val() output if there's a specialised function to get the submission value
				row[sfid] = inputs[sfid].getAPIValue();
			}
        }
        value.push(row);
    }
    return value;
}
SubformInput.prototype.setReadOnly = function(readonly){
	for (var r = 0; r < this.field.SubFieldInputs.length; r++){
		if (this.field.SubFieldInputs[r]){
			for (var sfid in this.field.SubFieldInputs[r]){
				if (readonly){
					this.field.SubFieldInputs[r][sfid].setReadOnly(readonly);
				} else if (this.field.SubFieldInputs[r][sfid].Field.hasOwnProperty('IsReadOnly')){
					if (this.field.SubFieldInputs[r][sfid].Field.IsReadOnly == "2"){
						this.field.SubFieldInputs[r][sfid].Field.readOnlyCheck();
					} else if (this.field.SubFieldInputs[r][sfid].Field.IsReadOnly == "0"){
						this.field.SubFieldInputs[r][sfid].setReadOnly(readonly);
					}
				} else if (!this.field.SubFieldInputs[r][sfid].Field.Readonly){
					this.field.SubFieldInputs[r][sfid].setReadOnly(readonly);
				}
			}
		}
	}
};

/** ask every input on every row for files that need cleanup after successful submission */
SubformInput.prototype.getFilesToClean = function(){
	var files = [];
	for (var r = 0; r < this.field.SubFieldInputs.length; r++){
		if (!this.field.SubFieldInputs[r]) continue;
		var inputs = this.field.SubFieldInputs[r];
		for (var sfid in inputs){
			if (inputs[sfid] && inputs[sfid].getFilesToClean){
				files = files.concat(inputs[sfid].getFilesToClean());
			}
		}
	}
	return files;
}