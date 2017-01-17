# from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class TopBar:
    """A class for top bar locators."""
    HAMBURGER_FOR_MAIN_MENU_ios = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]'
                                                   '/UIAWebView[1]/UIALink[3]/UIAStaticText[1]')


class WelcomeScreen:
    """A class for welcome screen locators - first screen after lunching the app."""
    LOCATION_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "LOCATION")]]')
    MY_MESSAGES_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "MY MESSAGES")]]')
    PHOTO_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "PHOTO")]]')
    VIDEO_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "VIDEO")]]')
    SOUND_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "SOUND")]]')
    SETTINGS_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "SETTINGS")]]')
    ABOUT_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "ABOUT")]]')
    LOGIN_BUTTON_ios = (MobileBy.XPATH, '//UIAWebView/UIALink[@name[contains(., "LOGIN")]]')
    LOGIN_BUTTON_by_index_ios = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[1]'
                                                 '/UIAScrollView[2]/UIAWebView[1]/UIALink[9]'
                                                 '[@name[contains(., "LOGIN")]]')
    SETTINGS_CONTACT_IDENTIFIER_FIELD_ios = (MobileBy.CLASS_NAME, 'UIATextField')
    SETTINGS_ALERT_APP_HAS_BEEN_ACTIVATED_ios = (MobileBy.XPATH, '//UIAStaticText[@name="App has been activated."]')
    SETTINGS_OK_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name="Ok"]')


class LoginScreen:
    """A class for login screen locators - screen after clicking into LOGIN."""
    TEXTFIELD_USERNAME_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIATextField[1]')
    TEXTFIELD_PASSWORD_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIASecureTextField[1]')
    TEXTFIELD_DOMAIN_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIATextField[2]')
    SUBMIT_BUTTON_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAButton[@name="Submit"]')
    # SUBMIT_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Submit')  # not working

    # Notification alert: "OCA now supports sending 'App Messages' to your device as notifications."
    NOTIFICATION_ABOUT_SENDING_MESSAGES_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name[contains(., '
                                                               '"OCA now supports ")]]')

    # "No" button for sending notifications on iOS
    NO_FOR_SENDING_NOTIFICATIONS_ON_ios = (MobileBy.XPATH, '//UIAWebView/UIALink[@name="No"]')

    # ACCEPT_BUTTON on Terms and Conditions"
    ACCEPT_BUTTON_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAButton[@name="Accept"]')

    # alert message with word "Invalid"
    ALERT_MSG_INVALID_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name="Invalid username and/or password"]')

    # alert message with "Your temporary account has been expired"

    ALERT_MSG_EXPIRED_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name[contains'
                                             '(., "Your temporary account has been expired")]]')

    # alert message with "The password for the current user is about to expire"

    ALERT_MSG_WILL_EXPIRE_ios = (MobileBy.XPATH, '//UIAStaticText[@name[contains('
                                                 '., "The password for the current user is about to expire")]]')

    # alert message with word "inactive"
    ALERT_MSG_SUSPENDED_ios = (MobileBy.XPATH, '//UIAWebView/UIAStaticText['
                                               '@name[contains(., "Your account is currently inactive")]]')
    # OK button on alert messages"
    OK_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name="Ok"]')


class MainMenuScreen(WelcomeScreen):
    """A class for main menu screen locators - first screen after correct login into the app."""
    ACTIVATE_WORKFLOW_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "ACTIVATE WORKFLOW")]]')
    CREATE_CONTACT_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "CREATE CONTACT")]]')
    CREATE_TASK_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "CREATE A TASK")]]')
    CREATE_REPORT_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "CREATE A REPORT")]]')
    WEBSITE_LINK_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "WEBSITE LINK")]]')
    INCIDENT_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "INCIDENT")]]')
    CREATE_ASSETS_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "CREATE ASSETS")]]')
    CREATE_LOG_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "CREATE A LOG")]]')
    RISKS_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "RISKS")]]')
    EVENTS_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "EVENTS")]]')
    LOGS_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "LOGS")]]')
    REPORTS_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "REPORTS")]]')
    MAP_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "MAP")]]')
    ASSETS_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "ASSETS")]]')
    INBOX_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "INBOX")]]')
    COMPOSE_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "COMPOSE")]]')
    SENT_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "SENT")]]')
    TASKS_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "TASKS")]]')
    DOCUMENTS_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "DOCUMENTS")]]')
    CONTACTS_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "CONTACTS")]]')
    ALLOCATE_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "ALLOCATE")]]')
    ACTIVATE_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "ACTIVATE")]]')
    OFFLINE_SYNC_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "OFFLINE SYNC")]]')
    LOGOUT_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "LOGOUT")]]')

    ALERT_ACTIVATE_BUTTON_ios = (MobileBy.XPATH, '//UIALink/UIAStaticText[@name="Activate"]')
    ALERT_CANCEL_BUTTON_ios = (MobileBy.XPATH, '//UIALink/UIAStaticText[@name="Cancel"]')
    ALERT_WORKFLOW_ACTIVATED_ios = (MobileBy.XPATH, '//UIAStaticText[@name="Workflow activated"]')


