/**
 * Extend TypeView to provide the edit interface for a type
 * @constructor
 */
function TypeEdit(id, page){
	this.typeAliases = {
		"number": "number",
		"email": "email",
		"url": "url",
		"phone": "tel",
		"mobile": "tel",
		"fax": "tel",
		"sgltxt": "text",
		"datetimeopt":"text",
		"datetime":"text",
		"date":"text"
	};
	this.initTypeEdit(id, page);
}
TypeEdit.prototype = new TypeView;
TypeEdit.prototype.constructor = TypeEdit;
TypeEdit.prototype.initTypeEdit = function(id, page, type){
	this.initTypeView(id, page, type);
    this.mode = id ? 'edit' : 'new';
	this.externalHandlers = false;
	this.footer.hide();

	if (window.device !== undefined && window.device.platform !== "Win32NT"){ //not available until phonegap loads
		this.typeAliases["datetimeopt"] = "datetime-local";
		this.typeAliases["datetime"] = "datetime-local";
		this.typeAliases["date"] = "date";
    }
	this.nestedLists = [];
    this.derivedIDs = [];
    this.datediffIDs = [];
    this.sequences = {};
};
/** 
 * Overwrite TypeView.fieldRender to display an input
 */
TypeEdit.prototype.fieldRender = function(field, value){
	var type = "text";
	if (this.typeAliases[field.Type]){
		type = this.typeAliases[field.Type];
	}
	var input = $("<input />")
			.prop("type", type)
			.prop("name", field.Label.toLowerCase())
			.prop("id", field.Label.toLowerCase())
			.prop("value", value).attr('data-clear-btn', true)
            .addClass('field-' + field.ID);
    if (field.Tooltip){
        input.attr('placeholder', field.Tooltip);
    }
    if (field.Maximum) {
        input.attr('maxlength', field.Maximum);
        if (device.platform == 'Android'){ //built-in iOS support is perfect. Android has open bugs reports so a JS solution is required
            input.on('keydown', function(event) {
                if (event.currentTarget.value.length >= event.currentTarget.maxLength) {
                    event.preventDefault();
                    return false;
                }
            });
        }
    }
    input.setReadOnly = function(readonly){
    	$(this).prop('disabled',readonly);
    	$(this).parent('div').toggleClass('ui-state-disabled',readonly);
    };
	field.Input = input;
	field.InitialValue = value;
	
	var row = $("<li class='ui-field-contain' />")
		.append($("<label />").prop("for", field.Label.toLowerCase()).text(field.Label));
    if (field.SequenceID && !this.ID){ //field has a sequence and this is a create operation
        this.sequences[field.ID] = field.SequenceID;
        row.append($("<input type='text' disabled='true'/>").addClass('seqfield-' + field.ID).val('(auto)'));
	}
	row.append(input);
	
	input.setReadOnly(field.IsReadOnly == 1 || (!field.hasOwnProperty('IsReadOnly') && field.Readonly));

	if (this.prepend && this.listview.children.length > 0){
		row.before(this.listview);
	}else{
		this.listview.append(row);
	}
	return row;
}
/**
 * After a row has been rendered, apply any UI enhancements.
 * Currently, this just listens to value changes for required fields and applies/hides styles as appropriate
 */
TypeEdit.prototype.enhanceRow = function(row, field){
	if (field.ApplyDefaultOnSave == '1' && !this.ID && field.Input && field.Input.prop){
		//fields that apply default on save are disabled.
		field.Input.prop('disabled', true);
		//if they have a default value set they should display (auto) but submit as empty to the API
		if (field.DefaultValue) {
			field.Input.val('(auto)').getAPIValue = function(){ return null; };
		}
	}

	//some fields can be required based on the value of other fields. set up listeners for those changes
	if (field.IsRequired == '2' && !$.isEmptyObject(field.IsRequiredFields)){
		this.handleRequired(field, row);
	}
	

	if ((field.Required || field.IsRequired == '2') ||
		(field.Minimum !== undefined && field.Minimum > 0)
	){
		if (field.Input && field.Input.change && row) {
			field.Input.change(function () {
				//the required status can change dynamically - check that first
				if (!field.Required || field.Readonly) {
					row.removeClass('required');
					return;
				}

				//otherwise, set the required class based on whether the field has a value
				var val = field.Input.val();
				if ((!val || $.isEmptyObject(val) || ($.isArray(val) && val.length == 0)) && !field.SequenceValue) {
					row.addClass('required');
				} else {
					row.removeClass('required');
				}
			});
			field.Input.change(); //set initial status by triggering the handler
		} else {
			
		}
    }
    if (field.IsReadOnly == '2' && !$.isEmptyObject(field.IsReadOnlyFields)){
		this.handleReadOnly(field, row);
	} else if (field.IsReadOnly == 1 || (!field.hasOwnProperty('IsReadOnly') && field.Readonly)){
    	field.Input.prop('disabled', true);
    }

	if (field.Visibility == '1' || !$.isEmptyObject(field.VisibilityFields)){
		this.handleVisibility(field, row);
	}
};
/**
 * Finish rendering the UI.
 * Called after the fields are rendered
 */
TypeEdit.prototype.afterRender = function(){
	this.listview.addClass('edit-view');
	this.content.enhanceWithin();
    this.content.trigger('rendered');
	var self = this;
	this.page.find(".ui-footer a[href='#save']").off().on('click', function(e){
        linkParams.selectorCancel = false;
        self.submit();
		e.preventDefault();
		return false;
	});
    this.page.find(".ui-footer a[href='#cancel']").off().on('click', function(e){
        if (self.lock){
            self.cancelLock();
            e.preventDefault();
            return false;
        }
    }).find('span').remove();

    if (this.lock){
        this.page.find(".ui-footer a[href='#cancel']").append(ViewUtil.ocaicon('lock_open white pad-left'));
    }
	this.footer.show();
	this.addNestedLists();
    this.resolveExpressions();
};
/**
 * Render a multitxt field as a text area
 */
