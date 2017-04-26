from appium.webdriver.common.mobileby import MobileBy


class CommonScreen:
    """A class for handling Common buttons on different screen"""
    LOADING = (MobileBy.CSS_SELECTOR, 'span.ui-icon-loading')
    #OK_BUTTON = (MobileBy.CSS_SELECTOR, '')


class TopBar:
    """A class for top bar locators."""
    HAMBURGER_FOR_MAIN_MENU = (MobileBy.CSS_SELECTOR, 'div#iconbar>a')
    BACK_ARROW = (MobileBy.CSS_SELECTOR, 'div#header>div>a:first-child')


class WelcomeScreen:
    """A class for welcome screen locators - first screen after lunching the app."""
    LOCATION_BUTTON = (MobileBy.CSS_SELECTOR, 'div#locationMenu>a')
    MY_MESSAGES_BUTTON = (MobileBy.CSS_SELECTOR, 'div#appMessagesMenu>a')
    PHOTO_BUTTON = (MobileBy.CSS_SELECTOR, 'div#photoMenu>a')
    VIDEO_BUTTON = (MobileBy.CSS_SELECTOR, 'div#videoMenu>a')
    SOUND_BUTTON = (MobileBy.CSS_SELECTOR, 'div#audioMenu>a')
    SETTINGS_BUTTON = (MobileBy.CSS_SELECTOR, 'div#settingsMenu>a')
    ABOUT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#aboutMenu>a')
    LOGIN_BUTTON = (MobileBy.CSS_SELECTOR, 'div#sessionMenu>a')


class SettingsScreen:
    """A class for settings screen locators - screen after clicking settings button"""
    # SETTINGS_CONTACT_IDENTIFIER_FIELD = (MobileBy.CSS_SELECTOR, '')
    # SETTINGS_ALERT_APP_HAS_BEEN_ACTIVATED = (MobileBy.CSS_SELECTOR, '')
    # SETTINGS_OK_BUTTON = (MobileBy.CSS_SELECTOR, '')
    SETTINGS_ALERT_ABOUT_PIN = (MobileBy.CSS_SELECTOR, 'div#settings>div.ui-popup-container.ui-popup-active')
    SETTINGS_SAVE_BUTTON = (MobileBy.CSS_SELECTOR, 'a#settingsBtnSave')


class LoginScreen:
    """A class for login screen locators - screen after clicking LOGIN button"""
    TEXTFIELD_USERNAME = (MobileBy.CSS_SELECTOR, 'input#sessionUsername')
    TEXTFIELD_PASSWORD = (MobileBy.CSS_SELECTOR, 'input#sessionPassword')
    TEXTFIELD_DOMAIN = (MobileBy.CSS_SELECTOR, 'input#sessionDomain')
    SUBMIT_BUTTON = (MobileBy.CSS_SELECTOR, 'a#sessionSubmit')

    # Notification alert: "OCA now supports sending 'App Messages' to your device as notifications."
    NOTIFICATION_ABOUT_SENDING_MESSAGES = (MobileBy.CSS_SELECTOR, 'div#menu>div.ui-popup-container.ui-popup-active>div[data-role="popup"]>div.ng-dialog-container>p')

    # "No" button for sending notifications on iOS
    NO_FOR_SENDING_NOTIFICATIONS_ON = (MobileBy.CSS_SELECTOR, 'div#menu>div.ui-popup-container.ui-popup-active>div[data-role="popup"]>div[data-role="controlgroup"]>div>a[data-button-index="2"]')

    # ACCEPT_BUTTON on Terms and Conditions"
    ACCEPT_BUTTON = (MobileBy.CSS_SELECTOR, 'a#sessionTermsAccept')

    # # alert message with word "Invalid"
    # ALERT_MSG_INVALID = (MobileBy.CSS_SELECTOR, '')
    #
    # # alert message with "Your temporary account has been expired"
    # ALERT_MSG_EXPIRED = (MobileBy.CSS_SELECTOR, '')
    #
    # # alert message with "The password for the current user is about to expire"
    # ALERT_MSG_WILL_EXPIRE = (MobileBy.CSS_SELECTOR, '')
    #
    # # alert message with word "inactive"
    # ALERT_MSG_SUSPENDED = (MobileBy.CSS_SELECTOR, '')
    # # OK button on alert messages"
    # OK_BUTTON = (MobileBy.CSS_SELECTOR, '')


class MainMenuScreen(WelcomeScreen):
    """A class for main menu screen locators - first screen after correct login into the app."""
    MAIN_MENU = (MobileBy.CSS_SELECTOR, 'div#menu>div[data-role="main"]>div.ui-grid-b.home-icon-grid')
    ACTIVATE_WORKFLOW_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#workflowView?id=1201"]')
    CREATE_CONTACT_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#contactNew?parent=4&type=1"]')
    CREATE_TASK_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#taskNew"]')
    CREATE_REPORT_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#reportNew?type=1"]')
    # WEBSITE_LINK_BUTTON = (MobileBy.CSS_SELECTOR, '')
    INCIDENT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#menu>div[data-role="main"]>div>div>a[href="#emeNew?type=1"]')
    CREATE_ASSETS_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#assetNew?type=1"]')
    CREATE_LOG_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#logNew?type=1"]')
    RISKS_BUTTON = (MobileBy.CSS_SELECTOR, 'div#riskMenu>a')
    EVENTS_BUTTON = (MobileBy.CSS_SELECTOR, 'div#emeMenu>a')
    LOGS_BUTTON = (MobileBy.CSS_SELECTOR, 'div#logMenu>a')
    REPORTS_BUTTON = (MobileBy.CSS_SELECTOR, 'div#reportMenu>a')
    MAP_BUTTON = (MobileBy.CSS_SELECTOR, 'div#map>a')
    ASSETS_BUTTON = (MobileBy.CSS_SELECTOR, 'div#assetMenu>a')
    INBOX_BUTTON = (MobileBy.CSS_SELECTOR, 'div#inboxMenu>a')
    COMPOSE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#messageMenu>a')
    SENT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#sentMenu>a')
    TASKS_BUTTON = (MobileBy.CSS_SELECTOR, 'div#taskMenu>a')
    DOCUMENTS_BUTTON = (MobileBy.CSS_SELECTOR, 'div#documentMenu>a')
    CONTACTS_BUTTON = (MobileBy.CSS_SELECTOR, 'div#contactMenu>a')
    ALLOCATE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#resourceAllocationMenu>a')
    ACTIVATE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#workflowMenu>a')
    OFFLINE_SYNC_BUTTON = (MobileBy.CSS_SELECTOR, 'div#outboxMenu>a')
    LOGOUT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#sessionMenu>a')

    # ALERT_ACTIVATE_BUTTON = (MobileBy.CSS_SELECTOR, '')
    # ALERT_CANCEL_BUTTON = (MobileBy.CSS_SELECTOR, '')
    # ALERT_WORKFLOW_ACTIVATED = (MobileBy.CSS_SELECTOR, '')


class LocationScreen:
    """A class for Location screen locators - screen after clicking into Location button in Main Menu."""
    SEND_ONCE_NOW = (MobileBy.CSS_SELECTOR, '')
    SEND_EVERY_SPINNER = (MobileBy.CSS_SELECTOR, '')
    CHOOSE_5_MINUTES_OPTION_iPad = (MobileBy.CSS_SELECTOR, '')
    ASSERT_5_MINUTES_OPTION = (MobileBy.CSS_SELECTOR, '')
    FOR_THE_NEXT_SPINNER = (MobileBy.CSS_SELECTOR, '')
    CHOOSE_1_HOUR_OPTION_iPad = (MobileBy.CSS_SELECTOR, '')
    ASSERT_1_HOUR_OPTION = (MobileBy.CSS_SELECTOR, '')
    START_BUTTON = (MobileBy.CSS_SELECTOR, 'button#locationStart')
    STOP_BUTTON = (MobileBy.CSS_SELECTOR, '')
    TRACKING_HISTORY_BUTTON = (MobileBy.CSS_SELECTOR, '')
    LOCATION_PAGE_HEADER = (MobileBy.CSS_SELECTOR, '')
    LOCATION_STATUS = (MobileBy.CSS_SELECTOR, '')


class EventsScreen:
    """A class for Events screen locators - screen after clicking into Events button in Main Menu."""
    #EVENTS_HEADER = (MobileBy.CSS_SELECTOR, '')

    # # filtering events by Type
    # ANY_TYPE_EXPAND = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div[data-role="main"]>div.filters>div[data-role="collapsible"]>h2>a>span[data-translate="Any Type"]')
    # CHOOSE_TYPE_INCIDENT = (MobileBy.CSS_SELECTOR, '')
    # INCIDENT_TYPE_EXPAND = (MobileBy.CSS_SELECTOR, '')
    # CHOOSE_TYPE_ANY = (MobileBy.CSS_SELECTOR, '')
    #
    # # filtering events by Status
    # ANY_STATUS_EXPAND = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div[data-role="main"]>div.filters>div[data-role="collapsible"]>h2>a>span[data-translate="Any Status"]')
    # CHOOSE_ACTIVE_STATUS = (MobileBy.CSS_SELECTOR, '')
    # ACTIVE_STATUS_EXPAND = (MobileBy.CSS_SELECTOR, '')
    # CHOOSE_INACTIVE_STATUS = (MobileBy.CSS_SELECTOR, '')
    # INACTIVE_STATUS_EXPAND = (MobileBy.CSS_SELECTOR, '')
    # CHOOSE_DRAFT_STATUS = (MobileBy.CSS_SELECTOR, '')
    # DRAFT_STATUS_EXPAND = (MobileBy.CSS_SELECTOR, '')
    # CHOOSE_ANY_STATUS = (MobileBy.CSS_SELECTOR, '')

    # filtering events using search field
    SEARCH_FIELD = (MobileBy.CSS_SELECTOR, 'input#emeSearch')

    # creating and editing Events
    #MORE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.ui-block-b>a[href="#"]')
    NEW_EVENT_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#emeNew?parent=0"]')

    # previously created event
    PREVIOUSLY_CREATED_EVENT = (MobileBy.CSS_SELECTOR, 'ul.emes.listview.ui-listview>li:first-child>a')
    PREVIOUSLY_CREATED_EVENT_CHECKBOX = (MobileBy.CSS_SELECTOR, 'ul.emes.listview.ui-listview>li:first-child>div.ui-checkbox')

    #CLEAR_PRIMARY_EVENT_BUTTON = (MobileBy.CSS_SELECTOR, 'li.primary.eme.clear.ui-first-child>a')
    #NOTIFICATION_PRIMARY_EVENT_CLEARED = (MobileBy.CSS_SELECTOR, '')


class TypesOfEventsScreen:
    """A class for Type of Events screen locators - first screen after creating new event with types of events."""
    # INCIDENT_TYPE_OF_EVENT = (MobileBy.CSS_SELECTOR, '')
    # EVENT_FOR_ON_LOAD_SAVE = (MobileBy.CSS_SELECTOR, '')
    # EVENT_FOR_CHOOSER_FIELDS = (MobileBy.CSS_SELECTOR, '')


class EventEditScreen:
    """A class for Edit Events screen locators - screen after opening edit mode of event or creating a new one."""
    SAVE_BUTTON_NEW_EVENT = (MobileBy.CSS_SELECTOR, 'div#emeNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                                    'a[href="#save"]')
    CANCEL_BUTTON = (MobileBy.CSS_SELECTOR, 'div#emeNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                            'a[href="#cancel"]')
    SAVE_BUTTON_EDIT_EVENT = (MobileBy.CSS_SELECTOR, 'div#emeEdit>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                                     'a[href="#save"]')
    CANCEL_BUTTON_EDIT_EVENT = (MobileBy.CSS_SELECTOR, 'div#emeEdit>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                                       'a[href="#cancel"]')
    NAME_FIELD = (MobileBy.CSS_SELECTOR, 'div#emeNew>div>ul>li>div>input#name')
    SEVERITY_LEVEL_SELECTOR = (MobileBy.CSS_SELECTOR, 'div#emeNew>div>ul>li>div>div>select[name="severity"]')  # for new event
    SEVERITY_LEVEL_SELECTOR_EDIT_EVENT = (MobileBy.CSS_SELECTOR, 'div#emeEdit>div>ul>li>div>div>select[name="severity"]')
    # CHOOSE_SEVERITY_LVL1_iPad = (MobileBy.CSS_SELECTOR, '')
    # CHOOSE_SEVERITY_LVL2_iPad = (MobileBy.CSS_SELECTOR, '')
    # CHOOSE_SEVERITY_LVL3_iPad = (MobileBy.CSS_SELECTOR, '')
    # CHOOSE_SEVERITY_LVL4_iPad = (MobileBy.CSS_SELECTOR, '')
    # CHOOSE_SEVERITY_LVL5_iPad = (MobileBy.CSS_SELECTOR, '')
    FINISHED_FIELD = (MobileBy.CSS_SELECTOR, '')
    DESCRIPTION_FIELD = (MobileBy.CSS_SELECTOR, 'iframe[title="Rich Text Editor, description"]')
    CREATE_MAPPING_DATA = (MobileBy.CSS_SELECTOR, 'div#emeEdit>div>ul.edit-view.ui-listview>li.geometryinput>a')
    EDIT_MAPPING_DATA = (MobileBy.CSS_SELECTOR, '')
    ELEMENT_TO_SCROLL = (MobileBy.CSS_SELECTOR, '')
    SEQUENCE_ONLOAD_HEADER = (MobileBy.CSS_SELECTOR, '')
    SEQUENCE_ONLOAD_VALUE = (MobileBy.CSS_SELECTOR, '')
    SEQUENCE_ONSAVE_HEADER = (MobileBy.CSS_SELECTOR, '')
    SEQUENCE_ONSAVE_VALUE = (MobileBy.CSS_SELECTOR, '')
    NEW_OPTION_LIST_HEADER = (MobileBy.CSS_SELECTOR, '')
    OPTION_LIST_VALUE_1 = (MobileBy.CSS_SELECTOR, '')
    OPTION_LIST_VALUE_2 = (MobileBy.CSS_SELECTOR, '')
    OPTION_LIST_VALUE_3 = (MobileBy.CSS_SELECTOR, '')
    FIELD_TO_RESTORE_1_HEADER = (MobileBy.CSS_SELECTOR, '')
    FIELD_TO_RESTORE_1_VALUE = (MobileBy.CSS_SELECTOR, '')
    FIELD_TO_RESTORE_2_HEADER = (MobileBy.CSS_SELECTOR, '')
    FIELD_TO_RESTORE_2_VALUE = (MobileBy.CSS_SELECTOR, '')
    CHOOSER_FIELD = (MobileBy.CSS_SELECTOR, '')
    SUBFORM_FIELD_ADD_ROW = (MobileBy.CSS_SELECTOR, 'div.subform>a')
    NEW_EVENTS_CHOOSER_IN_SUB_FORM = (MobileBy.CSS_SELECTOR, 'div.subform>div.subform-row>ul.subform-row>li>div.ui-select')
    DELETE_SUB_EVENT_FROM_CHOOSER = (MobileBy.CSS_SELECTOR, 'div.subform>div.subform-row>a.delete')


class EventDetailsScreen:
    """A class for Event Details screen locators - screen with event details - after opening event."""
    EDIT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#emeView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.edit.ui-block-a>a')
    DELETE_EVENT_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#confirmDeleteEME"]')
    DELETE_CONFIRM_BUTTON = (MobileBy.CSS_SELECTOR, '')
    MORE_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#emeViewMoreMenu"]')
    NEW_SUB_EVENT = (MobileBy.CSS_SELECTOR, 'li.eme.new.subeme>a')
    SET_AS_PRIMARY_BUTTON = (MobileBy.CSS_SELECTOR, 'li.primary.eme.set.ineme.ui-first-child>a')
    EVENT_INFO_BUTTON = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.ui-block-a>a.emeView')


class Map:
    """A class for Map screen locators."""
    PLOT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-b>li#mapPlot>a')
    TOOL_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div[data-role="footer"]>div.ui-navbar>ul.ui-grid-b>li#openMapToolMore>a[href="#mapToolMore"]')
    POINT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div#mapToolMore-popup>div#mapToolMore>div[data-collapsed-icon="arrow-d"]>div[data-wkt="POINT"]>h2>a')
    POINT_DEFAULT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div#mapToolMore-popup>div#mapToolMore>div[data-collapsed-icon="arrow-d"]>div[data-wkt="POINT"]>div>ul>li>a')
    LINE_DEFAULT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div#mapToolMore-popup>div#mapToolMore>div[data-collapsed-icon="arrow-d"]>div[data-wkt="LINESTRING"]>div>ul>li>a')
    CIRCLE_DEFAULT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div#mapToolMore-popup>div#mapToolMore>div[data-collapsed-icon="arrow-d"]>div[data-wkt="CIRCLE"]>div>ul>li>a')
    POLYGON_DEFAULT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div#mapToolMore-popup>div#mapToolMore>div[data-collapsed-icon="arrow-d"]>div[data-wkt="POLYGON"]>div>ul>li>a')
    # MAP_AREA_12 = (MobileBy.CSS_SELECTOR, '')
    # MAP_AREA_13 = (MobileBy.CSS_SELECTOR, '')
    # MAP_AREA_17 = (MobileBy.CSS_SELECTOR, '')
    MAP_AREA_18 = (MobileBy.CSS_SELECTOR, 'div#mapPage>div.ui-content>div#mapCanvas>div#mapCanvas_root>div#mapCanvas_container>div#mapCanvas_layers>div#mapCanvas_layer0>div>img#mapCanvas_layer0_tile_12_2_2')
    LINE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div#mapToolMore-popup>div#mapToolMore>div[data-collapsed-icon="arrow-d"]>div[data-wkt="LINESTRING"]>h2>a')
    CIRCLE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div#mapToolMore-popup>div#mapToolMore>div[data-collapsed-icon="arrow-d"]>div[data-wkt="CIRCLE"]>h2>a')
    POLYGON_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div#mapToolMore-popup>div#mapToolMore>div[data-collapsed-icon="arrow-d"]>div[data-wkt="POLYGON"]>h2>a')
    SAVE_MAP_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                              'a[data-translate="Save"]')
    CANCEL_MAP_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                                'a[data-translate="Cancel"]')
    LAYERS = (MobileBy.CSS_SELECTOR, 'div#mapPage>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-b>li.ui-block-a>a[href="#mapLayers"]')
    FIRST_LAYER_ON_THE_LIST = (MobileBy.CSS_SELECTOR, 'div#mapLayers>div.ui-content>ul>li:first-child')
    LAYERS_DONE = (MobileBy.CSS_SELECTOR, 'div#mapLayers>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.ui-block-a>a#layersDone')
    PLOT_TYPE_ASSET = (MobileBy.CSS_SELECTOR, 'div#mapPlotType>div.ui-content>ul.ui-listview>li>a[data-link="#assetNew?parent=0"]')


class PhotoScreen:
    """A class for Photo screen locators - screen after clicking into Photo button in Main Menu."""
    #PHOTO_PAGE_HEADER = (MobileBy.CSS_SELECTOR, '')
    GALLERY_BUTTON = (MobileBy.CSS_SELECTOR, 'div#photo>div.ui-content>div#photo-placeholder>div.ui-block-a>div.center-text>span[data-open="album"]>span.icon')
    TAKE_NEW_BUTTON = (MobileBy.CSS_SELECTOR, 'div#photo>div.ui-content>div.ui-grid-a>div.ui-block-b>div.center-text>span[data-open="camera"]>span.icon')
    DESCRIPTION_FIELD = (MobileBy.CSS_SELECTOR, 'textarea#photo-input-description')
    SEND_BUTTON = (MobileBy.CSS_SELECTOR, 'div#photo>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.ui-block-a>a#photoBtnSend')
    RESET_BUTTON = (MobileBy.CSS_SELECTOR, 'a#photoBtnReset')


class VideoScreen:
    """A class for Video screen locators - screen after clicking into Video button in Main Menu."""
    #VIDEO_PAGE_HEADER = (MobileBy.CSS_SELECTOR, '')
    GALLERY_BUTTON = (MobileBy.CSS_SELECTOR, 'div#video>div.ui-content>div#video-placeholder>div.ui-block-a>div.center-text>span[data-open="album"]>span.icon')
    RECORD_NEW_BUTTON = (MobileBy.CSS_SELECTOR, 'div#video>div.ui-content>div.ui-grid-a>div.ui-block-b>div.center-text>span[data-open="camera"]>span.icon')
    SEND_BUTTON = (MobileBy.CSS_SELECTOR, 'div#video>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.ui-block-a>a#videoBtnSend')
    DESCRIPTION_FIELD = (MobileBy.CSS_SELECTOR, 'textarea#video-input-description')


class SoundScreen:
    """A class for Sound screen locators - screen after clicking into Sound button in Main Menu."""
    #SOUND_PAGE_HEADER = (MobileBy.CSS_SELECTOR, '')
    RECORD_SOUND_BUTTON = (MobileBy.CSS_SELECTOR, 'div#audio>div>div.ui-grid-a>div#audio-placeholder>span')
    DESCRIPTION_FIELD = (MobileBy.CSS_SELECTOR, 'textarea#audio-input-description')
    SEND_BUTTON = (MobileBy.CSS_SELECTOR, 'div#audio>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.ui-block-a>a#audioBtnSend')


# class SoundRecorderScreen:
#     """A class for Sound Recorder screen locators - screen after clicking into record sound button in Sound Page."""
#     RECORD_SOUND = (MobileBy.CSS_SELECTOR, 'toggle audio recording')
#     DONE_BUTTON = (MobileBy.CSS_SELECTOR, 'Done')
#
#
# class GalleryScreen:
#     """A class for handling Gallery"""
#     GALLERY_ELEMENT_1 = (MobileBy.CSS_SELECTOR, '//XCUIElementTypeCell[@name[contains(., "Photo")]][1]')
#     GALLERY_VIDEOS_POPOVER = (MobileBy.CSS_SELECTOR, '//XCUIElementTypeButton[@name="Videos"]')
#     GALLERY_VIDEO_ELEMENT_1 = (MobileBy.CSS_SELECTOR, '//XCUIElementTypeCell[1]')
#     USE_BUTTON = (MobileBy.CSS_SELECTOR, 'Choose')


# class CameraScreen:
#     """A class for handling Camera"""
#     PHOTO_CAPTURE = (MobileBy.CSS_SELECTOR, 'PhotoCapture')
#     CANCEL_BUTTON = (MobileBy.CSS_SELECTOR, 'Cancel')
#     CAMERA_CHOOSER = (MobileBy.CSS_SELECTOR, 'FrontBackFacingCameraChooser')
#     RETAKE = (MobileBy.CSS_SELECTOR, 'Retake')
#     USE_PHOTO = (MobileBy.CSS_SELECTOR, 'Use Photo')
#     VIDEO_CAPTURE = (MobileBy.CSS_SELECTOR, 'VideoCapture')  # record and stop recording
#     USE_VIDEO = (MobileBy.CSS_SELECTOR, 'Use Video')


class NewContactScreen:
    """A class for handling New Contact screen"""
    SAVE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#contactNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                          'a[href="#save"]')
    CANCEL_BUTTON = (MobileBy.CSS_SELECTOR, 'div#contactNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                            'a[href="#cancel"]')
    FIRST_NAME = (MobileBy.CSS_SELECTOR, 'input[id="first name"]')


class NewTaskScreen:
    """A class for handling New Task screen"""
    SAVE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#taskNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                          'a[href="#save"]')
    CANCEL_BUTTON = (MobileBy.CSS_SELECTOR, 'div#taskNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                            'a[href="#cancel"]')
    TITLE = (MobileBy.CSS_SELECTOR, 'input.field-Name')
    # ASSIGNED = (MobileBy.CSS_SELECTOR, '')
    # ADD_CONTACTS_AND_GROUPS = (MobileBy.CSS_SELECTOR, '')
    # ADD_RESOURCE_STRUCTURE_NODES = (MobileBy.CSS_SELECTOR, '')
    # ADD_RESOURCE_ASSIGNMENTS = (MobileBy.CSS_SELECTOR, '')
    # CHOOSE_USERS = (MobileBy.CSS_SELECTOR, '')
    # CHOOSE_CONTACTS = (MobileBy.CSS_SELECTOR, '')
    # START_DATE = (MobileBy.CSS_SELECTOR, '')
    # HIDE_DATE_PICKER = (MobileBy.CSS_SELECTOR, '')


class ReportsScreen:
    """A class for handling Reports screen"""
    TITLE = (MobileBy.CSS_SELECTOR, 'div#reportNew>div.ui-content>ul.edit-view>li:first-child>div>input#title')
    LODGING_AGENCY_PICKER = (MobileBy.CSS_SELECTOR, 'div#field-1201-button>select[name="lodging agency"]')
    # LODGING_AGENCY = (MobileBy.CSS_SELECTOR, '')  # picker wheel on iOS and popup on Android are native elements
    PUBLISH_NEW_REPORT = (MobileBy.CSS_SELECTOR, 'div#reportNew>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-b>li.ui-block-a>a[href="#save"]')
    CANCEL_NEW_REPORT = (MobileBy.CSS_SELECTOR, 'div#reportNew>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-b>li.ui-block-c>a[href="#cancel"]')
    PUBLISH_EDITED_REPORT = (MobileBy.CSS_SELECTOR, 'div#reportEdit>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-b>li.ui-block-a>a[href="#save"]')
    CANCEL_EDITED_REPORT = (MobileBy.CSS_SELECTOR, 'div#reportEdit>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-b>li.ui-block-c>a[href="#cancel"]')
    TYPE_FILTER = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:first-child>h2>a')
    FIRST_TYPE = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:first-child>div>ul[data-role="listview"]>li:first-child>a')  # ALL REPORTS
    SECOND_TYPE = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:first-child>div>ul[data-role="listview"]>li:nth-child(2)>a')  # MEDIA RELEASE
    THIRD_TYPE = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:first-child>div>ul[data-role="listview"]>li:nth-child(3)>a')  # REPORT_FOR_TESTS
    FOURTH_TYPE = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:first-child>div>ul[data-role="listview"]>li:nth-child(4)>a')  # SITUATION REPORT
    STATUS_FILTER = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:nth-child(2)>h2>a')
    FIRST_STATUS = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:nth-child(2)>div>ul[data-role="listview"]>li:first-child>a')  # ANY STATUS
    SECOND_STATUS = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:nth-child(2)>div>ul[data-role="listview"]>li:nth-child(2)>a')  # ACTIVE
    THIRD_STATUS = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:nth-child(2)>div>ul[data-role="listview"]>li:nth-child(3)>a')  # INACTIVE
    FOURTH_STATUS = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:nth-child(2)>div>ul[data-role="listview"]>li:nth-child(4)>a')  # DRAFT
    SEARCH_FIELD = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div.ui-input-search>input#reportSearch')
    CREATE_REPORT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-solo>li>a[href="#reportNew"]')
    EDIT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#reportView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.edit>a')
    FIRST_REPORT_ON_THE_LIST = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div.main>ul>li:first-child>a')
    MORE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#reportView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li:last-child>a[href="#reportViewMoreMenu"]')
    DELETE_REPORT = (MobileBy.CSS_SELECTOR, 'div#reportView>div.ui-popup-container>div#reportViewMoreMenu>ul>li.report.delete>a')
    EDIT_REPORT_TITLE = (MobileBy.CSS_SELECTOR, 'div#reportEdit>div.ui-content>ul.edit-view>li:first-child>div>input#title')
    DELETE_ALERT = (MobileBy.CSS_SELECTOR, 'div#reportView>div#confirmDeleteReport-popup>div#confirmDeleteReport>div.ng-dialog-container>div>div.ui-controlgroup-controls>a:first-child')
    ASSETS_CHOOSER_FIELD = (MobileBy.CSS_SELECTOR, 'div#reportEdit>div.ui-content>ul.edit-view>li[name="new assets chooser"]>div.ui-select>div')  # inside already created report
    CREATE_MAPPING_DATA = (MobileBy.CSS_SELECTOR, 'div#reportEdit>div.ui-content>ul.edit-view>li.geometryinput>a')
    SEQUENCE_ON_LOAD = (MobileBy.CSS_SELECTOR, 'div#reportNew>div.ui-content>ul.edit-view>li.ui-field-contain.ui-li-static.ui-body-inherit>label[for="on_load"]')
    SEQUENCE_ON_SAVE = (MobileBy.CSS_SELECTOR, 'div#reportNew>div.ui-content>ul.edit-view>li.ui-field-contain.ui-li-static.ui-body-inherit>label[for="on_save"]')


class LogsScreen:
    """A class for handling New Log screen"""
    SAVE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#logNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                          'a[href="#save"]')
    CANCEL_BUTTON = (MobileBy.CSS_SELECTOR, 'div#logNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                            'a[href="#cancel"]')
    # LODGING_AGENCY_PICKER = (MobileBy.CSS_SELECTOR, '')
    ENTRY_FIELD = (MobileBy.CSS_SELECTOR, 'iframe[title="Rich Text Editor, entry"]')  # not working on iOS10
    TYPES_FILTER = (MobileBy.CSS_SELECTOR, 'div#logIndex>div.ui-content>div[data-role="collapsible"]>h2>a')
    FIRST_FILTER = (MobileBy.CSS_SELECTOR, 'div#logIndex>div.ui-content>div[data-role="collapsible"]>div>ul>li:first-child>a')
    SECOND_FILTER = (MobileBy.CSS_SELECTOR, 'div#logIndex>div.ui-content>div[data-role="collapsible"]>div>ul>li:nth-child(2)>a')
    THIRD_FILTER = (MobileBy.CSS_SELECTOR, 'div#logIndex>div.ui-content>div[data-role="collapsible"]>div>ul>li:nth-child(3)>a')


class SentScreen:
    """A class for handling Sent screen"""
    # SEARCH = EventsScreen.SEARCH_FIELD
    SENT_COMMUNICATIONS_EMAIL = (MobileBy.CSS_SELECTOR, '')


class ComposeScreen:
    """A class for handling Compose screen"""
    ADD_RECIPIENTS_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#messageAddRecipients"]')
    MESSAGE_EMAIL = (MobileBy.CSS_SELECTOR, 'a[href="#messageEmail"]')
    EMAIL_SUBJECT_FIELD = (MobileBy.CSS_SELECTOR, 'input#emailSubject')
    EMAIL_TEXT_FIELD = (MobileBy.CSS_SELECTOR, 'iframe[title="Rich Text Editor, emailBody"]')
    EMAIL_OK = (MobileBy.CSS_SELECTOR, '#EmailOK')
    MESSAGE_SMS = (MobileBy.CSS_SELECTOR, 'a[href="#messageSMS"]')
    SMS_TEXT_FIELD = (MobileBy.CSS_SELECTOR, '#SMSBody')
    SMS_OK = (MobileBy.CSS_SELECTOR, '#SMSOK')
    MESSAGE_VOICE = (MobileBy.CSS_SELECTOR, 'a[href="#messageVoice"]')
    VOICE_TEXT_FIELD = (MobileBy.CSS_SELECTOR, '#voiceText')
    TEXT_TO_SPEECH_BUTTON = (MobileBy.CSS_SELECTOR, '#voiceTextMethod>a')
    VOICE_OK = (MobileBy.CSS_SELECTOR, '#voiceOK')
    MESSAGE_FAX = (MobileBy.CSS_SELECTOR, 'a[href="#messageFax"]')
    FAX_DOCUMENT_BUTTON = (MobileBy.CSS_SELECTOR, '#faxDocumentMethod')
    FAX_OK_BUTTON = (MobileBy.CSS_SELECTOR, 'div#messageFax>div[data-role="footer"]>div[data-role="navbar"]>ul>li.ui-block-a>a')
    COMMS_DOCUMENTS_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#documentfolderTreeView?selector=true&id=2"]')
    ADD_CONTACTS_AND_GROUPS = (MobileBy.CSS_SELECTOR, 'a.maywrap.ui-link.ui-btn.ui-shadow.ui-corner-all')  # list of two elements - select [0]
    ADD_RESOURCES_STRUCTURE_NODES = (MobileBy.CSS_SELECTOR, 'a.maywrap.ui-link.ui-btn.ui-shadow.ui-corner-all')  # list of two elements - select [1]
    CONTACTS_ARROW = (MobileBy.CSS_SELECTOR, 'a[href="#contactgroupTreeView?selector=true&id=4"]')
    USERS_ARROW = (MobileBy.CSS_SELECTOR, 'a[href="#contactgroupTreeView?selector=true&id=3"]')
    CONTACT_FOR_APPIUM_TESTS = (MobileBy.CSS_SELECTOR, 'input[data-label="A_CONTACT_FOR_APPIUM_TESTS"]')
    SEND_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#confirmSendMessage"]')
    ALERT_SEND_BUTTON = (MobileBy.CSS_SELECTOR, 'div.ui-controlgroup-controls>a#messageSend')


class RisksScreen:
    """A class for handling Risks screen"""
    CREATE_RISK_REGISTER = (MobileBy.CSS_SELECTOR, 'a[href="#riskregisterNew"]')
    NAME_FOR_NEW_RISK_REGISTER = (MobileBy.CSS_SELECTOR, 'input#name')
    CREATE_NEW_CONTEXT_INPUT_FIELD = (MobileBy.CSS_SELECTOR, 'input[id="or create new context"]')
    SAVE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#riskregisterNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                          'a[href="#save"]')
    CANCEL_BUTTON = (MobileBy.CSS_SELECTOR, 'div#riskregisterNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                            'a[href="#cancel"]')
    # PREVIOUSLY_CREATED_RISK_REGISTER = (MobileBy.CSS_SELECTOR, 'div#riskRegisterIndex>div.ui-content>ul.registers>li:first-child')  # not working on iOS 10
    # PREVIOUSLY_CREATED_CONTEXT = (MobileBy.CSS_SELECTOR, 'div#riskcontextTreeView>div.ui-content>ul.contexts>li:first-child')
    # PREVIOUSLY_CREATED_RISK = (MobileBy.CSS_SELECTOR, 'div#riskcontextTreeView>div.ui-content>ul.risks>li:first-child')
    LIBRARY_CONTROL = (MobileBy.CSS_SELECTOR, 'div#riskcontrollibraryTreeView>div.ui-content>ul.category>li:first-child')
    PREVIOUSLY_CREATED_RISK_REGISTER = (MobileBy.CSS_SELECTOR, 'ul.registers.listview.ui-listview>li>a')
    PREVIOUSLY_CREATED_CONTEXT = (MobileBy.CSS_SELECTOR, 'ul.contexts.listview.ui-listview>li>a')
    PREVIOUSLY_CREATED_RISK = (MobileBy.CSS_SELECTOR, 'ul.risks.listview.ui-listview>li>a')
    RISK_REGISTERS_LIST = (MobileBy.CSS_SELECTOR, 'ul.registers.listview.ui-listview>li:first-child>a')
    NEW_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#riskcontextTreeMoreMenu"]')
    ADD_NEW_CONTEXT = (MobileBy.CSS_SELECTOR, 'a[href="#riskcontextNew?parent=0"]')
    ADD_NEW_RISK = (MobileBy.CSS_SELECTOR, 'ul.context.footer.menu.ui-listview>li.new.risk>a')
    ADD_NEW_CONTEXT_IN_EXISTING_CONTEXT = (MobileBy.CSS_SELECTOR, 'ul.context.footer.menu.ui-listview>li.new.riskcontext>a')
    ADD_NEW_LIBRARY_RISK = (MobileBy.CSS_SELECTOR, 'ul.context.footer.menu.ui-listview>li.library>a')
    SEARCH_FIELD = (MobileBy.CSS_SELECTOR, 'input#riskregisterSearch')
    NAME_FOR_NEW_CONTEXT = (MobileBy.CSS_SELECTOR, 'div#riskcontextNew>div>ul>li.ui-field-contain.ui-li-static.ui-body-inherit>div>input#name')
    NAME_FOR_NEW_RISK = (MobileBy.CSS_SELECTOR, 'div#riskNew>div>ul>li>div>input#name')
    SAVE_NEW_CONTEXT = (MobileBy.CSS_SELECTOR, 'div#riskcontextNew>div[data-role="footer"]>div>ul>li>a[href="#save"]')
    SAVE_NEW_RISK = (MobileBy.CSS_SELECTOR, 'div#riskNew>div[data-role="footer"]>div>ul>li>a[href="#save"]')
    OK_BUTTON = (MobileBy.CSS_SELECTOR, 'div#risklibraryTreeView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.ui-block-a>a')
    OK_BUTTON_IN_RISK_CONTROL_LIBRARY = (MobileBy.CSS_SELECTOR, 'div#riskcontrollibraryTreeView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.ui-block-a>a')
    MORE_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#riskViewMoreMenu"]')
    ADD_NEW_CONTROL = (MobileBy.CSS_SELECTOR, 'li.new.control>a')
    ADD_LIBRARY_CONTROL = (MobileBy.CSS_SELECTOR, 'li.library.control>a')
    MARK_AS_REVIEWED = (MobileBy.CSS_SELECTOR, 'a[href="#confirmReviewRisk"]')
    DELETE_RISK = (MobileBy.CSS_SELECTOR, 'a[href="#confirmDeleteRisk"]')
    NAME_FOR_NEW_CONTROL = (MobileBy.CSS_SELECTOR, 'div#riskcontrolNew>div>ul.edit-view.ui-listview>li>div>input#name')
    STATUS_SELECTOR = (MobileBy.CSS_SELECTOR, 'div#field-101-button>select#field-101')
    SAVE_NEW_CONTROL = (MobileBy.CSS_SELECTOR, 'div#riskcontrolNew>div[data-role="footer"]>div>ul>li>a[href="#save"]')
    VIEW_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#riskcontextTreeViewMenu"]')
    VIEW_REGISTER_BUTTON = (MobileBy.CSS_SELECTOR, 'li.root.ui-last-child>a')
    REGISTER_VIEW = (MobileBy.CSS_SELECTOR, 'div#riskregisterView>div[data-role="main"]')
    DELETE_ALERT = (MobileBy.CSS_SELECTOR, 'div#confirmDeleteRisk>div.ng-dialog-container>div[data-role="controlgroup"]>div.ui-controlgroup-controls>a:first-child')
    REVIEW_ALERT = (MobileBy.CSS_SELECTOR, 'div#confirmReviewRisk>div.ng-dialog-container>div[data-role="controlgroup"]>div.ui-controlgroup-controls>a:first-child')
    RISK_LIBRARY = (MobileBy.CSS_SELECTOR, 'div#risklibraryTreeView>div.ui-content>ul.category>li:first-child>a')
    RISK_INSIDE_LIBRARY = (MobileBy.CSS_SELECTOR, 'div#risklibraryTreeView>div.ui-content>ul.item>li:first-child')


class AssetsScreen:
    """A class for handling Assets screen"""
    NAME = (MobileBy.CSS_SELECTOR, 'div#assetNew>div.ui-content>ul.edit-view>li:first-child>div.ui-input-text>input#name')
    SAVE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#assetNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                          'a[href="#save"]')
    CANCEL_BUTTON = (MobileBy.CSS_SELECTOR, 'div#assetNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                            'a[href="#cancel"]')
    NEW_BUTTON = (MobileBy.CSS_SELECTOR, 'li#openAssetTreeMore>a[href="#assetTreeMore"]')
    NEW_ASSET_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#assetNew?parent=0"]')
    ASSET_TYPE = (MobileBy.CSS_SELECTOR, 'div#assetNew>div.ui-content>ul>li:first-child>a')  # first asset type on the list
    PREVIOUSLY_CREATED_ASSET = (MobileBy.CSS_SELECTOR, 'div#assetTreeView>div.ui-content>div.main>ul[data-role="listview"]>li:first-child>a')
    PREVIOUSLY_CREATED_ASSET_CHECKBOX = (MobileBy.CSS_SELECTOR, 'div#assetTreeView>div.ui-content>div.main>ul[data-role="listview"]>li:first-child>div.ui-checkbox')  # whole list element - not just link
    EDIT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#assetView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.edit>a')
    COST_PER_UNIT_FIELD = (MobileBy.CSS_SELECTOR, 'div#assetEdit>div.ui-content>ul.edit-view>li>div>input[id="cost per unit"]')
    SAVE_EDITED_ASSET = (MobileBy.CSS_SELECTOR, 'div#assetEdit>div[data-role="footer"]>div[data-role="navbar"]>ul>li>a[href="#save"]')
    MORE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#assetView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.ui-block-b>a[href="#assetViewMoreMenu"]')
    DELETE_THIS_ASSET = (MobileBy.CSS_SELECTOR, 'div#assetView>div#assetViewMoreMenu-popup>div#assetViewMoreMenu>ul>li.delete>a[href="#confirmDeleteAsset"]')
    NEW_CHILD_ASSET = (MobileBy.CSS_SELECTOR, 'div#assetView>div#assetViewMoreMenu-popup>div#assetViewMoreMenu>ul>li.new>a')
    DELETE_ALERT = (MobileBy.CSS_SELECTOR, 'div#assetView>div#confirmDeleteAsset-popup>div#confirmDeleteAsset>div.ng-dialog-container>div>div.ui-controlgroup-controls>a:first-child')
    CANCEL_ALERT = (MobileBy.CSS_SELECTOR, 'div#assetView>div#confirmDeleteAsset-popup>div#confirmDeleteAsset>div.ng-dialog-container>div>div.ui-controlgroup-controls>a:last-child')
    PREVIOUSLY_CREATED_CHILD_ASSET = (MobileBy.CSS_SELECTOR, 'div#assetTreeView>div.ui-content>div.main>ul.assets>li:first-child>a')
    CHILD_ASSET_INSIDE_OTHER_ASSET = (MobileBy.CSS_SELECTOR, 'div#assetTreeView>div.ui-content>div.main>ul>li:first-child>a')
    SEARCH_FIELD = (MobileBy.CSS_SELECTOR, 'div#assetTreeView>div.ui-content>div.filters>div>input[id="assetSearch"]')
    CREATE_MAPPING_DATA = (MobileBy.CSS_SELECTOR, 'div#assetNew>div.ui-content>ul.edit-view>li.geometryinput>a')
    ADD_MEDIA_BUTTON = (MobileBy.CSS_SELECTOR, 'div#assetNew>div.ui-content>ul.edit-view>li.ui-li-static.ui-body-inherit>div.addmedia.edit-mode>a')


class SelectMediaScreen:
    """A class for handling Select Media Screen"""
    TAKE_PHOTO = (MobileBy.CSS_SELECTOR, 'div#filesystemMediaSelect>div.ui-content>div.ui-grid-a>div#filePhotoCapture>div.center-text>span.icon')
    RECORD_VIDEO = (MobileBy.CSS_SELECTOR, 'div#filesystemMediaSelect>div.ui-content>div.ui-grid-a>div#fileVideoCapture>div.center-text>span.icon')
    RECORD_AUDIO = (MobileBy.CSS_SELECTOR, 'div#filesystemMediaSelect>div.ui-content>div.ui-grid-a>div#fileAudioCapture>div.center-text>span.icon')
    VIDEO_GALLERY = (MobileBy.CSS_SELECTOR, 'div#filesystemMediaSelect>div.ui-content>div.ui-grid-a>div#fileVideoGallery>div.center-text>span.icon')
    PHOTO_GALLERY = (MobileBy.CSS_SELECTOR, 'div#filesystemMediaSelect>div.ui-content>div.ui-grid-a>div#filePhotoGallery>div.center-text>span.icon')
