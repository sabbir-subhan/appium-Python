from appium.webdriver.common.mobileby import MobileBy


class CommonScreen:
    """A class for handling Common buttons on different screen"""
    LOADING = (MobileBy.CSS_SELECTOR, '')
    SAVE_BUTTON = (MobileBy.CSS_SELECTOR, '')
    CANCEL_BUTTON = (MobileBy.CSS_SELECTOR, '')
    OK_BUTTON = (MobileBy.CSS_SELECTOR, '')
    PICKER_WHEEL = (MobileBy.CSS_SELECTOR, '')


class TopBar:
    """A class for top bar locators."""
    HAMBURGER_FOR_MAIN_MENU = (MobileBy.CSS_SELECTOR, 'div#iconbar>a')


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
    SETTINGS_CONTACT_IDENTIFIER_FIELD = (MobileBy.CSS_SELECTOR, '')
    SETTINGS_ALERT_APP_HAS_BEEN_ACTIVATED = (MobileBy.CSS_SELECTOR, '')
    SETTINGS_OK_BUTTON = (MobileBy.CSS_SELECTOR, '')


class LoginScreen:
    """A class for login screen locators - screen after clicking LOGIN button"""
    TEXTFIELD_USERNAME = (MobileBy.CSS_SELECTOR, '')
    TEXTFIELD_PASSWORD = (MobileBy.CSS_SELECTOR, '')
    TEXTFIELD_DOMAIN = (MobileBy.CSS_SELECTOR, 'input#sessionDomain')
    SUBMIT_BUTTON = (MobileBy.CSS_SELECTOR, 'a#sessionSubmit')  # ??

    # Notification alert: "OCA now supports sending 'App Messages' to your device as notifications."
    NOTIFICATION_ABOUT_SENDING_MESSAGES = (MobileBy.CSS_SELECTOR, '')

    # "No" button for sending notifications on iOS
    NO_FOR_SENDING_NOTIFICATIONS_ON = (MobileBy.CSS_SELECTOR, '')

    # ACCEPT_BUTTON on Terms and Conditions"
    ACCEPT_BUTTON = (MobileBy.CSS_SELECTOR, '')

    # alert message with word "Invalid"
    ALERT_MSG_INVALID = (MobileBy.CSS_SELECTOR, '')

    # alert message with "Your temporary account has been expired"
    ALERT_MSG_EXPIRED = (MobileBy.CSS_SELECTOR, '')

    # alert message with "The password for the current user is about to expire"
    ALERT_MSG_WILL_EXPIRE = (MobileBy.CSS_SELECTOR, '')

    # alert message with word "inactive"
    ALERT_MSG_SUSPENDED = (MobileBy.CSS_SELECTOR, '')
    # OK button on alert messages"
    OK_BUTTON = (MobileBy.CSS_SELECTOR, '')


class MainMenuScreen(WelcomeScreen):
    """A class for main menu screen locators - first screen after correct login into the app."""
    ACTIVATE_WORKFLOW_BUTTON = (MobileBy.CSS_SELECTOR, '')
    CREATE_CONTACT_BUTTON = (MobileBy.CSS_SELECTOR, '')
    CREATE_TASK_BUTTON = (MobileBy.CSS_SELECTOR, '')
    CREATE_REPORT_BUTTON = (MobileBy.CSS_SELECTOR, '')
    WEBSITE_LINK_BUTTON = (MobileBy.CSS_SELECTOR, '')
    INCIDENT_BUTTON = (MobileBy.CSS_SELECTOR, '')
    CREATE_ASSETS_BUTTON = (MobileBy.CSS_SELECTOR, '')
    CREATE_LOG_BUTTON = (MobileBy.CSS_SELECTOR, '')
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

    ALERT_ACTIVATE_BUTTON = (MobileBy.CSS_SELECTOR, '')
    ALERT_CANCEL_BUTTON = (MobileBy.CSS_SELECTOR, '')
    ALERT_WORKFLOW_ACTIVATED = (MobileBy.CSS_SELECTOR, '')


