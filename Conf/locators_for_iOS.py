from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class iOS:
    """A class for handling iOS device for example keyboard"""
    BUTTON_DONE_TO_HIDE_KEYBOARD = (By.CSS_SELECTOR, '')
    RETURN_BUTTON = (By.CSS_SELECTOR, '')
    IOS_OK = (By.CSS_SELECTOR, '')
    IOS_ALLOW = (By.CSS_SELECTOR, "")


class CommonScreen:
    """A class for handling Common buttons on different screen"""
    LOADING = (By.CSS_SELECTOR, '')
    SAVE_BUTTON = (By.CSS_SELECTOR, '')
    CANCEL_BUTTON = (By.CSS_SELECTOR, '')
    OK_BUTTON = (By.CSS_SELECTOR, '')
    PICKER_WHEEL = (By.CSS_SELECTOR, '')
    WEB_VIEW = (By.CSS_SELECTOR, '')


class TopBar:
    """A class for top bar locators."""
    HAMBURGER_FOR_MAIN_MENU = (By.CSS_SELECTOR, '')


class WelcomeScreen:
    """A class for welcome screen locators - first screen after lunching the app."""
    LOCATION_BUTTON = (By.CSS_SELECTOR, '')
    MY_MESSAGES_BUTTON = (By.CSS_SELECTOR, '')
    PHOTO_BUTTON = (By.CSS_SELECTOR, '')
    VIDEO_BUTTON = (By.CSS_SELECTOR, '')
    SOUND_BUTTON = (By.CSS_SELECTOR, '')
    SETTINGS_BUTTON = (By.CSS_SELECTOR, '')
    ABOUT_BUTTON = (By.CSS_SELECTOR, '')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'a.sessionMenu.ui-link')
    LOGIN_BUTTON_by_index = (By.CSS_SELECTOR, '')


class SettingsScreen:
    """A class for settings screen locators - screen after clicking settings button"""
    SETTINGS_CONTACT_IDENTIFIER_FIELD = (By.CSS_SELECTOR, '')
    SETTINGS_ALERT_APP_HAS_BEEN_ACTIVATED = (By.CSS_SELECTOR, '')
    SETTINGS_OK_BUTTON = (By.CSS_SELECTOR, '')


class LoginScreen:
    """A class for login screen locators - screen after clicking LOGIN button"""
    TEXTFIELD_USERNAME = (By.CSS_SELECTOR, '')
    TEXTFIELD_PASSWORD = (By.CSS_SELECTOR, '')
    TEXTFIELD_DOMAIN = (By.CSS_SELECTOR, 'input#sessionDomain')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '')

    # Notification alert: "OCA now supports sending 'App Messages' to your device as notifications."
    NOTIFICATION_ABOUT_SENDING_MESSAGES = (By.CSS_SELECTOR, '')

    # "No" button for sending notifications on iOS
    NO_FOR_SENDING_NOTIFICATIONS_ON = (By.CSS_SELECTOR, '')

    # ACCEPT_BUTTON on Terms and Conditions"
    ACCEPT_BUTTON = (By.CSS_SELECTOR, '')

    # alert message with word "Invalid"
    ALERT_MSG_INVALID = (By.CSS_SELECTOR, '')

    # alert message with "Your temporary account has been expired"
    ALERT_MSG_EXPIRED = (By.CSS_SELECTOR, '')

    # alert message with "The password for the current user is about to expire"
    ALERT_MSG_WILL_EXPIRE = (By.CSS_SELECTOR, '')

    # alert message with word "inactive"
    ALERT_MSG_SUSPENDED = (By.CSS_SELECTOR, '')
    # OK button on alert messages"
    OK_BUTTON = (By.CSS_SELECTOR, '')


