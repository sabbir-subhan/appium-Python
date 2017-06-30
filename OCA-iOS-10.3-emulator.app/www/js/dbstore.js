/**
 * Set up a database controller
 * @see https://github.com/litehelpers/Cordova-sqlcipher-adapter#usage
 */

var dbStore = {
	name:         "oca.db",
	DB:           null,
	VERSION:      "2.0",
	decrypted:    false,
	DB_KEY_ALIAS: "OCA_DB_KEY",

	purgeTimer: 	null,
	purgeTimestamp: null,

	init: function(secret) {
		secret = secret || '';

		if (window.sqlitePlugin) {
			var params = {name: this.name, location: 'default'};
			if (secret) params.key = secret;
			window.sqlitePlugin.openDatabase(params, function(DB) { //success callback
				this.DB        = DB;
				this.decrypted = true;

				if (this.VERSION !== localStorage[dbStore.name + '_VERSION']) {
					this.schemaMigrate();
				} else {
					console.log('trigger database ready schema is up to date');
					$(window).trigger('databaseReady');
				}
			}.bind(this), function() {
				console.error("Unable to open database. Can we fallback to localstorage?");

			});
		} else {
			if (!window.openDatabase){
				window.openDatabase = dbStore.shimOpenDatabase;
			}

			this.DB = window.openDatabase(this.name, '', "OCApp", 5 * 1024 * 1024, function() { //created callback
				localStorage[dbStore.name + '_VERSION'] = undefined;
				this.schemaMigrate();
			}.bind(this));

			if (!this.DB) {
				console.error("Unable to open database. Can we fallback to localstorage?");
				return;
			}
			this.decrypted = true;

			if (this.VERSION !== localStorage[dbStore.name + '_VERSION']) {
				this.schemaMigrate();
			} else {
				$(window).trigger('databaseReady');
			}
		}
	},

	schemaMigrate: function() {
		if (localStorage[dbStore.name + '_VERSION'] === undefined || localStorage[dbStore.name + '_VERSION'] == 'undefined' || !localStorage[dbStore.name + '_VERSION']) {
			//first time database creation
			this.DB.transaction(function(tx) {
				tx.executeSql(dbStore.CREATE_TABLE_OFFLINESYNC, [], function() {
					localStorage[dbStore.name + '_VERSION'] = "1.0";
					dbStore.schemaMigrate();
				}, dbStore.e);
			}, this.e, this.d);
		} else if (localStorage[dbStore.name + '_VERSION'] == "1.0") {
			//version two: response storage
			this.DB.transaction(function(tx) {
				tx.executeSql(dbStore.CREATE_TABLE_RESPONSES, [], function() {
					console.info(arguments);
					localStorage[dbStore.name + '_VERSION'] = "2.0";
					setTimeout(function() {
						$(window).trigger('databaseReady');
					}, 10); //wait a tick to make sure the database is really ready
				}, dbStore.e);
			}, this.e, this.d);
		}
	},

	n: function(tx, results) {
		//n for nothing
		//makes it easy to swap between logging and not logging (but mind .d doesnt hit .DB usages if doing find and replace)
	},
	d: function(tx, results) {
		if (!tx) return;
		console.debug(tx, results);
		if (!results && tx.rows) results = tx;
		for (var i = 0; results && i < results.rows.length; i++) console.debug(results.rows.item(i));
	},
	e: function(tx, error) {
		if (!error || tx.message) error = tx;
		var err = new Error(error && error.message ? error.message : error);
		console.error(JSON.stringify(err.stack));
		console.error(tx, error);
	},

	/**
	 * Dev convenience method to execute arbitrary SQL
	 * @param sql
	 * @param params
	 */
	sql: function(sql, params, success, error) {
		params  = params || [];
		success = success || this.d;
		error   = error || function(tx, error) {
				console.error("Problematic SQL: ", sql);
				this.e(tx, error);
			}.bind(this);

		if (this.isReady()) {
			this.DB.transaction(function(tx) {
				tx.executeSql(sql, params, success, error);
			}.bind(this), this.e, this.d);
		} else {
			console.warn("Database not ready for: ", sql);
		}
	},

	wipe: function(deferred) {
		console.log('wiping database', deferred ? 'with def' : 'no def');
		var d = deferred ? deferred.resolve : this.d;
		var e = deferred ? deferred.resolve : this.e;  //the most likely reason for being unable to delete the database is it not existing

		if (window.sqlitePlugin) {
			localStorage[dbStore.name + '_VERSION'] = undefined;
			dbStore.DB                              = null;

			window.sqlitePlugin.deleteDatabase({name: this.name, location: 'default'}, d, e);
		} else if (this.DB) {
			this.DB.transaction(function(tx) {
				tx.executeSql("DELETE FROM responses WHERE 1=1", [], d, e);
			}.bind(this), e, d);
		} else { //no database set up so there's nothing to wipe
			if (deferred) deferred.resolve();
		}
	},

	vacuum: function() {
		if (this.DB && this.DB.executeSql) {
			this.DB.executeSql("VACUUM", [], dbStore.d, dbStore.e);
		}
	},

	purge: function(deferred) {
		if (!this.DB) {
			$(window).one('databaseReady', $.proxy(this.purge, this, deferred));
			return;
		}
		this.DB.transaction(function(tx) {
			tx.executeSql("DELETE FROM responses WHERE datetime(data_expiry) < datetime('now')", [], function() {
				if (deferred) deferred.resolve();
				this.purgeTimestamp = null;

				tx.executeSql("SELECT MIN(data_expiry) AS NextPurge FROM responses", [], function(tx, results){
					if (results.rows.length){
						this.nextPurge(results.rows.item(0).NextPurge);
					}
				}.bind(this), this.e)
			}.bind(this), this.e);

		}.bind(this), this.e, this.d);
	},

	nextPurge: function(dataExpiry){
		if (!dataExpiry) return;

		var expiryTimestamp = new Date(dataExpiry).valueOf() + 5000;
		if (!this.purgeTimestamp || expiryTimestamp < this.purgeTimestamp){

			var wait = expiryTimestamp - Date.now().valueOf();
			if (this.purgeTimer) clearTimeout(this.purgeTimer);

			this.purgeTimer = setTimeout(this.purge.bind(this), wait);
			this.purgeTimestamp = expiryTimestamp;
		}
	},

	create: function(pin) {
		encryption.createSecretKey(this.DB_KEY_ALIAS, pin, this.createOK.bind(this), this.createFail.bind(this));
	},

	createOK: function(secret) {
		var $initAfterWipe = $.Deferred();
		$initAfterWipe.done(this.init.bind(this, secret));

		this.wipe($initAfterWipe);
	},

	createFail: function(e) {
		console.error(e);
		util.alertDialog("Unable to set up encrypted storage");
        OCASession.set('UseAppEncryption', false);
        dbStore.init();
        Session.goHome();
	},

	decrypt: function(pin) {
		encryption.getSecretKey(this.DB_KEY_ALIAS, pin, this.decryptOK.bind(this), this.decryptFail.bind(this));
	},

	decryptOK: function(secret) {
		this.init(secret);
	},

	decryptFail: function(e) {
		console.error(e);
		util.alertDialog("Unable to unlock encrypted storage");
	},

	isDecrypted: function() {
		return this.DB && this.decrypted;
	},

	isReady: function() {
		return this.DB && this.decrypted && localStorage[dbStore.name + '_VERSION'] == this.VERSION;
	},

	//sql statement constants
	CREATE_TABLE_OFFLINESYNC: "CREATE TABLE offlinesync (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, method VARCHAR(10) NOT NULL, url VARCHAR(255) NOT NULL, timestamp INT NULL, data TEXT NOT NULL)",
	CREATE_TABLE_RESPONSES:   "CREATE TABLE responses (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, url VARCHAR(255) NOT NULL, data TEXT NOT NULL, cache_expiry VARCHAR(50) NULL, data_expiry VARCHAR(50) NULL)",

	/**
	 * a mock database object shim which can replace webSQL - either because it's missing (FF/IE),
	 * or to prevent caching (mobile interface where encryption is mandatory but unavailable)
	 */
	mockDatabase: {
		tx:           {
			executeSql: function(sql, params, sqlSuccess, sqlError) {
				sqlSuccess(dbStore.mockDatabase.tx, dbStore.mockDatabase.emptyResults);
			}
		},
		emptyResults: {
			rows: []
		},
		transaction:  function(txCallback, txError, txSuccess) {
			txCallback(dbStore.mockDatabase.tx);
			txSuccess();
		}
	},
	shimOpenDatabase: function(name, version, displayName, size, callback){
		var db = dbStore.mockDatabase;
		return db;
	}
}