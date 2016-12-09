from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class WelcomeScreen(object):
    """A class for welcome screen locators - first screen after lunching the app."""
    LOGIN_BUTTON = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "LOGIN")]]')
    LOGIN_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "LOGIN")]]')


class LoginScreen(object):
    """A class for login screen locators - screen after clicking into LOGIN."""
    TEXTFIELD_USERNAME = (MobileBy.XPATH, './/android.widget.EditText[@index="1"]')
    TEXTFIELD_USERNAME_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIATextField[1]')
    TEXTFIELD_PASSWORD = (MobileBy.XPATH, './/android.widget.EditText[@index="3"]')
    TEXTFIELD_PASSWORD_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIASecureTextField[1]')
    TEXTFIELD_DOMAIN = (MobileBy.XPATH, './/android.widget.EditText[@index="5"]')
    TEXTFIELD_DOMAIN_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIATextField[2]')
    SUBMIT_BUTTON = (MobileBy.XPATH, '//android.widget.Button[@content-desc="Submit"]')
    SUBMIT_BUTTON_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAButton[@name="Submit"]')

    # Notification alert: "OCA now supports sending 'App Messages' to your device as notifications."
    NOTIFICATION_ABOUT_SENDING_MESSAGES_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name[contains(., '
                                                         '"OCA now supports ")]]')

    # "No" button for sending notifications on iOS
    NO_FOR_SENDING_NOTIFICATIONS_ON_ios = (MobileBy.XPATH, '//UIAWebView/UIALink[@name="No"]')

    # ACCEPT_BUTTON on Terms and Conditions"
    ACCEPT_BUTTON = (MobileBy.XPATH, './/android.widget.Button[@content-desc="Accept"]')
    ACCEPT_BUTTON_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAButton[@name="Accept"]')

    # alert message with word "Invalid"
    ALERT_MSG_INVALID = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "Invalid")]]')
    ALERT_MSG_INVALID_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name="Invalid username and/or password"]')

    # alert message with "Your temporary account has been expired"
    ALERT_MSG_EXPIRED = (MobileBy.XPATH, './/android.view.View[@content-desc[contains('
                                   '., "Your temporary account has been expired")]]')

    ALERT_MSG_EXPIRED_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name[contains'
                                       '(., "Your temporary account has been expired")]]')

    # alert message with "The password for the current user is about to expire"
    ALERT_MSG_WILL_EXPIRE = (MobileBy.XPATH,
                             './/android.view.View[@content-desc[contains('
                             '., "The password for the current user is about to expire")]]')

    ALERT_MSG_WILL_EXPIRE_ios = (MobileBy.XPATH, '//UIAStaticText[@name'
                                           '[contains(., "The password for the current user is about to expire")]]')

    # alert message with word "inactive"
    ALERT_MSG_SUSPENDED = (MobileBy.XPATH,
                           './/android.view.View[@content-desc[contains(., "Your account is currently inactive")]]')
    ALERT_MSG_SUSPENDED_ios = (MobileBy.XPATH, '//UIAWebView[1]/'
                                         'UIAStaticText[@name[contains(., "Your account is currently inactive")]]')

# DO ZASTĄPIENIA PRZEZ OK_BUTTON
    # alert message about expiring password
    NOTICE_ALERT_OK_BUTTON = (MobileBy.XPATH,
                              './/android.view.View[@index="24"]//android.view.View[@content-desc[contains(., "Ok")]]')

    # OK button on alert messages"
    OK_BUTTON = (MobileBy.XPATH, './/android.view.View[@content-desc="Ok"]')
    OK_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name="Ok"]')


class MainMenuScreen(object):
    """A class for main menu screen locators - first screen after correct login into the app."""
    BUTTONS = (MobileBy.CLASS_NAME, 'android.view.View')
    LOGOUT_BUTTON = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "LOGOUT")]]')
    LOGOUT_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "LOGOUT")]]')
    EVENTS_BUTTON = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "EVENTS")]]')
    EVENTS_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "EVENTS")]]')