TypeEdit.prototype.multitxtRender = function(field, value){
    value = value || "";
    if (value) value = value.replace(/\r/g, ""); //remove carriage returns so the diff later works
	var input = $("<textarea />").prop("name", field.Label.toLowerCase()).prop("id", field.Label.toLowerCase()).addClass('field-' + field.ID).text(value);
	field.Input = input;
	field.InitialValue = value;
	var row = $("<li class='ui-field-contain' />")
		.append($("<label />").prop("for", field.Label.toLowerCase()).text(field.Label))
		.append(input);

	// if the text area is focused, trigger the jquerymobile autogrow
	input.one('focus', function(){
		input.textinput('refresh');
	});
	input.setReadOnly = function(readonly){
		$(this).prop('disabled',readonly);
    	$(this).toggleClass('ui-state-disabled',readonly);
	}

	this.listview.append(row);
    return row;
};

/**
 * If a rich text field has values in it, don't allow the user to edit because all formatting will be lost.
 * If it's empty, just handle this like a multi line text field.
 */
TypeEdit.prototype.richtextRender = function(field, value){
	var $row;
	var useCKEditor = (device.platform != 'Win32NT'); //disable for WP8 devices

	if (useCKEditor){
		$row = this.multitxtRender(field, value); //passing HTML to text area is okay, and will magically work in CKEditor
		var $textarea = field.Input;
		$textarea.wrap('<div class="ui-input-ckeditor" />');

		field.Input = new CKEditorInput(field, value);
		field.Input.enhance($textarea[0]);
	} else {
		//dont use ckeditor. show rich text preview if a value is set, otherwise a plain text interface
		if (value){
			$row = TypeView.prototype.richtextRender.call(this, field, value);
			$row.find('iframe').css('opacity', '0.5'); //grey out to indicate disabled
		} else {
			$row = this.multitxtRender(field, value);
			field.Input = new RichTextInput(field);
		}
	}

    return $row;
};
/**
 * Render a location field as a LocationInput
 * @see LocationInput
 */
TypeEdit.prototype.locationRender = function(field, data){
	field.Input = new LocationInput();
	var row = field.Input.render(field, data);
	this.listview.append(row);
	return row;
};
/**
 * Render an opt field as a EnhancedOptionList if multiple selection is allowed, otherwise as a normal HTML SELECT
 * @see EnhancedOptionList
 */
