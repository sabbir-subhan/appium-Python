cordova.define("com.noggin.encryption.encryption", function(require, exports, module) {
var encryption = {

	isRooted: function(success, error){
		cordova.exec(success, error, "EncryptionService", "isRooted", []);
	},

	createSecretKey: function(alias, password, success, error){
		cordova.exec(success, error, "EncryptionService", "createSecretKey", [alias, password])
	},

	getSecretKey: function(alias, password, success, error){
		cordova.exec(success, error, "EncryptionService", "getSecretKey", [alias, password]);
	}

};
module.exports = encryption;
});
