from selenium.webdriver.common.by import By


class WelcomeScreen(object):
    """A class for welcome screen locators - first screen after lunching the app."""
    LOGIN_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "LOGIN")]]')
    LOGIN_BUTTON_ios = (By.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]'
                                  '/UIALink[9][@name[contains(., "LOGIN")]]')


class LoginScreen(object):
    """A class for login screen locators - screen after clicking into LOGIN."""
    TEXTFIELD_USERNAME = (By.XPATH, './/android.widget.EditText[@index="1"]')
    TEXTFIELD_USERNAME_ios = (By.XPATH,
                              '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIATextField[1]')
    TEXTFIELD_PASSWORD = (By.XPATH, './/android.widget.EditText[@index="3"]')
    TEXTFIELD_PASSWORD_ios = (By.XPATH,
                              '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIASecureTextField[1]')
    TEXTFIELD_DOMAIN = (By.XPATH, './/android.widget.EditText[@index="5"]')
    TEXTFIELD_DOMAIN_ios = (By.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIATextField[2]')
    BUTTON_DONE_TO_HIDE_KEYBOARD_ios = (By.XPATH, '//UIAApplication[1]/UIAWindow[2]'
                                                  '/UIAToolbar[1]/UIAButton[3][@name="Done"]')
    SUBMIT_BUTTON = (By.XPATH, '//android.widget.Button[@content-desc="Submit"]')
    SUBMIT_BUTTON_ios = (By.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAButton[1]')

    # Notification alert: "OCA now supports sending 'App Messages' to your device as notifications."
    NOTIFICATION_ABOUT_SENDING_MESSAGES_ios = (By.NAME, "OCA now supports "
                                                        "sending 'App Messages' to your device as notifications.")

    # "No" button for sending notifications on iOS
    NO_FOR_SENDING_NOTIFICATIONS_ON_ios = (By.XPATH, '//UIAApplication[1]'
                                                     '/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[4]')

    # ACCEPT_BUTTON on Terms and Conditions"
    ACCEPT_BUTTON = (By.XPATH, './/android.widget.Button[@content-desc="Accept"]')
    ACCEPT_BUTTON_ios = (By.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAButton[1]')

    # alert message with word "Invalid"
    ALERT_MSG_INVALID = (By.XPATH, './/android.view.View[@content-desc[contains(., "Invalid")]]')
    ALERT_MSG_INVALID_ios = (By.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]'
                                       '/UIAStaticText[5][@name="Invalid username and/or password"]')

    # alert message with "Your temporary account has been expired"
    ALERT_MSG_EXPIRED = (By.XPATH, './/android.view.View[@content-desc[contains('
                                   '., "Your temporary account has been expired")]]')

    ALERT_MSG_EXPIRED_ios = (By.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]'
                                       '/UIAWebView[1]/UIAStaticText[5][@name[contains'
                                       '(., "Your temporary account has been expired")]]')

    # alert message with "The password for the current user is about to expire"
    ALERT_MSG_WILL_EXPIRE = (By.XPATH,
                             './/android.view.View[@content-desc[contains('
                             '., "The password for the current user is about to expire")]]')
    ALERT_MSG_WILL_EXPIRE_ios = (By.XPATH, '')

    # alert message with word "inactive"
    ALERT_MSG_SUSPENDED = (By.XPATH,
                           './/android.view.View[@content-desc[contains(., "Your account is currently inactive")]]')
    ALERT_MSG_SUSPENDED_ios = (By.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/'
                                         'UIAStaticText[5][@name[contains(., "Your account is currently inactive")]]')

    # alert message about expiring password
    NOTICE_ALERT_OK_BUTTON = (By.XPATH,
                              './/android.view.View[@index="24"]//android.view.View[@content-desc[contains(., "Ok")]]')
    # the same as OK_BUTTON ??
    #NOTICE_ALERT_OK_BUTTON_ios = (By.XPATH, '')

    # OK button on alert messages"
    OK_BUTTON = (By.XPATH, './/android.view.View[@content-desc="Ok"]')
    OK_BUTTON_ios = (By.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[4]')


class MainMenuScreen(object):
    """A class for main menu screen locators - first screen after correct login into the app."""
    BUTTONS = (By.CLASS_NAME, 'android.view.View')
    BUTTONS_ios = (By.CLASS_NAME, '')
    LOGOUT_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "LOGOUT")]]')
    LOGOUT_BUTTON_ios = (By.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[24]')
    LOGOUT_SUBMIT_ios = (By.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAButton[1]')
    EVENTS_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "EVENTS")]]')
    EVENTS_BUTTON_ios = (By.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[4]')


class EventsScreen(object):
    """A class for Events screen locators - screen after clicking into Events button in Main Menu."""
    EVENTS_HEADER = (By.XPATH, './/android.view.View[@content-desc[contains(., "Events")]]')
    EVENTS_HEADER_ios = (By.XPATH, '')

    # filtering events by Type
    ANY_TYPE_EXPAND = (By.XPATH, './/android.view.View[@content-desc[contains(., "Any Type click to expand")]]')
    ANY_TYPE_EXPAND_ios = (By.XPATH, '')
    CHOOSE_TYPE_INCIDENT = (By.XPATH, './/android.view.View[@content-desc="Incident"]')
    CHOOSE_TYPE_INCIDENT_ios = (By.XPATH, '')
    INCIDENT_TYPE_EXPAND = (By.XPATH, './/android.view.View[@content-desc[contains(., "Incident click to expand")]]')
    INCIDENT_TYPE_EXPAND_ios = (By.XPATH, '')
    CHOOSE_TYPE_ANY = (By.XPATH, './/android.view.View[@content-desc="Any Type"]')
    CHOOSE_TYPE_ANY_ios = (By.XPATH, '')

    # filtering events by Status
    ANY_STATUS_EXPAND = (By.XPATH, './/android.view.View[@content-desc[contains(., "Any Status click to expand")]]')
    ANY_STATUS_EXPAND_ios = (By.XPATH, '')
    CHOOSE_ACTIVE_STATUS = (By.XPATH, './/android.view.View[@content-desc="Active"]')
    CHOOSE_ACTIVE_STATUS_ios = (By.XPATH, '')
    ACTIVE_STATUS_EXPAND = (By.XPATH, './/android.view.View[@content-desc[contains(., "Active click to expand")]]')
    ACTIVE_STATUS_EXPAND_ios = (By.XPATH, '')
    CHOOSE_INACTIVE_STATUS = (By.XPATH, './/android.view.View[@content-desc="Inactive"]')
    CHOOSE_INACTIVE_STATUS_ios = (By.XPATH, '')
    INACTIVE_STATUS_EXPAND = (By.XPATH, './/android.view.View[@content-desc[contains(., "Inactive click to expand")]]')
    INACTIVE_STATUS_EXPAND_ios = (By.XPATH, '')
    CHOOSE_DRAFT_STATUS = (By.XPATH, './/android.view.View[@content-desc="Draft"]')
    CHOOSE_DRAFT_STATUS_ios = (By.XPATH, '')
    DRAFT_STATUS_EXPAND = (By.XPATH, './/android.view.View[@content-desc[contains(., "Draft click to expand")]]')
    DRAFT_STATUS_EXPAND_ios = (By.XPATH, '')
    CHOOSE_ANY_STATUS = (By.XPATH, './/android.view.View[@content-desc="Any Status"]')
    CHOOSE_ANY_STATUS_ios = (By.XPATH, '')

    # filtering events using search field
    SEARCH_FIELD = (By.XPATH, './/android.widget.EditText[@index="3"]')
    SEARCH_FIELD_ios = (By.XPATH, '')
    EVENTS_HEADER_AFTER_SEARCH = (By.XPATH, './/android.view.View[@index="5"]')
    EVENTS_HEADER_AFTER_SEARCH_ios = (By.XPATH, '')

    # creating and editing Events
    MORE_BUTTON = (By.XPATH, './/android.widget.Spinner[@content-desc[contains(., "More")]]')
    MORE_BUTTON_ios = (By.XPATH, '')
    NEW_EVENT_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "New event")]]')
    NEW_EVENT_BUTTON_ios = (By.XPATH, '')

    # previously created event
    CREATED_EVENT_1 = (By.XPATH, './/android.view.View[@content-desc[contains(., "Test")]]')
    CREATED_EVENT_1_ios = (By.XPATH, '')
    CREATED_EVENT_2 = (By.XPATH, './/android.view.View[@content-desc[contains(., "Test Appium - second event")]]')
    CREATED_EVENT_2_ios = (By.XPATH, '')
    CREATED_EVENT_3 = (By.XPATH, './/android.view.View[@content-desc[contains(., "Test to create sub event")]]')
    CREATED_EVENT_3_ios = (By.XPATH, '')
    CLEAR_PRIMARY_EVENT_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "Clear primary event")]]')
    CLEAR_PRIMARY_EVENT_BUTTON_ios = (By.XPATH, '')
    NOTIFICATION_PRIMARY_EVENT_CLEARED = (By.XPATH, './/android.view.View[@content-desc="Primary event cleared"]')
    NOTIFICATION_PRIMARY_EVENT_CLEARED_ios = (By.XPATH, '')
    GO_BACK_TO_MAIN_MENU_ARROW_BUTTON = (By.XPATH, ".//android.webkit.WebView[@index='0']"
                                                   "//android.view.View[@index='0']"
                                                   "//android.view.View[@index='0']")
    GO_BACK_TO_MAIN_MENU_ARROW_BUTTON_ios = (By.XPATH, '')