TypeEdit.prototype.optRender = function(field, data){
	var input = null, row = null;
	var rendernormal = true;
	if (!field.Options) field.Options = []; //undefined options shouldnt happen in prod but can occur in dev. catch it.

	if (field.Options.length > EnhancedOptionList.COUNT_THRESHOLD){
		rendernormal = false;
	}
	for (var i = 0; i < field.Options.length; i++){
		if (field.Options[i][1].length > EnhancedOptionList.LENGTH_THRESHOLD){
			rendernormal = false;
		}
	}
	if (field.Maximum > 1){
		rendernormal = false;
	}

	if (rendernormal){
		// normal select
		input = $("<select />").prop("name", field.Label.toLowerCase()).prop("id", "field-"+field.ID);
        if (field.Define) input.addClass('define-' + field.Define);
        TypeEdit.renderOptions(field,input);
		row = $("<li class='ui-field-contain' />")
			.append($("<label />").prop("for", field.Label.toLowerCase()).text(field.Label))
			.append(input);
		if (field.Minimum === "0" && data === false) {
//			
		} else {
			input.val(data);
		}
		input.setReadOnly = function(readonly){
			$(this).prop('disabled',readonly);
    		$(this).parent('div').toggleClass('ui-state-disabled',readonly);
		}
		
	} else {
		input = new EnhancedOptionList(field);
		row = input.render(data);
	}
	field.Input = input;
	field.InitialValue = data;
    row.addClass('field' + field.ID).data('input', input);
	this.listview.append(row);
	if (field.NestedListParentLabel){
		this.nestedLists.push(field);
	}
    var lv = this.listview;
    input.change(function(){
        lv.trigger('fieldChange' + field.ID, input);
		row.trigger('change');
    });
	return row;
};
TypeEdit.prototype.handleVisibility = function(field, row){
    if (!row){
        return; //no row, nothing to handle
    }
    if (field.VisibilityFieldID){
        field.VisibilityFields = {}
        field.VisibilityFields[field.VisibilityFieldID] = [field.VisibilityFieldOptionID];
    }
    var $lv = this.fullLV || this.listview;
    for (var id in field.VisibilityFields){
        $lv.on('fieldChange' + id, $.proxy(this.checkVisibility, this, field, row, $lv));
    }
    this.content.on('rendered', $.proxy(this.checkVisibility, this, field, row, $lv, true));
    row.hide();
    field.defaultApplied = false;
};
TypeEdit.prototype.checkVisibility = function(field, row, $lv, initialrender){
    var show = true;
    for (var id in field.VisibilityFields){
        var input = $lv.find('.field' + id).data('input');
        if (input){
            var val = input.val();
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
    }
    if (show){
		//handle ApplyDefaultWhenVisible - meaning if we are editing a field and making it visible for the first time, the default value should be set
    	if (this.ID && this.typeData.ApplyDefaultWhenVisible && initialrender !== true && !field.defaultApplied && field.DefaultValue){
    		if (field.Input && field.Input.kill) { //call the kill method if present, to clean up any listeners and shut itself down
    			field.Input.kill();
			}
			var oldRow = row;
			var data = field.DefaultValue;
			if (typeof data == 'string') {
			data = data.replace(/\$\{((?:\\\\|\\\}|[^\}])+)\}/g,''); 	//dont show expressions in the field value
			}

			row = this[field.Type + "Render"].call(this, field, data);	//we can't just set .val(default) on the inputs - different field types have different processing steps for the default value.
			oldRow.replaceWith(row);									//re-render the whole row and replace the existing one (which is hidden, so the user shouldn't notice any reflow)
			this.enhanceRow(row, field);
			field.$row = row;
			oldRow.remove();

			field.InitialValue = null; //make sure this field is included in the submission delta - setting the default value has made a change which needs to be saved

			if (data !== field.DefaultValue){ 	//check for workflow expressions to evaluate. if they were removed, data wont match default value
				this.resolveExpression(field.ID, field.DefaultValue);
			}
			row.enhanceWithin();				//make sure the replacement row is pretty
			this.listview.listview('refresh');
		}
    	field.defaultApplied = true;
    }
    row.showIf(show);
}
TypeEdit.prototype.handleRequired = function(field, row){
	if (!row){ return; } //no row, nothing to handle
	var $lv = this.fullLV || this.listview;
	for (var id in field.IsRequiredFields){
		$lv.on('fieldChange' + id, $.proxy(this.checkRequired, this, field, row, $lv));
	}
	this.content.on('rendered', $.proxy(this.checkRequired, this, field, row, $lv));
};
TypeEdit.prototype.checkRequired = function(field, row, $lv){
	var req = true;
	for (var id in field.IsRequiredFields){
		var input = $lv.find('.field' + id).data('input');
		if (input){
			var val = input.val();
			if (!$.isArray(val)) val = [val];
			var reqField = false;
			for (var v = 0; v < val.length; v++){
				if (val[v] && val[v].indexOf('/api/') === 0){ //convert from an API endpoint (/api/v1/contactgroup/22) to the ID (22)
					var bits = val[v].split('/');
					val[v] = bits.pop();
				}
				if ($.inArray(val[v], field.IsRequiredFields[id]) !== -1) {
					reqField = true;
				}
			}
			req = req && reqField;
		}
	}

	field.Required = req;
	field.Input.change();
}
TypeEdit.prototype.handleReadOnly = function(field, row){
	if (!row || field.DerivedField){ return; }
	var $lv = this.fullLV || this.listview;
	for (var id in field.IsReadOnlyFields){
		$lv.on('fieldChange' + id, $.proxy(this.checkReadOnly, this, field, row, $lv));
	}
	field.readOnlyCheck = $.proxy(this.checkReadOnly, this, field, row, $lv);
	this.content.on('rendered', field.readOnlyCheck);
};
TypeEdit.prototype.checkReadOnly = function(field, row, $lv){
	var ro = true;
	if (!field.IsSubField || !field.ParentSubFormField.Readonly){

		for (var id in field.IsReadOnlyFields){
			var input = $lv.find('.field' + id).data('input');
			if (input){
				var val = input.val();
				if (!$.isArray(val)) val = [val];
				var roField = false;
				for (var v = 0; v < val.length; v++){
					if (val[v] && val[v].indexOf('/api/') === 0){ //convert from an API endpoint (/api/v1/contactgroup/22) to the ID (22)
						var bits = val[v].split('/');
						val[v] = bits.pop();
					}
					if ($.inArray(val[v], field.IsReadOnlyFields[id]) !== -1) {
						roField = true;
					}
				}
				ro = ro && roField;
			}
		}
	}
	
	field.Readonly = ro;
	field.Input.setReadOnly(ro);
	field.Input.change();
}
TypeEdit.prototype.addNestedLists = function(){
	for (var n = 0; n < this.nestedLists.length; n++){
		var child = this.nestedLists[n];
        var cInput = child.Input;
		var parentLabel = child.NestedListParentLabel;

		//parent change listener for child fields which are EnhancedOptionLists
		var parentChangeHandler = function(values, child){
			child.Input.applyNestedListMapping(values);
		};

		//parent change listener for child fields which are select fields
		var parentChangeHandlerSingleSelect = function(values, child){
			var showAll = (values.length === 0); //no parent value = show all child options
			if (!showAll){
				for (var v = 0; v < values.length; v++){
					var currentValue = values[v].toLowerCase();
					if (child.NestedListMap[currentValue] === null){	//null = allow all
						showAll = true;
					}
				}
			}

			var fauxChild = {DefaultValue: child.DefaultValue};
			var value = child.Input.val();
			if (showAll){
				if (child.Options.length === child.Input.children().length){
					return; //input already showing all options
				} else {
					fauxChild = child;
				}
			} else {
				fauxChild.Minimum = child.Minimum;
				fauxChild.Required = child.Required;
				fauxChild.Options = [];

				var optionLookup = {}; //look up by label - note mappings come through as lower case
				for (var i = 0; i < child.Options.length; i++){
					optionLookup[child.Options[i][1].toLowerCase()] = child.Options[i];
				}

				for (var v = 0; v < values.length; v++){
					var currentValue = values[v].toLowerCase();
					if (child.NestedListMap[currentValue]){
						for (var o = 0; o < child.NestedListMap[currentValue].length; o++){
							var allowed = child.NestedListMap[currentValue][o].toLowerCase(); //should already be lowercase, but the API has been known to make mistakes... from time to time
							if (optionLookup[allowed]) fauxChild.Options.push(optionLookup[allowed]);
						}
					}
				}

				var allowedValues = fauxChild.Options.map(function (option){
					return option[0]; //first key is value
				});
				//current value is no longer allowed. clear the field
				if (value && $.inArray(value, allowedValues) === -1){
					value = null;
				}
			}
			TypeEdit.renderOptions(fauxChild, child.Input);
			child.Input.val(value).change();
		};

		if (child.Input.is('select')) { //use single select handler
			parentChangeHandler = parentChangeHandlerSingleSelect;
		}

		//handle normal option list parent field value
		var parentSingleField = this.listview.find("select[name='" + parentLabel + "']");
		parentSingleField.on('change', $.proxy(function(parentChangeHandler, child){
			var currentLabel = this.find('option:selected').text();
			parentChangeHandler([currentLabel], child);
		}, parentSingleField, parentChangeHandler, child));

		//handle enhanced option list parent field value
		var parentMultipleField = this.listview.find("li[name='" + parentLabel + "']");
		parentMultipleField.on('change', $.proxy(function(parentChangeHandler, child){
			var eol = this.data('input');
			var labels = eol.getNestedListParentKeys();
			parentChangeHandler(labels, child);
		}, parentMultipleField, parentChangeHandler, child));

		parentSingleField.trigger('change');
		parentMultipleField.trigger('change');
	}
};

TypeEdit.prototype.resolveExpressions = function(){
    var request = {
        DerivedFields: this.derivedIDs,
        DateDiffFields: this.datediffIDs
    };
    if (!this.ID){ //for creating objects, also resolve expressions and sequences
        request.Expressions = this.expressions;
		if (!this.hasChangeListeners){ //resolve sequences, but only once on load. Once hasChangeListeners is set, sequences have loaded.
        	request.Sequences = this.sequences;
		}
    }

    var hasData = false; //check at least one part of the request is not empty before sending
    for (var k in request){
        if (request[k] && (!$.isEmptyObject(request[k]) || request[k].length)) {
            hasData = true;
        }
    }

    if (!hasData) return; //nothing to resolve

	request.Context = this.getContext();

    new Gopher({
        url: '/workflowexpressions/resolve',
        data: request,
        backgroundMode: true
    }, $.proxy(this.gotExpressions, this)).post(false);
}

/**
 * Evaluate a single expression.
 * Used for applying default values with expressions when the field becomes visible
 * @param fieldID
 * @param expression
 */
TypeEdit.prototype.resolveExpression = function(fieldID, expression){
	var request = {Expressions: {}, Context: this.getContext()};
	request.Expressions[fieldID] = expression;

	new Gopher({
		url: '/workflowexpressions/resolve',
		data: request,
		backgroundMode: true
	}, $.proxy(this.gotExpressions, this)).post(false);
}

TypeEdit.prototype.gotExpressions = function(data){
    data = data[0];
    for (var id in data.Expressions){
		this.typeData.Fields[id].Input.val(data.Expressions[id]);
    }
    this.expressions = []; //only look them up the first time, not on subsequent calls after value changes
    for (var id in data.DerivedFields){
		this.typeData.Fields[id].Input.val(data.DerivedFields[id].value);
        if (!this.hasChangeListeners){
            for (var f = 0; f < data.DerivedFields[id].fields.length; f++){
                var fid = data.DerivedFields[id].fields[f];
                if (this.typeData.Fields[fid]) this.typeData.Fields[fid].Input.change($.proxy(this.resolveExpressions, this));
            }
        }
    }
    for (var id in data.DateDiffFields){
		this.typeData.Fields[id].Input.val(data.DateDiffFields[id].value);
        if (!this.hasChangeListeners){
            for (var f = 0; f < data.DateDiffFields[id].fields.length; f++){
                var fid = data.DateDiffFields[id].fields[f];
                if (this.typeData.Fields[fid]) this.typeData.Fields[fid].Input.change($.proxy(this.resolveExpressions, this));
            }
        }
    }
    for (var id in data.Sequences){
        var val = data.Sequences[id].value;
        this.typeData.Fields[id].SequenceValue = val;
        $('.seqfield-' + id).val(val);
		this.typeData.Fields[id].Input.change();
        if (!this.hasChangeListeners){
            for (var f = 0; f < data.Sequences[id].fields.length; f++){
                var fid = data.Sequences[id].fields[f];
                if (this.typeData.Fields[fid]) this.typeData.Fields[fid].Input.change($.proxy(this.resolveExpressions, this));
            }
        }
    }
    this.hasChangeListeners = true;
}

/** render asset chooser field as an slmc of type 'asset'*/
TypeEdit.prototype.assetchooserRender = function(field, data){
	return this.slmcRender(field, data, 'assetTreeView');
};
/** render teamrole chooser field as an slmc of type 'teamrole'*/
TypeEdit.prototype.teamrolechooserRender = function(field, data){
	return this.slmcRender(field, data, 'teamroleIndex');
};
/** render resourcestructurenode chooser field as an slmc of type 'resourcestructurenode'*/
TypeEdit.prototype.resourcestructurenodechooserRender = function(field, data){
	return this.slmcRender(field, data, 'teamroleIndex'); //internal routes and references are still called teamrole
};
/** render contact chooser field as an slmc of type 'contact'*/
TypeEdit.prototype.contactchooserRender = function(field, data){
	return this.slmcRender(field, data, 'contactgroupTreeView?mode=contacts');
};
/** render eme chooser field as an slmc of type 'eme' */
TypeEdit.prototype.emechooserRender = function(field, data){
    return this.slmcRender(field, data, 'emeTreeView');
};
/** render document chooser field as an slmc of type 'document' */
TypeEdit.prototype.documentchooserRender = function(field, data){
    return this.slmcRender(field, data, 'documentfolderTreeView');
};
/** render log chooser field as an slmc of type 'log' */
TypeEdit.prototype.logentrychooserRender = function(field, data){
	return this.slmcRender(field, data, 'logIndex');
}
/** render contact group chooser field as an slmc of type 'contactgroup' */
TypeEdit.prototype.contactgroupchooserRender = function(field, data){
	return this.slmcRender(field, data, 'contactgroupTreeView?mode=groups');
}

TypeEdit.prototype.renderRelations = function(){
	this.typeData.Attachments = {InitialValue: {}};
	this.typeData.Detachments = {InitialValue: {}};
	var detacher = new MediaDeselectorInput(this, this.typeData.Detachments);
	this.typeData.Detachments.Input = detacher;
	this.listview.append($("<li data-role='list-divider'/>").text(OCA.getI18n().gettext("Related")));

	if (this.data) {
		for (var direction in this.data.RelatedObjects){
			var relations = this.data.RelatedObjects[direction];
			for (var relation in relations){
				for (var url in relations[relation]){
					var label = relations[relation][url];
					if (url.indexOf('/api/v') !== 0) url = Configuration.getAPIPath() + url;
					var match = url.match(/\/api\/v\d\/(\w+)\/(\d+)/);
					var type = match[1];
					if (type == 'document'){
						var row = $("<li>" + label + ViewUtil.ocaicon('close2 inline-right medium') + "</li>");
						row.data('url', url).on('click', 'span.icon', function(){
							detacher.add(row.data('url'));
							row.remove();
						});
						this.listview.append(row);
					}
				}
			}
		}
	}
	this.typeData.Attachments.Input = new MediaSelectorInput(this, this.typeData.Attachments).render();
	//offline mode, restore existing data
	if (this.data && this.data.Attachments && !$.isEmptyObject(this.data.Attachments)){
		for (var url in this.data.Attachments){
			this.typeData.Attachments.Input.selectorCallback(url, this.data.Attachments[url], true);
		}
	}
};

TypeEdit.prototype.renderMapping = function(){
    if (!this.supportsLocation && !(this.data && this.data.Geometry && this.data.Geometry.WKT)){ return;}
    this.listview.append($("<li data-role='list-divider'/>").text(OCA.getI18n().gettext("Mapping")));

    if (linkParams.geometry && linkParams.geometry.data){
        if (!this.data) this.data = {};
        this.data.Geometry = linkParams.geometry;
    }

    this.typeData.Geometry = {InitialValue: (this.data && this.data.Geometry && (this.data.Geometry.WKT || this.data.Geometry.data)) ? this.data.Geometry : {}};
    this.typeData.Geometry.Input = new GeometryInput(this, this.typeData.Geometry, this.typeData.RestrictedFeatureSymbologies).render();
};

/**
 * Static function to render the options for a single select option list
 *
 * @param {Object} field The field definition
 * @param {DOMNode} select the <select> dom node to add the options to
 */
TypeEdit.renderOptions = function(field,select){
	select.empty();

	if (!field.DefaultValue) {
		select.append($("<option />").prop('value', '').text("("+OCA.getI18n().gettext('none')+")"));
	}
	if (field.Options && field.Options.length){
		for (var i = 0; i < field.Options.length; i++){
			select.append($("<option />" ).prop('value', field.Options[i][0]).text(field.Options[i][1]));
		}
	}
};

/**
 * Render an SLMC widget
 *
 * Note that this can be called statically outside of a Type, eg the message compose screen
 */
TypeEdit.prototype.slmcRender = function(field, data, type){

	if (field.Options && field.Options.length){
		//convert options to optlist format
		field.Options = field.Options.map(function(option){
			return [option.URL, option.Name];
		})
		//if the field is filtered, the object type may have provided the options
		//just render as an optlist and
		var optData = !data ? null : data.map(function(object){
			return object.url;
		});
		if (field.Maximum <= 1 && optData && optData.length == 1) optData = optData[0];

		var row = TypeEdit.prototype.optRender.call(this, field, optData);

		//add a method to convert back to SLMC data
		field.Input.getAPIValue = function(){
			var value = [];
			if (field.Input instanceof EnhancedOptionList){ //field will return array of URLs
				var data = field.Input.val();
				if (data){
					if (!$.isArray(data)) data = [data];

					for (var d = 0; d < data.length; d++){
						value.push({url: data[d], label: 'dummy label'});
					}
				}
			} else { //normal <option> list
				$(this).children().each(function (i, e) {
					e = $(e);
					if (e.is(':selected') && e.val()) { //dont add the (none) option
						value.push({url: e.val(), label: e.text()});
					}
				});
			}
			return value;
		}
		return row;
	}


	type = type || this.getSLMCType(field);
	var joiner = (type.indexOf("?") === -1) ? "?" : "&";
    var slmcPage = '#' +  type + joiner + 'selector=true&id=0';

	field.Input = new SLMC(field, row, slmcPage, this);
	var row = field.Input.render(data);
	this.listview.append(row);
	return row;
}
/**
 * Format a datetime field date for display using toLocaleDateString and toLocaleTimeString
 */
TypeEdit.prototype.datetimeFormat = function (date, optional){
	//update to use OCA preferences if set

	//var time = " " + date.toLocaleTimeString();
	if (optional && date.getHours() == 0 && date.getMinutes() == 0){
		return ViewUtil.displayDate(date)
	}
	return ViewUtil.displayDateTime(date)
}
/**
 * Render a datetime field for input.
 * @android Adds a click handler to load the noggin datepicker plugin for Android only
 * @ios Converts the data to an abbreviated ISOString value in order to be parsed correctly for iOS. Removes clear button so the native date picker can handle it
 */
TypeEdit.prototype.datetimeRender = function(field, data){
	var initialValue = data;
	var date;
	if (data === 'now' || data === 'timeopened' || data === 'today'){
		date = new Date();
		if (data === 'today'){ //date only, no time
			date.setHours(0,0,0,0);
		}
	} else if (data && !isNaN(Date.parse(data))){
		date = new Date(data);
	}

	if (date){
		if (device.platform == "iOS" || device.platform == "Android" || device.platform == "Mobile Interface"){	//iOS and Android are using HTML5 datetime-local inputs
			data = ViewUtil.dateConvert(date, "%Y-%m-%dT%H:%M:00");		//requiring format according to http://www.w3.org/TR/html-markup/input.datetime-local.html#input.datetime-local.attrs.value
		} else if (date.getHours() != 0 || date.getMinutes() != 0){ 	//time is set, display time
			data = ViewUtil.displayDateTime(date);
		} else {
			data = ViewUtil.displayDate(date); 							//just display as date
		}
	}

	var row = this.fieldRender(field, data);
	row.data('date', date);
	field.Input.data('initialValue', initialValue);
	field.Input.data('hasChanged', false);

	var self = this;
	if (device.platform === 'Win32NT'){ //add wp8 date picker plugin calls
		row.on('click', function(event){
			if (event.target.tagName !== 'INPUT') {
				return;	//dont fire on row select or the clear button
			}
			if (row.data('pickerActive')) return;
			row.data('pickerActive', true);
			setTimeout(function(){row.data('pickerActive', false);}, 300);
			noggin.datePicker(row.data('date'), field.Type, $.proxy(self.setDateTimeValue, self, row));
		});
		var input = row.find('input');
		//wait for the clear button to exist (added by jquerymobile)
		//when it does, override the clear button behaviour to stop it refocusing on the date field
		var onload = setInterval(function(){
			var clear = row.find('.ui-input-clear');
			if (clear.length){
				clear.unbind('click').on('click', function(event){
					input
						.val( "" )
						.trigger( "change" );
					row.find('.ui-input-clear').addClass( "ui-input-clear-hidden" );
					event.preventDefault();
				});
				clearInterval(onload);
			}
		}, 500);
	} else {
		row.find('input').attr('data-clear-btn', 'false'); //ios/android date picker has a clear button built in
	}
	field.Input.change(function(e){
		if (e.isTrigger) return; //ignore change events triggered by app to work out readonly etc
		field.Input.data('hasChanged', true);
	});

    field.Input.getAPIValue = TypeEdit.getDateTimeAPIValue;
	return row;
};

/** define a special function to return date values in ISO format for API submission */
TypeEdit.getDateTime = function(){
	var val = this.val();
	if (!val) return val;

	if (OCALocale.get('DateTimeFormat') && OCALocale.get('DateTimeFormat').indexOf('%B') != -1){
		//if date format contains full months, try converting the date value
		val = ViewUtil.convertFullMonth(val);
	}

	var date = val.substring(0, 10);
	var time = val.substring(11);
	if (date.indexOf('/') !== -1){ //convert 01/01/2014 to 2014-01-01
		var bits = date.split('/');
		date = bits[2] + "-" + bits[1] + "-" + bits[0];
		if (OCALocale.selectLanguage() === 'en_US' && bits[0] <= 12){
			date = bits[2] + "-" + bits[0] + "-" + bits[1];
		}
	}
	if (!time) { //although a datetime field, certain default values may cause the time not to be set
		time = "00:00:00";
	} else if (OCALocale.get('DateTimeFormat') && OCALocale.get('DateTimeFormat').indexOf('%P') != -1){
		//if date format contains full months, try converting the date value
		time = ViewUtil.convertAMPMTime(time);
	}
	val = date + "T" + time;

	var off = new Date().getTimezoneOffset(); //minutes to UTC
	if (off < 0){ //offset negative means in front of UTC
		val += "+";
	} else {
		val += "-";
	}
	//convert minutes to HH:mm
	off = Math.abs(off);
	var hours = Math.floor(off / 60);
	if (hours < 10) hours = "0" + hours;
	var minutes = off % 60;
	if (minutes < 10) minutes = "0" + minutes;
	val += hours + ":" + minutes;

	var date = new Date(val);
	return date;
}

