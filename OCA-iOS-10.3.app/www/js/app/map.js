router.add({
    "#mapPage": function(){
        if (theSilentCartographer.map) {
            theSilentCartographer.map.resize();
            theSilentCartographer.map.reposition();
            if (theSilentCartographer.map.infoWindow){
                theSilentCartographer.map.infoWindow.hide();
            }
        }
        if (theSilentCartographer.$tools){
            theSilentCartographer.$tools.hide();
        }
        if (theSilentCartographer.editToolbar){
            theSilentCartographer.editToolbar.deactivate()
        }
    },
    "#mapPage$": function(){
        if (linkParams.mapShouldResume) {
            linkParams.mapShouldResume = false; //reset
            return;
        }

        theSilentCartographer.stopPlotting(); //when loading from menu, start afresh
        theSilentCartographer.handleLink(); //might have object creation message to display
        if (theSilentCartographer.map) {
            theSilentCartographer.resumePosition();
        }
    },
    "#mapPlotType": function(){
        if (linkParams.createdObject || linkParams.selectorCancel) util.goBack(); //if returning from creating an object, continue going backwards.
    },
    "#mapPage[?]wip": function(){
//        window.linkParams = {geometry: {
//            type: 'eme',
//            ID: 226201
//        }};
//        theSilentCartographer.linkMode = 'geometry';
//        theSilentCartographer.handleLink();
        setTimeout(function(){
            theSilentCartographer.getSavedMap(76,true);
        },1500);

    },
    "#mapPage[?]search=true": function(){
        theSilentCartographer.linkMode = 'search';
        theSilentCartographer.handleLink();
    },
	"#mapPage[?]address=true": function(){
        theSilentCartographer.stopPlotting();
        theSilentCartographer.linkMode = 'address';
        theSilentCartographer.handleLink();
    },
    "#mapPage[?]geometry=true": function(){
        if (linkParams.mapShouldResume) {
            linkParams.mapShouldResume = false; //reset
            return;
        }

        theSilentCartographer.stopPlotting();
        theSilentCartographer.linkMode = 'geometry';
        theSilentCartographer.handleLink();
    },
    "#mapPage[?]selector=true": function(){
        if (linkParams.mapShouldResume) {
            linkParams.mapShouldResume = false; //reset
            return;
        }

        theSilentCartographer.linkMode = 'selector';
        theSilentCartographer.handleLink();
    },
    "#mapPage[?]id=(\\d+)": function (type, match, ui, page, e) {
        var created = linkParams.createdObject;
        theSilentCartographer.linkMode = 'savedmap';
        window.linkParams = {
            mapID: match[1]
        };
        theSilentCartographer.handleLink();
        theSilentCartographer.getSavedMap(match[1], created); //if returning from creating an object to the saved map, reload the map
    },
    "#mapPage[?]layer=(\\d+)": function(type, match){
        setTimeout(function(){
            theSilentCartographer.showStaticLayer(match[1]);
        },1000);
    },
    "#mapPage[?]linklayer=(\\d+)": function(type, match){
        setTimeout(function(){
            theSilentCartographer.showLinkLayers([match[1]]);
        },1000);
    },
    "#mapPage[?]type=(\\w+)&id=(\\d+)(&selector=true)?": function(type, match){
        theSilentCartographer.getObjectMap(match[1], match[2], !!match[3]);
    },
    "#mapLayers": function(){
        if (theSilentCartographer.$layersPage.find('.ui-content ul').children().length === 0){
            theSilentCartographer.getLayers();
        }
    },
    "#savedMaps": function(){
        if (theSilentCartographer.$savedMapsPage.find('.ui-content ul').children().length === 0){
            theSilentCartographer.getSavedMaps();
        }
    },
    "#mapPlotShortcut": function(type, match, ui, page){
        if (linkParams.createdObject || linkParams.selectorCancel) util.goBack(); //if returning from creating an object, continue going backwards.
        theSilentCartographer.showMapPlotShortcuts($(page));
    },
    "#mapAttributesView": function(t, m, u, page){
        new MapAttributesView($(page)).getData();
    },
    "#mapAttributesEdit": function(t, m, ui, page){
        new MapAttributesEdit($(page)).getData();
    }
});
$(document).on('pageinit', '#mapPage', function(e){
    theSilentCartographer.init($(this));
});
//require arcgis files on load so they are available for dashboard map cards and object geocoding
$(document).ready(function() {
    require(['esri/tasks/locator', 'esri/SpatialReference', 'esri/map', 'esri/geometry/Point', 'esri/geometry/Circle',
                'esri/symbols/SimpleMarkerSymbol', 'esri/symbols/SimpleLineSymbol', 'esri/graphic', 'esri/graphicsUtils',
                'esri/layers/WebTiledLayer', 'esri/layers/ArcGISTiledMapServiceLayer', 'esri/layers/ArcGISImageServiceLayer',
                "esri/layers/GeoRSSLayer", "esri/layers/ImageServiceParameters", "esri/layers/KMLLayer", 'esri/toolbars/draw',
                'esri/toolbars/edit', "esri/tasks/geometry", "esri/dijit/LocateButton", 'dojo/ready'], function() {
        $(document).trigger('mapReady');
        $('#map a').attr('href', '#mapPage').removeClass('disabled-until-load')
    })
});

$(document).one("pageshow", "#mapPage", function(e){ //pageinit is too early for the esri mapping to init. listen for the first pageshow instead
    require(['./js/lib/geojsonlayer.js'], function(GJL){
        esri.layers.GeoJsonLayer = GJL;
    });
    navigator.geolocation.getCurrentPosition(
        function(geo){
            theSilentCartographer.loadMap(geo.coords);
            theSilentCartographer.handleLink(); //if the map being loaded for the first time is from a link in an object
        },
        function(failure){
            theSilentCartographer.loadMap();
            theSilentCartographer.handleLink(); //if the map being loaded for the first time is from a link in an object
        },
        {timeout: 5000}
    );
});
$(document).on('pageinit', "#mapLayers", function(){
    theSilentCartographer.initLayers($(this));
});
$(document).on('pageinit', "#savedMaps", function(){
    theSilentCartographer.initSavedMaps($(this));
});
$(document).on('pageinit', '#mapPlotType', function(){
    theSilentCartographer.initMapPlotType($(this));
});
$(document).on('pageinit', '#mapSearch', function(){
    theSilentCartographer.initMapSearch($(this));
});

