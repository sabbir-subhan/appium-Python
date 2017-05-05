router.add({
    "#riskMatrixView[?]id=(\\d+)$": function(type, match, ui, page, e){
        RiskController.getMatrix(match[1]);
    },
    "#riskMatrixView[?]id=(\\d+)&registerID=(\\d+)&contextID=(\\d+)": function(type, match, ui, page, e){
        RiskController.getMatrix(match[1], match[2], match[3]);
    },
    "#riskMatrixView[?]selector=true": function(type, match, ui, page, e){
        RiskController.getMatrixSelector();
    },
    "#risktypeIndex[?]selector=true&id=0": function(type, match, ui, page){
        RiskController.getTypes($(page));
    },
    "#riskRegisterIndex$": function(type,match, ui, page){
        RiskController.selectorMode = false;
        RiskController.getRegisters();
    },
    "#risklibraryTreeView[?]id=(\\d+)$": function(type, match, ui, page, e){
        RiskController.getLibrary($(page), 'risk', match[1]);
    },
    "#riskcontrollibraryTreeView[?]id=(\\d+)$": function(type, match, ui, page, e){
        RiskController.getLibrary($(page), 'riskcontrol', match[1])
    },
    "#risklibraryTreeView[?]id=(\\d+)&registerID=(\\d+)": function(type, match, ui, page, e){
        RiskController.getLibrary($(page), 'risk', match[1], match[2]);
    },
    "#riskcontrollibraryTreeView[?]id=(\\d+)&registerID=(\\d+)": function(type, match, ui, page, e){
        RiskController.getLibrary($(page), 'riskcontrol', match[1], match[2])
    },
    "#risklibraryTreeView[?]selector=true&id=(\\d+)": function(type, match, ui, page, e){
        RiskController.getLibraryRiskControls($(page), match[1]);
    },
    "#riskcontextTreeView[?]selector=true&id=(\\d+)": function(type, match, ui, page, e){
        RiskController.selectorMode = 'riskcontext'; //contexts mode gets confused when both selectable and parented, this is the backup route
        RiskController.renderListing(match[1]);
    },
    "#riskcontextTreeView[?]mode=(\\w+)&selector=true&id=(\\d+)": function(type, match, ui, page, e){
        RiskController.selectorMode = match[1];
        RiskController.renderListing(match[2]);
    },
    "#riskcontextTreeView[?]id=(\\d+)&registerID=(\\d+)$": function(type, match, ui, page, e){
        RiskController.selectorMode = false;
        RiskController.renderListing(match[1], match[2]);
    },
    "#riskcontextTreeView[?]id=(\\d+)&registerID=(\\d+)&matrixID=(\\d+)&xIndex=(\\d+)&yIndex=(\\d+)": function(type, match, ui, page, e){
        RiskController.getRisksFromCell(match[1], match[2], match[3], match[4], match[5], RiskController.currentRatingField);
    },
    "#riskcontrolIndex[?]mode=riskcontrol&selector=true&id=(\\d+)": function(type, match, ui, page, e){
        RiskController.selectorMode = true;
        RiskController.riskcontrolSelector(match[1]);
    },
    "#riskView[?]id=(\\d+)": function(type,match,ui,page,e){
        new RiskView(match[1], page).getData();
    },
    "#riskEdit[?]id=(\\d+)": function(type,match,ui,page,e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
        new RiskEdit(match[1], page).getData();
    },
    "#riskNew[?]parent=(\\d+)&register=(\\d+)$": function(type, match, ui, page, e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
        new RiskNew(match[1], page).getTypes(match[2]);
    },
    "#riskNew[?]parent=(\\d+)&register=(\\d+)&timestamp=(\\d+)": function(type, match, ui, page, e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
        new RiskNew(match[1], page).getNewCacheData(match[2]);
    },
    "#riskregisterView[?]id=(\\d+)": function(type,match,ui,page,e){
        new RiskRegisterView(match[1], page).getData();
    },
    "#riskregisterEdit[?]id=(\\d+)": function(type,match,ui,page,e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
        new RiskRegisterEdit(match[1], page).getData();
    },
    "#riskregisterNew$": function(type, match, ui, page, e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
        new RiskRegisterNew(page).getTypes();
    },
    "#riskregisterNew[?]timestamp=(\\d+)": function(type, match, ui, page, e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
        new RiskRegisterNew(page).getNewCacheData(match[1]);
    },
    "#riskcontextView[?]id=(\\d+)": function(type,match,ui,page,e){
        new RiskContextView(match[1], page).getData();
    },
    "#riskcontextEdit[?]id=(\\d+)": function(type,match,ui,page,e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
        new RiskContextEdit(match[1], page).getData();
    },
    "#riskcontextNew[?]parent=(\\d+)$": function(type, match, ui, page, e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
        new RiskContextNew(match[1], page).getTypes();
    },
    "#riskcontextNew[?]parent=(\\d+)&timestamp=(\\d+)": function(type, match, ui, page, e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
        new RiskContextNew(match[1], page).getNewCacheData(match[2]);
    },
    "#riskcontrolView[?]id=(\\d+)": function(type,match,ui,page,e){
        new RiskControlView(match[1], page).getData();
    },
    "#riskcontrolEdit[?]id=(\\d+)": function(type,match,ui,page,e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
        new RiskControlEdit(match[1], page).getData();
    },
    "#riskcontrolNew[?]parent=(\\d+)$": function(type, match, ui, page, e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
        new RiskControlNew(match[1], page).getTypes();
    },
    "#riskcontrolNew[?]parent=(\\d+)&timestamp=(\\d+)": function(type, match, ui, page, e){
        if (ViewUtil.selector.previousObject){
            ViewUtil.selector.previousObject = null;
            app.checkLoaded();
            return;
        }
        new RiskControlNew(match[1], page).getNewCacheData(match[2]);
    }
});
$(document).on("pageinit", "#riskMatrixView", function(e){
    RiskController.initMatrix(this);
});
$(document).on("pageinit", "#riskRegisterIndex", function(e){
    RiskController.init(this);
});
$(document).on("pageinit", "#riskcontextTreeView", function(e){
    RiskController.initContext(this);
});
$(document).on("pageinit", "#riskcontrolIndex", function(e){
    RiskController.initControlSelector(this);
});
var RiskController = $.extend({}, app, {
    selectorMode: false,
    ratingTypes: ["Inherent", "Residual", "Target"],
    Terminology: { //will be overwritten by API response
        "Risk":         {"Title":"Risk",            "Plural":"Risks",           "IndefiniteArticle":"a" },
        "Control":      {"Title":"Control",         "Plural":"Controls",        "IndefiniteArticle":"a" },
        "InherentRisk": {"Title":"Inherent risk",   "Plural":"Inherent risks",  "IndefiniteArticle":"an"},
        "ResidualRisk": {"Title":"Residual risk",   "Plural":"Residual risks",  "IndefiniteArticle":"a" },
        "TargetRisk":   {"Title":"Target risk",     "Plural":"Target risks",    "IndefiniteArticle":"a" }
    },
    initTerminology: function(){
        if (OCA.checkFeature('RISKS')){
            new Gopher('/riskterminology', RiskController.gotTerminology).run();
        }
    },
    gotTerminology: function(data){
        var terms = data[0];
        for (var term in terms){
            var t = terms[term];
            var sing = term;
            var plur = term + 's';
            var singLC = term.toLowerCase();
            var plurLC = singLC + 's';
            $('span.term.' + sing).text(t.Title);
            $('span.term.' + plur).text(t.Plural);
            $('span.term.' + singLC).text(t.Title.toLowerCase());
            $('span.term.' + plurLC).text(t.Plural.toLowerCase());
            //indefinite article not currently used
        }
        RiskController.Terminology = terms;
    },
    initMatrix: function(page){
        this.$matrixPage = $(page);
        this.$ratingTypes = $(page).find('.ratingTypes').on('click', 'li', $.proxy(this.changeRatingField, this));
    },
    changeRatingField: function(e){
        var $li = $(e.target);
        this.currentRatingField = $li.data('type');
        var key = this.currentRatingField + 'Risk';
        this.$matrixPage.find('.cell .count').hide();
        this.$matrixPage.find('.cell .count.' + this.currentRatingField).show();
        this.$ratingTypes.find('h2 span.label').text(RiskController.Terminology[key].Title);
        this.$ratingTypes.collapsible('collapse');
    },
    init: function(page){
        this.$registerPage = $(page);
        this.$registerLV = this.$registerPage.find('.registers');
        this.$registerLV.on('click', 'a', $.proxy(this.loadRegister, this));
        this.$registerPage.find('#riskregisterSearch').keypress(function(e){
            if (e.which == 13){
                RiskController.getRegisters($(this).val());
            }
        }).on('change', function(e){
                if ($(this).val() == ''){
                    RiskController.getRegisters();
                }
            });
    },
    initContext: function(page){
        this.$contextPage = $(page);
        this.$contextsLV = this.$contextPage.find('.listview.contexts');
        this.$risksLV = this.$contextPage.find('.listview.risks');

    },
    initControlSelector: function(page){
        this.$controlsLV = $(page).find('.listview.riskcontrols');
    },
    getTypes: function($page){
        new Gopher('/risktypes', $.proxy(this.gotTypes, this, $page.find('.risktype.listview'))).run();
    },
    gotTypes: function($lv, data, extra){
        ViewUtil.populateLV($lv, data, 'risktype', 'risk', true, extra.nextPageURL);
        this.returnedLists = 2;
        this.checkLoaded($lv, $lv);
    },
    getMatrix: function(id, registerID, contextID){
        this.selectorMode = false;
        this.currentMatrixID = id;
        this.currentRegisterID = registerID;
        this.currentContextID = contextID;
        var url = '/riskmatrix/' + id;
        var showCount = registerID && contextID;
        if (showCount){
            url += "?field[]=RISKCOUNT&registerID=" + registerID + "&contextID=" + contextID;
        }
        new Gopher(url, $.proxy(this.gotMatrix, this, showCount)).run();
    },
    getMatrixSelector: function(){
        this.selectorMode = true;
        this.gotMatrix(false, linkParams.matrix);
    },
    gotMatrix: function(showCount, data){
        data = data[0] ? data[0] : data;
        data = $.extend(true, {}, data); //clone because we're keeping it for a while for the cell handlers
        this.$matrixPage.find('h2.heading').text(data.Name);
        var $grid = this.$matrixPage.find('div#matrixGrid').empty().attr('class', '');
        $grid.append("<div class='ui-block-a grid xlabel ylabel'></div>"); //spacer

        $grid.addClass('ui-grid-c');
        this.$matrixPage.find('.xlabel.heading').text(data.XLabel);
        this.$matrixPage.find('.ylabel.heading').text(data.YLabel);
        for (var x = 0; x < data.XAxisLabels.length; x++){
            $grid.append("<div class='ui-block-b xlabel grid'><div class='rotate'>" + data.XAxisLabels[x].Name + "</div></div>");
        }
        var c = 0;
        for (var y = 0; y < data.YAxisLabels.length; y++){
            $grid.append("<div class='ui-block-a ylabel grid'><div class='rotate'>" + data.YAxisLabels[y].Name + "</div></div>");
            for (x = 0; x < data.XAxisLabels.length; x++){
                var cell = data.Cells[c];
                var $cell = $("<div class='ui-block-b grid cell " + ViewUtil.lightDarkStyle(cell.Colour) + "'><a href='#' class='ui-shadow ui-btn ui-corner-all ui-mini cell cellresize' data-cell='"+ c + "' style='background-color: #" + cell.Colour+ "'><span>" +
                    cell.Name.substr(0, 10)
                    + "</span></a></div>");
                if (showCount){
                    var $a = $cell.find('a').text('');
                    for (var t =0; t < this.ratingTypes.length; t++){
                        var type = this.ratingTypes[t];
                        $a.append("<span class='count " + type + "'>" + cell[type + "RiskCount"] + "</span>");
                    }
                    $a.attr('href', this.getCellLink(cell));
                }
                $grid.append($cell);
                c++;
            }
        }
        this.$ratingTypes.showIf(showCount);
        if (showCount){
            this.$ratingTypes.find('li:first-child a').click();
        }

        //resize all cells to be the same size
        setTimeout($.proxy(this.resizeGrid, this),100);
        $(window).on('orientationchange', function(){
            if ($('body').pagecontainer('getActivePage').prop('id') === 'riskMatrixView'){
                setTimeout($.proxy(RiskController.resizeGrid, RiskController), 1000); //takes a while for the window's dimensions to update. annoying
            }
        });

        //handle cell clicks
        $grid.off().on('click', 'a.cell', $.proxy(this.cellSelect, this, data));
    },
    getCellLink: function(cell){
        var url = "#riskcontextTreeView?id=" + this.currentContextID;
        url += "&registerID=" + this.currentRegisterID;
        url += "&matrixID=" + this.currentMatrixID;
        url += "&xIndex=" + cell.XIndex;
        url += "&yIndex=" + cell.YIndex;
        return url;
    },
    getRegisters: function(search){
        var url = '/riskregisters?orderby=Name&field[]=RiskContextID';
        if (search) url += '&search=' + search;
        new Gopher(url, $.proxy(this.gotRegisters, this)).run({offlineError: 'inline'});
    },
    gotRegisters: function(data, extra){
        ViewUtil.populateLV(this.$registerLV, data, 'riskregister', 'risk_register', false, extra.nextPageURL);
        if (this.$registerLV.children().length === 0) {
            this.$registerLV.append("<li data-theme='e'>"+OCA.getI18n().gettext('There are no items to display')+"</li>").listview('refresh');
        }
        this.checkLoaded();
    },
    loadRegister: function(e){
        var $a = $(e.target);
        var registerID = parseInt($a.attr('href').replace('#riskregisterView?id=', ''), 10);
        var contextID = parseInt($a.data('riskcontextid'), 10);
        contextID = isNaN(contextID) ? 0 : contextID;

        new Gopher('/riskregister/' + registerID, $.proxy(this.gotRiskRegister, this, contextID, registerID)).run();

        e.preventDefault();
        return false;
    },
    gotRiskRegister: function(contextID, registerID, data){
        this.currentRiskRegister = data[0];
        $('body').pagecontainer('change', '#riskcontextTreeView?id=' + contextID + "&registerID=" + registerID, {});
    },
    renderListing: function(contextID, registerID){
        this.$contextPage.find('.context.footer.menu .notroot').showIf(contextID != 0);
        this.$contextPage.find('#riskcontextTreeViewMenu .riskcontextView').prop('href', '#riskcontextView?id=' + contextID);
        this.$contextPage.find('#riskcontextTreeMoreMenu a.new.risk').prop('href', '#riskNew?parent=' + contextID + '&register=' + registerID);
        this.$contextPage.find('#riskcontextTreeMoreMenu a.new.riskcontext').prop('href', '#riskcontextNew?parent=' + contextID);
        this.$contextPage.find('#riskcontextTreeMoreMenu a.library.risk').off().on('click', $.proxy(this.startRiskLibrary, this, contextID, registerID));

        this.$contextPage.find('.selector-mode').showIf(this.selectorMode);
        this.$contextPage.find('.normal-mode').showIf(!this.selectorMode);

        this.$contextPage.find('.listview').empty();
        this.$contextPage.find('.ui-listview.extra-data').remove();
        $(window).off('scroll.listview'); //remove pagination handlers

        var $viewMenu = this.$contextPage.find('#riskcontextTreeViewMenu ul');
        $viewMenu.find('.view.matrix').remove();
        if (this.currentRiskRegister){
            if(registerID && contextID != 0){ //if a register and not the root
                for (var matrixURL in this.currentRiskRegister.RiskMatrices){
                    var label = this.currentRiskRegister.RiskMatrices[matrixURL];
                    var id = ViewUtil.getID(matrixURL);
                    var link = "#riskMatrixView?id=" + id + "&registerID=" + registerID + "&contextID=" + contextID;
                    var $link = $("<li class='view matrix'><a href='" + link + "'>View as " + label + " matrix</a></li>");
                    $viewMenu.prepend($link);
                }
                $viewMenu.enhanceWithin().listview('refresh');
            }
            var root = ViewUtil.getID(this.currentRiskRegister.RiskContextURL);
            this.$contextPage.find('.context.footer.menu .root').showIf((root == contextID));
            this.$contextPage.find('#riskcontextTreeViewMenu .riskregisterView').prop('href', '#riskregisterView?id=' + registerID);
        } else {
            this.currentRiskRegister = null;
        }

        this.returnedLists = 0;
        new Gopher("/riskcontext/" + contextID + "/riskcontexts", $.proxy(this.gotRiskContexts, this, registerID)).run();
        if (contextID != 0) {
            new Gopher("/riskcontext/" + contextID, $.proxy(this.changeContextHeading, this)).run();
            if (this.selectorMode !== 'riskcontext'){ //dont need risks if selecting context
                var url = "/riskcontext/" + contextID + "/risks";
                if (registerID) url += "?registerID=" + registerID;
                new Gopher(url, $.proxy(this.gotRisks, this)).run();
            } else {
                this.returnedLists++; //only one thing to fetch
            }
        } else if (registerID) {
            this.returnedLists++; //only one thing to fetch
            new Gopher('/riskregister/' + registerID, $.proxy(this.changeContextHeading, this)).run();
        } else {
            this.changeContextHeading([{Name: OCA.getI18n().gettext('Contexts')}]);
        }
    },
    riskcontrolSelector: function(riskID){
        new Gopher('/risk/' + riskID + '/riskcontrols', $.proxy(this.gotRiskControls, this)).run();
    },
    getLibrary: function($page, type, categoryID, registerID){
        $page.find('.listview').empty();
        var root = "/" + type + "librarycategory/" + categoryID + "/";

        this.returnedLists = 0;
        new Gopher(root + type + "librarycategories", $.proxy(this.gotLibraryCategories, this, $page, type, registerID)).run();
        if (categoryID){
            var items = root + type + "s";
            if (registerID) items += "?registerID=" + registerID;
            new Gopher(items, $.proxy(this.gotLibraryItems, this, $page, type)).run();
        } else {
            this.returnedLists++; //only one thing to ftech
        }
    },
    getLibraryRiskControls: function($page, riskID){
        //handle the special case of listing controls from a library risk so the user can select non-mandatory risk controls
        $page.find('.listview').empty();
        this.returnedLists = 1;
        new Gopher('/risk/' + riskID + '/riskcontrols', $.proxy(this.gotLibraryRiskControls, this, $page, riskID)).run();
    },
    gotLibraryCategories: function($page, type, registerID, data, extra){
        var $catLV = $page.find('.listview.category');
        var $itemLV = $page.find('.listview.item');
        var extraParams = registerID ? {registerID: registerID} : null;
        ViewUtil.populateLV($catLV, data, type + 'libraryTree', 'folder', false, extra.nextPageURL, extraParams);
        this.returnedLists++;
        this.checkLoaded($catLV, $itemLV);
    },
    gotLibraryItems: function($page, type, data, extra){
        var $catLV = $page.find('.listview.category');
        var $itemLV = $page.find('.listview.item');
        var selectorMode = type == 'risk' ? {parent: true, parentSelect:true} : true;
        ViewUtil.populateLV($itemLV, data, type  + 'libraryTree', type == 'risk' ? 'risk' : 'risk_control', selectorMode, extra.nextPageURL);
        this.returnedLists++;
        this.checkLoaded($catLV, $itemLV);
    },
    gotLibraryRiskControls: function($page, riskID, data, extra){
        var $itemLV = $page.find('.listview.item');
        for (var i = 0; i < data.length; i++){
            var id = ViewUtil.getID(data[i].URL);
            data[i].URL = Configuration.getAPIPath() + '/riskcontrol/' + riskID + '-' + id; //prepend riskcontrol IDs with the parent riskID
        }
        ViewUtil.populateLV($itemLV, data, 'riskcontrollibraryTree', 'risk_control', true, extra.nextPageURL);
        this.returnedLists++;
        this.checkLoaded($page.find('.listview.category'), $itemLV);
    },
    startRiskLibrary: function(contextID, registerID){
        var page = "#risklibraryTreeView?id=0";
        if (registerID) page += "&registerID=" + registerID;

        ViewUtil.selector.start({
            callbackOK: $.proxy(this.riskLibrarySelected, this, contextID),
            data: {},
            previousObject: this
        });
        $("body").pagecontainer( "change", page, {});
    },
    riskLibrarySelected: function(contextID, data){
        var risks = {};
        for (var k in data){
            var item = data[k];
            if (item.checked){
                var id = item.id + "";
                if (id.indexOf('-') != -1){ //riskcontrol, format riskID-riskcontrolID
                    var bits = id.split('-');
                    if (!risks[bits[0]]){
                        risks[bits[0]] = [];
                    }
                    risks[bits[0]].push(bits[1]);
                } else {
                    if (!risks[id]){
                        risks[id] = [];
                    }
                }
            }
        }
        if (!$.isEmptyObject(risks)){
            new Gopher({url: '/riskcontext/' + contextID + '/risks', data: risks}, function(){
                util.reload();
            }).post();
        }
    },
    getRisksFromCell: function(contextID, registerID, matrixID, x, y, ratingField){
        this.$contextPage.find('.ui-footer').hide();

        this.$contextPage.find('.listview').empty();
        this.$contextPage.find('.ui-listview.extra-data').remove();
        $(window).off('scroll.listview'); //remove pagination handlers

        this.returnedLists = 1; //no contexts to get
        var url = "/riskcontext/" + contextID + "/risks?registerID=" + registerID + '&matrixID=' + matrixID + '&xIndex=' + x + '&yIndex=' + y + '&ratingField=' + ratingField;
        new Gopher(url, $.proxy(this.gotRisks, this)).run();
        this.changeContextHeading([{Name: this.Terminology.Risk.Plural}]); //fake it into the API response format to reuse the function
    },
    changeContextHeading: function(data){
        this.$contextPage.find('div.heading-row h2').text(data[0].Name);
    },
    gotRiskContexts:function(registerID, data, extra){
        var selectorMode = this.selectorMode
            ? {unselectable: this.selectorMode !== 'riskcontext', mode: this.selectorMode, parent: this.selectorMode === 'riskcontext'}
            : false;
        var extraParams = registerID ? {registerID: registerID} : null;
        ViewUtil.populateLV(this.$contextsLV, data, 'riskcontextTree', 'folder', selectorMode, extra.nextPageURL, extraParams);
        this.returnedLists++;
        this.checkLoaded();
    },
    gotRisks: function(data, extra){
        var selectorMode = this.selectorMode
            ? {mode: this.selectorMode}
            : false;
        var type = 'risk';
        if (this.selectorMode === 'riskcontrol') {
            selectorMode.unselectable = true;
            type = this.selectorMode;
        }
        ViewUtil.populateLV(this.$risksLV, data, type, 'risk', selectorMode, extra.nextPageURL);
        this.returnedLists++;
        this.checkLoaded();
    },
    gotRiskControls: function(data, extra){
        ViewUtil.populateLV(this.$controlsLV, data, 'riskcontrol', 'risk_control', true, extra.nextPageURL);
        this.returnedLists = 2;
        this.checkLoaded(this.$controlsLV, this.$controlsLV);
    },
    checkLoaded: function($lv1, $lv2){
        app.checkLoaded();
        $lv1 = $lv1 || this.$contextsLV; //support calling this function with parameters, but default to the contexts LV
        $lv2 = $lv2 || this.$risksLV;    //and risks LV
        if ($lv1 && $lv2 && this.returnedLists == 2 && $lv1.children().length === 0 && $lv2.children().length === 0) {
            $lv1.append($("<li />").data('theme','e').text(OCA.getI18n().gettext('There are no items to display'))).listview('refresh');
        }
    },
    cellSelect: function(data, e){
        var id = $(e.currentTarget).data('cell');
        var cell = data.Cells[id];
        if (this.selectorMode){
            ViewUtil.selector.data = {
                Cell: cell,
                YAxis: data.YAxisLabels[cell.YIndex],
                XAxis: data.XAxisLabels[cell.XIndex]
            };
            ViewUtil.selector.select();
        }
    },
    //note: this function uses window.innerHeight and window.innerWidth rather than jquery functions because of a bug observed on a retina iPad
    //probably the issue noted here: https://issues.apache.org/jira/browse/CB-4323
    resizeGrid: function(){
        var max = 0;
        var baseCellWidth  = 35;
        var baseCellHeight = 45;
        var cellSpacing = 10; //CSS: #matrixGrid .grid margin is 5px

        $('#matrixGrid .ui-btn.cellresize').each(function(i,e){
            max = Math.max(max, $(e).height());
        }).height(max);

        //find largest cell label
        max = 0;
        $('#matrixGrid .cell span').each(function(i,e){
            max = Math.max(max, $(e).width())
        });
        var cellWidth = Math.max(max, baseCellWidth);
        $('#matrixGrid .grid').not('.xlabel, .ylabel').width(cellWidth);

        //y labels
        max = 0;
        var yCount = 0;
        $('#matrixGrid .ylabel').each(function(i,e){
            var width = $(e).find('.rotate').width();
            max = Math.max(max, width);
            yCount++;
        })
        var yLabelWidth = Math.cos(45 * Math.PI / 180) * max + 20; //20 for padding
        $('#matrixGrid .ylabel').width(yLabelWidth);

//        $('#matrixGrid .ylabel .rotate').width(max) //label positioning
        //x labels
        max = 0;
        var xCount = 0;
        $('#matrixGrid .xlabel').each(function(i,e){
            var width = $(e).find('.rotate').width();
            max = Math.max(max, width);
            xCount++;
        });
        var xLabelHeight = Math.sin(45 * Math.PI / 180) * max + 15; //15 for padding
        $('#matrixGrid .xlabel').height(xLabelHeight).filter('.ui-block-b').width(baseCellWidth);
        $('#matrixGrid .xlabel .rotate').width(max);

        $('#matrixGrid').width( yLabelWidth  + cellSpacing + xCount * (cellWidth      + cellSpacing));         //count - 1 to exclude label column
        $('#matrixGrid').height(xLabelHeight + cellSpacing + yCount * (baseCellHeight + cellSpacing));

        var $wrap = this.$matrixPage.find('.wrapper');
        var off = $wrap.offset();
        $wrap.height(window.innerHeight - off.top - 11); //padding 10 + border 1
        var $yhead = this.$matrixPage.find('.ylabel.heading');
        var $gridContainer = this.$matrixPage.find('.grid.container');
        $gridContainer.height(window.innerHeight - $gridContainer.offset().top);
        $gridContainer.width( Math.min(window.innerWidth  - off.left, $('#matrixGrid').width())); //fill window, unless grid is smaller than the window

        var visibleGridH = Math.min($('#matrixGrid').height(), $gridContainer.height())
        //align y heading to the left, ideally in the middle of the grid but at least visible on the screen
        $yhead.css('top', Math.min(off.top + visibleGridH / 2, window.innerHeight - $yhead.width() / 2));
        $yhead.css('margin-left', - $yhead.width() / 2);
//        $('.xlabel.heading').width(Math.min($('#matrixGrid').width(), $gridContainer.width()));
    }
});
$(window).on('init-OCA_RISK', RiskController.initTerminology); //when logged into a system with OCA_Risk pack

function RiskRegisterView(id, page){
    this.initRiskRegisterView(id, page);
}
RiskRegisterView.prototype = new TypeView;
RiskRegisterView.prototype.constructor = RiskRegisterView;
RiskRegisterView.prototype.initRiskRegisterView = function(id, page){
    this.initTypeView(id, page, "riskregister");
    this.deleteLevels -= 2;  //go back extra because of the tree view and the view options popup.
    // ignore the popup if it is iOS9
	if (device.platform === "iOS" && parseInt(device.version) >= 9){
		this.deleteLevels++;
	}
};
RiskRegisterView.prototype.renderOptions = function(){
    this.fieldRender({Label: OCA.getI18n().gettext('Name') }, this.data.Name);
    this.fieldRender({Label: OCA.getI18n().gettext('Context') }, this.data.RiskContext ? this.data.RiskContext : OCA.getI18n().gettext('all'));
    this.slmcRender({Label: RiskController.Terminology.Risk.Title + " " + OCA.getI18n().gettext('Types')}, this.getSLMCData(this.data.RiskTypes), false);
}
RiskRegisterView.prototype.getSLMCData = function(obj){
    var data = [];
    for (var url in obj){
        data.push({url: url, label: obj[url]});
    }
    return data;
}
RiskRegisterView.prototype.afterRender = function(){
    TypeView.prototype.afterRender.call(this);

    var canEdit    = (this.data.WritePolicyURL != -1)

    var $deletePopup = this.page.find('#confirmDeleteRiskRegister');
    ViewUtil.applyTemplate($deletePopup,{item: 'riskregister', label: OCA.getI18n().gettext('register')}, 'confirmDelete');
    $deletePopup.find('a.delete').off().on('click', $.proxy(this.deleteItem, this));
    var $mm = this.moreMenu;
    $mm.find('li.riskregister.delete').showIf(canEdit).on('click', function(e){
        $mm.popup('close');
        $deletePopup.popup('open');
        e.preventDefault();
    });
}

function RiskRegisterEdit(id, page){
    this.initRiskRegisterEdit(id, page);
}
RiskRegisterEdit.prototype = new TypeEdit;
RiskRegisterEdit.prototype.constructor = RiskRegisterEdit;
RiskRegisterEdit.prototype.initRiskRegisterEdit = function(id, page){
    this.initTypeEdit(id, page, "riskregister");
    this.supportsLocation = false;
};
RiskRegisterEdit.prototype.renderOptions = function(){
    if (!this.data) this.data = {};
    this.typeData.Name = {Label: OCA.getI18n().gettext('Name')};
    this.fieldRender(this.typeData.Name, this.data.Name);
    this.typeData.ContextChooserURL = {Label: OCA.getI18n().gettext('Select existing context'), Empty: '(' + OCA.getI18n().gettext('all') + ')', Maximum: 1};
    var context = this.data.RiskContextURL
        ? [{url: this.data.RiskContextURL, label: this.data.RiskContext}]
        : null;
    this.riskcontextchooserRender(this.typeData.ContextChooserURL, context);
    this.addNewContext(); //new hook, edit doesnt use it
    this.typeData.RiskTypes = {Label: RiskController.Terminology.Risk.Title + " " + OCA.getI18n().gettext('Types')};
    this.slmcRender(this.typeData.RiskTypes, RiskRegisterView.prototype.getSLMCData.call(this, this.data.RiskTypes), 'risktypeIndex');
}
RiskRegisterEdit.prototype.addNewContext = function(){};
RiskRegisterEdit.prototype.renderRelations = function(){};
RiskRegisterEdit.prototype.getOptions = function(optionObj){
    var options = [];
    for (var val in optionObj){
        options.push([val, optionObj[val]]);
    }
    return options;
}

function RiskRegisterNew(page){
    this.initRiskRegisterNew(page);
}
RiskRegisterNew.prototype = new RiskRegisterEdit;
RiskRegisterNew.prototype.constructor = RiskContextNew;
RiskRegisterNew.prototype.initRiskRegisterNew = function(page){
    this.initRiskRegisterEdit(null, page);
    this.createURL = '/riskregisters';
}
RiskRegisterNew.prototype.hasChanged = TypeNew.prototype.hasChanged;
RiskRegisterNew.prototype.submission = function(submission){
    if (this.submitted) return;
    this.submitted = true;
    submission['TypeURL'] = Configuration.getAPIPath() + this.typeEndpoint + '/' + this.typeID;
    var desc = OCA.getI18n().gettext("Created new register");
    window.linkParams = {createdObject: 'RiskRegister', message: desc};
    new Gopher({url: this.createURL, data: submission, desc: desc, oldTimestamp: this.timestamp}, function(){
		util.goBack();
    }, $.proxy(this.dataError, this)).post();
}
RiskRegisterNew.prototype.addNewContext = function(){
    this.typeData.NewContextName = {Label: OCA.getI18n().gettext('or create new context')};
    var newRow = this.fieldRender(this.typeData.NewContextName, null);
    this.typeData.NewContextTypeURL = {
        Label: OCA.getI18n().gettext('Context types'),
        Options: this.getOptions(this.typeData.RiskContextTypes),
        DefaultValue: true //remove 'none' option
    };
    var typeRow = this.optRender(this.typeData.NewContextTypeURL, null);
    newRow.append(this.typeData.NewContextTypeURL.Input);
    typeRow.remove();
}
RiskRegisterNew.prototype.getOptions = function(types){
    var options = [];
    for (var url in types){
        options.push([url, types[url]]);
    }
    return options;
}

function RiskContextView(id, page){
    this.initRiskContextView(id, page);
}
RiskContextView.prototype = new TypeView;
RiskContextView.prototype.constructor = RiskContextView;
RiskContextView.prototype.initRiskContextView = function(id, page){
    this.initTypeView(id, page, "riskcontext");
    this.deleteLevels -= 2; //go back extra because of the tree view and the view options popup
};
RiskContextView.prototype.renderOptions = function(){
    this.fieldRender({Label: OCA.getI18n().gettext('Name') }, this.data.Name);
    this.slmcRender( {Label: OCA.getI18n().gettext('Owner')}, this.data.Owners, 'contact');
    this.fieldRender({Label: OCA.getI18n().gettext('Review frequency')}, this.getReviewFrequency());
}
RiskContextView.prototype.getReviewFrequency = function(){
    if (!this.data.ReviewFrequencyUnit) return null;
    return this.data.ReviewFrequencyUnit + ' ' + this.typeData.ReviewFrequencyRecurrenceUnits[this.data.ReviewFrequencyRecurrenceUnitID];
}
RiskContextView.prototype.afterRender = function(){
    TypeView.prototype.afterRender.call(this);

    var canEdit    = (this.data.WritePolicyURL != -1)

    var $deletePopup = this.page.find('#confirmDeleteRiskContext');
    ViewUtil.applyTemplate($deletePopup,{item: 'riskcontext', label: OCA.getI18n().gettext('context')}, 'confirmDelete');
    $deletePopup.find('a.delete').off().on('click', $.proxy(this.deleteItem, this));
    var $mm = this.moreMenu;
    $mm.find('li.riskcontext.delete').showIf(canEdit).on('click', function(e){
        $mm.popup('close');
        $deletePopup.popup('open');
        e.preventDefault();
    });
}

function RiskContextEdit(id, page){
    this.initRiskContextEdit(id, page);
}
RiskContextEdit.prototype = new TypeEdit;
RiskContextEdit.prototype.constructor = RiskContextEdit;
RiskContextEdit.prototype.initRiskContextEdit = function(id, page){
    this.initTypeEdit(id, page, "riskcontext");
    this.supportsLocation = false;
};
RiskContextEdit.prototype.renderOptions = function(){
    if (!this.data) this.data = {};
    this.typeData.Name = {Label: OCA.getI18n().gettext('Name')};
    this.fieldRender(this.typeData.Name, this.data.Name);
//    this.addParent();
    this.typeData.Owners = {Label: OCA.getI18n().gettext('Owner'), Empty: '(' + OCA.getI18n().gettext('inherited') + ')'};
    this.slmcRender(this.typeData.Owners, this.data.Owners, 'contactgroupTreeView?mode=contacts');

    this.typeData.ReviewFrequencyUnit = {Label: OCA.getI18n().gettext('Review frequency'), Tooltip: '(' + OCA.getI18n().gettext('inherited') + ')', Type: 'number'};
    this.numberRender(this.typeData.ReviewFrequencyUnit, this.data.ReviewFrequencyUnit);
    this.typeData.ReviewFrequencyRecurrenceUnitID = {Label: '', Options: this.getOptions(this.typeData.ReviewFrequencyRecurrenceUnits)};
    var unitRow = this.optRender(this.typeData.ReviewFrequencyRecurrenceUnitID, this.data.ReviewFrequencyRecurrenceUnitID);
    this.typeData.ReviewFrequencyRecurrenceUnitID.Input.appendTo(this.typeData.ReviewFrequencyUnit.Input.parent());
    unitRow.remove();
}
RiskContextEdit.prototype.addParent = function(){
    this.typeData.ParentID = {Label: OCA.getI18n().gettext('Parent'), Maximum: 1};
    this.riskcontextchooserRender(this.typeData.ParentID, this.data.ParentRiskContext);
}
RiskContextEdit.prototype.renderRelations = function(){};
RiskContextEdit.prototype.getOptions = function(optionObj){
    var options = [];
    for (var val in optionObj){
        options.push([val, optionObj[val]]);
    }
    return options;
}

function RiskContextNew(parentID, page){
    this.initRiskContextNew(parentID, page);
}
RiskContextNew.prototype = new RiskContextEdit;
RiskContextNew.prototype.constructor = RiskContextNew;
RiskContextNew.prototype.initRiskContextNew = function(parentID, page){
    this.initRiskContextEdit(null, page);
    this.createURL = '/riskcontext/' + parentID + '/riskcontexts';
}
RiskContextNew.prototype.hasChanged = TypeNew.prototype.hasChanged;
RiskContextNew.prototype.submission = function(submission){
    if (this.submitted) return;
    this.submitted = true;
    submission['TypeURL'] = Configuration.getAPIPath() + this.typeEndpoint + '/' + this.typeID;
    var desc = OCA.getI18n().gettext("Created new context");
    window.linkParams = {createdObject: 'RiskContext', message: desc};
    new Gopher({url: this.createURL, data: submission, desc: desc, oldTimestamp: this.timestamp}, function(){
		util.goBack();
    }, $.proxy(this.dataError, this)).post();
}
RiskContextNew.prototype.addParent = function(){}; //parent already set by route param

function RiskControlView(id, page){
    this.initRiskControlView(id, page);
}
RiskControlView.prototype = new TypeView;
RiskControlView.prototype.constructor = RiskControlView;
RiskControlView.prototype.initRiskControlView = function(id, page){
    this.initTypeView(id, page, "riskcontrol");
};
RiskControlView.prototype.beforeRender = function(){
    TypeView.prototype.beforeRender.call(this);

    var riskID = ViewUtil.getID(this.data.RiskURL);
    new Gopher('/risk/' + riskID, $.proxy(this.gotRisk, this)).run();
}
RiskControlView.prototype.gotRisk = function(data){
    this.prepend = true; //prepending, so call fields in reverse of display order
    this.fieldRender({Label: RiskController.Terminology.Risk.Title}, data[0].Name);
    this.fieldRender({Label: OCA.getI18n().gettext('Context')}, data[0].Context);
    this.prepend = false;
    this.listview.listview('refresh');
}
RiskControlView.prototype.renderOptions = function(){
    if (!$.isEmptyObject(this.data.Events)){
        var $emeHeader = $("<li data-role='list-divider'/>").text(OCA.getI18n().gettext("Events"));
        this.listview.append($emeHeader);
    }
    for (var emeURL in this.data.Events){
        var emeID = ViewUtil.getID(emeURL);
        this.listview.append("<li><a href='#emeView?id=" + emeID +"'><span class='icon error pad-right'></span>" + this.data.Events[emeURL] + "</a></li>");
    }
};
RiskControlView.prototype.afterRender = function(){
    TypeView.prototype.afterRender.call(this);

    var canEdit    = (this.data.WritePolicyURL != -1)

    var $deletePopup = this.page.find('#confirmDeleteRiskControl');
    ViewUtil.applyTemplate($deletePopup, {item: 'control', label: RiskController.Terminology.Control.Title.toLowerCase()}, 'confirmDelete');
    $deletePopup.find('a.delete').off().on('click', $.proxy(this.deleteItem, this));
    var $mm = this.moreMenu;
    $mm.find('li.riskcontrol.delete').showIf(canEdit).on('click', function(){
        $mm.popup('close');
        $deletePopup.popup('open');
    });
}
RiskControlView.prototype.renderRelations = function(){};

function RiskControlEdit(id, page){
    this.initRiskControlEdit(id, page);
}
RiskControlEdit.prototype = new TypeEdit;
RiskControlEdit.prototype.constructor = RiskControlEdit;
RiskControlEdit.prototype.initRiskControlEdit = function(id, page){
    this.initTypeEdit(id, page, "riskcontrol");
    this.supportsLocation = false;
};
RiskControlEdit.prototype.renderRelations = function(){};

function RiskControlNew(parentID, page){
    this.initRiskControlNew(parentID, page);
}
RiskControlNew.prototype = new RiskControlEdit;
RiskControlNew.prototype.constructor = RiskControlNew;
RiskControlNew.prototype.initRiskControlNew = function(parentID, page){
    this.initRiskControlEdit(null, page);
    this.createURL = '/risk/' + parentID + '/riskcontrols';
}
RiskControlNew.prototype.hasChanged = TypeNew.prototype.hasChanged;
RiskControlNew.prototype.submission = function(submission){
    if (this.submitted) return;
    this.submitted = true;
    submission['TypeURL'] = Configuration.getAPIPath() + this.typeEndpoint + '/' + this.typeID;
    var desc = OCA.getI18n().gettext("Created new ") + this.typeData.Name;
    window.linkParams = {createdObject: 'RiskControl', message: desc};
    new Gopher({url: this.createURL, data: submission, desc: desc, oldTimestamp: this.timestamp}, function(){
		util.goBack();
    }, $.proxy(this.dataError, this)).post();
}

function RiskView(id, page){
    this.initRiskView(id, page);
}
RiskView.prototype = new TypeView;
RiskView.prototype.constructor = RiskView;
RiskView.prototype.initRiskView = function(id, page){
    this.initTypeView(id, page, "risk");
    this.defineLookup = {};
};
RiskView.prototype.beforeRender = function(){
    TypeView.prototype.beforeRender.call(this);

    if (this.data.RiskContext){
        this.fieldRender({Label: OCA.getI18n().gettext('Context')}, this.data.RiskContext);
    }
}
RiskView.prototype.afterRender = function(){
    TypeView.prototype.afterRender.call(this);

    var canEdit    = (this.data.WritePolicyURL != -1)

    var $deletePopup = this.page.find('#confirmDeleteRisk');
    ViewUtil.applyTemplate($deletePopup, {item: 'Risk', label: RiskController.Terminology.Risk.Title.toLowerCase()}, 'confirmDelete');
    $deletePopup.find('a.delete').off().on('click', $.proxy(this.deleteItem, this));
    var $mm = this.moreMenu;
    $mm.find('li.risk.delete').showIf(canEdit).on('click', function(){
        $mm.popup('close');
        $deletePopup.popup('open');
    });
    $mm.find('li.control.new a').prop('href', '#riskcontrolNew?parent=' + this.ID);
    $mm.find('li.control.library').off().on('click', $.proxy(this.startControlLibrary, this));

    var $reviewPopup = this.page.find('#confirmReviewRisk');
    $reviewPopup.find('a.review').off().on('click', $.proxy(this.reviewRisk, this));
    $mm.find('li.risk.review').showIf(canEdit).on('click', function(){
        $mm.popup('close');
        $reviewPopup.popup('open');
    });
}
RiskView.prototype.startControlLibrary = function(){
    ViewUtil.selector.start({
        callbackOK: $.proxy(this.controlLibrarySelected, this),
        data: {},
        previousObject: this
    });
    $("body").pagecontainer("change", "#riskcontrollibraryTreeView?id=0", {});
};
RiskView.prototype.controlLibrarySelected = function(data){
    var controls = [];
    for (var k in data){
        if (data[k].checked){
            controls.push(data[k].id);
        }
    }
    if (controls.length){
        new Gopher({url: '/risk/' + this.ID + '/riskcontrols', data: controls}, function(){
            setTimeout(util.reload, 100); //use timeout so the cache clearing finishes
        }).post();
    }
};
RiskView.prototype.reviewRisk = function(){
    var root = this.endpoint + this.ID;
    new Gopher(root + '/review', function(){
        new Gopher(root).uncache();
        util.reload();
    }).post();
};
RiskView.prototype.optRender = function(field, data){
    field = this.addAxisOptions(field, data);
    return TypeView.prototype.optRender.call(this, field, data);
}
RiskView.prototype.getRatingCell = function(field){
    var define = field.Define.replace('RATING', '');
    var x = this.defineLookup[define + 'XAXIS'];
    var y = this.defineLookup[define + 'YAXIS'];
    if (x && y){
        var matrix = this.typeData.Matrix;
        for (var c = 0; c < matrix.Cells.length; c++){
            var cell = matrix.Cells[c];
            if (cell.XIndex == x && cell.YIndex == y){
                return cell;
            }
        }
    }
    return null;
}
RiskView.prototype.riskratingRender = function(field,data){
    var cell = this.getRatingCell(field);
    data = cell ? cell.Name : '(none)';
    return this.fieldRender(field, "<a href='#' class='ui-btn matrix' style='background-color: #" + (cell ?  cell.Colour : '') + "'>" + data + "</a>");
}
RiskView.prototype.getAxisOptions = function(axisLabels){
    var opts = [];
    for (var l = 0; l < axisLabels.length; l++){
        opts.push([l, axisLabels[l].Name]);
    }
    return opts;
}
RiskView.prototype.addAxisOptions = function(field, data){
    switch (field.Define){
        case 'RESIDUALRISKXAXIS':
        case 'TARGETRISKXAXIS':
        case 'INHERENTRISKXAXIS':
            field.Options = this.getAxisOptions(this.typeData.Matrix.XAxisLabels);
            break;
        case 'RESIDUALRISKYAXIS':
        case 'TARGETRISKYAXIS':
        case 'INHERENTRISKYAXIS':
            field.Options = this.getAxisOptions(this.typeData.Matrix.YAxisLabels);
            break;
    }
    if (field.Define){
        this.defineLookup[field.Define] = data;
    }
    return field;
}
RiskView.prototype.renderOptions = function(){
    var $conHeader = $("<li data-role='list-divider'/>").text(RiskController.Terminology.Control.Plural);
    this.listview.append($conHeader);
    var $conLI = $('<li></li>').appendTo(this.listview);
    new Gopher(this.endpoint + this.ID + '/riskcontrols', $.proxy(this.gotControls, this, $conLI, $conHeader)).run();

    if (!$.isEmptyObject(this.data.Events)){
        var $emeHeader = $("<li data-role='list-divider'/>").text(OCA.getI18n().gettext("Events"));
        this.listview.append($emeHeader);
    }
    for (var emeURL in this.data.Events){
        var emeID = ViewUtil.getID(emeURL);
        this.listview.append("<li><a href='#emeView?id=" + emeID +"'><span class='icon error pad-right'></span>" + this.data.Events[emeURL] + "</a></li>");
    }
    if (this.data.LastReviewDate || this.data.NextReviewDueDate){
        this.listview.append("<li data-role='list-divider'>Reviews</li>");
        this.datetimeRender({Label: OCA.getI18n().gettext('Last reviewed')}, this.data.LastReviewDate);
        this.datetimeRender({Label: OCA.getI18n().gettext('Next review due')}, this.data.NextReviewDueDate);
    }
}
RiskView.prototype.gotControls = function($conLI, $conHeader, data){
    if (!data.length){
        $conLI.remove();
        $conHeader.remove();
        return; //no controls for this risk
    }

    var $clv = $("<ul>");
    for (var d=0; d < data.length; d++){
        var url;
        if (data[d].local){
            url = "#storage";
            data[d].Name = "(pending) " + data[d].Name;
        } else {
            var id = data[d].URL.split('/').pop();
            url = '#riskcontrolView?id=' + id;
        }
        $clv.append("<li><a href='" + url + "'><span class='icon risk_control pad-right'></span>" + data[d].Name +'</a></li>');
    }
    $conLI.append($clv);
    $clv.listview();
}
RiskView.prototype.renderRelations = function(){};

function RiskEdit(id, page){
    this.initRiskEdit(id, page);
}
RiskEdit.prototype = new TypeEdit;
RiskEdit.prototype.constructor = RiskEdit;
RiskEdit.prototype.initRiskEdit = function(id, page){
    this.initTypeEdit(id, page, "risk");
    this.defineLookup = {};
    this.supportsLocation = false;
};
RiskEdit.prototype.addAxisOptions = RiskView.prototype.addAxisOptions;
RiskEdit.prototype.getAxisOptions = RiskView.prototype.getAxisOptions;
RiskEdit.prototype.getRatingCell = RiskView.prototype.getRatingCell;
RiskEdit.prototype.optRender = function(field,data){
    field = this.addAxisOptions(field, data);
    var row = TypeEdit.prototype.optRender.call(this, field, data);
    if (field.Define){
        var self = this;
        field.Input.change(function(e){
            self.defineLookup[field.Define] = e.target.value;
            var define = field.Define.replace('XAXIS', '').replace('YAXIS', ''); //return first part of the string without XAXIS/YAXIS
            self.listview.trigger('change-' + define);
        });
    }
    return row;
}
RiskEdit.prototype.riskratingRender = function(field,data){
    var cell = this.getRatingCell(field);
    data = cell ? {Cell: cell} : null;
    field.Input = new MatrixInput(this, field, data).render();

    var self = this;
    this.listview.on('change-' + field.Input.defineSection, function(){
        cell = self.getRatingCell(field);
        data = cell ? {Cell: cell} : null;
        field.Input.updateField(data);
    });

    var row = field.Input.$row;
    TypeEdit.prototype.enhanceRow.call(this, row, field);
    return row;
}
RiskEdit.prototype.renderRelations = function(){};

function RiskNew(parentID, page){
    this.initRiskNew(parentID, page);
}
RiskNew.prototype = new RiskEdit;
RiskNew.prototype.constructor = RiskNew;
RiskNew.prototype.initRiskNew = function(parentID, page){
    this.parentID = parentID;
    this.initRiskEdit(null, page);
    this.createURL = '/riskcontext/' + parentID + '/risks';
}
RiskNew.prototype.getTypes = function(registerID){
    var url = this.typeEndpoint + 's';
    if (registerID) url += '?registerID=' + registerID;
    new Gopher(url, $.proxy(this.gotTypes, this), log.e).run();
};
RiskNew.prototype.hasChanged = TypeNew.prototype.hasChanged;
RiskNew.prototype.submission = function(submission){
    if (this.submitted) return;
    this.submitted = true;
    submission['TypeURL'] = Configuration.getAPIPath() + this.typeEndpoint + '/' + this.typeID;
    var desc = OCA.getI18n().gettext("Created new ") + this.typeData.Name;
    window.linkParams = {createdObject: 'Risk', message: desc};
    new Gopher({url: this.createURL, data: submission, desc: desc, oldTimestamp: this.timestamp}, function(){
		util.goBack();
    }, $.proxy(this.dataError, this)).post();
}

function MatrixInput(view, field, data){
    this.view = view;
    this.field = field;
    this.data = data;
    this.matrix = view.typeData.Matrix;
    this.defineSection = field.Define.replace('RATING', '');
    this.XInput = this.view.listview.find('.define-' + this.defineSection + 'XAXIS');
    this.YInput = this.view.listview.find('.define-' + this.defineSection + 'YAXIS');
}
MatrixInput.prototype.render = function(){
    this.$row = $("<li class='ui-field-contain ui-li-static matrix input' />")
        .append($("<label />").prop("for", this.field.Label.toLowerCase()).text(this.field.Label))
    this.$btn = $("<a href='#'>("+OCA.getI18n().gettext('none')+")</a>");
    if (this.data){
        this.updateField();
    }
    this.$btn.on('click', $.proxy(this.loadSelector, this));
    this.$row.append(this.$btn);
    this.view.listview.append(this.$row);
    return this;
}
MatrixInput.prototype.updateField = function(data){
    if (data !== undefined) this.data = data;
    if (this.data){
        this.$btn.text(this.data.Cell.Name).css('background-color', '#' + this.data.Cell.Colour);
    } else {
        this.$btn.text('('+OCA.getI18n().gettext('none')+')').css('background-color', '');
    }
}
MatrixInput.prototype.loadSelector = function(){
    linkParams.matrix = this.matrix;
    ViewUtil.selector.start({
        callbackOK: $.proxy(this.selectorCallback, this),
        data: this.data,
        previousObject: this
    });
    $("body").pagecontainer( "change", "#riskMatrixView?selector=true", {});

};
MatrixInput.prototype.selectorCallback = function(response){
    this.data = response;
    this.updateField();
    this.XInput.val(response.Cell.XIndex).change();
    this.YInput.val(response.Cell.YIndex).change();
}
MatrixInput.prototype.val = function(){ return null; }; //the value of matrix inputs is never actually submitted

/** render risk chooser field as an slmc with links to the items */
TypeView.prototype.riskchooserRender = function(field, data){
    return this.slmcRender(field, data, true);
};
/** render risk control chooser field as an slmc with links to the items */
TypeView.prototype.riskcontrolchooserRender = function(field, data){
    return this.slmcRender(field, data, true);
};
TypeView.prototype.riskcontextchooserRender = function(field, data){
    return this.slmcRender(field, data, true);
};

/** render risk chooser field as an slmc of type 'risk'*/
TypeEdit.prototype.riskchooserRender = function(field, data){
    return this.slmcRender(field, data, 'riskcontextTreeView?mode=risk');
};
/** render risk control chooser field as an slmc of type 'risk control'*/
TypeEdit.prototype.riskcontrolchooserRender = function(field, data){
    return this.slmcRender(field, data, 'riskcontextTreeView?mode=riskcontrol');
};
TypeEdit.prototype.riskcontextchooserRender = function(field, data){
    return this.slmcRender(field, data, 'riskcontextTreeView?mode=riskcontext');
}