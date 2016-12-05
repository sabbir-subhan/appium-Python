from selenium.webdriver.common.by import By


class WelcomeScreen(object):
    """A class for welcome screen locators - first screen after lunching the app."""
    LOGIN_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "LOGIN")]]')
    LOGIN_BUTTON_ios = (By.XPATH, '//UIALink[@name[contains(., "LOGIN")]]')


class LoginScreen(object):
    """A class for login screen locators - screen after clicking into LOGIN."""
    TEXTFIELD_USERNAME = (By.XPATH, './/android.widget.EditText[@index="1"]')
    TEXTFIELD_USERNAME_ios = (By.XPATH, '//UIAWebView[1]/UIATextField[1]')
    TEXTFIELD_PASSWORD = (By.XPATH, './/android.widget.EditText[@index="3"]')
    TEXTFIELD_PASSWORD_ios = (By.XPATH, '//UIAWebView[1]/UIASecureTextField[1]')
    TEXTFIELD_DOMAIN = (By.XPATH, './/android.widget.EditText[@index="5"]')
    TEXTFIELD_DOMAIN_ios = (By.XPATH, '//UIAWebView[1]/UIATextField[2]')
    SUBMIT_BUTTON = (By.XPATH, '//android.widget.Button[@content-desc="Submit"]')
    SUBMIT_BUTTON_ios = (By.XPATH, '//UIAWebView[1]/UIAButton[@name="Submit"]')

    # Notification alert: "OCA now supports sending 'App Messages' to your device as notifications."
    NOTIFICATION_ABOUT_SENDING_MESSAGES_ios = (By.XPATH, '//UIAWebView[1]/UIAStaticText[@name[contains(., '
                                                         '"OCA now supports ")]]')

    # "No" button for sending notifications on iOS
    NO_FOR_SENDING_NOTIFICATIONS_ON_ios = (By.XPATH, '//UIAWebView[1]/UIALink[@name="No"]')

    # ACCEPT_BUTTON on Terms and Conditions"
    ACCEPT_BUTTON = (By.XPATH, './/android.widget.Button[@content-desc="Accept"]')
    ACCEPT_BUTTON_ios = (By.XPATH, '//UIAWebView[1]/UIAButton[@name="Accept"]')

    # alert message with word "Invalid"
    ALERT_MSG_INVALID = (By.XPATH, './/android.view.View[@content-desc[contains(., "Invalid")]]')
    ALERT_MSG_INVALID_ios = (By.XPATH, '//UIAWebView[1]/UIAStaticText[@name="Invalid username and/or password"]')

    # alert message with "Your temporary account has been expired"
    ALERT_MSG_EXPIRED = (By.XPATH, './/android.view.View[@content-desc[contains('
                                   '., "Your temporary account has been expired")]]')

    ALERT_MSG_EXPIRED_ios = (By.XPATH, '//UIAWebView[1]/UIAStaticText[@name[contains'
                                       '(., "Your temporary account has been expired")]]')

    # alert message with "The password for the current user is about to expire"
    ALERT_MSG_WILL_EXPIRE = (By.XPATH,
                             './/android.view.View[@content-desc[contains('
                             '., "The password for the current user is about to expire")]]')
                # TO DO
    ALERT_MSG_WILL_EXPIRE_ios = (By.XPATH, '')

    # alert message with word "inactive"
    ALERT_MSG_SUSPENDED = (By.XPATH,
                           './/android.view.View[@content-desc[contains(., "Your account is currently inactive")]]')
    ALERT_MSG_SUSPENDED_ios = (By.XPATH, '//UIAWebView[1]/'
                                         'UIAStaticText[@name[contains(., "Your account is currently inactive")]]')

    # alert message about expiring password
    NOTICE_ALERT_OK_BUTTON = (By.XPATH,
                              './/android.view.View[@index="24"]//android.view.View[@content-desc[contains(., "Ok")]]')
    # the same as OK_BUTTON ??
    #NOTICE_ALERT_OK_BUTTON_ios = (By.XPATH, '')

    # OK button on alert messages"
    OK_BUTTON = (By.XPATH, './/android.view.View[@content-desc="Ok"]')
    #OK_BUTTON_ios = (By.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[4]')
    OK_BUTTON_ios = (By.XPATH, '//UIAWebView[1]/UIALink[@name="Ok"]')


