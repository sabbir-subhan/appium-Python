/**
 * media object provides the base implementation for media uploads.
 * Specific types (eg. video, audio, image) clone this object then customize their properties / methods as needed)
 * Things to customize / implement:
 *
 * - type, a property that identifies the type of media, eg. audio, photo, video.
 * - doCapture() , this function opens up the phone's capture device. eg. camera, audio recorder, file picker
 * - mimeType, typically set in the doCapture() method. It is given by cordova. Use default if you don't know the mime-type
 * - setThumbHtml(), sets a thumbnail / preview of the captured media item.
 *
 * You can also override any of the other methods, eg error handlers.
 *
 *  Notes on some features / conventions:
 *
 *  The type property
 *  The type property is used as a prefix for id attributes. Each media upload form have their own div container called a
 *  'placeholder'. For example, audio type has a #audio-placeholder.
 *
 *  Session
 *  Session restoration feature saves the link to the previously uploaded media item and restores these parameters.
 *
 *  Upload Progress Bar Indicator
 *  There's a nifty feature which will indicate a progress bar to your file upload. To see it, add a
 *  $('#' + this.type + '-progress') div container to your document.
 *  this.uploadProgress.update() will be called by cordova automatically through a callback.
 *
 *  Location
 *  The geo location of media items can be submitted too. Use the setLocation method. The location is also kept in the
 *  session.
 *
 *  Uploads
 *  The actual file upload is handled by Gopher.inboxSubmit()
 *  it uses cordova's FileTransfer() object to send to the inboxsubmit API end-point. Customize this.uploadMedia() to
 *  provide your own upload handling functionality
 *
 */
var media = {
    type: 'media', // override
    mimeType: 'application/octet-stream', // override
    noMediaMsg: 'No media captured',
    mediaUri: '',
    thumbUri: '',
    placeholderHTML: '',
    location: null,
    init: function (page) {
        this.$page = page;
        this.$content = this.$page.find('.ui-content');
        var $media = $('#' + this.type);
        var self = this;
        this.placeholderHTML = $('#' + this.type + '-placeholder').html();
        var deactivateButton = function ($obj) {
            // workaround to fix a bug where the button didn't remove ui-btn-active class automatically after clicking
            $obj.removeClass('ui-btn-active');
        };
        var $info = $('#' + this.type + '-info');
        if ($info.length) {
            this.noMediaMsg = $info.html();
        }

        $('#' + this.type + 'BtnReset').addClass('ui-disabled');
        $media.on('click', '#' + this.type + '-placeholder .icon', function (e) {
            // Retrieve image file location from specified source
            if (self.mediaUri) {
                // already media attached. User needs to cancel
                return;
            }
            navigator.geolocation.getCurrentPosition(
                function (pos) {
                    self.setLocation(pos);
                },
                function (error) {
                    // location error
                },
                {}
            );

            if (typeof self.doCapture === 'undefined') {
                // extended objects should override self.doCapture()
                navigator.camera.getPicture(function (uri) {
                        self.gotMedia.apply(self, [uri]);
                    },
                    function (message) {
                        console.log('get media failed');
                        console.log(message);
                    },
                    { quality: 50,
                        destinationType: navigator.camera.DestinationType.FILE_URI,
                        sourceType: navigator.camera.PictureSourceType.SAVEDPHOTOALBUM
                    }
                );
            } else {
                // capture method was overridden
                self.doCapture(e.target);
            }
            setTimeout(deactivateButton($(this)), 500);
        });
        $media.on('click', '#' + this.type + 'BtnSend', function (e) {
            self.uploadMedia();
            setTimeout(deactivateButton($(this)), 500);
        });
        $media.on('click', '#' + this.type + 'BtnReset', function (e) {
            self.cancel();
            setTimeout(deactivateButton($(this)), 500);
        });
        this.sessionRestore();
    },

    // error when capturing audio / video
    captureError: function (error) {
        switch (error.code) {
            case error.CAPTURE_INTERNAL_ERR:
                // camera or mic failed
                break;
            case error.CAPTURE_APPLICATION_BUSY:
                // currently serving another request
                break;
            case error.CAPTURE_INVALID_ARGUMENT:
                // invalid API use
                break;
            case error.CAPTURE_NO_MEDIA_FILES:
                // user exited with no files captured
                break;
            case error.CAPTURE_NOT_SUPPORTED:
                // feature not available on this device
                break;
            default:
            // unknown error
        }
    },

    sessionRestore: function () {
        // pre-saved data
        this.mediaUri = OCASession.get(this.type + 'mediaUri');
        this.location = OCASession.get(this.type + 'location');
        $('#' + this.type + '-input-description').val(OCASession.get(this.type + 'description'));
        this.renderThumb(this.thumbUri);
    },

    setLocation: function (pos) {
        this.location = pos;
        OCASession.set(this.type + 'location', pos);
    },

    setThumbHtml: function (mediaUri) {
        // by default it is img. If video or audio then extend this and embed a player
        $('#' + this.type + '-placeholder').html('<img id="' + this.type + 'mediaThumb" src=""> ');
        var $thumb = $('#' + this.type + 'mediaThumb');
        $thumb.attr('src', mediaUri);
        $thumb.attr('width', '150'); //
    },

    renderThumb: function (mediaUri) {
        if (mediaUri) {
            this.setThumbHtml(mediaUri);
            var type = this.type;
            window.resolveLocalFileSystemURL(mediaUri, function (fileEntry) {
                fileEntry.file(function (fileObj) {
                    console.log("Size = " + fileObj.size);
                    window.resolveLocalFileSystemURL(mediaUri, function (fileEntry) {
                        fileEntry.file(function (fileObj) {
                            var filename = mediaUri.substr(mediaUri.lastIndexOf('/') + 1);
                            $('#' + type + '-info').html(filename + '<br>' + (Math.round((fileObj.size / 1048576) * 100) / 100) + ' MB');
                        });
                    });
                });
            });
        } else {
            this.reset();
        }
    },

    gotMedia: function (mediaUri, thumbUri) {
        this.mediaUri = mediaUri;
        console.log('File path is: ' + mediaUri);
        OCASession.set(this.type + 'mediaUri', mediaUri);
        if (typeof thumbUri == 'undefined') {
            this.thumbUri = this.mediaUri;
        } else {
            this.thumbUri = thumbUri;
        }
        $('#' + this.type + 'BtnReset').removeClass('ui-disabled');
        this.renderThumb(this.thumbUri);
    },

    cancel: function () {
        // if no media, return to home otherwise
        this.reset();
        $('#' + this.type + 'BtnReset').addClass('ui-disabled');
    },
    // Implements onprogress, see http://docs.phonegap.com/en/2.4.0/cordova_file_file.md.html#FileTransfer
    uploadProgress: {
        update: function (progressEvent) {
            var $progress = $('#' + this.type + '-progress');
            if (progressEvent.lengthComputable) {
                var percent = 100;
                if (progressEvent.loaded != progressEvent.total) {
                    var scale;
                    scale = (parseInt($progress.find('.progress-bar').css('width'), 10) / 100);
                    percent = Math.round((progressEvent.loaded / progressEvent.total) * 100);
                    if ((percent % 10) == 0) {
                        $progress.find('.progress-bar-indicator').css('width', (percent * scale) + 'px');
                    }
                }
            }
        },

        start: function () {
            var $progress = $('#' + this.type + '-progress');
            $progress.show();
        },

        end: function () {
            var $progress = $('#' + this.type + '-progress');
            setTimeout(function () {
                $progress.find('.progress-bar-indicator').css('width', '0px');
                $progress.hide();
            }, 1000);
        }
    },


    // submit the media
    uploadMedia: function () {
        var $description = $('#' + this.type + '-input-description');
        if (!this.mediaUri.length) {
            return false;
        }
        var result = this.validate();
        if (!result.valid) {
            util.alertDialog(result.errors[0], jQuery.noop, 'Error', 'Ok');
        }
        // save body in case request fails.
        OCASession.set(this.type + 'description', $description.val());
        var lat = '';
        var lng = '';
        var accuracy = '';
        if (this.location != null) {
            console.log(JSON.stringify(this.location));
            lat = this.location.coords.latitude;
            lng = this.location.coords.longitude;
            accuracy = this.location.coords.accuracy;
        }
//        self.uploadProgress.start.apply(self);

		new Gopher({url: '/inboxitems', data: this.mediaUri}, $.proxy(this.win, this), $.proxy(this.fail, this)).inboxSubmit(
//            this.mediaUri,
            this.mimeType,
            $description.val(),
            lat, lng, accuracy
        );
        return true;
    },

    validate: function () {
        var result = {
            'valid': true,
            'errors': []
        };
        return result;
    },

    // media upload successful
    win: function (r) {
		// util.log('UPLOAD SUCCESS HANDLER', r);
        this.uploadProgress.end.apply(this);
//        console.log("Code = " + r.responseCode);
//        console.log("Response = " + r.response);
//        console.log("Sent = " + r.bytesSent);
        this.reset();
        $("body").pagecontainer("change", $('#home'), {reverse: false});
    },

    // media upload failed
    fail: function (error) {
        this.uploadProgress.end.apply(this);
        util.log("File transfer error", error);
        //401, 403 and 404 are known error statuses. handle these.
        switch (error.http_status){
            case 404:
                $("body").pagecontainer("change", '#not-available');
                return;
            case 401:
            case 403:
                util.alertDialog(OCA.getI18n().gettext('Authentication failure. Please re-activate your contact identifier'), jQuery.noop, 'Error', 'Ok');
                return;
        }
        //handle connection error, or else 
        switch (error.code) {
            case FileTransferError.CONNECTION_ERR:
                console.log('FileTransferError.CONNECTION_ERR');
                util.alertDialog(OCA.getI18n().gettext('Connection is offline, please try again later'), jQuery.noop, 'Error', 'Ok');
                return;
            case FileTransferError.INVALID_URL_ERR:     //shouldnt happen if comms is set up correctly for this account
            case FileTransferError.FILE_NOT_FOUND_ERR:  //sometimes returned generically when the http status is the real answer
            default:
                util.alertDialog(OCA.getI18n().gettext('Unable to submit media, please try again later'), jQuery.noop, 'Error', 'Ok');
        }
    },

    // clear the form
    reset: function () {
        OCASession.set(this.type + 'description', '');
        OCASession.set(this.type + 'mediaUri', '');
        $('#' + this.type + '-placeholder').html(this.placeholderHTML);
        $('#' + this.type + '-info').html(this.noMediaMsg + '<br>');
        this.mediaUri = '';
        $('#' + this.type + '-input-description').val('');
        // TODO delete the file.


    },

    launchFromIntent: function (type, uri) {
        if (type == "image") type = "photo";
        $("body").pagecontainer("change", '#' + type, {});
        window[type].attach(uri);
    }
};