class TypesOfEventsScreen(object):
    """A class for Type of Events screen locators - first screen after creating new event with types of events."""
    INCIDENT_TYPE_OF_EVENT = (By.XPATH, './/android.view.View[@content-desc[contains(., "Incident")]]')
    INCIDENT_TYPE_OF_EVENT_ios = (By.XPATH, '')


class EventEditScreen(object):
    """A class for Edit Events screen locators - screen after opening edit mode of event or creating a new one."""
    NAME_FIELD = (By.XPATH, './/android.widget.EditText[@index="1"]')
    NAME_FIELD_ios = (By.XPATH, '')
    SEVERITY_LEVEL_SELECTOR = (By.XPATH, './/android.widget.ListView[@index="0"]'
                                         '//android.view.View[@index="3"]'
                                         '//android.widget.Spinner[@index="2"]')
    SEVERITY_LEVEL_SELECTOR_ios = (By.XPATH, '')
    CHOOSE_SEVERITY_LVL1 = (By.NAME, 'Severity 1')
    CHOOSE_SEVERITY_LVL1_ios = (By.NAME, 'Severity 1')
    CHOOSE_SEVERITY_LVL2 = (By.NAME, 'Severity 2')
    CHOOSE_SEVERITY_LVL2_ios = (By.NAME, 'Severity 2')
    CHOOSE_SEVERITY_LVL3 = (By.NAME, 'Severity 3')
    CHOOSE_SEVERITY_LVL3_ios = (By.NAME, 'Severity 3')
    CHOOSE_SEVERITY_LVL4 = (By.NAME, 'Severity 4')
    CHOOSE_SEVERITY_LVL4_ios = (By.NAME, 'Severity 4')
    FINISHED_FIELD = (By.XPATH, './/android.view.View[@content-desc="Finished"]')
    FINISHED_FIELD_ios = (By.XPATH, '')
    TIME_DATE = (By.XPATH, './/android.widget.ImageButton[@content-desc="Increase year"]')
    TIME_DATE_ios = (By.XPATH, '')
    SET_BUTTON = (By.ID, 'android:id/button1')
    SET_BUTTON_ios = (By.ID, '')
    SAVE_BUTTON = (By.XPATH, './/android.widget.Button[@content-desc="Save"]')
    SAVE_BUTTON_ios = (By.XPATH, '')
    DESCRIPTION_FIELD = (By.XPATH,
                         ".//android.widget.ListView[@index='0']"
                         "//android.view.View[@index='8' and @content-desc[contains(., 'Description')]]"
                         "//android.view.View[@index='1']"
                         "//android.view.View[@index='1']"
                         "//android.view.View[@index='0']"
                         "//android.view.View[@index='0']"
                         "//android.view.View[@index='0' and @clickable='true']")
    DESCRIPTION_FIELD_ios = (By.XPATH, '')

    # headers for scrolling
    FINISHED_HEADER = (By.XPATH, './/android.view.View[@content-desc="Finished"]')
    FINISHED_HEADER_ios = (By.XPATH, '')
    LEADAGENCY_HEADER = (By.XPATH, './/android.view.View[@content-desc="Lead agency"]')
    LEADAGENCY_HEADER_ios = (By.XPATH, '')
    IMPACT_HEADER = (By.XPATH, './/android.view.View[@content-desc="Impact"]')
    IMPACT_HEADER_ios = (By.XPATH, '')
    CAUSE_HEADER = (By.XPATH, './/android.view.View[@content-desc="Cause"]')
    CAUSE_HEADER_ios = (By.XPATH, '')
    SITUATION_HEADER = (By.XPATH, './/android.view.View[@content-desc="Situation"]')
    SITUATION_HEADER_ios = (By.XPATH, '')
    ISSUES_HEADER = (By.XPATH, './/android.view.View[@content-desc="Issues"]')
    ISSUES_HEADER_ios = (By.XPATH, '')
    OBJECTIVES_HEADER = (By.XPATH, './/android.view.View[@content-desc="Objectives"]')
    OBJECTIVES_HEADER_ios = (By.XPATH, '')
    STRATEGIES_HEADER = (By.XPATH, './/android.view.View[@content-desc="Strategies"]')
    STRATEGIES_HEADER_ios = (By.XPATH, '')
    TACTICS_HEADER = (By.XPATH, './/android.view.View[@content-desc="Tactics"]')
    TACTICS_HEADER_ios = (By.XPATH, '')
    COMMUNICATIONS_HEADER = (By.XPATH, './/android.view.View[@content-desc="Communications"]')
    COMMUNICATIONS_HEADER_ios = (By.XPATH, '')
    RELATED_HEADER = (By.XPATH, './/android.view.View[@content-desc="Related"]')
    RELATED_HEADER_ios = (By.XPATH, '')
    CREATE_MAPPING_DATA = (By.XPATH, ".//android.view.View[@content-desc[contains(., ' mapping data')]]")
    CREATE_MAPPING_DATA_ios = (By.XPATH, '')