TypeEdit.getDateTimeAPIValue = function(){
	var date = TypeEdit.getDateTime.call(this);
	if (this.data('hasChanged') == false){				//if data has not been explicitly set AND the default value was to the date / time of submission,
		var initial = this.data('initialValue');		// send the default to the API rather than an ISO date string
		if (initial === 'now' || initial === 'today'){
			return initial;
		}
	}
	return date && date != 'Invalid Date' ? date.toISOString() : '';
}

TypeEdit.getDateAPIValue = function(){
	var date = TypeEdit.getDateTime.call(this);
	if (this.data('hasChanged') == false){				//if data has not been explicitly set AND the default value was to the date / time of submission,
		var initial = this.data('initialValue');		// send the default to the API rather than an ISO date string
		if (initial === 'now' || initial === 'today'){
			return initial;
		}
	}
	return date && date != 'Invalid Date' ? ViewUtil.dateConvert(date, '%Y-%m-%d') : '';
}

TypeEdit.prototype.datetimeoptRender = function(field, data){
	return this.datetimeRender(field, data);
};
/**
 * Render a datetime field for input.
 * @android Adds a click handler to load the noggin datepicker plugin for Android only
 */
TypeEdit.prototype.dateRender = function(field, data){
	var initialValue = data;
	var date;
	if (data === 'now' || data === 'today'){
		date = new Date();
	} else if(data && !isNaN(Date.parse(data))){
        date = new Date(data);
	}

	if (date){
		if (device.platform == "iOS" || device.platform == "Android" || device.platform == "Mobile Interface"){	//iOS and Android are using HTML5 date inputs
			data = ViewUtil.dateConvert(date, "%Y-%m-%d");				//requiring format according to http://www.w3.org/TR/html-markup/input.date.html#input.date.attrs.value
		} else {
			data = ViewUtil.displayDate(date);
		}
	}

	var row = this.fieldRender(field, data);
	row.data('date', date);
	field.Input.data('initialValue', initialValue);
	field.Input.data('hasChanged', false);
	var self = this;
	if (device.platform === "Win32NT"){
		row.on('click', function(event){
			if (event.target.tagName !== 'INPUT') return;	//dont fire on row select or the clear button
			if (row.data('pickerActive')) return;
			row.data('pickerActive', true);
			setTimeout(function(){ row.data('pickerActive', false); }, 300);
			noggin.datePicker(row.data('date'), 'date', $.proxy(self.setDateValue, self, row));
		});
	} else {
		row.find('input').attr('data-clear-btn', 'false'); //ios and android date picker has a clear button already
	}
	field.Input.change(function(e){
		if (e.isTrigger) return; //ignore change events triggered by app to work out readonly etc
		field.Input.data('hasChanged', true);
	});

	field.Input.getAPIValue = TypeEdit.getDateAPIValue;
	return row;
};
TypeEdit.prototype.subformRender = function(field, data){
    data = data || [];
    var row = TypeView.prototype.subformRender.call(this, field, data);
    var subContainer = row.find('div.subform');
    var add = $("<a href='#' data-role='button' data-inline='true' class='add' data-theme='b'>" + OCA.getI18n().gettext('Add row') + "</a>");
    add.click($.proxy(this.addSubformRow, this, add, field));
    subContainer.append(add);
    return row;
}
TypeEdit.prototype.addSubformRow = function($btn, field){
	var id = this.ID; 	//new subform rows should be treated like a create action (e.g. applying default values)
	this.ID = null;		// so clear the ID and they will be treated as a new object
    var $subform = this.createSubformRow(field);
	this.ID = id;		//restore once the new row has been created
    $btn.before($subform);
    this.listview.enhanceWithin();
    this.content.trigger('rendered');
}

TypeEdit.prototype.createSubformRow = function(field, data){
    var index = field.SubFieldInputs.length;
    var listBackup = this.nestedLists; //separate main nested lists from sub lists
    this.nestedLists = [];
    var $container = TypeView.prototype.createSubformRow.call(this, field, data);

    var $del = $("<a href='#' class='delete'>" + ViewUtil.ocaicon('close2') + "</a>");
    $container.prepend($del);
    $del.trigger('create');
    $del.click($.proxy(this.removeSubformRow, this, $container, field, index));

    var $subLV = $container.find('ul.subform-row');
    TypeEdit.prototype.addNestedLists.call({nestedLists: this.nestedLists, listview: $subLV});
    this.nestedLists = listBackup;
    return $container;
}

TypeEdit.prototype.removeSubformRow = function($row, field, index){
    $row.remove();
    delete field.SubFieldInputs[index];
}