class EventsScreen(object):
    """A class for Events screen locators - screen after clicking into Events button in Main Menu."""
    EVENTS_HEADER = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "Events")]]')
    EVENTS_HEADER_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name="Events"]')

    # filtering events by Type
    ANY_TYPE_EXPAND = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "Any Type click to expand")]]')
    ANY_TYPE_EXPAND_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "Any Type click to expand")]]')
    CHOOSE_TYPE_INCIDENT = (MobileBy.XPATH, './/android.view.View[@content-desc="Incident"]')
    CHOOSE_TYPE_INCIDENT_ios = (MobileBy.XPATH, '//UIAStaticText[@name="Incident"]')
    INCIDENT_TYPE_EXPAND = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "Incident click to expand")]]')
    INCIDENT_TYPE_EXPAND_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Incident click to expand")]]')
    CHOOSE_TYPE_ANY = (MobileBy.XPATH, './/android.view.View[@content-desc="Any Type"]')
    CHOOSE_TYPE_ANY_ios = (MobileBy.XPATH, '//UIAStaticText[@name="Any Type"]')

    # filtering events by Status
    ANY_STATUS_EXPAND = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "Any Status click to expand")]]')
    ANY_STATUS_EXPAND_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Any Status click to expand")]]')
    CHOOSE_ACTIVE_STATUS = (MobileBy.XPATH, './/android.view.View[@content-desc="Active"]')
    CHOOSE_ACTIVE_STATUS_ios = (MobileBy.XPATH, '//UIALink[@name="Active"]')
    ACTIVE_STATUS_EXPAND = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "Active click to expand")]]')
    ACTIVE_STATUS_EXPAND_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Active click to expand")]]')
    CHOOSE_INACTIVE_STATUS = (MobileBy.XPATH, './/android.view.View[@content-desc="Inactive"]')
    CHOOSE_INACTIVE_STATUS_ios = (MobileBy.XPATH, '//UIALink[@name="Inactive"]')
    INACTIVE_STATUS_EXPAND = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "Inactive click to expand")]]')
    INACTIVE_STATUS_EXPAND_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Inactive click to expand")]]')
    CHOOSE_DRAFT_STATUS = (MobileBy.XPATH, './/android.view.View[@content-desc="Draft"]')
    CHOOSE_DRAFT_STATUS_ios = (MobileBy.XPATH, '//UIALink[@name="Draft"]')
    DRAFT_STATUS_EXPAND = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "Draft click to expand")]]')
    DRAFT_STATUS_EXPAND_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Draft click to expand")]]')
    CHOOSE_ANY_STATUS = (MobileBy.XPATH, './/android.view.View[@content-desc="Any Status"]')
    CHOOSE_ANY_STATUS_ios = (MobileBy.XPATH, '//UIALink[@name="Any Status"]')

    # filtering events using search field
    SEARCH_FIELD = (MobileBy.XPATH, './/android.widget.EditText[@index="3"]')
    SEARCH_FIELD_ios = (MobileBy.XPATH, '//UIATextField[@name="Search:"]')
    EVENTS_HEADER_AFTER_SEARCH = (MobileBy.XPATH, './/android.view.View[@index="5"]')

    # creating and editing Events
    MORE_BUTTON = (MobileBy.XPATH, './/android.widget.Spinner[@content-desc[contains(., "More")]]')
    MORE_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name[contains(., "More")]]')
    NEW_EVENT_BUTTON = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "New event")]]')
    NEW_EVENT_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "New event")]]')

    # previously created event
    CREATED_EVENT_1 = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "Test")]]')
    CREATED_EVENT_1_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Test Appium iOS")]]')
    CREATED_EVENT_2 = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "Test Appium - second event")]]')
    CREATED_EVENT_2_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Test Appium iOS - second event")]]')
    CREATED_EVENT_3 = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "Test to create sub event")]]')
    CREATED_EVENT_3_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "iOS to create sub")]]')
    CLEAR_PRIMARY_EVENT_BUTTON = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "Clear primary event")]]')
    CLEAR_PRIMARY_EVENT_BUTTON_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name'
                                                '[contains(., "Clear primary event")]]')
    NOTIFICATION_PRIMARY_EVENT_CLEARED = (MobileBy.XPATH, './/android.view.View[@content-desc="Primary event cleared"]')
    NOTIFICATION_PRIMARY_EVENT_CLEARED_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name="Primary event cleared"]')
    GO_BACK_TO_MAIN_MENU_ARROW_BUTTON = (MobileBy.XPATH, ".//android.webkit.WebView[@index='0']"
                                                   "//android.view.View[@index='0']"
                                                   "//android.view.View[@index='0']")
    GO_BACK_TO_MAIN_MENU_ARROW_BUTTON_ios = (MobileBy.XPATH, '//UIAApplication[1]'
                                                       '/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[1]')
    HAMBURGER_FOR_MAIN_MENU_ios = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]'
                                             '/UIAWebView[1]/UIALink[3]/UIAStaticText[1]')


class TypesOfEventsScreen(object):
    """A class for Type of Events screen locators - first screen after creating new event with types of events."""
    INCIDENT_TYPE_OF_EVENT = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "Incident")]]')
    INCIDENT_TYPE_OF_EVENT_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "Incident")]]')
    EVENT_FOR_ON_LOAD_SAVE = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "event_for_on_load")]]')
    EVENT_FOR_ON_LOAD_SAVE_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "event_for_on_load")]]')
    EVENT_FOR_CHOOSER_FIELDS = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "event_for_chooser")]]')
    EVENT_FOR_CHOOSER_FIELDS_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "event_for_chooser")]]')


class EventEditScreen(object):
    """A class for Edit Events screen locators - screen after opening edit mode of event or creating a new one."""
    NAME_FIELD = (MobileBy.XPATH, './/android.widget.EditText[@index="1"]')
    NAME_FIELD_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIATextField[@name="Name"]')
    SEVERITY_LEVEL_SELECTOR = (MobileBy.XPATH, './/android.widget.ListView[@index="0"]'
                                         '//android.view.View[@index="3"]'
                                         '//android.widget.Spinner[@index="2"]')
    SEVERITY_LEVEL_SELECTOR_ios = (MobileBy.XPATH, '//UIAElement[2]')
    CHOOSE_SEVERITY_LVL1 = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Severity 1"]')
    CHOOSE_SEVERITY_LVL1_iPad = (MobileBy.XPATH, '//UIATableCell[@name="Severity 1"]')
    CHOOSE_SEVERITY_LVL1_iPhone = (MobileBy.XPATH, '//UIAPicker/UIAPickerWheel[@value="Severity 1"]')
    CHOOSE_SEVERITY_LVL2 = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Severity 2"]')
    CHOOSE_SEVERITY_LVL2_iPad = (MobileBy.XPATH, '//UIATableCell[@name="Severity 2"]')
    CHOOSE_SEVERITY_LVL2_iPhone = (MobileBy.XPATH, '//UIAPicker/UIAPickerWheel[@value="Severity 2"]')
    CHOOSE_SEVERITY_LVL3 = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Severity 3"]')
    CHOOSE_SEVERITY_LVL3_iPad = (MobileBy.XPATH, '//UIATableCell[@name="Severity 3"]')
    CHOOSE_SEVERITY_LVL3_iPhone = (MobileBy.XPATH, '//UIAPicker/UIAPickerWheel[@value="Severity 3"]')
    CHOOSE_SEVERITY_LVL4 = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Severity 4"]')
    CHOOSE_SEVERITY_LVL4_iPad = (MobileBy.XPATH, '//UIATableCell[@name="Severity 4"]')
    CHOOSE_SEVERITY_LVL4_iPhone = (MobileBy.XPATH, '//UIAPicker/UIAPickerWheel[@value="Severity 4"]')
    SEVERITY_PICKER_ios = (MobileBy.XPATH, '//UIAApplication/UIAWindow/UIAPicker/UIAPickerWheel')
    FINISHED_FIELD = (MobileBy.XPATH, './/android.view.View[@content-desc="Finished"]')
    FINISHED_FIELD_ios = (MobileBy.XPATH, '//UIAStaticText[@name="Finished"]')
    TIME_DATE = (MobileBy.XPATH, './/android.widget.ImageButton[@content-desc="Increase year"]')
    SET_BUTTON = (MobileBy.ID, 'android:id/button1')
    SAVE_BUTTON = (MobileBy.XPATH, './/android.widget.Button[@content-desc="Save"]')
    SAVE_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name="Save"]')
    DESCRIPTION_FIELD = (MobileBy.XPATH,
                         ".//android.widget.ListView[@index='0']"
                         "//android.view.View[@index='8' and @content-desc[contains(., 'Description')]]"
                         "//android.view.View[@index='1']"
                         "//android.view.View[@index='1']"
                         "//android.view.View[@index='0']"
                         "//android.view.View[@index='0']"
                         "//android.view.View[@index='0' and @clickable='true']")
    DESCRIPTION_FIELD_ios = (MobileBy.XPATH, '//UIATextField[3]')

    # headers for scrolling
    FINISHED_HEADER = (MobileBy.XPATH, './/android.view.View[@content-desc="Finished"]')
    LEADAGENCY_HEADER = (MobileBy.XPATH, './/android.view.View[@content-desc="Lead agency"]')
    IMPACT_HEADER = (MobileBy.XPATH, './/android.view.View[@content-desc="Impact"]')
    CAUSE_HEADER = (MobileBy.XPATH, './/android.view.View[@content-desc="Cause"]')
    SITUATION_HEADER = (MobileBy.XPATH, './/android.view.View[@content-desc="Situation"]')
    ISSUES_HEADER = (MobileBy.XPATH, './/android.view.View[@content-desc="Issues"]')
    OBJECTIVES_HEADER = (MobileBy.XPATH, './/android.view.View[@content-desc="Objectives"]')
    STRATEGIES_HEADER = (MobileBy.XPATH, './/android.view.View[@content-desc="Strategies"]')
    TACTICS_HEADER = (MobileBy.XPATH, './/android.view.View[@content-desc="Tactics"]')
    COMMUNICATIONS_HEADER = (MobileBy.XPATH, './/android.view.View[@content-desc="Communications"]')
    RELATED_HEADER = (MobileBy.XPATH, './/android.view.View[@content-desc="Related"]')
    CREATE_MAPPING_DATA = (MobileBy.XPATH, ".//android.view.View[@content-desc[contains(., 'Create mapping data')]]")
    CREATE_MAPPING_DATA_ios = (MobileBy.XPATH, "//UIALink[@name[contains(., 'Create mapping data')]]")
    EDIT_MAPPING_DATA = (MobileBy.XPATH, ".//android.view.View[@content-desc[contains(., 'Edit mapping data')]]")
    EDIT_MAPPING_DATA_ios = (MobileBy.XPATH, "//UIALink[@name[contains(., 'Create mapping data')]]")
    ELEMENT_TO_SCROLL_ios = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAImage[1]')
    SEQUENCE_ONLOAD_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="sequence_onload"]')
    SEQUENCE_ONLOAD_HEADER_ios = (MobileBy.XPATH, '//UIAStaticText[@name="sequence_onload"]')
    SEQUENCE_ONLOAD_VALUE = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="test on load"]')
    SEQUENCE_ONLOAD_VALUE_ios = (MobileBy.XPATH, '//UIATextField[@value="test on load"]')
    SEQUENCE_ONSAVE_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="sequence_onsave"]')
    SEQUENCE_ONSAVE_HEADER_ios = (MobileBy.XPATH, '//UIAStaticText[@name="sequence_onsave"]')
    SEQUENCE_ONSAVE_VALUE = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="(auto)"]')
    SEQUENCE_ONSAVE_VALUE_ios = (MobileBy.XPATH, '//UIATextField[@value="(auto)"]')
    NEW_OPTION_LIST_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="New option list"]')
    NEW_OPTION_LIST_HEADER_ios = (MobileBy.XPATH, '//UIAStaticText[@name="New option list"]')
    OPTION_LIST_VALUE_1 = (MobileBy.XPATH, '//android.view.View[@content-desc="1"]')
    OPTION_LIST_VALUE_2 = (MobileBy.XPATH, '//android.view.View[@content-desc="2"]')
    OPTION_LIST_VALUE_3 = (MobileBy.XPATH, '//android.view.View[@content-desc="3"]')
    OPTION_LIST_VALUE_1_ios = (MobileBy.XPATH, '//UIAStaticText[@name="1"]')
    OPTION_LIST_VALUE_2_ios = (MobileBy.XPATH, '//UIAStaticText[@name="2"]')
    OPTION_LIST_VALUE_3_ios = (MobileBy.XPATH, '//UIAStaticText[@name="3"]')
    FIELD_TO_RESTORE_1_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="field to restore"]')
    FIELD_TO_RESTORE_1_HEADER_ios = (MobileBy.XPATH, '//UIAStaticText[@name="field to restore"]')
    FIELD_TO_RESTORE_1_VALUE = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="value for field 1"]')
    FIELD_TO_RESTORE_1_VALUE_ios = (MobileBy.XPATH, '//UIATextField[@value="value for field 1"]')
    FIELD_TO_RESTORE__2_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="New email address"]')
    FIELD_TO_RESTORE__2_HEADER_ios = (MobileBy.XPATH, '//UIAStaticText[@name="New email address"]')
    FIELD_TO_RESTORE_2_VALUE = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="test@noggin.com"]')
    FIELD_TO_RESTORE_2_VALUE_ios = (MobileBy.XPATH, '//UIATextField[@value="test@noggin.com"]')
    CANCEL_BUTTON = (MobileBy.XPATH, '//android.widget.Button[@content-desc="Cancel"]')
    CANCEL_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name="Cancel"]')
    CHOOSER_FIELD = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "New events chooser")]]')
    CHOOSER_FIELD_ios = (MobileBy.XPATH, '//UIAWebView/UIALink/UIALink[@name[contains(., "New events chooser")]]')
    PREVIOUSLY_CREATED_EVENT_FOR_CHOOSER = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Test")]]')
    PREVIOUSLY_CREATED_EVENT_FOR_CHOOSER_ios = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Test Appium iOS")]]')
    SUBFORM_FIELD_ADD_ROW = (MobileBy.XPATH, '//android.widget.Button[@content-desc="Add row"]')
    SUBFORM_FIELD_ADD_ROW_ios = (MobileBy.XPATH, '//UIAButton[@name="Add row"]')
    NEW_EVENTS_CHOOSER_IN_SUB_FORM = (MobileBy.XPATH, '//android.view.View'
                                                '[@content-desc[contains(., "New events chooser inside sub form")]]')
    NEW_EVENTS_CHOOSER_IN_SUB_FORM_ios = (MobileBy.XPATH, '//UIAWebView/UIALink/UIALink'
                                                    '[@name[contains(., "New events chooser inside sub form")]]')
    PREVIOUSLY_CREATED_EVENT_FOR_SUBFORM_CHOOSER_ios = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Test")]]')
    #DELETE_SUB_EVENT_FROM_CHOOSER = (MobileBy.XPATH, '//android.widget.ListView[0]/android.view.View[8]/android.view.View[1]')
    DELETE_SUB_EVENT_FROM_CHOOSER = (MobileBy.XPATH, '//android.widget.ListView/android.view.View[@index="8"]/android.view.View[@index="1"]')
    #DELETE_SUB_EVENT_FROM_CHOOSER_ios = (MobileBy.XPATH, '//UIAScrollView[2]/UIAWebView[1]/UIALink[6]')


class EventDetailsScreen(object):
    """A class for Event Details screen locators - screen with event details - after opening event."""
    EDIT_BUTTON = (MobileBy.XPATH, './/android.widget.Button[@content-desc="Edit"]')
    EDIT_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name="Edit"]')
    DELETE_EVENT_BUTTON = (MobileBy.XPATH, "//android.widget.ListView[@index='2']"
                                     "//android.view.View[@index='2']"
                                     "//android.view.View[@content-desc[contains(., 'Delete event')]]")
    DELETE_EVENT_BUTTON_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "Delete event")]]')
    DELETE_CONFIRM_BUTTON = (MobileBy.XPATH, './/android.view.View[@content-desc="Delete"]')
    DELETE_CONFIRM_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name="Delete"]')
    NEW_SUB_EVENT = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "New sub event")]]')
    NEW_SUB_EVENT_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "New sub event")]]')
    SET_AS_PRIMARY_BUTTON = (MobileBy.XPATH, './/android.view.View[@content-desc[contains(., "Set as primary")]]')
    SET_AS_PRIMARY_BUTTON_ios = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Set as primary")]]')


class Map(object):
    TOOL_BUTTON = (MobileBy.XPATH, ".//android.widget.Spinner[@content-desc[contains(., 'Tool')]]")
    TOOL_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Tool")]]')
    POINT_BUTTON = (MobileBy.XPATH, ".//android.view.View[@content-desc[contains(., 'Point click to expand')]]")
    POINT_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Point click to expand")]]')
    DEFAULT_BUTTON = (MobileBy.XPATH, ".//android.view.View[@content-desc='Default']")
    DEFAULT_BUTTON_ios = (MobileBy.XPATH, '//UIAStaticText[@name="Default"]')
    ADD_POINT_INTO_MAP = (MobileBy.XPATH, ".//android.widget.Image[@index='6']")
    ADD_POINT_INTO_MAP_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAImage[13]')
    #ADD_POINT_INTO_MAP_ios = (MobileBy.XPATH, '/UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAImage[13]')
    LINE_BUTTON = (MobileBy.XPATH, ".//android.view.View[@content-desc[contains(., 'Line click to expand')]]")
    LINE_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Line click to expand")]]')
    ADD_LINE1 = (MobileBy.XPATH, ".//android.widget.Image[@index='5']")
    ADD_LINE1_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAImage[12]')
    ADD_LINE2 = (MobileBy.XPATH, ".//android.widget.Image[@index='3']")
    ADD_LINE2_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAImage[17]')
    CIRCLE_BUTTON = (MobileBy.XPATH, ".//android.view.View[@content-desc[contains(., 'Circle click to expand')]]")
    CIRCLE_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Circle click to expand")]]')
    ADD_CIRCLE_INTO_MAP = (MobileBy.XPATH, ".//android.widget.Image[@index='6']")
    ADD_CIRCLE_INTO_MAP_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAImage[12]')
    POLYGON_BUTTON = (MobileBy.XPATH, ".//android.view.View[@content-desc[contains(., 'Polygon click to expand')]]")
    POLYGON_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Polygon click to expand")]]')
    ADD_POLYGON1 = (MobileBy.XPATH, ".//android.widget.Image[@index='5']")
    ADD_POLYGON1_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAImage[12]')
    ADD_POLYGON2 = (MobileBy.XPATH, ".//android.widget.Image[@index='6']")
    ADD_POLYGON2_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAImage[17]')
    ADD_POLYGON3 = (MobileBy.XPATH, ".//android.widget.Image[@index='3']")
    ADD_POLYGON3_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAImage[18]')
    SAVE_MAP_BUTTON = (MobileBy.XPATH, ".//android.widget.Button[@content-desc='Save']")
    SAVE_MAP_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Save")]]')
    BUTTON_ALLOW_LOCATION_ios = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[7]/UIAAlert[1]/UIACollectionView[1]'
                                           '/UIACollectionCell[2]/UIAButton[@name="Allow"]')


class iOSkeyboard(object):
    """A class for handling iOS keyboard"""

    BUTTON_DONE_TO_HIDE_KEYBOARD = (MobileBy.XPATH, '//UIAWindow[2]/UIAToolbar[1]/UIAButton[@name="Done"]')
    RETURN_BUTTON = (MobileBy.XPATH, '//UIAButton[@name="Return"]')


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass
