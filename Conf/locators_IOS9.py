""" locators for iOS 9 """

# indexes in iOS9 is staring from 1

from appium.webdriver.common.mobileby import MobileBy


class iOS:
    """A class for handling iOS device for example keyboard"""
    BUTTON_DONE_TO_HIDE_KEYBOARD = (MobileBy.XPATH, '//UIAWindow[2]/UIAToolbar[1]/UIAButton[@name="Done"]')
    RETURN_BUTTON = (MobileBy.XPATH, '//UIAButton[@name="Return"]')
    BUTTON_ALLOW_LOCATION = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[7]/UIAAlert[1]/UIACollectionView[1]'
                                             '/UIACollectionCell[2]/UIAButton[@name="Allow"]')
    IOS_OK = (MobileBy.ACCESSIBILITY_ID, 'OK')
    # IOS_ALLOW = (MobileBy.ACCESSIBILITY_ID, "Allow")
    IOS_ALLOW = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[7]/UIAAlert[1]/UIACollectionView[1]'
                                 '/UIACollectionCell[2]/UIAButton[@name="Allow"]')
    AIRPLANE_MODE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Airplane Mode')
    # AIRPLANE_MODE_BUTTON = (MobileBy.XPATH, '//UIAElement[@name="Airplane Mode"][@value="0"]')


class DeviceSettings:
    """A class for handling Device Settings"""
    GENERAL = (MobileBy.XPATH, '//UIATableCell[@name="General"]')
    KEYBOARD = (MobileBy.XPATH, '//UIATableCell[@name="Keyboard"]')
    AUTO_CORRECTION = (MobileBy.XPATH, '//UIATableCell[@name="Auto-Correction"][@value="1"]')


class CommonScreen:
    """A class for handling Common buttons on different screen"""
    LOADING = (MobileBy.XPATH, '//UIAStaticText[@name="loading"]')
    UPLOADING = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Uploading")]]')
    SAVE_BUTTON = (MobileBy.XPATH, '//UIAButton[@name="Save"]')
    CANCEL_BUTTON = (MobileBy.XPATH, '//UIAButton[@name="Cancel"]')
    OK_BUTTON = (MobileBy.XPATH, '//UIAButton[@name="Ok"]')
    PICKER_WHEEL = (MobileBy.CLASS_NAME, 'UIAPickerWheel')
    WEB_VIEW = (MobileBy.CLASS_NAME, 'UIAWebView')
    WHOLE_APP_SCREEN = (MobileBy.XPATH, '//UIAApplication[@name="OCA"]')
    FIRST_INPUT_FIELD = (MobileBy.XPATH, '//UIATextField[1]')  # locating input field by xpath with name won't work
    ADD_MEDIA = (MobileBy.NAME, 'Add media')
    ADD_MEDIA2 = (MobileBy.XPATH, '//UIAButton[@name="Add media"]')
    POPUP_UNFILLED_FIELDS = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Required fields are not filled")]]')  # Validation error


class TopBar:
    """A class for top bar locators."""
    # HAMBURGER_FOR_MAIN_MENU = (MobileBy.CSS_SELECTOR, 'div#iconbar')
    # HAMBURGER_FOR_MAIN_MENU = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]'
    #                                            '/UIAWebView[1]/UIALink[3]/UIAStaticText[1]')


class WelcomeScreen:
    """A class for welcome screen locators - first screen after lunching the app."""
    LOCATION_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "LOCATION")]]')
    MY_MESSAGES_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "MY MESSAGES")]]')
    PHOTO_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "PHOTO")]]')
    VIDEO_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "VIDEO")]]')
    SOUND_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "SOUND")]]')
    SETTINGS_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "SETTINGS")]]')
    ABOUT_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "ABOUT")]]')
    LOGIN_BUTTON = (MobileBy.XPATH, '//UIAWebView/UIALink[@name[contains(., "LOGIN")]]')
    # LOGIN_BUTTON_by_index = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[1]'
    #                                          '/UIAScrollView[2]/UIAWebView[1]/UIALink[9]'
    #                                          '[@name[contains(., "LOGIN")]]')


class SettingsScreen:
    """A class for settings screen locators - screen after clicking settings button"""
    SETTINGS_CONTACT_IDENTIFIER_FIELD = (MobileBy.CLASS_NAME, 'UIATextField')
    SETTINGS_ALERT_APP_HAS_BEEN_ACTIVATED = (MobileBy.XPATH, '//UIAStaticText[@name="App has been activated."]')
    SETTINGS_OK_BUTTON = (MobileBy.XPATH, '//UIALink[@name="Ok"]')


