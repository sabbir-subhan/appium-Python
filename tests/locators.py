from selenium.webdriver.common.by import By


class WelcomeScreen(object):
    """A class for welcome screen locators - first screen after lunching the app."""
    LOGIN_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "LOGIN")]]')


class LoginScreen(object):
    """A class for login screen locators - screen after clicking into LOGIN."""
    TEXTFIELD_USERNAME = (By.XPATH, './/android.widget.EditText[@index="1"]')
    TEXTFIELD_PASSWORD = (By.XPATH, './/android.widget.EditText[@index="3"]')
    TEXTFIELD_DOMAIN = (By.XPATH, './/android.widget.EditText[@index="5"]')
    SUBMIT_BUTTON = (By.XPATH, '//android.widget.Button[@content-desc="Submit"]')

    # ACCEPT_BUTTON on Terms and Conditions"
    ACCEPT_BUTTON = (By.XPATH, './/android.widget.Button[@content-desc="Accept"]')

    # alert message with word "Invalid"
    ALERT_MSG_INVALID = (By.XPATH, './/android.view.View[@content-desc[contains(., "Invalid")]]')

    # alert message with word "Invalid"
    ALERT_MSG_EXPIRED = (By.XPATH, './/android.view.View[@content-desc[contains('
                                   '., "Your temporary account has been expired")]]')

    # alert message with word "Invalid"
    ALERT_MSG_WILL_EXPIRE = (By.XPATH,
                             './/android.view.View[@content-desc[contains('
                             '., "The password for the current user is about to expire")]]')

    # alert message with word "inactive"
    ALERT_MSG_SUSPENDED = (By.XPATH,
                           './/android.view.View[@content-desc[contains(., "Your account is currently inactive")]]')

    # OK button on alert message"
    OK_BUTTON = (By.XPATH, './/android.view.View[@content-desc="Ok"]')


class MainMenuScreen(object):
    """A class for main menu screen locators - first screen after correct login into the app."""
    BUTTONS = (By.CLASS_NAME, 'android.view.View')
    LOGOUT_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "LOGOUT")]]')
    EVENTS_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "EVENTS")]]')
    NOTICE_ALERT = (By.XPATH, './/android.view.View[@index="24"]//android.view.View[@content-desc[contains(., "Ok")]]')


class EventsScreen(object):
    """A class for Events screen locators - screen after clicking into Events button in Main Menu."""
    EVENTS_HEADER = (By.XPATH, './/android.view.View[@content-desc[contains(., "Events")]]')

    # filtering events by Type
    ANY_TYPE_EXPAND = (By.XPATH, './/android.view.View[@content-desc[contains(., "Any Type click to expand")]]')
    CHOOSE_TYPE_INCIDENT = (By.XPATH, './/android.view.View[@content-desc="Incident"]')
    INCIDENT_TYPE_EXPAND = (By.XPATH, './/android.view.View[@content-desc[contains(., "Incident click to expand")]]')
    CHOOSE_TYPE_ANY = (By.XPATH, './/android.view.View[@content-desc="Any Type"]')

    # filtering events by Status
    ANY_STATUS_EXPAND = (By.XPATH, './/android.view.View[@content-desc[contains(., "Any Status click to expand")]]')
    CHOOSE_ACTIVE_STATUS = (By.XPATH, './/android.view.View[@content-desc="Active"]')
    ACTIVE_STATUS_EXPAND = (By.XPATH, './/android.view.View[@content-desc[contains(., "Active click to expand")]]')
    CHOOSE_INACTIVE_STATUS = (By.XPATH, './/android.view.View[@content-desc="Inactive"]')
    INACTIVE_STATUS_EXPAND = (By.XPATH, './/android.view.View[@content-desc[contains(., "Inactive click to expand")]]')
    CHOOSE_DRAFT_STATUS = (By.XPATH, './/android.view.View[@content-desc="Draft"]')
    DRAFT_STATUS_EXPAND = (By.XPATH, './/android.view.View[@content-desc[contains(., "Draft click to expand")]]')
    CHOOSE_ANY_STATUS = (By.XPATH, './/android.view.View[@content-desc="Any Status"]')

    # filtering events using search field
    SEARCH_FIELD = (By.XPATH, './/android.widget.EditText[@index="3"]')
    EVENTS_HEADER_AFTER_SEARCH = (By.XPATH, './/android.view.View[@index="5"]')

    # creating and editing Events
    MORE_BUTTON = (By.XPATH, './/android.widget.Spinner[@content-desc[contains(., "More")]]')
    NEW_EVENT_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "New event")]]')

    # previously created event
    CREATED_EVENT_1 = (By.XPATH, './/android.view.View[@content-desc[contains(., "Test")]]')
    CREATED_EVENT_2 = (By.XPATH, './/android.view.View[@content-desc[contains(., "Test Appium - second event")]]')
    CREATED_EVENT_3 = (By.XPATH, ".//android.view.View[@content-desc[contains(., 'Test to create sub event')]]")
    CLEAR_PRIMARY_EVENT_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "Clear primary event")]]')
    NOTIFICATION_PRIMARY_EVENT_CLEARED = (By.XPATH, ".//android.view.View[@content-desc='Primary event cleared']")
    GO_BACK_TO_MAIN_MENU_ARROW_BUTTON = (By.XPATH, ".//android.webkit.WebView[@index='0']"
                                                   "//android.view.View[@index='0']"
                                                   "//android.view.View[@index='0']")


