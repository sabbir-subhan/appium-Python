""" locators for Android """

from appium.webdriver.common.mobileby import MobileBy


class Android:
    """A class for handling Android device for example alerts"""

    # Android alerts
    ANDROID_ALLOW = (MobileBy.ID, 'com.android.packageinstaller:id/permission_allow_button')
    ANDROID_DENY = (MobileBy.ID, 'com.android.packageinstaller:id/permission_deny_button')
    ANDROID_ALLOW2 = (MobileBy.XPATH, '//android.widget.Button[@text="ALLOW"]')

    # Set date and time
    ANDROID_SET_BUTTON = (MobileBy.ID, 'android:id/button1')
    ANDROID_CANCEL_BUTTON = (MobileBy.ID, 'android:id/button2')
    ANDROID_CLEAR_BUTTON = (MobileBy.ID, 'android:id/button3')
    # TURN_WIFI_ON = (MobileBy.XPATH, '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.view.ViewGroup[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]')
    SWITCH_WIFI_ANDROID_7 = (MobileBy.XPATH, '//android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.view.ViewGroup[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]')
    SWITCH_WIFI_ANDROID_7_1 = (MobileBy.XPATH, '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.view.ViewGroup[1]/android.widget.Button[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]')
    SWITCH_AIRPLANE_MODE_7_1 = (MobileBy.ACCESSIBILITY_ID, 'Airplane mode')
    SWITCH_ON_AIRPLANE_MODE_7 = (MobileBy.ACCESSIBILITY_ID, 'Airplane,mode,On.,Button')
    SWITCH_OFF_AIRPLANE_MODE_7 = (MobileBy.ACCESSIBILITY_ID, 'Airplane,mode,Off.,Button')
    # SWITCH_AIRPLANE_MODE_7 = (MobileBy.ACCESSIBILITY_ID, 'Airplane,mode,Off.,Button')


class CommonScreen:
    """A class for handling Common buttons on different screen"""
    # LOADING = (MobileBy.XPATH, '//android.view.View[@content-desc="loading"]')
    # LOADING = (MobileBy.XPATH, '//android.view.View[@content-desc="loading" and @enabled="true"]')
    LOADING = (MobileBy.ACCESSIBILITY_ID, 'loading')
    UPLOADING = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Uploading")]]')  # not working
    SAVE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Save')
    CANCEL_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Cancel')
    CANCEL_BUTTON_by_index = (MobileBy.XPATH, '//android.view.View[2]/android.widget.Button')
    OK_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Ok')
    # WEB_VIEW = (MobileBy.XPATH, '//android.webkit.WebView[@scrollable="true"]')
    WEB_VIEW = (MobileBy.CLASS_NAME, 'android.webkit.WebView')
    SPINNER_ON_THE_RIGHT = (MobileBy.XPATH, '//android.widget.ListView[1]/android.view.View[2]'
                                            '/android.widget.Spinner[@clickable="true"]')
    SPINNER_ON_THE_LEFT = (MobileBy.XPATH, '//android.widget.ListView[1]/android.view.View[1]'
                                           '/android.widget.Spinner[@clickable="true"]')
    WHOLE_APP_SCREEN = (MobileBy.ACCESSIBILITY_ID, 'OCA')
    FIRST_INPUT_FIELD = (MobileBy.XPATH, '//android.widget.EditText[1]')  # first input filed inside OCA objects, like events, assets, reports
    ADD_MEDIA = (MobileBy.ACCESSIBILITY_ID, 'Add media')  # button Add Media inside OCA objects
    ADD_MEDIA2 = (MobileBy.XPATH, '//android.widget.Button[@name="Add media"]')
    POPUP_UNFILLED_FIELDS = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Required fields are not filled")]]')  # Validation error


class TopBar:
    """A class for top bar locators."""
    HAMBURGER_FOR_MAIN_MENU_by_xpath = (MobileBy.XPATH, '//android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]')
    HAMBURGER_FOR_MAIN_MENU_by_id = (MobileBy.ID, 'iconbar')


class WelcomeScreen:
    """A class for welcome screen locators - first screen after lunching the app."""
    LOCATION_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "LOCATION")]]')
    MY_MESSAGES_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "MY MESSAGES")]]')
    PHOTO_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "PHOTO")]]')
    VIDEO_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "VIDEO")]]')
    SOUND_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "SOUND")]]')
    SETTINGS_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "SETTINGS")]]')
    ABOUT_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "ABOUT")]]')
    LOGIN_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "LOGIN")]]')
    LOGIN_BUTTON_by_index = (MobileBy.XPATH, '//android.webkit.WebView/android.view.View/'
                                             'android.view.View[@index="6"]/android.view.View[@index="0"]')


class SettingsScreen:
    """A class for settings screen locators - screen after clicking settings button"""
    SETTINGS_CONTACT_IDENTIFIER_FIELD = (MobileBy.CLASS_NAME, 'android.widget.EditText')
    SETTINGS_ALERT_APP_HAS_BEEN_ACTIVATED = (MobileBy.ACCESSIBILITY_ID, 'App has been activated.')
    SETTINGS_OK_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Ok')