class LoginScreen:
    """A class for login screen locators - screen after clicking into LOGIN."""
    TEXTFIELD_USERNAME = (MobileBy.XPATH, '//UIAWebView[1]/UIATextField[1]')
    TEXTFIELD_PASSWORD = (MobileBy.XPATH, '//UIAWebView[1]/UIASecureTextField[1]')
    TEXTFIELD_DOMAIN = (MobileBy.XPATH, '//UIAWebView[1]/UIATextField[1]')
    SUBMIT_BUTTON = (MobileBy.XPATH, '//UIAWebView[1]/UIAButton[@name="Submit"]')
    # SUBMIT_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Submit')  # not working

    # Notification alert: "OCA now supports sending 'App Messages' to your device as notifications."
    NOTIFICATION_ABOUT_SENDING_MESSAGES = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name[contains(., '
                                                               '"OCA now supports ")]]')

    # "No" button for sending notifications on iOS
    NO_FOR_SENDING_NOTIFICATIONS_ON = (MobileBy.XPATH, '//UIAWebView/UIALink[@name="No"]')

    # ACCEPT_BUTTON on Terms and Conditions"
    ACCEPT_BUTTON = (MobileBy.XPATH, '//UIAWebView[1]/UIAButton[@name="Accept"]')

    # alert message with word "Invalid"
    ALERT_MSG_INVALID = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name="Invalid username and/or password"]')

    # alert message with "Your temporary account has been expired"

    ALERT_MSG_EXPIRED = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name[contains'
                                             '(., "Your temporary account has been expired")]]')

    # alert message with "The password for the current user is about to expire"

    ALERT_MSG_WILL_EXPIRE = (MobileBy.XPATH, '//UIAStaticText[@name[contains('
                                                 '., "The password for the current user is about to expire")]]')

    # alert message with word "inactive"
    ALERT_MSG_SUSPENDED = (MobileBy.XPATH, '//UIAWebView/UIAStaticText['
                                               '@name[contains(., "Your account is currently inactive")]]')
    # OK button on alert messages"
    OK_BUTTON = (MobileBy.XPATH, '//UIALink[@name="Ok"]')


class MainMenuScreen(WelcomeScreen):
    """A class for main menu screen locators - first screen after correct login into the app."""
    ACTIVATE_WORKFLOW_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "ACTIVATE WORKFLOW")]]')
    CREATE_CONTACT_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "CREATE CONTACT")]]')
    CREATE_TASK_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "CREATE A TASK")]]')
    CREATE_REPORT_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "CREATE A REPORT")]]')
    WEBSITE_LINK_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "WEBSITE LINK")]]')
    INCIDENT_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "INCIDENT")]]')
    CREATE_ASSETS_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "CREATE ASSETS")]]')
    CREATE_LOG_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "CREATE A LOG")]]')
    RISKS_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "RISKS")]]')
    EVENTS_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "EVENTS")]]')
    LOGS_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "LOGS")]]')
    REPORTS_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "REPORTS")]]')
    MAP_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "MAP")]]')
    ASSETS_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "ASSETS")]]')
    INBOX_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "INBOX")]]')
    COMPOSE_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "COMPOSE")]]')
    SENT_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "SENT")]]')
    TASKS_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "TASKS")]]')
    DOCUMENTS_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "DOCUMENTS")]]')
    CONTACTS_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "CONTACTS")]]')
    ALLOCATE_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "ALLOCATE")]]')
    ACTIVATE_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "ACTIVATE")]]')
    OFFLINE_SYNC_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "OFFLINE SYNC")]]')
    LOGOUT_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "LOGOUT")]]')

    ALERT_ACTIVATE_BUTTON = (MobileBy.XPATH, '//UIALink/UIAStaticText[@name="Activate"]')
    ALERT_CANCEL_BUTTON = (MobileBy.XPATH, '//UIALink/UIAStaticText[@name="Cancel"]')
    ALERT_WORKFLOW_ACTIVATED = (MobileBy.XPATH, '//UIAStaticText[@name="Workflow activated"]')


class LocationScreen:
    """A class for Location screen locators - screen after clicking into Location button in Main Menu."""
    SEND_ONCE_NOW = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Send once now")]]')
    SEND_EVERY_SPINNER = (MobileBy.XPATH, '//UIAWebView/UIAElement[@name="Send every"]')
    CHOOSE_5_MINUTES_OPTION_iPad = (MobileBy.XPATH, '//UIAWindow/UIAPopover/UIATableView/UIATableCell[2]')
    ASSERT_5_MINUTES_OPTION = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name="5 minutes"]')
    FOR_THE_NEXT_SPINNER = (MobileBy.XPATH, '//UIAWebView/UIAElement[@name="For the next"]')
    CHOOSE_1_HOUR_OPTION_iPad = (MobileBy.XPATH, '//UIAWindow/UIAPopover/UIATableView/UIATableCell[3]')
    ASSERT_1_HOUR_OPTION = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name="1 hour"]')
    START_BUTTON = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Start")]]')
    LOCATION_PAGE_HEADER = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Your location was last sent")]]')
    LOCATION_STATUS = (MobileBy.XPATH, "//UIAStaticText[@name[contains(., 'few seconds ago')]]")