class TypesOfEventsScreen(object):
    """A class for Type of Events screen locators - first screen after creating new event with types of events."""
    INCIDENT_TYPE_OF_EVENT = (By.XPATH, './/android.view.View[@content-desc[contains(., "Incident")]]')


class EventEditScreen(object):
    """A class for Edit Events screen locators - screen after opening edit mode of event or creating a new one."""
    NAME_FIELD = (By.XPATH, './/android.widget.EditText[@index="1"]')
    SEVERITY_LEVEL_SELECTOR = (By.XPATH, './/android.widget.ListView[@index="0"]'
                                         '//android.view.View[@index="3"]'
                                         '//android.widget.Spinner[@index="2"]')
    CHOOSE_SEVERITY_LVL1 = (By.NAME, 'Severity 1')
    CHOOSE_SEVERITY_LVL2 = (By.NAME, 'Severity 2')
    CHOOSE_SEVERITY_LVL3 = (By.NAME, 'Severity 3')
    CHOOSE_SEVERITY_LVL4 = (By.NAME, 'Severity 4')
    FINISHED_FIELD = (By.XPATH, './/android.view.View[@content-desc="Finished"]')
    TIME_DATE = (By.XPATH, './/android.widget.ImageButton[@content-desc="Increase year"]')
    SET_BUTTON = (By.ID, 'android:id/button1')
    SAVE_BUTTON = (By.XPATH, './/android.widget.Button[@content-desc="Save"]')
    DESCRIPTION_FIELD = (By.XPATH,
                         ".//android.widget.ListView[@index='0']"
                         "//android.view.View[@index='8' and @content-desc[contains(., 'Description')]]"
                         "//android.view.View[@index='1']"
                         "//android.view.View[@index='1']"
                         "//android.view.View[@index='0']"
                         "//android.view.View[@index='0']"
                         "//android.view.View[@index='0' and @clickable='true']")
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
    CREATE_MAPPING_DATA = (By.XPATH, ".//android.view.View[@content-desc[contains(., ' mapping data')]]")


class EventDetailsScreen(object):
    """A class for Event Details screen locators - screen with event details - after opening event."""
    EDIT_BUTTON = (By.XPATH, './/android.widget.Button[@content-desc="Edit"]')
    DELETE_EVENT_BUTTON = (By.XPATH, "//android.widget.ListView[@index='2']"
                                     "//android.view.View[@index='2']"
                                     "//android.view.View[@content-desc[contains(., 'Delete event')]]")
    DELETE_CONFIRM_BUTTON = (By.XPATH, './/android.view.View[@content-desc="Delete"]')
    NEW_SUB_EVENT = (By.XPATH, './/android.view.View[@content-desc[contains(., "New sub event")]]')
    SET_AS_PRIMARY_BUTTON = (By.XPATH, './/android.view.View[@content-desc[contains(., "Set as primary")]]')


class Map(object):
    TOOL_BUTTON = (By.XPATH, ".//android.widget.Spinner[@content-desc[contains(., 'Tool')]]")
    POINT_BUTTON = (By.XPATH, ".//android.view.View[@content-desc[contains(., 'Point click to expand')]]")
    POINT_DEFAULT_BUTTON = (By.XPATH, ".//android.view.View[@content-desc='Default']")
    ADD_POINT_INTO_MAP = (By.XPATH, ".//android.widget.Image[@index='6']")
    LINE_BUTTON = (By.XPATH, ".//android.view.View[@content-desc[contains(., 'Line click to expand')]]")
    LINE_DEFAULT_BUTTON = (By.XPATH, ".//android.view.View[@content-desc='Default']")
    ADD_LINE1 = (By.XPATH, ".//android.widget.Image[@index='5']")
    ADD_LINE2 = (By.XPATH, ".//android.widget.Image[@index='6']")
    CIRCLE_BUTTON = (By.XPATH, ".//android.view.View[@content-desc[contains(., 'Circle click to expand')]]")
    CIRCLE_DEFAULT_BUTTON = (By.XPATH, ".//android.view.View[@content-desc='Default']")
    ADD_CIRCLE_INTO_MAP = (By.XPATH, ".//android.widget.Image[@index='6']")
    POLYGON_BUTTON = (By.XPATH, ".//android.view.View[@content-desc[contains(., 'Polygon click to expand')]]")
    POLYGON_DEFAULT_BUTTON = (By.XPATH, ".//android.view.View[@content-desc='Default']")
    ADD_POLYGON1 = (By.XPATH, ".//android.widget.Image[@index='5']")
    ADD_POLYGON2 = (By.XPATH, ".//android.widget.Image[@index='6']")
    ADD_POLYGON3 = (By.XPATH, ".//android.widget.Image[@index='9']")
    SAVE_MAP_BUTTON = (By.XPATH, ".//android.widget.Button[@content-desc='Save']")


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass


