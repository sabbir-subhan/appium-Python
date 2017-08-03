""" locators for iOS 10 """

from appium.webdriver.common.mobileby import MobileBy


class iOS:
    """A class for handling iOS device for example keyboard"""
    BUTTON_DONE_TO_HIDE_KEYBOARD = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Done"]')
    RETURN_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Return"]')
    IOS_OK = (MobileBy.ACCESSIBILITY_ID, 'OK')
    IOS_ALLOW = (MobileBy.ACCESSIBILITY_ID, "Allow")
    AIRPLANE_MODE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Airplane Mode')
    # AIRPLANE_MODE_BUTTON = (MobileBy.XPATH, '//UIAElement[@name="Airplane Mode"][@value="0"]')
    WIFI_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Wi-FI')


class CommonScreen:
    """A class for handling Common buttons on different screen"""
    LOADING = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="loading"]')
    UPLOADING = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name[contains(., "Uploading")]]')
    SAVE_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Save"]')
    WRITE_ACCESS_LEVEL = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Write Access Level"]')
    CANCEL_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Cancel"]')
    OK_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Ok"]')
    PICKER_WHEEL = (MobileBy.CLASS_NAME, 'XCUIElementTypePickerWheel')
    WEB_VIEW = (MobileBy.CLASS_NAME, 'XCUIElementTypeScrollView')
    WHOLE_APP_SCREEN = (MobileBy.NAME, 'OCA')


class TopBar:
    """A class for top bar locators."""
    # HAMBURGER_FOR_MAIN_MENU = (MobileBy.CSS_SELECTOR, 'div#iconbar')
    # HAMBURGER_FOR_MAIN_MENU = (MobileBy.XPATH, '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeLink[1]/XCUIElementTypeStaticText[1]')


class WelcomeScreen:
    """A class for welcome screen locators - first screen after lunching the app."""
    LOCATION_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "LOCATION")]]')
    MY_MESSAGES_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "MY MESSAGES")]]')
    PHOTO_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "PHOTO")]]')
    VIDEO_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "VIDEO")]]')
    SOUND_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "SOUND")]]')
    SETTINGS_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "SETTINGS")]]')
    ABOUT_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "ABOUT")]]')
    LOGIN_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "LOGIN")]]')
    # LOGIN_BUTTON_by_index = (MobileBy.XPATH, '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]'
    #                                          '/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]'
    #                                          '/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]'
    #                                          '/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]'
    #                                          '/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]'
    #                                          '/XCUIElementTypeOther[7]/XCUIElementTypeLink[1]')


class SettingsScreen:
    """A class for settings screen locators - screen after clicking settings button"""
    SETTINGS_CONTACT_IDENTIFIER_FIELD = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextField')
    SETTINGS_ALERT_APP_HAS_BEEN_ACTIVATED = (MobileBy.XPATH, '//XCUIElementTypeStaticText['
                                                             '@name="App has been activated."]')
    SETTINGS_OK_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name="Ok"]')


class LoginScreen:
    """A class for login screen locators - screen after clicking LOGIN button"""
    TEXTFIELD_USERNAME = (MobileBy.XPATH, '//XCUIElementTypeTextField[1]')
    TEXTFIELD_PASSWORD = (MobileBy.XPATH, '//XCUIElementTypeSecureTextField[1]')
    TEXTFIELD_DOMAIN = (MobileBy.XPATH, '//XCUIElementTypeTextField[1]')
    SUBMIT_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Submit"]')

    # Notification alert: "OCA now supports sending 'App Messages' to your device as notifications."
    NOTIFICATION_ABOUT_SENDING_MESSAGES = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name[contains(., '
                                                           '"OCA now supports ")]]')

    # "No" button for sending notifications on iOS
    NO_FOR_SENDING_NOTIFICATIONS_ON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name="No"]')

    # ACCEPT_BUTTON on Terms and Conditions"
    ACCEPT_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Accept"]')

    # alert message with word "Invalid"
    ALERT_MSG_INVALID = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Invalid username and/or password"]')

    # alert message with "Your temporary account has been expired"
    ALERT_MSG_EXPIRED = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name[contains'
                                         '(., "Your temporary account has been expired")]]')

    # alert message with "The password for the current user is about to expire"
    ALERT_MSG_WILL_EXPIRE = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name[contains('
                                             '., "The password for the current user is about to expire")]]')

    # alert message with word "inactive"
    ALERT_MSG_SUSPENDED = (MobileBy.XPATH, '//XCUIElementTypeStaticText['
                                           '@name[contains(., "Your account is currently inactive")]]')
    # OK button on alert messages"
    OK_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name="Ok"]')