class MainMenuScreen(WelcomeScreen):
    """A class for main menu screen locators - first screen after correct login into the app."""
    ACTIVATE_WORKFLOW_BUTTON = (By.CSS_SELECTOR, '')
    CREATE_CONTACT_BUTTON = (By.CSS_SELECTOR, '')
    CREATE_TASK_BUTTON = (By.CSS_SELECTOR, '')
    CREATE_REPORT_BUTTON = (By.CSS_SELECTOR, '')
    WEBSITE_LINK_BUTTON = (By.CSS_SELECTOR, '')
    INCIDENT_BUTTON = (By.CSS_SELECTOR, '')
    CREATE_ASSETS_BUTTON = (By.CSS_SELECTOR, '')
    CREATE_LOG_BUTTON = (By.CSS_SELECTOR, '')
    RISKS_BUTTON = (By.CSS_SELECTOR, '')
    EVENTS_BUTTON = (By.CSS_SELECTOR, '')
    LOGS_BUTTON = (By.CSS_SELECTOR, '')
    REPORTS_BUTTON = (By.CSS_SELECTOR, '')
    MAP_BUTTON = (By.CSS_SELECTOR, '')
    ASSETS_BUTTON = (By.CSS_SELECTOR, '')
    INBOX_BUTTON = (By.CSS_SELECTOR, '')
    COMPOSE_BUTTON = (By.CSS_SELECTOR, '')
    SENT_BUTTON = (By.CSS_SELECTOR, '')
    TASKS_BUTTON = (By.CSS_SELECTOR, '')
    DOCUMENTS_BUTTON = (By.CSS_SELECTOR, '')
    CONTACTS_BUTTON = (By.CSS_SELECTOR, '')
    ALLOCATE_BUTTON = (By.CSS_SELECTOR, '')
    ACTIVATE_BUTTON = (By.CSS_SELECTOR, '')
    OFFLINE_SYNC_BUTTON = (By.CSS_SELECTOR, '')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '')

    ALERT_ACTIVATE_BUTTON = (By.CSS_SELECTOR, '')
    ALERT_CANCEL_BUTTON = (By.CSS_SELECTOR, '')
    ALERT_WORKFLOW_ACTIVATED = (By.CSS_SELECTOR, '')


class LocationScreen:
    """A class for Location screen locators - screen after clicking into Location button in Main Menu."""
    SEND_ONCE_NOW = (By.CSS_SELECTOR, '')
    SEND_EVERY_SPINNER = (By.CSS_SELECTOR, '')
    CHOOSE_5_MINUTES_OPTION_iPad = (By.CSS_SELECTOR, '')
    ASSERT_5_MINUTES_OPTION = (By.CSS_SELECTOR, '')
    FOR_THE_NEXT_SPINNER = (By.CSS_SELECTOR, '')
    CHOOSE_1_HOUR_OPTION_iPad = (By.CSS_SELECTOR, '')
    ASSERT_1_HOUR_OPTION = (By.CSS_SELECTOR, '')
    START_BUTTON = (By.CSS_SELECTOR, '')
    STOP_BUTTON = (By.CSS_SELECTOR, '')
    TRACKING_HISTORY_BUTTON = (By.CSS_SELECTOR, '')
    LOCATION_PAGE_HEADER = (By.CSS_SELECTOR, '')
    LOCATION_STATUS = (By.CSS_SELECTOR, '')


class EventsScreen:
    """A class for Events screen locators - screen after clicking into Events button in Main Menu."""
    EVENTS_HEADER = (By.CSS_SELECTOR, '')

    # filtering events by Type
    ANY_TYPE_EXPAND = (By.CSS_SELECTOR, '')
    CHOOSE_TYPE_INCIDENT = (By.CSS_SELECTOR, '')
    INCIDENT_TYPE_EXPAND = (By.CSS_SELECTOR, '')
    CHOOSE_TYPE_ANY = (By.CSS_SELECTOR, '')

    # filtering events by Status
    ANY_STATUS_EXPAND = (By.CSS_SELECTOR, '')
    CHOOSE_ACTIVE_STATUS = (By.CSS_SELECTOR, '')
    ACTIVE_STATUS_EXPAND = (By.CSS_SELECTOR, '')
    CHOOSE_INACTIVE_STATUS = (By.CSS_SELECTOR, '')
    INACTIVE_STATUS_EXPAND = (By.CSS_SELECTOR, '')
    CHOOSE_DRAFT_STATUS = (By.CSS_SELECTOR, '')
    DRAFT_STATUS_EXPAND = (By.CSS_SELECTOR, '')
    CHOOSE_ANY_STATUS = (By.CSS_SELECTOR, '')

    # filtering events using search field
    SEARCH_FIELD = (By.CSS_SELECTOR, '')

    # creating and editing Events
    MORE_BUTTON = (By.CSS_SELECTOR, '')
    NEW_EVENT_BUTTON = (By.CSS_SELECTOR, '')

    # previously created event
    PREVIOUSLY_CREATED_EVENT = (By.CSS_SELECTOR, '')

    CLEAR_PRIMARY_EVENT_BUTTON = (By.CSS_SELECTOR, '')
    NOTIFICATION_PRIMARY_EVENT_CLEARED = (By.CSS_SELECTOR, '')


class TypesOfEventsScreen:
    """A class for Type of Events screen locators - first screen after creating new event with types of events."""
    INCIDENT_TYPE_OF_EVENT = (By.CSS_SELECTOR, '')
    EVENT_FOR_ON_LOAD_SAVE = (By.CSS_SELECTOR, '')
    EVENT_FOR_CHOOSER_FIELDS = (By.CSS_SELECTOR, '')


class EventEditScreen:
    """A class for Edit Events screen locators - screen after opening edit mode of event or creating a new one."""
    NAME_FIELD = (By.CSS_SELECTOR, '')
    NAME_FIELD_by_index = (By.CSS_SELECTOR, '')
    SEVERITY_LEVEL_SELECTOR = (By.CSS_SELECTOR, '')
    CHOOSE_SEVERITY_LVL1_iPad = (By.CSS_SELECTOR, '')
    CHOOSE_SEVERITY_LVL2_iPad = (By.CSS_SELECTOR, '')
    CHOOSE_SEVERITY_LVL3_iPad = (By.CSS_SELECTOR, '')
    CHOOSE_SEVERITY_LVL4_iPad = (By.CSS_SELECTOR, '')
    CHOOSE_SEVERITY_LVL5_iPad = (By.CSS_SELECTOR, '')
    SEVERITY_PICKER = (MobileBy.XPATH, '//XCUIElementTypeApplication/XCUIElementTypeWindow'
                                       '/XCUIElementTypePicker/XCUIElementTypePickerWheel')
    FINISHED_FIELD = (By.CSS_SELECTOR, '')
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, '')
    CREATE_MAPPING_DATA = (By.CSS_SELECTOR, '')
    EDIT_MAPPING_DATA = (By.CSS_SELECTOR, '')
    ELEMENT_TO_SCROLL = (By.CSS_SELECTOR, '')
    SEQUENCE_ONLOAD_HEADER = (By.CSS_SELECTOR, '')
    SEQUENCE_ONLOAD_VALUE = (By.CSS_SELECTOR, '')
    SEQUENCE_ONSAVE_HEADER = (By.CSS_SELECTOR, '')
    SEQUENCE_ONSAVE_VALUE = (By.CSS_SELECTOR, '')
    NEW_OPTION_LIST_HEADER = (By.CSS_SELECTOR, '')
    OPTION_LIST_VALUE_1 = (By.CSS_SELECTOR, '')
    OPTION_LIST_VALUE_2 = (By.CSS_SELECTOR, '')
    OPTION_LIST_VALUE_3 = (By.CSS_SELECTOR, '')
    FIELD_TO_RESTORE_1_HEADER = (By.CSS_SELECTOR, '')
    FIELD_TO_RESTORE_1_VALUE = (By.CSS_SELECTOR, '')
    FIELD_TO_RESTORE_2_HEADER = (By.CSS_SELECTOR, '')
    FIELD_TO_RESTORE_2_VALUE = (By.CSS_SELECTOR, '')
    CHOOSER_FIELD = (By.CSS_SELECTOR, '')
    SUBFORM_FIELD_ADD_ROW = (By.CSS_SELECTOR, '')
    NEW_EVENTS_CHOOSER_IN_SUB_FORM = (By.CSS_SELECTOR, '')
    DELETE_SUB_EVENT_FROM_CHOOSER = (By.CSS_SELECTOR, '')