class LoginScreen:
    """A class for login screen locators - screen after clicking into LOGIN."""
    TEXTFIELD_USERNAME = (MobileBy.ACCESSIBILITY_ID, 'Username')
    TEXTFIELD_PASSWORD = (MobileBy.XPATH, '//android.widget.EditText[@index="3"]')
    TEXTFIELD_DOMAIN = (MobileBy.XPATH, '//android.widget.EditText[@index="1"]')
    SUBMIT_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Submit')

    # Notification alert: "OCA now supports sending 'App Messages' to your device as notifications."
    NOTIFICATION_ABOUT_SENDING_MESSAGES = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., '
                                                           '"OCA now supports ")]]')
    SSO_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'SSO')

    # "No" button for sending notifications on Android
    NO_FOR_SENDING_NOTIFICATIONS_ON = (MobileBy.ACCESSIBILITY_ID, 'No')

    # ACCEPT_BUTTON on Terms and Conditions"
    ACCEPT_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Accept')

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
    OK_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Ok')


class MainMenuScreen(WelcomeScreen):
    """A class for main menu screen locators - first screen after correct login into the app."""
    MENU = (MobileBy.ID, 'menu')
    BUTTONS = (MobileBy.CLASS_NAME, 'android.view.View')
    ACTIVATE_WORKFLOW_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "ACTIVATE WORKFLOW")]]')
    CREATE_CONTACT_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "CREATE CONTACT")]]')
    CREATE_TASK_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "CREATE A TASK")]]')
    CREATE_REPORT_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "CREATE A REPORT")]]')
    WEBSITE_LINK_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "WEBSITE LINK")]]')
    INCIDENT_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "INCIDENT")]]')
    CREATE_ASSETS_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "CREATE ASSETS")]]')
    CREATE_LOG_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "CREATE A LOG")]]')
    RISKS_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "RISKS")]]')
    EVENTS_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "EVENTS")]]')
    LOGS_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "LOGS")]]')
    REPORTS_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "REPORTS")]]')
    MAP_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "MAP")]]')
    ASSETS_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "ASSETS")]]')
    INBOX_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "INBOX")]]')
    COMPOSE_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "COMPOSE")]]')
    SENT_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "SENT")]]')
    TASKS_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "TASKS")]]')
    DOCUMENTS_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "DOCUMENTS")]]')
    CONTACTS_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "CONTACTS")]]')
    ALLOCATE_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "ALLOCATE")]]')
    ACTIVATE_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "ACTIVATE")]]')
    OFFLINE_SYNC_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "OFFLINE SYNC")]]')
    LOGOUT_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "LOGOUT")]]')  # there is problem with that locator because buttons suddenly don't have attribute content-desc
    ALERT_ACTIVATE_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc="Activate" and @focusable ="true"]')
    ALERT_CANCEL_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Cancel")]]')
    ALERT_WORKFLOW_ACTIVATED = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Workflow activated")]]')


class LocationScreen:
    """A class for Location screen locators - screen after clicking into Location button in Main Menu."""
    SEND_ONCE_NOW = (MobileBy.XPATH, '//android.widget.Button[@content-desc[contains(., "Send once now")]]')
    SEND_EVERY_SPINNER = (MobileBy.XPATH, '//android.widget.Spinner[@index="7"]')
    CHOOSE_5_MINUTES_OPTION = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="5 minutes"]')
    ASSERT_5_MINUTES_OPTION = (MobileBy.XPATH, '//android.widget.Spinner[@content-desc="5 minutes"]')
    FOR_THE_NEXT_SPINNER = (MobileBy.XPATH, '//android.widget.Spinner[@index="11"]')
    CHOOSE_1_HOUR_OPTION = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="1 hour"]')
    ASSERT_1_HOUR_OPTION = (MobileBy.XPATH, '//android.widget.Spinner[@content-desc="1 hour"]')
    ASSERT_SENDING_NOW = (MobileBy.XPATH, '//android.widget.Button[content-desc[contains(., "Sending now")]]')
    START_BUTTON = (MobileBy.XPATH, '//android.widget.Button[@content-desc[contains(., "Start")]]')
    START_BUTTON_disabled = (MobileBy.XPATH, '//android.widget.Button[@content-desc['
                                             'contains(., "Start")] and @enabled="false"]')
    LOCATION_PAGE_HEADER = (MobileBy.ACCESSIBILITY_ID, 'Your location was last sent')
    # LOCATION_STATUS = (MobileBy.ACCESSIBILITY_ID, 'a few seconds ago')
    LOCATION_STATUS = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., " seconds ago")]]')


class EventsScreen:
    """A class for Events screen locators - screen after clicking into Events button in Main Menu."""
    EVENTS_HEADER = (MobileBy.ACCESSIBILITY_ID, 'Events')

    # filtering events by Type
    ANY_TYPE_EXPAND = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Any Type click to expand")]]')
    CHOOSE_TYPE_INCIDENT = (MobileBy.ACCESSIBILITY_ID, 'Incident')
    INCIDENT_TYPE_EXPAND = (MobileBy.XPATH, '//android.view.View[@content-desc[contains('
                                            '., "Incident click to expand")]]')
    CHOOSE_TYPE_ANY = (MobileBy.ACCESSIBILITY_ID, 'Any Type')

    # filtering events by Status
    ANY_STATUS_EXPAND = (MobileBy.XPATH, '//android.view.View[@content-desc[contains('
                                         '., "Any Status click to expand")]]')
    CHOOSE_ACTIVE_STATUS = (MobileBy.ACCESSIBILITY_ID, 'Active')
    ACTIVE_STATUS_EXPAND = (MobileBy.XPATH, '//android.view.View[@content-desc[contains('
                                            '., "Active click to expand")]]')
    CHOOSE_INACTIVE_STATUS = (MobileBy.ACCESSIBILITY_ID, 'Inactive')
    INACTIVE_STATUS_EXPAND = (MobileBy.XPATH, '//android.view.View[@content-desc[contains('
                                              '., "Inactive click to expand")]]')
    CHOOSE_DRAFT_STATUS = (MobileBy.ACCESSIBILITY_ID, 'Draft')
    DRAFT_STATUS_EXPAND = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Draft click to expand")]]')
    CHOOSE_ANY_STATUS = (MobileBy.ACCESSIBILITY_ID, 'Any Status')

    # filtering events using search field
    SEARCH_FIELD = (MobileBy.CLASS_NAME, 'android.widget.EditText')
    EVENTS_HEADER_AFTER_SEARCH = (MobileBy.XPATH, '//android.view.View[@index="5"]')

    # MORE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'More▼')

    MORE_BUTTON = (MobileBy.XPATH, '//android.widget.ListView[1]/android.view.View[2]'
                                   '/android.widget.Spinner[@clickable="true"]')

    # creating and editing Events
    NEW_EVENT_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'New event ')
    # NEW_EVENT_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "New event")]]')

    # previously created event
    PREVIOUSLY_CREATED_EVENT = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Appium")]]')
    # CREATED_EVENT_2 = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "second event")]]')
    # CREATED_EVENT_2 = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "sub event")]]')

    CLEAR_PRIMARY_EVENT_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc="Clear primary event"]')
    NOTIFICATION_PRIMARY_EVENT_CLEARED = (MobileBy.XPATH, '//android.view.View[@content-desc[contains'
                                                          '(., "Primary event cleared")]]')
    GO_BACK_TO_MAIN_MENU_ARROW_BUTTON = (MobileBy.XPATH, "//android.webkit.WebView[@index='0']"
                                                         "//android.view.View[@index='0']"
                                                         "//android.view.View[@index='0']")
    NOTIFICATION_ABOUT_OFFLINE_MODE = (MobileBy.XPATH, '//android.view.View[@content-desc="Offline mode"]')
    # NOTIFICATION_ABOUT_OFFLINE_MODE = (MobileBy.ACCESSIBILITY_ID, 'Offline mode')


class TypesOfEventsScreen:
    """A class for Type of Events screen locators - first screen after creating new event with types of events."""
    INCIDENT_TYPE_OF_EVENT = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Incident")]]')
    EVENT_FOR_ON_LOAD_SAVE = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "event_for_on_load")]]')
    EVENT_FOR_CHOOSER_FIELDS = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "event_for_chooser")]]')
    EVENT_TYPE_WITH_OPTION_LIST = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "event_with_option_list")]]')