class LocationScreen:
    """A class for Location screen locators - screen after clicking into Location button in Main Menu."""
    SEND_ONCE_NOW = (MobileBy.CSS_SELECTOR, '')
    SEND_EVERY_SPINNER = (MobileBy.CSS_SELECTOR, '')
    CHOOSE_5_MINUTES_OPTION_iPad = (MobileBy.CSS_SELECTOR, '')
    ASSERT_5_MINUTES_OPTION = (MobileBy.CSS_SELECTOR, '')
    FOR_THE_NEXT_SPINNER = (MobileBy.CSS_SELECTOR, '')
    CHOOSE_1_HOUR_OPTION_iPad = (MobileBy.CSS_SELECTOR, '')
    ASSERT_1_HOUR_OPTION = (MobileBy.CSS_SELECTOR, '')
    START_BUTTON = (MobileBy.CSS_SELECTOR, '')
    STOP_BUTTON = (MobileBy.CSS_SELECTOR, '')
    TRACKING_HISTORY_BUTTON = (MobileBy.CSS_SELECTOR, '')
    LOCATION_PAGE_HEADER = (MobileBy.CSS_SELECTOR, '')
    LOCATION_STATUS = (MobileBy.CSS_SELECTOR, '')


class EventsScreen:
    """A class for Events screen locators - screen after clicking into Events button in Main Menu."""
    EVENTS_HEADER = (MobileBy.CSS_SELECTOR, '')

    # filtering events by Type
    ANY_TYPE_EXPAND = (MobileBy.CSS_SELECTOR, '')
    CHOOSE_TYPE_INCIDENT = (MobileBy.CSS_SELECTOR, '')
    INCIDENT_TYPE_EXPAND = (MobileBy.CSS_SELECTOR, '')
    CHOOSE_TYPE_ANY = (MobileBy.CSS_SELECTOR, '')

    # filtering events by Status
    ANY_STATUS_EXPAND = (MobileBy.CSS_SELECTOR, '')
    CHOOSE_ACTIVE_STATUS = (MobileBy.CSS_SELECTOR, '')
    ACTIVE_STATUS_EXPAND = (MobileBy.CSS_SELECTOR, '')
    CHOOSE_INACTIVE_STATUS = (MobileBy.CSS_SELECTOR, '')
    INACTIVE_STATUS_EXPAND = (MobileBy.CSS_SELECTOR, '')
    CHOOSE_DRAFT_STATUS = (MobileBy.CSS_SELECTOR, '')
    DRAFT_STATUS_EXPAND = (MobileBy.CSS_SELECTOR, '')
    CHOOSE_ANY_STATUS = (MobileBy.CSS_SELECTOR, '')

    # filtering events using search field
    SEARCH_FIELD = (MobileBy.CSS_SELECTOR, '')

    # creating and editing Events
    MORE_BUTTON = (MobileBy.CSS_SELECTOR, '')
    NEW_EVENT_BUTTON = (MobileBy.CSS_SELECTOR, '')

    # previously created event
    PREVIOUSLY_CREATED_EVENT = (MobileBy.CSS_SELECTOR, '')

    CLEAR_PRIMARY_EVENT_BUTTON = (MobileBy.CSS_SELECTOR, '')
    NOTIFICATION_PRIMARY_EVENT_CLEARED = (MobileBy.CSS_SELECTOR, '')


class TypesOfEventsScreen:
    """A class for Type of Events screen locators - first screen after creating new event with types of events."""
    INCIDENT_TYPE_OF_EVENT = (MobileBy.CSS_SELECTOR, '')
    EVENT_FOR_ON_LOAD_SAVE = (MobileBy.CSS_SELECTOR, '')
    EVENT_FOR_CHOOSER_FIELDS = (MobileBy.CSS_SELECTOR, '')


class EventEditScreen:
    """A class for Edit Events screen locators - screen after opening edit mode of event or creating a new one."""
    NAME_FIELD = (MobileBy.CSS_SELECTOR, '')
    NAME_FIELD_by_index = (MobileBy.CSS_SELECTOR, '')
    SEVERITY_LEVEL_SELECTOR = (MobileBy.CSS_SELECTOR, '')
    CHOOSE_SEVERITY_LVL1_iPad = (MobileBy.CSS_SELECTOR, '')
    CHOOSE_SEVERITY_LVL2_iPad = (MobileBy.CSS_SELECTOR, '')
    CHOOSE_SEVERITY_LVL3_iPad = (MobileBy.CSS_SELECTOR, '')
    CHOOSE_SEVERITY_LVL4_iPad = (MobileBy.CSS_SELECTOR, '')
    CHOOSE_SEVERITY_LVL5_iPad = (MobileBy.CSS_SELECTOR, '')
    SEVERITY_PICKER = (MobileBy.XPATH, '//XCUIElementTypeApplication/XCUIElementTypeWindow'
                                       '/XCUIElementTypePicker/XCUIElementTypePickerWheel')
    FINISHED_FIELD = (MobileBy.CSS_SELECTOR, '')
    DESCRIPTION_FIELD = (MobileBy.CSS_SELECTOR, '')
    CREATE_MAPPING_DATA = (MobileBy.CSS_SELECTOR, '')
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
    SUBFORM_FIELD_ADD_ROW = (MobileBy.CSS_SELECTOR, '')
    NEW_EVENTS_CHOOSER_IN_SUB_FORM = (MobileBy.CSS_SELECTOR, '')
    DELETE_SUB_EVENT_FROM_CHOOSER = (MobileBy.CSS_SELECTOR, '')