class EventDetailsScreen:
    """A class for Event Details screen locators - screen with event details - after opening event."""
    EDIT_BUTTON = (By.CSS_SELECTOR, '')
    DELETE_EVENT_BUTTON = (By.CSS_SELECTOR, '')
    DELETE_CONFIRM_BUTTON = (By.CSS_SELECTOR, '')
    NEW_SUB_EVENT = (By.CSS_SELECTOR, '')
    SET_AS_PRIMARY_BUTTON = (By.CSS_SELECTOR, '')


class Map:
    """A class for Map screen locators."""
    PLOT_BUTTON = (By.CSS_SELECTOR, '')
    TOOL_BUTTON = (By.CSS_SELECTOR, '')
    POINT_BUTTON = (By.CSS_SELECTOR, '')
    DEFAULT_BUTTON = (By.CSS_SELECTOR, '')
    MAP_AREA_12 = (By.CSS_SELECTOR, '')
    MAP_AREA_13 = (By.CSS_SELECTOR, '')
    MAP_AREA_17 = (By.CSS_SELECTOR, '')
    MAP_AREA_18 = (By.CSS_SELECTOR, '')
    LINE_BUTTON = (By.CSS_SELECTOR, '')
    CIRCLE_BUTTON = (By.CSS_SELECTOR, '')
    POLYGON_BUTTON = (By.CSS_SELECTOR, '')
    SAVE_MAP_BUTTON = (By.CSS_SELECTOR, '')


class PhotoScreen:
    """A class for Photo screen locators - screen after clicking into Photo button in Main Menu."""
    PHOTO_PAGE_HEADER = (By.CSS_SELECTOR, '')
    GALLERY_BUTTON = (By.CSS_SELECTOR, '')
    TAKE_NEW_BUTTON = (By.CSS_SELECTOR, '')
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, '')
    SEND_BUTTON = (By.CSS_SELECTOR, '')
    RESET_BUTTON = (By.CSS_SELECTOR, '')


class VideoScreen:
    """A class for Video screen locators - screen after clicking into Video button in Main Menu."""
    VIDEO_PAGE_HEADER = (By.CSS_SELECTOR, '')
    RECORD_NEW_BUTTON = (By.CSS_SELECTOR, '')


class SoundScreen:
    """A class for Sound screen locators - screen after clicking into Sound button in Main Menu."""
    SOUND_PAGE_HEADER = (By.CSS_SELECTOR, '')
    RECORD_SOUND_BUTTON = (By.CSS_SELECTOR, '')


class SoundRecorderScreen:
    """A class for Sound Recorder screen locators - screen after clicking into record sound button in Sound Page."""
    RECORD_SOUND = (By.CSS_SELECTOR, 'toggle audio recording')
    DONE_BUTTON = (By.CSS_SELECTOR, 'Done')


class GalleryScreen:
    """A class for handling Gallery"""
    GALLERY_ELEMENT_1 = (By.CSS_SELECTOR, '//XCUIElementTypeCell[@name[contains(., "Photo")]][1]')
    GALLERY_VIDEOS_POPOVER = (By.CSS_SELECTOR, '//XCUIElementTypeButton[@name="Videos"]')
    GALLERY_VIDEO_ELEMENT_1 = (By.CSS_SELECTOR, '//XCUIElementTypeCell[1]')
    USE_BUTTON = (By.CSS_SELECTOR, 'Choose')


class CameraScreen:
    """A class for handling Camera"""
    PHOTO_CAPTURE = (By.CSS_SELECTOR, 'PhotoCapture')
    CANCEL_BUTTON = (By.CSS_SELECTOR, 'Cancel')
    CAMERA_CHOOSER = (By.CSS_SELECTOR, 'FrontBackFacingCameraChooser')
    RETAKE = (By.CSS_SELECTOR, 'Retake')
    USE_PHOTO = (By.CSS_SELECTOR, 'Use Photo')
    VIDEO_CAPTURE = (By.CSS_SELECTOR, 'VideoCapture')  # record and stop recording
    USE_VIDEO = (By.CSS_SELECTOR, 'Use Video')


