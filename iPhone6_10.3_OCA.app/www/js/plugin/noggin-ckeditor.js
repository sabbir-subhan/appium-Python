function CKEditorInput(field, value){
	jQueryInterface.call(this, field, value);
	this.ready = false;
	this.config = {
		allowedContent: true, 					//TODO reduce this to only the content that can be set by the OCA Server ckeditor
		disallowedContent: 'script; *[on*]',	//... but for the time being, this provides some security
		coreStyles_strike: {element: 'strike', overrides: 's'},
		disableNativeSpellChecker: false,
		disableObjectResizing: true,
		extraPlugins: 'maximize',
		font_defaultLabel: 'Arial',
		protectedSource: [/<style[\s\S]*?>[\s\S]*?<\/style>/gi],
		removePlugins: 'about',
		resizeEnabled: false,
		skin: 'moono',
		toolbar: [
			['Bold', 'Italic', 'Underline'],
			['BulletedList', 'NumberedList']
		],
		removeButtons: 'link',
		contentsCss: 'css/richtext.css'
	};

	if (device.platform != 'iOS'){
		this.config.toolbar.push(['Maximize']); //add maximise button for platforms that support it.
	}

	if (field.Readonly){
		this.config.readOnly = true;
	}
}

CKEditorInput.prototype             = new jQueryInterface;
CKEditorInput.prototype.constructor = CKEditorInput;

CKEditorInput.prototype.enhance = function(textarea){
	this.editor = CKEDITOR.replace(textarea, this.config);
	this.editor.on('instanceReady', function() {
		this.isReady = true;
		this.field.InitialValue = this.val(); //ckeditor strips whitespace, so make sure our initial value matches the exact output format
		ViewUtil.loadMediaForRichContent(this.editor.document.$);
		if (this.field.Readonly) this.editor.setReadOnly(true);

		//deal with iOS problems when the editor is active and the app does a page navigation - can result in odd screen dimension calculations and the header bar being misplaced
		var $page = $(this.editor.container.$).parents('.ui-page');

		$(document).on('pagebeforechange', function(){
			this.focusManager.blur(true);				//try the ckeditor blur method
			$page.find('input').first().focus().blur(); //find a different input, and change focus to it, then instantly blur to hide the keyboard and restore the screen
		}.bind(this.editor));
		this.editor.on('blur', function(){
			$('#header').css('position', '');
		})
		this.editor.on('focus', function(){
			$('#header').css('position', 'relative');
		})
		$page.find('input, select, textarea').on('focus', function(){
			$('#header').css('position', '');
			this.focusManager.blur(true);
		}.bind(this.editor));

		//fire change at most every 15 seconds
		var lastChange = (new Date() / 1000) - 15;
		this.editor.on('change', function(){
			var now = new Date() / 1000;
			if (now - lastChange > 15){
				this.change();
				lastChange = now;
			}
		}.bind(this));
	}.bind(this));

	// this.editor.on('dialogShow', function(){
	// 	document.addEventListener("backbutton", this.closeCurrentDialog);
	// }.bind(this));
	// this.editor.on('dialogHide', function(){
	// 	document.removeEventListener("backbutton", this.closeCurrentDialog);
	// }.bind(this));
	//
	// if (device.platform != "iOS") {
	// 	this.editor.on('focus', function () {
	// 		this.editor.execCommand('maximize');
	// 	}.bind(this));
	// 	document.addEventListener('backbutton', this.minimize.bind(this));
	// }
};

CKEditorInput.prototype.val = function(value){
	if (value !== undefined){
		if (this.isReady){
			var self = this;
			this.editor.setData(value, {callback: function(){
				ViewUtil.loadMediaForRichContent(self.editor.document.$);
			}});
		} else {
			this.editor.on('instanceReady', $.proxy(this.val, this, value));
		}
	} else {
		if (this.isReady){
			return this.editor.getData();
		} else {
			return this.value;
		}
	}
};

CKEditorInput.prototype.prop = function(prop, value){
	if (prop == 'disabled' && this.isReady){
		this.editor.setReadOnly(value);
	}
};
CKEditorInput.prototype.setReadOnly = function(readonly){
	this.field.$row.toggleClass('ckreadonly', !!readonly);
	if (this.isReady){
		this.editor.setReadOnly(readonly);
	} else {
		this.field.Readonly = true;
	}
};