class MainMenuScreen(object):
    """A class for main menu screen locators - first screen after correct login into the app."""
    BUTTONS = (By.CLASS_NAME, 'android.view.View')
    LOGOUT_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "LOGOUT")]]')
    LOGOUT_BUTTON_ios = (By.XPATH, '//UIALink[@name[contains(., "LOGOUT")]]')
    EVENTS_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "EVENTS")]]')
    EVENTS_BUTTON_ios = (By.XPATH, '//UIALink[@name[contains(., "EVENTS")]]')


class EventsScreen(object):
    """A class for Events screen locators - screen after clicking into Events button in Main Menu."""
    EVENTS_HEADER = (By.XPATH, './/android.view.View[@content-desc[contains(., "Events")]]')
    EVENTS_HEADER_ios = (By.XPATH, '//UIAWebView[1]/UIAStaticText[@name="Events"]')

    # filtering events by Type
    ANY_TYPE_EXPAND = (By.XPATH, './/android.view.View[@content-desc[contains(., "Any Type click to expand")]]')
    ANY_TYPE_EXPAND_ios = (By.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "Any Type click to expand")]]')
    CHOOSE_TYPE_INCIDENT = (By.XPATH, './/android.view.View[@content-desc="Incident"]')
    CHOOSE_TYPE_INCIDENT_ios = (By.XPATH, '//UIAStaticText[@name="Incident"]')
    INCIDENT_TYPE_EXPAND = (By.XPATH, './/android.view.View[@content-desc[contains(., "Incident click to expand")]]')
    INCIDENT_TYPE_EXPAND_ios = (By.XPATH, '//UIALink[@name[contains(., "Incident click to expand")]]')
    CHOOSE_TYPE_ANY = (By.XPATH, './/android.view.View[@content-desc="Any Type"]')
    CHOOSE_TYPE_ANY_ios = (By.XPATH, '//UIAStaticText[@name="Any Type"]')

    # filtering events by Status
    ANY_STATUS_EXPAND = (By.XPATH, './/android.view.View[@content-desc[contains(., "Any Status click to expand")]]')
    ANY_STATUS_EXPAND_ios = (By.XPATH, '//UIALink[@name[contains(., "Any Status click to expand")]]')
    CHOOSE_ACTIVE_STATUS = (By.XPATH, './/android.view.View[@content-desc="Active"]')
    CHOOSE_ACTIVE_STATUS_ios = (By.XPATH, '//UIALink[@name="Active"]')
    ACTIVE_STATUS_EXPAND = (By.XPATH, './/android.view.View[@content-desc[contains(., "Active click to expand")]]')
    ACTIVE_STATUS_EXPAND_ios = (By.XPATH, '//UIALink[@name[contains(., "Active click to expand")]]')
    CHOOSE_INACTIVE_STATUS = (By.XPATH, './/android.view.View[@content-desc="Inactive"]')
    CHOOSE_INACTIVE_STATUS_ios = (By.XPATH, '//UIALink[@name="Inactive"]')
    INACTIVE_STATUS_EXPAND = (By.XPATH, './/android.view.View[@content-desc[contains(., "Inactive click to expand")]]')
    INACTIVE_STATUS_EXPAND_ios = (By.XPATH, '//UIALink[@name[contains(., "Inactive click to expand")]]')
    CHOOSE_DRAFT_STATUS = (By.XPATH, './/android.view.View[@content-desc="Draft"]')
    CHOOSE_DRAFT_STATUS_ios = (By.XPATH, '//UIALink[@name="Draft"]')
    DRAFT_STATUS_EXPAND = (By.XPATH, './/android.view.View[@content-desc[contains(., "Draft click to expand")]]')
    DRAFT_STATUS_EXPAND_ios = (By.XPATH, '//UIALink[@name[contains(., "Draft click to expand")]]')
    CHOOSE_ANY_STATUS = (By.XPATH, './/android.view.View[@content-desc="Any Status"]')
    CHOOSE_ANY_STATUS_ios = (By.XPATH, '//UIALink[@name="Any Status"]')

    # filtering events using search field
    SEARCH_FIELD = (By.XPATH, './/android.widget.EditText[@index="3"]')
    SEARCH_FIELD_ios = (By.XPATH, '//UIATextField[@name="Search:"]')
    EVENTS_HEADER_AFTER_SEARCH = (By.XPATH, './/android.view.View[@index="5"]')

    # creating and editing Events
    MORE_BUTTON = (By.XPATH, './/android.widget.Spinner[@content-desc[contains(., "More")]]')
    MORE_BUTTON_ios = (By.XPATH, '//UIAButton[@name[contains(., "More")]]')
    NEW_EVENT_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "New event")]]')
    NEW_EVENT_BUTTON_ios = (By.XPATH, '//UIALink[@name[contains(., "New event")]]')

    # previously created event
    CREATED_EVENT_1 = (By.XPATH, './/android.view.View[@content-desc[contains(., "Test")]]')
    CREATED_EVENT_1_ios = (By.XPATH, '//UIALink[@name[contains(., "Test Appium iOS")]]')
    CREATED_EVENT_2 = (By.XPATH, './/android.view.View[@content-desc[contains(., "Test Appium - second event")]]')
    CREATED_EVENT_2_ios = (By.XPATH, '//UIALink[@name[contains(., "Test Appium iOS - second event")]]')
    CREATED_EVENT_3 = (By.XPATH, './/android.view.View[@content-desc[contains(., "Test to create sub event")]]')
    CREATED_EVENT_3_ios = (By.XPATH, '//UIALink[@name[contains(., "iOS to create sub")]]')
    CLEAR_PRIMARY_EVENT_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "Clear primary event")]]')
    CLEAR_PRIMARY_EVENT_BUTTON_ios = (By.XPATH, '//UIAWebView[1]/UIAStaticText[@name'
                                                '[contains(., "Clear primary event")]]')
    NOTIFICATION_PRIMARY_EVENT_CLEARED = (By.XPATH, './/android.view.View[@content-desc="Primary event cleared"]')
    NOTIFICATION_PRIMARY_EVENT_CLEARED_ios = (By.XPATH, '//UIAWebView[1]/UIAStaticText[@name="Primary event cleared"]')
    GO_BACK_TO_MAIN_MENU_ARROW_BUTTON = (By.XPATH, ".//android.webkit.WebView[@index='0']"
                                                   "//android.view.View[@index='0']"
                                                   "//android.view.View[@index='0']")
    GO_BACK_TO_MAIN_MENU_ARROW_BUTTON_ios = (By.XPATH, '//UIAApplication[1]'
                                                       '/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[1]')
    HAMBURGER_FOR_MAIN_MENU_ios = (By.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]'
                                             '/UIAWebView[1]/UIALink[3]/UIAStaticText[1]')


class TypesOfEventsScreen(object):
    """A class for Type of Events screen locators - first screen after creating new event with types of events."""
    INCIDENT_TYPE_OF_EVENT = (By.XPATH, './/android.view.View[@content-desc[contains(., "Incident")]]')
    INCIDENT_TYPE_OF_EVENT_ios = (By.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "Incident")]]')
    EVENT_FOR_ON_LOAD_SAVE_ios = (By.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "event_for_on_load")]]')
    EVENT_FOR_CHOOSER_FIELDS_ios = (By.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "event_for_chooser")]]')


class EventEditScreen(object):
    """A class for Edit Events screen locators - screen after opening edit mode of event or creating a new one."""
    NAME_FIELD = (By.XPATH, './/android.widget.EditText[@index="1"]')
    NAME_FIELD_ios = (By.XPATH, '//UIAWebView[1]/UIATextField[@name="Name"]')
    SEVERITY_LEVEL_SELECTOR = (By.XPATH, './/android.widget.ListView[@index="0"]'
                                         '//android.view.View[@index="3"]'
                                         '//android.widget.Spinner[@index="2"]')
    SEVERITY_LEVEL_SELECTOR_ios = (By.XPATH, '//UIAElement[2]')
    #CHOOSE_SEVERITY_LVL1 = (By.NAME, 'Severity 1')
    CHOOSE_SEVERITY_LVL1 = (By.XPATH, '//android.widget.CheckedTextView[@text="Severity 1"]')
    CHOOSE_SEVERITY_LVL1_ios = (By.XPATH, '//UIATableCell[@name="Severity 1"]')
    #CHOOSE_SEVERITY_LVL2 = (By.NAME, 'Severity 2')
    CHOOSE_SEVERITY_LVL2 = (By.XPATH, '//android.widget.CheckedTextView[@text="Severity 2"]')
    CHOOSE_SEVERITY_LVL2_ios = (By.XPATH, '//UIATableCell[@name="Severity 2"]')
    #CHOOSE_SEVERITY_LVL3 = (By.NAME, 'Severity 3')
    CHOOSE_SEVERITY_LVL3 = (By.XPATH, '//android.widget.CheckedTextView[@text="Severity 3"]')
    CHOOSE_SEVERITY_LVL3_ios = (By.XPATH, '//UIATableCell[@name="Severity 3"]')
    #CHOOSE_SEVERITY_LVL4 = (By.NAME, 'Severity 4')
    CHOOSE_SEVERITY_LVL4 = (By.XPATH, '//android.widget.CheckedTextView[@text="Severity 4"]')
    CHOOSE_SEVERITY_LVL4_ios = (By.XPATH, '//UIATableCell[@name="Severity 4"]')
    FINISHED_FIELD = (By.XPATH, './/android.view.View[@content-desc="Finished"]')
    FINISHED_FIELD_ios = (By.XPATH, '//UIAStaticText[@name="Finished"]')
    TIME_DATE = (By.XPATH, './/android.widget.ImageButton[@content-desc="Increase year"]')
    SET_BUTTON = (By.ID, 'android:id/button1')
    SAVE_BUTTON = (By.XPATH, './/android.widget.Button[@content-desc="Save"]')
    SAVE_BUTTON_ios = (By.XPATH, '//UIAButton[@name="Save"]')
    DESCRIPTION_FIELD = (By.XPATH,
                         ".//android.widget.ListView[@index='0']"
                         "//android.view.View[@index='8' and @content-desc[contains(., 'Description')]]"
                         "//android.view.View[@index='1']"
                         "//android.view.View[@index='1']"
                         "//android.view.View[@index='0']"
                         "//android.view.View[@index='0']"
                         "//android.view.View[@index='0' and @clickable='true']")
    DESCRIPTION_FIELD_ios = (By.XPATH, '//UIATextField[3]')

    # headers for scrolling
    FINISHED_HEADER = (By.XPATH, './/android.view.View[@content-desc="Finished"]')
    LEADAGENCY_HEADER = (By.XPATH, './/android.view.View[@content-desc="Lead agency"]')
    IMPACT_HEADER = (By.XPATH, './/android.view.View[@content-desc="Impact"]')
    CAUSE_HEADER = (By.XPATH, './/android.view.View[@content-desc="Cause"]')
    SITUATION_HEADER = (By.XPATH, './/android.view.View[@content-desc="Situation"]')
    ISSUES_HEADER = (By.XPATH, './/android.view.View[@content-desc="Issues"]')
    OBJECTIVES_HEADER = (By.XPATH, './/android.view.View[@content-desc="Objectives"]')
    STRATEGIES_HEADER = (By.XPATH, './/android.view.View[@content-desc="Strategies"]')
    TACTICS_HEADER = (By.XPATH, './/android.view.View[@content-desc="Tactics"]')
    COMMUNICATIONS_HEADER = (By.XPATH, './/android.view.View[@content-desc="Communications"]')
    RELATED_HEADER = (By.XPATH, './/android.view.View[@content-desc="Related"]')
    CREATE_MAPPING_DATA = (By.XPATH, ".//android.view.View[@content-desc[contains(., 'Create mapping data')]]")
    CREATE_MAPPING_DATA_ios = (By.XPATH, "//UIALink[@name[contains(., 'Create mapping data')]]")
    EDIT_MAPPING_DATA = (By.XPATH, ".//android.view.View[@content-desc[contains(., 'Edit mapping data')]]")
    EDIT_MAPPING_DATA_ios = (By.XPATH, "//UIALink[@name[contains(., 'Create mapping data')]]")
    ELEMENT_TO_SCROLL_ios = (By.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAImage[1]')
    SEQUENCE_ONLOAD_HEADER_ios = (By.XPATH, '//UIAStaticText[@name="sequence_onload"]')
    SEQUENCE_ONLOAD_VALUE_ios = (By.XPATH, '//UIAStaticText[@value="test on load"]')
    SEQUENCE_ONSAVE_HEADER_ios = (By.XPATH, '//UIAStaticText[@name="sequence_onsave"]')
    SEQUENCE_ONSAVE_VALUE_ios = (By.XPATH, '//UIAStaticText[@value="(auto)"]')
    NEW_OPTION_LIST_HEADER_ios = (By.XPATH, '//UIAStaticText[@name="New option list"]')
    OPTION_LIST_VALUE_1_ios = (By.XPATH, '//UIAStaticText[@name="1"]')
    OPTION_LIST_VALUE_2_ios = (By.XPATH, '//UIAStaticText[@name="2"]')
    OPTION_LIST_VALUE_3_ios = (By.XPATH, '//UIAStaticText[@name="3"]')
    FIELD_TO_RESTORE_HEADER_ios = (By.XPATH, '//UIAStaticText[@name="field to restore"]')
    FIELD_TO_RESTORE_VALUE_ios = (By.XPATH, '//UIATextField[@value="value for field 1"]')
    FIELD_TO_RESTORE__2_HEADER_ios = (By.XPATH, '//UIAStaticText[@name="New email address"]')
    FIELD_TO_RESTORE_2_VALUE_ios = (By.XPATH, '//UIATextField[@value="lukaszbitnoise@gmail.com"]')
    CANCEL_BUTTON_ios = (By.XPATH, '//UIAButton[@name="Cancel"]')
    CHOOSER_FIELD_ios = (By.XPATH, '//UIAWebView/UIALink/UIALink[@name[contains(., "New events chooser")]]')
    # EVENT_INSIDE_CHOOSER_ios = (By.XPATH, '//UIAWebView/UIALink/UIALink[@name[contains(., "Test Appium iOS")]]')
    SUBFORM_FIELD_ADD_ROW_ios = (By.XPATH, '//UIAButton[@name="Add row"]')
    NEW_EVENTS_CHOOSER_IN_SUB_FORM = (By.XPATH, '//UIALink[@name[contains(., "New events chooser inside sub form")]]')
    # SUB_EVENT_INSIDE_CHOOSER_ios = (By.XPATH, '//UIAWebView/UIALink/UIALink[@name'
    #                                           '[contains(., "iOS to create sub event")]]')
    DELETE_SUB_EVENT_FROM_CHOOSER_ios = (By.XPATH, '//UIAScrollView[2]/UIAWebView[1]/UIALink[6]')


class EventDetailsScreen(object):
    """A class for Event Details screen locators - screen with event details - after opening event."""
    EDIT_BUTTON = (By.XPATH, './/android.widget.Button[@content-desc="Edit"]')
    EDIT_BUTTON_ios = (By.XPATH, '//UIAButton[@name="Edit"]')
    DELETE_EVENT_BUTTON = (By.XPATH, "//android.widget.ListView[@index='2']"
                                     "//android.view.View[@index='2']"
                                     "//android.view.View[@content-desc[contains(., 'Delete event')]]")
    DELETE_EVENT_BUTTON_ios = (By.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "Delete event")]]')
    DELETE_CONFIRM_BUTTON = (By.XPATH, './/android.view.View[@content-desc="Delete"]')
    DELETE_CONFIRM_BUTTON_ios = (By.XPATH, '//UIALink[@name="Delete"]')
    NEW_SUB_EVENT = (By.XPATH, './/android.view.View[@content-desc[contains(., "New sub event")]]')
    NEW_SUB_EVENT_ios = (By.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "New sub event")]]')
    SET_AS_PRIMARY_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "Set as primary")]]')
    SET_AS_PRIMARY_BUTTON_ios = (By.XPATH, '//UIAStaticText[@name[contains(., "Set as primary")]]')


