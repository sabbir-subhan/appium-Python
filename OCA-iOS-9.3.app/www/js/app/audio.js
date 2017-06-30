router.add({
    "#audio": {
        handler: function (type, match, ui, page, e) {
            //if not allowed, redirect to settings page
            if (type != "pagebeforeshow") return;

            if (!util.isActivated()) {
                mediaAudio.$content.hide(); //TODO cant hide when coming via the menu
                settings.redirect = '#audio';
                $("body").pagecontainer("change", $('#settings'), {reverse: false, changeHash: false});
            } else if (!OCA.checkFeature("INBOUNDCOMMS_SUBMIT")){	//logged in but old version
                $("body").pagecontainer("change", '#not-available', {changeHash: false});
			} else {
                mediaAudio.$content.show();
				app.checkLoaded();
            }
            e.preventDefault();
        },
        events: "bs"
    }
});
$(document).on("pageinit", "#audio", function (e) {
    audio.init($(this));
});
var mediaAudio = $.extend({}, media);
mediaAudio.Heading = '';
mediaAudio.type = 'audio';
mediaAudio.doCapture = function () {
	Session.preserveDB = true;
    navigator.device.capture.captureAudio(
        function (mediaFiles) {
            var i, path, len, type;
            for (i = 0, len = mediaFiles.length; i < len; i += 1) {
                path = mediaFiles[i].fullPath;
                type = mediaFiles[i].type;
                // do something interesting with the file
                console.log('Got this audio file: ' + path);
            }
            mediaAudio.mimeType = type;
            mediaAudio.gotMedia(path);
        }, mediaAudio.captureError
    );
};
mediaAudio.setThumbHtml = function (mediaUri) {
    // include 'controls' attribute if you want to have controls
    //var html = '<video id="' + this.type + 'mediaThumb"  width="80" webkit-playsinline >'
    //    +'<source src="'+mediaUri+'" type="'+mediaAudio.mimeType+'">'
    //    +'</video>';
    var html = '<div id="' + this.type + 'mediaThumb">' + ViewUtil.ocaicon('file medium') + '<br></div>';
    $('#audio-info').text('');
    $('#' + this.type + '-placeholder').html(html);
};
var audio = $.extend({}, app, {
    init: function (page) {
        mediaAudio.init.apply(mediaAudio, [page]);
        console.log('type is ' + media.type);
    },
    attach: function (Uri) {
        if (device.platform == 'Win32NT') { //as per the video page. futz with the paths.
            Uri = '//' + Uri;
        }
        mediaAudio.reset();
        mediaAudio.gotMedia(Uri);
    }
});