/**
 * Destroy this input instance
 */
CKEditorInput.prototype.kill = function(){
	if (this.editor){
		this.editor.removeAllListeners();
		CKEDITOR.remove(this.editor);
	}
}

// CKEditorInput.prototype.closeCurrentDialog = function(){
// 	var currentDialog = CKEDITOR.dialog.getCurrent();
// 	if (currentDialog != null){
// 		currentDialog.hide();
// 	}
// };
//
// CKEditorInput.prototype.minimize = function(){
// 	var command = this.editor.getCommand( 'maximize' );
// 	if (command && command.state == CKEDITOR.TRISTATE_ON){ 	//back button pressed and the editor is currently maximised.
// 		this.editor.execCommand('maximize');				//trigger maximize to minimize
// 	}
// }
//when images in mobile are swapped out the original src stored in data-apisrc -- swap it back when getting val.
// CKEditorInput.prototype.val                = function(){
// 	var data = this.editor.getData();
// 	var parsed = ViewUtil.parseHTML(data);
// 	$(parsed).find('img[data-apisrc]').each(function(){
//     	$(this).attr('src',$(this).attr('data-apisrc'));
//     	$(this).removeAttr('data-apisrc');
//     });
//     var output = ViewUtil.parsedToXhtml(parsed);
// 	return output;
// }
//annoyingly ckeditor setData is async - 
// CKEditorInput.prototype.setValue           = function(data, callback){
// 	//after setting ckeditor value run autogrow - and if callback supplied, run it also.
// 	var options = {
// 		callback: function(){
// 			// this.autogrow();
// 			if (typeof callback == 'function'){
// 				callback();
// 			}
// 		}.bind(this)
// 	}
// 	var setDataFunc = function(html){
// 		// if ckeditor not ready.. wait until ready then set data and run callback
// 		if (this.isReady){
// 			this.editor.setData(html,options);
// 		} else {
// 			this.editor.on('instanceReady',function(){
// 				this.editor.setData(html,options);
// 			}.bind(this));
// 		}
// 	}
// 	//only swap images on mobile device (not interface) - and no need if data is empty
// 	if ((data != null) && (data != '') && (device.platform != "Mobile Interface")){
//
// 		ViewUtil.swapImages.call(this, data, function(html){
//     		setDataFunc.call(this,html);
//
//     	}.bind(this));
// 	} else {
// 		setDataFunc.call(this,data);
//
// 	}
// }

// CKEditorInput.prototype.autogrow = function(){
// 	this.editor.commands.autogrow.exec();
// }
// //removing max height.. ckeditor should grow as long as it needs.. but kept line commented out in case needs to be reverted.
// CKEditorInput.prototype.autoGrow = function(current){
// 	if (current && current.data && current.data.currentHeight && current.data.newHeight) {
// 		//this.editor.container.$.lastChild.lastChild.style.height = Math.min(this.maxheight, Math.max(current.data.newHeight + this.autoGrow_buffer,this.minheight)) + 'px';
// 		this.editor.container.$.lastChild.lastChild.style.height = Math.max(current.data.newHeight + this.autoGrow_buffer,this.minheight) + 'px';
// 	}
// }