class EventEditScreen:
    """A class for Edit Events screen locators - screen after opening edit mode of event or creating a new one."""
    SAVE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Save')
    # SAVE_BUTTON = (MobileBy.XPATH, '//android.widget.Button[@content-desc[contains(., "Save")]]')
    NAME_FIELD = (MobileBy.ID, 'name')
    NAME_FIELD2 = (MobileBy.XPATH, '//android.widget.EditText[@index="1"]')
    SEVERITY_LEVEL_SELECTOR = (MobileBy.ID, 'field-1801')
    SEVERITY_LEVEL_SELECTOR2 = (MobileBy.XPATH, '//android.widget.ListView[@index="0"]/android.view.View['  # for Android 4
                                                '@index="3" and @content-desc[contains(., "Severity")]]/'
                                                'android.widget.Spinner[@index="2"]')
    CHOOSE_SEVERITY_LVL1 = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Severity 1"]')
    CHOOSE_SEVERITY_LVL2 = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Severity 2"]')
    CHOOSE_SEVERITY_LVL3 = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Severity 3"]')
    CHOOSE_SEVERITY_LVL4 = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Severity 4"]')
    CHOOSE_SEVERITY_LVL5 = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Severity 5"]')
    FINISHED_FIELD = (MobileBy.ACCESSIBILITY_ID, 'Finished')
    TIME_DATE = (MobileBy.ACCESSIBILITY_ID, 'Increase year')
    SET_BUTTON = (MobileBy.ID, 'android:id/button1')
    DESCRIPTION_FIELD = (MobileBy.XPATH, '//android.widget.ListView[1]/android.view.View[9]/android.view.View[2]'
                                         '/android.view.View[2]/android.view.View[1]/android.view.View[1]')
    CREATE_MAPPING_DATA = (MobileBy.XPATH, "//android.view.View[@content-desc[contains(., 'Create mapping data')]]")
    ADD_MEDIA_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Add media')
    EDIT_MAPPING_DATA = (MobileBy.XPATH, "//android.view.View[@content-desc[contains(., 'Edit mapping data')]]")
    SEQUENCE_ONLOAD_HEADER = (MobileBy.ACCESSIBILITY_ID, 'sequence_onload')
    SEQUENCE_ONLOAD_VALUE = (MobileBy.ACCESSIBILITY_ID, 'test on load')
    SEQUENCE_ONSAVE_HEADER = (MobileBy.ACCESSIBILITY_ID, 'sequence_onsave')
    SEQUENCE_ONSAVE_VALUE = (MobileBy.ACCESSIBILITY_ID, '(auto)')
    # SEQUENCE_ONSAVE_VALUE = (MobileBy.ACCESSIBILITY_ID, 'test on save')
    NEW_OPTION_LIST_HEADER = (MobileBy.ACCESSIBILITY_ID, 'New option list')
    # NEW_OPTION_LIST_HEADER = (MobileBy.XPATH, '//android.view.View[@content-desc="New option list"]')
    # NEW_OPTION_LIST_HEADER = (MobileBy.XPATH, '//android.widget.ListView/android.view.View'
    #                                           '[@content-desc[contains(., "New option list")]]/android.widget.Spinner')
    HEADER_ON_OPTION_LIST_PAGE = (MobileBy.ACCESSIBILITY_ID, 'New option list')
    OPTION_LIST_VALUE_1 = (MobileBy.ACCESSIBILITY_ID, '1')
    OPTION_LIST_VALUE_2 = (MobileBy.ACCESSIBILITY_ID, '2')
    OPTION_LIST_VALUE_3 = (MobileBy.ACCESSIBILITY_ID, '3')
    FIELD_TO_RESTORE_1_HEADER = (MobileBy.ACCESSIBILITY_ID, 'field to restore')
    FIELD_TO_RESTORE_1_VALUE = (MobileBy.XPATH, '//android.widget.EditText[@content-desc[contains(., "value for field 1")]]')
    # FIELD_TO_RESTORE_1_VALUE = (MobileBy.ACCESSIBILITY_ID, 'value for field 1')
    FIELD_TO_RESTORE_2_HEADER = (MobileBy.ACCESSIBILITY_ID, 'New email address')
    FIELD_TO_RESTORE_2_VALUE = (MobileBy.ACCESSIBILITY_ID, 'test@noggin.com')
    FIELD_TO_RESTORE_3_HEADER = (MobileBy.ACCESSIBILITY_ID, 'New website address')
    FIELD_TO_RESTORE_3_VALUE = (MobileBy.ACCESSIBILITY_ID, 'http://bitnoi.se/')
    CHOOSER_FIELD = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "New events chooser")]]')
    # PREVIOUSLY_CREATED_EVENT = (MobileBy.XPATH, '//android.view.View[@content-desc['
    #                                             'contains(., "Appium")]]')
    SUBFORM_FIELD_ADD_ROW = (MobileBy.ACCESSIBILITY_ID, 'Add row')
    NEW_EVENTS_CHOOSER_IN_SUB_FORM = (MobileBy.XPATH, '//android.view.View[@content-desc['
                                                      'contains(., "New events chooser inside sub form")]]')
    DELETE_SUB_EVENT_FROM_CHOOSER = (MobileBy.XPATH, '//android.widget.ListView/android.view.View[@index="8"]'
                                                     '/android.view.View[@index="1"]')
    # PREVIOUSLY_CREATED_EVENT_FOR_SUBFORM_CHOOSER = (MobileBy.XPATH, '//android.view.View[@content-desc['
    #                                                                 'contains(., "Test to create")]]')

    # headers
    FINISHED_HEADER = (MobileBy.ACCESSIBILITY_ID, 'Finished')
    LEADAGENCY_HEADER = (MobileBy.ACCESSIBILITY_ID, 'Lead agency')
    IMPACT_HEADER = (MobileBy.ACCESSIBILITY_ID, 'Impact')
    CAUSE_HEADER = (MobileBy.ACCESSIBILITY_ID, 'Cause')
    SITUATION_HEADER = (MobileBy.ACCESSIBILITY_ID, 'Situation')
    ISSUES_HEADER = (MobileBy.ACCESSIBILITY_ID, 'Issues')
    OBJECTIVES_HEADER = (MobileBy.ACCESSIBILITY_ID, 'Objectives')
    STRATEGIES_HEADER = (MobileBy.ACCESSIBILITY_ID, 'Strategies')
    TACTICS_HEADER = (MobileBy.ACCESSIBILITY_ID, 'Tactics')
    COMMUNICATIONS_HEADER = (MobileBy.ACCESSIBILITY_ID, 'Communications')
    RELATED_HEADER = (MobileBy.ACCESSIBILITY_ID, 'Related')
    MAPPING_HEADER = (MobileBy.ACCESSIBILITY_ID, 'Mapping')
    ACCESS_LEVELS_HEADER = (MobileBy.ACCESSIBILITY_ID, 'Access Levels')


class EventDetailsScreen:
    """A class for Event Details screen locators - screen with event details - after opening event."""
    EDIT_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Edit')
    DELETE_EVENT_BUTTON = (MobileBy.XPATH, "//android.widget.ListView[@index='2']"
                                           "//android.view.View[@index='2']"
                                           "//android.view.View[@content-desc[contains(., 'Delete event')]]")
    DELETE_CONFIRM_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Delete')
    NEW_SUB_EVENT = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "New sub event")]]')
    SET_AS_PRIMARY_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Set as primary")]]')
    EVENT_INFO_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Event info')


class Map:
    """A class for Map screen locators."""
    TOOL_BUTTON = (MobileBy.XPATH, "//android.widget.Spinner[@content-desc[contains(., 'Tool')]]")
    POINT_BUTTON = (MobileBy.XPATH, "//android.view.View[@content-desc[contains(., 'Point click to expand')]]")
    DEFAULT_BUTTON = (MobileBy.ACCESSIBILITY_ID, "Default")
    MAP_AREA_9 = (MobileBy.XPATH, "//android.widget.Image[@index='9']")
    MAP_AREA_3 = (MobileBy.XPATH, "//android.widget.Image[@index='3']")
    MAP_AREA_6 = (MobileBy.XPATH, "//android.widget.Image[@index='6']")
    LINE_BUTTON = (MobileBy.XPATH, "//android.view.View[@content-desc[contains(., 'Line')]]")
    CIRCLE_BUTTON = (MobileBy.XPATH, "//android.view.View[@content-desc[contains(., 'Circle')]]")
    POLYGON_BUTTON = (MobileBy.XPATH, "//android.view.View[@content-desc[contains(., 'Polygon')]]")
    SAVE_MAP_BUTTON = (MobileBy.ACCESSIBILITY_ID, "Save")
    SAVED_MAP_FOR_MOBILE = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "FOR MOBILE")]]')
    SAVED_MAP_ALL_ACTIVE_EVENTS = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "All active events")]]')
    SAVED_MAP_ALL_ASSETS = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "All assets")]]')
    SAVED_MAP_ALL_CONTACTS = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "All contacts")]]')
    SAVED_MAP_ALL_TASKS = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "All tasks")]]')
    DUPLICATED_GEOMETRY = (MobileBy.XPATH, '//android.widget.Image[@clickable="false"][last()]')


class PhotoScreen:
    """A class for Photo screen locators - screen after clicking into Photo button in Main Menu."""
    PHOTO_PAGE_HEADER = (MobileBy.ACCESSIBILITY_ID, 'Send a photo to OCA')
    GALLERY_BUTTON = (MobileBy.XPATH, '//android.view.View[2]/android.view.View[2]/android.view.View[1]')  # accessibility id won't work because it pinpoints only text
    TAKE_NEW_BUTTON = (MobileBy.XPATH, '//android.view.View[2]/android.view.View[3]/android.view.View[1]')  # accessibility id won't work because it pinpoints only text
    SEND_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Send')
    RESET_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Reset')
    DESCRIPTION_FIELD = (MobileBy.ACCESSIBILITY_ID, 'Description (optional)')


class VideoScreen:
    """A class for Video screen locators - screen after clicking into Photo button in Main Menu."""
    VIDEO_PAGE_HEADER = (MobileBy.ACCESSIBILITY_ID, 'Send a video to OCA')
    RECORD_NEW_BUTTON = (MobileBy.XPATH, '//android.view.View[2]/android.view.View[3]/android.view.View[1]')


class GalleryScreen:
    """A class for handling Gallery"""
    GALLERY_ELEMENT_1 = (MobileBy.XPATH, '//android.widget.GridView[1]/android.widget.FrameLayout[1]')
    GALLERY_ELEMENT_1_android7 = (MobileBy.XPATH, '//android.widget.RelativeLayout[1]/android.view.View[1]')
    GALLERY_ELEMENTS_android7 = (MobileBy.ID, 'com.android.documentsui:id/icon_mime_lg')  # list of elements
    # VIDEOS = (MobileBy.XPATH, '//android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.view.View[1]/*[1]')  # first child
    # VIDEOS = (MobileBy.ID, 'com.android.gallery3d:id/gl_root_view')
    # VIDEOS2 = (MobileBy.ID, 'com.sec.android.gallery3d:id/gl_root_view')
    # GALLERY_BUTTON_IN_SIDE_MENU = (MobileBy.XPATH, '//android.widget.TextView[@text="Videos"]')
    VIDEOS_BUTTON_IN_GALLERY = (MobileBy.XPATH, '//android.widget.TextView[@text="Videos"]')
    GALLERY_BUTTON_IN_SIDE_MENU = (MobileBy.XPATH, '//android.widget.TextView[@text="Gallery"]')
    RECENT_BUTTON_IN_SIDE_MENU = (MobileBy.XPATH, '//android.widget.TextView[@text="Recent"]')
    CAMERA_FOLDER = (MobileBy.XPATH, '//android.widget.TextView[@text="Camera"]')
    GALLERY_SHOW_ROOTS = (MobileBy.ACCESSIBILITY_ID, 'Show roots')  # for Android 5.1.1, 7.0 and 7.1
    GALLERY_SHOW_ROOTS_Android_4 = (MobileBy.ID, 'up')  # for Android 4.4.2


class SoundScreen:
    """A class for Sound screen locators - screen after clicking into Sound button in Main Menu."""
    SOUND_PAGE_HEADER = (MobileBy.ACCESSIBILITY_ID, 'Send a sound recording to OCA')
    RECORD_SOUND_BUTTON = (MobileBy.XPATH, '//android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]')  # android 6 - by ID is not working


class SoundRecorderScreen:
    """A class for Sound Recorder screen locators - screen after clicking into record sound button in Sound Page."""
    RECORD_SOUND_android_4 = (MobileBy.ID, 'com.android.soundrecorder:id/recordButton')  # android 4
    STOP_RECORDING_android_4 = (MobileBy.ID, 'com.android.soundrecorder:id/stopButton')  # android 4
    DONE_BUTTON_android_4 = (MobileBy.ID, 'com.android.soundrecorder:id/acceptButton')  # android 4
    RECORD_SOUND_android_5 = (MobileBy.ID, 'com.tct.soundrecorder:id/recordButton')  # android 5
    STOP_RECORDING_android_5 = (MobileBy.ID, 'com.tct.soundrecorder:id/wave_view')  # android 5  # to test
    # STOP_RECORDING_android_5 = (MobileBy.ACCESSIBILITY_ID, 'Pause record')  # android 5  # not working
    DONE_BUTTON_android_5 = (MobileBy.ACCESSIBILITY_ID, 'Save record')  # android 5
    RECORD_SOUND_android_6 = (MobileBy.ACCESSIBILITY_ID, 'Record')  # android 6
    RECORD_SOUND_android_6_version2 = (MobileBy.ID, 'com.android.soundrecorder:id/recordButton')  # android 6
    STOP_RECORDING_android_6 = (MobileBy.ACCESSIBILITY_ID, 'Stop')  # android 6
    DONE_BUTTON_android_6 = (MobileBy.ACCESSIBILITY_ID, 'Done')  # android 6, 7
    STOP_RECORDING_android_7 = (MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="Stop"]')  # android 7