class MainMenuScreen(WelcomeScreen):
    """A class for main menu screen locators - first screen after correct login into the app."""
    ACTIVATE_WORKFLOW_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "ACTIVATE WORKFLOW")]]')
    CREATE_CONTACT_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "CREATE CONTACT")]]')
    CREATE_TASK_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "CREATE A TASK")]]')
    CREATE_REPORT_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "CREATE A REPORT")]]')
    WEBSITE_LINK_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "WEBSITE LINK")]]')
    INCIDENT_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "INCIDENT")]]')
    CREATE_ASSETS_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "CREATE ASSETS")]]')
    CREATE_LOG_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "CREATE A LOG")]]')
    RISKS_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "RISKS")]]')
    EVENTS_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "EVENTS")]]')
    LOGS_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "LOGS")]]')
    REPORTS_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "REPORTS")]]')
    MAP_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "MAP")]]')
    ASSETS_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "ASSETS")]]')
    INBOX_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "INBOX")]]')
    COMPOSE_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "COMPOSE")]]')
    SENT_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "SENT")]]')
    TASKS_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "TASKS")]]')
    DOCUMENTS_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "DOCUMENTS")]]')
    CONTACTS_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "CONTACTS")]]')
    ALLOCATE_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "ALLOCATE")]]')
    ACTIVATE_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "ACTIVATE")]]')
    OFFLINE_SYNC_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "OFFLINE SYNC")]]')
    LOGOUT_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "LOGOUT")]]')

    ALERT_ACTIVATE_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink/XCUIElementTypeStaticText[@name="Activate"]')
    ALERT_CANCEL_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink/XCUIElementTypeStaticText[@name="Cancel"]')
    ALERT_WORKFLOW_ACTIVATED = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Workflow activated"]')


