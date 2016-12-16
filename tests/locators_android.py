# from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class TopBar:
    """A class for top bar locators."""
    HAMBURGER_FOR_MAIN_MENU = (MobileBy.XPATH, "//android.webkit.WebView[@index='0']"
                                               "/android.view.View[@index='0']"
                                               "/android.view.View[@index='2']"
                                               "/android.view.View[@index='0']")


class WelcomeScreen:
    """A class for welcome screen locators - first screen after lunching the app."""
    LOGIN_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "LOGIN")]]')
    LOGIN_BUTTON_by_index = (MobileBy.XPATH, '//android.webkit.WebView/android.view.View/'
                                             'android.view.View[@index="6"]/android.view.View[@index="0"]')


class LoginScreen:
    """A class for login screen locators - screen after clicking into LOGIN."""
    TEXTFIELD_USERNAME = (MobileBy.XPATH, '//android.widget.EditText[@index="1"]')
    TEXTFIELD_PASSWORD = (MobileBy.XPATH, '//android.widget.EditText[@index="3"]')
    TEXTFIELD_DOMAIN = (MobileBy.XPATH, '//android.widget.EditText[@index="5"]')
    SUBMIT_BUTTON = (MobileBy.XPATH, '//android.widget.Button[@content-desc="Submit"]')

    # Notification alert: "OCA now supports sending 'App Messages' to your device as notifications."
    NOTIFICATION_ABOUT_SENDING_MESSAGES = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., '
                                                           '"OCA now supports ")]]')

    # "No" button for sending notifications on iOS
    NO_FOR_SENDING_NOTIFICATIONS_ON = (MobileBy.XPATH, '//android.view.View[@content-desc="No"]')

    # ACCEPT_BUTTON on Terms and Conditions"
    ACCEPT_BUTTON = (MobileBy.XPATH, '//android.widget.Button[@content-desc="Accept"]')

    # alert message with word "Invalid"
    ALERT_MSG_INVALID = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Invalid")]]')

    # alert message with "Your temporary account has been expired"
    ALERT_MSG_EXPIRED = (MobileBy.XPATH, '//android.view.View[@content-desc[contains('
                                         '., "Your temporary account has been expired")]]')

    # alert message with "The password for the current user is about to expire"
    ALERT_MSG_WILL_EXPIRE = (MobileBy.XPATH,
                             '//android.view.View[@content-desc[contains('
                             '., "The password for the current user is about to expire")]]')

    # alert message with word "inactive"
    ALERT_MSG_SUSPENDED = (MobileBy.XPATH,
                           '//android.view.View[@content-desc[contains(., "Your account is currently inactive")]]')

    # OK button on alert messages"
    OK_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc="Ok"]')


class MainMenuScreen:
    """A class for main menu screen locators - first screen after correct login into the app."""
    BUTTONS = (MobileBy.CLASS_NAME, 'android.view.View')
    LOGOUT_BUTTON = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "LOGOUT")]]')
    EVENTS_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "EVENTS")]]')
    LOCATION_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "LOCATION")]]')


class LocationScreen:
    """A class for Location screen locators - screen after clicking into Location button in Main Menu."""
    SEND_ONCE_NOW = (MobileBy.XPATH, '//android.widget.Button[@content-desc[contains(., "Send once now")]]')
    SEND_EVERY_SPINNER = (MobileBy.XPATH, '//android.widget.Spinner[@index="7"]')
    CHOOSE_1_HOUR_OPTION = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="1 hour"]')
    ASSERT_1_HOUR_OPTION = (MobileBy.XPATH, '//android.widget.Spinner[@content-desc="1 hour"]')
    ASSERT_SENDING_NOW = (MobileBy.XPATH, '//android.widget.Button[content-desc[contains(., "Sending now")]]')
    START_BUTTON = (MobileBy.XPATH, '//android.widget.Button[@content-desc[contains(., "Start")]]')
    START_BUTTON_disabled = (MobileBy.XPATH, '//android.widget.Button[@content-desc['
                                             'contains(., "Start")] and @enabled="false"]')
    LOCATION_PAGE_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc['
                                            'contains(., "Your location was last sent")]]')


class EventsScreen:
    """A class for Events screen locators - screen after clicking into Events button in Main Menu."""
    EVENTS_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Events")]]')

    # filtering events by Type
    ANY_TYPE_EXPAND = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Any Type click to expand")]]')
    CHOOSE_TYPE_INCIDENT = (MobileBy.XPATH, '//android.view.View[@content-desc="Incident"]')
    INCIDENT_TYPE_EXPAND = (MobileBy.XPATH, '//android.view.View[@content-desc[contains('
                                            '., "Incident click to expand")]]')
    CHOOSE_TYPE_ANY = (MobileBy.XPATH, '//android.view.View[@content-desc="Any Type"]')

    # filtering events by Status
    ANY_STATUS_EXPAND = (MobileBy.XPATH, '//android.view.View[@content-desc[contains('
                                         '., "Any Status click to expand")]]')
    CHOOSE_ACTIVE_STATUS = (MobileBy.XPATH, '//android.view.View[@content-desc="Active"]')
    ACTIVE_STATUS_EXPAND = (MobileBy.XPATH, '//android.view.View[@content-desc[contains('
                                            '., "Active click to expand")]]')
    CHOOSE_INACTIVE_STATUS = (MobileBy.XPATH, '//android.view.View[@content-desc="Inactive"]')
    INACTIVE_STATUS_EXPAND = (MobileBy.XPATH, '//android.view.View[@content-desc[contains('
                                              '., "Inactive click to expand")]]')
    CHOOSE_DRAFT_STATUS = (MobileBy.XPATH, '//android.view.View[@content-desc="Draft"]')
    DRAFT_STATUS_EXPAND = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Draft click to expand")]]')
    CHOOSE_ANY_STATUS = (MobileBy.XPATH, '//android.view.View[@content-desc="Any Status"]')

    # filtering events using search field
    SEARCH_FIELD = (MobileBy.XPATH, '//android.widget.EditText[@index="3"]')
    EVENTS_HEADER_AFTER_SEARCH = (MobileBy.XPATH, '//android.view.View[@index="5"]')

    # creating and editing Events
    MORE_BUTTON = (MobileBy.XPATH, '//android.widget.Spinner[@content-desc[contains(., "More")]]')
    NEW_EVENT_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "New event")]]')

    # previously created event
    CREATED_EVENT_1 = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Test Appium Android")]]')
    CREATED_EVENT_2 = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., " second event")]]')
    CREATED_EVENT_3 = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., " to create sub event")]]')
    CLEAR_PRIMARY_EVENT_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains('
                                                  '., "Clear primary event")]]')
    NOTIFICATION_PRIMARY_EVENT_CLEARED = (MobileBy.XPATH, '//android.view.View[@content-desc="Primary event cleared"]')
    GO_BACK_TO_MAIN_MENU_ARROW_BUTTON = (MobileBy.XPATH, "//android.webkit.WebView[@index='0']"
                                                         "//android.view.View[@index='0']"
                                                         "//android.view.View[@index='0']")


class TypesOfEventsScreen:
    """A class for Type of Events screen locators - first screen after creating new event with types of events."""
    INCIDENT_TYPE_OF_EVENT = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Incident")]]')
    EVENT_FOR_ON_LOAD_SAVE = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "event_for_on_load")]]')
    EVENT_FOR_CHOOSER_FIELDS = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "event_for_chooser")]]')


class EventEditScreen:
    """A class for Edit Events screen locators - screen after opening edit mode of event or creating a new one."""
    NAME_FIELD = (MobileBy.XPATH, '//android.widget.EditText[@index="1"]')
    SEVERITY_LEVEL_SELECTOR = (MobileBy.XPATH, '//android.widget.ListView[@index="0"]'
                                               '//android.view.View[@index="3"]'
                                               '//android.widget.Spinner[@index="2"]')
    CHOOSE_SEVERITY_LVL1 = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Severity 1"]')
    CHOOSE_SEVERITY_LVL2 = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Severity 2"]')
    CHOOSE_SEVERITY_LVL3 = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Severity 3"]')
    CHOOSE_SEVERITY_LVL4 = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Severity 4"]')
    FINISHED_FIELD = (MobileBy.XPATH, '//android.view.View[@content-desc="Finished"]')
    TIME_DATE = (MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="Increase year"]')
    SET_BUTTON = (MobileBy.ID, 'android:id/button1')
    SAVE_BUTTON = (MobileBy.XPATH, '//android.widget.Button[@content-desc="Save"]')
    DESCRIPTION_FIELD = (MobileBy.XPATH,
                         "//android.widget.ListView[@index='0']"
                         "//android.view.View[@index='8' and @content-desc[contains(., 'Description')]]"
                         "//android.view.View[@index='1']"
                         "//android.view.View[@index='1']"
                         "//android.view.View[@index='0']"
                         "//android.view.View[@index='0']"
                         "//android.view.View[@index='0' and @clickable='true']")

    # headers for scrolling
    FINISHED_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="Finished"]')
    LEADAGENCY_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="Lead agency"]')
    IMPACT_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="Impact"]')
    CAUSE_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="Cause"]')
    SITUATION_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="Situation"]')
    ISSUES_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="Issues"]')
    OBJECTIVES_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="Objectives"]')
    STRATEGIES_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="Strategies"]')
    TACTICS_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="Tactics"]')
    COMMUNICATIONS_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="Communications"]')
    RELATED_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="Related"]')

    CREATE_MAPPING_DATA = (MobileBy.XPATH, "//android.view.View[@content-desc[contains(., 'Create mapping data')]]")
    EDIT_MAPPING_DATA = (MobileBy.XPATH, "//android.view.View[@content-desc[contains(., 'Edit mapping data')]]")
    SEQUENCE_ONLOAD_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="sequence_onload"]')
    SEQUENCE_ONLOAD_VALUE = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="test on load"]')
    SEQUENCE_ONSAVE_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="sequence_onsave"]')
    SEQUENCE_ONSAVE_VALUE = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="(auto)"]')
    NEW_OPTION_LIST_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="New option list"]')
    OPTION_LIST_VALUE_1 = (MobileBy.XPATH, '//android.view.View[@content-desc="1"]')
    OPTION_LIST_VALUE_2 = (MobileBy.XPATH, '//android.view.View[@content-desc="2"]')
    OPTION_LIST_VALUE_3 = (MobileBy.XPATH, '//android.view.View[@content-desc="3"]')
    FIELD_TO_RESTORE_1_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="field to restore"]')
    FIELD_TO_RESTORE_1_VALUE = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="value for field 1"]')
    FIELD_TO_RESTORE_2_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="New email address"]')
    FIELD_TO_RESTORE_2_VALUE = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="test@noggin.com"]')
    CANCEL_BUTTON = (MobileBy.XPATH, '//android.widget.Button[@content-desc="Cancel"]')
    CHOOSER_FIELD = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "New events chooser")]]')
    PREVIOUSLY_CREATED_EVENT_FOR_CHOOSER = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Test")]]')
    SUBFORM_FIELD_ADD_ROW = (MobileBy.XPATH, '//android.widget.Button[@content-desc="Add row"]')
    NEW_EVENTS_CHOOSER_IN_SUB_FORM = (MobileBy.XPATH, '//android.view.View[@content-desc['
                                                      'contains(., "New events chooser inside sub form")]]')
    DELETE_SUB_EVENT_FROM_CHOOSER = (MobileBy.XPATH, '//android.widget.ListView/android.view.View[@index="8"]'
                                                     '/android.view.View[@index="1"]')


class EventDetailsScreen:
    """A class for Event Details screen locators - screen with event details - after opening event."""
    EDIT_BUTTON = (MobileBy.XPATH, '//android.widget.Button[@content-desc="Edit"]')
    DELETE_EVENT_BUTTON = (MobileBy.XPATH, "//android.widget.ListView[@index='2']"
                                           "//android.view.View[@index='2']"
                                           "//android.view.View[@content-desc[contains(., 'Delete event')]]")
    DELETE_CONFIRM_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc="Delete"]')
    NEW_SUB_EVENT = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "New sub event")]]')
    SET_AS_PRIMARY_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Set as primary")]]')


class Map:
    """A class for Map screen locators."""
    TOOL_BUTTON = (MobileBy.XPATH, "//android.widget.Spinner[@content-desc[contains(., 'Tool')]]")
    POINT_BUTTON = (MobileBy.XPATH, "//android.view.View[@content-desc[contains(., 'Point click to expand')]]")
    DEFAULT_BUTTON = (MobileBy.XPATH, "//android.view.View[@content-desc='Default']")
    MAP_AREA_9 = (MobileBy.XPATH, "//android.widget.Image[@index='9']")
    MAP_AREA_5 = (MobileBy.XPATH, "//android.widget.Image[@index='5']")
    MAP_AREA_6 = (MobileBy.XPATH, "//android.widget.Image[@index='6']")
    LINE_BUTTON = (MobileBy.XPATH, "//android.view.View[@content-desc[contains(., 'Line')]]")
    CIRCLE_BUTTON = (MobileBy.XPATH, "//android.view.View[@content-desc[contains(., 'Circle')]]")
    POLYGON_BUTTON = (MobileBy.XPATH, "//android.view.View[@content-desc[contains(., 'Polygon')]]")
    SAVE_MAP_BUTTON = (MobileBy.XPATH, "//android.widget.Button[@content-desc='Save']")


class CameraScreen:
    """A class for handling Camera"""
    PHOTO_CAPTURE = (MobileBy.ACCESSIBILITY_ID, 'Shutter')
    CANCEL_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Review cancel')
    CAMERA_CHOOSER = (MobileBy.ID, 'com.android.camera2:id/btn_switch_camera')
    CAMERA_CHOOSER2 = (MobileBy.ID, 'com.tct.camera:id/onscreen_camera_picker')
    RETAKE = (MobileBy.ACCESSIBILITY_ID, 'Review retake')
    USE_PHOTO = (MobileBy.ACCESSIBILITY_ID, 'Review done')
    USE_PHOTO2 = (MobileBy.ACCESSIBILITY_ID, 'OK')


class Android:
    """A class for handling Android device for example alerts"""

    ANDROID_ALLOW = (MobileBy.ID, 'com.android.packageinstaller:id/permission_allow_button')
    PHOTO_FROM_GALLERY = (MobileBy.ID, 'com.android.documentsui:id/icon_thumb')