var theSilentCartographer = $.extend({}, app, {
    ARCGIS_GEOCODE: "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer",
    mapLoaded: false,
    currentGeometry: [],
    drawingLayer: true,
    staticLayers: [],
    linkLayers: [],
    defaultPointSymbol: {width: 34, height: 34, xoffset: 4, yoffset: 17},
    DEFAULT_ZOOM: 12,
    MAP_REPOSITION_TIME: 300, //300 seconds = 5 minutes
    wktOverrides: {},
    layerURLs: {},

    /** Layers and Saved Maps */
    initLayers: function($page){
        this.$layersPage = $page;
        this.$layersPage.find('#layersDone').click(function(){
            theSilentCartographer.clearLayers();
            var IDs = [];
            $page.find('ul.static input:checked').each(function(i,e){
                IDs.push($(e).data('id'));
            });
            theSilentCartographer.showStaticLayers(IDs);
            var linkIDs = [];
            $page.find('ul.links input:checked').each(function(i,e){
                linkIDs.push($(e).data('id'));
            });
            theSilentCartographer.showLinkLayers(linkIDs);
        });

    },
    initSavedMaps: function (page){
        this.$savedMapsPage = page;
    },
    initMapPlotType: function($page){
        $page.find('a').on('click', function(e){
            linkParams.selectorCancel = true;
            var $a = $(e.target);
            $("body").pagecontainer("change", $a.data('link'));
        });
    },
    showMapPlotShortcuts: function($page){
        var $lv = $page.find('ul.links').empty();
        if (this.currentLinks){
            linkParams.selectorCancel = true;
            for (var l = 0; l < this.currentLinks.length; l++){
                var link = this.currentLinks[l];
                var page = this.getMobilePage(link);
                $("<li><a href='" + page + "'>" + link.Name + "</a></li>").appendTo($lv);
            }
        }
        $lv.enhanceWithin().listview('refresh');
    },
    initMapSearch: function($page){
        this.$searchLV = $page.find('.ui-content ul');
        var $search = $page.find('#mapSearchInput');
        $search.keypress(function(e){
            if (e.which == 13){                             //pressing enter key
                theSilentCartographer.mapSearch($(this).val());
            }
        });
        $page.find('#runSearchButton').on('click', function(){ //search button in footer
            theSilentCartographer.mapSearch($search.val());
        });

        this.$searchLV.on('click', 'li', function(){
            var loc = $(this).data('location');
            window.linkParams = {
                dontClearMap: true,
                showLocation: loc
            };
            $("body").pagecontainer("change", '#mapPage?search=true');
        })
    },
    mapSearch: function(address){
        $.mobile.loading('show');
        var locator = new esri.tasks.Locator(this.ARCGIS_GEOCODE);
        locator.outSpatialReference = this.map.spatialReference;
        locator.addressToLocations({
            address: {
                SingleLine: address
            },
            outFields: ["Loc_name"]
        }, $.proxy(this.searchResults, this));
    },
    searchResults: function(data){
        this.$searchLV.empty();
        if (data.length === 0){
            this.$searchLV.append("<li>No results</li>");
        } else {
            var last = '';
            for (var i = 0; i < data.length; i++){
                var result = data[i];
                if (result.address != last && result.score > 80){
                    last = result.address;
                    $('<li><a>' + result.address + '</a></li>').data('location', result.location).appendTo(this.$searchLV);
                }
            }
        }
        this.$searchLV.listview('refresh');
        $.mobile.loading('hide');

        if (data.length === 1){
            window.linkParams = {
                dontClearMap: true,
                showLocation: data[0].location
            };
            $("body").pagecontainer("change", '#mapPage?search=true');
        }
    },
    getSavedMap: function(id, dontCheckCache){
        new Gopher({url: '/map/' + id, dontCheckCache: dontCheckCache}, $.proxy(this.gotSavedMap, this, false), function(){
            util.alertDialog(OCA.getI18n().gettext("Unable to load saved map"), jQuery.noop, 'Error', 'Ok');
        }).run();
    },
    gotSavedMap: function(selectorMode, map){
        if (!this.mapLoaded) return; //map not loaded yet.
//        util.log('got saved map', selectorMode ? 'sel' : 'non');
        this.clearLayers(true);
        this.currentGeometry = [];
        if(this.map) this.map.graphics.clear();
        if (map[0]) map = map[0];
        if (map.Zoom) this.zoom = map.Zoom;

        for (var i = 0; map.Layers && i < map.Layers.length; i++){
            this.showLayer(map.Layers[i]);
        }

        if (this.map.graphics.graphics.length){
            this.fitGraphics();
        } else if (map.Zoom && map.Lat && map.Lng){
            this.moveTo(map.Lng, map.Lat, map.Zoom);
        }
        this.checkLoaded();
        if (selectorMode){
            this.plotting = true;
            this.creating = false;
        } else {
            //have loaded a saved map
            this.plotting = false;
            this.creating = false;
        }
        this.updateFooter();
        this.checkAutoSelectPlot();
    },
    showStaticLayers: function(layerIDs){
        for (var l = 0; l < layerIDs.length; l++){
            this.showStaticLayer(layerIDs[l]);
        }
    },
    showLinkLayers: function(linkIDs){
        for (var l = 0; l < linkIDs.length; l++){
            new Gopher('/link/' + linkIDs[l], $.proxy(this.gotLinkLayer, this)).run();
        }
    },
    clearLayers: function(clearLayerPage){
        clearLayerPage = clearLayerPage || false;
        for (var s = 0; s < this.staticLayers.length; s++){
            this.map.removeLayer(this.staticLayers[s]);
        }
        this.staticLayers = [];
        for (var s = 0; s < this.linkLayers.length; s++){
            this.map.removeLayer(this.linkLayers[s]);
        }
        this.linkLayers = [];

        if (clearLayerPage && this.$layersPage){
            this.$layersPage.find('input:checked').toggle();
        }
    },
    getObjectMap: function(type, id, selectorMode){
        new Gopher('/' + type + '/' + id + '/map', $.proxy(this.gotSavedMap, this, selectorMode), function(){
            util.alertDialog(OCA.getI18n().gettext("Unable to load saved map"), jQuery.noop, 'Error', 'Ok');
        }).run();
    },
    createObjectMap: function(locationFields){ //create a fake object map based on any currently set location field data
        var map = {Layers: []};
        if (locationFields && !$.isEmptyObject(locationFields)){
            var layer = {LayerType: 'DRAWING', FillColour: 'CC00FF', Objects: []};
            for (var fID in locationFields){
                var f = locationFields[fID];
                if (f.Lng && f.Lat){
                    var object = {
                        id: 'locationfield-' + fID,
                        WKT: 'POINT(' + f.Lng + ' ' + f.Lat + ')',
                        Param: {field: fID}
                    }
                    layer.Objects.push(object);
                }
            }
            map.Layers.push(layer);
        }
        this.gotSavedMap(this.plotting, map);
    },
    createLocationFieldOverrides: function(type, id, locationFields){
        this.wktOverrides = {};
        if (locationFields && !$.isEmptyObject(locationFields)){
            for (var fID in locationFields){
                var f = locationFields[fID];
                if (f.Lng && f.Lat){
                    var id = "location-" + type + '-' + id + '-' + fID;
                    var wkt = 'POINT(' + f.Lng + ' ' + f.Lat + ')';
                    this.wktOverrides[id] = wkt;
                }
            }
        }
    },
    showLayer: function(layerData){
        if (this.plotting && layerData.LayerType !== "DRAWING") return; //if plot mode, only show drawing layer

        var Line = esri.symbol.CartographicLineSymbol; //shortcut
        var Fill = esri.symbol.SimpleFillSymbol;
        var Icon = esri.symbol.PictureMarkerSymbol;

        if (layerData.StrokeWeight && layerData.StrokeColour){
            this.currentLineSymbol = new Line(Line.STYLE_SOLID, new dojo.Color('#' + layerData.StrokeColour), layerData.StrokeWeight, Line.CAP_ROUND, Line.JOIN_MITER, 10);
        }
        if (layerData.FillColour){
            this.currentFillSymbol = new Fill(Fill.STYLE_SOLID, null, this.getDojoColor(layerData.FillColour, 0.5));
            this.currentPointSymbol = new Icon(Configuration.getAPIDomain() + '/pkg/xhtml_default_map/point.php?rgb='+layerData.FillColour, 34, 34)
                .setOffset(4, 17);
        }

        var layer;
        //noinspection FallThroughInSwitchStatementJS
		switch (layerData.LayerType){
            case "QUERY":
                this.drawingLayer = false;
            case "DRAWING":
                if (layerData.Objects.length === undefined){ //if Objects is not in the expected array format, take a stab at fixing it
                    if (layerData.Objects[0]){
                        var objs = [];
                        for (var k in layerData.Objects){
                            if (!isNaN(k)) objs.push(layerData.Objects[k]); //Objects is a hash, add everything with numeric keys
                        }
                        layerData.Objects = objs
                    } else if (layerData.Objects.icon){ //only one object, convert to array
                        layerData.Objects = [layerData.Objects]
                    }
                }
                var layerLine = this.currentLineSymbol;
                var layerFill = this.currentFillSymbol;
                var layerIcon = this.currentPointSymbol;
                for (var d = 0; d < layerData.Objects.length; d++){
                    var obj = this.normaliseObject(layerData.Objects[d]);
                    if (obj.StrokeColour){
                        this.currentLineSymbol = new Line(Line.STYLE_SOLID, this.getDojoColor(obj.StrokeColour), obj.StrokeWeight, Line.CAP_ROUND, Line.JOIN_MITER, 10);
                    } else {
                        this.currentLineSymbol = layerLine; //reset to layer default
                    }
                    if (obj.FillColour){
                        this.currentFillSymbol = new Fill(Fill.STYLE_SOLID, null, this.getDojoColor(obj.FillColour, 0.5));
                    } else {
                        this.currentFillSymbol = layerFill;
                    }
                    if (obj.Icon){
                        this.currentPointSymbol = new Icon(Configuration.getAPIDomain() + obj.Icon, obj.IconW, obj.IconH).setOffset(obj.IconW/2 - obj.IconX, obj.IconH/-2 + obj.IconY);
                    } else {
                        this.currentPointSymbol = layerIcon;
                    }

                    this.drawingLayer = true;

                    this.displayWKT(obj.WKT, obj.Features, obj.Tool, obj.Param);
                }
                break;
            case "GEORSS":
            case "ARCGISLAYER":
                layer = this.addLinkLayer(layerData, layerData.LinkID);
                break;
            case "BOUNDARY":
                break;
            case "STATIC":
                this.showStaticLayer(layerData.StaticGISID);
                break;
            case "ADDRESS":
                this.findAddress(layerData.Name, false, this.currentPointSymbol);
                break;
            default:
                console.log("I HAVE NO IDEA WHAT TYPE YOU AER", layerData.LayerType, layerData);
        }
        if (layer) this.map.addLayer(layer);
        this.currentFillSymbol = this.currentLineSymbol = this.currentPointSymbol = null;
    },
    normaliseObject: function(obj){
        //convert old API output to a normalised map object and apply some defaults
        if (obj.strokeColour) obj.StrokeColour = obj.strokeColour;
        if (obj.strokecolour) obj.StrokeColour = obj.strokecolour;
        if (obj.strokeweight) obj.StrokeWeight = obj.strokeweight;
        if (!obj.StrokeWeight) obj.StrokeWeight = 3;

        if (obj.fillColour) obj.FillColour = obj.fillColor;
        if (obj.fillcolour) obj.FillColour = obj.fillcolor;

        if (obj.icon){
            obj.Icon = obj.icon;
            obj.IconX = obj.iconx;
            obj.IconY = obj.icony;
            obj.IconW = obj.iconw;
            obj.IconH = obj.iconh;
        }

        if (this.wktOverrides[obj.id]){
            obj.WKT = this.wktOverrides[obj.id];
        } else if (obj.wkt && obj.wkt.value){
            obj.WKT = obj.wkt.value;
        }

        if ((!obj.Features || obj.Features.length == 0) && obj.Attributes && obj.Attributes.length){
            obj.Features = this.loadFeaturesFromAttributes(obj.Attributes);
        } else if (obj.Features && obj.Features.length){ //correct single attributes not in array format
            for (var f = 0; f < obj.Features.length; f++){
                if (obj.Features[f].Attributes && !obj.Features[f].Attributes.length && obj.Features[f].Attributes.FeatureValue){
                    obj.Features[f].Attributes = [obj.Features[f].Attributes];
                }
            }
        }

        if (obj.tool) obj.Tool = obj.tool;

        if (!obj.Param){
            obj.Param = {};
            if ($.isArray(obj.param)){
                for (var p = 0; p < obj.param.length; p++){
                    obj.Param[obj.param[p].name] = obj.param[p].value;
                }
            } else if (obj.param){
                obj.Param = obj.param;
            }
        }
        return obj;
    },
    getSavedMaps: function(){
        new Gopher('/maps', $.proxy(this.gotSavedMaps, this)).run();
    },
    gotSavedMaps: function(maps, extra){
        var $lv = this.$savedMapsPage.find('.ui-content ul');
        ViewUtil.populateLV($lv, maps, 'map', 'world_map', false, extra.NextPageURL);
        if ($lv.children().length === 0){
            $lv.append($("<li />").data('theme','e').text(OCA.getI18n().gettext('There are no saved maps available for display'))).listview('refresh');
        }
        this.checkLoaded();
    },
    getLayers: function(){
        this.returnedLists = 0;
        new Gopher('/maplayers', $.proxy(this.gotLayers, this)).run();
        OCA.IncidentManager = true;
        if (OCA.IncidentManager && OCA.versionAtLeast('1.6.18')){
            new Gopher('/links?type[]=GEORSS&type[]=GEOJSON&type[]=KML&type[]=ARCGISLAYER', $.proxy(this.gotLinks, this)).run();
        } else {
            this.returnedLists++;
        }
    },
    gotLayers: function(layers, extra){
        ViewUtil.populateLV(this.$layersPage.find('ul.static'), layers, 'layer', '', true, extra.NextPageURL);
        this.checkLayersLoaded();
    },
    gotLinks: function(links, extra){
        ViewUtil.populateLV(this.$layersPage.find('ul.links'), links, 'layer', '', true, extra.NextPageURL);
        this.checkLayersLoaded();
    },
    checkLayersLoaded: function(){
        app.checkLoaded.call(this);
        if (this.returnedLists == 2 && this.$layersPage.find('ul.static').children().length === 0 && this.$layersPage.find('ul.links').children().length === 0) {
            this.$layersPage.find('ul.static').append($("<li />").data('theme','e').text(OCA.getI18n().gettext('There are no items to display'))).listview('refresh');
        }
    },

    /** Plotting */
    updateFooter: function(){
        var $selMode = this.page.find('.selector-mode');
        $selMode.showIf(this.plotting);
        this.page.find('.ui-footer.normal-mode').showIf(!this.plotting);

        var $save = $selMode.find('a.selector-save');

        this.footer.find('#mapClear').visibleIf(this.map && this.map.graphics.graphics.length);
        var $plot = this.footer.find('#mapPlot a');

        if (!this.currentGeometry.length){
            $save.html('&nbsp;');
            $save.removeClass('ui-btn-b')
            $plot.text(OCA.getI18n().gettext('Plot')).off('.mapdrawing');
        } else {
            $save.addClass('ui-btn-b');
            if (this.creating){
                $save.text(OCA.getI18n().gettext('Create'));
            } else if (this.plotting){
                $save.text(OCA.getI18n().gettext('Save'));
            }
        }
    },

    /** Interfaces */
    handleLink: function(){
        if (!this.mapLoaded) return; //map not loaded yet.

        var type = this.linkMode || "address";
        if (!linkParams.dontClearMap){
            this.currentGeometry = [];
            this.map.graphics.clear();
        }

        //object types may restrict available feature symbology tools.
       
        if (linkParams.restrictedFeatureSymbologies){
            this.restrictSymbologyFeatures(linkParams.restrictedFeatureSymbologies);
            setTimeout(function(){
                window.linkParams.restrictedFeatureSymbologies = null;
            }, 2000); //clear the params in a timeout so
        } else {
            this.resetSymbologyFeatures();
        }

        if (type === 'selector') {
            this.startSelectorMode();
        } else if (type === "geometry" && linkParams.geometry) {
            if (linkParams.geometry.restorableGeometry) {
                this.restoreGeometry(linkParams.geometry.restorableGeometry);
            } else {
                if (linkParams.geometry.type && linkParams.geometry.ID) {
                    this.createLocationFieldOverrides(linkParams.geometry.type, linkParams.geometry.ID, linkParams.geometry.locationFields);
                    this.getObjectMap(linkParams.geometry.type, linkParams.geometry.ID, this.plotting);
                } else {    //adding geometry for a new object, no id yet set
                    this.createObjectMap(linkParams.geometry.locationFields);
                }
            }
            window.linkParams = {};
        } else if (linkParams.createdObject) {
            this.plotting = false;
            util.infobar(linkParams.message);
            this.linkMode     = null;
            window.linkParams = {};
            setTimeout(function() {util.infobarClear();}, 10000);
        } else if (linkParams.selectorCancel) {
            this.linkMode     = null;
            window.linkParams = {}; //dont need to do anything except go back
        } else if (linkParams.showLocation) {
            this.currentPointSymbol = new esri.symbol.PictureMarkerSymbol(Configuration.getAPIDomain() + '/pkg/xhtml_default_map/point.php?rgb=cc00ff', 34, 34).setOffset(4, 17);
            this.displayPoint(linkParams.showLocation);
            this.centerAndZoom(linkParams.showLocation, this.DEFAULT_ZOOM);
            this.updateFooter();
            this.linkMode     = null;
            window.linkParams = {}
        } else if (type == 'savedmap') {
            theSilentCartographer.getSavedMap(linkParams.mapID);
            this.linkMode     = null;
            window.linkParams = {};
        } else {
            if (linkParams.mapFromAddress && linkParams.mapFromAddress.data && linkParams.mapFromAddress.data.Lat && linkParams.mapFromAddress.data.Lng) {
                this.displayAddress(linkParams.mapFromAddress.data);
            } else if (linkParams.mapFromAddress && linkParams.mapFromAddress.content) {
                this.findAddress(linkParams.mapFromAddress.content);
            }
            this.linkMode     = null;
            window.linkParams = {};
        }

    },
    centerAndZoom: function(point, zoom){
        this.center = point;
        this.zoom = zoom;
        this.mapPositionTime = Date.now();
        this.map.centerAndZoom(this.center, this.zoom);
    },
    moveTo: function(lng, lat, zoom){
        zoom = zoom || this.DEFAULT_ZOOM;
        this.centerAndZoom(new esri.geometry.Point(lng, lat), zoom);
    },
    moveToCurrentPosition: function(){
        var self = this;
        navigator.geolocation.getCurrentPosition(
            function(geo){
                self.moveTo(geo.coords.longitude, geo.coords.latitude)
            },
            $.noop,
            {timeout: 5000}
        );
    },
    resumePosition: function(){
        util.log('resuming map at ', this.center, this.zoom, this.mapPositionTime);
        var diff = (Date.now() - this.mapPositionTime) / 1000; //difference betwen map times in seconds
        util.log('map resumed ago', diff);
        if (diff > this.MAP_REPOSITION_TIME){
            this.moveToCurrentPosition();
        } else {
            this.centerAndZoom(this.center, this.zoom);
        }
    },
    showStaticLayer: function(id){
        var url = Configuration.getAPIUrl() + "/maplayer/" + id + "/tile"; //?x=${col}&y=${row}&z=${level}";
        var wtl = new esri.layers.WebTiledLayer(url, {id: 'Static layer ' + id});
        var id = this.map.addLayer(wtl);
        this.staticLayers.push(id);
    },
    gotLinkLayer: function(data){
        
        if (!data || !data[0]) return;

        var layerData = data[0].MapLayer;
        this.addLinkLayer(layerData, true);
    },
    addLinkLayer: function(layerData, isLinkLayer){
        //use main link URL as key
        this.layerURLs[layerData.WMSURL] = [layerData.WMSURL];
        if (layerData.ProxyURLs && layerData.ProxyURLs.length){
            this.layerURLs[layerData.WMSURL] = layerData.ProxyURLs.slice();
        }

        console.log('for this layer, trying ', this.layerURLs[layerData.WMSURL]);
        var url = this.layerURLs[layerData.WMSURL].shift();
        console.log('FIRST TRY: ', url);
        var type = layerData.FeedType || layerData.LayerType;

        if (type == 'ARCGISLAYER'){ //ArcGIS is more work, call a separate function
            this.getArcGISLayer(url, layerData, isLinkLayer);
        } else {
            var getLayer = function (type, url){
                console.log('get layer', type, url);
                switch(type){
                    case "GEORSS":
                        return new esri.layers.GeoRSSLayer(url);
                    case "KML":
                        return new esri.layers.KMLLayer(url);
                    case "GEOJSON":
                        return new esri.layers.GeoJsonLayer({url: url}); //https://github.com/Esri/geojson-layer-js
                }
                return null;
            }

            var gotLayer = function(layer){
                if (!layer) return;
                console.log('got layer');

                layer.on('load', function(){
                    console.log('layer loaded', type, url);
                    var id = theSilentCartographer.map.addLayer(layer);
                    if (isLinkLayer){
                        theSilentCartographer.linkLayers.push(id);
                    }
                });
                layer.on('error', function(){
                    console.log('layer error', type, url);
                    if (theSilentCartographer.layerURLs[layerData.WMSURL].length){
                        url = theSilentCartographer.layerURLs[layerData.WMSURL].shift();
                        console.log('next URL to try:', url);
                        gotLayer(getLayer(type, url));
                    }
                })
            }

            gotLayer(getLayer(type, url));
        }
    },
    showLayerInfo: function(layerData, e){
        var g = e.graphic;

        var display = layerData.DisplayField
            ? g.attributes[layerData.DisplayField]
            : '';
        this.map.infoWindow.setTitle(display);

//		var datetimeformat = layer.getWgt().datetimeformat;
		var fields = g.getLayer().fields;
		var fIndex = {};
		for (var f = 0; f < fields.length; f++){
			fIndex[fields[f].name] = fields[f];
		}

        var content = [];
        for (var f = 0; f < layerData.SelectedFields.length; f++){
            var key = layerData.SelectedFields[f];
			var label = key;
			var value = g.attributes[key];
			var field = fIndex[key];
			if (field){
				if (field.alias) {
					label = field.alias;
				}

				if (field.type == 'esriFieldTypeDate'){
					var esriDate = new Date(value);
					value = esriDate.toLocaleString();
				}
			}
            content.push("<b>" + key + "</b>: " + value);
        }
        content = content.join("<br />");
        this.map.infoWindow.setContent(content);

        //handle tools
        var self = this;
        if (layerData.ObjectLinks && layerData.ObjectLinks.length){
            var label = OCA.getI18n().gettext('Save as') + ((layerData.ObjectLinks.length === 1)
                ? ' ' + layerData.ObjectLinks[0].Name
                : '...');

            var $btn = $(ViewUtil.btn('saveas', label)).on('click', function(){
                    self.handleLayerObjectLinks(layerData, g);
                });
            $(this.map.infoWindow._contentPane).append($btn);
        }

        this.map.infoWindow.show(
            e.mapPoint,
            this.map.getInfoWindowAnchor(e.screenPoint)
        );

        e.preventDefault();
        e.stopPropagation();
        return false;
    },
    getArcGISLayer: function(url, layerData, isLinkLayer){
        var gotFeed = function(feed, layerData, isLinkLayer, result){
            console.log('gotArcGisLayer', result, arguments);
            var layer;
            if (result.error) {
                if (result.error.code == 498 || result.error.code == 499){
                    //TODO get fresh token case
                    console.log('GET FRESH TOKEN CASE');
                    return;
                } else if (result.error.code == 404){
                    console.log('404 layer not found', feed);
                    return;
                }
            }

            var opacity = 1;
            if (layerData.Transparency){
                opacity = (100 - layerData.Transparency) / 100;
            }
            if (result.type && result.type.toLowerCase().match(/feature/)){ //feature layer
                layer = new esri.layers.FeatureLayer(feed, {
                    mode: esri.layers.FeatureLayer.MODE_ONDEMAND,
                    outFields: layerData.SelectedFields,
                    opacity: opacity
                });
                if (layerData.SelectedFields && layerData.SelectedFields.length){
                    layer.on('click', $.proxy(this.showLayerInfo, this, layerData));
                }
            } else if (result.serviceDataType && result.serviceDataType.toLowerCase().match(/esriimageservicedatatype/)) { //image service layer
                var params = new esri.layers.ImageServiceParameters();
                params.format = "png";
                params.noData = 0;
                layer = new esri.layers.ArcGISImageServiceLayer(feed, {
                    imageServiceParameters: params,
                    opacity:opacity
                });
            } else if (result.tileServers && result.tileServers[0] != 'undefined') { //Tiled map layer
                layer = new esri.layers.ArcGISTiledMapServiceLayer(feed, {
                    opacity: opacity
                });
            } else { //raster layer
                var imageParameters = new esri.layers.ImageParameters();
                imageParameters.format = "jpeg";
                layer = new esri.layers.ArcGISDynamicMapServiceLayer(feed, {
                    opacity: opacity,
                    imageParameter: imageParameters
                });
            }

            if (layer){
                var id = this.map.addLayer(layer);
                if (isLinkLayer){
                    this.linkLayers.push(id);
                }
                layer.on('load', function(){
                    theSilentCartographer.fitGraphics(layer.fullExtent || layer.extent || layer.initialExtent);
                });
            }
        };

        var getFeed = function(url){
            console.log('get feed', url);
            var feed = url;
            var join = feed.indexOf('?') === -1 ? '?' : '&';
            if (layerData.Token){
                feed += join + 'token=' + layerData.Token;
                join = '&';
            }

            $.ajax(feed + join + 'f=json', {
                dataType: 'json',
                error: function(){
                    console.log('arcgis layer load error', url);
                    if (theSilentCartographer.layerURLs[layerData.WMSURL].length){
                        url = theSilentCartographer.layerURLs[layerData.WMSURL].shift();
                        console.log('next URL to try:', url);
                        getFeed(url);
                    }
                },
                success: $.proxy(gotFeed, theSilentCartographer, feed, layerData, isLinkLayer)
            });
        }

        getFeed(url);

    },
    restoreGeometry: function(restorable){
        for(var r=0; r < restorable.length; r++){
            var geometry = restorable[r];
            switch (geometry.WKTType){
                case 'POINT':
                    this.displayPoint   (geometry, geometry.feature);   break;
                case  'LINESTRING':
                    this.displayLine    (geometry, geometry.feature);   break;
                case 'CIRCLE':
                case 'POLYGON':
                    this.displayPolygon (geometry, geometry.feature);   break;
            }
        }
    },
    displayWKT: function(wkt, features, tool, params){
        if (!wkt) return;
        if (m = /^([A-Z]+)\s*\((.*)\)$/.exec(wkt)) {
            var featureIndex = {};
            if (features){
                if (m[1] === "GEOMETRYCOLLECTION"){
                    for (var f = 0; f < features.length; f++){
                        var off = features[f].Offset;
                        if (off === undefined) off = f; //if no offset is explicitly set, assume offset is the array position
                        featureIndex[off] = features[f];
                    }
                } else if ($.isArray(features)){
                    //not a geometrycollection, assume the first feature is the style to apply
                    features = features[0];
                } //else, this is recursive from a geocollection and the feature is an object. dont need to do anything
            }

            var geo, graphic;
            switch (m[1]) {
                case 'POINT':
                    if (m = /^POINT\s*\(([0-9.-]+ +[0-9.-]+)\)$/.exec(wkt)) {
                        var bits = m[1].split(' ');
                        geo = this.displayAddress({
                            Lng: bits[0], Lat: bits[1]
                        }, false, features);
                    }
                    break;
                case 'LINESTRING':
                    if (m = /^LINESTRING\s*\((([0-9.-]+ +[0-9.-]+)( *, *[0-9.-]+ +[0-9.-]+)*)\)$/.exec(wkt)) {
                        var p = m[1].split(/ *, */);
                        var points = [];
                        for (var i = 0; i < p.length; i++) points.push(p[i].split(' '));
                        geo = new esri.geometry.Polyline(points);
                        geo = esri.geometry.geographicToWebMercator(geo);
                        geo.WKTType = 'LINESTRING';
                        this.displayLine(geo, features);
                    }
                    break;
                case 'POLYGON':
                    if (m = /^POLYGON\s*\((( *?\,? *\((([0-9.-]+ +[0-9.-]+)( *, *[0-9.-]+ +[0-9.-]+)*)\))+)\)$/.exec(wkt)) {
                        //Cannot use capturing as the polygon could contain multiple "rings"
                        var p = m[1].slice(1,m[1].length-1); //Remove the first and last character
                        var ringBits = p.split(/\) *, *\(/);
                        var rings = [];
                        for (var i = 0; i < ringBits.length; i++){
                            var p = ringBits[i].split(/ *, */);
                            rings[i] = [];
                            for (var x = 0; x < p.length; x++){
                                rings[i][x] = p[x].split(' ');
                            }
                        }
                        geo = new esri.geometry.Polygon(rings);
                        geo = esri.geometry.geographicToWebMercator(geo);
                        geo.WKTType = 'POLYGON';
                        this.displayPolygon(geo, features);
                    } else {
                        console.log(' WKT does not match regex', wkt);
                    }
                    break;
                case 'CIRCLE':
                    if (m = /^CIRCLE\s*\(([0-9.-]+ +[0-9.-]+) *, *([0-9.-]+ +[0-9.-]+)\)$/.exec(wkt)) {
                        var center = new esri.geometry.Point(m[1].split(' '));
                        center = esri.geometry.geographicToWebMercator(center);
                        var edge   = new esri.geometry.Point(m[2].split(' '));
                        edge = esri.geometry.geographicToWebMercator(edge);
                        var radius = esri.geometry.getLength(center, edge);
                        var geo = new esri.geometry.Circle(center, {
                            radius: radius,
                            radiusUnit: esri.Units.METERS,
                            geodesic: false
                        });
                        geo.WKTType = 'CIRCLE';
                        this.displayPolygon(geo, features);
                    }
                    break;
                case 'GEOMETRYCOLLECTION':
                    if (m = /^GEOMETRYCOLLECTION\s*\((.*)\)$/.exec(wkt)) {

                        var d = 0; var a = ['']; var s = m[1];
                        for (var i = 0; i < s.length; i++) {
                            if (s.substr(i,1) == ',' && d == 0) {
                                a.push('');
                            } else {
                                if (s.substr(i,1) == ')') d--;
                                a[a.length-1] += s.substr(i,1);
                                if (s.substr(i,1) == '(') d++;
                            }
                        }
                        for (var i = 0; i < a.length; i++) {
                            this.displayWKT(a[i], featureIndex[i], tool);
                        }
                    }
                    break;
            }
            if (geo && tool){
                geo.tool = tool; //for tool display on click of graphic
            }
            if (geo && this.drawingLayer){
                geo.drawing = true;
            }
            if (geo && params){
                geo.params = params;
            }
        }
    },
    fitGraphics: function(extent){
        if (extent){
            if (!extent.spatialReference.isWebMercator()){
                if (this.isGeographic(extent)){
                    extent = esri.geometry.geographicToWebMercator(extent);
                } else {
                    console.log('Unknown co-ordinate system: ', extent);
                    return;
                }
            }
            var newE = this.map.extent.union(extent);
            if (!this.isExtentTooBig(newE)){
                this.map.setExtent(newE);
            }
        } else if (this.map.graphics && this.map.graphics.graphics && this.map.graphics.graphics.length){
            var zoomExtent = esri.graphicsExtent(this.map.graphics.graphics);
            if (zoomExtent) {
                this.map.setExtent(zoomExtent, true);
            } else {
                var geo = this.map.graphics.graphics[0].geometry;
                if (geo.type === 'point'){
                    this.centerAndZoom(geo, this.zoom);
                }
            }
        }
    },
    isGeographic: function(extent){
        var isGeo = Math.abs(extent.xmin) <= 180 &&
            Math.abs(extent.xmax) <= 180 &&
            Math.abs(extent.ymin) <=  90 &&
            Math.abs(extent.ymax) <=  90;

        return isGeo;
    },
    isExtentTooBig: function(extent){
        if ((extent.xmax - extent.xmin) > 10000000 || (extent.ymax - extent.ymin) > 10000000){
            return true; //if the extent exceeds 10 million units, it's larger than australia and probably useless
        }
        return false;
    },
    startSelectorMode: function(){
//        console.log('start selector mode', linkParams);
        this.currentGeometry = [];
        this.map.graphics.clear();
        this.plotting = true;
        this.creating = false;

        theSilentCartographer.linkMode = 'geometry'
        theSilentCartographer.handleLink();

        this.updateFooter();

        var ok = ViewUtil.selector.callbackOK; //selector mode has already started
        ViewUtil.selector.callbackOK = $.proxy(this.selectorBack, this, ok);
        ViewUtil.selector.callbackCancel = $.proxy(this.stopPlotting, this);
    },
    selectorBack: function(ok){
        //if an polyline/gon has been part drawn and the user clicks save
        if (this.currentTool && this.draw){
            this.draw.finishDrawing();
            this.editToolbar.deactivate();
        }
        var data = this.getCurrentGeometry();
        ok(data);
        this.stopPlotting();
    },
    handleViewTool: function(tool){
        if (!tool) return;
        if (tool.signal && tool.signal.substr(0,4) === 'view' && tool.toolarg){
            var type = tool.signal.substr(4);
            var id = tool.toolarg['pk[id]'] ? tool.toolarg['pk[id]'] : tool.toolarg.value; //handle new and old API format respectively
            if (id){
                $("body").pagecontainer("change", '#' + type + "View?id=" + id);
            }
        }
    },
    handleAttributesTool: function(geometry){
        this.selectedIndex = this.currentGeometry.indexOf(geometry);
        if (this.selectedIndex == -1){
            return; //what happened?
        }
        this.currentAttributes = [];
        if (geometry.feature && geometry.feature.Attributes) {
            this.currentAttributes = geometry.feature.Attributes;
        }
        var mode = this.plotting ? 'Edit' : 'View';

        linkParams.mapShouldResume = true; //the map should resume its current state when the attributes page is closed.
        $("body").pagecontainer("change", '#mapAttributes' + mode);
    },
    updateAttributes: function(attributes){
        if (!this.currentGeometry[this.selectedIndex].feature) this.currentGeometry[this.selectedIndex].feature = {};
        this.currentGeometry[this.selectedIndex].feature.Attributes = attributes;
    },
    deleteFeature: function(graphic){
        for (var g = 0; g < this.currentGeometry.length; g++){
            if (graphic.geometry === this.currentGeometry[g]){
                this.map.graphics.remove(graphic);
                this.currentGeometry.splice(g, 1);
                theSilentCartographer.editToolbar.deactivate();
                theSilentCartographer.$tools.off().hide();
            }
        }
    },
    duplicateFeature: function(graphic){
        if (!graphic || !graphic.geometry) return;

        this.duplicateWKT = this.getWKT(graphic.geometry);
        this.duplicateFeatures = graphic.geometry.feature;
        var $tools = this.page.find('#mapToolMore');
        $tools.find('div.Tool').hide();
        $tools.find("div.Tool[data-wkt=" + graphic.geometry.WKTType + "]").show().collapsible('expand');
        $tools.popup('open');
        $tools.one('popupafterclose', function(){
            $tools.find('div.Tool').show();
        })
        this.editToolbar.deactivate()
    },
    activateEditControls: function(graphic) {
        var Edit = esri.toolbars.Edit;
        var tool = 0;
        if (graphic.geometry.WKTType === 'LINESTRING' || graphic.geometry.WKTType === 'POLYGON'){
            tool = tool | Edit.EDIT_VERTICES | Edit.MOVE;
        } else if (graphic.geometry.WKTType === 'CIRCLE'){
            tool = tool | Edit.MOVE | Edit.SCALE;
        } else if (graphic.geometry.WKTType === 'POINT'){
            tool = Edit.MOVE;
        }

        //specify toolbar options
        var options = {
            allowAddVertices: true,
            allowDeleteVertices: false,
            uniformScaling: true
        };
        this.editToolbar.activate(tool, graphic, options);
    },
    startPlotting: function(){
        this.currentGeometry = [];
//        this.map.graphics.clear();
        this.drawingLayer = this.plotting = this.creating = true;
        this.updateFooter();
        ViewUtil.selector.start({
            data: {},
            callbackOK: $.proxy(this.createFromGeometry, this),
            callbackCancel: $.proxy(this.stopPlotting, this),
            goBack: false
        })
    },
    clearMap: function(){
        this.currentGeometry = [];
        if (this.map){
			if (this.geoLocate.tracking) {
				this.geoLocate.locate();
			}
			if (this.geoLocate.highlightGraphic) {
				this.geoLocate.clear();
			}
            if (this.map.graphics) {
			    this.map.graphics.clear();
			}
        }
        if (this.draw){
            this.draw.deactivate();
        }
        if (this.editToolbar) {
            this.editToolbar.deactivate();
        }
        if (this.$tools){
            this.$tools.off().hide();
        }
        this.updateFooter();
    },
    createFromGeometry: function(){
        linkParams.geometry = this.getCurrentGeometry();
        var nextPage = OCA.IncidentManager
            ? '#mapPlotType' //emergency pack installed, user picks between assets, events, reports and tasks
            : '#taskNew';    //core only, user can only create tasks
        $("body").pagecontainer("change", nextPage);
    },
    createFromSession: function(locations){
        var wkt;
        if (this.currentTool == 'POLYGON'){
            wkt = 'POLYGON((';
            locations.push(locations[0]); //polygon needs to return to the origin
        } else if (this.currentTool == 'POINT'){
            wkt = 'POINT(';
        } else if (this.currentTool == 'CIRCLE'){
            wkt = 'CIRCLE(';
            var edge = locations[0]; //offset the edge at a reasonable distance.
            edge.longitude += 0.003; //in the context, user should be quite zoomed in
            edge.latitude  += 0.003;
            locations.push(edge);
        } else {
            wkt = 'LINESTRING(';
        }
        var pts = [];
        for (var l = 0; l < locations.length; l++){
            pts.push(locations[l].longitude + " " + locations[l].latitude);
        }
        wkt += pts.join(',');

        wkt += ")";
        if (this.currentTool == 'POLYGON'){
            wkt += ')';
        }
//        console.log('create ', locations, wkt);
        linkParams.mapShouldResume = true;
        this.displayWKT(wkt, this.currentFeature);
        this.updateFooter();
        setTimeout(function () {
            theSilentCartographer.fitGraphics();
        }, 1000);
        this.currentTool = this.currentFeature = null;
    },
    stopPlotting: function(){
        this.creating = false;
        this.plotting = false;
        this.clearMap();
        util.infobarClear();
        this.$tools
            .empty()
            .off()
            .hide();
    },
    getCurrentGeometry: function(){
        if (this.currentGeometry.length === 0){
            return null;
        }

        var wkt = '';
        var attributes = {};
        var fields = {};

        var geometry = [];

        for (var g = 0; g < this.currentGeometry.length; g++){
            if (this.currentGeometry[g].params && this.currentGeometry[g].params.field){
                fields[this.currentGeometry[g].params.field] = this.getLocationFieldData(this.currentGeometry[g]);
            } else {
                geometry.push(this.currentGeometry[g]);
            }
        }

        if (geometry.length === 0){
            wkt = null;
        } else if (geometry.length === 1){
            wkt = this.getWKT(geometry[0]);
            if (geometry[0].feature && geometry[0].feature.Attributes && geometry[0].feature.Attributes.length)
                attributes['0'] = geometry[0].feature.Attributes;
        } else {
            wkt = "GEOMETRYCOLLECTION(";
            var collection = [];
            for (var i = 0; i < geometry.length; i++){
                collection.push(this.getWKT(geometry[i]));
                if (geometry[i].feature && geometry[i].feature.Attributes && (geometry[i].feature.Attributes.length || !$.isEmptyObject(geometry[i].feature.Attributes))){
                    if (geometry[i].feature.Attributes.length){
                        attributes[i] = geometry[i].feature.Attributes;
                    } else {
                        attributes[i] = [geometry[i].feature.Attributes];
                    }
                }

            }
            wkt += collection.join(",");
            wkt += ")";
        }
        var val = {data: {WKT: wkt, Attributes: attributes}, restorableGeometry: this.currentGeometry, locationFields: fields};
        if (wkt === null) val.data = null;
        return val;
    },
    getLocationFieldData: function(geo){
        if (geo.WKTType !== 'POINT') return; //this is only for location fields, which should only be points.

        if (geo.location){ //some reverse geo-coding has occurred! return the new data
            return geo.location;
        } else {
            return {
                Lat: geo.getLatitude(),
                Lng: geo.getLongitude()
            };
        }
    },
    getGeometry: function(wkt){
        var m;
        var geo;
        if (m = /^POINT\s*\(([0-9.-]+ +[0-9.-]+)\)$/.exec(wkt)) {
            var bits = m[1].split(' ');
            geo = new esri.geometry.Point(bits[0], bits[1]); //lng, lat
            geo = esri.geometry.geographicToWebMercator(geo);
            geo.WKTType = 'POINT';

        } else if (m = /^LINESTRING\s*\((([0-9.-]+ +[0-9.-]+)( *, *[0-9.-]+ +[0-9.-]+)*)\)$/.exec(wkt)) {
            var p = m[1].split(/ *, */);
            var points = [];
            for (var i = 0; i < p.length; i++) points.push(p[i].split(' '));
            geo = new esri.geometry.Polyline(points);
            geo = esri.geometry.geographicToWebMercator(geo);
            geo.WKTType = 'LINESTRING';
        } else if (m = /^POLYGON\s*\((( *?\,? *\((([0-9.-]+ +[0-9.-]+)( *, *[0-9.-]+ +[0-9.-]+)*)\))+)\)$/.exec(wkt)) {
            //Cannot use capturing as the polygon could contain multiple "rings"
            var p = m[1].slice(1,m[1].length-1); //Remove the first and last character
            var ringBits = p.split(/\) *, *\(/);
            var rings = [];
            for (var i = 0; i < ringBits.length; i++){
                var p = ringBits[i].split(/ *, */);
                rings[i] = [];
                for (var x = 0; x < p.length; x++){
                    rings[i][x] = p[x].split(' ');
                }
            }
            geo = new esri.geometry.Polygon(rings);
            geo = esri.geometry.geographicToWebMercator(geo);
            geo.WKTType = 'POLYGON';
        } else if (m = /^CIRCLE\s*\(([0-9.-]+ +[0-9.-]+) *, *([0-9.-]+ +[0-9.-]+)\)$/.exec(wkt)) {
            var center = new esri.geometry.Point(m[1].split(' '));
            center = esri.geometry.geographicToWebMercator(center);
            var edge   = new esri.geometry.Point(m[2].split(' '));
            edge = esri.geometry.geographicToWebMercator(edge);
            var radius = esri.geometry.getLength(center, edge);
            var geo = new esri.geometry.Circle(center, {
                radius: radius,
                radiusUnit: esri.Units.METERS,
                geodesic: false
            });
            geo.WKTType = 'CIRCLE';
        }
        return geo;
    },
    getWKT: function(geo){
        if (!geo.WKTType && geo.type){
            switch (geo.type){
                case 'polygon'  : geo.WKTType = 'POLYGON';    break;
                case 'point'    : geo.WKTType = 'POINT';      break;
                case 'line'     : geo.WKTType = 'LINESTRING'; break;
            }
        }
        if (!geo.WKTType){
            console.error('no WKTType type, return null');
            return null;
        }
        var wkt = geo.WKTType + '(';

        function wktPt(geometry, reference){
            if (reference) geometry = new esri.geometry.Point(geometry, reference);
            return geometry.getLongitude() + " " + geometry.getLatitude();
        }

        switch (geo.WKTType){
            case 'POINT':
                wkt += wktPt(geo);
                break;
            case 'LINESTRING':
                var pts = [];
                for(var l = 0; l < geo.paths[0].length; l++) pts.push(wktPt(geo.paths[0][l], geo.spatialReference));
                wkt += pts.join(",");
                break;
            case 'CIRCLE':
                var edge = new esri.geometry.Point(geo.rings[0][0], geo.spatialReference);
                var center = geo.getExtent().getCenter();
                wkt += wktPt(center) + "," + wktPt(edge);
                break;
            case 'POLYGON':
                var rings = [];
                for (var r = 0; r < geo.rings.length; r++){
                    var points = [];
                    for (var p = 0; p < geo.rings[r].length; p++){
                        points.push(wktPt(geo.rings[r][p], geo.spatialReference));
                    }
                    rings.push('(' + points.join(',') + ')');
                }
                wkt += rings.join(',')
                break;
        }
        wkt += ")";
        return wkt;
    },

    /** Init */
	init: function(page){
		this.page = page;
		this.content = this.page.find('.ui-content');
        this.footer = this.page.find('.ui-footer');

        this.$plot = this.footer.find('#mapPlot');
        this.plotMode = false;
        this.page.find('.selector-mode').showIf(this.plotMode);
        this.page.find('.ui-footer.normal-mode').showIf(!this.plotMode);
        this.$plot.click($.proxy(this.startPlotting, this, true));

        this.footer.find('#mapClear').click($.proxy(this.clearMap, this));

        this.$tools = this.page.find('#tools').hide();

        new Gopher({url: '/symbology/features', dontProcessError:true}, $.proxy(this.gotFeatures, this), $.proxy(this.noFeatures, this)).run();
    },
    noFeatures: function(){
        this.footer.hide();
    },
    gotFeatures: function(data) {
        this.symbologyFeatures = data;
        if (!this.restrictedSymbology) { //if the map is first loaded with restricted symbology, dont clobber it with the full list
            this.renderPlotTools(this.symbologyFeatures);
        }
    },
    /* reset the plot tools to the full list fetched from /symbology/features */
    resetSymbologyFeatures: function(){
        if (this.restrictedSymbology){
            //only re-render the tools popup if they are currently restricted
            this.restrictedSymbology = false;
            this.renderPlotTools(this.symbologyFeatures);
        }
    },
    /* restrict the plot tools to a subset of symbology features provided by an object type */
    restrictSymbologyFeatures: function(data){
        this.restrictedSymbology = true;
        this.renderPlotTools(data);
    },
    checkAutoSelectPlot: function(){
        if (this.restrictedSymbology && (Object.keys(this.symbologyFeaturesIndex).length == 1) && !this.currentGeometry.length){
            this.page.find('.Tool ul li a').trigger('tap');
        }
    },
    /* render a list of feature symbologies to a set of plot tools */
    renderPlotTools: function(data){
        var cpt = JSON.stringify(data.map(function(d){ return d.id; })); //create a hash of the tools data
        if (this.currentPlotTools == cpt) { return; }                    //and if its the same as the current tools, do nothing
        this.currentPlotTools = cpt;

        this.symbologyFeaturesIndex = {};
        this.page.find('.Tool ul').empty(); //clear any existing tools

        var types = {
            "Point":   {tool: "POINT",    ul: this.page.find('.Point.Tool   ul')},
            "Line":    {tool: "POLYLINE", ul: this.page.find('.Line.Tool    ul')},
            "Circle":  {tool: "CIRCLE",   ul: this.page.find('.Circle.Tool  ul')},
            "Polygon": {tool: "POLYGON",  ul: this.page.find('.Polygon.Tool ul')}
        };

        var $popup = this.page.find('#mapToolMore');
        $popup.find('h2').off('click.repos').on('click.repos', function(){
            $popup.popup('reposition', {positionTo: '#openMapToolMore'});
        });
        for (var i = 0; i < data.length; i++){
            var f = data[i];
            f.Attributes = f.DefaultAttributes; //apply default attributes to all features.
            //make this feature able to be looked up by its attributes
            for (var a = 0; a < f.Attributes.length; a++){
                this.symbologyFeaturesIndex[this.getAttributeKey(f.Attributes[a])] = f;
            }
            var type = types[f.FeatureType];
            $("<li><a>" + f.Name + "</a></li>").on('tap', $.proxy(this.drawStart, this, type.tool, f, $popup)).appendTo(type.ul);
        }
        this.page.find('.Tool').show();     //by default, all sections show
        this.page.find('.Tool ul').each(function(i,e) {
            var ul = $(e);
            if (ul.children().length) {     //if a child menu has items, refresh the listview
                ul.listview('refresh');
                ul.parents('.Tool').addClass('ActiveTool'); //setting classes explicitly for better unit testing. otherwise, ':visible' would be an acceptable selector. this is probably more performant too
            } else {                        //else, hide the whole section
                ul.parents('.Tool').removeClass('ActiveTool').hide();
            }
        });
        if(this.page.find('.Tool.ActiveTool').length == 1){ //only tools of one type exist
            this.page.find('.Tool.ActiveTool').collapsible('expand');
        }
    },
    getAttributeKey: function(att){
        return att.FeatureKey + att.FeatureType + att.FeatureValue;
    },
    loadFeaturesFromAttributes: function(attributes){
        if (!this.symbologyFeaturesIndex) {
            return [];
        }
        if (attributes[0] && $.isArray(attributes[0])) attributes = attributes[0]; //api might return array in array.

        for (var a = 0; a < attributes.length; a++){
            var attKey = this.getAttributeKey(attributes[a]);
            if (this.symbologyFeaturesIndex[attKey]){
                var matched = $.extend({}, this.symbologyFeaturesIndex[attKey]);
                matched.Attributes = attributes; //overwrite with any additions to the defaults
                return [matched];
            }
        }
    },
    loadMap: function(coords){
        
        if (OCA.Settings.CFG_GMAP_LONGITUDE && OCA.Settings.CFG_GMAP_LATITUDE){
            this.center = new esri.geometry.Point(OCA.Settings.CFG_GMAP_LONGITUDE, OCA.Settings.CFG_GMAP_LATITUDE);
        }
        else if (coords && coords.latitude && coords.longitude){
            this.center = new esri.geometry.Point(coords.longitude, coords.latitude);
        } else {
            this.center = new esri.geometry.Point(149.133228, -35.268543);
        }

        if (OCA.Settings.CFG_GMAP_ZOOM){
             this.zoom = Math.round(OCA.Settings.CFG_GMAP_ZOOM); //bad config might have a float.
         } else {
             this.zoom = this.DEFAULT_ZOOM;
         }

        this.basemap = 'streets';
        this.mapPositionTime = Date.now();

        dojo.extend(esri.layers.ArcGISTiledMapServiceLayer, {
            getTileUrl: function(zoom, row, col, img){
                var url = this.url + "/tile/" + zoom + "/" + row + "/" + col;
                var urlKey = url.replace('http://services.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile','WSM');
				//TODO http or https?
//                if (localStorage[urlKey]){
//                    console.log('returning cached tile for ' + urlKey);
//                    return localStorage[urlKey];
//                }
//
//                new Gopher({url: url, mode: "image"}, function(data){
//                    console.log(urlKey, data);
//                    var arr = new Uint8Array(data);
//                    var raw = String.fromCharCode.apply(null,arr);
//                    var b64 = window.btoa(raw);
//                    var dataUri = "data:image/jpeg;base64,"+b64;
//                    var dataStr = dataUri.substr(0, 100);
//                    console.log('convert', dataStr, dataUri, b64, raw, arr);
//                    localStorage[urlKey] = data;
//                }).run();
//                console.log('get tile url TMSL', url);

                return url;
            }
        });

        dojo.extend(esri.layers.WebTiledLayer, {
            getTileUrl: function(zoom, row, col, img){
                var url = this.url + "?x=" + col + "&y=" + row + "&z=" + zoom;
                //fetch the static tiles from the API via gophers for caching
                new Gopher({url: url, mode: "text", dontProcessError:true, backgroundMode:true}, (function(){
					var imag = img;
					return function(data) {
						if (!imag) {
							console.log('No img tag!');
							return;
						}
						imag.src = "data:image/png;base64," + data;
					}
                })()).run();

                return "";
            }
        });
        dojo.extend(esri.layers.GeoRSSLayer, { //force http for phones, let the mobile interface use https if it wants. this feature clearly not designed for cordova
            serviceUrl:
                ((location.protocol == 'file:')
                    ? 'https:'
                    : location.protocol
                ) + "//utility.arcgis.com/sharing/rss"
        });

        var $canvas = $('#mapCanvas');
        var header = (OCA.$header) ? OCA.$header.height() : 47;
        $canvas.height($(document).height() - header - 5);

		//Disabling the zoom animation as this causes the ArcGIS library to completely die if tracking is enabled during a big zoom.
        esri.config.defaults.map.zoomDuration = 0;
        this.map = new esri.Map("mapCanvas", {
            center: this.center,
            zoom:   this.zoom,
            basemap:this.basemap,
            logo: false,
            autoResize: false
        });

        var self = this;
        this.map.on("load", function(){
            self.mapLoaded = true;
            self.draw = new esri.toolbars.Draw(self.map);
            self.draw.on('draw-end', $.proxy(self.drawEnd, self));
            self.editToolbar = new esri.toolbars.Edit(self.map, {uniformScaling: true});
            self.handleLink();
            //icon click handlers
            self.map.graphics.on('click', function(evt) {
                console.log('graphics click', evt, self.currentTool);
                if (self.currentTool || !evt.graphic) return;
                evt.preventDefault();
                evt.stopPropagation();
                var g = evt.graphic;
                self.map.infoWindow.hide();

                if (self.plotting && g.geometry.drawing){
                    self.editToolbar.deactivate();
                    self.activateEditControls(g);
                    //show buttons if the graphic is in plotting mode and not linked to a location field
                    self.$tools
                        .empty()
                        .off()
                        .hide();
                    if (!(g.geometry.params && g.geometry.params.field)){
                        self.$tools
                            .append(ViewUtil.btn('delete', OCA.getI18n().gettext('Delete item')))
                            .on('click', 'a.delete', function(){
                                self.deleteFeature(g);
                            })
                            .append(ViewUtil.btn('duplicate', OCA.getI18n().gettext('Duplicate')))
                            .on('click', 'a.duplicate', function(){
                                self.duplicateFeature(g);
                            });
                        if (OCA.versionAtLeast('1.6.17')){ //code for saving attributes required API change in 1.6.18
                            self.$tools.append(ViewUtil.btn('attributes', OCA.getI18n().gettext('Edit attributes')))
                                .on('click', 'a.attributes', function(){
                                    self.handleAttributesTool(g.geometry);
                                });
                        }
                        self.$tools.show();
                    }
                } else {
                    self.$tools.empty().off();
                    if (g.geometry){
                        if (g.geometry.tool){
                            var tool = g.geometry.tool;
                            if (tool[0]) tool = tool[0];
                            if (tool.signal && tool.signal.substr(0,4) === 'view'){
                                self.$tools
                                    .append(ViewUtil.btn('view', tool.name))
                                    .on('click', 'a.view', function(){
                                        self.handleViewTool(tool);
                                    })
                                    .show();
                            }
                        }
                        if (g.geometry.feature && g.geometry.feature.Attributes && g.geometry.feature.Attributes.length){
                            self.$tools
                                .append(ViewUtil.btn('attributes', OCA.getI18n().gettext('View attributes')))
                                .on('click', 'a.attributes', function(){
                                    self.handleAttributesTool(g.geometry);
                                })
                                .show();
                        }
                    }
                }
            });
            self.map.on("click", function(evt){
                if (self.plotting){
                    self.editToolbar.deactivate();
                } else {
//                    console.log('click on map while not plotting')
                }
                self.$tools.off().hide();
            });
            var currentLength, currentIndex;
            self.editToolbar.on('activate', function(evt){
               currentIndex = self.currentGeometry.indexOf(evt.graphic.geometry);
               currentLength = self.currentGeometry.length;
            });
            var updateGeometry = function(geo){
                var old = self.currentGeometry[currentIndex];
                geo.drawing = old.drawing;
                geo.feature = old.feature;
                geo.WKTType = old.WKTType;
                geo.params  = old.params;
                geo.symbol  = old.symbol;
                self.currentGeometry[currentIndex] = geo;

                if (geo.WKTType === 'POINT' && geo.params && geo.params.field && OCA.Settings.ReverseGeocodeTiedMarker !== false){  //a point, able to be reverse geocoded
                    if (geo.x != old.x || geo.y != old.y){                                                                          //and the point has moved
                        var locator = new esri.tasks.Locator(self.ARCGIS_GEOCODE);
                        locator.outSpatialReference = self.map.spatialReference;
                        locator.locationToAddress(geo, 100, function(candidate){
                            if (candidate.score > 80){
                                var a = candidate.address;
                                geo.location = {
                                    Country: a.CountryCode,
                                    State: a.Region,
                                    Suburb: a.City,
                                    Postcode: a.Postal,
                                    StreetName: a.Address,
                                    StreetNumber: '',
                                    Lat: geo.getLatitude(),
                                    Lng: geo.getLongitude()
                                }
                            }
                        });
                    }
                }
            }
            self.editToolbar.on('deactivate', function(evt){
                if (self.currentGeometry.length < currentLength){
                    //deletion do nothing
                } else {
                    //update current geometry array with the new edited geometry item
                    updateGeometry(evt.graphic.geometry);
                }
                currentLength = currentIndex = null;
            });
            self.editToolbar.on('vertex-move-stop, scale-stop, graphic-move-stop, graphic-click', function(evt){
                updateGeometry(evt.graphic.geometry);
            });
        });

        $(window).off('infobarResize orientationchange').on('infobarResize orientationchange', function(){
            if ($('body').pagecontainer('getActivePage').prop('id') === 'mapPage'){
//                console.log('infobar resizeing because the activty page');
                self.map.resize();
                self.map.reposition();
            }
        });

        $(document).on('pagebeforechange.mapPosition pause', function(){
            if (self.map && self.map.extent && $('body').pagecontainer('getActivePage').prop('id') === 'mapPage'){
                self.zoom = self.map.getZoom();
                self.center = esri.geometry.webMercatorToGeographic(self.map.extent.getCenter());
                self.mapPositionTime = Date.now();
            }
        });

        this.geoLocate = new esri.dijit.LocateButton({map: this.map, useTracking: true, setScale: false}, "locateButton");
        this.geoLocate.startup();
        //Location events zoom/scale the map according to the accuracy of the reading
        //I dont know exactly what units that 'scale' refers to, but 1000 (actually zoom 19, scale 1100) shows about half a block
        //and using the accuracy of the location reading (which might be 20 or less for accurate GPS) zooms in too far to be useful
        //override the built-in method to make sure the scale is always reasonable
        var getScale = this.geoLocate._getScale;
        this.geoLocate._getScale = function(a){
            return Math.max(getScale.call(this.geoLocate, a), 1000);
        }.bind(this);

        //if the user pans so that their position graphic is no longer on screen, stop tracking
        //MUST listen to swipe or mouse events for this - pan-end fires in many situations including location updates
		this.map.on('mouse-drag-end, swipe-end', function(){
			if (this.geoLocate.tracking && this.geoLocate.highlightGraphic && !this.map.extent.contains(this.geoLocate.highlightGraphic.geometry)) {
				this.geoLocate.locate(); //toggles tracking to off.
			}
		}.bind(this));
		$(document).on('pagebeforechange', function(){
			if (this.geoLocate.tracking) {
			    this.geoLocate.locate();
            }
            if (this.geoLocate.highlightGraphic) {
			    this.geoLocate.clear();
            }
		}.bind(this));
    },


    drawStart: function(tool, feature, $popup, e){
        if (e){
            e.preventDefault();
            e.stopPropagation();
        }
        if ($popup) $popup.popup('close');
        if (this.duplicateFeatures){
            feature = $.extend({}, this.duplicateFeatures, feature);
        }

        //if an polyline/gon has been part drawn and the user chooses another tool
        if (this.currentTool && this.draw){
            this.draw.finishDrawing();
        }
        var Line = esri.symbol.CartographicLineSymbol; //shortcut
        var Fill = esri.symbol.SimpleFillSymbol;
        var Icon = esri.symbol.PictureMarkerSymbol;

        if (feature.StrokeWidth && feature.StrokeColour)
            this.currentLineSymbol = new Line(Line.STYLE_SOLID, new dojo.Color('#' + feature.StrokeColour), feature.StrokeWidth, Line.CAP_ROUND, Line.JOIN_MITER, 10);
        if (feature.FillColour){
            this.currentFillSymbol = new Fill(Fill.STYLE_SOLID, null, this.getDojoColor(feature.FillColour, 0.5));
            this.currentPointSymbol = new Icon(Configuration.getAPIDomain() + '/pkg/xhtml_default_map/point.php?rgb='+feature.FillColour, 34, 34)
                .setOffset(4, 17);
        }
        this.currentTool = tool;
        this.currentFeature = feature;

        if (this.duplicateWKT){
            var geometry = this.getGeometry(this.duplicateWKT);
            //already have everything we need, go straight to draw end
            this.drawEnd({geometry: geometry});
            return;
        }

        this.draw.activate(esri.toolbars.Draw[tool]);
        var msg;
        var btnIcon = 'marker';
        var btnCallback = function(){
            $.mobile.loading('show');
            navigator.geolocation.getCurrentPosition(
                function(geo){
                    $.mobile.loading('hide');
                    theSilentCartographer.drawEnd();
                    theSilentCartographer.createFromSession([geo.coords]);
            },  function(fail){
                    $.mobile.loading('hide');
                    util.alertDialog(OCA.getI18n().gettext('Unable to determine position'), jQuery.noop, OCA.getI18n().gettext('Error'), OCA.getI18n().gettext('Ok'));
            },  {timeout: 5000});
        };
        var historyURL = 'locationHistory?selector=true';
        switch (this.currentTool){
            case 'POINT':
                msg = OCA.getI18n().gettext('Tap to place a point');
                break;
            case 'LINE':
            case 'POLYLINE':
            case 'POLYGON':
                msg = OCA.getI18n().gettext('Tap to place a point. Double tap to place the end point');
                btnCallback = function(){
                    ViewUtil.selector.start({
                        data: {},
                        callbackOK: $.proxy(theSilentCartographer.createFromSession, theSilentCartographer),
                        callbackCancel: $.noop,
                        makeBackup: true
                    });
                    ViewUtil.selector.test = "poly";
                    $("body").pagecontainer("change", '#' + historyURL);
                };
                btnIcon = 'tracking_map';
                if (device.platform == "Mobile Interface"){
                    btnIcon = false; //shouldnt be able to select tracking in the mobile interface
                }
                break;
            case 'CIRCLE':
                msg = OCA.getI18n().gettext('Tap to place the centre then drag the radius out');
                break;
        }
        util.infobar(msg, false, false, btnIcon, btnCallback);

        //if a page navigation happens while drawing, treat it as user cancellinwg behaviour
        var self = this;
        $(document).one('pagebeforechange.mapdrawing', function(event, navObj){
            self.drawEnd();
            if (navObj.options.role != 'popup' && navObj.options.dataUrl != historyURL){ //dont do this for the tools popup, or when plotting from location history
                console.log('page change map drawing stop plotting', arguments);
                self.stopPlotting();
            }
        });

    },
    drawEnd: function(e){
//        console.log('draw end', e);
        this.map.showZoomSlider();
        this.draw.deactivate();
        this.$tools.off().hide();
        util.infobarClear();
        $(document).off('.mapdrawing');
        if (e && e.geometry){
            e.geometry.drawing = true;
            e.geometry.WKTType = this.currentTool;
            var label = false;
            //noinspection FallThroughInSwitchStatementJS
			switch (this.currentTool){
                case 'POINT':
                    this.displayPoint(e.geometry, this.currentFeature);
                    break;
                case 'LINE':
                case 'POLYLINE':
                    e.geometry.WKTType = 'LINESTRING';
                    this.displayLine(e.geometry, this.currentFeature);
                    break;
                case 'CIRCLE':
                    label = true;
                case 'POLYGON':
                    this.displayPolygon(e.geometry, this.currentFeature, label);
                    break;

            }
            var cf = this.currentFeature;
            var self = this;
            setTimeout(function(){
                self.handleObjectLinks(cf);
            },500);
            this.currentTool = this.currentFeature = this.duplicateFeatures = this.duplicateWKT = null;
        }
        this.updateFooter();
    },
    handleObjectLinks: function(currentFeature){
        //nothing to handle unless we're in creation mode with a feature which has object links
        if (!this.creating || !currentFeature.ObjectLinks || !currentFeature.ObjectLinks.length) return;

        linkParams.geometry = this.getCurrentGeometry();
        var links = currentFeature.ObjectLinks;
        this.navigateObjectLinks(links);
    },
    navigateObjectLinks: function(links){
        if (links.length === 1){
            var page = this.getMobilePage(links[0]);
            $("body").pagecontainer("change", page);
        } else {
            this.currentLinks = links;
            $("body").pagecontainer("change", "#mapPlotShortcut");
        }
    },
    handleLayerObjectLinks: function(layerData, selectedGraphic){
        linkParams.geometry = {};
        console.log('handle layer object link', layerData, selectedGraphic);

        var wkt = this.getWKT(selectedGraphic.geometry);

        var convertedAttributes = []; //convert attributes from a hash to the expected OCA format. make best guesses about the field types
        for (var key in selectedGraphic.attributes){
            var value = selectedGraphic.attributes[key];
            var type;
            if (!isNaN(value) && value){
                type = 'decimal'; //is set to number, thus decimal
            } else if (!isNaN(Date.parse(value)) && value){
                type = 'datetime'; //string that parses as date
            } else {
                type = 'string'; //fallback
            }
            if (value === null || value === undefined){
                value = ''; //cant be null in OCA
            }
            convertedAttributes.push({
                FeatureKey: key,
                FeatureTypeField: type,
                FeatureValue: value
            });
        }

        if (wkt){
            linkParams.geometry = {
                data: {
                    WKT: wkt,
                    Attributes: {0: convertedAttributes}
                },
                restorableGeometry: [selectedGraphic.geometry],
                locationFields: null
            };
            
            this.navigateObjectLinks(layerData.ObjectLinks);
        }
    },
    getMobilePage: function(link){
        return "#" + link['Type'] + "New?type=" + link['TypeID'];
    },
    findAddress: function(address, move, symbol){
        if (move === undefined) move = true;
        if (!symbol){
            symbol = new esri.symbol.SimpleMarkerSymbol()
                .setPath("M16,3.5c-4.142,0-7.5,3.358-7.5,7.5c0,4.143,7.5,18.121,7.5,18.121S23.5,15.143,23.5,11C23.5,6.858,20.143,3.5,16,3.5z M16,14.584c-1.979,0-3.584-1.604-3.584-3.584S14.021,7.416,16,7.416S19.584,9.021,19.584,11S17.979,14.584,16,14.584z")
                .setSize(20)
                .setOffset(0,18);
        }

        var locator = new esri.tasks.Locator(this.ARCGIS_GEOCODE);
        locator.outSpatialReference = this.map.spatialReference;
        locator.addressToLocations({
            address: {
                SingleLine: address
            },
            outFields: ["Loc_name"]
        }, $.proxy(this.locatorResults, this, move, symbol));
    },
    externalGeocode: function(address, callback){
        var locator = new esri.tasks.Locator(this.ARCGIS_GEOCODE);
        locator.outSpatialReference = new esri.SpatialReference(102100);
        locator.addressToLocations({
            address: {
                SingleLine: address
            },
            outFields: ["Loc_name"]
        }, $.proxy(this.externalGeocodeResults, this, callback));
    },
    locatorResults: function(move, symbol, data){
        var match;
        var matchScore = 80;
        for (var i = 0; i < data.length; i++){
            var result = data[i];
            if (result.score > matchScore){
                match = result;
                matchScore = result.score;
            }
        }
        if (match){
            this.currentPointSymbol = symbol;
            var point = new esri.geometry.Point(match.location.x, match.location.y, match.location.spatialReference);
            point.WKTType = 'POINT';
            this.displayPoint(point);
            //move map
            if (move) this.centerAndZoom(geometry, this.DEFAULT_ZOOM);
        }
    },
    externalGeocodeResults: function(callback, data){
        var match;
        var matchScore = 80;
        for (var i = 0; i < data.length; i++){
            var result = data[i];
            if (result.score > matchScore){
                match = result;
                matchScore = result.score;
            }
        }
        if (match){
            callback(match);
        }
    },
    displayAddress: function(addressData, move, feature){
        if (move === undefined) move = true;
        var geometry = new esri.geometry.Point(addressData.Lng, addressData.Lat);
        geometry = esri.geometry.geographicToWebMercator(geometry);
        geometry.WKTType = 'POINT';
        this.displayPoint(geometry, feature);
        //TODO: add text?

        //move map
        if (move) this.centerAndZoom(geometry, this.DEFAULT_ZOOM);
        return geometry;
    },
    displayPoint: function(geometry, feature){
        geometry.WKTType = 'POINT';
        geometry.feature = feature;
        if (this.drawingLayer) this.currentGeometry.push(geometry);
        var symbol = this.currentPointSymbol;

        if (feature && feature.SymbolSrc){
            if (!symbol) symbol = this.defaultPointSymbol;
            //override default symbol with new url. same icon size and offset.
            symbol = new esri.symbol.PictureMarkerSymbol(Configuration.getAPIDomain() + feature.SymbolSrc,symbol.width, symbol.height).setOffset(symbol.xoffset, symbol.yoffset);
        }

        if (!symbol){
            if (geometry.symbol) {
                symbol = geometry.symbol; //geometry should be restored with the correct data
            } else {
                symbol = new esri.symbol.SimpleMarkerSymbol()
                    .setPath("M16,3.5c-4.142,0-7.5,3.358-7.5,7.5c0,4.143,7.5,18.121,7.5,18.121S23.5,15.143,23.5,11C23.5,6.858,20.143,3.5,16,3.5z M16,14.584c-1.979,0-3.584-1.604-3.584-3.584S14.021,7.416,16,7.416S19.584,9.021,19.584,11S17.979,14.584,16,14.584z")
                    .setSize(20)
                    .setOffset(0,18);
            }
        }
        geometry.symbol = symbol;
        var graphic = new esri.Graphic(geometry, symbol);
        this.map.graphics.add(graphic);
    },
    displayLine: function(geometry, feature){
//        console.log('display line!', geometry, feature);
        geometry.feature = feature;
        if (this.drawingLayer) this.currentGeometry.push(geometry);
        var symbol = this.currentLineSymbol || new esri.symbol.SimpleLineSymbol();
        if (feature && feature.StrokeColour && feature.StrokeWidth){
            var Line = esri.symbol.CartographicLineSymbol
            symbol = new Line(this.getStrokeStyle(feature.StrokeStyle), new dojo.Color('#' + feature.StrokeColour), feature.StrokeWidth, Line.CAP_ROUND, Line.JOIN_MITER, 10);
        }
        var graphic = new esri.Graphic(geometry, symbol);
        this.map.graphics.add(graphic);
    },
    displayPolygon: function(geometry, feature){
//        console.log('display polygon', geometry, feature);
        geometry.feature = feature;
        if (this.drawingLayer) this.currentGeometry.push(geometry);
        var symbol = this.currentFillSymbol || new esri.symbol.SimpleFillSymbol();
        if (feature && feature.FillStyle && feature.FillColour && feature.FillOpacity){
            symbol = new esri.symbol.SimpleFillSymbol(
                this.getFillStyle(feature.FillStyle),
                null, /* no outline */
                this.getDojoColor(feature.FillColour, feature.FillOpacity)
            );
            if (feature.StrokeStyle && feature.StrokeWidth) {
                symbol.setOutline(new esri.symbol.SimpleLineSymbol(
                    this.getStrokeStyle(feature.StrokeStyle),
                    new dojo.Color('#' + feature.StrokeColour),
                    feature.StrokeWidth));
            }
        }
        var graphic = new esri.Graphic(geometry, symbol);
        this.map.graphics.add(graphic);
    },
    getDojoColor: function(hex, opacity){
        hex = hex || '000000';
        if (hex.indexOf('#') !== 0) hex = '#' + hex;
        var color = new dojo.Color(hex);
        if (opacity){
            opacity = parseFloat(opacity,10);
            if (opacity > 1) opacity /= 100; //convert to %
            var rgba = color.toRgba();
            rgba[3] = opacity;
            color = new dojo.Color(rgba);
        }
        return color;
    },
    getFillStyle: function(style) {

        var fillMap = {
            1 : esri.symbol.SimpleFillSymbol.STYLE_SOLID,
            2 : esri.symbol.SimpleFillSymbol.STYLE_BACKWARDDIAGONAL,
            3 : esri.symbol.SimpleFillSymbol.STYLE_CROSS,
            4 : esri.symbol.SimpleFillSymbol.STYLE_FORWARDDIAGONAL,
            5 : esri.symbol.SimpleFillSymbol.STYLE_HORIZONTAL,
            6 : esri.symbol.SimpleFillSymbol.STYLE_VERTICAL
        };

        if (typeof fillMap[style] != 'undefined') {
            return fillMap[style];
        } else {
            return esri.symbol.CartographicLineSymbol.STYLE_SOLID;
        }
    },
    getStrokeStyle: function(style) {
        var strokeMap = {
            1 : esri.symbol.CartographicLineSymbol.STYLE_SOLID,
            2 : esri.symbol.CartographicLineSymbol.STYLE_DASH,
            3 : esri.symbol.CartographicLineSymbol.STYLE_DASHDOT,
            4 : esri.symbol.CartographicLineSymbol.STYLE_DASHDOTDOT,
            5 : esri.symbol.CartographicLineSymbol.STYLE_DOT,
            6 : esri.symbol.CartographicLineSymbol.STYLE_INSIDE_FRAME,
            7 : esri.symbol.CartographicLineSymbol.STYLE_LONGDASH,
            8 : esri.symbol.CartographicLineSymbol.STYLE_LONGDASHDOT,
            9 : esri.symbol.CartographicLineSymbol.STYLE_SHORTDASH,
            10 : esri.symbol.CartographicLineSymbol.STYLE_SHORTDASHDOT,
            11 : esri.symbol.CartographicLineSymbol.STYLE_SHORTDASHDOTDOT,
            12 : esri.symbol.CartographicLineSymbol.STYLE_SHORTDOT
        };

        if (typeof strokeMap[style] != 'undefined') {
            return strokeMap[style];
        } else {
            return esri.symbol.CartographicLineSymbol.STYLE_SOLID;
        }
    }
});

function MapAttributesView($page){
    this.initTypeView(null, $page);
    this.policies = [];
}
MapAttributesView.prototype = new TypeView;
MapAttributesView.prototype.constructor = MapAttributesView;
MapAttributesView.prototype.getData = function(){
    this.data = this.convertDataFromMap(theSilentCartographer.currentAttributes);
    this.getType();
    this.render();
}
MapAttributesView.prototype.getType = function(){
    this.typeData = {Fields: {
        Attributes: {
            Label: "Attributes",
            Type: "subform",
            SubFields: {
                FeatureKey:      {Label: "Key",   Type: "sgltxt",   Required: true},
                FeatureTypeField:{Label: "Type",  Type: "opt",      Options: [['string', 'String'], ['decimal', 'Decimal'], ['datetime', 'Date/Time']], DefaultValue: 'string'},
                textValue:       {Label: "Value", Type: "sgltxt",   VisibilityFields: {FeatureTypeField: ['string']}, Required: true},
                numberValue:     {Label: "Value", Type: "number",   VisibilityFields: {FeatureTypeField: ['decimal']}, Required: true},
                datetimeValue:   {Label: "Value", Type: "datetime", VisibilityFields: {FeatureTypeField: ['datetime']}, Required: true}
            }
        }
    }};
}
MapAttributesView.prototype.convertDataFromMap = function(attributes){
    //hack map data into type data format
    if (!attributes) attributes = [];
    if (attributes[0] && attributes[0][0]) attributes = attributes[0]; //fix double nested arrays
    for (var a = 0; a < attributes.length; a++){
        if (!attributes[a].FeatureTypeField){ //old API version. guess based on OCA constants
            if (attributes[a].FeatureType == '1')       attributes[a].FeatureTypeField = 'string';
            else if (attributes[a].FeatureType == '8')  attributes[a].FeatureTypeField = 'decimal';
            else if (attributes[a].FeatureType == '13') attributes[a].FeatureTypeField = 'datetime';
        }


        if (attributes[a].FeatureTypeField == 'string'  ) attributes[a].textValue     = attributes[a].FeatureValue;
        if (attributes[a].FeatureTypeField == 'decimal' ) attributes[a].numberValue   = attributes[a].FeatureValue;
        if (attributes[a].FeatureTypeField == 'datetime') attributes[a].datetimeValue = attributes[a].FeatureValue;
    }
    return {FieldData: {Attributes: attributes}};
}

function MapAttributesEdit($page){
    this.initTypeEdit(null, $page);
}
MapAttributesEdit.prototype = new TypeEdit;
MapAttributesEdit.prototype.constructor = MapAttributesEdit;
MapAttributesEdit.prototype.getData = MapAttributesView.prototype.getData;
MapAttributesEdit.prototype.getType = MapAttributesView.prototype.getType;
MapAttributesEdit.prototype.convertDataFromMap = MapAttributesView.prototype.convertDataFromMap
MapAttributesEdit.prototype.render = function(){ //dont show policies, relations, etc
    this.listview = $("<ul />");
    this.renderFields();
    this.content.append(this.listview);
    this.afterRender();
    this.listview.listview();
    $.mobile.loading('hide');
}
MapAttributesEdit.prototype.getSubmission = function(){
    var attributes = this.typeData.Fields.Attributes.Input.val();
    var submission = [];
    for (var a = 0; a < attributes.length; a++){
        submission[a] = {
            FeatureKey: attributes[a].FeatureKey,
            FeatureTypeField: attributes[a].FeatureTypeField
        };
        switch (attributes[a].FeatureTypeField){
            case 'string':   submission[a].FeatureValue = attributes[a].textValue;     break;
            case 'decimal':  submission[a].FeatureValue = attributes[a].numberValue;   break;
            case 'datetime': submission[a].FeatureValue = attributes[a].datetimeValue; break;
        }
    }
    return submission;
}
MapAttributesEdit.prototype.submission = function(submission){
    if (this.valid()){
        theSilentCartographer.updateAttributes(submission);
        util.goBack(); //return to map
    }
}
MapAttributesEdit.prototype.beforeRender = function(){
    this.footer.show();
}

