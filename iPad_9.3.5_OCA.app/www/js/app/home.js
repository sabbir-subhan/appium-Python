//controllers for the loading page and menu
$(document).on("pageinit", "#home", function(e) {
	homeController.init($(this));
	setTimeout(ViewUtil.resizeForScrolling, 1000);
});
$(document).on("pageinit", "#menu", function(e) {
	menuController.init($(this));
});
router.add(
	{
		"#home":           function(type, match, ui, page, e) {
			if (homeController.dashboard === false) {
				//data has loaded, no dashboard, straight to menu
				$("body").pagecontainer("change", '#menu', {changeHash: false});
				return;
			} else {
				homeController.loadDashboard();
			}
			homeController.reset();
			homeController.checkLoaded();
			setTimeout(function() {
				$(window).trigger('resize'); //force dashboard charts to reorientate as it may have changed since last showing
			}, 50);
			ViewUtil.pullToRefresh(homeController.$content, $.proxy(homeController.getDashboard, homeController, true));
		},
		"#menu":           function(type, match, ui, page, e) {
			homeController.reset();
			homeController.checkLoaded();
		},
		"#analyticsTable": function(type, match, ui, page) {
			var Card = window.linkParam.AnalyticsTableCard;
			Card.renderPage($(page));
		},
		"#analyticsChart": function(type, match, ui, page) {
			var Card = window.linkParam.AnalyticsChartCard;
			Card.renderPage($(page));
		}
	});
var homeController = $.extend({}, app, {
	dashboard: null,

	init: function($page) {
		OCA.$header = $('#header');
		OCA.$header.find('.navigation').hide();
		this.$page    = $page;
		this.$content = this.$page.find('.ui-content');
	},

	loadDashboard: function() {
		if (!OCA.initted || !this.$page) return;

		if (OCASession.isLoggedIn()) {
			//fetch dashboard
			this.getDashboard();
		} else {
			$("body").pagecontainer("change", '#menu', {changeHash: false});
		}
	},

	getDashboard: function(dontCache){
		new Gopher('/me/dashboard', $.proxy(this.gotDashboard, this), $.proxy(this.noDashboard, this)).run({dontCheckCache: dontCache, dontProcessError: true});
	},

	gotDashboard: function(data, response) {
		data = $.extend(true, [], data);
		if (data.length === 0) {
			this.noDashboard({status: 404}); //dashboard with no cards is unhelpful
		} else {
			this.dashboard = true;

			//show/hide the dashboard menu icon, but check FeaturesLoaded to avoid a race condition
			if (OCA.FeaturesLoaded) {
				OCA.Features.DASH = OCA.Visibility.DASH = true;
				Session.showMenu();
			} else {
				$(window).one('gotFeatures', function() {
					OCA.Features.DASH = OCA.Visibility.DASH = true;
					Session.showMenu();
				});
			}

			new Dashboard(this.$page, data).render();
		}
	},

	noDashboard: function(xhr, status, error) {
		if (xhr.status == 404) { //definitely no dashboard found
			this.dashboard = false;
			$('#homeMenu').remove();
			$("body").pagecontainer("change", '#menu', {changeHash: false});
		} else if (xhr.status == 401){ //unauthorised, go to menu
			$("body").pagecontainer("change", '#menu', {changeHash: false});
		}
	},

	reset: function() {
		//reset the history when on the home page. Mainly this fixes iOS9 bugs.
		$.mobile.navigate.history.stack       = $.mobile.navigate.history.stack.slice(0, 1);
		$.mobile.navigate.history.activeIndex = 0;

		OCA.$header.find('.navigation').hide();
		$(document).one('pagebeforechange', function() {
			OCA.$header.find('.navigation').show();
		});
		window.linkParams = {}; //start from scratch
	},

	checkLoaded: function() {
		//mobile interface does not use encryption, but the dev environment should show the PIN flow
		var isMobileInterface = window.location.protocol.indexOf('http') === 0;
		if (OCASession.mustUseAppEncryption() && !isMobileInterface){
			if (!OCASession.getEncryptionPIN()){
				return Session.setPIN();
			} else if (Session.shouldCheckPIN()){
				return Session.checkPIN();
			}
		}

		if (ViewUtil.selector.previousObject) {
			//if on a selector before selecting home, clear the selector. the context has been lost.
			ViewUtil.selector.previousObject = null;
		}
		app.checkLoaded.call(this);
		if (this.redirectAfterLogin) {
			this.redirectLink.apply(this, this.redirectAfterLogin);
		}
	},

	redirectLink: function(type, ID, forceSAML) {
		this.redirectAfterLogin = false;
		var page                = '';

		switch (type) {
			case 'communication':
				page = 'sentCommView?id=' + ID;
				break;
			case 'logentry':
				page = 'logView?id=' + ID;
				break;
			case 'file':
				type = 'document'; 	//deliberate fallthrough
			case 'asset':
			case 'eme':
			case 'report':
			case 'contactgroup':
			case 'contact':
			case 'documentfolder':
			case 'task':
			case 'document':
			case 'risk':
			case 'riskcontext':
				page = type + 'View?id=' + ID;
				break;
			case 'nothing':		//do nothing - used to ignore unsupported types
				return;
			case 'inbox':
				page = 'inboxitemView?id=' + ID;
				break;
			case 'map':
				page = 'mapPage?id=' + ID;
				break;
			default:
				page = 'home'; //dont show a message, just leave them on the home screen
				break;
		}

		if (OCASession.isLoggedIn()) {
			if (OCA.FeaturesLoaded) {
				$("body").pagecontainer("change", '#' + page);
				OCA.$header.find('.navigation').show();
			} else {
				$(window).one('gotFeatures', function() {
					$("body").pagecontainer("change", '#' + page);
					OCA.$header.find('.navigation').show();
				});
			}
		} else {
			this.redirectAfterLogin = arguments;
			if (forceSAML) {
				Session.redirectSAML();
			} else {
				$("body").pagecontainer("change", Session.SAMLAvailable ? '#sessionSSO' : '#session');
			}
		}
	}
})
var menuController = $.extend({}, app, {
	init: function($page) {
		this.$page    = $page;
		this.$content = this.$page.find('.ui-content');
		this.$grid    = this.$content.find('.home-icon-grid');
		Session.initMenu(this.$grid); //show/hide menu icons
	},
});

function Dashboard($page, cards) {
	this.$dash = $page.find('.dashboard').empty();
	this.cards = cards.splice(0); //clone
}

Dashboard.prototype.render = function() {
	for (var c = 0; c < this.cards.length; c++) {
		var cardData = this.cards[c];
		var CardView = this.getCard(cardData);
		CardView.render(this.$dash);

		cardData.View = CardView;
	}
}

Dashboard.prototype.getCard = function(cardData) {
	if (!cardData.Type) cardData.Type = 'ANALYTICS'; //TODO
	switch (cardData.Type) {
		case 'QUICKACCESSBUTTON':
			return new QuickAccessCard(cardData);
		case 'SAVEDMAP':
			return new SavedMapCard(cardData);
		case 'ANALYTICS-CHART':
			return new AnalyticsChartCard(cardData);
		case 'ANALYTICS-TABLE':
			return new AnalyticsTableCard(cardData);
		default:
			return new CardView(cardData);
	}
}

function CardView(data) {
	this.data = data;
}

CardView.prototype.render = function($dash) {
	var $card = $('<div class="card"/>');
	ViewUtil.applyTemplate($card, this.data, 'dashboardcard');
	$dash.append($card);
	this.afterRender($card);

	//if the title is too big, try at most twice to make it smaller
	var $title = $card.find('.title');
	var loops  = 0;
	while ($title[0].scrollHeight > $title.height() && loops++ < 2) {
		$title.find('.text').wrapInner("<span class='reduce-font-size'></span>");
	}
}

CardView.prototype.afterRender = function() {}

function QuickAccessCard(data) {
	this.data = data;
	this.setContent();
}

QuickAccessCard.prototype             = new CardView;
QuickAccessCard.prototype.constructor = QuickAccessCard;

QuickAccessCard.prototype.setContent = function() {
	var $grid = $('<div class="ui-grid-b home-icon-grid"></div>');
	$grid.addClass('count-' + this.data.Buttons.length);
	for (var b = 0; b < this.data.Buttons.length; b++) {
		$grid.append(ViewUtil.getQuickAccessButton(this.data.Buttons[b]));
	}
	this.data.Content = $grid[0].outerHTML;
}

QuickAccessCard.prototype.afterRender = function($card) {
	ViewUtil.addQuickAccessButtonListeners($card);
}

function SavedMapCard(data) {
	this.data = data;
	this.setContent();
}

SavedMapCard.prototype             = new CardView;
SavedMapCard.prototype.constructor = SavedMapCard;

SavedMapCard.prototype.setContent = function() {
	//
}

SavedMapCard.prototype.afterRender = function($card) {
	if (!window.esri || !window.esri.geometry.Point){
		$(document).on('mapReady', $.proxy(this.afterRender, this, $card));
		return;
	}
	$card.append("<div class='scroll-protection'></div>"); //absolutely positioned div that sits over the map to prevent scroll being captured

	var center = new esri.geometry.Point(this.data.Lng, this.data.Lat);

	var map = new esri.Map($card.find('.content')[0], {
		center:     center,
		zoom:       this.data.Zoom - 2, //n.b. might get replaced by the setExtent after rendering graphics
		basemap:    'streets',
		logo:       false,
		autoResize: false,
		nav:        false,
		slider:     false,
	});//init map

	map.on('load', function() {
		map.disablePan();
		map.disableMapNavigation();

		var extext = new esri.geometry.Extent(180, 90, -180, -90);
		for (var i = 0; i < this.data.Markers.length; i++) {
			var data = this.data.Markers[i];

			extext.xmin = Math.min(extext.xmin, data.Lng);
			extext.xmax = Math.max(extext.xmax, data.Lng);
			extext.ymin = Math.min(extext.ymin, data.Lat);
			extext.ymax = Math.max(extext.ymax, data.Lat);

			var point   = new esri.geometry.Point(data.Lng, data.Lat);
			var line    = new esri.symbol.SimpleLineSymbol().setColor(new esri.Color([0, 0, 0, 0]));
			var symbol  = new esri.symbol.SimpleMarkerSymbol().setSize(10).setColor(new esri.Color('#' + data.Colour)).setOutline(line);
			var graphic = new esri.Graphic(point, symbol);
			map.graphics.add(graphic);
		}

		if (this.data.Markers.length) {
			extext = esri.geometry.geographicToWebMercator(extext);
			map.setExtent(extext, true);
		}
	}.bind(this));

	$card.on('click', function(id) {
		homeController.redirectLink('map', id);
	}.bind(this, ViewUtil.getID(this.data.ObjectURL)));

	$(window).on('infobarResize orientationchange', function() {
		if (map && $('body').pagecontainer('getActivePage').prop('id') === 'home') {
			map.resize();
			map.reposition();
		}
	});
}

function AnalyticsChartCard(data) {
	this.data      = data;
	this.highchart = data.Content && data.Content.highchart;
	if (!this.highchart) {
		console.log(this.data, 'errorrrror');
	}
	this.setContent();

	this.overrides = {
		chart:       {
			style: {
				'font-size':   '10px',
				'font-family': "'LatoLight', 'Lato', 'Arial'"
			},
		},
		exporting:   {
			enabled: false,
			url:     null
		},
		title:       {
			floating:      true,
			verticalAlign: 'bottom',
			align:         'left',
			x:             2,
			y:             -2,
			text:          null,
		},
		subtitle:    {
			floating:      true,
			align:         'right',
			verticalAlign: 'bottom',
			x:             -2,
			y:             -2,
			text:          null
		},
		plotOptions: {
			pie:    {
				dataLabels: {
					connectorPadding: 5,
					connectorWidth:   1,
					padding:          1,
					distance:         10,
					formatter:        function() {
						if (!this.key.substr) return this.key;
						return this.key.substr(0, 20);
					},
					style:            {
						fontSize:   '10px',
						fontFamily: "'LatoLight', 'Lato', 'Arial'"
					},
				},
				size:       '100%'
			},
			column: {
				dataLabels: {
					style: {
						fontSize:   '10px',
						fontFamily: "'LatoLight', 'Lato', 'Arial'"
					},
				}
			},
			line:   {
				dataLabels: {
					style: {
						fontSize:   '10px',
						fontFamily: "'LatoLight', 'Lato', 'Arial'"
					},
				}
			},
		},
		xAxis:       {
			labels: {
				distance:        1,
				maxStaggerLines: 5,
				style:           {
					'font-size':   '10px',
					'font-family': "'LatoLight', 'Lato', 'Arial'"
				},
				formatter:       function() {
					if (!this.value.substr) return this.value;
					return this.value.substr(0, 10);
				}
			}
		}
	};

	this.overridePage = {
		chart:       {
			style: {
				'font-family': "'LatoLight', 'Lato', 'Arial'"
			},
		},
		exporting:   {
			enabled: false,
			url:     null
		},
		plotOptions: {
			pie:    {
				dataLabels: {
					connectorPadding: 5,
					connectorWidth:   1,
					padding:          1,
					distance:         10,
					style:            {
						fontFamily: "'LatoLight', 'Lato', 'Arial'"
					},
				},
			},
			column: {
				dataLabels: {
					style: {
						fontFamily: "'LatoLight', 'Lato', 'Arial'"
					},
				}
			},
			line:   {
				dataLabels: {
					style: {
						fontFamily: "'LatoLight', 'Lato', 'Arial'"
					},
				}
			},
		},
		xAxis:       {
			labels: {
				distance:        1,
				maxStaggerLines: 5,
				style:           {
					'font-family': "'LatoLight', 'Lato', 'Arial'"
				},
			}
		}
	};
}

AnalyticsChartCard.prototype             = new CardView;
AnalyticsChartCard.prototype.constructor = AnalyticsChartCard;

AnalyticsChartCard.prototype.setContent = function() {
	this.data.Content = "";
};

AnalyticsChartCard.prototype.newChart = function(chartData) {
	var chart = new Highcharts.Chart(chartData);
	if (chart) {
		var oldSize = chart.setSize;

		//add override so that the chart never resizes unless its actively visible on the current page
		chart.setSize = function(width, height, animation) {
			var $active = $("body").pagecontainer("getActivePage");
			var $parent = $(chart.container).parents('.ui-page');
			if ($parent.is($active)) {
				oldSize.apply(this, arguments);
			}
		};
	}
	return chart;
}

AnalyticsChartCard.prototype.afterRender = function($card) {
	var $title = $card.find('.title').append(ViewUtil.ocaicon('chevron-right inline-right grey'));

	var id = 'card-' + ViewUtil.getID(this.data.ObjectURL);
	$card.find('.content').attr('id', id);

	var chartData            = $.extend(true, {}, this.highchart, this.overrides);
	chartData.chart.renderTo = id;
	if (chartData.series && chartData.series[0] && chartData.series[0].type == 'pie') {
		chartData.series[0].size = '100%';
	}
	try {
		this.cardChart = this.newChart(chartData);
	} catch (e) {
		console.error(e);
	}

	$title.on('click', function() {
		window.linkParam = {
			AnalyticsChartCard: this
		}
		$("body").pagecontainer("change", '#analyticsChart');
	}.bind(this));
};