class CameraScreen:
    """A class for handling Camera"""
    CAPTURE_BUTTON_ANDROID_4_and_5 = (MobileBy.ACCESSIBILITY_ID, 'Shutter')  # and Android 6
    CAPTURE_BUTTON_ANDROID_6 = (MobileBy.XPATH, '//GLButton[@text="Shutter"]')  # Android 7
    CAPTURE_BUTTON_ANDROID_6_version2 = (MobileBy.ACCESSIBILITY_ID, 'Shutter button')
    # CAPTURE_BUTTON_ANDROID_7 = (MobileBy.XPATH, '//GLViewGroup[3]/GLViewGroup[1]/GLButton[2]')
    RECORD_BUTTON_ANDROID_7 = (MobileBy.XPATH, '//GLButton[@text="Record"]')
    STOP_BUTTON_ANDROID_7 = (MobileBy.XPATH, '//GLButton[@text="Stop"]')
    CANCEL_PHOTO_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Review cancel')
    CAMERA_CHOOSER_ANDROID4 = (MobileBy.ID, 'com.android.camera2:id/btn_switch_camera')
    CAMERA_CHOOSER_ANDROID5 = (MobileBy.ID, 'com.tct.camera:id/onscreen_camera_picker')
    CAMERA_CHOOSER_ANDROID6 = (MobileBy.ACCESSIBILITY_ID, 'Switch camera')
    CAMERA_CHOOSER_ANDROID_6 = (MobileBy.ACCESSIBILITY_ID, 'Front and back camera switch')  # also Android 4, 5 emulator
    CAMERA_CHOOSER_ANDROID7 = (MobileBy.XPATH, '//SideQuickSetting[1]/SideQuickSettingItem[3]/ItemDataButton[1]/GLButton[1]')
    RETAKE_ANDROID_4 = (MobileBy.ACCESSIBILITY_ID, 'Review retake')
    RETAKE_ANDROID_5 = (MobileBy.ID, 'com.tct.camera:id/btn_retake')
    RETAKE_ANDROID_6 = (MobileBy.ID, 'com.sec.android.app.camera:id/retry')
    RETAKE_ANDROID_6_version2 = (MobileBy.ID, 'com.android.camera:id/btn_retake')
    USE_PHOTO_ANDROID4 = (MobileBy.ACCESSIBILITY_ID, 'Review done')
    USE_PHOTO_ANDROID5 = (MobileBy.ACCESSIBILITY_ID, 'OK')  # com.tct.camera:id/btn_done
    USE_PHOTO_ANDROID7 = (MobileBy.ID, 'com.sec.android.app.camera:id/okay')  # Android 7
    USE_PHOTO_ANDROID6 = (MobileBy.ID, 'com.android.camera:id/btn_done')  # Android 6


class ContactsScreen:
    """A class for handling Contacts screen"""
    FIRST_NAME = (MobileBy.ID, 'first name')
    FIRST_NAME2 = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="First name"]')
    CONTACT_TYPE_PERSON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Person")]]')
    CONTACT_TYPE_WITH_ON_LOAD_SEQUENCE = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "contact_with_on_load_sequence")]]')
    CONTACT_TYPE_WITH_VISIBILITY_RULES = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "contact_with_visibility_rules")]]')
    DELETED_CONTACT = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "delete")]]')
    IMPORTED_CONTACT_FIRST_NAME_VALUE = (MobileBy.ACCESSIBILITY_ID, 'Communication')
    SEQUENCE_ONSAVE_VALUE = (MobileBy.ACCESSIBILITY_ID, 'test on save')
    NEW_CONTACT_GROUP_TYPE_GROUP = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Group")]]')
    CONTACTS_GROUP = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Contacts")]]')
    USERS_GROUP = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Users")]]')
    MAILING_LIST_GROUP = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Mailing list")]]')
    NEW_CONTACT_GROUP_WITH_ON_LOAD_SEQUENCE = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "contact_group_with_on_load_sequence")]]')
    OFFLINE_CONTACTS_GROUP = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "offline_contact_group")]]')


class TasksScreen:
    """A class for handling New Task screen"""
    TITLE = (MobileBy.ID, 'title')
    TITLE2 = (MobileBy.XPATH, '//android.view.View[1]/android.widget.EditText[1]')
    ASSIGNED = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Assigned")]]')
    ADD_CONTACTS_AND_GROUPS = (MobileBy.XPATH, '//android.widget.Button[@content-desc[contains'
                                               '(., "Add contacts and groups")]]')
    ADD_RESOURCE_STRUCTURE_NODES = (MobileBy.XPATH, '//android.widget.Button[@content-desc[contains(., "Add Resource structure nodes")]]')
    ADD_RESOURCE_STRUCTURE_NODES2 = (MobileBy.XPATH, '//android.view.View[@name[contains(., "Add Resource structure nodes")]]')
    ADD_RESOURCE_ASSIGNMENTS = (MobileBy.XPATH, '//android.widget.Button[@content-desc[contains'
                                                '(., "Add Resource assignments")]]')
    CHOOSE_USERS = (MobileBy.ACCESSIBILITY_ID, 'Users')
    CHOOSE_CONTACTS = (MobileBy.ACCESSIBILITY_ID, 'Contacts')
    START_DATE = (MobileBy.ID, 'start date')
    START_DATE2 = (MobileBy.XPATH, '//android.view.View[2][@content-desc="Start Date"]')
    CREATED_TASK_WITH_APPROVAL = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Report approval")]]')
    MY_TASKS = (MobileBy.ACCESSIBILITY_ID, 'My Tasks')
    ALL_TASKS = (MobileBy.ACCESSIBILITY_ID, 'All Tasks')
    COMPLETED_TASKS = (MobileBy.ACCESSIBILITY_ID, 'Completed Tasks')
    INCOMPLETE_TASKS = (MobileBy.XPATH, 'Incomplete Tasks')
    # ACTION_REQUIRED_TASKS = (MobileBy.XPATH, 'Action Required Tasks')
    ACTION_REQUIRED_TASKS = (MobileBy.ACCESSIBILITY_ID, 'Action Required Tasks')


class ReportsScreen:
    """A class for handling Reports screen"""
    LODGING_AGENCY_PICKER = (MobileBy.ID, 'field-1201')
    LODGING_AGENCY_PICKER2 = (MobileBy.XPATH, '//android.view.View[4]/android.widget.Spinner[1]')
    LODGING_AGENCY = (MobileBy.XPATH, '//android.widget.CheckedTextView[2]')
    PUBLISH_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Publish')
    PUBLISH_BUTTON2 = (MobileBy.XPATH, '//android.view.View[@content-desc="Publish"]')
    CREATED_REPORT_WITH_ALL_FIELDS = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Large")]]')
    CREATED_REPORT_WITH_CHOOSER_FIELDS = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "chooser_fields")]]')
    CREATED_REPORT_WITH_ASSIGNED_QUESTION = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "assigned_question")]]')
    REPORT_TYPE_WITH_ALL_FIELDS = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "report_for_tests")]]')
    REPORT_TYPE_WITH_CHOOSER_FIELDS = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "report_with_chooser_fields")]]')
    REPORT_TYPE_WITH_ON_CREATE_APPROVAL_WORKFLOW = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "report_with_on_create_approval")]]')
    REPORT_TYPE_WITH_ON_LOAD_SEQUENCE = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "report_with_on_load_sequence")]]')
    REPORT_TYPE_WITH_VISIBILITY_RULES = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "report_with_visibility_rules")]]')
    REPORT_TYPE_WITH_ASSIGNED_QUESTION = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "report_with_assigned_question")]]')
    MEDIA_RELEASE_FIELD = (MobileBy.XPATH, '//android.view.View[@content-desc="Media release Editor toolbars "]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[1]')


class LogsScreen:
    """A class for handling Logs screen"""
    LODGING_AGENCY_PICKER = (MobileBy.ID, 'field-201')
    LODGING_AGENCY_PICKER2 = (MobileBy.XPATH, '//android.view.View[2]/android.widget.Spinner[1]')
    ENTRY_FIELD = (MobileBy.XPATH, '//android.view.View[@content-desc="Rich Text Editor, entry"]/android.view.View[2]')
    CREATED_LOG_WITH_ALL_FIELDS = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "all fields")]]')
    LOG_TYPE_WITH_ALL_FIELDS = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "log_with_all_fields")]]')
    LOG_TYPE_WITH_CHOOSER_FIELDS = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "log_with_chooser_fields")]]')
    LOG_TYPE_WITH_ON_LOAD_SEQUENCE = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "log_with_on_load_sequence")]]')
    LOG_TYPE_WITH_VISIBILITY_RULES = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "log_with_visibility_rules")]]')


class SentScreen:
    """A class for handling Sent screen"""
    SEARCH = EventsScreen.SEARCH_FIELD
    SENT_COMMUNICATIONS_EMAIL = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Short message, Email")]]')


class ComposeScreen:
    """A class for handling Compose screen"""
    ADD_RECIPIENTS_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Add recipients")]]')
    MESSAGE_EMAIL = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Email")]]')
    EMAIL_SUBJECT_FIELD = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="Subject"]')
    EMAIL_TEXT_FIELD = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "emailBody")]]'
                                        '/android.view.View/android.view.View/android.view.View'
                                        '/android.view.View')  # android 4,5
    EMAIL_TEXT_FIELD2 = (MobileBy.XPATH, '//android.view.View[@content-desc="Rich Text Editor, emailBody"]//android.view.View[@clickable="true"]')  # android 6
    EMAIL_TEXT_FIELD3 = (MobileBy.XPATH, '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[4]/android.view.View[2]/android.view.View[1]/android.view.View[1]')  # android 7
    MESSAGE_SMS = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "SMS")]]')
    SMS_TEXT_FIELD = (MobileBy.CLASS_NAME, 'android.widget.EditText')
    MESSAGE_VOICE = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Voice")]]')
    VOICE_TEXT_FIELD = (MobileBy.CLASS_NAME, 'android.widget.EditText')
    TEXT_TO_SPEECH_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc="Text-to-speech"]')
    MESSAGE_FAX = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Fax")]]')
    FAX_DOCUMENT_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Fax document")] '
                                           'and @clickable="true"]')
    COMMS_DOCUMENTS_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc="Comms documents "]')
    FILES_LIST = (MobileBy.CLASS_NAME, 'android.widget.ListView')
    FAX_PDF_FILE = (MobileBy.ACCESSIBILITY_ID, 'OCA Generic Escalation Fax.pdf')
    FAX_OK_BUTTON = (MobileBy.ID, 'faxOK')
    REQUIRE_ACKNOWLEDGMENT = (MobileBy.XPATH, '//android.view.View[@content-desc'
                                              '[contains(., "Require acknowledgment")]]')
    REPLY_TRACKING = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Reply tracking")]]')
    READ_ACCESS_LEVEL = (MobileBy.XPATH, '')
    ADD_CONTACTS_AND_GROUPS = (MobileBy.XPATH, '//android.widget.Button[@content-desc'
                                               '[contains(., "Add contacts and groups")]]')
    ADD_RESOURCES_STRUCTURE_NODES = (MobileBy.XPATH, '//android.widget.Button[@content-desc'
                                                     '[contains(., "Add Resource structure ")]]')
    CONTACTS_ARROW = (MobileBy.XPATH, '//android.view.View[@content-desc[contains'
                                      '(., "Contacts")]]/android.view.View[@index="2"]')
    USERS_ARROW = (MobileBy.XPATH, '//android.view.View[@content-desc[contains'
                                   '(., "Users")]]/android.view.View[@index="2"]')
    MAILING_LIST_UNSUBSCRIBES_ARROW = (MobileBy.XPATH, '//android.view.View[@content-desc'
                                                       '[contains(., "Mailing list unsubscribes ")]]'
                                                       '/android.view.View[@index="2"]')
    CONTACT_FOR_APPIUM_TESTS = (MobileBy.XPATH, '//android.view.View[@content-desc="A_CONTACT_FOR_APPIUM_TESTS"]')
    ALERT_SEND_BUTTON_by_id = (MobileBy.ID, 'messageSend')
    ALERT_SEND_BUTTON_by_name = (MobileBy.XPATH, '//android.widget.Button[@content-desc="Send"]')  # for Android < 4