class EventDetailsScreen(object):
    """A class for Event Details screen locators - screen with event details - after opening event."""
    EDIT_BUTTON = (By.XPATH, './/android.widget.Button[@content-desc="Edit"]')
    EDIT_BUTTON_ios = (By.XPATH, '')
    DELETE_EVENT_BUTTON = (By.XPATH, "//android.widget.ListView[@index='2']"
                                     "//android.view.View[@index='2']"
                                     "//android.view.View[@content-desc[contains(., 'Delete event')]]")
    DELETE_EVENT_BUTTON_ios = (By.XPATH, '')
    DELETE_CONFIRM_BUTTON = (By.XPATH, './/android.view.View[@content-desc="Delete"]')
    DELETE_CONFIRM_BUTTON_ios = (By.XPATH, '')
    NEW_SUB_EVENT = (By.XPATH, './/android.view.View[@content-desc[contains(., "New sub event")]]')
    NEW_SUB_EVENT_ios = (By.XPATH, '')
    SET_AS_PRIMARY_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "Set as primary")]]')
    SET_AS_PRIMARY_BUTTON_ios = (By.XPATH, '')


class Map(object):
    TOOL_BUTTON = (By.XPATH, ".//android.widget.Spinner[@content-desc[contains(., 'Tool')]]")
    TOOL_BUTTON_ios = (By.XPATH, '')
    POINT_BUTTON = (By.XPATH, ".//android.view.View[@content-desc[contains(., 'Point click to expand')]]")
    POINT_BUTTON_ios = (By.XPATH, '')
    POINT_DEFAULT_BUTTON = (By.XPATH, ".//android.view.View[@content-desc='Default']")
    POINT_DEFAULT_BUTTON_ios = (By.XPATH, '')
    ADD_POINT_INTO_MAP = (By.XPATH, ".//android.widget.Image[@index='6']")
    ADD_POINT_INTO_MAP_ios = (By.XPATH, '')
    LINE_BUTTON = (By.XPATH, ".//android.view.View[@content-desc[contains(., 'Line click to expand')]]")
    LINE_BUTTON_ios = (By.XPATH, '')
    LINE_DEFAULT_BUTTON = (By.XPATH, ".//android.view.View[@content-desc='Default']")
    LINE_DEFAULT_BUTTON_ios = (By.XPATH, '')
    ADD_LINE1 = (By.XPATH, ".//android.widget.Image[@index='5']")
    ADD_LINE1_ios = (By.XPATH, '')
    ADD_LINE2 = (By.XPATH, ".//android.widget.Image[@index='6']")
    ADD_LINE2_ios = (By.XPATH, '')
    CIRCLE_BUTTON = (By.XPATH, ".//android.view.View[@content-desc[contains(., 'Circle click to expand')]]")
    CIRCLE_BUTTON_ios = (By.XPATH, '')
    CIRCLE_DEFAULT_BUTTON = (By.XPATH, ".//android.view.View[@content-desc='Default']")
    CIRCLE_DEFAULT_BUTTON_ios = (By.XPATH, '')
    ADD_CIRCLE_INTO_MAP = (By.XPATH, ".//android.widget.Image[@index='6']")
    ADD_CIRCLE_INTO_MAP_ios = (By.XPATH, '')
    POLYGON_BUTTON = (By.XPATH, ".//android.view.View[@content-desc[contains(., 'Polygon click to expand')]]")
    POLYGON_BUTTON_ios = (By.XPATH, '')
    POLYGON_DEFAULT_BUTTON = (By.XPATH, ".//android.view.View[@content-desc='Default']")
    POLYGON_DEFAULT_BUTTON_ios = (By.XPATH, '')
    ADD_POLYGON1 = (By.XPATH, ".//android.widget.Image[@index='5']")
    ADD_POLYGON1_ios = (By.XPATH, '')
    ADD_POLYGON2 = (By.XPATH, ".//android.widget.Image[@index='6']")
    ADD_POLYGON2_ios = (By.XPATH, '')
    ADD_POLYGON3 = (By.XPATH, ".//android.widget.Image[@index='3']")
    ADD_POLYGON3_ios = (By.XPATH, '')
    SAVE_MAP_BUTTON = (By.XPATH, ".//android.widget.Button[@content-desc='Save']")
    SAVE_MAP_BUTTON_ios = (By.XPATH, '')


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass


