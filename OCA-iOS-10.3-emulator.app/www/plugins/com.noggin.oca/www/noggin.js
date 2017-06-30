cordova.define("com.noggin.oca.noggin", function(require, exports, module) {

var noggin = {
	//the success callback will be executed every time the location service successfully updates its position,
	//to allow the last sent time to be tracked
	startLocationTracking: function (interval, finish, success, error){
		console.log("start location tracking");
		if (interval == 0 && finish == 0) {
            console.log("once only");
        } else {
            if (device.platform === 'iOS'){
                var mode = Configuration.get('iosAccuracySetting') || 'high';
                cordova.exec(log.d, log.e, 'NogginService', 'setLocationMode', [mode]);
            }
        }
        var pin = Configuration.get('pin');
        var dId = util.getDeviceId();
        var session;
        var domain;
        if (OCASession.isLoggedIn()) {
            session = OCASession.getSessionId();
            domain = Configuration.getAPIUrl();
            if (domain) domain += "/locations";
        }
        cordova.exec(success, error, "NogginService", "startLocationTracking", [interval, finish, pin, dId, session, domain]);
	},
	stopLocationTracking: function(success, error){
		console.log("stop location tracking");
		cordova.exec(success, error, "NogginService", "stopLocationTracking", []);
	},
    getStatus : function(success, error) {
        cordova.exec(success, error, "NogginService", 'getStatus', []);
    },
    getLocationSessions: function(count, success, error){
        cordova.exec(success, error, "NogginService", "getLocationSessions", [count]);
    },
	addDownload: function(title, uri, path, mime){
		cordova.exec(
			function(){console.log("successful download " + uri)}, 
			function(){console.error("failed download " + uri)}, 
			"NogginService", 
			"addDownload", 
			[title, uri, path, OCASession.get('id'), mime]
		);
	},
	datePicker: function(date, format, success, error){
		if (!date) date = new Date();
		error = error || log.e
		cordova.exec(
			function(data){
				success(new Date(data));
			}, 
			error, 
			"NogginService",
			format + "Picker",
			[date.getFullYear(), date.getMonth(), date.getDate(), date.getHours(), date.getMinutes()]
		);
	}
};

//this file gets wrapped by cordova when it installs, and the variable must be exported to the 'module'
//variable added by the wrapping process.
module.exports = noggin;

});