TypeEdit.prototype.fileuploadRender = function(field, data){
    if (!field.ShowCanvas || field.ShowCanvas == '0') {
		if (OCA.versionAtLeast('1.7.0')) {
			field.Input = new FileInput(this, field, data).render();
			return field.Input.$row;
		} else {
			return; //file upload fields depend on OCA Server 1.7.0 API changes
		}
	} else {
		var input = $("<canvas></canvas>")
			.prop("name", field.Label.toLowerCase())
			.prop("id",   field.Label.toLowerCase())
			.addClass('fileupload ui-canvas field-' + field.ID);

		var row = $("<li class='ui-field-contain ui-li-static fileupload field' />")
			.append('<div class="scroll-protection"></div>')
			.append($("<label />").prop("for", field.Label.toLowerCase()).text(field.Label))
			.append(input);

		//there's a bug on iOS 7 where editing the canvas will cause the clear button to vanish. I don't know why
		//please don't ask me why this works, but it does. A dummy button is addded and hidden
		row.append("<a href='#' data-role='button' data-inline='true' class='dummy' data-theme='b' style='display:none;'>Dummy</a>");

		var btns = $("<div class='canvasButtons'><a href='#' data-role='button' data-inline='true' class='clear' data-theme='b'>Clear</a></div>");
		var revert = $("<a href='#' data-role='button' data-inline='true' class='revert' data-theme='b'>Revert</a>").hide();
		btns.on('click', 'a.clear', function(){
			var sketch = input.data('sketch');
			sketch.reset();
			row.find('img').hide(); //remove any images and make sure the canvas is shown
			input.show();
			revert.show();
		});
		row.append(btns);

		var initialValue = null;
		if (data && data.dataURI){
			//if existing data, show an image instead of the canvas
			btns.before('<img src="' + data.dataURI + '">');
			input.hide();

			initialValue = data.dataURI;

			btns.on('click', 'a.revert', function(){
				var sketch = input.data('sketch');
				sketch.val(initialValue);
				row.find('img').show(); //show image, hide canvas
				input.hide();
				revert.hide();
			});
			btns.append(revert);
		}


		this.listview.append(row);
		input.sketch({defaultSize: 2, initialValue: initialValue});
		field.Input = input.data('sketch');
		field.InitialValue = initialValue;
		field.Input.getAPIValue = function(){
			var dataURI = this.val();

			if (dataURI){
				if (dataURI == initialValue){
					return data; //maintaining existing data
				} else {
					return {
						dataURI: dataURI, //data is the base64 val of the canvas
						name: field.Label
					};
				}
			}
			if (!dataURI) return null;
		}
		field.Input.prop = function(key, value){
			if (key == 'disabled') {
				row.toggleClass(key, value);
			} else {
				row.prop.apply(this, arguments);
			}
		}
		field.Input.setReadOnly = function(value){
			row.toggleClass('disabled', value);
		}
		field.Input.change = function(){
			this.change.apply(this, arguments);
		}.bind(field.Input.canvas);
		var val = field.Input.val;
		field.Input.val = function(value){
			if (value !== undefined) {
				if (value.dataURI){ //array format, extract only the dataURI
					value = value.dataURI;
				}
				//only send the value if it's a valid dataURI
				//this is defensive programming against bad config
				//if we ever properly support setting signature fields via default value this would also need to show
				// the preview image and revert button if not already present
				if (value.substr(0, 21) == 'data:image/png;base64'){
					return val.call(this, value);
				}
			} else {
				return val.call(this, value);
			}
		}

		return row;
	}
}

TypeEdit.prototype.outcomeRender = function(){}
/** derived fields can't be edited or calculated on the mobile side */
TypeEdit.prototype.derivedfieldRender = function(field, data){
    var row = this.fieldRender(field, data);
    field.Input.setReadOnly(true);

    this.derivedIDs.push(field.ID);
    return row;
}
TypeEdit.prototype.datediffRender = function(field, data){
    var row = this.fieldRender(field, data);
    field.Input.prop('disabled', true);

    this.datediffIDs.push(field.ID);
    return row;
}
/** chart fields can't be edited */
TypeEdit.prototype.chartRender = function(){}

/**
 * Success callback from the android date picker plugin
 * Updates the date field value from the given parameters
 * @param {JQuery} row
 * @param {date} date
 */
TypeEdit.prototype.setDateValue = function(row, date){
	row.data('date', date);
	row.data('pickerActive', true);		//mark the picker as active to stop it being relaunched
	setTimeout(function(){row.data('pickerActive', false)}, 300);		//but only temporarily
	row.find('input').val(date.toLocaleDateString()).change().blur();
}
/**
 * Success callback from the wp8 date picker plugin
 * Updates the datetime field value from the given parameters
 * @param {JQuery} row
 * @param {date} date
 */
TypeEdit.prototype.setDateTimeValue = function(row, date){
	row.data('date', date);
	row.data('pickerActive', true);		//mark the picker as active to stop it being relaunched
	setTimeout(function(){row.data('pickerActive', false)}, 300);		//but only temporarily
	row.find('input').val(this.datetimeFormat(date, true)).change().blur();
}
/**
 * Submits the form data after it calculates the delta of the form - i.e. only submits fields which have changed value
 */
TypeEdit.prototype.submit = function(){
	var submission = this.getSubmission();

	if (!submission) {
		if (this.processed) return;
		this.processed = true;
		util.goBack();
	} else if (this.valid()) {
		this.submission(submission);
	}
};

TypeEdit.prototype.getSubmission = function(getAll){
    getAll = getAll || false;
	var submission = {FieldData: {}};
	var cleanupFiles = [];
	var submit = false, field = null;
	for (var id in this.typeData.Fields){
		field = this.typeData.Fields[id];
		if (field.Input && (this.hasChanged(field) || getAll)) {
			submission.FieldData[id] = field.Input.val();
            if (field.SequenceValue){
                submission.FieldData[id] = {
					prefix: field.SequenceValue,
                    value: submission.FieldData[id]
                };
            }
            if (field.Input.getAPIValue){ //overwrite the val() output if there's a specialised function to get the submission value
                submission.FieldData[id] = field.Input.getAPIValue();
            }
            if (field.Input.getFilesToClean) {
				cleanupFiles = cleanupFiles.concat(field.Input.getFilesToClean());
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
	if (cleanupFiles.length){
		submission.CleanupFiles = cleanupFiles;
	}
	return submit ? submission : null;
}

TypeEdit.prototype.getContext = function(){
	var context = {
		SubjectTypeURL: Configuration.getAPIPath() + this.typeEndpoint + '/' + this.typeID,
		SubjectURL: this.ID
			? Configuration.getAPIPath() + this.endpoint + this.ID
			: null
	}

	if (this.data && this.data.Geometry && this.data.Geometry.data){
		context.Geometry = this.data.Geometry.data;
	}
	var submission = this.getSubmission(true);
	context.Data = submission.FieldData ? submission.FieldData : submission;

	return context;
}
/**
 * Performs client side validation on the submitted form.
 * Currently checks:
 * - Required fields are filled in
 */
TypeEdit.prototype.valid = function(){
	var valid = true;
	var errors = [];

    var fieldValid = function(field, input){
        var visible = true;
        if (input){ //input is explicitly passed in for subforms, because the correct input for this row has to be chosen
			if (input.is) {
				visible = input.is(':visible');
			} else {
				visible = field.$row && field.$row.is(':visible');
			}
        } else {
            visible = field.$row && field.$row.is(':visible');
            input = field.Input; //for all other field types, the input is accessible from the main field object
        }

        if ((field.Required && !field.Readonly) && visible && input && input.val){
            var val = input.val() || field.SequenceValue; //if no value set, fall back to the sequence value which might be there.
            if (!val || JSON.stringify(val) === JSON.stringify([]) || JSON.stringify(val) === JSON.stringify({})){
                return false;
            }
        }
        return true;
    }
    var geomvalid = true;
    if (this.typeData.RequiredMapping) {
    	geomvalid = false;
    }
    if (this.typeData.Geometry && this.typeData.Geometry.Input.data && this.typeData.Geometry.Input.data.WKT){
    	geomvalid = true;
    }

	for (var id in this.typeData.Fields){
		var field = this.typeData.Fields[id];
		if (!field.Input) {
			continue; //skip fields with no input
		}
		var val = field.Input.val();
		if (field.Type == 'location'){
			if (val && val.IsTiedMarker){
				geomvalid = true;
			}
		} else if ((field.ContributeGeo) && (parseInt(field.ContributeGeo) == 1) && val && val.length){
			geomvalid = true;
		}
        if (field.Type == 'subform'){
            for (var row in field.SubFieldInputs){
                for (var subID in field.SubFields){
                    var subfield = field.SubFields[subID];
                    var input = field.SubFieldInputs[row][subID];
					if (!input) continue; //e.g. file upload fields on old OCAs

					val = input.val();
                    if (subfield.Type == 'location'){
                    	//sub-location-fields do not contribute geometry 
                    } else if (subfield.ContributeGeo && (parseInt(subfield.ContributeGeo) == 1) && val && val.length){
                    	geomvalid = true; //it might not be valid.. but can't know without the backend call -- needs to check if the selected objects have geometry
                    }
                    if (!fieldValid(subfield,input)){
                        valid = false;
                        errors.push(subfield.Label + " (" + field.Label + " row " + (parseInt(row,10) + 1) + ")");
                    }
                }
            }
        } else if (!fieldValid(field)){
            valid = false;
            errors.push(field.Label);
		}
	}
	if (!geomvalid){
		valid  = false;
		errors.push(OCA.getI18n().gettext("<br />Mapping geometry is required for this " + this.typelabel + " type"));
	}
	if (!valid){
		util.alertDialog(OCA.getI18n().translate("Required fields are not filled in: %s").fetch(errors.join(", ")), $.noop, OCA.getI18n().gettext("Validation error"));
		app.checkLoaded();
	}
	return valid;
}
/**
 * Sends form submission to the server
 */
TypeEdit.prototype.submission = function(submission){
	if (this.submitted) return;
	this.submitted = true;
	var desc = "Edited " + (this.data.FullName || this.data.Name || this.type);
	new Gopher({url:this.endpoint + this.ID, data:submission, desc: desc, typeURL: this.data.TypeURL}, function(){
		util.goBack();
	}, $.proxy(this.dataError, this)).put();

	if (submission.Attachments) {
		this.addRelatedDocuments(submission.Attachments);
	}
	if (submission.Detachments){
		this.removeRelatedDocuments(submission.Detachments);
	}
}
/**
 * Sends files to the /related/documents endpoint for this object
 * @param {object} files object with file URIs as keys and file names as values
 * @param {string} [url] defaults to /type/id/related/documents but may be overridden
 */
TypeEdit.prototype.addRelatedDocuments = function(files, url){
	url = url || this.endpoint + this.ID;
	url += '/related/documents';
	for (var file in files){
		new Gopher({
			url: url,
			data: file,
			backgroundMode: true
		}, $.proxy(fileStore.clearFiles, fileStore, [file])).uploadFile();
	}
}

TypeEdit.prototype.removeRelatedDocuments = function(documents){
	for (var url in documents){
		new Gopher(url).sendDelete();
	}
}
/**
 * Delta comparison function to check if a field's value has changed.
 * Values are compared simply for equality, and also via converting the current and initial values to stringified JSON to test object or array equality
 */
TypeEdit.prototype.hasChanged = function(field){
	if (field.InitialValue == null) field.InitialValue = '';
	if (!field.Input) return false;

	var current = field.Input.val();
	if (current == null) current = '';
	if (current == field.InitialValue){
		return false;
	}
	if ((field.Type == "richtext") && (current.trim() == field.InitialValue.trim())){
		return false;
	}

	//test for object/array equality
	if (JSON.stringify(current) == JSON.stringify(field.InitialValue)) return false;

	return true;
}
/**
 * failure callback for form submission.
 * Response handling is covered by the Gopher class, this just marks the form as unsubmitted so that it may be retried
 */
TypeEdit.prototype.dataError = function(){
	this.submitted = false;
	console.log('dataError', arguments);
}

TypeEdit.prototype.attachAfterSubmit = function(attachments, responsePayloads, data, createdURL){
	var back = -1;
	if (createdURL) {
		this.ID = createdURL.split("/").pop();
		this.addRelatedDocuments(attachments);
		if (this.timestamp){ //save after a validation fix. Go back extra levels to avoid any pending routes
			back += this.deleteLevels;
		}
	}
	util.goBack(back);
}
/**
 * For internal display purposes, this function evaluates the type data and current data to determine a name or label
 */
TypeEdit.prototype.getName = function(){
	if (!this.typeData || !this.typeData.Fields) return '';

	var knownDefines = ['NAME', 'TITLE']; //list of define symbols used across types to determine the name
	for (var fID in this.typeData.Fields){
		var field = this.typeData.Fields[fID];
		if (knownDefines.indexOf(field.Define) !== -1 && field.Input && field.Input.val() && field.Input.val() !== '(auto)') {
			return field.Input.val();
		}
	}

	//fall back to the data from the server - if there is any (checking after defines so that current edits can take priority)
	if (this.data && this.ID){
		var name = this.data.Name || this.data.FullName;
		if (name) return name;
	}

	//failing that, look for text fields used in summaries or with likely-sounding labels
	var labelGuesses = ['Name', 'Label'];
	for (var fID in this.typeData.Fields){
		var field = this.typeData.Fields[fID];
		if (field.Type != 'sgltxt') continue;

		if ((labelGuesses.indexOf(field.Label) !== -1 || field.ShowInSummary != '0') && field.Input && field.Input.val() && field.Input.val() !== '(auto)') {
			return field.Input.val();
		}
	}

	//failing that, give the type name
	return this.typeData.Name;
}