AnalyticsChartCard.prototype.renderPage = function($page) {
	$page.find('.title').text(this.data.Title);
	$page.find('#analyticsChartContent').text('-'); //clear any old stuff

	var chartData            = $.extend(true, {}, this.highchart, this.overridePage);
	chartData.chart.renderTo = 'analyticsChartContent'; //hardcoded div ID for this page
	chartData.chart.width    = $(window).width();
	chartData.chart.height   = $(window).height() - OCA.$header.height() - 2;

//	if (chartData.series && chartData.series[0] && chartData.series[0].type == 'pie') {
//		chartData.series[0].size = '50%';
//	}

	try {
		this.chart = this.newChart(chartData);

		$(window).on('orientationchange', function() {
			this.chart.options.chart.width  = $(window).width();
			this.chart.options.chart.height = $(window).height() - OCA.$header.height() - 2;
			$(window).trigger('resize');
			setTimeout(function() {
				this.chart.options.chart.width  = $(window).width();
				this.chart.options.chart.height = $(window).height() - OCA.$header.height() - 2;
				$(window).trigger('resize');
			}.bind(this), 300);
		}.bind(this));

	} catch (e) {
		console.error(e);
	}
};

AnalyticsChartCard.prototype.renderField = function($lv){
	var $row  = $("<li />").appendTo($lv);
	var $title = $("<h6 />").text(this.data.Title).appendTo($row);
	var $chart = $("<div />").addClass('chart-field').appendTo($row);

	var chartData            = $.extend(true, {}, this.highchart, this.overrides);
	chartData.chart.renderTo = $chart[0];

	try {
		this.chart = this.newChart(chartData);

		$(window).on('orientationchange', function() {
			$(window).trigger('resize');
			setTimeout(function() {
				$(window).trigger('resize');
			}.bind(this), 300);
		}.bind(this));

		setTimeout(function() {
			$(window).trigger('resize');
		}.bind(this), 300);
	} catch (e) {
		console.error(e);
	}
}

function AnalyticsTableCard(data) {
	this.data = data;
}

AnalyticsTableCard.prototype             = new CardView;
AnalyticsTableCard.prototype.constructor = AnalyticsTableCard;

AnalyticsTableCard.prototype.afterRender = function($card) {
	var $title = $card.find('.title').append(ViewUtil.ocaicon('chevron-right inline-right grey'));

	//find the last row being displayed
	var $content = $card.find('.content');
	var $rows    = $content.find('tbody tr');
	if ($rows.length > 5) {
		var cardHeight = $card.height();
		for (var r = 5; r < $rows.length && r < 12; r++) { //10th row and later hidden by CSS and report no position
			if ($($rows[r]).position().top > cardHeight) { //rows overflow the card. show overlay
				$card.append("<div class='extra-content-overlay'></div>");
				break;
			}
		}
	}

	$card.on('click', '.title, .extra-content-overlay', function() {
		window.linkParam = {
			AnalyticsTableCard: this
		}
		$("body").pagecontainer("change", '#analyticsTable');
	}.bind(this))

	$card.find('a').on('click', function() {
//		console.log('asadsasdasd');
	});
	$card.on('click', 'a', ViewUtil.linkClickHandler);
}

AnalyticsTableCard.prototype.renderPage = function($page) {
	$page.find('.title').text(this.data.Title);
	$page.find('#analyticsTableContent').html(this.data.Content);

	var $table = $page.find('table');

	setTimeout(function() {
//		var $thead = $table.find('thead');
//		$thead.find('th').each(function(i,e){
//			console.log(i, $(e).text(), $(e).width());
//		});

		if (this.data.NextPageURL) {
			this.paginate($table, this.data.NextPageURL)
		}

		$table.on('click', 'a', ViewUtil.linkClickHandler);

	}.bind(this), 1);
};

AnalyticsTableCard.prototype.paginate = function($table, nextURL) {
	var win = $(window);

	win.on('scroll.analytics-table', function() {
		var currentID = $("body").pagecontainer("getActivePage").prop('id');
		if (currentID != 'analyticsTable') {
			win.off('scroll.analytics-table');
			return;
		}
		if ((win.height() + win.scrollTop()) > ($table.height() + $table.position().top) * .66) {
			win.off('scroll.analytics-table');
			new Gopher(nextURL, function(data, extra) {
				$table.append($(data[0].Content).find('tbody').html());
				if (data[0].NextPageURL) {
					this.paginate($table, data[0].NextPageURL);
				}
			}.bind(this)).run({backgroundMode: true});
		}
	}.bind(this));
};