class LocationScreen:
    """A class for Location screen locators - screen after clicking into Location button in Main Menu."""
    SEND_ONCE_NOW = (MobileBy.XPATH, '//XCUIElementTypeButton[@name[contains(., "Send once now")]]')
    SEND_EVERY_SPINNER = (MobileBy.XPATH, '//XCUIElementTypeOther[@name="Send every"]')
    CHOOSE_5_MINUTES_OPTION_iPad = (MobileBy.XPATH, '//XCUIElementTypePopover/XCUIElementTypeTableView'
                                                    '/XCUIElementTypeTableCell[2]')
    ASSERT_5_MINUTES_OPTION = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="5 minutes"]')
    FOR_THE_NEXT_SPINNER = (MobileBy.XPATH, '//XCUIElementTypeOther[@name="For the next"]')
    CHOOSE_1_HOUR_OPTION_iPad = (MobileBy.XPATH, '//XCUIElementTypePopover/XCUIElementTypeTableView'
                                                 '/XCUIElementTypeTableCell[3]')
    ASSERT_1_HOUR_OPTION = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="1 hour"]')
    START_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name[contains(., "Start")]]')
    STOP_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name[contains(., "Stop")]]')
    TRACKING_HISTORY_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Tracking history"]')
    LOCATION_PAGE_HEADER = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name[contains('
                                            '., "Your location was last sent")]]')
    LOCATION_STATUS = (MobileBy.XPATH, "//XCUIElementTypeStaticText[@name[contains(., ' seconds ago')]]")


class EventsScreen:
    """A class for Events screen locators - screen after clicking into Events button in Main Menu."""
    EVENTS_HEADER = (MobileBy.XPATH, '//XCUIElementTypeOther[@name="Events"]')

    # filtering events by Type
    ANY_TYPE_EXPAND = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Any Type click to expand")]]')
    CHOOSE_TYPE_INCIDENT = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Incident"]')
    INCIDENT_TYPE_EXPAND = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Incident click to expand")]]')
    CHOOSE_TYPE_ANY = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Any Type"]')

    # filtering events by Status
    ANY_STATUS_EXPAND = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Any Status click to expand")]]')
    CHOOSE_ACTIVE_STATUS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name="Active"]')
    ACTIVE_STATUS_EXPAND = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Active click to expand")]]')
    CHOOSE_INACTIVE_STATUS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name="Inactive"]')
    INACTIVE_STATUS_EXPAND = (MobileBy.XPATH, '//XCUIElementTypeLink[@name['
                                              'contains(., "Inactive click to expand")]]')
    CHOOSE_DRAFT_STATUS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name="Draft"]')
    DRAFT_STATUS_EXPAND = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Draft click to expand")]]')
    CHOOSE_ANY_STATUS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name="Any Status"]')

    # filtering events using search field
    SEARCH_FIELD = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextField')

    # creating and editing Events
    MORE_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name[contains(., "More")]]')
    NEW_EVENT_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "New event")]]')

    # previously created event
    PREVIOUSLY_CREATED_EVENT = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Appium")]]')
    # CREATED_EVENT_2 = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains('
    #                                    '., "Test Appium - second event")]]')
    # CREATED_EVENT_3 = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "to create sub")]]')
    CLEAR_PRIMARY_EVENT_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name'
                                                  '[contains(., "Clear primary event")]]')
    NOTIFICATION_PRIMARY_EVENT_CLEARED = (MobileBy.XPATH, '//XCUIElementTypeStaticText['
                                                          '@name="Primary event cleared"]')
    NOTIFICATION_ABOUT_OFFLINE_MODE = (MobileBy.ACCESSIBILITY_ID, 'Offline mode')


class TypesOfEventsScreen:
    """A class for Type of Events screen locators - first screen after creating new event with types of events."""
    INCIDENT_TYPE_OF_EVENT = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Incident")]]')
    EVENT_FOR_ON_LOAD_SAVE = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "event_for_on_load")]]')
    EVENT_FOR_CHOOSER_FIELDS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "event_for_chooser")]]')