class RisksScreen:
    """A class for handling Risks screen"""

    NEW_BUTTON = (By.CSS_SELECTOR, '')
    VIEW_BUTTON = (By.CSS_SELECTOR, '')


class NewContactScreen:
    """A class for handling New Contact screen"""
    FIRST_NAME = (By.CSS_SELECTOR, '')


class NewTaskScreen:
    """A class for handling New Task screen"""
    TITLE = (By.CSS_SELECTOR, '')
    ASSIGNED = (By.CSS_SELECTOR, '')
    ADD_CONTACTS_AND_GROUPS = (By.CSS_SELECTOR, '')
    ADD_RESOURCE_STRUCTURE_NODES = (By.CSS_SELECTOR, '')
    ADD_RESOURCE_ASSIGNMENTS = (By.CSS_SELECTOR, '')
    CHOOSE_USERS = (By.CSS_SELECTOR, '')
    CHOOSE_CONTACTS = (By.CSS_SELECTOR, '')
    START_DATE = (By.CSS_SELECTOR, '')
    HIDE_DATE_PICKER = (By.CSS_SELECTOR, '')


class NewReportScreen:
    """A class for handling New Report screen"""
    LODGING_AGENCY_PICKER = (By.CSS_SELECTOR, '')
    LODGING_AGENCY = (By.CSS_SELECTOR, '')
    PUBLISH_BUTTON = (By.CSS_SELECTOR, '')


class NewAssetScreen:
    """A class for handling New Asset screen"""
    pass


class NewLogScreen:
    """A class for handling New Log screen"""
    LODGING_AGENCY_PICKER = (By.CSS_SELECTOR, '')
    ENTRY_FIELD = (By.CSS_SELECTOR, '')


class SentScreen:
    """A class for handling Sent screen"""
    SEARCH = EventsScreen.SEARCH_FIELD
    SENT_COMMUNICATIONS_EMAIL = (By.CSS_SELECTOR, '')


class ComposeScreen:
    """A class for handling Compose screen"""
    ADD_RECIPIENTS_BUTTON = (By.CSS_SELECTOR, '')
    MESSAGE_EMAIL = (By.CSS_SELECTOR, '')
    EMAIL_SUBJECT_FIELD = (By.CSS_SELECTOR, '')
    EMAIL_TEXT_FIELD = (By.CSS_SELECTOR, '')
    MESSAGE_SMS = (By.CSS_SELECTOR, '')
    SMS_TEXT_FIELD = (By.CSS_SELECTOR, '')
    MESSAGE_VOICE = (By.CSS_SELECTOR, '')
    VOICE_TEXT_FIELD = (By.CSS_SELECTOR, '')
    TEXT_TO_SPEECH_BUTTON = (By.CSS_SELECTOR, '')
    MESSAGE_FAX = (By.CSS_SELECTOR, '')
    FAX_DOCUMENT_BUTTON = (By.CSS_SELECTOR, '')
    COMMS_DOCUMENTS_BUTTON = (By.CSS_SELECTOR, '')
    FILES_LIST = (By.CSS_SELECTOR, '')
    FAX_PDF_FILE = (By.CSS_SELECTOR, '')
    FAX_OK_BUTTON = (By.CSS_SELECTOR, '')
    REQUIRE_ACKNOWLEDGMENT = (By.CSS_SELECTOR, '')
    REPLY_TRACKING = (By.CSS_SELECTOR, '')
    READ_ACCESS_LEVEL = (By.CSS_SELECTOR, '')
    ADD_CONTACTS_AND_GROUPS = (By.CSS_SELECTOR, '')
    ADD_RESOURCES_STRUCTURE_NODES = (By.CSS_SELECTOR, '')
    CONTACTS_ARROW = (By.CSS_SELECTOR, '')
    USERS_ARROW = (By.CSS_SELECTOR, '')
    MAILING_LIST_UNSUBSCRIBES_ARROW = (By.CSS_SELECTOR, '')
    CONTACT_FOR_APPIUM_TESTS = (By.CSS_SELECTOR, 'input[data-label="CONTACT_FOR_APPIUM_TESTS"]')
    ALERT_SEND_BUTTON = (By.CSS_SELECTOR, '')


