router.add({
	"#teamroleIndex[?]query=(.*)": function(type, match){
		Teamroles.search(match[1]);
	},
	"#teamroleIndex$": function(type, match, ui, page, e){
		Teamroles.index();
	},
	"#teamroleIndex[?]selector=true": function(type, match, ui, page, e){
		Teamroles.index(true);
	},
    "#teamroleAllocation": function(type, match, ui, page, e){
        Teamroles.allocation($(page));
    },
    "#teamrolePrimary": function(type, match, ui, page, e){
        Teamroles.primary($(page));
    },
    "#teamIndex$": function(type, match, ui, page, e){
        Teamroles.teamIndex();
    },
    "#teamIndex[?]selector=true": function(type, match, ui, page, e){
        Teamroles.teamIndex(true);
    }
});

$(document).on("pageinit", "#teamroleIndex", function(e){ 
	Teamroles.init($(this));
});
$(document).on("pageinit", "#teamIndex", function(e){
    Teamroles.initTeam($(this));
});
var Teamroles = $.extend({}, app, {
	migrations: {				//map v1 teamrole strings to v2 resource strings
		'Teamroles': 			'Resource structure nodes',
		'Teamrole Search': 		'Resource Search',
		'/teamroles': 			'/resourcestructurenodes',
		'/me/possibleteamroles':'/me/possibleresourcestructurenodes',
		'/me/currentteamroles': '/me/currentresourcestructurenodes',
		'/teams': 				'/resourceassignments',
        '/me/currentteamrole/': '/me/currentresourcestructurenode/',
        '/api/v1/teamrole/':    '/api/v2/resourcestructurenode/'
	},
	init: function(page){
		this.page = page;
		this.content = this.page.find('.ui-content');
		this.footer = this.page.find('.ui-footer');
		app.init.call(this);
		this.listview = this.content.find("ul.teamroles.listview");
		this.content.find('#teamroleSearch').keypress(function(e){
			if (e.which == 13){
				Teamroles.search($(this).val(), Teamroles.selectorMode);
			}
		}).on('change', function(e){
			if ($(this).val() == ''){
				Teamroles.index(Teamroles.selectorMode);
			}
		});
	},
    initTeam: function($page){
        this.$team = $page;
        this.$teamLV = this.$team.find('ul.teams');
        this.$teamFooter = this.$team.find('.ui-footer');
    },
	index: function(selectorMode){
		this.selectorMode = selectorMode || false;
		this.page.find('.selector-mode').visibleIf(this.selectorMode);

		this.content.find('div.heading-row h2').text(OCA.getI18n().gettext(this.migrate('Teamroles')));
		new Gopher(this.migrate("/teamroles"), $.proxy(this.gotTeamroles, this)).run();
	},
    teamIndex: function(selectorMode){
        this.selectorMode = selectorMode || false;
        new Gopher(this.migrate("/teams"), $.proxy(this.gotTeams, this)).run();
    },
    allocation: function($page){
        var $lv = $page.find('ul.teamroles').empty();
        new Gopher(this.migrate("/me/possibleteamroles"), $.proxy(this.gotPossibleRoles, this, $lv)).run();
        new Gopher(this.migrate("/me/currentteamroles"),  $.proxy(this.gotCurrentRoles, this, $lv)).run();
    },
    primary: function($page){
        var $lv = $page.find('ul.teamroles');
        new Gopher(this.migrate("/me/currentteamroles"),  $.proxy(this.gotPrimaryRoles, this, $lv)).run();
    },
    gotPossibleRoles: function($lv, data){
        this.possibleRoles = data;
        this.renderAllocate($lv);
    },
    gotCurrentRoles: function($lv, data){
        this.currentRoles = data;
        this.renderAllocate($lv);
    },
    gotPrimaryRoles: function($lv, data){
        ViewUtil.populateLV($lv.empty(), data, 'teamrole', 'administrator_role', true);
    },
    renderAllocate: function($lv){
        if (this.possibleRoles && this.currentRoles){
            var data = {};
            for (var i = 0; this.currentRoles && i < this.currentRoles.length; i++){
                var item = this.currentRoles[i];
                var bits = item.URL.split("/");
                var id = bits.pop();
                var type = bits.pop();
                data[type + "-" + id] = {
                    id: id,
                    label: item.Name,
                    checked: true,
                    initial: true
                };
            }
            ViewUtil.selector.start({
                callbackOK: $.proxy(this.allocateCallback, this),
                callbackCancel: util.goBack,
                data: data,
                previousObject: this,
                goBack: true,
                single: false
            });

            ViewUtil.populateLV($lv, this.possibleRoles, 'teamrole', 'administrator_role', true);
            if (this.possibleRoles.length === 0) {
                $lv.append("<li data-theme='e'>"+OCA.getI18n().gettext('There are no items to display')+"</li>").listview('refresh');
            }
        }
    },
    allocateCallback: function(data){
        var pr = OCA.getPrimaryRole();

        for(var k in data){
            var item = data[k];
            if (item.initial && item.checked){
                //nothing has changed
            } else if (!item.checked){  //role was unchecked
                new Gopher(this.migrate('/me/currentteamrole/') + item.id).sendDelete();
                if (pr){
                    var url = this.migrate('/api/v1/teamrole/') + item.id;
                    if (url === pr.url){ //allocating out of the current primary role
                        OCA.setPrimaryRole(null, null, false);
                    }
                }
            } else if (!item.initial && item.checked){  //role was checked
                console.log('Allocating into ' + item.label);
                new Gopher(this.migrate('/me/currentteamrole/') + item.id).put(false);
            }
        }
        new Gopher(this.migrate('/me/currentteamroles')).uncache();
        new Gopher('/tasks/assigned/me').uncache(); //roles change, assigned tasks can change
        this.currentRoles = null;
        util.goBack();
    },
	search: function(query, mode){
		this.selectorMode = mode || false;
		if (query){
			query = encodeURIComponent(query);
			this.content.find('div.heading-row h2').text(OCA.getI18n().gettext(this.migrate('Teamrole Search')));
			new Gopher(this.migrate("/teamroles") + "?search="+query, $.proxy(this.gotTeamroles, this)).run();
		} else {
			this.index(this.selectorMode)
		}
	},
	gotTeamroles: function(data, extra){
        this.footer.showIf(this.selectorMode);
		ViewUtil.populateLV(this.listview, data, 'teamrole', 'adminstrator_role', this.selectorMode, extra.nextPageURL);
		if (data.length === 0) {
			this.listview.append("<li data-theme='e'>"+OCA.getI18n().gettext('There are no items to display')+"</li>").listview('refresh');
		}
		this.checkLoaded();
	},
    gotTeams: function(data, extra){
        this.$teamFooter.showIf(this.selectorMode);
        ViewUtil.populateLV(this.$teamLV, data, 'team', 'adminstrator_role', this.selectorMode, extra.nextPageURL);
        if (data.length === 0) {
            this.listview.append("<li data-theme='e'>"+OCA.getI18n().gettext('There are no items to display')+"</li>").listview('refresh');
        }
        this.checkLoaded();
    },
	/**
	 * Change 'Teamroles' labels to 'Resource Assignments'
	 * Should only be called on systems of appropriate versions
	 */
	migrateLabels: function(){
		$(".migrateTranslation[data-translate='Add team roles'], .migrateTranslation[data-translate='Add roles']")
			.text(OCA.getI18n().gettext('Add Resource structure nodes'))//n.b full text is required so the translation scraper picks it up
			.attr('data-translate', 'Add Resource structure nodes')
			.data('translate', 'Add Resource structure nodes');

		$(".migrateTranslation[data-translate='Team roles']")
			.text(OCA.getI18n().gettext('Resource structure nodes'))
			.attr('data-translate', 'Resource structure nodes')
			.data('translate', 'Resource structure nodes');

		$(".migrateTranslation[data-translate='Add teams']")
			.text(OCA.getI18n().gettext('Add Resource assignments'))
			.attr('data-translate', 'Add Resource assignments')
			.data('translate', 'Add Resource assignments');

		$(".migrateTranslation[data-translate='Teams']")
			.text(OCA.getI18n().gettext('Resource assignments'))
			.attr('data-translate', 'Resource assignments')
			.data('translate', 'Resource assignments');
	},
	/**
	 * Converts any teamrole string or API path to the resource assignment equivalent, if the system is 1.7.0 or later
	 * @param string str teamrole string
	 * @returns string
	 */
	migrate: function(str){
		if (OCA.versionAtLeast('1.7.0') && this.migrations[str]){
			return this.migrations[str];
		}
		return str;
	}
});