class EventEditScreen:
    """A class for Edit Events screen locators - screen after opening edit mode of event or creating a new one."""
    SAVE_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Save"]')
    NAME_FIELD = (MobileBy.XPATH, '//XCUIElementTypeTextField[1]')
    NAME_FIELD_by_index = (MobileBy.XPATH, '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]'
                                           '/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]'
                                           '/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]'
                                           '/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]'
                                           '/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]'
                                           '/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]')
    SEVERITY_LEVEL_SELECTOR = (MobileBy.XPATH, '//XCUIElementTypeOther[4]/XCUIElementTypeOther[3]')
    # CHOOSE_SEVERITY_LVL1_iPad = (MobileBy.XPATH, '//XCUIElementTypeTableCell[@name="Severity 1"]')
    # CHOOSE_SEVERITY_LVL2_iPad = (MobileBy.XPATH, '//XCUIElementTypeTableCell[@name="Severity 2"]')
    # CHOOSE_SEVERITY_LVL3_iPad = (MobileBy.XPATH, '//XCUIElementTypeTableCell[@name="Severity 3"]')
    # CHOOSE_SEVERITY_LVL4_iPad = (MobileBy.XPATH, '//XCUIElementTypeTableCell[@name="Severity 4"]')
    # CHOOSE_SEVERITY_LVL5_iPad = (MobileBy.XPATH, '//XCUIElementTypeTableCell[@name="Severity 5"]')
    CHOOSE_SEVERITY_LVL1_iPad = (MobileBy.XPATH, '//XCUIElementTypeCell/XCUIElementTypeStaticText[@value="Severity 1"]')
    CHOOSE_SEVERITY_LVL2_iPad = (MobileBy.XPATH, '//XCUIElementTypeCell/XCUIElementTypeStaticText[@value="Severity 2"]')
    CHOOSE_SEVERITY_LVL3_iPad = (MobileBy.XPATH, '//XCUIElementTypeCell/XCUIElementTypeStaticText[@value="Severity 3"]')
    CHOOSE_SEVERITY_LVL4_iPad = (MobileBy.XPATH, '//XCUIElementTypeCell/XCUIElementTypeStaticText[@value="Severity 4"]')
    CHOOSE_SEVERITY_LVL5_iPad = (MobileBy.XPATH, '//XCUIElementTypeCell/XCUIElementTypeStaticText[@value="Severity 5"]')
    SEVERITY_PICKER = (MobileBy.XPATH, '//XCUIElementTypeApplication/XCUIElementTypeWindow'
                                       '/XCUIElementTypePicker/XCUIElementTypePickerWheel')
    FINISHED_FIELD = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Finished"]')
    DESCRIPTION_FIELD = (MobileBy.XPATH, '//XCUIElementTypeOther[9]/XCUIElementTypeOther[2]'
                                         '/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]'
                                         '/XCUIElementTypeTextView[1]')
    CREATE_MAPPING_DATA = (MobileBy.XPATH, "//XCUIElementTypeLink[@name[contains(., 'Create mapping data')]]")
    EDIT_MAPPING_DATA = (MobileBy.XPATH, "//XCUIElementTypeLink[@name[contains(., 'Create mapping data')]]")
    ELEMENT_TO_SCROLL = (MobileBy.XPATH, '//XCUIElementTypeApplication[1]/XCUIElementTypeScrollView[2]'
                                         '/XCUIElementTypeImage[1]')
    SEQUENCE_ONLOAD_HEADER = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="sequence_onload"]')
    SEQUENCE_ONLOAD_VALUE = (MobileBy.XPATH, '//XCUIElementTypeTextField[@value="test on load"]')
    SEQUENCE_ONSAVE_HEADER = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="sequence_onsave"]')
    SEQUENCE_ONSAVE_VALUE = (MobileBy.XPATH, '//XCUIElementTypeTextField[@value="(auto)"]')
    NEW_OPTION_LIST_HEADER = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="New option list"]')
    OPTION_LIST_VALUE_1 = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="1"]')
    OPTION_LIST_VALUE_2 = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="2"]')
    OPTION_LIST_VALUE_3 = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="3"]')
    FIELD_TO_RESTORE_1_HEADER = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="field to restore"]')
    FIELD_TO_RESTORE_1_VALUE = (MobileBy.XPATH, '//XCUIElementTypeTextField[@value="value for field 1"]')
    FIELD_TO_RESTORE_2_HEADER = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="New email address"]')
    FIELD_TO_RESTORE_2_VALUE = (MobileBy.XPATH, '//XCUIElementTypeTextField[@value="test@noggin.com"]')
    FIELD_TO_RESTORE_3_HEADER = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="New website address"]')
    FIELD_TO_RESTORE_3_VALUE = (MobileBy.XPATH, '//XCUIElementTypeTextField[@value="http://bitnoi.se/"]')
    CHOOSER_FIELD = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name[contains(., "New events chooser")]]')
    # PREVIOUSLY_CREATED_EVENT_FOR_CHOOSER = (MobileBy.XPATH, '//XCUIElementTypeOther[2]/XCUIElementTypeOther[6]'
    #                                                         '/XCUIElementTypeOther[2]')
    SUBFORM_FIELD_ADD_ROW = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Add row"]')
    NEW_EVENTS_CHOOSER_IN_SUB_FORM = (MobileBy.XPATH, '//XCUIElementTypeStaticText['
                                                      '@name="New events chooser inside sub form"]')
    # PREVIOUSLY_CREATED_EVENT_FOR_SUBFORM_CHOOSER = PREVIOUSLY_CREATED_EVENT_FOR_CHOOSER
    DELETE_SUB_EVENT_FROM_CHOOSER = (MobileBy.XPATH, '//XCUIElementTypeOther[9]/XCUIElementTypeLink[1]'
                                                     '/XCUIElementTypeStaticText[1][@name=""]')


class EventDetailsScreen:
    """A class for Event Details screen locators - screen with event details - after opening event."""
    EDIT_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Edit"]')
    DELETE_EVENT_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Delete event")]]')
    DELETE_CONFIRM_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name="Delete"]')
    NEW_SUB_EVENT = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "New sub event")]]')
    SET_AS_PRIMARY_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name[contains(., "Set as primary")]]')
    EVENT_INFO_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Event info"]')


class Map:
    """A class for Map screen locators."""
    PLOT_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name[contains(., "Plot")]]')
    TOOL_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name[contains(., "Tool")]]')
    POINT_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Point click to expand")]]')
    DEFAULT_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Default"]')
    MAP_AREA_12 = (MobileBy.XPATH, '//XCUIElementTypeImage[5]')
    MAP_AREA_13 = (MobileBy.XPATH, '//XCUIElementTypeImage[8]')
    MAP_AREA_17 = (MobileBy.XPATH, '//XCUIElementTypeImage[2]')
    MAP_AREA_18 = (MobileBy.XPATH, '//XCUIElementTypeImage[3]')
    LINE_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Line")]]')
    CIRCLE_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Circle")]]')
    POLYGON_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Polygon")]]')
    SAVE_MAP_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name[contains(., "Save")]]')
    SAVED_MAP_FOR_MOBILE = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "FOR MOBILE")]]')
    SAVED_MAP_ALL_ACTIVE_EVENTS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "All active events")]]')
    SAVED_MAP_ALL_ASSETS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "All assets")]]')
    SAVED_MAP_ALL_CONTACTS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "All contacts")]]')
    SAVED_MAP_ALL_TASKS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "All tasks")]]')
    DUPLICATED_GEOMETRY = (MobileBy.XPATH, '//XCUIElementTypeImage[@visible="true"][last()]')
    # WHOLE_MAP = (MobileBy.XPATH, '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]')  # wrong locator


class PhotoScreen:
    """A class for Photo screen locators - screen after clicking into Photo button in Main Menu."""
    PHOTO_PAGE_HEADER = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name[contains(., "Send a photo to OCA")]]')
    GALLERY_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]'
                                      '/XCUIElementTypeStaticText[1]')
    TAKE_NEW_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]'
                                       '/XCUIElementTypeStaticText[1]')
    DESCRIPTION_FIELD = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextView')
    SEND_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Send"]')
    RESET_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Reset"]')


class VideoScreen:
    """A class for Video screen locators - screen after clicking into Video button in Main Menu."""
    VIDEO_PAGE_HEADER = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name[contains(., "Send a video to OCA")]]')
    # RECORD_NEW_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]')  # works too
    RECORD_NEW_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Record New"]')


class SoundScreen:
    """A class for Sound screen locators - screen after clicking into Sound button in Main Menu."""
    SOUND_PAGE_HEADER = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name['
                                         'contains(., "Send a sound recording to OCA")]]')
    RECORD_SOUND_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeWindow/'
                                           'XCUIElementTypeStaticText[2]')


class SoundRecorderScreen:
    """A class for Sound Recorder screen locators - screen after clicking into record sound button in Sound Page."""
    RECORD_SOUND = (MobileBy.ACCESSIBILITY_ID, 'toggle audio recording')
    DONE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Done')


class GalleryScreen:
    """A class for handling Gallery"""
    GALLERY_ELEMENT_1 = (MobileBy.XPATH, '//XCUIElementTypeCell[@name[contains(., "Photo")]][1]')
    GALLERY_VIDEOS_POPOVER_iPad = (MobileBy.XPATH, '//XCUIElementTypePopover/XCUIElementTypeTableView/XCUIElementTypeCell[@name="Videos"]')
    GALLERY_VIDEOS_POPOVER = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Videos"]')
    GALLERY_VIDEO_ELEMENT_1 = (MobileBy.XPATH, '//XCUIElementTypeCell[1]')
    USE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Choose')
    FIRST_PHOTO_GALLERY_ELEMENT = (MobileBy.XPATH, '//XCUIElementTypeCollectionView[1]/XCUIElementTypeCell[1]')
    GALLERY_ELEMENTS = (MobileBy.XPATH, '//XCUIElementTypeCollectionView[1]/XCUIElementTypeCell')
    LAST_ELEMENT = (MobileBy.XPATH, '//XCUIElementTypeCollectionView[1]/XCUIElementTypeCell[last()]')


class CameraScreen:
    """A class for handling Camera"""
    PHOTO_CAPTURE = (MobileBy.ACCESSIBILITY_ID, 'PhotoCapture')
    CANCEL_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Cancel')
    CAMERA_CHOOSER = (MobileBy.ACCESSIBILITY_ID, 'FrontBackFacingCameraChooser')
    RETAKE = (MobileBy.ACCESSIBILITY_ID, 'Retake')
    USE_PHOTO = (MobileBy.ACCESSIBILITY_ID, 'Use Photo')
    VIDEO_CAPTURE = (MobileBy.ACCESSIBILITY_ID, 'VideoCapture')  # record and stop recording
    USE_VIDEO = (MobileBy.ACCESSIBILITY_ID, 'Use Video')


class ContactsScreen:
    """A class for handling Contacts screen"""
    FIRST_NAME = (MobileBy.XPATH, '//XCUIElementTypeOther[@name="First name"]')
    CONTACT_TYPE_PERSON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Person")]]')
    CONTACT_TYPE_WITH_ON_LOAD_SEQUENCE = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "contact_with_on_load_sequence")]]')
    CONTACT_TYPE_WITH_VISIBILITY_RULES = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "contact_with_visibility_rules")]]')
    DELETED_CONTACT = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "delete")]]')
    EMAIL_FIELD = (MobileBy.XPATH, '//XCUIElementTypeOther[@name="Email"]')
    IMPORTED_CONTACT_FIRST_NAME_VALUE = (MobileBy.XPATH, '//XCUIElementTypeTextField[@value="Communication"]')
    SEQUENCE_ONSAVE_VALUE = (MobileBy.XPATH, '//XCUIElementTypeTextField[@value="test on save"]')
    ADDRESS_FIELD = (MobileBy.XPATH, '//XCUIElementTypeOther[@name="Address"]')
    NEW_CONTACT_GROUP_TYPE_GROUP = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Group")]]')
    CONTACTS_GROUP = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Contacts")]]')
    USERS_GROUP = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Users")]]')
    MAILING_LIST_GROUP = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Mailing list")]]')
    NEW_CONTACT_GROUP_WITH_ON_LOAD_SEQUENCE = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "contact_group_with_on_load_sequence")]]')
    OFFLINE_CONTACTS_GROUP = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "offline_contact_group")]]')


class TasksScreen:
    """A class for handling New Task screen"""
    TITLE = (MobileBy.XPATH, '//XCUIElementTypeTextField[1]')  # locating input field by xpath with name won't work
    ASSIGNED = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Assigned"]')
    ADD_CONTACTS_AND_GROUPS = (MobileBy.XPATH, '//XCUIElementTypeButton[@name['
                                               'contains(., "Add contacts and groups")]]')
    ADD_RESOURCE_STRUCTURE_NODES = (MobileBy.XPATH, '//XCUIElementTypeButton[@name[contains(., '
                                                    '"Add Resource structure nodes")]]')
    ADD_RESOURCE_ASSIGNMENTS = (MobileBy.XPATH, '//XCUIElementTypeButton[@name['
                                                'contains(., "Add Resource assignments")]]')
    CHOOSE_USERS = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Users"]')
    CHOOSE_CONTACTS = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Contacts"]')
    START_DATE = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Start Date"]')
    HIDE_DATE_PICKER = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Completed Date"]')
    # CREATED_TASK_WITH_APPROVAL = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Report approval")]]')
    CREATED_TASK_WITH_APPROVAL = (MobileBy.XPATH, '//XCUIElementTypeLink[@name="Report approval"]')
    MY_TASKS = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="My Tasks"]')
    ALL_TASKS = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="All Tasks"]')
    COMPLETED_TASKS = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Completed Tasks"]')
    INCOMPLETE_TASKS = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Incomplete Tasks"]')
    ACTION_REQUIRED_TASKS = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Action Required Tasks"]')


class ReportsScreen:
    """A class for handling Reports screen"""
    LODGING_AGENCY_PICKER = (MobileBy.XPATH, '//XCUIElementTypeOther[4]/XCUIElementTypeOther[3]')
    # LODGING_AGENCY = (MobileBy.XPATH, '//XCUIElementTypePopover/XCUIElementTypeTableView/XCUIElementTypeTableCell[2]')
    LODGING_AGENCY = (MobileBy.XPATH, '//XCUIElementTypeCell/XCUIElementTypeStaticText[@value="contact_group_for_tests"]')  # contact_group_for_tests
    PUBLISH_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Publish"]')
    # CREATED_REPORT_WITH_ALL_FIELDS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Large")]]')
    CREATED_REPORT_WITH_ALL_FIELDS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name="Large Report"]')
    CREATED_REPORT_WITH_CHOOSER_FIELDS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "chooser fields")]]')
    CREATED_REPORT_WITH_ASSIGNED_QUESTION = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "assigned question")]]')
    REPORT_TYPE_WITH_ALL_FIELDS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "report_for_tests")]]')
    REPORT_TYPE_WITH_CHOOSER_FIELDS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "report_with_chooser_fields")]]')
    REPORT_TYPE_WITH_ON_CREATE_APPROVAL_WORKFLOW = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "report_with_on_create_approval")]]')
    REPORT_TYPE_WITH_ON_LOAD_SEQUENCE = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "report_with_on_load_sequence")]]')
    REPORT_TYPE_WITH_VISIBILITY_RULES = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "report_with_visibility_rules")]]')
    REPORT_TYPE_WITH_ASSIGNED_QUESTION = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "report_with_assigned_question")]]')
    ASSETS_CHOOSER_FIELD = (MobileBy.XPATH, '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[10]/XCUIElementTypeOther[2]')  # inside already created report
    ON_LOAD_FIELD = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="on_load"]')
    NEW_OPTION_LIST = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="New option list"]')
    MEDIA_RELEASE_FIELD = (MobileBy.XPATH, '//XCUIElementTypeOther[6]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeTextView[1]')


class LogsScreen:
    """A class for handling Logs screen"""
    LODGING_AGENCY_PICKER = (MobileBy.XPATH, '//XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]')  # different locator than in New Report Page
    ENTRY_FIELD = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextView')
    #CREATED_LOG_WITH_ALL_FIELDS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name="all fields"]')
    CREATED_LOG_WITH_ALL_FIELDS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "all fields")]]')
    LOG_TYPE_WITH_ALL_FIELDS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "log_with_all_fields")]]')
    LOG_TYPE_WITH_CHOOSER_FIELDS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "log_with_chooser_fields")]]')
    LOG_TYPE_WITH_ON_LOAD_SEQUENCE = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "log_with_on_load_sequence")]]')
    LOG_TYPE_WITH_VISIBILITY_RULES = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "log_with_visibility_rules")]]')


class SentScreen:
    """A class for handling Sent screen"""
    SEARCH = EventsScreen.SEARCH_FIELD
    SENT_COMMUNICATIONS_EMAIL = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Short message, Email")]]')


class ComposeScreen:
    """A class for handling Compose screen"""
    ADD_RECIPIENTS_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Add recipients")]]')
    MESSAGE_EMAIL = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Email")]]')
    EMAIL_SUBJECT_FIELD = (MobileBy.XPATH, '//XCUIElementTypeTextField[1]')
    EMAIL_TEXT_FIELD = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextView')
    MESSAGE_SMS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "SMS")]]')
    SMS_TEXT_FIELD = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextView')
    MESSAGE_VOICE = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Voice")]]')
    VOICE_TEXT_FIELD = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextView')
    TEXT_TO_SPEECH_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name="Text-to-speech"]')
    MESSAGE_FAX = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Fax")]]')
    FAX_DOCUMENT_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Fax document")]]')
    COMMS_DOCUMENTS_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeLink[@name="Comms documents"]')
    FILES_LIST = (MobileBy.CLASS_NAME, '')
    FAX_PDF_FILE = (MobileBy.ACCESSIBILITY_ID, 'OCA Generic Escalation Fax.pdf')
    FAX_OK_BUTTON = (MobileBy.ID, 'faxOK')
    REQUIRE_ACKNOWLEDGMENT = (MobileBy.XPATH, '//XCUIElementTypeLink[@name'
                                              '[contains(., "Require acknowledgment")]]')
    REPLY_TRACKING = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Reply tracking")]]')
    READ_ACCESS_LEVEL = (MobileBy.XPATH, '')
    ADD_CONTACTS_AND_GROUPS = (MobileBy.XPATH, '//XCUIElementTypeButton[@name'
                                               '[contains(., "Add contacts and groups")]]')
    ADD_RESOURCES_STRUCTURE_NODES = (MobileBy.XPATH, '//XCUIElementTypeButton[@name'
                                                     '[contains(., "Add Resource structure ")]]')
    CONTACTS_ARROW = (MobileBy.XPATH, '//XCUIElementTypeOther[2]/XCUIElementTypeLink[1]/XCUIElementTypeLink[1]/XCUIElementTypeStaticText[1]')
    USERS_ARROW = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains'
                                   '(., "Users")]]/XCUIElementTypeLink[@index="2"]')
    MAILING_LIST_UNSUBSCRIBES_ARROW = (MobileBy.XPATH, '//XCUIElementTypeLink[@name'
                                                       '[contains(., "Mailing list unsubscribes ")]]'
                                                       '/XCUIElementTypeLink[@index="2"]')
    CONTACT_FOR_APPIUM_TESTS = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="A_CONTACT_FOR_APPIUM_TESTS"]')
    ALERT_SEND_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Send"]')


class RisksScreen:
    """A class for handling Risks screen"""
    CHOOSE_STATUS_IMPLEMENTED_iPad = (MobileBy.XPATH, '//XCUIElementTypeTableCell[@name="Implemented"]')
    CREATE_RISK_REGISTER = (MobileBy.ACCESSIBILITY_ID, 'Create risk register')
    PREVIOUSLY_CREATED_RISK_REGISTER = (MobileBy.XPATH, '')
    NEW_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name[contains(., "New")]]')
    VIEW_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name[contains(., "View")]]')
    #STATUS_SELECTOR = (MobileBy.XPATH, '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeWebView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]')
    STATUS_SELECTOR = (MobileBy.XPATH, '//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]')


class AssetsScreen:
    """A class for handling Assets screen"""
    CREATED_MAP_ASSET = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Map")]]')
    CREATED_ASSET_WITH_NAME_BALLART = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "Ballarat")]]')
    ASSET_TYPE_WITH_MAX_NUMBER_OF_FIELDS = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "asset_with_max_number_of_fields")]]')
    ASSET_TYPE_WITH_VISIBILITY_RULES = (MobileBy.XPATH, '//XCUIElementTypeLink[@name[contains(., "asset_with_visibility_rules")]]')

