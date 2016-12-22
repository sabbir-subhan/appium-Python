# from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class TopBar:
    """A class for top bar locators."""
    HAMBURGER_FOR_MAIN_MENU_ios = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]'
                                                   '/UIAWebView[1]/UIALink[3]/UIAStaticText[1]')


class WelcomeScreen:
    """A class for welcome screen locators - first screen after lunching the app."""
    LOGIN_BUTTON_ios = (MobileBy.XPATH, '//UIAWebView/UIALink[@name[contains(., "LOGIN")]]')
    LOGIN_BUTTON_by_index_ios = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[1]'
                                                 '/UIAScrollView[2]/UIAWebView[1]/UIALink[9]')


class LoginScreen:
    """A class for login screen locators - screen after clicking into LOGIN."""
    TEXTFIELD_USERNAME_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIATextField[1]')
    TEXTFIELD_PASSWORD_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIASecureTextField[1]')
    TEXTFIELD_DOMAIN_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIATextField[2]')
    SUBMIT_BUTTON_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAButton[@name="Submit"]')
    # SUBMIT_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Submit') for testing

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


class MainMenuScreen:
    """A class for main menu screen locators - first screen after correct login into the app."""
    LOGOUT_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "LOGOUT")]]')
    EVENTS_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "EVENTS")]]')
    LOCATION_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "LOCATION")]]')
    MAP_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "MAP")]]')
    PHOTO_BUTTON_ios = (MobileBy.XPATH, '//UIALink[@name[contains(., "PHOTO")]]')


class LocationScreen:
    """A class for Location screen locators - screen after clicking into Location button in Main Menu."""
    SEND_ONCE_NOW_ios = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Send once now")]]')
    # button have attribute visible: false
    CHECK_SENDING_NOW_BUTTON_ios = (MobileBy.XPATH, '')
    SEND_EVERY_SPINNER_ios = (MobileBy.XPATH, '//UIAWebView/UIAElement[@name="Send every"]')
    CHOOSE_1_HOUR_OPTION_iPad = (MobileBy.XPATH, '//UIAWindow/UIAPopover/UIATableView/UIATableCell[6]')
    ASSERT_1_HOUR_OPTION_ios = (MobileBy.XPATH, '//UIAWebView[1]/UIAStaticText[@name="1 hour"]')
    START_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Start")]]')
    LOCATION_PAGE_HEADER_ios = (MobileBy.XPATH, '//UIAStaticText[@name[contains(., "Your location was last sent")]]')


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
    SAVE_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name="Save"]')
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
    CANCEL_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name="Cancel"]')
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
    GALLERY_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Gallery")]]')
    TAKE_NEW_BUTTON_ios = (MobileBy.XPATH, '//UIAButton[@name[contains(., "Take New")]]')


class CameraScreen:
    """A class for handling Camera"""
    PHOTO_CAPTURE = (MobileBy.ACCESSIBILITY_ID, 'PhotoCapture')
    CANCEL_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Cancel')
    CAMERA_CHOOSER = (MobileBy.ACCESSIBILITY_ID, 'FrontBackFacingCameraChooser')
    RETAKE = (MobileBy.ACCESSIBILITY_ID, 'Retake')
    USE_PHOTO = (MobileBy.ACCESSIBILITY_ID, 'Use Photo')


class iOS:
    """A class for handling iOS device for example keyboard"""
    BUTTON_DONE_TO_HIDE_KEYBOARD = (MobileBy.XPATH, '//UIAWindow[2]/UIAToolbar[1]/UIAButton[@name="Done"]')
    RETURN_BUTTON = (MobileBy.XPATH, '//UIAButton[@name="Return"]')
    # BUTTON_ALLOW_LOCATION_ios = (MobileBy.XPATH, '//UIAApplication[1]/UIAWindow[7]/UIAAlert[1]/UIACollectionView[1]'
    #                                              '/UIACollectionCell[2]/UIAButton[@name="Allow"]')
    # BUTTON_ALLOW_ACCESS_TO_CAMERA = (MobileBy.ACCESSIBILITY_ID, 'OK')