class LocationScreen:
    """A class for Location screen locators - screen after clicking into Location button in Main Menu."""
    SEND_ONCE_NOW_ios = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Send once now")]]')
    SEND_EVERY_SPINNER_ios = (MobileBy.XPATH, '//UIAWebView/UIAElement[@name="Send every"]')
    CHOOSE_5_MINUTES_OPTION_iPad = (MobileBy.XPATH, '//UIAWindow/UIAPopover/UIATableView/UIATableCell[2]')
    ASSERT_5_MINUTES_OPTION_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name="5 minutes"]')
    FOR_THE_NEXT_SPINNER_ios = (MobileBy.XPATH, '//UIAWebView/UIAElement[@name="For the next"]')
    CHOOSE_1_HOUR_OPTION_iPad = (MobileBy.XPATH, '//UIAWindow/UIAPopover/UIATableView/UIATableCell[3]')
    ASSERT_1_HOUR_OPTION_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name="1 hour"]')
    START_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Start")]]')
    LOCATION_PAGE_HEADER_ios = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Your location was last sent")]]')
    LOCATION_STATUS_ios = (MobileBy.XPATH, "//UIAStaticText[@name[contains(., 'few seconds ago')]]")


class EventsScreen:
    """A class for Events screen locators - screen after clicking into Events button in Main Menu."""
    EVENTS_HEADER_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name="Events"]')

    # filtering events by Type
    ANY_TYPE_EXPAND_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "Any Type click to expand")]]')
    CHOOSE_TYPE_INCIDENT_ios = (MobileBy.XPATH, '//UIAStaticText[@name="Incident"]')
    INCIDENT_TYPE_EXPAND_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Incident click to expand")]]')
    CHOOSE_TYPE_ANY_ios = (MobileBy.XPATH, '//UIAStaticText[@name="Any Type"]')

    # filtering events by Status
    ANY_STATUS_EXPAND_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Any Status click to expand")]]')
    CHOOSE_ACTIVE_STATUS_ios = (MobileBy.XPATH, '//UIALink[@name="Active"]')
    ACTIVE_STATUS_EXPAND_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Active click to expand")]]')
    CHOOSE_INACTIVE_STATUS_ios = (MobileBy.XPATH, '//UIALink[@name="Inactive"]')
    INACTIVE_STATUS_EXPAND_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Inactive click to expand")]]')
    CHOOSE_DRAFT_STATUS_ios = (MobileBy.XPATH, '//UIALink[@name="Draft"]')
    DRAFT_STATUS_EXPAND_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Draft click to expand")]]')
    CHOOSE_ANY_STATUS_ios = (MobileBy.XPATH, '//UIALink[@name="Any Status"]')

    # filtering events using search field
    SEARCH_FIELD_ios = (MobileBy.XPATH, '//UIATextField[@name="Search:"]')

    # creating and editing Events
    MORE_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name[contains(., "More")]]')
    NEW_EVENT_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "New event")]]')

    # previously created event
    CREATED_EVENT_1_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Test Appium iOS")]]')
    CREATED_EVENT_2_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Test Appium iOS - second event")]]')
    CREATED_EVENT_3_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "iOS to create sub")]]')
    CLEAR_PRIMARY_EVENT_BUTTON_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name'
                                                      '[contains(., "Clear primary event")]]')
    NOTIFICATION_PRIMARY_EVENT_CLEARED_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText['
                                                              '@name="Primary event cleared"]')


class TypesOfEventsScreen:
    """A class for Type of Events screen locators - first screen after creating new event with types of events."""
    INCIDENT_TYPE_OF_EVENT_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "Incident")]]')
    EVENT_FOR_ON_LOAD_SAVE_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "event_for_on_load")]]')
    EVENT_FOR_CHOOSER_FIELDS_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "event_for_chooser")]]')