class EventDetailsScreen:
    """A class for Event Details screen locators - screen with event details - after opening event."""
    EDIT_BUTTON = (MobileBy.CSS_SELECTOR, '')
    DELETE_EVENT_BUTTON = (MobileBy.CSS_SELECTOR, '')
    DELETE_CONFIRM_BUTTON = (MobileBy.CSS_SELECTOR, '')
    NEW_SUB_EVENT = (MobileBy.CSS_SELECTOR, '')
    SET_AS_PRIMARY_BUTTON = (MobileBy.CSS_SELECTOR, '')


class Map:
    """A class for Map screen locators."""
    PLOT_BUTTON = (MobileBy.CSS_SELECTOR, '')
    TOOL_BUTTON = (MobileBy.CSS_SELECTOR, '')
    POINT_BUTTON = (MobileBy.CSS_SELECTOR, '')
    DEFAULT_BUTTON = (MobileBy.CSS_SELECTOR, '')
    MAP_AREA_12 = (MobileBy.CSS_SELECTOR, '')
    MAP_AREA_13 = (MobileBy.CSS_SELECTOR, '')
    MAP_AREA_17 = (MobileBy.CSS_SELECTOR, '')
    MAP_AREA_18 = (MobileBy.CSS_SELECTOR, '')
    LINE_BUTTON = (MobileBy.CSS_SELECTOR, '')
    CIRCLE_BUTTON = (MobileBy.CSS_SELECTOR, '')
    POLYGON_BUTTON = (MobileBy.CSS_SELECTOR, '')
    SAVE_MAP_BUTTON = (MobileBy.CSS_SELECTOR, '')


class PhotoScreen:
    """A class for Photo screen locators - screen after clicking into Photo button in Main Menu."""
    PHOTO_PAGE_HEADER = (MobileBy.CSS_SELECTOR, '')
    GALLERY_BUTTON = (MobileBy.CSS_SELECTOR, '')
    TAKE_NEW_BUTTON = (MobileBy.CSS_SELECTOR, '')
    DESCRIPTION_FIELD = (MobileBy.CSS_SELECTOR, '')
    SEND_BUTTON = (MobileBy.CSS_SELECTOR, '')
    RESET_BUTTON = (MobileBy.CSS_SELECTOR, '')


class VideoScreen:
    """A class for Video screen locators - screen after clicking into Video button in Main Menu."""
    VIDEO_PAGE_HEADER = (MobileBy.CSS_SELECTOR, '')
    RECORD_NEW_BUTTON = (MobileBy.CSS_SELECTOR, '')


class SoundScreen:
    """A class for Sound screen locators - screen after clicking into Sound button in Main Menu."""
    SOUND_PAGE_HEADER = (MobileBy.CSS_SELECTOR, '')
    RECORD_SOUND_BUTTON = (MobileBy.CSS_SELECTOR, '')


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


class RisksScreen:
    """A class for handling Risks screen"""

    NEW_BUTTON = (MobileBy.CSS_SELECTOR, '')
    VIEW_BUTTON = (MobileBy.CSS_SELECTOR, '')


class NewContactScreen:
    """A class for handling New Contact screen"""
    FIRST_NAME = (MobileBy.CSS_SELECTOR, '')