class EventsScreen:
    """A class for Events screen locators - screen after clicking into Events button in Main Menu."""
    EVENTS_HEADER = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name="Events"]')

    # filtering events by Type
    ANY_TYPE_EXPAND = (MobileBy.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "Any Type click to expand")]]')
    CHOOSE_TYPE_INCIDENT = (MobileBy.XPATH, '//UIAStaticText[@name="Incident"]')
    INCIDENT_TYPE_EXPAND = (MobileBy.XPATH, '//UIALink[@name[contains(., "Incident click to expand")]]')
    CHOOSE_TYPE_ANY = (MobileBy.XPATH, '//UIAStaticText[@name="Any Type"]')

    # filtering events by Status
    ANY_STATUS_EXPAND = (MobileBy.XPATH, '//UIALink[@name[contains(., "Any Status click to expand")]]')
    CHOOSE_ACTIVE_STATUS = (MobileBy.XPATH, '//UIALink[@name="Active"]')
    ACTIVE_STATUS_EXPAND = (MobileBy.XPATH, '//UIALink[@name[contains(., "Active click to expand")]]')
    CHOOSE_INACTIVE_STATUS = (MobileBy.XPATH, '//UIALink[@name="Inactive"]')
    INACTIVE_STATUS_EXPAND = (MobileBy.XPATH, '//UIALink[@name[contains(., "Inactive click to expand")]]')
    CHOOSE_DRAFT_STATUS = (MobileBy.XPATH, '//UIALink[@name="Draft"]')
    DRAFT_STATUS_EXPAND = (MobileBy.XPATH, '//UIALink[@name[contains(., "Draft click to expand")]]')
    CHOOSE_ANY_STATUS = (MobileBy.XPATH, '//UIALink[@name="Any Status"]')

    # filtering events using search field
    # SEARCH_FIELD = (MobileBy.XPATH, '//UIATextField[@name="Search:"]')
    SEARCH_FIELD = (MobileBy.XPATH, '//UIATextField[@name[contains(., "Search")]]')  # TEST IT

    # creating and editing Events
    MORE_BUTTON = (MobileBy.XPATH, '//UIAButton[@name[contains(., "More")]]')
    NEW_EVENT_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "New event")]]')

    # previously created event
    PREVIOUSLY_CREATED_EVENT = (MobileBy.XPATH, '//UIALink[@name[contains(., "Appium")]]')
    # CREATED_EVENT_2 = (MobileBy.XPATH, '//UIALink[@name[contains(., "Test Appium - second event")]]')
    # CREATED_EVENT_3 = (MobileBy.XPATH, '//UIALink[@name[contains(., "to create sub")]]')
    CLEAR_PRIMARY_EVENT_BUTTON = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name'
                                                  '[contains(., "Clear primary event")]]')
    NOTIFICATION_PRIMARY_EVENT_CLEARED = (MobileBy.XPATH, '//UIAStaticText[@name[contains'
                                                          '(., "Primary event cleared")]]')
    NOTIFICATION_ABOUT_OFFLINE_MODE = (MobileBy.ACCESSIBILITY_ID, 'Offline mode')


class TypesOfEventsScreen:
    """A class for Type of Events screen locators - first screen after creating new event with types of events."""
    INCIDENT_TYPE_OF_EVENT = (MobileBy.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "Incident")]]')
    EVENT_FOR_ON_LOAD_SAVE = (MobileBy.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "event_for_on_load")]]')
    EVENT_FOR_CHOOSER_FIELDS = (MobileBy.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "event_for_chooser")]]')
    EVENT_TYPE_WITH_OPTION_LIST = (MobileBy.XPATH, '//UIAWebView/UIALink[@name[contains(., "event_with_option_list")]]')
    EVENT_FOR_ALL_FIELDS = (MobileBy.XPATH, '//UIAWebView/UIALink[@name[contains(., "event for all fields")]]')
    EVENT_WITH_RICH_TEXT = (MobileBy.XPATH, '//UIAWebView/UIALink[@name[contains(., "event_with_rich_text")]]')


class EventEditScreen:
    """A class for Edit Events screen locators - screen after opening edit mode of event or creating a new one."""
    # SAVE_BUTTON = CommonScreen.SAVE_BUTTON
    SAVE_BUTTON = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Save")]]')
    NAME_FIELD = (MobileBy.XPATH, '//UIAScrollView/UIAWebView/UIATextField[@name="Name"]')
    NAME_FIELD_by_index = (MobileBy.XPATH, '//UIAScrollView/UIAWebView/UIATextField[1]')
    SEVERITY_LEVEL_SELECTOR = (MobileBy.XPATH, '//UIAElement[2]')
    CHOOSE_SEVERITY_LVL1_iPad = (MobileBy.XPATH, '//UIATableCell[@name="Severity 1"]')
    CHOOSE_SEVERITY_LVL2_iPad = (MobileBy.XPATH, '//UIATableCell[@name="Severity 2"]')
    CHOOSE_SEVERITY_LVL3_iPad = (MobileBy.XPATH, '//UIATableCell[@name="Severity 3"]')
    CHOOSE_SEVERITY_LVL4_iPad = (MobileBy.XPATH, '//UIATableCell[@name="Severity 4"]')
    CHOOSE_SEVERITY_LVL5_iPad = (MobileBy.XPATH, '//UIATableCell[@name="Severity 5"]')
    SEVERITY_PICKER = (MobileBy.XPATH, '//UIAApplication/UIAWindow/UIAPicker/UIAPickerWheel')
    FINISHED_FIELD = (MobileBy.XPATH, '//UIAStaticText[@name="Finished"]')
    DESCRIPTION_FIELD = (MobileBy.XPATH, '//UIATextField[3]')
    CREATE_MAPPING_DATA = (MobileBy.XPATH, "//UIALink[@name[contains(., 'Create mapping data')]]")
    EDIT_MAPPING_DATA = (MobileBy.XPATH, "//UIALink[@name[contains(., 'Create mapping data')]]")
    ELEMENT_TO_SCROLL = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAImage[1]')
    SEQUENCE_ONLOAD_HEADER = (MobileBy.XPATH, '//UIAStaticText[@name="sequence_onload"]')
    SEQUENCE_ONLOAD_VALUE = (MobileBy.XPATH, '//UIATextField[@value="test on load"]')
    SEQUENCE_ONSAVE_HEADER = (MobileBy.XPATH, '//UIAStaticText[@name="sequence_onsave"]')
    SEQUENCE_ONSAVE_VALUE = (MobileBy.XPATH, '//UIATextField[@value="(auto)"]')
    NEW_OPTION_LIST_HEADER = (MobileBy.XPATH, '//UIAStaticText[@name="New option list"]')
    OPTION_LIST_VALUE_1 = (MobileBy.XPATH, '//UIAStaticText[@name="1"]')
    OPTION_LIST_VALUE_2 = (MobileBy.XPATH, '//UIAStaticText[@name="2"]')
    OPTION_LIST_VALUE_3 = (MobileBy.XPATH, '//UIAStaticText[@name="3"]')
    OPTION_LIST_VALUE_1_iPad = (MobileBy.XPATH, '//UIATableCell[@name="1"]')
    OPTION_LIST_VALUE_2_iPad = (MobileBy.XPATH, '//UIATableCell[@name="2"]')
    OPTION_LIST_VALUE_3_iPad = (MobileBy.XPATH, '//UIATableCell[@name="3"]')
    FIELD_TO_RESTORE_1_HEADER = (MobileBy.XPATH, '//UIAStaticText[@name="field to restore"]')
    FIELD_TO_RESTORE_1_VALUE = (MobileBy.XPATH, '//UIATextField[@value="value for field 1"]')
    FIELD_TO_RESTORE_2_HEADER = (MobileBy.XPATH, '//UIAStaticText[@name="New email address"]')
    FIELD_TO_RESTORE_2_VALUE = (MobileBy.XPATH, '//UIATextField[@value="test@noggin.com"]')
    FIELD_TO_RESTORE_3_HEADER = (MobileBy.XPATH, '//UIAStaticText[@name="New website address"]')
    FIELD_TO_RESTORE_3_VALUE = (MobileBy.XPATH, '//UIATextField[@value="http://bitnoi.se/"]')
    CHOOSER_FIELD = (MobileBy.XPATH, '//UIAStaticText[@name="New events chooser"]')
    # PREVIOUSLY_CREATED_EVENT_FOR_CHOOSER = (MobileBy.XPATH, '//UIAStaticText[@name[contains('
    #                                                         '., "Test Appium")]]')
    SUBFORM_FIELD_ADD_ROW = (MobileBy.XPATH, '//UIAButton[@name="Add row"]')
    # NEW_EVENTS_CHOOSER_IN_SUB_FORM = (MobileBy.XPATH, '//UIAStaticText[@name[contains'
    #                                                   '(., "New events chooser inside sub form")]]')
    PREVIOUSLY_CREATED_EVENT_FOR_SUBFORM_CHOOSER = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Test")]]')
    DELETE_SUB_EVENT_FROM_CHOOSER = (MobileBy.XPATH, '//UIAWebView[1]/UIALink[4]/UIAStaticText[1]')


class EventDetailsScreen:
    """A class for Event Details screen locators - screen with event details - after opening event."""
    EDIT_BUTTON = (MobileBy.XPATH, '//UIAButton[@name="Edit"]')
    DELETE_EVENT_BUTTON = (MobileBy.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "Delete event")]]')
    DELETE_CONFIRM_BUTTON = (MobileBy.XPATH, '//UIALink[@name="Delete"]')
    NEW_SUB_EVENT = (MobileBy.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "New sub event")]]')
    SET_AS_PRIMARY_BUTTON = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Set as primary")]]')
    EVENT_INFO_BUTTON = (MobileBy.XPATH, '//UIAButton[@name="Event info"]')  # TEST IT


class Map:
    """A class for Map screen locators."""
    PLOT_BUTTON = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Plot")]]')
    TOOL_BUTTON = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Tool")]]')
    POINT_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "Point click to expand")]]')
    DEFAULT_BUTTON = (MobileBy.XPATH, '//UIAStaticText[@name="Default"]')
    MAP_AREA_12 = (MobileBy.XPATH, '//UIAWebView[1]/UIAImage[12]')  # those locators will not work for iOS9 - iPhones
    MAP_AREA_13 = (MobileBy.XPATH, '//UIAWebView[1]/UIAImage[13]')
    MAP_AREA_17 = (MobileBy.XPATH, '//UIAWebView[1]/UIAImage[17]')
    MAP_AREA_18 = (MobileBy.XPATH, '//UIAWebView[1]/UIAImage[18]')
    LINE_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "Line")]]')
    CIRCLE_BUTTON = (MobileBy.XPATH, '//UIAScrollView[2]/UIAWebView[1]/UIALink[@name[contains(., "Circle")]]')
    POLYGON_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "Polygon")]]')
    SAVE_MAP_BUTTON = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Save")]]')
    SAVED_MAP_FOR_MOBILE = (MobileBy.XPATH, '//UIAWebView/UIALink[@name[contains(., "FOR MOBILE")]]')
    MAP_LAYER_FOR_APPIUM = (MobileBy.XPATH, '//UIAWebView/UIALink[@name[contains(., "map_layer_for_appium")]]')
    SAVED_MAP_ALL_ACTIVE_EVENTS = (MobileBy.XPATH, '//UIAWebView/UIALink[@name[contains(., "All active events")]]')
    SAVED_MAP_ALL_ASSETS = (MobileBy.XPATH, '//UIAWebView/UIALink[@name[contains(., "All assets")]]')
    SAVED_MAP_ALL_CONTACTS = (MobileBy.XPATH, '//UIAWebView/UIALink[@name[contains(., "All contacts")]]')
    SAVED_MAP_ALL_TASKS = (MobileBy.XPATH, '//UIAWebView/UIALink[@name[contains(., "All tasks")]]')
    DUPLICATED_GEOMETRY = (MobileBy.XPATH, '//UIAWebView[1]/UIAImage[@visible="true"][last()]')


class PhotoScreen:
    """A class for Photo screen locators - screen after clicking into Photo button in Main Menu."""
    PHOTO_PAGE_HEADER = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Send a photo to OCA")]]')
    GALLERY_BUTTON = (MobileBy.XPATH, '//UIAStaticText[2]')  # appium 1.5.3 can't tap that element - probably it's a bug in Appium - visible: false
    # GALLERY_BUTTON = (MobileBy.XPATH, '//UIAStaticText[@name="Gallery"]')  # this locator will find only text, not the icon
    # TAKE_NEW_BUTTON = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Take New")]]')  # this locator will find only text, not the icon
    TAKE_NEW_BUTTON = (MobileBy.XPATH, '//UIAStaticText[4]')  # appium 1.5.3 can't tap that element - probably it's a bug in Appium - visible: false
    DESCRIPTION_FIELD = (MobileBy.CLASS_NAME, 'UIATextField')
    SEND_BUTTON = (MobileBy.XPATH, '//UIAButton[@name="Send"]')
    RESET_BUTTON = (MobileBy.XPATH, '//UIAButton[@name="Reset"]')


class VideoScreen:
    """A class for Video screen locators - screen after clicking into Video button in Main Menu."""
    VIDEO_PAGE_HEADER = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Send a video to OCA")]]')
    # RECORD_NEW_BUTTON = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Record New")]]')  # this locator will find only text, not the icon
    RECORD_NEW_BUTTON = (MobileBy.XPATH, '//UIAStaticText[4]')  # appium 1.5.3 can't tap that element - probably it's a bug in Appium - visible: false


class SoundScreen:
    """A class for Sound screen locators - screen after clicking into Sound button in Main Menu."""
    SOUND_PAGE_HEADER = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Send a sound recording to OCA")]]')
    RECORD_SOUND_BUTTON = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[2]')  # appium 1.5.3 can't tap that element - probably it's a bug in Appium - visible: false


class SoundRecorderScreen:
    """A class for Sound Recorder screen locators - screen after clicking into record sound button in Sound Page."""
    RECORD_SOUND = (MobileBy.ACCESSIBILITY_ID, 'toggle audio recording')
    DONE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Done')


class GalleryScreen:
    """A class for handling Gallery"""
    GALLERY_ELEMENT_1_iPad = (MobileBy.XPATH, '//UIAPopover[1]/UIACollectionView[1]/UIACollectionCell[1]')
    # GALLERY_ELEMENT_2 = (MobileBy.XPATH, '//UIATableView[1]/UIATableCell[1]')  # not working for iOS9 emulator
    # GALLERY_ELEMENT_1 = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[2][@visible="true"]')
    GALLERY_ELEMENT = (MobileBy.XPATH, '//UIACollectionView[@name="PhotosGridView"]/UIACollectionCell[@visible="true"][last()]')
    # GALLERY_VIDEO = (MobileBy.XPATH, '//UIACollectionView[@name="VideosGridView"]/UIACollectionCell[@visible="true"][last()]')
    GALLERY_VIDEOS_POPOVER_iPad = (MobileBy.XPATH, '//UIAPopover[1]/UIATableView[1]/UIATableCell[@name="Videos"]')
    GALLERY_VIDEOS_POPOVER = (MobileBy.XPATH, '//UIATableCell[@name="Videos"]')
    USE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Use')
    CHOOSE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Choose')


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
    FIRST_NAME = (MobileBy.XPATH, '//UIATextField[@name="First name"]')
    CONTACT_TYPE_PERSON = (MobileBy.XPATH, '//UIALink[@name[contains(., "Person")]]')
    CONTACT_TYPE_WITH_ON_LOAD_SEQUENCE = (MobileBy.XPATH, '//UIALink[@name[contains(., "contact_with_on_load_sequence")]]')
    CONTACT_TYPE_WITH_VISIBILITY_RULES = (MobileBy.XPATH, '//UIALink[@name[contains(., "contact_with_visibility_rules")]]')
    DELETED_CONTACT = (MobileBy.XPATH, '//UIALink[@name[contains(., "delete")]]')
    EMAIL_FIELD = (MobileBy.XPATH, '//UIATextField[@name="Email"]')
    IMPORTED_CONTACT_FIRST_NAME_VALUE = (MobileBy.XPATH, '//UIATextField[@value="Communication"]')
    SEQUENCE_ONSAVE_VALUE = (MobileBy.XPATH, '//UIATextField[@value="test on save"]')
    NEW_CONTACT_GROUP_TYPE_GROUP = (MobileBy.XPATH, '//UIALink[@name[contains(., "Group")]]')
    CONTACTS_GROUP = (MobileBy.XPATH, '//UIALink[@name[contains(., "Contacts")]]')
    USERS_GROUP = (MobileBy.XPATH, '//UIALink[@name[contains(., "Users")]]')
    MAILING_LIST_GROUP = (MobileBy.XPATH, '//UIALink[@name[contains(., "Mailing list")]]')
    NEW_CONTACT_GROUP_WITH_ON_LOAD_SEQUENCE = (MobileBy.XPATH, '//UIALink[@name[contains(., "contact_group_with_on_load_sequence")]]')
    NEW_CONTACT_GROUP_TYPE_CONTACT_GROUP_WITH_RICH_TEXT = (MobileBy.XPATH, '//UIALink[@name[contains(., "contact_group_with_rich_text")]]')
    CONTACT_TYPE_CONTACT_WITH_RICH_TEXT = (MobileBy.XPATH, '//UIALink[@name[contains(., "contact_with_rich_text")]]')
    OFFLINE_CONTACTS_GROUP = (MobileBy.XPATH, '//UIALink[@name[contains(., "offline_contact_group")]]')


class TasksScreen:
    """A class for handling New Task screen"""
    TITLE = (MobileBy.XPATH, '//UIATextField[1]')  # locating input field by xpath with name won't work
    ASSIGNED = (MobileBy.XPATH, '//UIAStaticText[@name="Assigned"]')
    ADD_CONTACTS_AND_GROUPS = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Add contacts and groups")]]')
    ADD_RESOURCE_STRUCTURE_NODES = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Add Resource structure nodes")]]')
    ADD_RESOURCE_STRUCTURE_NODES2 = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Add Resource structure nodes")]]')
    ADD_RESOURCE_ASSIGNMENTS = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Add Resource assignments")]]')
    CHOOSE_USERS = (MobileBy.XPATH, '//UIAStaticText[@name="Users"]')
    CHOOSE_CONTACTS = (MobileBy.XPATH, '//UIAStaticText[@name="Contacts"]')
    START_DATE = (MobileBy.XPATH, '//UIAStaticText[@name="Start Date"]')
    HIDE_DATE_PICKER = (MobileBy.XPATH, '//UIAStaticText[@name="Completed Date"]')
    CREATED_TASK_WITH_APPROVAL = (MobileBy.XPATH, '//UIALink[@name[contains(., "Report approval")]]')
    MY_TASKS = (MobileBy.XPATH, '//UIAStaticText[@name="My Tasks"]')
    ALL_TASKS = (MobileBy.XPATH, '//UIAStaticText[@name="All Tasks"]')
    COMPLETED_TASKS = (MobileBy.XPATH, '//UIAStaticText[@name="Completed Tasks"]')
    INCOMPLETE_TASKS = (MobileBy.XPATH, '//UIAStaticText[@name="Incomplete Tasks"]')
    ACTION_REQUIRED_TASKS = (MobileBy.XPATH, '//UIAStaticText[@name="Action Required Tasks"]')


class ReportsScreen:
    """A class for handling Report screen"""
    # LODGING_AGENCY_PICKER = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAElement[1]')
    LODGING_AGENCY_PICKER_FIELD = (MobileBy.XPATH, '//UIAStaticText[@name="Lodging agency"]/following-sibling::UIAElement[1]')
    LODGING_AGENCY_PICKER = (MobileBy.XPATH, '//UIAWebView/UIAElement[@value="(none)"]')
    LODGING_AGENCY = (MobileBy.XPATH, '//UIAPopover/UIATableView/UIATableCell[2]')  # index in iOS9 is staring from 1
    # LODGING_AGENCY = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIATableView[1]/UIATableCell[2]')
    PUBLISH_BUTTON = (MobileBy.XPATH, '//UIAButton[@name="Publish"]')
    CREATED_REPORT_WITH_ALL_FIELDS = (MobileBy.XPATH, '//UIALink[@name[contains(., "Large")]]')
    CREATED_REPORT_WITH_CHOOSER_FIELDS = (MobileBy.XPATH, '//UIALink[@name[contains(., "chooser_fields")]]')
    CREATED_REPORT_WITH_ASSIGNED_QUESTION = (MobileBy.XPATH, '//UIALink[@name[contains(., "assigned_question")]]')
    REPORT_TYPE_WITH_ALL_FIELDS = (MobileBy.XPATH, '//UIALink[@name[contains(., "report_for_tests")]]')
    REPORT_TYPE_WITH_CHOOSER_FIELDS = (MobileBy.XPATH, '//UIALink[@name[contains(., "report_with_chooser_fields")]]')
    REPORT_TYPE_WITH_ON_CREATE_APPROVAL_WORKFLOW = (MobileBy.XPATH, '//UIALink[@name[contains(., "report_with_on_create_approval")]]')
    REPORT_TYPE_WITH_ON_LOAD_SEQUENCE = (MobileBy.XPATH, '//UIALink[@name[contains(., "report_with_on_load_sequence")]]')
    REPORT_TYPE_WITH_VISIBILITY_RULES = (MobileBy.XPATH, '//UIALink[@name[contains(., "report_with_visibility_rules")]]')
    REPORT_TYPE_WITH_ASSIGNED_QUESTION = (MobileBy.XPATH, '//UIALink[@name[contains(., "report_with_assigned_question")]]')
    REPORT_TYPE_WITH_OPTION_LIST = (MobileBy.XPATH, '//UIALink[@name[contains(., "report_with_option_list")]]')
    REPORT_TYPE_WITH_RICH_TEXT = (MobileBy.XPATH, '//UIALink[@name[contains(., "report_with_rich_text")]]')
    MEDIA_RELEASE_FIELD = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIATextField[2]')


class LogsScreen:
    """A class for handling Logs screen"""
    # LODGING_AGENCY_PICKER = (MobileBy.XPATH, '//UIAWebView/UIAElement[1]')
    LODGING_AGENCY_PICKER = ReportsScreen.LODGING_AGENCY_PICKER
    ENTRY_FIELD = (MobileBy.CLASS_NAME, 'UIATextField')
    ENTRY_FIELD_BY_XPATH = (MobileBy.XPATH, '//UIATextField[1]')
    ENTRY_FIELD_FIRST_PARAGRAPH = ENTRY_FIELD
    # ENTRY_FIELD_BY_XPATH = (MobileBy.XPATH, '//UIAElement[@name[contains(., "Rich Text Editor, entry")]]')  # not working
    # ENTRY_FIELD_FIRST_PARAGRAPH = (MobileBy.XPATH, '//UIAElement[@name="Rich Text Editor, entry"]/UIAElement[1]/UIAElement[1]')  # not working
    CREATED_LOG_WITH_ALL_FIELDS = (MobileBy.XPATH, '//UIALink[@name[contains(., "all fields")]]')
    LOG_TYPE_WITH_ALL_FIELDS = (MobileBy.XPATH, '//UIALink[@name[contains(., "log_with_all_fields")]]')
    LOG_TYPE_WITH_CHOOSER_FIELDS = (MobileBy.XPATH, '//UIALink[@name[contains(., "log_with_chooser_fields")]]')
    LOG_TYPE_WITH_ON_LOAD_SEQUENCE = (MobileBy.XPATH, '//UIALink[@name[contains(., "log_with_on_load_sequence")]]')
    LOG_TYPE_WITH_VISIBILITY_RULES = (MobileBy.XPATH, '//UIALink[@name[contains(., "log_with_visibility_rules")]]')
    LOG_TYPE_WITH_RICH_TEXT = (MobileBy.XPATH, '//UIALink[@name[contains(., "log_with_rich_text")]]')


class SentScreen:
    """A class for handling Sent screen"""
    SEARCH = (MobileBy.XPATH, '//UIATextField[@name="Search"]')
    SENT_COMMUNICATIONS_EMAIL = (MobileBy.XPATH, '//UIALink[@name[contains(., "Short message, Email")]]')


class ComposeScreen:
    """A class for handling Compose screen"""
    ADD_RECIPIENTS_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "Add recipients")]]')
    MESSAGE_EMAIL = (MobileBy.XPATH, '//UIALink[@name[contains(., "Email")]]')
    EMAIL_SUBJECT_FIELD = (MobileBy.XPATH, '//UIATextField[1]')
    EMAIL_TEXT_FIELD = (MobileBy.XPATH, '//UIATextField[2]')
    MESSAGE_SMS = (MobileBy.XPATH, '//UIALink[@name[contains(., "SMS")]]')
    SMS_TEXT_FIELD = (MobileBy.CLASS_NAME, 'UIATextField')
    MESSAGE_VOICE = (MobileBy.XPATH, '//UIALink[@name[contains(., "Voice")]]')
    VOICE_TEXT_FIELD = (MobileBy.CLASS_NAME, 'UIATextField')
    TEXT_TO_SPEECH_BUTTON = (MobileBy.XPATH, '//UIALink[@name="Text-to-speech"]')
    MESSAGE_FAX = (MobileBy.XPATH, '//UIALink[@name[contains(., "Fax")]]')
    FAX_DOCUMENT_BUTTON = (MobileBy.XPATH, '//UIALink[@name[contains(., "Fax document")]]')
    COMMS_DOCUMENTS_BUTTON = (MobileBy.XPATH, '//UIALink[@name="Comms documents"]')
    FAX_PDF_FILE = (MobileBy.XPATH, '//UIAStaticText[@name="OCA Generic Escalation Fax.pdf"]')
    FAX_OK_BUTTON = (MobileBy.XPATH, '//UIAButton[@name="Ok"]')
    REQUIRE_ACKNOWLEDGMENT = (MobileBy.XPATH, '//UIALink[@name'
                                              '[contains(., "Require acknowledgment")]]')
    REPLY_TRACKING = (MobileBy.XPATH, '//UIALink[@name[contains(., "Reply tracking")]]')
    ADD_CONTACTS_AND_GROUPS = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Add contacts and groups")]]')
    ADD_RESOURCES_STRUCTURE_NODES = (MobileBy.XPATH, '//UIAButton[@name'
                                                     '[contains(., "Add Resource structure ")]]')
    CONTACT_FOR_APPIUM_TESTS = (MobileBy.XPATH, '//UIAStaticText[@name="A_CONTACT_FOR_APPIUM_TESTS"]')
    ALERT_SEND_BUTTON = (MobileBy.XPATH, '//UIAButton[4][@name="Send"]')


class RisksScreen:
    """A class for handling Risks screen"""
    # CHOOSE_STATUS_IMPLEMENTED_iPad = (MobileBy.XPATH, '//UIATableCell[@name="Implemented"]')
    CHOOSE_STATUS_IMPLEMENTED_iPad = (MobileBy.XPATH, '//UIAPopover/UIATableView/UIATableCell[3]')  # index is starting from 1
    # CHOOSE_STATUS_IMPLEMENTED_iPad = (MobileBy.XPATH, '//UIAPopover/UIATableCell[@name="Implemented"]')
    CREATE_RISK_REGISTER = (MobileBy.ACCESSIBILITY_ID, 'Create risk register')
    PREVIOUSLY_CREATED_RISK_REGISTER = (MobileBy.XPATH, '')
    NEW_BUTTON = (MobileBy.XPATH, '//UIAButton[@name[contains(., "New")]]')
    VIEW_BUTTON = (MobileBy.XPATH, '//UIAButton[@name[contains(., "View")]]')
    STATUS_SELECTOR = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAElement[1]')
    RISK_TYPE_FOR_TEST = (MobileBy.XPATH, '//UIALink[@name[contains(., "new_risk_type")]]')
    RISK_TYPE_WITH_OPTION_LIST = (MobileBy.XPATH, '//UIALink[@name[contains(., "risk_with_option_list")]]')


class AssetsScreen:
    """A class for handling Assets screen"""
    CREATED_MAP_ASSET = (MobileBy.XPATH, '//UIALink[@name[contains(., "Map")]]')
    CREATED_ASSET_WITH_NAME_BALLART = (MobileBy.XPATH, '//UIALink[@name[contains(., "Ballarat")]]')
    ASSET_TYPE_WITH_MAX_NUMBER_OF_FIELDS = (MobileBy.XPATH, '//UIALink[@name[contains(., "asset_with_max_number_of_fields")]]')
    ASSET_TYPE_WITH_VISIBILITY_RULES = (MobileBy.XPATH, '//UIALink[@name[contains(., "asset_with_visibility_rules")]]')
    ASSET_TYPE_WITH_OPTION_LIST = (MobileBy.XPATH, '//UIALink[@name[contains(., "asset_with_option_list")]]')
    ASSET_TYPE_WITH_RICH_TEXT = (MobileBy.XPATH, '//UIALink[@name[contains(., "asset_with_rich_text")]]')
    SAVE_OPTION_LIST = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Save")]]')
    NEW_DATE_OPTIONAL_TIME2 = (MobileBy.XPATH, '//UIAStaticText[@name="New date & optional time2"]')
    OPTION_LIST_READ_ONLY_IOS = (MobileBy.XPATH, '//UIAStaticText[@name="Is Read only ?"]')
    NEW_PHONE_NUMBER = (MobileBy.XPATH, '//UIATextField[@value="+61212345111" and @enabled="true"]')
    NEW_FAX_NUMBER = (MobileBy.XPATH, '//UIATextField[@value="+61212345222" and @enabled="true"]')
    NEW_EMAIL_ADDRESS = (MobileBy.XPATH, '//UIATextField[@value="testbitnoise@gmail.com" and @enabled="true"]')
    NEW_WEBSITE_ADDRESS = (MobileBy.XPATH, '//UIATextField[@value="http://www.google.com" and @enabled="true"]')
    NEW_SINGLE_LINE_TEXT = (MobileBy.XPATH, '//UIATextField[@value="test_appium_single_line" and @enabled="true"]')
    NEW_MULTI_LINE_TEXT = (MobileBy.XPATH, '//UIATextField[@value="test_appium_multi_line" and @enabled="true"]')
    NEW_PHONE_NUMBER_DISABLED_1 = (MobileBy.XPATH, '//UIATextField[@value="+61212345111" and @enabled="false"]')
    NEW_FAX_NUMBER_DISABLED_1 = (MobileBy.XPATH, '//UIATextField[@value="+61212345222" and @enabled="false"]')
    NEW_PHONE_NUMBER_DISABLED_2 = (MobileBy.XPATH, '//UIATextField[@value="(02) 1234 5111" and @enabled="false"]')
    NEW_FAX_NUMBER_DISABLED_2 = (MobileBy.XPATH, '//UIATextField[@value="(02) 1234 5222" and @enabled="false"]')
    NEW_EMAIL_ADDRESS_DISABLED = (MobileBy.XPATH, '//UIATextField[@value="testbitnoise@gmail.com" and @enabled="false"]')
    NEW_WEBSITE_ADDRESS_DISABLED = (MobileBy.XPATH, '//UIATextField[@value="http://www.google.com" and @enabled="false"]')
    NEW_SINGLE_LINE_TEXT_DISABLED = (MobileBy.XPATH, '//UIATextField[@value="test_appium_single_line" and @enabled="false"]')
    NEW_MULTI_LINE_TEXT_DISABLED = (MobileBy.XPATH, '//UIATextField[@value="test_appium_multi_line" and @enabled="false"]')
    NEW_PHONE_NUMBER2 = (MobileBy.XPATH, '//UIATextField[@value="+61212345333" and @enabled="true"]')
    NEW_FAX_NUMBER2 = (MobileBy.XPATH, '//UIATextField[@value="+61212345444" and @enabled="true"]')
    NEW_EMAIL_ADDRESS2 = (MobileBy.XPATH, '//UIATextField[@value="testbit@wp.pl" and @enabled="true"]')
    NEW_WEBSITE_ADDRESS2 = (MobileBy.XPATH, '//UIATextField[@value="http://www.bitnoi.se" and @enabled="true"]')
    NEW_SINGLE_LINE_TEXT2 = (MobileBy.XPATH, '//UIATextField[@value="test_appium_single_line2" and @enabled="true"]')
    NEW_MULTI_LINE_TEXT2 = (MobileBy.XPATH, '//UIATextField[@value="test_appium_multi_line2" and @enabled="true"]')
