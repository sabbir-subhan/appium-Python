router.add({
	"#about": function(type, match, ui, page, e){
		about.displaySystem();
	}
});
$(document).on("pageinit", "#about", function (e) {
    about.init($(this));
});
var about = {
	init: function(page){
		this.$page = page;
		this.$content = this.$page.find('.ui-content');
		if (
			device.platform.indexOf('iPhone') == 0 ||
			device.platform.indexOf('iPad')   == 0 ||
			device.platform.indexOf('iPod')   == 0 ||
			device.platform.indexOf('iOS')    == 0
		){
			this.$content.find('.oca-link').remove();
		}
        this.$content.find('.about.version').text('v ' + OCA.VERSION);

        this.displaySystem();
	},
    displaySystem: function(){
        var sys = [
            OCASession.getSessionId() ? Configuration.getClientUrl().replace('https://', '') : '',
        ];
        //show user, as long as its not dummy data
        if (OCASession.getUser() && OCASession.getUser() != 'cookie' && OCASession.getUser() != 'samlUser'){
            sys.push('Active user: ' + OCASession.getUser());
        }
        if (OCASession.getSessionId() && OCA.Packs){

            for (var p = 0; p < OCA.Packs.length; p++){
                var pack = OCA.Packs[p];
                sys.push(pack.Label + " (" + pack.Version + ")");
            }
        }
        sys = sys.join("<br />");

        this.$content.find('.about.system').html(sys);
    }
}
