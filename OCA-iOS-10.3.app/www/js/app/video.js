router.add({
    "#video": {
        handler: function (type, match, ui, page, e) {
            //if not allowed, redirect to settings page
            if (type != "pagebeforeshow") return;

            if (!util.isActivated()) {
                mediaVideo.$content.hide(); //TODO cant hide when coming via the menu
                settings.redirect = '#video';
                $("body").pagecontainer("change", $('#settings'), {reverse: false, changeHash: false});
            } else if (!OCA.checkFeature("INBOUNDCOMMS_SUBMIT")){	//logged in but old version
                $("body").pagecontainer("change", '#not-available', {changeHash: false});
			} else {
                mediaVideo.$content.show();
				app.checkLoaded();
            }
            e.preventDefault();
        },
        events: "bs"
    }
});
$(document).on("pageinit", "#video", function (e) {
    video.init($(this));
});
var mediaVideo = $.extend({}, media);
mediaVideo.Heading = '';
mediaVideo.type = 'video';
mediaVideo.doCapture = function (target) {
    var wasClicked = target.getAttribute('data-open');
    if (wasClicked == 'album') {
		Session.preserveDB = true;
        // open the gallery, only show videos
        navigator.camera.getPicture(function (uri) {
                video.attach(uri);
            },
            function (message) {
                console.log('get media failed');
                console.log(message);
            },
            { quality: 50,
                destinationType: navigator.camera.DestinationType.FILE_URI,
                sourceType: navigator.camera.PictureSourceType.PHOTOLIBRARY,
                mediaType: navigator.camera.MediaType.VIDEO
            }
        );
    } else {
        // open the capture device directly
        navigator.device.capture.captureVideo(
            function (mediaFiles) {
                var i, path, type;
                i = 0; // we only need one
                if (mediaFiles.length) {
                    path = mediaFiles[i].fullPath;
                    type = mediaFiles[i].type;
                } else {
                    return;
                }
                mediaVideo.mimeType = type;
                video.attach(path);
            }, mediaVideo.captureError, {}
        );
    }
};
mediaVideo.setThumbHtml = function (mediaUri) {
    if (device.platform == 'Win32NT'){
        //unable to embed a video element on WP8 because it has issues with the path. just show a file
        var html = '<div id="' + this.type + 'mediaThumb">' + ViewUtil.ocaicon('file medium') + '<br></div>';
        $('#video-info').text('');
        $('#' + this.type + '-placeholder').html(html);
        $('#home').width(); //video page sizes oddly on resumption. forcing it to calculate the page dimensions seems to reset it.
    } else {
        // include 'controls' attribute if you want to have controls
        var html = '<video controls id="' + this.type + 'mediaThumb"  width="150" webkit-playsinline>'
            + '<source src="' + mediaUri + '">'
            + '</video>';
        $('#' + this.type + '-placeholder').html(html);
        var $thumb = $('#' + this.type + 'mediaThumb');
        $thumb.attr('width', '100%'); // TODO: responsive design ^_^
    }
};

var video = $.extend({}, app, {
    init: function (page) {
        mediaVideo.init.apply(mediaVideo, [page]);
    },
    attach: function (Uri) {
        //for WP8
        // turn /VideoCache... into ///VideoCache... , which is the format returned by the image code
        // either format submits to the inbox, but only /// will be resolved in a way which detects filename and size
        if (device.platform == 'Win32NT' && Uri.indexOf('/VideoCache') === 0) {
            Uri = '//' + Uri;
        }
        mediaVideo.reset();
        mediaVideo.gotMedia(Uri);
    }
});