class Map(object):
    TOOL_BUTTON = (By.XPATH, ".//android.widget.Spinner[@content-desc[contains(., 'Tool')]]")
    TOOL_BUTTON_ios = (By.XPATH, '//UIAButton[@name[contains(., "Tool")]]')
    POINT_BUTTON = (By.XPATH, ".//android.view.View[@content-desc[contains(., 'Point click to expand')]]")
    POINT_BUTTON_ios = (By.XPATH, '//UIALink[@name[contains(., "Point click to expand")]]')
    DEFAULT_BUTTON = (By.XPATH, ".//android.view.View[@content-desc='Default']")
    DEFAULT_BUTTON_ios = (By.XPATH, '//UIAStaticText[@name="Default"]')
    ADD_POINT_INTO_MAP = (By.XPATH, ".//android.widget.Image[@index='6']")
    ADD_POINT_INTO_MAP_ios = (By.XPATH, '//UIAWebView[1]/UIAImage[13]')
    #ADD_POINT_INTO_MAP_ios = (By.XPATH, '/UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAImage[13]')
    LINE_BUTTON = (By.XPATH, ".//android.view.View[@content-desc[contains(., 'Line click to expand')]]")
    LINE_BUTTON_ios = (By.XPATH, '//UIALink[@name[contains(., "Line click to expand")]]')
    ADD_LINE1 = (By.XPATH, ".//android.widget.Image[@index='5']")
    ADD_LINE1_ios = (By.XPATH, '//UIAWebView[1]/UIAImage[12]')
    ADD_LINE2 = (By.XPATH, ".//android.widget.Image[@index='3']")
    ADD_LINE2_ios = (By.XPATH, '//UIAWebView[1]/UIAImage[17]')
    CIRCLE_BUTTON = (By.XPATH, ".//android.view.View[@content-desc[contains(., 'Circle click to expand')]]")
    CIRCLE_BUTTON_ios = (By.XPATH, '//UIALink[@name[contains(., "Circle click to expand")]]')
    ADD_CIRCLE_INTO_MAP = (By.XPATH, ".//android.widget.Image[@index='6']")
    ADD_CIRCLE_INTO_MAP_ios = (By.XPATH, '//UIAWebView[1]/UIAImage[12]')
    POLYGON_BUTTON = (By.XPATH, ".//android.view.View[@content-desc[contains(., 'Polygon click to expand')]]")
    POLYGON_BUTTON_ios = (By.XPATH, '//UIALink[@name[contains(., "Polygon click to expand")]]')
    ADD_POLYGON1 = (By.XPATH, ".//android.widget.Image[@index='5']")
    ADD_POLYGON1_ios = (By.XPATH, '//UIAWebView[1]/UIAImage[12]')
    ADD_POLYGON2 = (By.XPATH, ".//android.widget.Image[@index='6']")
    ADD_POLYGON2_ios = (By.XPATH, '//UIAWebView[1]/UIAImage[17]')
    ADD_POLYGON3 = (By.XPATH, ".//android.widget.Image[@index='3']")
    ADD_POLYGON3_ios = (By.XPATH, '//UIAWebView[1]/UIAImage[18]')
    SAVE_MAP_BUTTON = (By.XPATH, ".//android.widget.Button[@content-desc='Save']")
    SAVE_MAP_BUTTON_ios = (By.XPATH, '//UIAButton[@name[contains(., "Save")]]')
    BUTTON_ALLOW_LOCATION_ios = (By.XPATH, '//UIAApplication[1]/UIAWindow[7]/UIAAlert[1]/UIACollectionView[1]'
                                           '/UIACollectionCell[2]/UIAButton[@name="Allow"]')


class iOSkeyboard(object):
    """A class for handling iOS keyboard"""

    BUTTON_DONE_TO_HIDE_KEYBOARD = (By.XPATH, '//UIAWindow[2]/UIAToolbar[1]/UIAButton[@name="Done"]')
    RETURN_BUTTON = (By.XPATH, '//UIAButton[@name="Return"]')


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass


