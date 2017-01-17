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
    SETTINGS_CONTACT_IDENTIFIER_FIELD = (MobileBy.CLASS_NAME, 'android.widget.EditText')
    SETTINGS_ALERT_APP_HAS_BEEN_ACTIVATED = (MobileBy.ACCESSIBILITY_ID, 'App has been activated.')


class LoginScreen:
    """A class for login screen locators - screen after clicking into LOGIN."""
    TEXTFIELD_USERNAME = (MobileBy.ACCESSIBILITY_ID, 'Username')
    TEXTFIELD_PASSWORD = (MobileBy.XPATH, '//android.widget.EditText[@index="3"]')
    TEXTFIELD_DOMAIN = (MobileBy.XPATH, '//android.widget.EditText[@index="5"]')
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
    LOCATION_STATUS = (MobileBy.ACCESSIBILITY_ID, 'a few seconds ago')


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

    # creating and editing Events
    MORE_BUTTON = (MobileBy.XPATH, '//android.widget.Spinner[@content-desc[contains(., "More")]]')
    NEW_EVENT_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "New event")]]')

    # previously created event
    CREATED_EVENT_1 = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Test Appium Android")]]')
    CREATED_EVENT_2 = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., " second event")]]')
    CREATED_EVENT_3 = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., " to create sub event")]]')

    CLEAR_PRIMARY_EVENT_BUTTON = (MobileBy.XPATH, '//android.view.View[@content-desc="Clear primary event"]')
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
    SEVERITY_LEVEL_SELECTOR = (MobileBy.XPATH, '//android.widget.ListView[@index="0"]/android.view.View['
                                               '@index="3" and @content-desc[contains(., "Severity")]]/'
                                               'android.widget.Spinner[@index="2"]')
    CHOOSE_SEVERITY_LVL1 = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Severity 1"]')
    CHOOSE_SEVERITY_LVL2 = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Severity 2"]')
    CHOOSE_SEVERITY_LVL3 = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Severity 3"]')
    CHOOSE_SEVERITY_LVL4 = (MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Severity 4"]')
    FINISHED_FIELD = (MobileBy.ACCESSIBILITY_ID, 'Finished')
    TIME_DATE = (MobileBy.ACCESSIBILITY_ID, 'Increase year')
    SET_BUTTON = (MobileBy.ID, 'android:id/button1')
    DESCRIPTION_FIELD = (MobileBy.XPATH,
                         "//android.widget.ListView[@index='0']"
                         "//android.view.View[@index='8' and @content-desc[contains(., 'Description')]]"
                         "//android.view.View[@index='1']"
                         "//android.view.View[@index='1']"
                         "//android.view.View[@index='0']"
                         "//android.view.View[@index='0']"
                         "//android.view.View[@index='0' and @clickable='true']")
    CREATE_MAPPING_DATA = (MobileBy.XPATH, "//android.view.View[@content-desc[contains(., 'Create mapping data')]]")
    ADD_MEDIA_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Add media')
    EDIT_MAPPING_DATA = (MobileBy.XPATH, "//android.view.View[@content-desc[contains(., 'Edit mapping data')]]")
    SEQUENCE_ONLOAD_HEADER = (MobileBy.ACCESSIBILITY_ID, 'sequence_onload')
    SEQUENCE_ONLOAD_VALUE = (MobileBy.ACCESSIBILITY_ID, 'test on load')
    SEQUENCE_ONSAVE_HEADER = (MobileBy.ACCESSIBILITY_ID, 'sequence_onsave')
    SEQUENCE_ONSAVE_VALUE = (MobileBy.ACCESSIBILITY_ID, '(auto)')
    NEW_OPTION_LIST_HEADER = (MobileBy.XPATH, '//android.widget.ListView/android.view.View'
                                              '[@content-desc[contains(., "New option list")]]/android.widget.Spinner')
    HEADER_ON_OPTION_LIST_PAGE = (MobileBy.ACCESSIBILITY_ID, 'New option list')
    OPTION_LIST_VALUE_1 = (MobileBy.ACCESSIBILITY_ID, '1')
    OPTION_LIST_VALUE_2 = (MobileBy.ACCESSIBILITY_ID, '2')
    OPTION_LIST_VALUE_3 = (MobileBy.ACCESSIBILITY_ID, '3')
    FIELD_TO_RESTORE_1_HEADER = (MobileBy.ACCESSIBILITY_ID, 'field to restore')
    FIELD_TO_RESTORE_1_VALUE = (MobileBy.ACCESSIBILITY_ID, 'value for field 1')
    FIELD_TO_RESTORE_2_HEADER = (MobileBy.ACCESSIBILITY_ID, 'New email address')
    FIELD_TO_RESTORE_2_VALUE = (MobileBy.ACCESSIBILITY_ID, 'test@noggin.com')
    CHOOSER_FIELD = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "New events chooser")]]')
    PREVIOUSLY_CREATED_EVENT_FOR_CHOOSER = (MobileBy.XPATH, '//android.view.View[@content-desc['
                                                            'contains(., "Test Appium Android")]]')
    SUBFORM_FIELD_ADD_ROW = (MobileBy.ACCESSIBILITY_ID, 'Add row')
    NEW_EVENTS_CHOOSER_IN_SUB_FORM = (MobileBy.XPATH, '//android.view.View[@content-desc['
                                                      'contains(., "New events chooser inside sub form")]]')
    DELETE_SUB_EVENT_FROM_CHOOSER = (MobileBy.XPATH, '//android.widget.ListView/android.view.View[@index="8"]'
                                                     '/android.view.View[@index="1"]')
    PREVIOUSLY_CREATED_EVENT_FOR_SUBFORM_CHOOSER = (MobileBy.XPATH, '//android.view.View[@content-desc['
                                                                    'contains(., "Test Android to create")]]')
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
    STOP_RECORDING_android_6 = (MobileBy.ACCESSIBILITY_ID, 'Stop')  # android 6
    DONE_BUTTON_android_6 = (MobileBy.ACCESSIBILITY_ID, 'Done')  # android 6


class CameraScreen:
    """A class for handling Camera"""
    CAPTURE_BUTTON_ANDROID_4_and_5 = (MobileBy.ACCESSIBILITY_ID, 'Shutter')
    CAPTURE_BUTTON_ANDROID_6 = (MobileBy.XPATH, '//GLButton[@text="Shutter"]')
    CANCEL_PHOTO_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Review cancel')
    CAMERA_CHOOSER_ANDROID4 = (MobileBy.ID, 'com.android.camera2:id/btn_switch_camera')
    CAMERA_CHOOSER = (MobileBy.ACCESSIBILITY_ID, 'Switch camera')  # for android 6
    CAMERA_CHOOSER2 = (MobileBy.ID, 'com.tct.camera:id/onscreen_camera_picker')
    RETAKE_ANDROID_4 = (MobileBy.ACCESSIBILITY_ID, 'Review retake')
    RETAKE_ANDROID_5 = (MobileBy.ID, 'com.tct.camera:id/btn_retake')
    RETAKE_ANDROID_6 = (MobileBy.ID, 'com.sec.android.app.camera:id/retry')
    USE_PHOTO_ANDROID4 = (MobileBy.ACCESSIBILITY_ID, 'Review done')
    USE_PHOTO_ANDROID5 = (MobileBy.ACCESSIBILITY_ID, 'OK')  # com.tct.camera:id/btn_done
    USE_PHOTO_ANDROID6 = (MobileBy.ID, 'com.sec.android.app.camera:id/okay')


class RisksScreen:
    """A class for handling Risks screen"""
    CREATE_RISK_REGISTER = (MobileBy.ACCESSIBILITY_ID, 'Create risk register')


class RiskRegisterEditScreen:
    """A class for handling Risk Register edit screen"""
    RISK_REGISTER_NAME = (MobileBy.XPATH, '//android.view.View[1]/android.widget.EditText[1]')


class NewContactScreen:
    """A class for handling New Contact screen"""
    FIRST_NAME = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="First name"]')


class NewTaskScreen:
    """A class for handling New Task screen"""
    TITLE = (MobileBy.XPATH, '//android.view.View[1]/android.widget.EditText[1]')
    ASSIGNED = (MobileBy.XPATH, '//android.view.View[@content-desc[contains(., "Assigned")]]')
    ADD_CONTACTS_AND_GROUPS = (MobileBy.XPATH, '//android.widget.Button[@content-desc[contains'
                                               '(., "Add contacts and groups")]]')
    ADD_RESOURCE_STRUCTURE_NODES = (MobileBy.XPATH, '//android.widget.Button[@content-desc[contains'
                                                    '(., "Add Resource structure nodes")]]')
    ADD_RESOURCE_ASSIGNMENTS = (MobileBy.XPATH, '//android.widget.Button[@content-desc[contains'
                                                '(., "Add Resource assignments")]]')
    CHOOSE_USERS = (MobileBy.ACCESSIBILITY_ID, 'Users')
    CHOOSE_CONTACTS = (MobileBy.ACCESSIBILITY_ID, 'Contacts')
    START_DATE = (MobileBy.XPATH, '//android.view.View[2][@content-desc="Start Date"]')


class NewReportScreen:
    """A class for handling New Report screen"""
    LODGING_AGENCY_PICKER = (MobileBy.XPATH, '//android.view.View[4]/android.widget.Spinner[1]')
    LODGING_AGENCY = (MobileBy.XPATH, '//android.widget.CheckedTextView[2]')
    PUBLISH_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Publish')


class NewAssetScreen:
    """A class for handling New Asset screen"""


class NewLogScreen:
    """A class for handling New Log screen"""
    LODGING_AGENCY_PICKER = (MobileBy.XPATH, '//android.view.View[2]/android.widget.Spinner[1]')
    ENTRY_FIELD = (MobileBy.XPATH, '//android.view.View[1]/android.view.View[1]/android.view.View'
                                   '[@focusable="true" and @clickable="true" and @scrollable="false"]')


class CommonScreen:
    """A class for handling Common buttons on different screen"""
    SAVE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Save')
    CANCEL_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Cancel')
    CANCEL_BUTTON_by_index = (MobileBy.XPATH, '//android.view.View[2]/android.widget.Button')
    OK_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Ok')
    WEB_VIEW = (MobileBy.XPATH, '//android.webkit.WebView[@scrollable="true"]')


class Android:
    """A class for handling Android device for example alerts"""

    # Android alerts
    ANDROID_ALLOW = (MobileBy.ID, 'com.android.packageinstaller:id/permission_allow_button')
    ANDROID_DENY = (MobileBy.ID, 'com.android.packageinstaller:id/permission_deny_button')

    # Set date and time
    ANDROID_SET_BUTTON = (MobileBy.ID, 'android:id/button1')
    ANDROID_CANCEL_BUTTON = (MobileBy.ID, 'android:id/button2')
    ANDROID_CLEAR_BUTTON = (MobileBy.ID, 'android:id/button3')