// CKEditorInput.prototype.loadplugins = function(){
// 	if (OCA.ckeditorpluginsloaded) return;
//
// 	OCA.ckeditorpluginsloaded = true;
//
// 	CKEDITOR.plugins.add('ocareplacement',
// 	{
// 		 editcounter:1 //start 1 based to avoid 0 == false errors
// 		,editreps:{}
//
// 		,init : function( editor ){
//
// 			if (editor.config.OCAReplacement && (editor.config.OCAReplacement.list || editor.config.allowOCAReplacement)){
// 				//var menu = new NG.ContextMenu(this.buildReplacementMenu(editor,editor.config.OCAReplacement.list));
// 				editor.addCommand('ocareplacement',{
// 					modes: {wysiwyg:1,source:0}
// 					,exec: function(editor){
// 						if (editor.readOnly) return;
// 						var button = document.getElementById(this.uiItems[0]._.id);
// 						var pos = NG.getPagePos(button);
// 						menu.show(pos.x,pos.y+20);
// 					}
// 				});
//
// 				editor.ui.add('OCAReplacement',CKEDITOR.UI_BUTTON,{
// 					label:'Insert'
// 					,icon:false
// 					,command:'ocareplacement'
// 					,className:'ngcke_textbutton'
// 				});
//
// 				var tbar = editor.config['toolbar_' + editor.config.toolbar];
// 				tbar.push(['OCAReplacement']);
// 			}
//
// 			editor.on(
// 				 'mode'
// 				,function(){
// 					if (this.document) {
// 						var spans = this.document.find('span[ng_replacement]');
// 						for (var i = 0; i < spans.count(); i++) {
// 							var span = spans.getItem(i);
// 							//span.on('dblclick',this.plugins.ocareplacement.editItem,this,span);
// 						}
// 					}
// 				}
// 				,editor
// 			);
// 		}
//
// 		,rawAttribute: function(value) {
// 			var list = [
// 				'&','&amp;', //MUST be first
// 				'<','&lt;',
// 				'>','&gt;',
// 				'"','&quot;',
// 				"'",'&apos;'
// 			];
//
// 			for (var i = 0; i < list.length; i+=2) {
//
// 				from = new RegExp(list[i+1],'gi');
// 				to = list[i];
//
// 				value = value.replace(from,to);
//
// 			}
//
// 			return value;
// 		}
// 		,afterInit : function(editor){
// 			// Register a filter to displaying placeholders after mode change.
//
// 			var dataProcessor = editor.dataProcessor,
// 				dataFilter = dataProcessor && dataProcessor.dataFilter,
// 				htmlFilter = dataProcessor && dataProcessor.htmlFilter;
//
// 			if ( dataFilter ){
// 				dataFilter.addRules({
// 					text:function(text){
// 						text = text.replace(/(%|\$|@|#)\{((?:\\\\|\\\}|[^\}])+)\}/g,function(whole,prefix,field_and_label){
// 							var field = '',
// 								label = '',
// 								replacementClass = 'ocareplacement';
//
// 							var res = field_and_label.match(/^((?:\\\\|\\\:|[^:])+):?(.*)$/);
//
// 							if (! res){
// 								return field_and_label;
// 							}
//
// 							field = CKEDITOR.plugins.get('ocareplacement').rawAttribute(res[1]);
// 							label = CKEDITOR.plugins.get('ocareplacement').rawAttribute(res[2]);
//
// 							if (! label){
// 								label = field;
// 							}
//
// 							field = CKEDITOR.plugins.get('ocareplacement').unescapeString(field);
// 							label = CKEDITOR.plugins.get('ocareplacement').unescapeString(label);
//
// 							if (prefix === '$') {
// 								replacementClass += ' green';
// 							} else if (prefix === '@') {
// 								replacementClass += ' orange';
// 							} else if (prefix === '#') {
// 								replacementClass += ' purple';
// 							}
//
// 							//Create an element to entitise
// 							var div = document.createElement('div');
// 							var span = document.createElement('span');
// 							span.setAttribute('data-label',label);
// 							span.setAttribute('class',replacementClass);
// 							span.setAttribute('ng_prefix',prefix);
// 							span.setAttribute('ng_replacement',field);
// 							span.setAttribute('contentEditable',false);
// 							span.setAttribute('title',label);
// 							span.appendChild(document.createTextNode(label));
// 							div.appendChild(span);
// 							return div.innerHTML;
//
// 						});
// 						return text;
// 					}
// 				},{applyToAll:true}); //Otherwise they are not applyed to items with contentEditable set to false
// 			}
//
// 			if (htmlFilter){
// 				htmlFilter.addRules({
// 					elements:{
// 						'span': function (element) {
// 							if (element.children.length > 1) return element;
// 							if (element.attributes.ng_prefix || element.attributes.ng_replacement){
// 								var prefix = element.attributes.ng_prefix || '%';
// 								var replacement = CKEDITOR.plugins.get('ocareplacement').rawAttribute(element.attributes.ng_replacement);
// 								var label  = CKEDITOR.plugins.get('ocareplacement').rawAttribute(element.attributes['data-label']) || replacement;
//
// 								label = CKEDITOR.plugins.get('ocareplacement').escapeString(label.trim());
// 								replacement = CKEDITOR.plugins.get('ocareplacement').escapeString(replacement);
//
// 								//The space is important to for the regex
// 								var ret = new CKEDITOR.htmlParser.text(prefix + '{' + replacement + ':' + label + ' }');
// 							 	element.replaceWith(ret);
// 							}
// 							return element;
// 						}
// 					}
// 				},{applyToAll:true}); //Otherwise they are not applied to items with contentEditable set to false
// 			}
// 		}
// 		,insertReplacement : function(editor,el){
// 			var prefix = el.prefix,
// 				colour = el.colour,
// 				label = el.label,
// 				field = el.field,
// 				replaceid = el.replaceid,
// 				replacementClass = 'ocareplacement',
// 				replacementElement;
//
// 			if (prefix === undefined || prefix === null) prefix = '%';
//
// 			if (colour) replacementClass += ' ' + colour;
//
// 			field = CKEDITOR.plugins.get('ocareplacement').unescapeString(field);
// 			label = CKEDITOR.plugins.get('ocareplacement').unescapeString(label);
//
// 			if (field == 'block') {
// 				prefix = '@';
// 				replacementClass = 'ocareplacement orange';
// 				var blockid = 'BLOCK-'+Math.random().toString(36).substr(2, 9);
// 				var blockcounter = 1;
// 				for (var i = 0; i < editor.document.$.body.getElementsByTagName('span').length; i++){
// 					var element = editor.document.$.body.getElementsByTagName('span')[i];
// 					var regex = /BEGIN(\d+)/;
// 					var match = regex.exec(element.getAttribute('data-label'));
// 					if (match && match[1]) {
// 						if (match[1] >= blockcounter) {
// 							blockcounter = ++match[1];
// 						}
// 					}
// 				}
// 				label = 'BEGIN';
// 				beginElement = editor.document.createElement('p');
// 				beginSpan = editor.document.createElement('span');
// 				beginSpan.setAttribute('ng_replacement', blockid);
// 				beginSpan.setAttribute('ng_prefix', prefix);
// 				beginSpan.setAttribute('class', replacementClass);
// 				beginSpan.setAttribute('contentEditable', 'false');
// 				beginSpan.setAttribute('title', blockid+': '+label);
// 				beginSpan.setAttribute('data-label', label+blockcounter);
// 				beginSpan.setHtml(label+blockcounter);
// 				beginElement.append(beginSpan);
//
// 				paragraphElement = editor.document.createElement('p');
// 				paragraphElement.setHtml('&nbsp;');
//
// 				label = 'END';
// 				endElement = editor.document.createElement('p');
// 				endSpan = editor.document.createElement('span');
// 				endSpan.setAttribute('ng_replacement', blockid);
// 				endSpan.setAttribute('ng_prefix', prefix);
// 				endSpan.setAttribute('class', replacementClass);
// 				endSpan.setAttribute('contentEditable', 'false');
// 				endSpan.setAttribute('title', blockid+': '+label);
// 				endSpan.setAttribute('data-label', label+blockcounter);
// 				endSpan.setHtml(label+blockcounter);
// 				endElement.append(endSpan);
//
// 				var plaintext = el.plaintext;
//
// 				var range = editor.getSelection().getRanges();
// 				if (range.length == 0) {
// 					alert('Cannot insert replacement block');
// 					return;
// 				}
// 				var boundary = range[0].getBoundaryNodes();
// 				var ss = boundary.startNode;
//
// 				// Note: Some browsers return multiple ranges even for a continuous selection.
// 				// Firefox, for example, returns one range for each table cell when one or more table rows are selected.
// 				boundary = range[range.length-1].getBoundaryNodes();
// 				var se = boundary.endNode;
//
// 				var ssp = ss.getParent();
// 				if (ssp instanceof CKEDITOR.dom.element && (ssp.getName() == 'head' || ssp.getName() == 'html')) {
// 					// Block markers will be in the head in this case;
// 					alert('Cannot insert replacement block');
// 					return;
// 				}
//
// 				//if (!plaintext) {
// 					if (ss instanceof CKEDITOR.dom.text || ss.getName() == 'br' || ss.getName() == 'td' || ss.getName() == 'span') {
// 						ss = ss.getParent();
// 						if (ss.getName() == 'td') {
// 							ss = ss.getParent();
// 						}
// 					}
// 				//}
// 				//if (!plaintext) {
// 					if (se instanceof CKEDITOR.dom.text || se.getName() == 'br' || se.getName() == 'td' || se.getName() == 'span') {
// 						se = se.getParent();
// 						if (se.getName() == 'td') {
// 							se = se.getParent();
// 						}
// 					}
// 				//}
//
// 				if (ss instanceof CKEDITOR.dom.element && ss.getName() == 'tr') {
// 					var table1 = ss.getParent().getParent(); // tbody > table
// 					var table2 = se.getParent().getParent(); // tbody > table or td > tr
// 					if (table2.getName() == 'tr') {
// 						se = table2; // tr
// 						table2 = se.getParent().getParent(); // tbody > table
// 					}
// 					if (table1.$ !== table2.$) {
// 						alert('Cannot insert replacement block');
// 						return;
// 					}
// 				}
// 				if (se instanceof CKEDITOR.dom.element && se.getName() == 'tr') {
// 					var table1 = ss.getParent().getParent(); // tbody > table or td > tr
// 					var table2 = se.getParent().getParent(); // tbody > table
// 					if (table1.getName() == 'tr') {
// 						ss = table1; // tr
// 						table1 = ss.getParent().getParent(); // tbody > table
// 					}
// 					if (table1.$ !== table2.$) {
// 						alert('Cannot insert replacement block');
// 						return;
// 					}
// 				}
//
// 				// A collapsed range has its start and end boundaries at the very same point so nothing is contained in it
// 				if (range.collapsed) {
// 					editor.insertElement(beginElement);
// 					paragraphElement.insertAfter(beginElement);
// 					endElement.insertAfter(paragraphElement);
// 				} else {
// 					if (ss instanceof CKEDITOR.dom.element && se instanceof CKEDITOR.dom.element && ss.getName() == 'tr' && se.getName() == 'tr') {
// 						beginTR = editor.document.createElement('tr');
// 						var cell = editor.document.createElement('td');
// 						cell.$.colSpan = ss.$.cells.length;
// 						cell.append(beginElement);
// 						beginTR.append(cell);
// 						beginTR.insertBefore(ss);
// 						endTR = editor.document.createElement('tr');
// 						cell = editor.document.createElement('td');
// 						cell.$.colSpan = se.$.cells.length;
// 						cell.append(endElement);;
// 						endTR.append(cell);
// 						endTR.insertAfter(se);
// 					} else {
// 						beginElement.insertBefore(ss);
// 						// Add breaks before and after the selections in plain text box
// 						if (ss instanceof CKEDITOR.dom.element && ss.getName() == 'span' || ss instanceof CKEDITOR.dom.text) {
// 							editor.document.createElement('br').insertBefore(ss);
// 						}
// 						endElement.insertAfter(se);
// 						if (se instanceof CKEDITOR.dom.element && se.getName() == 'span' || se instanceof CKEDITOR.dom.text) {
// 							editor.document.createElement('br').insertAfter(se);
// 						}
// 					}
// 				}
// 			}  else {
// 				replacementElement = editor.document.createElement('span');
// 				replacementElement.setAttribute('ng_replacement', field);
// 				replacementElement.setAttribute('ng_prefix', prefix);
// 				replacementElement.setAttribute('class', replacementClass);
// 				replacementElement.setAttribute('contentEditable', 'false');
// 				replacementElement.setAttribute('title',label);
// 				replacementElement.setAttribute('data-label', label);
// 				replacementElement.setHtml(label);
//
// 				var editspan = null;
// 				if (replaceid !== undefined) {
//
// 					if (editor.plugins.ocareplacement.editreps[replaceid]) {
// 						editspan = editor.plugins.ocareplacement.editreps[replaceid];
// 					}
//
// 				}
//
// 				if (editspan) {
// 					replacementElement.replace(editspan);
// 				} else {
// 					editor.insertElement(replacementElement);
// 				}
//
// 				replacementElement.on('dblclick',editor.plugins.ocareplacement.editItem,editor,replacementElement);
// 			}
// 		}
// 		,escapeString : function(string){
//
// 			var newstring = string;
//
// 			newstring = newstring.replace(/\\/g,'\\\\');
// 			newstring = newstring.replace(/:/g,'\\\:');
// 			newstring = newstring.replace(/}/g,'\\\}');
//
// 			return newstring;
//
// 		}
// 		,unescapeString : function(string){
//
// 			var newstring = string;
//
// 			newstring = newstring.replace(/\\\:/g,':');
// 			newstring = newstring.replace(/\\\}/g,'}');
// 			newstring = newstring.replace(/\\\\/g,'\\');
//
// 			return newstring;
//
// 		}
//
// 	});
//
//
// 	CKEDITOR.plugins.add('ocablock',{
// 		init:function(editor){
//
// 			var cf = function(t,editor){
// 				if (editor.readOnly) return;
// 				var style = new CKEDITOR.style({element:t});
// 				style.type = CKEDITOR.STYLE_BLOCK;
// 				style.apply(editor.document);
// 			}
//
// 			//TODO - Buttons are not "greyed" out when the editor is disabled
// 			editor.ui.add('Heading1',CKEDITOR.UI_BUTTON,{
// 				label:'Heading 1'
// 				,click:cf.bind(editor,'h1')
// 				,className:'ocacke_heading1'
// 			});
//
// 			editor.ui.add('Heading2',CKEDITOR.UI_BUTTON,{
// 				label:'Heading 2'
// 				,click:cf.bind(editor,'h2')
// 				,className:'ocacke_heading2'
// 			});
//
// 			editor.ui.add('Heading3',CKEDITOR.UI_BUTTON,{
// 				label:'Heading 3'
// 				,click:cf.bind(editor,'h3')
// 				,className:'ocacke_heading3'
// 			});
//
// 			editor.ui.add('Pre',CKEDITOR.UI_BUTTON,{
// 				label:'Fixed width'
// 				,click:cf.bind(editor,'pre')
// 				,className:'ocacke_pre'
// 			});
//
// 			editor.ui.add('Paragraph',CKEDITOR.UI_BUTTON,{
// 				label:'Paragraph'
// 				,click:cf.bind(editor,'p')
// 				,className:'ocacke_paragraph'
// 			});
// 		}
// 	});
// 	CKEDITOR.plugins.add('ocanotes',
// 	{
// 		requires: 'widget',
// 		icons:false,
// 		label:'Footnote/Endnote',
// 		init: function(editor){
//
// 			editor.widgets.add('ocanotes', {
// 				allowedContent:'span[ngendnote,ngfootnote]',
// 				button:OCA.getI18n().gettext('Add footnote / endnote'),
// 				data: function(){
//
// 					switch (this.data.type){
// 						case 'ngfootnote':
// 							this.element.removeAttribute('ngendnote');
// 							break;
// 						case 'ngendnote':
// 							this.element.removeAttribute('ngfootnote');
// 							break;
// 					}
//
// 					this.element.setAttribute(this.data.type,'<p>' + this.specialChars(this.data.note,true) + '</p>');
// 					this.setTitle();
// 				}
// 				,dialog:'ocanotes'
// 				,draggable: false //Should be allowed, but causes bugs so disable for now
// 				,init: function(){
//
// 					if (! this.data.type){
// 						if (this.element.hasAttribute('ngendnote')){
// 							this.data.type = 'ngendnote';
// 						}else{
// 							this.data.type = 'ngfootnote';
// 						}
// 					}
//
// 					var note = this.specialChars(this.element.getAttribute(this.data.type),false);
//
// 					note = note.substr(3);
// 					note = note.substr(0,note.length - 4);
// 					this.setData('note',note);
//
// 					this.setTitle();
// 				}
// 				,inline:true
// 				,requiredContent:'span[ngendnote,ngfootnote]'
// 				,template:'<span ngfootnote="&lt;p&gt;&lt;/p&gt;">&#8291;</span>' //the 8291 character is an invisibile separator, required otherwise
// 				                                                                  //CKEditor removes the span. A space does not suffice as then
// 																				  //a paragraph that ONLY contains a footnote / endnote removes the note
// 				,upcast: function(element){
// 					return (element.name == 'span' && (element.attributes['ngendnote'] != undefined || element.attributes['ngfootnote'] != undefined));
// 				}
//
// 				//Internal functions here
// 				,specialChars: function(content,encode){
//
// 					//Cannot use an object as order is critical
// 					var list = [
// 						'&','&amp;', //MUST be first
// 						'<','&lt;',
// 						'>','&gt;',
// 						'"','&quot;',
// 						"'",'&apos;'
// 					];
//
// 					for (var i = 0; i < list.length; i +=2 ){
//
// 						var from,to;
// 						if (encode){
// 							from = new RegExp(list[i],'gi');
// 							to   = list[i+1];
// 						}else{
// 							from = new RegExp(list[i+1],'gi');
// 							to   = list[i];
// 						}
//
// 						content = content.replace(from,to);
//
// 					}
//
// 					return content;
// 				}
// 				,setTitle: function(){
//
// 					var title;
// 					var base;
//
// 					switch (this.data.type){
// 						case 'ngendnote':
// 							base = 'End';
// 							break;
// 						case 'ngfootnote':
// 							base = 'Foot';
// 							break;
// 					}
//
// 					title = OCA.getI18n().gettext(base + 'note') + ':' + this.data.note;
//
// 					this.element.setAttribute('title',title);
// 				}
//
// 			});
//
// 			CKEDITOR.dialog.add('ocanotes',function(editor){
// 				return {
// 					 title:OCA.getI18n().gettext('Edit footnote / endnote')
// 					,minWidth:400
// 					,minHeight:150
// 					,contents:[
// 						{
// 							 id:'info'
// 							,elements: [
// 								{
// 									id:'type'
// 									,type:'select'
// 									,label:OCA.getI18n().gettext('Type')
// 									,items:[
// 										 [OCA.getI18n().gettext('Footnote'),'ngfootnote']
// 										,[OCA.getI18n().gettext('Endnote') ,'ngendnote' ]
// 									]
// 									,setup: function(widget){
// 										this.setValue(widget.data.type);
// 									}
// 									,commit: function(widget){
// 										widget.setData('type',this.getValue());
// 									}
// 								}
// 								,{
// 									 id:'note'
// 									,type:'text'
// 									,label:OCA.getI18n().gettext('Note')
// 									,width:'100%'
// 									,setup: function(widget){
// 										this.setValue(widget.data.note);
// 									}
// 									,commit: function(widget){
// 										widget.setData('note',this.getValue());
// 									}
// 								}
// 							]
// 						}
// 					]
// 				};
// 			});
//
// 			//Note, if this is removed, then the name of the command
// 			//for the toolbar changes to "Ocanotes"
// 			editor.ui.addButton('OCANotes', {
// 				label: OCA.getI18n().gettext('Footnote/Endnote')
// 				,command: 'ocanotes'
// 				,icon:'Footnote/Endnote'
// 				,className:'ngcke_textbutton'
// 			})
//
// 		}
// 	});
//
//
// 	CKEDITOR.plugins.add('stopimagepaste', {
// 		init: function(editor) {
// 			function replaceImgText(html) {
// 				var ret = html.replace(/<img\s[^>]*?src\s*=\s*["']\s*https?:\/\/[^>]+>/gi, function(img) {
// 					alert(OCA.getI18n().gettext('Dropping or pasting images directly into the editor is not allowed.'));
// 					return '';
// 				});
// 				return ret;
// 			}
//
//             function chkImg() {
//                 // don't execute code if the editor is readOnly
//                 if (editor.readOnly) {
//                     return;
// 				}
//                 setTimeout(function() {
// 					html = editor.document.$.body.innerHTML;
//                     html = replaceImgText(html);
// 					// Firefox can drop image from local file manager. Disable it as well.
//                     editor.document.$.body.innerHTML = html.replace(/<img\s[^>]*?src\s*=\s*["']\s*data:.+;base64,.*?"[^>]*>/gi, function(img) {
// 						alert(OCA.getI18n().gettext('Dropping images directly into the editor is not allowed.'));
// 						return '';
// 					});
//                 },100);
//             }
//
// 			editor.on( 'contentDom', function() {
//                 // For Firefox
//                 editor.document.on('drop', chkImg);
//                 // For IE
//                 editor.document.getBody().on('drop', chkImg);
//             });
//
// 			// Paste from clipboard
// 			editor.on('paste', function(e) {
// 				var html = e.data.dataValue;
// 				if (!html) {
// 					return;
// 				}
// 				e.data.dataValue = replaceImgText(html);
// 			});
// 			// Switch between source mode and normal mode
// 			editor.on('mode', function(e){
//
// 				var html = editor.getData();;
// 				if (!html) {
// 					return;
// 				}
// 				setTimeout(function(){
// 					editor.setData(replaceImgText(html));
// 				}, 10);
// 			});
//
// 		} //Init
//     });
// }