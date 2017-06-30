router.add({
	"#location$": {
		handler: function(type, match, ui, page, e){
			console.log(type);
	        //if not allowed, redirect to settings page
	        if (type != "pagebeforeshow") return;
	        
	        if ((!Configuration.get('isActivated') || !Configuration.get('pin')) && !OCASession.isLoggedIn()) {
	        	loc.$content.hide(); //TODO cant hide when coming via the menu
//	            util.alertDialog("Access Denied. Insert your Contact identifier to continue.", jQuery.noop, 'Permissions', 'Ok');
	        	settings.redirect = '#location';
                $("body").pagecontainer("change", $('#settings'), {reverse: false, changeHash: false});
	        } else {
	        	loc.$content.show();
	            loc.getStatus();
				app.checkLoaded();
	        }
	        e.preventDefault();
	    },
	    events: "bs"
	},
    "#locationHistory$": function(type, match, ui, page, e){
        loc.getHistory();
    },
    "#locationHistory[?]selector=true": function(){
        loc.getHistory(true);
    }
});
$(document).on("pageinit", "#location", function(e){
	loc.init($(this));
});
$(document).on("pageinit", "#locationHistory", function(e){
    loc.initHistory($(this));
});
$(document).on("pagehide", "#location", function(){
	clearTimeout(loc.updateLastSentTimer);
});
var loc = $.extend({}, app, {
	KM_TO_MILES: 0.62137119,
	KM_TO_NM: 0.539956803,

	lastSentTime: null,
	updateLastSentTimer: 0,
	init: function(page){
		this.$page = page;
		this.$content = this.$page.find('.ui-content').enhanceWithin();
		
		this.$sendNow = this.$content.find('#locationSendNow').button();
		this.$sendNow.click(function(e){
			$(this).find('.label').text(OCA.getI18n().gettext('Sending now'));
			$(this).button('disable').button('refresh');
			noggin.startLocationTracking(0, 0, loc.locationSuccess, loc.locationFail);
			
		});
		this.$start = this.$content.find('#locationStart').button();
		this.$stop = this.$content.find('#locationStop').button();
		this.$start.click(function(e){
			var interval = loc.$content.find('#locationInterval').val() * 60;			//intervals are set in minutes, convert to seconds
			var duration = loc.$content.find('#locationDuration').val() * 60 * 60;		//duration set in hours,		convert to seconds
			loc.$stop.button('enable');
			$(this).button('disable');
			noggin.startLocationTracking(interval, duration, loc.locationSuccess, loc.locationFail);
		});

		this.$stop.click(function(e){
			noggin.stopLocationTracking(loc.locationStopped, log.e);
		});
//        .button('disable');
		this.$lastSent = this.$content.find('#locationLastSent');
		this.getStatus(true);
		this.updateLastSent();
		this.$content.find('.ios.lowpower').hide();
        $(document).on("pause", function(){
            if(loc.updateLastSentTimer) clearTimeout(loc.updateLastSentTimer)
        }); //turn off javascript timer while in the background
        $(document).on("resume", function(){
        	console.log("resume handler");
            loc.getStatus();
        });

	},
	locationSuccess: function(result){
//		console.log("LOCATION SUCCESS");
		if (result == "OK"){
//			console.log("settings updated");
		} else {
			loc.getStatus();
		}
	},
	locationFail: function(result){
		if (!location.showingError){
			location.showingError = true
			util.alertDialog(OCA.getI18n().gettext(result), function(){
				location.showingError = false;
			}, OCA.getI18n().gettext('Could not submit location'), OCA.getI18n().gettext('Ok'));
		}
		loc.getStatus();
	},
	locationStopped: function(result){
//		console.log("LOCATION STOPPED");
		loc.$stop.button('disable');
		loc.getStatus();
	},
	getStatus: function (fromInit){
		var self = this;
		noggin.getStatus(
            function (result) {
//                console.log('result!', result);
            	if (result == "Location Updated") {
            		//this is the callback for the location success since the previous one was lost (in a reboot, garbage collection, etc)
            		//call get status to really get the status and then go no further with this result. which is not a result at all.
					self.getStatus();
            		return;
            	}
				self.$sendNow.find('.label').text(OCA.getI18n().gettext('Send once now'));
				self.$sendNow.button('enable').button('refresh');
				if (result.isTracking){
					self.$sendNow.button('disable');
					self.$start.button('disable');
					self.$stop.button('enable');
				} else {
					self.$start.button('enable');
					self.$stop.button('disable');
				}
				if (self.$content){
					var interval = result.interval / 60; 	//convert seconds to minutes
					var duration = result.duration / 3600; 	//seconds to hours
                    duration = duration+"";
                    if (duration.substring(0,2) == "0.") duration = duration.substring(1); //lose leading zero
                    if (duration == ".5") duration = ".50"; //match value exactly
                    var $int = self.$content.find('#locationInterval');
                    if (interval && duration){
                        $int.val(interval).change();
						self.$content.find('#locationDuration').val(duration).change();
                    }
                    if (result.isTracking){
						self.$content.find('label[for=locationInterval]').text('Sending every'); //TODO i18n
						self.$content.addClass('trackingMode');
						self.$content.find('.currentInterval').text($int.find('option:selected').text());
						self.$content.find('#locationInterval-button').hide();
                        if (result.until > 621355968000000000){ //wp8 : convert Ticks to unix timestamp
                            result.until = (result.until - 621355968000000000) / 10000;
                        }
						self.$content.find('.currentDuration').text(ViewUtil.relativeInterval(new Date(), new Date(result.until), true));
						self.$content.find('#locationDuration-button').hide();
                    } else {
						self.$content.find('label[for=locationInterval]').text('Send every');
						self.$content.removeClass('trackingMode');
						self.$content.find('.currentInterval').text('')
						self.$content.find('#locationInterval-button').show();
						self.$content.find('.currentDuration').text('')
						self.$content.find('#locationDuration-button').show();
                    }
				}
				if (result.lastSent){
					self.lastSentTime = new Date(result.lastSent);
                    Configuration.set('locationLastSentTime', self.lastSentTime);
					self.updateLastSent();
				}
            },
            function (error){
                console.log('error callback for nogginsistrackingstarted');
                console.log(error);
            }
        );
		self.$content.find('.ios.lowpower').showIf(Configuration.get('iosAccuracySetting') === 'low');
	},
	updateLastSent: function(){
        if (!this.lastSentTime){
			//try to look up last sent time from storage
            var savedTime = Configuration.get('locationLastSentTime');
            if (savedTime) {
                this.lastSentTime = new Date (Configuration.get('locationLastSentTime'));
            }
		}
		var label = "";
		var timeout = 0;
		if (!this.lastSentTime){
			label = OCA.getI18n().gettext("Never");
		} else {
			var now = new Date();
			var diff = now - this.lastSentTime;
			if (diff < 5000 ){						//5 seconds
				label = OCA.getI18n().gettext("a few seconds ago");
				timeout = 10000;
			} else if (diff < 100000){				//100 seconds
                label = OCA.getI18n().translate("about %d seconds ago").fetch(Math.round(diff / 1000));
				timeout = 10000;
			} else if (diff < 3600000){				//1 hour
                label = OCA.getI18n().translate("about %d minutes ago").fetch(Math.round(diff / 60000));
				timeout = 60000;
			} else if (diff < 86400000 && now.getDate() == this.lastSentTime.getDate()){	//same day of month and within 24 hours, display time
				label = ViewUtil.displayTime(this.lastSentTime);
			} else {
				label = ViewUtil.displayDateTime(this.lastSentTime);
			}
		}
		this.$lastSent.text(label);
        this.lastSentLabel = label;
		if (timeout){
			clearTimeout(this.updateLastSentTimer);
			this.updateLastSentTimer = setTimeout($.proxy(this.getStatus, this), timeout);
		}
	},
	//start location tracking service and navigate to the location screen
	startTracking: function(intervalMinutes, durationHours){
		var interval = intervalMinutes * 60;		//intervals are set in minutes, convert to seconds
		var duration = durationHours   * 60 * 60;	//duration set in hours,		convert to seconds
		noggin.startLocationTracking(interval, duration, loc.locationSuccess, loc.locationFail);
        $("body").pagecontainer("change", $('#location'));
	},
    initHistory: function($page){
        this.$history = $page;
//        this.$history.find('#refreshHistory').click($.proxy(this.getHistory, this));
    },
    getHistory: function(selectorMode){
        this.selectorMode = (selectorMode == true);
        noggin.getLocationSessions(10, $.proxy(this.gotHistory, this), log.e);
    },
    gotHistory: function(results){
        var $lv = this.$history.find('.ui-content ul').empty();
        for (var r = 0; r < results.length; r++){
            var $row = $("<li />").html(this.sessionSummary(results[r]));
            var result = results[r];
            if (this.selectorMode){
                $row.wrapInner("<a href='#' />").click($.proxy(ViewUtil.selector.select, ViewUtil.selector, result.locations));
            }
            $lv.append($row);
        }

        if ($lv.children().length === 0){
            $lv.append($("<li />").data('theme','e').text(OCA.getI18n().gettext('There are no tracking sessions recorded')));
        }
        $lv.listview('refresh');
        this.checkLoaded();
    },
    sessionSummary: function(session){
        //"Tracking from [relative date]";
        //"2 hours, 10 km, n points"
        var summary = OCA.getI18n().gettext('Tracking from') + ' ' + ViewUtil.relativeDate(session.start, true);
        if (session.locations.length){
            summary += "<br />";
            summary += ViewUtil.relativeInterval(session.locations[0].event_date, session.locations[session.locations.length-1].event_date);
            summary += ", ";
            summary += this.getDistance(session.locations);
            summary += ", " + session.locations.length + " points";
        }
        return summary;
    },
    //http://stackoverflow.com/questions/27928/how-do-i-calculate-distance-between-two-latitude-longitude-points
    getDistance: function(locations){
        var total = 0;

        var deg2rad = function(deg){
            return deg * (Math.PI/180)
        }
        var km = function(lat1,lon1,lat2,lon2) {
            var R = 6371; // Radius of the earth in km
            var dLat = deg2rad(lat2-lat1);  // deg2rad below
            var dLon = deg2rad(lon2-lon1);
            var a =
                    Math.sin(dLat/2) * Math.sin(dLat/2) +
                        Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) *
                            Math.sin(dLon/2) * Math.sin(dLon/2)
                ;
            var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
            var d = R * c; // Distance in km
            return d;
        }

        var accurateLocations = locations.filter(function (location) {
            return parseInt(location.accuracy,10) < 100
        })

        if (accurateLocations.length > locations.length * 0.8) {
            locations = accurateLocations; //if at least 80% of the locations are under 100m, just use those ones.
        }

        for (var l = 0; l < locations.length - 1; l++){
            var a = locations[l];
            var b = locations[l + 1];
            total += km(a.latitude, a.longitude, b.latitude, b.longitude);
        }

		return this.formatDistance(total);
    },

	//convert a decimal value for kilometers into a friendly number in the units that OCA is configured to use
	formatDistance: function(kmDistance){
		var unit = "km"; //get settings
		var total = kmDistance;

		if (OCA.Settings.DistanceMeasurement == 'mi'){
			unit = 'mi';
			total *= this.KM_TO_MILES;
		} else if (OCA.Settings.DistanceMeasurement == 'nmi'){
			unit = 'nmi';
			total *= this.KM_TO_NM;
		}

		if (total < 1){
			return total.toFixed(2) + " " + unit; //0.45 km
		} else if (total < 10){
			return total.toFixed(1) + " " + unit; //4.5 km
		} else {
			return total.toFixed(0) + " " + unit; //45 km
		}
	}
});