class EventEditScreen:
    """A class for Edit Events screen locators - screen after opening edit mode of event or creating a new one."""
    NAME_FIELD_ios = (MobileBy.XPATH, '//UIAScrollView/UIAWebView/UIATextField[@name="Name"]')
    NAME_FIELD_by_index_ios = (MobileBy.XPATH, '//UIAScrollView/UIAWebView/UIATextField[1]')
    SEVERITY_LEVEL_SELECTOR_ios = (MobileBy.XPATH, '//UIAElement[2]')
    CHOOSE_SEVERITY_LVL1_iPad = (MobileBy.XPATH, '//UIATableCell[@name="Severity 1"]')
    CHOOSE_SEVERITY_LVL1_iPhone = (MobileBy.XPATH, '//UIAPicker/UIAPickerWheel[@value="Severity 1"]')
    CHOOSE_SEVERITY_LVL2_iPad = (MobileBy.XPATH, '//UIATableCell[@name="Severity 2"]')
    CHOOSE_SEVERITY_LVL2_iPhone = (MobileBy.XPATH, '//UIAPicker/UIAPickerWheel[@value="Severity 2"]')
    CHOOSE_SEVERITY_LVL3_iPad = (MobileBy.XPATH, '//UIATableCell[@name="Severity 3"]')
    CHOOSE_SEVERITY_LVL3_iPhone = (MobileBy.XPATH, '//UIAPicker/UIAPickerWheel[@value="Severity 3"]')
    CHOOSE_SEVERITY_LVL4_iPad = (MobileBy.XPATH, '//UIATableCell[@name="Severity 4"]')
    CHOOSE_SEVERITY_LVL4_iPhone = (MobileBy.XPATH, '//UIAPicker/UIAPickerWheel[@value="Severity 4"]')
    SEVERITY_PICKER_ios = (MobileBy.XPATH, '//UIAApplication/UIAWindow/UIAPicker/UIAPickerWheel')
    FINISHED_FIELD_ios = (MobileBy.XPATH, '//UIAStaticText[@name="Finished"]')
    DESCRIPTION_FIELD_ios = (MobileBy.XPATH, '//UIATextField[3]')

    CREATE_MAPPING_DATA_ios = (MobileBy.XPATH, "//UIALink[@name[contains(., 'Create mapping data')]]")
    EDIT_MAPPING_DATA_ios = (MobileBy.XPATH, "//UIALink[@name[contains(., 'Create mapping data')]]")
    ELEMENT_TO_SCROLL_ios = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAImage[1]')
    SEQUENCE_ONLOAD_HEADER_ios = (MobileBy.XPATH, '//UIAStaticText[@name="sequence_onload"]')
    SEQUENCE_ONLOAD_VALUE_ios = (MobileBy.XPATH, '//UIATextField[@value="test on load"]')
    SEQUENCE_ONSAVE_HEADER_ios = (MobileBy.XPATH, '//UIAStaticText[@name="sequence_onsave"]')
    SEQUENCE_ONSAVE_VALUE_ios = (MobileBy.XPATH, '//UIATextField[@value="(auto)"]')
    NEW_OPTION_LIST_HEADER_ios = (MobileBy.XPATH, '//UIAStaticText[@name="New option list"]')
    OPTION_LIST_VALUE_1_ios = (MobileBy.XPATH, '//UIAStaticText[@name="1"]')
    OPTION_LIST_VALUE_2_ios = (MobileBy.XPATH, '//UIAStaticText[@name="2"]')
    OPTION_LIST_VALUE_3_ios = (MobileBy.XPATH, '//UIAStaticText[@name="3"]')
    FIELD_TO_RESTORE_1_HEADER_ios = (MobileBy.XPATH, '//UIAStaticText[@name="field to restore"]')
    FIELD_TO_RESTORE_1_VALUE_ios = (MobileBy.XPATH, '//UIATextField[@value="value for field 1"]')
    FIELD_TO_RESTORE_2_HEADER_ios = (MobileBy.XPATH, '//UIAStaticText[@name="New email address"]')
    FIELD_TO_RESTORE_2_VALUE_ios = (MobileBy.XPATH, '//UIATextField[@value="test@noggin.com"]')
    CHOOSER_FIELD_ios = (MobileBy.XPATH, '//UIAWebView/UIALink/UIALink[@name[contains(., "New events chooser")]]')
    PREVIOUSLY_CREATED_EVENT_FOR_CHOOSER_ios = (MobileBy.XPATH, '//UIAStaticText[@name[contains('
                                                                '., "Test Appium iOS")]]')
    SUBFORM_FIELD_ADD_ROW_ios = (MobileBy.XPATH, '//UIAButton[@name="Add row"]')
    NEW_EVENTS_CHOOSER_IN_SUB_FORM_ios = (MobileBy.XPATH, '//UIAWebView/UIALink/UIALink[@name[contains('
                                                          '., "New events chooser inside sub form")]]')
    PREVIOUSLY_CREATED_EVENT_FOR_SUBFORM_CHOOSER_ios = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Test")]]')
    DELETE_SUB_EVENT_FROM_CHOOSER_ios = (MobileBy.XPATH, '//UIAScrollView/UIAWebView/UIALink[6]')


class EventDetailsScreen:
    """A class for Event Details screen locators - screen with event details - after opening event."""
    EDIT_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name="Edit"]')
    DELETE_EVENT_BUTTON_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "Delete event")]]')
    DELETE_CONFIRM_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name="Delete"]')
    NEW_SUB_EVENT_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIALink[@name[contains(., "New sub event")]]')
    SET_AS_PRIMARY_BUTTON_ios = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Set as primary")]]')


class Map:
    """A class for Map screen locators."""
    PLOT_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Plot")]]')
    TOOL_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Tool")]]')
    POINT_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Point click to expand")]]')
    DEFAULT_BUTTON_ios = (MobileBy.XPATH, '//UIAStaticText[@name="Default"]')
    MAP_AREA_12_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAImage[12]')
    MAP_AREA_13_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAImage[13]')
    MAP_AREA_17_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAImage[17]')
    MAP_AREA_18_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAImage[18]')
    LINE_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Line")]]')
    CIRCLE_BUTTON_ios = (MobileBy.XPATH, '//UIAScrollView[2]/UIAWebView[1]/UIALink[@name[contains(., "Circle")]]')
    POLYGON_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "Polygon")]]')
    SAVE_MAP_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Save")]]')


class PhotoScreen:
    """A class for Photo screen locators - screen after clicking into Photo button in Main Menu."""
    PHOTO_PAGE_HEADER_ios = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Send a photo to OCA")]]')
    # GALLERY_BUTTON_ios = (MobileBy.XPATH, '//UIAStaticText[2][@visible="false"]')  # appium can't tap that element - probably it's a bug in Appium
    GALLERY_BUTTON_ios = (MobileBy.XPATH, '//UIAStaticText[@name="Gallery"]')  # this locator will find only text, not the icon
    TAKE_NEW_BUTTON_ios = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Take New")]]')  # this locator will find only text, not the icon
    DESCRIPTION_FIELD_ios = (MobileBy.CLASS_NAME, 'UIATextField')
    SEND_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name="Send"]')
    RESET_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name="Reset"]')


class VideoScreen:
    """A class for Video screen locators - screen after clicking into Video button in Main Menu."""
    VIDEO_PAGE_HEADER_ios = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Send a video to OCA")]]')
    # RECORD_NEW_BUTTON_ios = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Record New")]]')  # this locator will find only text, not the icon
    RECORD_NEW_BUTTON_ios = (MobileBy.XPATH, 'UIAScrollView[2]/UIAWebView[1]/UIAStaticText[4]')  # appium can't tap that element - probably it's a bug in Appium - visible: false


class SoundScreen:
    """A class for Sound screen locators - screen after clicking into Sound button in Main Menu."""
    SOUND_PAGE_HEADER_ios = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Send a sound recording to OCA")]]')
    RECORD_SOUND_BUTTON_ios = (MobileBy.XPATH, '//UIAScrollView/UIAWebView/UIAStaticText[2]')  # appium can't tap that element - probably it's a bug in Appium - visible: false


class SoundRecorderScreen:
    """A class for Sound Recorder screen locators - screen after clicking into record sound button in Sound Page."""
    RECORD_SOUND_ios = (MobileBy.ACCESSIBILITY_ID, 'toggle audio recording')
    DONE_BUTTON_ios = (MobileBy.ACCESSIBILITY_ID, 'Done')


class GalleryScreen:
    """A class for handling Gallery"""
    GALLERY_ELEMENT_1_ios = (MobileBy.XPATH, '//UIAPopover[1]/UIACollectionView[1]/UIACollectionCell[1]')
    GALLERY_VIDEOS_POPOVER_ios = (MobileBy.XPATH, '//UIAPopover[1]/UIATableView[1]/UIATableCell[@name="Videos"]')
    USE_VIDEO_BUTTON_ios = (MobileBy.ACCESSIBILITY_ID, 'Use')


class CameraScreen:
    """A class for handling Camera"""
    PHOTO_CAPTURE_ios = (MobileBy.ACCESSIBILITY_ID, 'PhotoCapture')
    CANCEL_BUTTON_ios = (MobileBy.ACCESSIBILITY_ID, 'Cancel')
    CAMERA_CHOOSER_ios = (MobileBy.ACCESSIBILITY_ID, 'FrontBackFacingCameraChooser')
    RETAKE_ios = (MobileBy.ACCESSIBILITY_ID, 'Retake')
    USE_PHOTO_ios = (MobileBy.ACCESSIBILITY_ID, 'Use Photo')
    VIDEO_CAPTURE_ios = (MobileBy.ACCESSIBILITY_ID, 'VideoCapture')  # record and stop recording
    USE_VIDEO_ios = (MobileBy.ACCESSIBILITY_ID, 'Use Video')


class RisksScreen:
    """A class for handling Risks screen"""


class NewContactScreen:
    """A class for handling New Contact screen"""
    FIRST_NAME_ios = (MobileBy.XPATH, '//UIATextField [@name="First name"]')


class NewTaskScreen:
    """A class for handling New Task screen"""
    TITLE_ios = (MobileBy.XPATH, '//UIATextField[1]')  # locating input field by xpath with name won't work
    ASSIGNED_ios = (MobileBy.XPATH, '//UIAStaticText[@name="Assigned"]')
    ADD_CONTACTS_AND_GROUPS_ios = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Add contacts and groups")]]')
    ADD_RESOURCE_STRUCTURE_NODES_ios = (MobileBy.XPATH, '//UIAButton[@name[contains(., '
                                                        '"Add Resource structure nodes")]]')
    ADD_RESOURCE_ASSIGNMENTS_ios = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Add Resource assignments")]]')
    CHOOSE_USERS_ios = (MobileBy.XPATH, '//UIAStaticText[@name="Users"]')
    CHOOSE_CONTACTS_ios = (MobileBy.XPATH, '//UIAStaticText[@name="Contacts"]')
    START_DATE_ios = (MobileBy.XPATH, '//UIAStaticText[@name="Start Date"]')
    HIDE_DATE_PICKER_ios = (MobileBy.XPATH, '//UIAStaticText[@name="Completed Date"]')


class NewReportScreen:
    """A class for handling New Report screen"""
    LODGING_AGENCY_PICKER_ios = (MobileBy.XPATH, '//UIAWebView/UIAElement[2]')
    LODGING_AGENCY_ios = (MobileBy.XPATH, '//UIAPopover/UIATableView/UIATableCell[2]')
    PUBLISH_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name="Publish"]')


# class NewAssetScreen:
#     """A class for handling New Asset screen"""


class NewLogScreen:
    """A class for handling New Log screen"""
    LODGING_AGENCY_PICKER_ios = (MobileBy.XPATH, '//UIAWebView/UIAElement[1]')
    ENTRY_FIELD_ios = (MobileBy.XPATH, '//UIATextField[1]')


class CommonButtonsScreen:
    """A class for handling Common buttons on different screen"""
    SAVE_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name="Save"]')
    CANCEL_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name="Cancel"]')
    OK_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name="Ok"]')


class iOS:
    """A class for handling iOS device for example keyboard"""
    BUTTON_DONE_TO_HIDE_KEYBOARD_ios = (MobileBy.XPATH, '//UIAWindow[2]/UIAToolbar[1]/UIAButton[@name="Done"]')
    RETURN_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name="Return"]')
    BUTTON_ALLOW_LOCATION_ios = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[7]/UIAAlert[1]/UIACollectionView[1]'
                                                 '/UIACollectionCell[2]/UIAButton[@name="Allow"]')
    BUTTON_ALLOW_ACCESS_TO_CAMERA = (MobileBy.ACCESSIBILITY_ID, 'OK')