class NewTaskScreen:
    """A class for handling New Task screen"""
    TITLE = (MobileBy.CSS_SELECTOR, '')
    ASSIGNED = (MobileBy.CSS_SELECTOR, '')
    ADD_CONTACTS_AND_GROUPS = (MobileBy.CSS_SELECTOR, '')
    ADD_RESOURCE_STRUCTURE_NODES = (MobileBy.CSS_SELECTOR, '')
    ADD_RESOURCE_ASSIGNMENTS = (MobileBy.CSS_SELECTOR, '')
    CHOOSE_USERS = (MobileBy.CSS_SELECTOR, '')
    CHOOSE_CONTACTS = (MobileBy.CSS_SELECTOR, '')
    START_DATE = (MobileBy.CSS_SELECTOR, '')
    HIDE_DATE_PICKER = (MobileBy.CSS_SELECTOR, '')


class NewReportScreen:
    """A class for handling New Report screen"""
    LODGING_AGENCY_PICKER = (MobileBy.CSS_SELECTOR, '')
    LODGING_AGENCY = (MobileBy.CSS_SELECTOR, '')
    PUBLISH_BUTTON = (MobileBy.CSS_SELECTOR, '')


class NewAssetScreen:
    """A class for handling New Asset screen"""
    pass


class NewLogScreen:
    """A class for handling New Log screen"""
    LODGING_AGENCY_PICKER = (MobileBy.CSS_SELECTOR, '')
    ENTRY_FIELD = (MobileBy.CSS_SELECTOR, '')


class SentScreen:
    """A class for handling Sent screen"""
    SEARCH = EventsScreen.SEARCH_FIELD
    SENT_COMMUNICATIONS_EMAIL = (MobileBy.CSS_SELECTOR, '')


class ComposeScreen:
    """A class for handling Compose screen"""
    ADD_RECIPIENTS_BUTTON = (MobileBy.CSS_SELECTOR, 'div#messagePage>div.ui-content>ul.recipients.ui-listview')
    MESSAGE_EMAIL = (MobileBy.CSS_SELECTOR, '')
    EMAIL_SUBJECT_FIELD = (MobileBy.CSS_SELECTOR, '')
    EMAIL_TEXT_FIELD = (MobileBy.CSS_SELECTOR, '')
    MESSAGE_SMS = (MobileBy.CSS_SELECTOR, '')
    SMS_TEXT_FIELD = (MobileBy.CSS_SELECTOR, '')
    MESSAGE_VOICE = (MobileBy.CSS_SELECTOR, '')
    VOICE_TEXT_FIELD = (MobileBy.CSS_SELECTOR, '')
    TEXT_TO_SPEECH_BUTTON = (MobileBy.CSS_SELECTOR, '')
    MESSAGE_FAX = (MobileBy.CSS_SELECTOR, '')
    FAX_DOCUMENT_BUTTON = (MobileBy.CSS_SELECTOR, '')
    COMMS_DOCUMENTS_BUTTON = (MobileBy.CSS_SELECTOR, '')
    FILES_LIST = (MobileBy.CSS_SELECTOR, '')
    FAX_PDF_FILE = (MobileBy.CSS_SELECTOR, '')
    FAX_OK_BUTTON = (MobileBy.CSS_SELECTOR, '')
    REQUIRE_ACKNOWLEDGMENT = (MobileBy.CSS_SELECTOR, '')
    REPLY_TRACKING = (MobileBy.CSS_SELECTOR, '')
    READ_ACCESS_LEVEL = (MobileBy.CSS_SELECTOR, '')
    ADD_CONTACTS_AND_GROUPS = (MobileBy.CSS_SELECTOR, 'a.maywrap.ui-link.ui-btn.ui-shadow.ui-corner-all')  # list of two elements - select [0]
    ADD_RESOURCES_STRUCTURE_NODES = (MobileBy.CSS_SELECTOR, 'a.maywrap.ui-link.ui-btn.ui-shadow.ui-corner-all')  # list of two elements - select [1]
    CONTACTS_ARROW = (MobileBy.CSS_SELECTOR, 'a[href="#contactgroupTreeView?selector=true&id=4"]')  # test it
    USERS_ARROW = (MobileBy.CSS_SELECTOR, 'a[href="#contactgroupTreeView?selector=true&id=3"]')  # test it
    MAILING_LIST_UNSUBSCRIBES_ARROW = (MobileBy.CSS_SELECTOR, '')
    CONTACT_FOR_APPIUM_TESTS = (MobileBy.CSS_SELECTOR, 'input[data-label="CONTACT_FOR_APPIUM_TESTS"]')
    ALERT_SEND_BUTTON = (MobileBy.CSS_SELECTOR, 'a#messageSend')


