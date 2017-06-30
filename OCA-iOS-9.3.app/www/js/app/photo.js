router.add({
    "#photo": {
        handler: function (type, match, ui, page, e) {
            //if not allowed, redirect to settings page
            if (type != "pagebeforeshow") return;

            if (!util.isActivated()) {
                mediaPhoto.$content.hide(); //TODO cant hide when coming via the menu
                settings.redirect = '#photo';
                $("body").pagecontainer("change", $('#settings'), {reverse: false, changeHash: false});
            } else if (!OCA.checkFeature("INBOUNDCOMMS_SUBMIT")){	//logged in but old version
                $("body").pagecontainer("change", '#not-available', {changeHash: false});
			} else {
                mediaPhoto.$content.show();
				app.checkLoaded();
            }
            e.preventDefault();
        },
        events: "bs"
    }
});
$(document).on("pageinit", "#photo", function (e) {
    photo.init($(this));
});
var mediaPhoto = $.extend({}, media);
mediaPhoto.Heading = '';
mediaPhoto.type = 'photo';
mediaPhoto.doCapture = function (target) {
    var wasClicked = target.getAttribute('data-open');
    var source;
    if (wasClicked == 'album') {
        source = navigator.camera.PictureSourceType.SAVEDPHOTOALBUM;
    } else if (wasClicked == 'camera') {
        source = navigator.camera.PictureSourceType.CAMERA;
    }
    if (source) {
		Session.preserveDB = true;
        navigator.camera.getPicture(function (uri) {
                photo.attach(uri);
            },
            function (message) {
                console.log('get media failed');
                console.log(message);
            },

            // note: out of memory problems on Android possible.
            // see http://simonmacdonald.blogspot.ca/2012/07/change-to-camera-code-in-phonegap-190.html
            { quality: 100,
                destinationType: navigator.camera.DestinationType.FILE_URI,
                encodingType: navigator.camera.EncodingType.JPEG,
                correctOrientation:true,
                sourceType: source,
				saveToPhotoAlbum: true
            }
        );
    }
};
var photo = $.extend({}, app, {
    init: function (page) {
        this.$page = page;
        this.$content = this.$page.find('.ui-content');
        mediaPhoto.init.apply(mediaPhoto, [page]);
    },

    attach: function (Uri) {
        mediaPhoto.reset();
        mediaPhoto.gotMedia(Uri);
    }
});