class RisksScreen:
    """A class for handling Risks screen"""
    CHOOSE_STATUS_IMPLEMENTED = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Implemented"]')
    CREATE_RISK_REGISTER = (MobileBy.ACCESSIBILITY_ID, 'Create risk register')
    # PREVIOUSLY_CREATED_RISK_REGISTER = (MobileBy.XPATH, '//android.view.View[2]/'
    #                                                     'android.widget.ListView[1]/android.view.View[1]')
    PREVIOUSLY_CREATED_RISK_REGISTER = (MobileBy.ACCESSIBILITY_ID, 'Appium - new risk register')
    ADD_NEW_CONTEXT = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Add new context")]]')
    VIEW_BUTTON = CommonScreen.SPINNER_ON_THE_LEFT
    NAME_FIELD_FOR_CONTEXT = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="Name"]')
    FIRST_CONTEXT_ON_THE_LIST = (MobileBy.XPATH, '//android.widget.ListView[1]/android.view.View[1]'
                                                 '/android.view.View[2]')
    RISK_TYPE_FOR_TEST = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "new_risk_type")]]')
    RISK_TYPE_WITH_OPTION_LIST = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "risk_with_option_list")]]')


class AssetsScreen:
    """A class for handling Assets screen"""
    CREATED_MAP_ASSET = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Map")]]')
    CREATED_ASSET_WITH_NAME_BALLART = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Ballarat")]]')
    ASSET_TYPE_WITH_MAX_NUMBER_OF_FIELDS = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "asset_with_max_number_of_fields")]]')
    ASSET_TYPE_WITH_VISIBILITY_RULES = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "asset_with_visibility_rules")]]')
    ASSET_TYPE_WITH_OPTION_LIST = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "asset_with_option_list")]]')
    SAVE_OPTION_LIST = (MobileBy.XPATH, '//android.widget.Button[@content-desc[contains(., "Save")]]')
    NEW_DATE_OPTIONAL_TIME2 = (MobileBy.XPATH, '//android.view.View[@content-desc="New date & optional time2"]')
    OPTION_LIST_READ_ONLY_IOS = (MobileBy.XPATH, '//android.view.View[@content-desc="Is Read only ?"]')
    NEW_PHONE_NUMBER = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="+61212345111" and @enabled="true"]')
    NEW_FAX_NUMBER = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="+61212345222" and @enabled="true"]')
    NEW_EMAIL_ADDRESS = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="testbitnoise@gmail.com" and @enabled="true"]')
    NEW_WEBSITE_ADDRESS = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="http://www.google.com" and @enabled="true"]')
    NEW_SINGLE_LINE_TEXT = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="test_appium_single_line" and @enabled="true"]')
    NEW_MULTI_LINE_TEXT = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="test_appium_multi_line" and @enabled="true"]')
    NEW_PHONE_NUMBER_DISABLED = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="+61212345111" and @enabled="false"]')
    NEW_FAX_NUMBER_DISABLED = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="+61212345222" and @enabled="false"]')
    NEW_EMAIL_ADDRESS_DISABLED = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="testbitnoise@gmail.com" and @enabled="false"]')
    NEW_WEBSITE_ADDRESS_DISABLED = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="http://www.google.com" and @enabled="false"]')
    NEW_SINGLE_LINE_TEXT_DISABLED = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="test_appium_single_line" and @enabled="false"]')
    NEW_MULTI_LINE_TEXT_DISABLED = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="test_appium_multi_line" and @enabled="false"]')
    NEW_PHONE_NUMBER2 = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="+61212345333" and @enabled="true"]')
    NEW_FAX_NUMBER2 = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="+61212345444" and @enabled="true"]')
    NEW_EMAIL_ADDRESS2 = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="testbit@wp.pl" and @enabled="true"]')
    NEW_WEBSITE_ADDRESS2 = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="http://www.bitnoi.se" and @enabled="true"]')
    NEW_SINGLE_LINE_TEXT2 = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="test_appium_single_line2" and @enabled="true"]')
    NEW_MULTI_LINE_TEXT2 = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="test_appium_multi_line2" and @enabled="true"]')


