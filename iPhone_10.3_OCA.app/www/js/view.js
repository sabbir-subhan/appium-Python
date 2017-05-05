/**
 * ViewUtil provides several convenience methods for view manipulation
 */
var ViewUtil = {
	templates: {},

	getID: function(url){
		return url ? url.split("/").pop() : null;
	},
	getType: function(url){
		if (url){ //api/v2/eme/123
			var bits = url.split("/"); // api , v2 , eme , 123
			bits.pop(); //remove id 123
			return bits.pop(); //eme
		}
	},
	/** Strips '/api/vXXX/' from the front of the url */
	stripAPI: function(url){
		return url.replace(/^\/api\/v\d+\//,'/');
	},
    getBaseRoute: function(type, OtherFields) {
		OtherFields = OtherFields || {};

        if (type === 'map'){
            return 'mapPage';
        } else if (type === 'riskcontrol'){
            return 'riskcontrolIndex';
        } else if (type === 'teamrole'){
			return '';
		}

        if (type === 'emeTree') {
            if ((typeof OtherFields.ActiveSubEvents != 'undefined') && (OtherFields.ActiveSubEvents < 1)) {
                // Proceed directly to emeView if no sub-events.
                type = 'eme';
            }
        }
        return type + 'View';
    },
	getRoute: function(type, URL, selector, otherFields, mode, extraParams){
		if (URL && URL[0] == '#') {
			URL = URL.substr(1); 												//its already a #appRoute path, so just return without the hash the template will add

			if (URL.indexOf('Pending?') !== -1){ 								// something like #emeNew? has been changed by GopherQueue to Pending. Replace it with the correct view and
				var bits = URL.split('?');
				URL = ViewUtil.getBaseRoute(type) + "?pending=true&" + bits[1]; // change it to the correct View base route, and restore any other parameters
			}
			return URL;
		}
		
		var ID   = ViewUtil.getID(URL);
		var base = ViewUtil.getBaseRoute(type, otherFields);

		if (!base) return ''; //some object types have no route because there is no additional data to load.

		var route = base + '?';

		if (mode && typeof mode == 'string') {
			route += "mode=" + mode + "&";
		}

		if (selector) {
			route += "selector=true&";
		}

		route += "id=" + ID;

		if (extraParams){
			route += ViewUtil.extraParams(extraParams);
		}

		return route;
	},
	extraParams: function(extraParams){
		var queryStr = '';
		for (var k in extraParams){
			queryStr += '&' + k + '=' + extraParams[k];
		}
		return queryStr;
	},
    getIcon : function(type, icon, OtherFields) { //TODO unused?
        if (type === 'emeTree') {
            if (OtherFields.hasOwnProperty('ActiveSubEvents') && OtherFields.ActiveSubEvents < 1) {
                // not a folder icon
                icon = 'warning_sign';
            }
        }
        return icon;
    },
	getDataAttr: function(OtherFields){
		var dataAttr = "";
		for (var attr in OtherFields){
			dataAttr += " data-" + attr + "=" + OtherFields[attr];
		}
		return dataAttr;
	},
	/**
	 * Convert a date into a string describing it relative to the current time.
	 * e.g. 'about 5 minutes ago' for something recent, 10:00 for something that was today, 01/01/2001 for something that was not today
	 * @param {Date} Date comparison date
	 * @param {boolean} [includeTime] can be set as true to force the time to be included in the returned value
	 * 
	 * @return {string} description of the date, relative to now
	 */
	relativeDate: function(date, includeTime){
        if (!(date instanceof Date)){
            if (isNaN(Date.parse(date))){
                return "Invalid date";
            }
            date = new Date(date);
        }
		if (!includeTime) includeTime = false;
		var label;
		var now = new Date();
		var diff = now - date;
		var hr, min;
		if (diff < 5000 ){						//5 seconds
			label = OCA.getI18n().translate("a few seconds ago").fetch();
		} else if (diff < 100000){				//100 seconds
			label = OCA.getI18n().translate("about %d seconds ago").fetch(Math.round(diff / 1000));
		} else if (diff < 3600000){				//1 hour
			label = OCA.getI18n().translate("about %d minutes ago").fetch(Math.round(diff / 60000));
		} else if (diff < 86400000 && now.getDate() === date.getDate()){	//same day of month and within 24 hours, display time
			label = ViewUtil.displayTime(date);
		} else {
			label = includeTime ? ViewUtil.displayDateTime(date) : ViewUtil.displayDate(date);
		}
		return label;
	},
    relativeInterval: function(start, end, fullUnits){
        if (!(start instanceof Date)){
            if (isNaN(Date.parse(start))){
                return "Invalid start date";
            }
            start = new Date(start);
        }
        if (!(end instanceof Date)){
            if (isNaN(Date.parse(end))){
                return "Invalid end date";
            }
            end = new Date(end);
        }
        var diff = Math.abs(end - start) / 1000; //ms to sec
        diff /= 60; //sec to min
        if (diff < 59){
            return Math.round(diff) + (fullUnits ? " minutes" : " min");
        }
        diff /= 60; //min to hrs
        if (diff < 23){
            return (Math.round(diff * 10) / 10) + (fullUnits ? " hours" : " hr");
        }
        diff /= 24; //hrs to days
        return Math.round(diff) + " days";
    },
	dateConvert: function(date,format){
		if (!date || date == 'Invalid Date') return '';
		//see http://pubs.opengroup.org/onlinepubs/007908799/xsh/strftime.html
		var aliases = {
			'%D': '%m/%d/%y',
			'%h': '%b',
			'%T': '%H:%M:%S',
			'%r': '%I:%M:%S %p',
			'%R': '%H:%M',
			'%F': '%Y-%m-%d',
		};
		for (var i in aliases){
			format=format.replace(i,aliases[i]);
		}

		var dow = date.getDay();
		var day = date.getDate();
		var mth = date.getMonth()+1;
		var yr  = date.getFullYear();

		var hr  = date.getHours();
		var min = date.getMinutes();
		var sec = date.getSeconds();

		function pad(num, pad){ //many date formats require two character numbers, 0 padded
			pad = pad || '0';
			return num < 10 ? pad + num : num;
		}

		var replaceProps={
			'%a': this.getDay(date).substr(0,3), 			// the locale's abbreviated weekday name.
			'%A': this.getDay(date), 						// the locale's full weekday name.
			'%b': this.getFullMonth(date).substr(0,3), 		// the locale's abbreviated month name.
			'%B': this.getFullMonth(date), 					// the locale's full month name.
			'%c': date.toLocaleString(),					// the locale's appropriate date and time representation.
			'%C': pad(Math.floor(yr / 100)),				// the century number (the year divided by 100 and truncated to an integer) as a decimal number [00-99].
			'%d': pad(day),									// the day of the month as a decimal number [01,31].
			'%e': pad(day, ' '),							// the day of the month as a decimal number [1,31]; a single digit is preceded by a space.
			'%g': '',										// TODO Two digit representation of the year going by ISO-8601:1988 standards
			'%G': '',										// TODO The full four-digit version of %g
			'%H': pad(hr),									// the hour (24-hour clock) as a decimal number [00,23].
			'%I': hr > 12 ? pad(hr - 12) : pad(hr), 		// the hour (12-hour clock) as a decimal number [01,12].
			'%j': '',										// TODO the day of the year as a decimal number [001,366]
			'%k': pad(hr, ' '),								// Two digit representation of the hour in 24-hour format, with a space preceding single digits,
			'%l': hr > 12 ? pad(hr - 12,' ') : pad(hr,' '), // Hour in 12-hour format, with a space preceding single digits
			'%m': pad(mth), 								// the month as a decimal number [01,12].
			'%M': pad(min),									// the minute as a decimal number [00,59].
			'%n': "\n",										// a newline character.
			'%p': hr	> 11 ? 'PM' : 'AM',					// the locale's equivalent of either a.m. or p.m. (uppercase)
			'%P': hr	> 11 ? 'pm' : 'am',					// the locale's equivalent of either a.m. or p.m. (lowercase)
			'%S': pad(sec),									// the second as a decimal number [00,61].
			'%t': "\t",										// a tab character.
			'%u': dow == 0 ? 7 : dow,						// the weekday as a decimal number [1,7], with 1 representing Monday.
			'%U': '',										// TODO the week number of the year (Sunday as the first day of the week) as a decimal number [00,53].
			'%V': '',										// TODO the week number of the year (Monday as the first day of the week) as a decimal number [01,53]. If the week containing 1 January has four or more days in the new year, then it is considered week 1. Otherwise, it is the last week of the previous year, and the next week is week 1.
			'%w': dow,										// the weekday as a decimal number [0,6], with 0 representing Sunday.
			'%W': '',										// TODO the week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.
			'%x': date.toLocaleDateString(),				// the locale's appropriate date representation.
			'%X': date.toLocaleDateString(),				// the locale's appropriate time representation.
			'%y': pad(yr % 100),							// the year without century as a decimal number [00,99].
			'%Y': date.getFullYear(),						// the year with century as a decimal number.
			'%Z': '',										// TODO the timezone name or abbreviation, or by no bytes if no timezone information exists.
			'%%': '%',										// %
		};
		for (var i in replaceProps){
			format=format.replace(i,replaceProps[i]);
		}
		return format;
	},
	getDay: function(date){
		return ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][date.getDay()];
	},
	getFullMonth: function(date){
		return [
			'January', 'February', 'March', 'April', 'May', 'June',
			'July', 'August', 'September', 'October', 'November', 'December'
		][date.getMonth()];
	},
	/**
	 * the %B format uses full months - e.g. 24 August 2015
	 * this function should convert that to 24/08/2015
	 * If full months are not present in the input, this will have no effect
	 * @param dateStr string value from the date field input
	 * @return converted date value.
	 */
	convertFullMonth: function(dateStr){
		var months = {
			' January ': '/01/', ' February ': '/02/' , ' March ': '/03/', ' April ': '/04/',
			' May ': '/05/', ' June ': '/06/', ' July ': '/07/', ' August ': '/08/',
			' September ': '/09/', ' October ': '/10/', ' November ': '/11/', ' December ': '/12/'
		};
		for(var month in months){
			dateStr = dateStr.replace(month, months[month]);
		}
		return dateStr;
	},
	/**
	 * convert time string from HH:mm:ss am|pm to HH:mm:ss
	 * @param timeStr
	 * @returns {*}
	 */
	convertAMPMTime: function(timeStr){
		if (timeStr.indexOf('am') != -1) { //time contains am. remove am text.
			timeStr.replace('am','');
		} else if (timeStr.indexOf('pm') != -1){ //time contains pm. convert hours value to
			var bits = timeStr.split(':');
			bits[0] = 12 + parseInt(bits[0],10);
			bits[2] = bits[2].replace('pm','');
			timeStr = bits.join(':');
		}

		return timeStr;
	},
	displayDateTime: function(dateStr){
		var date = typeof dateStr == 'Date' ? dateStr : new Date(dateStr);
		if (OCALocale.get('DateTimeFormat')){
			var value = OCALocale.get('DateTimeFormat');
		} else {
			var value = '%d/%m/%Y %H:%M';
		}
		return this.dateConvert(date,value);
	},
	displayDate: function(dateStr){
		var date = typeof dateStr == 'Date' ? dateStr : new Date(dateStr);
		if (OCALocale.get('DateFormat')){
			var value = OCALocale.get('DateFormat');
		} else {
			var value = '%d/%m/%Y';
		}
		return this.dateConvert(date,value);
	},
	displayTime: function(dateStr){
		var date = typeof dateStr == 'Date' ? dateStr : new Date(dateStr);
		if (OCALocale.get('TimeFormat')){
			var value = OCALocale.get('TimeFormat');
		} else {
			var value = '%H:%M';
		}
		return this.dateConvert(date,value);
	},
    btn: function(className, label){
        return '<a href="#" data-role="button" data-mini="true" data-inline="true" data-theme="b" class="ui-link ui-btn ui-btn-b ui-btn-inline ui-shadow ui-corner-all ui-mini '
            + className + '">' + label + '</a>';
    },

	/**
	 * initialise the view utilities by setting some basic event listeners and registering some handlebars helpers
	 */
	init: function(){
		$(document).on('click', '.selector-save', function(){ViewUtil.selector.select();}); //make sure select is called with no values
		$(document).on('click', '.selector-cancel', ViewUtil.selector.cancel);
		$(document).on('click', '.ui-btn', function(){
			var btn = $(this);
			setTimeout(function(){ btn.removeClass('ui-btn-active');}, 300);
		});
		$(document).on('popupafteropen', function(event){
            //close the popup if the user scrolls, but do it in a timeout because ios appears to have a scroll event while the popup is opening
            $(event.target).find('.transspecial').each(OCA.translateSpecial);
        	$(event.target).find('[data-translate]').not('.transspecial').each(OCA.translateStandard);
            setTimeout(function(){
                $(window).one('scroll', function(){
                    if (event.target.id.indexOf('confirm') !== 0 &&
						event.target.id != 'mapToolMore' &&
						event.target.className.indexOf('dynamic-popup') === -1 && //dont scroll-close dynamic dialogs
						event.target.parentNode !== null){ //do nothing if popup has already been remove()d
                    	$(event.target).popup('close');
                    }
                });
            }, 500);
		});
		Handlebars.registerHelper('getID', this.getID);
        Handlebars.registerHelper('getRoute', this.getRoute);
        Handlebars.registerHelper('getIcon', this.getIcon);
		Handlebars.registerHelper('getDataAttr', this.getDataAttr);
		var checkboxClass = function(key, object){
			if (object && object[key]){
				return 'checkbox_tick';
			} else {
				return 'checkbox';
			}
		};
		Handlebars.registerHelper('checkboxClass', checkboxClass);
		var checkboxChecked = function(key, object){
			if (object && object[key]){
				return " checked=checked";
			} else {
				return '';
			}
		};
		var selectorName = function(url){
			return ViewUtil.getType(url) + "-" + ViewUtil.getID(url);
		};
		Handlebars.registerHelper('optChecked', function(id,object){
			return checkboxChecked(id,object);
		});
		Handlebars.registerHelper('optClass', function(id,object){
			return checkboxClass(id,object);
		});
		Handlebars.registerHelper('selectorChecked', function(url, object){
			var key = selectorName(url);
			return checkboxChecked(key, object);
		});
		Handlebars.registerHelper('selectorClass', function(url, object){
			var key = selectorName(url);
			return checkboxClass(key, object);
		});
		Handlebars.registerHelper('selectorName', selectorName);
		Handlebars.registerHelper('inboxIcon', function(type){
			switch(type){
				case 'SMS':
					return 'iphone';
				case 'Email':
					return 'inbox';
				case 'Voice':
					return 'collaboration';
				case 'Fax':
				case 'OCA Connect':
				case 'CAP':
				case 'RSS':
				case 'GeoRSS':
				case 'ATOM':
				case 'Directly Submitted':
					return 'file';
			}
		});
		Handlebars.registerHelper('appMsgIcon', function(data){
			if (data.Status == 'ACKNOWLEDGED') {
				return 'circle_ok green';
			} else if (data.Actions.length){ // && !data.MenuChoice){ //presence of actions but nothing selected
				return 'help red';
			} else if (data.IsDismissed == '1' || data.IsRead == '1') { //no actions, read, nothing
				return '';
			} else {
				return 'circle blue small'; //no actions but unread
			}
		});
		Handlebars.registerHelper('relativeDate', function(date){
			return ViewUtil.relativeDate(new Date(date));
		});
		Handlebars.registerHelper('relativeDateTime', function(date){
			return ViewUtil.relativeDate(new Date(date), true);
		});
		Handlebars.registerHelper('sentLVName', function(contact){
			return contact ? contact : 'workflow';
		});
		Handlebars.registerHelper('contactName', function(contact){
			return contact.displayName || contact.nickname || contact.name.formatted;
		});
        Handlebars.registerHelper('extraParams', this.extraParams);
		Handlebars.registerHelper('oneIndexed', function(zeroIndex){ 	//{{@index}} will be 0-indexed value as per JavaScript, but sometimes you need the 1-indexed equivalent
			return zeroIndex + 1; 										//so just increment by 1
		});
		Handlebars.registerHelper('toLowerCase', function(str){ return str ? str.toLowerCase() : '' });

		$(document).ready(function(){
			//load templates when the whole DOM has loaded.
			ViewUtil.listviewTemplate = Handlebars.compile($("#listviewHB").html());
			ViewUtil.listviewSelectTemplate = Handlebars.compile($("#listviewSelectHB").html());
		});

		$(window).on('orientationchange', function() {
			this.pullToRefreshLength = Math.ceil($(window).height() / 3);
		}.bind(this));
		this.pullToRefreshLength = Math.ceil($(window).height() / 3);
	},
    lightDarkStyle: function(hex){
        var red   = parseInt(hex.substr(0,2),16);
        var green = parseInt(hex.substr(2,2),16);
        var blue  = parseInt(hex.substr(4,2),16);

        var brightness = ((red * 299) + (green * 587) + (blue * 114)) / 255000;

        // values range from 0 to 1
        // anything greater than 0.5 should be bright enough for dark text
        if (brightness >= 0.5) {
            return "dark-text";
        } else {
            return "light-text";
        }
    },
	/**
	 * Handle data displayed in selector mode and the callbacks from that
	 * ViewUtil.selector.data is where the currently selected values are stored
	 */
	selector: {
		data: {},
		callbackOK: function(){},
		callbackCancel: function(){},
		single: false,
		startingHistory: 0,
        goBack: true, //whether to navigate back after a selection
        previousObject: null, //used when returning from selector to keep previously generated typeedit page
		/**
		 * When the selector is submitted, send the data to the success callback and go back the required amount of steps in the history.
		 * It should return to the page which launched the selector
		 */
		select: function(value){
			var data = value || ViewUtil.selector.data;
			if (!this.validate(data)){
				return;
			}

			ViewUtil.selector.callbackOK(data);
			ViewUtil.selector.data = {};
			ViewUtil.selector.single = false;

			ViewUtil.selector.depth = 0;
            if (ViewUtil.selector.goBack !== false){
                util.goBack(ViewUtil.selector.startingHistory - $.mobile.navigate.history.getIndex()); //designed to back to the page which called the selector
            }
            ViewUtil.selector.goBack = true;
            if (ViewUtil.selector.restoreBackup){
                ViewUtil.selector.start(ViewUtil.selector.restoreBackup);
                ViewUtil.selector.restoreBackup = null;
            }
		},
		/* if field data has been set for this selector, validate the selected options against that.
		 * display error messages if the selection is invalid
		 * return boolean indicating validity
		 */
		validate: function(value){
			if (!this.field) return true; //nothing to validate against

			var selected = 0;
			for (var v in value){
				var item = value[v];
				if (item.checked) selected++;
			}

			if (selected < this.field.Minimum){
				util.alertDialog(OCA.getI18n().gettext("You must select at least " + this.field.Minimum + " values"), jQuery.noop, 'Validation', 'Ok');
				return false;
			} else if (selected > this.field.Maximum){
				util.alertDialog(OCA.getI18n().gettext("You must select at most "  + this.field.Maximum + " values"), jQuery.noop, 'Validation', 'Ok');
				return false;
			} else {
				return true;
			}
		},
		/**
		 * When the selector is cancelled, call the failure callback and go back the required amount of steps in the history.
		 * It should return to the page which launched the selector
		 */
		cancel: function(){
			ViewUtil.selector.data = {};
			ViewUtil.selector.callbackCancel();
			ViewUtil.selector.single = false;
			ViewUtil.selector.depth = 0;
			ViewUtil.selector.field = null;

            if (ViewUtil.selector.goBack !== false){
			    util.goBack(ViewUtil.selector.startingHistory - $.mobile.navigate.history.getIndex()); //designed to back to the page which called the selector
            }
            ViewUtil.selector.goBack = true;
            if (ViewUtil.selector.restoreBackup){
                ViewUtil.selector.start(ViewUtil.selector.restoreBackup);
                ViewUtil.selector.restoreBackup = null;
            }
		},
		/** 
		 * save the current history depth when loading the selector 
		 */
		start: function(props){
            if (props && props.makeBackup){
                ViewUtil.selector.restoreBackup = this.backup();
            }

            //reset defaults
            ViewUtil.selector.single = false;
            ViewUtil.selector.depth = 0;
            ViewUtil.selector.goBack = true;
			ViewUtil.selector.field = null;

			ViewUtil.selector.startingHistory = $.mobile.navigate.history.getIndex();
			if (props && props.extraBack) {
				ViewUtil.selector.startingHistory -= props.extraBack; //if there is an intermediate screen (e.g. to select type) the selector should jump back extra.
			}
			$.extend(this, props);
		},
        reset: function(){
            ViewUtil.selector.single = false;
            ViewUtil.selector.depth = 0;
            ViewUtil.selector.goBack = true;
            ViewUtil.selector.startingHistory = 0;
            ViewUtil.selector.previousObject = null;
			ViewUtil.selector.field = null;
        },
        backup: function(){
            return {
                data:           this.data,
                callbackOK:     this.callbackOK,
                callbackCancel: this.callbackCancel,
                single:         this.single,
                goBack:         this.goBack,
                previousObject: this.previousObject,
                extraBack:      this.extraBack,
				startingHistory:this.startingHistory,
				field:			this.field
            }
        }
	},
	/**
	 * Utilty method to render an array of summary data into a listview
	 * @param {JQuery} lv listview
	 * @param {Array} data array of summary items
	 * @param {string} type the type name of the data items
	 * @param {string} icon the name of the icon to display for each item
	 * @param [selectorMode] 	whether this is in selector mode (i.e. listview will be rendered with checkboxes instead of icons).
     *                			If not false, may be an object containing selector mode options
	 * @param {string} [nextURL] if there is an URL to fetch to get the next page of results
     * @param {object} [extraParams] hash of any extra parameters which should be used to create the URL for each list item
	 */
	populateLV: function(lv, data, type, icon, selectorMode, nextURL, extraParams){
		selectorMode = selectorMode || false;
		var unselectable = selectorMode && selectorMode.unselectable;

		if (data.length == 0) {
			lv.empty();
		} else if (selectorMode && !selectorMode.unselectable){
			lv.html(this.listviewSelectTemplate({data: data, icon: icon, type: type, selectorData: this.selector.data, mode: selectorMode}));
			
			lv.off().on('click', 'div.ui-checkbox', function(e){
				var $in  = $(this).find('input');
				$in.prop('checked', !$in.prop('checked'));
				ViewUtil.selector.data[$in.prop('name')] = {
					checked: $in.prop('checked'),
					label: $in.data('label'),
					id: $in.data('id')
				};
				
				if ($in.prop('checked')){
					$(this).find('span').removeClass('checkbox').addClass('checkbox_tick');
				} else {
					$(this).find('span').removeClass('checkbox_tick').addClass('checkbox');
				}
				if (ViewUtil.selector.single){
					ViewUtil.selector.select();	//in single mode. do the 'ok' callback as soon as something is selected
				}
				e.preventDefault();
			});
            if (selectorMode.parentSelect){
                lv.on('click', 'a.parent-mode', function(e){
                    var $in  = $(this).parent().find('input');
                    $in.prop('checked', true);
                    ViewUtil.selector.data[$in.prop('name')] = {
                        checked: $in.prop('checked'),
                        label: $in.data('label'),
                        id: $in.data('id')
                    };
                    $(this).find('div.ui-checkbox span').removeClass('checkbox').addClass('checkbox_tick');
                });
            }
		} else {
			var mode = selectorMode && selectorMode.mode;
            lv.html(this.listviewTemplate({data: data, icon: icon, type: type, unselectable: unselectable, mode: mode, extraParams: extraParams}));
		}

		if (nextURL){
			this.paginate(lv, type, icon, selectorMode, nextURL);
		}
		lv.find('.transspecial').each(OCA.translateSpecial);
	},

	/**
	 * Adds pagination to a listview by listening to scroll events. 
	 * When the user is two-thirds of the way down the list, the next results are requested and appended to the page
	 * 
	 * @param {JQuery} lv previous listview. New content is added after it
	 * @param {string} type of object
	 * @param {string} icon name
	 * @param {bool} selectorMode
	 * @param {string} nextURL
	 */
	paginate: function($lv, type, icon, selectorMode, nextURL){
		var win = $(window);
		var startID = $("body").pagecontainer("getActivePage").prop('id');
		win.on('scroll.listview.' + type, function(){
			var currentID = $("body").pagecontainer("getActivePage").prop('id');
			if (currentID != startID){
				win.off('scroll.listview.' + type);
				return;
			}
			if ((win.height() + win.scrollTop()) > ($lv.height() + $lv.position().top) * .66){
				win.off('scroll.listview.' + type);
				var newLV = $("<ul class='ui-listview extra-data'/>");
				$lv.after(newLV);
				new Gopher(nextURL, function(data, extra){
					ViewUtil.populateLV(newLV, data, type, icon, selectorMode, extra.nextPageURL)
				}).run({offlineError: 'inline'});
			}
		});
	},
	/**
	 * Applies a template to a parent container. 
	 * Supports pagination if required.
	 * @param {JQuery} lv parent container
	 * @param {object} data for template
	 * @param {string} templateName ID of template. If not previously compiled, it will be loaded and compiled from the document
	 * @param {string} [nextURL] the URL where the next set of results may be found, if applicable
	 */
	applyTemplate: function(lv, data, templateName, nextURL){
		if (!this.templates[templateName]) this.templates[templateName] = Handlebars.compile($("#" + templateName).html());
		lv.html(this.templates[templateName]({data: data}));
		if (nextURL){
			this.paginateTemplate(lv, templateName, nextURL);
		}
		lv.find('.transspecial').each(OCA.translateSpecial);
	},
	
	/**
	 * Adds pagination to an element created from a template by listening to scroll events. 
	 * When the user is two-thirds of the way down the list, the next results are requested and appended to the page via the template
	 * 
	 * @param {JQuery} $lv previous listview. New content is added after it
	 * @param {string} templateName ID of template
	 * @param {string} nextURL
	 */
	paginateTemplate: function($lv, templateName, nextURL){
		var win = $(window);
		win.on('scroll.listview.' + templateName, function(){
			if ((win.height() + win.scrollTop()) > ($lv.height() + $lv.position().top) * .66){
				win.off('scroll.listview.' + templateName);
				var newLV = $("<ul class='ui-listview extra-data'/>");
				$lv.after(newLV);
				new Gopher(nextURL, function(data, extra){
					ViewUtil.applyTemplate(newLV, data, templateName, extra.nextPageURL)
				}).run({offlineError: 'inline'});
			}
		});
	},
	
	/**
	 * utility function to generate the HTML code to display the requested icon
	 */
    ocaicon: function(icon){
        return '<span class="icon ' + icon + '"></span>';
    },
	
	/**
	 * Utilty function to convert location data into a string
	 * @param {object} data location data
	 * @param {string} [linebreak] value used for line breaks. Defaults to "<br />"
	 */
	formatLocationData: function(data, linebreak){
		linebreak = linebreak || "<br />";
		var value = "";
		if (data.InternalAddress) value += data.InternalAddress + ", ";
		if (data.BuildingName) value += data.BuildingName;
		if (value != "") value += linebreak;

		if (data.StreetNumber) value += data.StreetNumber + " ";
		if (data.StreetName) value += data.StreetName + ", ";
		if (data.Suburb) value += data.Suburb + linebreak;

		if (data.State) value += data.State + " ";
		if (data.Postcode) value += data.Postcode + ", ";
		if (data.Country) value += data.Country;

        if (value == '' && data.Lat && data.Lng){ //if Lat and Lng are the only entered values, display them.
            value += 'Lat: ' + data.Lat + linebreak + 'Lng: ' + data.Lng;
        }
		return value;
	},
    resizeForScrolling: function(){
        //access via window. because it may not be defined.
        if (window.device && window.device.platform !== 'iOS') return; //no support for fancy scrolling on Android

        var $active = $("body").pagecontainer("getActivePage");
        if ($active.prop('id') === 'mapPage') return; //dont mess with the map

        //set a fixed height on the content to support inertial scrolling (i.e. bounce)
        var $content = $active.find('.ui-content');
        var $footer = $active.find('.ui-footer');
        var fixedHeight = function(){
            var minH = $active.css('min-height').replace('px', '');
            var winHAvail = window.innerHeight - $active.css('padding-top').replace('px', '') - $active.css('padding-bottom').replace('px', '');
            if ($footer.length && !$footer.is('.ui-footer-fixed')){
                return; //footer is not fixed. don't set any heights, or do inertial scrolling
            }
            var contentHeight = $content.outerHeight();
            if (contentHeight > winHAvail){ //if content should be scrollable, set the height to the available window size so that the interial scrolling works properly
                //console.log('content bigger than available. setting content height');
                $content.outerHeight(winHAvail);
            }
            if (minH > winHAvail){
                //console.log('min height set to avail because yo');
                $active.css('min-height', winHAvail); //minH shouldnt exceed available space
            }
            if (contentHeight < minH){
//                console.log('autoheight becayse is small');
                $content.height('auto'); //clear any previously set heights
            }
        }
        setTimeout(fixedHeight,100); //min height might not have been set yet, make a second check a bit later
        setTimeout(fixedHeight,1000);
        $(window).off('infobarResize').on('infobarResize', function(){
            setTimeout(fixedHeight,100); //min height might not have been set yet, make a second check a bit later
            setTimeout(fixedHeight,1000);
        });
    },
    populateIFrame: function($frame, content){
        if (!$frame[0].contentWindow){
            return;
        }
        var iframeDoc = $frame[0].contentWindow.document;

		//TODO: with regex, replace all img src=/api/v2/media/ID to img src=(dataURI) api-src=/api/v2/media/ID
		//this prevents img loading errors while still allowing the code to fetch and insert the records, and subsequently preserve the api-src value
        var iframeContent = "<!doctype html>" +
            "<html><head><title>iFrame</title></head></html>" +
            "<link rel='stylesheet' type='text/css' href='css/richtext.css'>" +
            "<body>"    +
            content     +
            "</body>"   +
            "</head>";


        iframeDoc.open();
        if (window.MSApp && MSApp.execUnsafeLocalFunction) { //windows platform hack
            MSApp.execUnsafeLocalFunction(function () {
                iframeDoc.write(iframeContent);
                iframeDoc.close();
            });
        } else {
            iframeDoc.write(iframeContent);
            iframeDoc.close();
        }
		var $fDoc = $(iframeDoc).find('body');
		$fDoc.css('max-width', ($(window).width() -40) + 'px'); //account for iframe margins

		setTimeout(function() {
			if ($fDoc.width() > $frame.parent().width()) {
				var newZoom = $frame.parent().width() / $fDoc.width() * .95;
				//document is wider than the screen. adjust zoom levels
				$fDoc.find('body').css('zoom', newZoom);

				//the new zoom will affect the reported height of the document.
				//adjust iframe size accordingly, with 50px as a generous buffer to account for margins in the rich text css etc
				// but no smaller than 100px
				$frame.height(Math.max(100, $fDoc.height() * newZoom + 50));
			} else if ($fDoc.height()+50 > $frame.height()) {
				$frame.height($fDoc.height());
				$frame.height($fDoc.height()+50); //set it a second time, because the iframe seems to frequently change its mind about the correct size
			}
		}, 0); //resize the iframe for best display. wrap in a timeout so it has the opportunity to settle the initial state

		ViewUtil.loadMediaForRichContent(iframeDoc);

		$(iframeDoc).find('a').on('click', ViewUtil.linkClickHandler);
    },
	linkClickHandler: function(e){
		var a = e.currentTarget;
		var url = a.href;
		if (url.indexOf('ngoca') == 0){	 //rich text content might have internal links - convert to an app route and redirect
			var route = url.replace('ngoca://', '').replace('request', 'nothing'); //strip scheme, ignore links to requests because they're not in the app
			var bits = route.split('/');
			homeController.redirectLink(bits.shift(), bits.shift()); //type, id
		} else {
			window.open(url, '_system'); //or it might have external links. Intercept them and open in a new window so the app is unaffected
		}
		e.preventDefault();
		e.stopPropagation();
		return false;
	},

	/*
	 *	look for links, either in the form of an internal linkobject and convert to ngoca:// or any other internal or external link, 
	 *	adds <a> tag around link if one doesn't exist already
	 */
	handleObjectLinks: function(message){

		var appLinkObjects = ['communication','logentry','file','asset','eme','report','contactgroup','contact','documentfolder','task','document','inbox','map','risk','riskcontext'];
		
		// first catching group is optional, check if <a> tag exists around link, ditto last group, looking for closing </a> tag
		// then searches for http or https, then looks for internal object link eg: clienturl?linkobject=eme&pk[id]=123 OR checks for generic link
		// for now generic links use same regex to detect as oca server.. but is a pretty bad one.. should be updated if/when oca server is. basically matches any string starting with http:// or https://
		var opentag = '(?:<a [^>]*?href=")?';
		var closetag = '(?:"[^>]*?>([^<]+?)<\\/a>)?';
		var protocol = '(https?\\:\\/\\/)';
		var internalRegex = '('+Configuration.getClientUrl().replace(/^https?\:\/\//i,'').replace(/\./g,'\\.') + '\\?linkobject\\=('+appLinkObjects.join('|')+')&pk(?:.*)?=(\\d+))';
		var externalRegex = '([^ \\t\\r\\n\\v\\f<"]+)';
		var linkregex = opentag + '(' + protocol + '(' + internalRegex + '|' + externalRegex + '))' + closetag;
		var re = new RegExp(linkregex,'ig');

		return message.replace(re,function(x1,x2,x3,x4,x5,x6,x7,x8,x9){

			return x6 ? '<a href="ngoca://'+x6+'/'+x7+'">'+(x9 ? x9 : x2)+'</a>' : (x8 ? '<a href="'+x3 + x8+'">'+(x9 ? x9 : x3 + x8)+'</a>' : '');
		});
	},
    adjustSize: function($frame){
    	var iframeDoc = $frame[0].contentWindow.document;
        var $fDoc = $(iframeDoc);

		if ($fDoc.width() > $frame.parent().width()){
			var newZoom = $frame.parent().width() / $fDoc.width() * .95;
			//document is wider than the screen. adjust zoom levels
			$fDoc.find('body').css('zoom', newZoom);

			//the new zoom will affect the reported height of the document.
			//adjust iframe size accordingly, with 10px padding
			// but no smaller than 100px
			$frame.height(Math.max(100, $fDoc.height() * newZoom + 10));
		} else if ($fDoc.height() > $frame.height()){
			$frame.height($fDoc.height());
		}
    },
	loadMediaForRichContent: function(iframeDoc){
        $(iframeDoc).find('img[src^="/api/v"]').each(function(i, img){
            var mediaURL = img.src.replace('file://', '').replace('x-wmapp0:', '');
            var alt = img.alt;
			img.alt = "Loading image...";
            new Gopher({url: mediaURL, backgroundMode:true}, function(downloadURL){
				if (device.platform === 'Win32NT') downloadURL = 'x-wmapp0:' + downloadURL; //WP8 fix. doesnt support cdvfile
                img.src = downloadURL;
				$(img).attr('alt', alt);
            }, function(){
                img.alt = "Error loading image."
            }).downloadMedia(function(progress){
                var kb = Math.round(progress.loaded / 1024);
                img.alt = 'Loading image... ' + kb + ' kb';
            });
        });
	},
    //parse richtext field content so images can be swapped as needed (without app attempting to download images beforehand causing not found error)
    parseHTML: function(html){
    	var parser = new DOMParser();
		return parser.parseFromString(html, "text/html");
    },
    //annoyingly had to use serialiser to get the resulting parsed response in xhtml (eg with closing / in img tags), and then strip the body tag off to get content
    parsedToXhtml: function(parsed){
    	var xmls = new XMLSerializer();
    	return xmls.serializeToString(parsed.body).replace(/^<body[^>]+>([\s\S]*)<\/body>$/,"$1");
    },
    //find images in rich text, run swapimgsrc
	swapImages: function(html, callback){
		var replacements = [];
		var parsed = ViewUtil.parseHTML(html);
		$(parsed).find('img[src^="/api/v"]').each($.proxy(ViewUtil.swapImgSrc,this,replacements,parsed,callback));

	},
	// swap images with a blank pixel (temporarily - to prevent not found errors rendering the content, then when all images download swap them out)
	swapImgSrc: function(replaceArray,parsed,callback,i,img){

		replaceArray[i] = false;
		var mediaURL = img.getAttribute('src').replace('file://', '').replace('x-wmapp0:', '');
	    var alt = img.alt;
	    img.alt = OCA.getI18n().gettext("Loading image...");
	    //prevent error loading image with wrong path by replacing with blank pixel until after gopher calls return
	    img.src = "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs%3D";
	    img.setAttribute('data-apisrc',mediaURL);

	    new Gopher({url: mediaURL, backgroundMode:true}, function(downloadURL){
			if (device.platform === 'Win32NT') downloadURL = 'x-wmapp0:' + downloadURL; //WP8 fix. doesnt support cdvfile
			
		    $(img).attr('src', downloadURL).attr('alt',alt);
		    replaceArray[i] = true;
		    
			if (replaceArray.indexOf(false) == -1){// if all image src's have been replaced, run callback
				var output = ViewUtil.parsedToXhtml(parsed);
				callback(output);
			}
	        
	    }, function(){
	    	console.log('error handling image');
	        img.alt = OCA.getI18n().gettext("Error loading image.");
	    }).downloadMedia(function(progress){
	        var kb = Math.round(progress.loaded / 1024);
	        img.alt = OCA.getI18n().gettext('Loading image... ') + kb + ' kb';
	    });
	},

	/**
	 * Escape any HTML special characters in a string
	 * @see http://stackoverflow.com/a/6234804
	 * @param {string} dirtyString - unescaped string
	 * @returns {string} escaped string
	 */
	escape: function(dirtyString){
		return dirtyString
			.replace(/&/g, "&amp;")
			.replace(/</g, "&lt;")
			.replace(/>/g, "&gt;")
			.replace(/"/g, "&quot;")
			.replace(/'/g, "&#039;");
    },

	/**
	 * Return a quick access button based on the provided Menu_APIPayload data
	 * @param {Object} qabData Menu_APIPayload representing one quick access button
	 * @param {string} qabData.Name		  The label to display for this button
	 * @param {string} qabData.IconClass  The css class name of the icon to display for this button
	 * @param {string} qabData.TargetURL  The API URL of the object or type this button links to
	 * @param {integer} qabData.TargetId  deprecated - may be provided by old OCA
	 * @param {string} qabData.TargetType deprecated - may be provided by old OCA
	 * @param {string} qabData.ParentURL  The API URL of the parent object this button relates to
	 * @param {Object} qabData.ExtraData  Any extra properties for the button
	 * @returns {JQuery} button
	 */
	getQuickAccessButton: function(qabData) {
		var targetID   = qabData.TargetURL ? ViewUtil.getID(qabData.TargetURL) : qabData.TargetId;
		var targetType = qabData.TargetURL ? ViewUtil.getType(qabData.TargetURL) : qabData.TargetType;
		var parentID   = qabData.ParentURL ? ViewUtil.getID(qabData.ParentURL) : 0;
		var parentType = qabData.ParentURL ? ViewUtil.getType(qabData.ParentURL) : '';

		var targetRoute = '#';
		var extraData   = '';
		var badge		= '';

		switch (targetType) {
			case 'workflow':
				targetRoute = '#workflowView?id=' + targetID;
				extraData   = ' data-mobiletrackingintervalminutes="' + (qabData['ExtraData']['MobileTrackingIntervalMinutes'] ? qabData['ExtraData']['MobileTrackingIntervalMinutes'] : '') + '"' +
					' data-mobiletrackingdurationhours="' + (qabData['ExtraData']['MobileTrackingDurationHours'] ? qabData['ExtraData']['MobileTrackingDurationHours'] : '') + '"';
				break;
			case 'reporttype':
				targetRoute = '#reportNew?type=' + targetID
				break;
			case 'link':
				targetRoute = qabData.ExtraData.URL;
				break;
			case 'contacttype':
				if (parentType == 'contactgroup') {
					targetRoute = '#contactNew?parent=' + parentID + '&type=' + targetID;
				}
				break;
			case 'task':
				targetRoute = '#taskNew';
				break;
			case 'assettype':
				if (parentType == 'asset') {
					targetRoute = '#assetNew?parent=' + parentID + '&type=' + targetID;
				} else {
					targetRoute = '#assetNew?type=' + targetID;
				}
				break;
			case 'emetype':
				if (parentType == 'eme') {
					targetRoute = '#emeNew?parent=' + parentID + '&type=' + targetID;
				} else {
					targetRoute = '#emeNew?type=' + targetID;
				}
				break;
			case 'logtype':
				targetRoute = '#logNew?type=' + targetID;
				break;
			case 'outboundcomm':
				targetRoute = '#messagePage?templateID=' + targetID;
				break;
			case 'menu':
				targetRoute = this.getMenuRoute(targetID);

				//don't show the button if the menu is invisible or the user doesn't have access
				var feature = this.getMenuFeature(targetID);
				if (feature){
					var visfeature = feature ? feature.split('_').shift() : null;
					if (!OCA.checkMenuVisibility(visfeature) || !OCA.checkFeature(feature)){
						return null; //TODO test
					}
				}
				badge = '<span class="badge" style="display:none"></span>';	//menu buttons duplicate any badges of the original icon
				break;
			default:
				console.log('not sure how to handle', qabData);
				return null;
		}

		return $('<div class="ui-block-b home-block userVisible qab">' +
				 '<a class="ui-link qabtype_' + targetType + '" href="' + targetRoute + '"' + extraData + '>' +
				 '<span class="icon ' + qabData.IconClass + '"></span>' + badge +
				 '<br />' + qabData.Name + '</a></div>');
	},

	/**
	 * Add handlers to workflow and link buttons within the specified element
	 * @param {JQuery} $element
	 */
	addQuickAccessButtonListeners: function($element){
		$element.on('click', '.qabtype_workflow', Workflow.confirmActivation);
		$element.on('click', '.qabtype_link', function(e){
			var href = e.currentTarget.href;
			window.open(href, '_system');
			return false;
		});
	},

	getMenuRoute: function(menuKey) {
		var menu = {
			"dashboard":    "#home",
			"risks":        "#riskRegisterIndex",
			"events":       "#emeTreeView?id=0",
			"logs":         "#logIndex",
			"reports":      "#reportIndex",
			"map":          "#mapPage",
			"location":     "#location",
			"assets":       "#assetTreeView?id=0",
			"my_messages":  "#appMessages",
			"inbox":        "#inbox",
			"compose":      "#messagePage",
			"sent":         "#sentComms",
			"photo":        "#photo",
			"video":        "#video",
			"sound":        "#audio",
			"tasks":        "#taskIndex",
			"documents":    "#documentfolderTreeView?id=0",
			"contacts":     "#contactgroupTreeView?id=0",
			"allocate":     "#teamroleAllocation",
			"settings":     "#settings",
			"activate":     "#workflowActivation",
			"offline_sync": "#storage",
			"about":        "#about",
			"logout":       "#session" //n.b. login wouldnt make sense
		};
		return menu[menuKey] ? menu[menuKey] : '#';
	},
	getMenuFeature: function(menuKey){
		var features = {
			"dashboard": "DASH",
			"risks":     "RISKS",
			"events":    "EMES",
			"logs":      "LOGS",
			"reports":   "REPORTS",
			"map":       "MAPPING",
			"assets":    "ASSETS",
			"inbox":     "INBOUNDCOMMS",
			"compose":   "OUTBOUNDCOMMS_SEND",
			"sent":      "OUTBOUNDCOMMS",
			"photo":     "INBOUNDCOMMS_SUBMIT",
			"video":     "INBOUNDCOMMS_SUBMIT",
			"sound":     "INBOUNDCOMMS_SUBMIT",
			"tasks":     "TASKS",
			"documents": "DOCUMENTSFOLDERS",
			"contacts":  "CONTACTSGROUPS",
			"allocate":  "RESOURCESTRUCTURENODES",
			"activate":  "WORKFLOWS_ACTIVATE"
		};
		return features[menuKey] ? features[menuKey] : '';
	},

	pullToRefresh: function($element, refreshFunction){
		if (!$element || !$element.length){
			console.log("Bad arguments for pull to refresh!", arguments);
		}
		var $menu = $('#menuIcon');

		$element.off('scroll.ptr').on('scroll.ptr', function(){
			if (this.scrollTop < -100){
				$menu.removeClass('menu').addClass('refresh');
			} else {
				$menu.removeClass('refresh').addClass('menu');
			}
		});
		$element.off('touchend.ptr').on('touchend.ptr', function(e){
			$menu.removeClass('refresh').addClass('menu');
			if (this.scrollTop < -100){
				$.mobile.loading('show');
				setTimeout(refreshFunction, 100);
				e.preventDefault();
				e.stopPropagation;
				return false;
			}
		})
	}
}
ViewUtil.init();		//call init when the application loads to handle the view related set up
/**
 * Parent View class. Has three properties:
 * page
 * content
 * footer
 */
function View(page){
	this.initView(page);
}
View.prototype.initView = function(page){
	this.page = $(page);		//properties of the view
	this.content = this.page.find('.ui-content').empty();
	this.footer = this.page.find('.ui-footer');
	if (!this.footer.length){	//fallback - mainly for the benefit of unit tests which might not have had the jQM styles applied
		this.footer = this.page.find('div[data-role=footer]');
	}
}
