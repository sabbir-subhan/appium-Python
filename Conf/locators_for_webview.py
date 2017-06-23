""" locators in WebView """

from appium.webdriver.common.mobileby import MobileBy


class CommonScreen:
    """A class for handling Common buttons on different screen"""
    LOADING = (MobileBy.CSS_SELECTOR, 'span.ui-icon-loading')
    # OK_BUTTON = (MobileBy.CSS_SELECTOR, '')


class TopBar:
    """A class for top bar locators."""
    HAMBURGER_FOR_MAIN_MENU = (MobileBy.CSS_SELECTOR, 'div#iconbar>a')
    BACK_ARROW = (MobileBy.CSS_SELECTOR, 'div#header>div>a:first-child')


class WelcomeScreen:
    """A class for welcome screen locators - first screen after lunching the app."""
    LOCATION_BUTTON = (MobileBy.CSS_SELECTOR, 'div#locationMenu>a')
    MY_MESSAGES_BUTTON = (MobileBy.CSS_SELECTOR, 'div#appMessagesMenu>a')
    PHOTO_BUTTON = (MobileBy.CSS_SELECTOR, 'div#photoMenu>a')
    VIDEO_BUTTON = (MobileBy.CSS_SELECTOR, 'div#videoMenu>a')
    SOUND_BUTTON = (MobileBy.CSS_SELECTOR, 'div#audioMenu>a')
    SETTINGS_BUTTON = (MobileBy.CSS_SELECTOR, 'div#settingsMenu>a')
    ABOUT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#aboutMenu>a')
    LOGIN_BUTTON = (MobileBy.CSS_SELECTOR, 'div#sessionMenu>a')


class SettingsScreen:
    """A class for settings screen locators - screen after clicking settings button"""
    # SETTINGS_CONTACT_IDENTIFIER_FIELD = (MobileBy.CSS_SELECTOR, '')
    # SETTINGS_ALERT_APP_HAS_BEEN_ACTIVATED = (MobileBy.CSS_SELECTOR, '')
    # SETTINGS_OK_BUTTON = (MobileBy.CSS_SELECTOR, '')
    SETTINGS_ALERT_ABOUT_PIN = (MobileBy.CSS_SELECTOR, 'div#settings>div.ui-popup-container.ui-popup-active')
    SETTINGS_SAVE_BUTTON = (MobileBy.CSS_SELECTOR, 'a#settingsBtnSave')
    PRIMARY_ROLE_SELECTOR = (MobileBy.CSS_SELECTOR, 'div#settings>div.ui-content>div.settings>ul.ui-listview>li[name="primary role"]>div.ui-select')
    FIRST_PRIMARY_ROLE_ON_THE_LIST = (MobileBy.CSS_SELECTOR, 'div#teamrolePrimary>div.ui-content>ul.teamroles>li:first-child')


class LoginScreen:
    """A class for login screen locators - screen after clicking LOGIN button"""
    TEXTFIELD_USERNAME = (MobileBy.CSS_SELECTOR, 'input#sessionUsername')
    TEXTFIELD_PASSWORD = (MobileBy.CSS_SELECTOR, 'input#sessionPassword')
    TEXTFIELD_DOMAIN = (MobileBy.CSS_SELECTOR, 'input#sessionDomain')
    SUBMIT_BUTTON = (MobileBy.CSS_SELECTOR, 'a#sessionSubmit')

    # Notification alert: "OCA now supports sending 'App Messages' to your device as notifications."
    NOTIFICATION_ABOUT_SENDING_MESSAGES = (MobileBy.CSS_SELECTOR, 'div#menu>div.ui-popup-container.ui-popup-active>div[data-role="popup"]>div.ng-dialog-container>p')

    # "No" button for sending notifications on iOS
    NO_FOR_SENDING_NOTIFICATIONS_ON = (MobileBy.CSS_SELECTOR, 'div#menu>div.ui-popup-container.ui-popup-active>div[data-role="popup"]>div[data-role="controlgroup"]>div>a[data-button-index="2"]')

    # ACCEPT_BUTTON on Terms and Conditions"
    ACCEPT_BUTTON = (MobileBy.CSS_SELECTOR, 'a#sessionTermsAccept')

    # # alert message with word "Invalid"
    # ALERT_MSG_INVALID = (MobileBy.CSS_SELECTOR, '')
    #
    # # alert message with "Your temporary account has been expired"
    # ALERT_MSG_EXPIRED = (MobileBy.CSS_SELECTOR, '')
    #
    # # alert message with "The password for the current user is about to expire"
    # ALERT_MSG_WILL_EXPIRE = (MobileBy.CSS_SELECTOR, '')
    #
    # # alert message with word "inactive"
    # ALERT_MSG_SUSPENDED = (MobileBy.CSS_SELECTOR, '')
    # # OK button on alert messages"
    # OK_BUTTON = (MobileBy.CSS_SELECTOR, '')


class MainMenuScreen(WelcomeScreen):
    """A class for main menu screen locators - first screen after correct login into the app."""
    MAIN_MENU = (MobileBy.CSS_SELECTOR, 'div#menu>div[data-role="main"]>div.ui-grid-b.home-icon-grid')
    ACTIVATE_WORKFLOW_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#workflowView?id=1201"]')
    CREATE_CONTACT_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#contactNew?parent=4&type=1"]')
    CREATE_TASK_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#taskNew"]')
    CREATE_REPORT_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#reportNew?type=1"]')
    # WEBSITE_LINK_BUTTON = (MobileBy.CSS_SELECTOR, '')
    INCIDENT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#menu>div[data-role="main"]>div>div>a[href="#emeNew?type=1"]')
    CREATE_ASSETS_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#assetNew?type=1"]')
    CREATE_LOG_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#logNew?type=1"]')
    RISKS_BUTTON = (MobileBy.CSS_SELECTOR, 'div#riskMenu>a')
    EVENTS_BUTTON = (MobileBy.CSS_SELECTOR, 'div#emeMenu>a')
    LOGS_BUTTON = (MobileBy.CSS_SELECTOR, 'div#logMenu>a')
    REPORTS_BUTTON = (MobileBy.CSS_SELECTOR, 'div#reportMenu>a')
    MAP_BUTTON = (MobileBy.CSS_SELECTOR, 'div#map>a')
    ASSETS_BUTTON = (MobileBy.CSS_SELECTOR, 'div#assetMenu>a')
    INBOX_BUTTON = (MobileBy.CSS_SELECTOR, 'div#inboxMenu>a')
    COMPOSE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#messageMenu>a')
    SENT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#sentMenu>a')
    TASKS_BUTTON = (MobileBy.CSS_SELECTOR, 'div#taskMenu>a')
    DOCUMENTS_BUTTON = (MobileBy.CSS_SELECTOR, 'div#documentMenu>a')
    CONTACTS_BUTTON = (MobileBy.CSS_SELECTOR, 'div#contactMenu>a')
    ALLOCATE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#resourceAllocationMenu>a')
    ACTIVATE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#workflowMenu>a')
    OFFLINE_SYNC_BUTTON = (MobileBy.CSS_SELECTOR, 'div#outboxMenu>a')
    LOGOUT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#sessionMenu>a')

    # ALERT_ACTIVATE_BUTTON = (MobileBy.CSS_SELECTOR, '')
    # ALERT_CANCEL_BUTTON = (MobileBy.CSS_SELECTOR, '')
    # ALERT_WORKFLOW_ACTIVATED = (MobileBy.CSS_SELECTOR, '')


class LocationScreen:
    """A class for Location screen locators - screen after clicking into Location button in Main Menu."""
    # SEND_ONCE_NOW = (MobileBy.CSS_SELECTOR, '')
    SEND_EVERY_SPINNER = (MobileBy.CSS_SELECTOR, 'div#location>div.ui-content>div.ui-grid-a>div.ui-block-b>div.ui-select>div#locationInterval-button>select[name="locationInterval"]')
    # CHOOSE_5_MINUTES_OPTION_iPad = (MobileBy.CSS_SELECTOR, '')
    # ASSERT_5_MINUTES_OPTION = (MobileBy.CSS_SELECTOR, '')
    FOR_THE_NEXT_SPINNER = (MobileBy.CSS_SELECTOR, 'div#locationDuration-button>select[name="locationDuration"]')
    # CHOOSE_1_HOUR_OPTION_iPad = (MobileBy.CSS_SELECTOR, '')
    # ASSERT_1_HOUR_OPTION = (MobileBy.CSS_SELECTOR, '')
    START_BUTTON = (MobileBy.CSS_SELECTOR, 'button#locationStart')
    # STOP_BUTTON = (MobileBy.CSS_SELECTOR, '')
    # TRACKING_HISTORY_BUTTON = (MobileBy.CSS_SELECTOR, '')
    # LOCATION_PAGE_HEADER = (MobileBy.CSS_SELECTOR, '')
    # LOCATION_STATUS = (MobileBy.CSS_SELECTOR, '')


class EventsScreen:
    """A class for Events screen locators - screen after clicking into Events button in Main Menu."""

    # filtering events by Type
    CLEAR_SEARCH_FIELD_BUTTON = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div.ui-content>div.filters>div.ui-input-search>a.ui-input-clear')
    # ANY_TYPE_EXPAND = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div[data-role="main"]>div.filters>div[data-role="collapsible"]>h2>a>span[data-translate="Any Type"]')
    # CHOOSE_TYPE_INCIDENT = (MobileBy.CSS_SELECTOR, '')
    # INCIDENT_TYPE_EXPAND = (MobileBy.CSS_SELECTOR, '')
    # CHOOSE_TYPE_ANY = (MobileBy.CSS_SELECTOR, '')

    # filtering events by Status
    # ANY_STATUS_EXPAND = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div[data-role="main"]>div.filters>div[data-role="collapsible"]>h2>a>span[data-translate="Any Status"]')
    TYPE_FILTER = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div.ui-content>div.filters>div[data-role="collapsible"]:first-child>h2>a')
    FIRST_TYPE = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div.ui-content>div.filters>div[data-role="collapsible"]:first-child>div>ul[data-role="listview"]>li:first-child>a')  # ALL REPORTS
    SECOND_TYPE = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div.ui-content>div.filters>div[data-role="collapsible"]:first-child>div>ul[data-role="listview"]>li:nth-child(2)>a')  # MEDIA RELEASE
    THIRD_TYPE = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div.ui-content>div.filters>div[data-role="collapsible"]:first-child>div>ul[data-role="listview"]>li:nth-child(3)>a')  # REPORT_FOR_TESTS
    FOURTH_TYPE = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div.ui-content>div.filters>div[data-role="collapsible"]:first-child>div>ul[data-role="listview"]>li:nth-child(4)>a')  # SITUATION REPORT
    STATUS_FILTER = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div.ui-content>div.filters>div[data-role="collapsible"]:nth-child(2)>h2>a')
    FIRST_STATUS = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div.ui-content>div.filters>div[data-role="collapsible"]:nth-child(2)>div>ul[data-role="listview"]>li:first-child>a')  # ANY STATUS
    SECOND_STATUS = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div.ui-content>div.filters>div[data-role="collapsible"]:nth-child(2)>div>ul[data-role="listview"]>li:nth-child(2)>a')  # ACTIVE
    THIRD_STATUS = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div.ui-content>div.filters>div[data-role="collapsible"]:nth-child(2)>div>ul[data-role="listview"]>li:nth-child(3)>a')  # INACTIVE
    FOURTH_STATUS = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div.ui-content>div.filters>div[data-role="collapsible"]:nth-child(2)>div>ul[data-role="listview"]>li:nth-child(4)>a')  # DRAFT

    # filtering events using search field
    SEARCH_FIELD = (MobileBy.CSS_SELECTOR, 'input#emeSearch')

    # creating and editing Events
    MORE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li#openEmeTreeMore>a[href="#emeTreeMore"]')
    NEW_EVENT_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#emeNew?parent=0"]')

    # previously created event
    PREVIOUSLY_CREATED_EVENT = (MobileBy.CSS_SELECTOR, 'ul.emes.listview.ui-listview>li:first-child>a')
    # PREVIOUSLY_CREATED_EVENT_CHECKBOX = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div.ui-content>div.main>ul[data-role="listview"]>li:first-child>div.ui-checkbox')
    PREVIOUSLY_CREATED_EVENT_CHECKBOX = (MobileBy.CSS_SELECTOR, 'ul.emes.listview.ui-listview>li:first-child>div.ui-checkbox')

    # CLEAR_PRIMARY_EVENT_BUTTON = (MobileBy.CSS_SELECTOR, 'li.primary.eme.clear.ui-first-child>a')
    # NOTIFICATION_PRIMARY_EVENT_CLEARED = (MobileBy.CSS_SELECTOR, '')
    VIEW_ON_MAP_BUTTON = (MobileBy.CSS_SELECTOR, 'div#emeView>div.ui-content>ul.ui-listview>li>a[href="#mapPage?geometry=true"]')  # button inside event details


class TypesOfEventsScreen:
    """A class for Type of Events screen locators - first screen after creating new event with types of events."""
    # INCIDENT_TYPE_OF_EVENT = (MobileBy.CSS_SELECTOR, '')
    # EVENT_FOR_ON_LOAD_SAVE = (MobileBy.CSS_SELECTOR, '')
    # EVENT_FOR_CHOOSER_FIELDS = (MobileBy.CSS_SELECTOR, '')


class EventEditScreen:
    """A class for Edit Events screen locators - screen after opening edit mode of event or creating a new one."""
    SAVE_BUTTON_NEW_EVENT = (MobileBy.CSS_SELECTOR, 'div#emeNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                                    'a[href="#save"]')
    CANCEL_BUTTON = (MobileBy.CSS_SELECTOR, 'div#emeNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                            'a[href="#cancel"]')
    SAVE_BUTTON_EDIT_EVENT = (MobileBy.CSS_SELECTOR, 'div#emeEdit>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                                     'a[href="#save"]')
    CANCEL_BUTTON_EDIT_EVENT = (MobileBy.CSS_SELECTOR, 'div#emeEdit>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                                       'a[href="#cancel"]')
    NAME_FIELD = (MobileBy.CSS_SELECTOR, 'div#emeNew>div>ul>li>div>input#name')
    SEVERITY_LEVEL_SELECTOR = (MobileBy.CSS_SELECTOR, 'div#emeNew>div>ul>li>div>div>select[name="severity"]')  # for new event
    SEVERITY_LEVEL_SELECTOR_EDIT_EVENT = (MobileBy.CSS_SELECTOR, 'div#emeEdit>div>ul>li>div>div>select[name="severity"]')
    # CHOOSE_SEVERITY_LVL1_iPad = (MobileBy.CSS_SELECTOR, '')
    # CHOOSE_SEVERITY_LVL2_iPad = (MobileBy.CSS_SELECTOR, '')
    # CHOOSE_SEVERITY_LVL3_iPad = (MobileBy.CSS_SELECTOR, '')
    # CHOOSE_SEVERITY_LVL4_iPad = (MobileBy.CSS_SELECTOR, '')
    # CHOOSE_SEVERITY_LVL5_iPad = (MobileBy.CSS_SELECTOR, '')
    # FINISHED_FIELD = (MobileBy.CSS_SELECTOR, '')
    DESCRIPTION_FIELD = (MobileBy.CSS_SELECTOR, 'iframe[title="Rich Text Editor, description"]')
    CREATE_MAPPING_DATA_EDIT = (MobileBy.CSS_SELECTOR, 'div#emeEdit>div>ul.edit-view.ui-listview>li.geometryinput>a')
    CREATE_MAPPING_DATA_NEW = (MobileBy.CSS_SELECTOR, 'div#emeNew>div>ul.edit-view.ui-listview>li.geometryinput>a')
    # EDIT_MAPPING_DATA = (MobileBy.CSS_SELECTOR, '')
    # ELEMENT_TO_SCROLL = (MobileBy.CSS_SELECTOR, '')
    # SEQUENCE_ONLOAD_HEADER = (MobileBy.CSS_SELECTOR, '')
    # SEQUENCE_ONLOAD_VALUE = (MobileBy.CSS_SELECTOR, '')
    # SEQUENCE_ONSAVE_HEADER = (MobileBy.CSS_SELECTOR, '')
    # SEQUENCE_ONSAVE_VALUE = (MobileBy.CSS_SELECTOR, '')
    # NEW_OPTION_LIST_HEADER = (MobileBy.CSS_SELECTOR, '')
    # OPTION_LIST_VALUE_1 = (MobileBy.CSS_SELECTOR, '')
    # OPTION_LIST_VALUE_2 = (MobileBy.CSS_SELECTOR, '')
    # OPTION_LIST_VALUE_3 = (MobileBy.CSS_SELECTOR, '')
    FIELD_TO_RESTORE_1_HEADER = (MobileBy.CSS_SELECTOR, 'div.ui-content>ul.edit-view>li>label[for="field to restore"]')
    # FIELD_TO_RESTORE_1_VALUE = (MobileBy.CSS_SELECTOR, '')
    FIELD_TO_RESTORE_2_HEADER = (MobileBy.CSS_SELECTOR, 'div.ui-content>ul.edit-view>li>label[for="new email address"]')
    # FIELD_TO_RESTORE_2_VALUE = (MobileBy.CSS_SELECTOR, '')
    FIELD_TO_RESTORE_3_HEADER = (MobileBy.CSS_SELECTOR, 'div.ui-content>ul.edit-view>li>label[for="new website address"]')
    # FIELD_TO_RESTORE_3_VALUE = (MobileBy.CSS_SELECTOR, '')
    # CHOOSER_FIELD = (MobileBy.CSS_SELECTOR, '')
    SUBFORM_FIELD_ADD_ROW = (MobileBy.CSS_SELECTOR, 'div.subform>a')
    NEW_EVENTS_CHOOSER_IN_SUB_FORM = (MobileBy.CSS_SELECTOR, 'div.subform>div.subform-row>ul.subform-row>li>div.ui-select')
    DELETE_SUB_EVENT_FROM_CHOOSER = (MobileBy.CSS_SELECTOR, 'div.subform>div.subform-row>a.delete')


class EventDetailsScreen:
    """A class for Event Details screen locators - screen with event details - after opening event."""
    EDIT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#emeView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.edit.ui-block-a>a')
    DELETE_EVENT_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#confirmDeleteEME"]')
    # DELETE_CONFIRM_BUTTON = (MobileBy.CSS_SELECTOR, '')
    MORE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#emeView>div[data-role="footer"]>div.ui-navbar>ul.ui-grid-a>li.more.ui-block-b>a[href="#emeViewMoreMenu"]')
    # MORE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#emeView>div[data-role="footer"]>div.ui-navbar>ul.ui-grid-a>li.more.ui-block-b')
    NEW_SUB_EVENT = (MobileBy.CSS_SELECTOR, 'li.eme.new.subeme>a')
    SET_AS_PRIMARY_BUTTON = (MobileBy.CSS_SELECTOR, 'li.primary.eme.set.ineme.ui-first-child>a')
    EVENT_INFO_BUTTON = (MobileBy.CSS_SELECTOR, 'div#emeTreeView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.ui-block-a>a.emeView')


class Map:
    """A class for Map screen locators."""
    PLOT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-b>li#mapPlot>a')
    TOOL_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div[data-role="footer"]>div.ui-navbar>ul.ui-grid-b>li#openMapToolMore>a[href="#mapToolMore"]')
    POINT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div#mapToolMore-popup>div#mapToolMore>div[data-collapsed-icon="arrow-d"]>div.Point>h2')
    POINT_DEFAULT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div#mapToolMore-popup>div#mapToolMore>div[data-collapsed-icon="arrow-d"]>div.Point>div>ul>li:first-child')
    POINT_2_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div#mapToolMore-popup>div#mapToolMore>div[data-collapsed-icon="arrow-d"]>div.Point>div>ul>li.ui-last-child')  # new symbology created in OCA
    LINE_DEFAULT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div#mapToolMore-popup>div#mapToolMore>div[data-collapsed-icon="arrow-d"]>div.Line>div>ul>li')
    CIRCLE_DEFAULT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div#mapToolMore-popup>div#mapToolMore>div[data-collapsed-icon="arrow-d"]>div.Circle>div>ul>li')
    POLYGON_DEFAULT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div#mapToolMore-popup>div#mapToolMore>div[data-collapsed-icon="arrow-d"]>div.Polygon>div>ul>li')
    MAP_AREA_18 = (MobileBy.CSS_SELECTOR, 'div#mapPage>div.ui-content>div#mapCanvas>div#mapCanvas_root>div#mapCanvas_container>div#mapCanvas_layers>div#mapCanvas_layer0>div>img#mapCanvas_layer0_tile_12_2_2')
    LINE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div#mapToolMore-popup>div#mapToolMore>div[data-collapsed-icon="arrow-d"]>div.Line>h2')
    CIRCLE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div#mapToolMore-popup>div#mapToolMore>div[data-collapsed-icon="arrow-d"]>div.Circle>h2')
    POLYGON_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div#mapToolMore-popup>div#mapToolMore>div[data-collapsed-icon="arrow-d"]>div.Polygon>h2')
    SAVE_MAP_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                              'a[data-translate="Save"]')
    CANCEL_MAP_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                                'a[data-translate="Cancel"]')
    LAYERS = (MobileBy.CSS_SELECTOR, 'div#mapPage>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-b>li.ui-block-a>a[href="#mapLayers"]')
    FIRST_LAYER_ON_THE_LIST = (MobileBy.CSS_SELECTOR, 'div#mapLayers>div.ui-content>ul>li:first-child')
    SECOND_LAYER_ON_THE_LIST = (MobileBy.CSS_SELECTOR, 'div#mapLayers>div.ui-content>ul>li:nth-child(2)')
    THIRD_LAYER_ON_THE_LIST = (MobileBy.CSS_SELECTOR, 'div#mapLayers>div.ui-content>ul>li:nth-child(3)')
    LAYERS_DONE = (MobileBy.CSS_SELECTOR, 'div#mapLayers>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.ui-block-a>a#layersDone')
    LAYERS_SAVED_MAPS = (MobileBy.CSS_SELECTOR, 'div#mapLayers>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.ui-block-b>a[href="#savedMaps"]')
    PLOT_TYPE_ASSET = (MobileBy.CSS_SELECTOR, 'div#mapPlotType>div.ui-content>ul.ui-listview>li>a[data-link="#assetNew?parent=0"]')
    LOCATE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div.ui-content>div#mapCanvas>div#locateButton>div.locateContainer>div')
    SEARCH_BUTTON_ON_MAP = (MobileBy.CSS_SELECTOR, 'div#mapPage>div.ui-content>div#mapCanvas>div#searchButton>a[href="#mapSearch"]')
    SEARCH_BUTTON = (MobileBy.CSS_SELECTOR, 'a#runSearchButton')
    FIRST_ADDRESS_ON_THE_LIST = (MobileBy.CSS_SELECTOR, 'div#mapSearch>div.ui-content>ul.ui-listview>li.ui-first-child')
    ZOOM_IN_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div.ui-content>div#mapCanvas>div#mapCanvas_root>div#mapCanvas_zoom_slider>div:first-child')
    ZOOM_OUT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div.ui-content>div#mapCanvas>div#mapCanvas_root>div#mapCanvas_zoom_slider>div:last-child')
    CLEAR_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div[data-role="footer"]>div.ui-navbar>ul.ui-grid-b>li#mapClear>a')
    FIRST_PLOT_OBJECT = (MobileBy.CSS_SELECTOR, 'div#mapPlotType>div.ui-content>ul.ui-listview>li:first-child>a')  # asset
    SECOND_PLOT_OBJECT = (MobileBy.CSS_SELECTOR, 'div#mapPlotType>div.ui-content>ul.ui-listview>li:nth-child(2)>a')  # event
    THIRD_PLOT_OBJECT = (MobileBy.CSS_SELECTOR, 'div#mapPlotType>div.ui-content>ul.ui-listview>li:nth-child(3)>a')  # report
    FOURTH_PLOT_OBJECT = (MobileBy.CSS_SELECTOR, 'div#mapPlotType>div.ui-content>ul.ui-listview>li:last-child>a')  # task
    VIEW_ATTRIBUTES_FROM_LAYER = (MobileBy.CSS_SELECTOR, 'div#mapPage>div.ui-content>div#mapCanvas>div#tools>a')  # view asset, event, task, contact
    DUPLICATED_GEOMETRY_ON_MAP = (MobileBy.CSS_SELECTOR, 'div#mapPage>div.ui-content>div#mapCanvas>div#mapCanvas_root>div#mapCanvas_container>div#mapCanvas_layers>svg>g#mapCanvas_graphics_layer>image:last-child')
    DUPLICATE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#mapPage>div.ui-content>div#mapCanvas>div#tools>a:nth-child(2)')
    MAP_ADDED_GEOMETRY_ALL = (MobileBy.CSS_SELECTOR, 'div#mapPage>div.ui-content>div#mapCanvas>div#mapCanvas_root>div#mapCanvas_container>div#mapCanvas_layers>svg>g#mapCanvas_graphics_layer>image')
    WHOLE_MAP = (MobileBy.CSS_SELECTOR, 'div#mapPage>div.ui-content>div#mapCanvas>div#mapCanvas_root>div#mapCanvas_container>div#mapCanvas_layers')
    ALL_EVENTS_AND_CONTACTS_GEOMETRY = (MobileBy.CSS_SELECTOR, 'div#mapPage>div.ui-content>div#mapCanvas>div#mapCanvas_root>div#mapCanvas_container>div#mapCanvas_layers>svg>g#mapCanvas_graphics_layer>image:last-child')
    ALL_ASSETS_AND_TASKS_GEOMETRY = (MobileBy.CSS_SELECTOR, 'div#mapPage>div.ui-content>div#mapCanvas>div#mapCanvas_root>div#mapCanvas_container>div#mapCanvas_layers>svg>g#mapCanvas_graphics_layer>image:nth-child(2)')
    MAP_ADDED_LAYER = (MobileBy.CSS_SELECTOR, 'div#mapPage>div.ui-content>div#mapCanvas>div#mapCanvas_root>div#mapCanvas_container>div#mapCanvas_layers>svg>g#mapCanvas_graphics_layer>image:last-child')
    MAP_ADDED_LAYER_SECOND_ELEMENT = (MobileBy.CSS_SELECTOR, 'div#mapPage>div.ui-content>div#mapCanvas>div#mapCanvas_root>div#mapCanvas_container>div#mapCanvas_layers>svg>g>image:nth-child(2)')
    MAP_ADDED_LAYER_FOR_MOBILE = (MobileBy.CSS_SELECTOR, 'div#mapPage>div.ui-content>div#mapCanvas>div#mapCanvas_root>div#mapCanvas_container>div#mapCanvas_layers>svg>g#mapCanvas_graphics_layer>path:last-child')


class PhotoScreen:
    """A class for Photo screen locators - screen after clicking into Photo button in Main Menu."""
    # PHOTO_PAGE_HEADER = (MobileBy.CSS_SELECTOR, '')
    GALLERY_BUTTON = (MobileBy.CSS_SELECTOR, 'div#photo>div.ui-content>div#photo-placeholder>div.ui-block-a>div.center-text>span[data-open="album"]>span.icon')
    TAKE_NEW_BUTTON = (MobileBy.CSS_SELECTOR, 'div#photo>div.ui-content>div.ui-grid-a>div.ui-block-b>div.center-text>span[data-open="camera"]>span.icon')
    DESCRIPTION_FIELD = (MobileBy.CSS_SELECTOR, 'textarea#photo-input-description')
    SEND_BUTTON = (MobileBy.CSS_SELECTOR, 'div#photo>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.ui-block-a>a#photoBtnSend')
    RESET_BUTTON = (MobileBy.CSS_SELECTOR, 'a#photoBtnReset')


class VideoScreen:
    """A class for Video screen locators - screen after clicking into Video button in Main Menu."""
    # VIDEO_PAGE_HEADER = (MobileBy.CSS_SELECTOR, '')
    GALLERY_BUTTON = (MobileBy.CSS_SELECTOR, 'div#video>div.ui-content>div#video-placeholder>div.ui-block-a>div.center-text>span[data-open="album"]>span.icon')
    # RECORD_NEW_BUTTON = (MobileBy.CSS_SELECTOR, 'div#video>div.ui-content>div.ui-grid-a>div.ui-block-b>div.center-text>span[data-open="camera"]>span.icon')
    RECORD_NEW_BUTTON = (MobileBy.CSS_SELECTOR, 'div#video>div.ui-content>div#video-placeholder>div.ui-block-b>div.center-text>span:first-child>span.icon')
    SEND_BUTTON = (MobileBy.CSS_SELECTOR, 'div#video>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.ui-block-a>a#videoBtnSend')
    DESCRIPTION_FIELD = (MobileBy.CSS_SELECTOR, 'textarea#video-input-description')


class SoundScreen:
    """A class for Sound screen locators - screen after clicking into Sound button in Main Menu."""
    # SOUND_PAGE_HEADER = (MobileBy.CSS_SELECTOR, '')
    RECORD_SOUND_BUTTON = (MobileBy.CSS_SELECTOR, 'div#audio>div>div.ui-grid-a>div#audio-placeholder>span')
    DESCRIPTION_FIELD = (MobileBy.CSS_SELECTOR, 'textarea#audio-input-description')
    SEND_BUTTON = (MobileBy.CSS_SELECTOR, 'div#audio>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.ui-block-a>a#audioBtnSend')


# class SoundRecorderScreen:
#     """A class for Sound Recorder screen locators - screen after clicking into record sound button in Sound Page."""
#     RECORD_SOUND = (MobileBy.CSS_SELECTOR, 'toggle audio recording')
#     DONE_BUTTON = (MobileBy.CSS_SELECTOR, 'Done')
#
#
# class GalleryScreen:
#     """A class for handling Gallery"""
#     GALLERY_ELEMENT_1 = (MobileBy.CSS_SELECTOR, '//XCUIElementTypeCell[@name[contains(., "Photo")]][1]')
#     GALLERY_VIDEOS_POPOVER = (MobileBy.CSS_SELECTOR, '//XCUIElementTypeButton[@name="Videos"]')
#     GALLERY_VIDEO_ELEMENT_1 = (MobileBy.CSS_SELECTOR, '//XCUIElementTypeCell[1]')
#     USE_BUTTON = (MobileBy.CSS_SELECTOR, 'Choose')


# class CameraScreen:
#     """A class for handling Camera"""
#     PHOTO_CAPTURE = (MobileBy.CSS_SELECTOR, 'PhotoCapture')
#     CANCEL_BUTTON = (MobileBy.CSS_SELECTOR, 'Cancel')
#     CAMERA_CHOOSER = (MobileBy.CSS_SELECTOR, 'FrontBackFacingCameraChooser')
#     RETAKE = (MobileBy.CSS_SELECTOR, 'Retake')
#     USE_PHOTO = (MobileBy.CSS_SELECTOR, 'Use Photo')
#     VIDEO_CAPTURE = (MobileBy.CSS_SELECTOR, 'VideoCapture')  # record and stop recording
#     USE_VIDEO = (MobileBy.CSS_SELECTOR, 'Use Video')


class ContactsScreen:
    """A class for handling Contacts screen"""
    SAVE_NEW_CONTACT = (MobileBy.CSS_SELECTOR, 'div#contactNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                               'a[href="#save"]')
    SAVE_EDITED_CONTACT = (MobileBy.CSS_SELECTOR, 'div#contactEdit>div[data-role="footer"]>div[data-role="navbar"]>ul>li>a[href="#save"]')
    CANCEL_NEW_CONTACT = (MobileBy.CSS_SELECTOR, 'div#contactNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                                 'a[href="#cancel"]')
    CANCEL_EDITED_CONTACT = (MobileBy.CSS_SELECTOR, 'div#contactEdit>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                                    'a[href="#cancel"]')
    FIRST_NAME_FOR_NEW_CONTACT = (MobileBy.CSS_SELECTOR, 'div#contactNew>div.ui-content>ul.ui-listview>li.ui-field-contain>div.ui-input-text>input[id="first name"]')
    FIRST_NAME_FOR_EDIT_CONTACT = (MobileBy.CSS_SELECTOR, 'div#contactEdit>div.ui-content>ul.ui-listview>li.ui-field-contain>div.ui-input-text>input[id="first name"]')
    FIRST_CONTACT_GROUP = (MobileBy.CSS_SELECTOR, 'div#contactgroupTreeView>div.ui-content>div.main>ul.groups>li:first-child>a')
    SECOND_CONTACT_GROUP = (MobileBy.CSS_SELECTOR, 'div#contactgroupTreeView>div.ui-content>div.main>ul.groups>li:nth-child(2)>a')
    THIRD_CONTACT_GROUP = (MobileBy.CSS_SELECTOR, 'div#contactgroupTreeView>div.ui-content>div.main>ul.groups>li:last-child>a')
    NEW_BUTTON = (MobileBy.CSS_SELECTOR, 'div#contactgroupTreeView>div[data-role="footer"]>div.ui-navbar>ul.ui-grid-a>li#openContactGroupTreeMore>a[href="#contactgroupTreeMore"]')
    ADD_NEW_CONTACT_GROUP = (MobileBy.CSS_SELECTOR, 'div#contactgroupTreeView>div#contactgroupTreeMore-popup>div#contactgroupTreeMore>ul>li.new.contactgroup>a')
    ADD_NEW_CONTACT_INTO_GROUP = (MobileBy.CSS_SELECTOR, 'div#contactgroupTreeView>div#contactgroupTreeMore-popup>div#contactgroupTreeMore>ul>li:nth-child(2)>a')
    IMPORT_CONTACT_FROM_DEVICE_INTO_GROUP = (MobileBy.CSS_SELECTOR, 'div#contactgroupTreeView>div#contactgroupTreeMore-popup>div#contactgroupTreeMore>ul>li.ingroup.new.import>a')
    # FIRST_CONTACT_ON_THE_LIST = (MobileBy.CSS_SELECTOR, 'div#contactgroupTreeView>div.ui-content>div.secondary>ul.listview>li:first-child')
    FIRST_CONTACT_ON_THE_LIST = (MobileBy.CSS_SELECTOR, 'div#contactgroupTreeView>div.ui-content>div.secondary>ul.listview>li:first-child>a')
    FIRST_CONTACT_ON_THE_LIST_WITH_CHECKBOX = (MobileBy.CSS_SELECTOR, 'div#contactgroupTreeView>div.ui-content>div.secondary>ul.listview>li:first-child>div.ui-checkbox')
    FIRST_CONTACT_GROUP_ON_THE_LIST = (MobileBy.CSS_SELECTOR, 'div#contactgroupTreeView>div.ui-content>div.main>ul>li:first-child')
    FIRST_CONTACT_GROUP_ON_THE_LIST_WITH_CHECKBOX = (MobileBy.CSS_SELECTOR, 'div#contactgroupTreeView>div.ui-content>div.main>ul>li:first-child>div.ui-checkbox')
    CONTACT_MORE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#contactView>div[data-role="footer"]>div.ui-navbar>ul.ui-grid-a>li.ui-block-b>a[href="#contactViewMoreMenu"]')
    CONTACT_GROUP_MORE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#contactgroupView>div.ui-footer>div.ui-navbar>ul.ui-grid-a>li#openContactGroupViewMore>a[href="#contactgroupViewMoreMenu"]')
    DELETE_CONTACT = (MobileBy.CSS_SELECTOR, 'div#contactView>div.ui-popup-container>div[data-role="popup"]>ul>li.delete.contact>a[href="#confirmDeleteContact"]')
    DELETE_CONTACT_GROUP = (MobileBy.CSS_SELECTOR, 'div#contactgroupView>div#contactgroupViewMoreMenu-popup>div#contactgroupViewMoreMenu>ul.ui-listview>li.delete>a[href="#confirmDeleteContactGroup"]')
    CONFIRM_DELETE = (MobileBy.CSS_SELECTOR, 'div#contactView>div.ui-popup-container>div#confirmDeleteContact>div.ng-dialog-container>div>div>a:first-child')
    CONFIRM_DELETE_GROUP = (MobileBy.CSS_SELECTOR, 'div#contactgroupView>div.ui-popup-container>div#confirmDeleteContactGroup>div.ng-dialog-container>div>div>a:first-child')
    CANCEL_DELETE = (MobileBy.CSS_SELECTOR, 'div#contactView>div.ui-popup-container>div#confirmDeleteContact>div.ng-dialog-container>div>div>a:last-child')
    CONTACT_EDIT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#contactView>div[data-role="footer"]>div.ui-navbar>ul.ui-grid-a>li.edit.ui-block-a>a')
    ORGANISATION_FIELD = (MobileBy.CSS_SELECTOR, 'input#organisation')
    EMAIL_FIELD = (MobileBy.CSS_SELECTOR, 'div#contactNew>div.ui-content>ul.ui-listview>li.ui-field-contain>div.ui-input-text>input#email')
    CONTACT_SEND_COMMUNICATION = (MobileBy.CSS_SELECTOR, 'div#contactView>div.ui-popup-container>div[data-role="popup"]>ul>li.send>a[href="#messagePage"]')
    SAVE_TO_DEVICE = (MobileBy.CSS_SELECTOR, 'div#contactView>div.ui-popup-container>div[data-role="popup"]>ul>li.save.contact.ui-last-child>a')
    WRITE_ACCESS_LEVEL_FOR_NEW_CONTACT = (MobileBy.CSS_SELECTOR, 'div#contactNew>div.ui-content>ul.ui-listview>li[name="write access level"]>div.ui-select>div')  # for new contact
    READ_ACCESS_LEVEL_FOR_NEW_GROUP = (MobileBy.CSS_SELECTOR, 'div#contactgroupNew>div.ui-content>ul.edit-view>li[name="read access level"]>div.ui-select>div')  # for new contact group
    OPTION_LIST_ADMINISTRATORS_ONLY = (MobileBy.CSS_SELECTOR, 'div#optionList>div.ui-content>ul>li:first-child>div')
    FIRST_CONTACT_ON_THE_LIST_TO_IMPORT_FROM_DEVICE = (MobileBy.CSS_SELECTOR, 'div#contactImport>div.ui-content>ul.contacts>li:first-child>a')
    SEQUENCE_ON_LOAD = (MobileBy.CSS_SELECTOR, 'div#contactNew>div.ui-content>ul.edit-view>li.ui-field-contain.ui-li-static.ui-body-inherit>label[for="on_load"]')
    SEQUENCE_ON_SAVE = (MobileBy.CSS_SELECTOR, 'div#contactNew>div.ui-content>ul.edit-view>li.ui-field-contain.ui-li-static.ui-body-inherit>label[for="on_save"]')
    OPTION_LIST = (MobileBy.CSS_SELECTOR, 'div#contactNew>div.ui-content>ul.edit-view>li[name="new option list"]')
    CLEAR_SEARCH_FIELD_BUTTON = (MobileBy.CSS_SELECTOR, 'div#contactgroupTreeView>div.ui-content>div.ui-input-search>a.ui-input-clear')
    ADDRESS_FIELD = (MobileBy.CSS_SELECTOR, 'div#contactNew>div.ui-content>ul>li>textarea.ui-body-c')
    ADDRESS_NUMBER = (MobileBy.CSS_SELECTOR, 'div#contactNew>div.ui-content>ul.ui-listview>li.ui-field-contain>ul.ui-listview>li>div>input#number')
    ADDRESS_STREET = (MobileBy.CSS_SELECTOR, 'div#contactNew>div.ui-content>ul.ui-listview>li.ui-field-contain>ul.ui-listview>li>div>input#street')
    ADDRESS_POST_CODE = (MobileBy.CSS_SELECTOR, 'div#contactNew>div.ui-content>ul.ui-listview>li.ui-field-contain>ul.ui-listview>li>div>input[id="post code"]')
    ADDRESS_COUNTRY = (MobileBy.CSS_SELECTOR, 'div#contactNew>div.ui-content>ul.ui-listview>li.ui-field-contain>ul.ui-listview>li>div>input#country')
    NAME_FIELD_FOR_NEW_CONTACT_GROUP = (MobileBy.CSS_SELECTOR, 'div#contactgroupNew>div.ui-content>ul>li:first-child>div.ui-input-text>input#name')
    NAME_FIELD_FOR_EDITED_CONTACT_GROUP = (MobileBy.CSS_SELECTOR, 'div#contactgroupEdit>div.ui-content>ul>li:first-child>div.ui-input-text>input#name')
    SAVE_NEW_CONTACT_GROUP = (MobileBy.CSS_SELECTOR, 'div#contactgroupNew>div.ui-footer>div.ui-navbar>ul.ui-grid-a>li.ui-block-a>a')
    SAVE_EDITED_CONTACT_GROUP = (MobileBy.CSS_SELECTOR, 'div#contactgroupEdit>div.ui-footer>div.ui-navbar>ul.ui-grid-a>li.ui-block-a>a')
    GROUP_INFO_BUTTON = (MobileBy.CSS_SELECTOR, 'div#contactgroupTreeView>div.normal-mode.ui-footer>div.ui-navbar>ul.ui-grid-a>li.ui-block-a>a.groupView')
    EDIT_GROUP_BUTTON = (MobileBy.CSS_SELECTOR, 'div#contactgroupView>div.ui-footer>div.ui-navbar>ul.ui-grid-a>li.edit>a.edit')
    CLEAR_NAME_FOR_EDITED_CONTACT_GROUP = (MobileBy.CSS_SELECTOR, 'div#contactgroupEdit>div.ui-content>ul.ui-listview>li.ui-field-contain>div.ui-input-text>a.ui-input-clear')
    CLEAR_FIRST_NAME_FOR_EDITED_CONTACT = (MobileBy.CSS_SELECTOR, 'div#contactEdit>div.ui-content>ul.ui-listview>li.ui-field-contain:nth-child(2)>div.ui-input-text>a')
    GROUP_SEND_COMMUNICATION = (MobileBy.CSS_SELECTOR, 'div#contactgroupView>div#contactgroupViewMoreMenu-popup>div#contactgroupViewMoreMenu>ul.ui-listview>li.send>a[href="#messagePage"]')
    CANCEL_NEW_CONTACT_GROUP = (MobileBy.CSS_SELECTOR, 'div#contactgroupNew>div.ui-footer>div.ui-navbar>ul.ui-grid-a>li.ui-block-b>a[href="#cancel"]')


class TasksScreen:
    """A class for handling Tasks screen"""
    SAVE_NEW_TASK_BUTTON = (MobileBy.CSS_SELECTOR, 'div#taskNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                                   'a[href="#save"]')
    CANCEL_BUTTON = (MobileBy.CSS_SELECTOR, 'div#taskNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                            'a[href="#cancel"]')
    SAVE_EDITED_TASK_BUTTON = (MobileBy.CSS_SELECTOR, 'div#taskEdit>div[data-role="footer"]>div[data-role="navbar"]>ul>li>a[href="#save"]')
    # TITLE = (MobileBy.CSS_SELECTOR, 'input.field-Name')
    TITLE = (MobileBy.CSS_SELECTOR, 'div#taskNew>div.ui-content>ul.edit-view>li:first-child>div.ui-input-text>input#title')
    # ASSIGNED = (MobileBy.CSS_SELECTOR, '')
    # ADD_CONTACTS_AND_GROUPS = (MobileBy.CSS_SELECTOR, '')
    # ADD_RESOURCE_STRUCTURE_NODES = (MobileBy.CSS_SELECTOR, '')
    # ADD_RESOURCE_ASSIGNMENTS = (MobileBy.CSS_SELECTOR, '')
    # CHOOSE_USERS = (MobileBy.CSS_SELECTOR, '')
    # CHOOSE_CONTACTS = (MobileBy.CSS_SELECTOR, '')
    # START_DATE = (MobileBy.CSS_SELECTOR, '')
    # HIDE_DATE_PICKER = (MobileBy.CSS_SELECTOR, '')
    YES_BUTTON_FOR_ACTION_REQUIRED = (MobileBy.CSS_SELECTOR, 'div#taskView>div.ui-content>ul.ui-listview>li.ui-li-static>ul.ui-grid-a.outcomeOptions>li.ui-block-a>a[href="#confirmOutcomeTask"]')
    ALERT_CONFIRM_ACTION_REQUIRED = (MobileBy.CSS_SELECTOR, 'div#taskView>div.ui-popup-container>div#confirmOutcomeTask>div.ng-dialog-container>div>div>a:first-child')
    FILTERS = (MobileBy.CSS_SELECTOR, 'div#taskIndex>div.ui-content>div[data-role="collapsible"]:first-child>h2>a')
    MY_TASKS = (MobileBy.CSS_SELECTOR, 'div#taskIndex>div.ui-content>div[data-role="collapsible"]:first-child>div>ul[data-role="listview"]>li:first-child>a')
    ALL_TASKS = (MobileBy.CSS_SELECTOR, 'div#taskIndex>div.ui-content>div[data-role="collapsible"]:first-child>div>ul[data-role="listview"]>li:nth-child(2)>a')
    INCOMPLETE_TASKS = (MobileBy.CSS_SELECTOR, 'div#taskIndex>div.ui-content>div[data-role="collapsible"]:first-child>div>ul[data-role="listview"]>li:nth-child(3)>a')
    ACTION_REQUIRED_TASKS = (MobileBy.CSS_SELECTOR, 'div#taskIndex>div.ui-content>div[data-role="collapsible"]:first-child>div>ul[data-role="listview"]>li:nth-child(4)>a')
    FIRST_TASK_ON_THE_LIST = (MobileBy.CSS_SELECTOR, 'div#taskIndex>div.ui-content>div.main>ul.tasks>li:first-child>a')
    CLEAR_SEARCH_FIELD_BUTTON = (MobileBy.CSS_SELECTOR, 'div#taskIndex>div.ui-content>div.ui-input-search>a.ui-input-clear')
    VIEW_ON_MAP_BUTTON = (MobileBy.CSS_SELECTOR, 'div#taskView>div.ui-content>ul.ui-listview>li>a[href="#mapPage?geometry=true"]')  # button inside task details
    CREATE_NEW_TASK_BUTTON = (MobileBy.CSS_SELECTOR, 'div#taskIndex>div.ui-footer>div.ui-navbar>ul>li>a[href="#taskNew"]')
    EDIT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#taskView>div.ui-footer>div.ui-navbar>ul.ui-grid-a>li.edit>a')
    FIRST_STRUCTURE_NODE_ON_THE_LIST = (MobileBy.CSS_SELECTOR, 'div#teamroleIndex>div.ui-content>ul.teamroles>li:first-child>div.ui-checkbox')
    SECOND_STRUCTURE_NODE_ON_THE_LIST = (MobileBy.CSS_SELECTOR, 'div#teamroleIndex>div.ui-content>ul.teamroles>li:nth-child(2)>div.ui-checkbox')
    LAST_STRUCTURE_NODE_ON_THE_LIST = (MobileBy.CSS_SELECTOR, 'div#teamroleIndex>div.ui-content>ul.teamroles>li:last-child>div.ui-checkbox')
    FIRST_RESOURCE_ASSIGNMENT_ON_THE_LIST = (MobileBy.CSS_SELECTOR, 'div#teamIndex>div.ui-content>ul.teams>li:first-child>div.ui-checkbox')
    SECOND_RESOURCE_ASSIGNMENT_ON_THE_LIST = (MobileBy.CSS_SELECTOR, 'div#teamIndex>div.ui-content>ul.teams>li:nth-child(2)>div.ui-checkbox')
    LAST_RESOURCE_ASSIGNMENT_ON_THE_LIST = (MobileBy.CSS_SELECTOR, 'div#teamIndex>div.ui-content>ul.teams>li:last-child>div.ui-checkbox')
    VALIDATION_ERROR_POPUP = (MobileBy.CSS_SELECTOR, 'div#taskNew>div.ui-popup-container.ui-popup-active')


class ReportsScreen:
    """A class for handling Reports screen"""
    TITLE = (MobileBy.CSS_SELECTOR, 'div#reportNew>div.ui-content>ul.edit-view>li:first-child>div>input#title')
    # LODGING_AGENCY_PICKER = (MobileBy.CSS_SELECTOR, 'div#field-1201-button>select[name="lodging agency"]')
    NEW_REPORT_LODGING_AGENCY_PICKER = (MobileBy.CSS_SELECTOR, 'div#reportNew>div.ui-content>ul.edit-view>li>div.ui-select>div.ui-btn>select[name="lodging agency"]')  # not working on iOS 10
    EDIT_REPORT_LODGING_AGENCY_PICKER = (MobileBy.CSS_SELECTOR, 'div#reportEdit>div.ui-content>ul.edit-view>li>div.ui-select>div.ui-btn>select[name="lodging agency"]')
    # LODGING_AGENCY = (MobileBy.CSS_SELECTOR, '')  # picker wheel on iOS and popup on Android are native elements
    PUBLISH_NEW_REPORT = (MobileBy.CSS_SELECTOR, 'div#reportNew>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-b>li.ui-block-a>a[href="#save"]')
    CANCEL_NEW_REPORT = (MobileBy.CSS_SELECTOR, 'div#reportNew>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-b>li.ui-block-c>a[href="#cancel"]')
    PUBLISH_EDITED_REPORT = (MobileBy.CSS_SELECTOR, 'div#reportEdit>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-b>li.ui-block-a>a[href="#save"]')
    CANCEL_EDITED_REPORT = (MobileBy.CSS_SELECTOR, 'div#reportEdit>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-b>li.ui-block-c>a[href="#cancel"]')
    TYPE_FILTER = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:first-child>h2>a')
    FIRST_TYPE = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:first-child>div>ul[data-role="listview"]>li:first-child>a')  # ALL REPORTS
    SECOND_TYPE = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:first-child>div>ul[data-role="listview"]>li:nth-child(2)>a')  # MEDIA RELEASE
    THIRD_TYPE = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:first-child>div>ul[data-role="listview"]>li:nth-child(3)>a')  # REPORT_FOR_TESTS
    FOURTH_TYPE = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:first-child>div>ul[data-role="listview"]>li:nth-child(4)>a')  # SITUATION REPORT
    STATUS_FILTER = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:nth-child(2)>h2>a')
    FIRST_STATUS = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:nth-child(2)>div>ul[data-role="listview"]>li:first-child>a')  # ANY STATUS
    SECOND_STATUS = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:nth-child(2)>div>ul[data-role="listview"]>li:nth-child(2)>a')  # ACTIVE
    THIRD_STATUS = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:nth-child(2)>div>ul[data-role="listview"]>li:nth-child(3)>a')  # INACTIVE
    FOURTH_STATUS = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div[data-role="collapsible"]:nth-child(2)>div>ul[data-role="listview"]>li:nth-child(4)>a')  # DRAFT
    SEARCH_FIELD = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div.ui-input-search>input#reportSearch')
    CREATE_REPORT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-solo>li>a[href="#reportNew"]')
    EDIT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#reportView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.edit>a')
    FIRST_REPORT_ON_THE_LIST = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div.main>ul>li:first-child>a')
    MORE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#reportView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li:last-child>a[href="#reportViewMoreMenu"]')
    DELETE_REPORT = (MobileBy.CSS_SELECTOR, 'div#reportView>div.ui-popup-container>div#reportViewMoreMenu>ul>li.report.delete>a')
    EDIT_REPORT_TITLE = (MobileBy.CSS_SELECTOR, 'div#reportEdit>div.ui-content>ul.edit-view>li:first-child>div>input#title')
    DELETE_ALERT = (MobileBy.CSS_SELECTOR, 'div#reportView>div#confirmDeleteReport-popup>div#confirmDeleteReport>div.ng-dialog-container>div>div.ui-controlgroup-controls>a:first-child')
    ASSETS_CHOOSER_FIELD = (MobileBy.CSS_SELECTOR, 'div#reportEdit>div.ui-content>ul.edit-view>li[name="new assets chooser"]>div.ui-select>div')  # inside already created report
    CREATE_MAPPING_DATA = (MobileBy.CSS_SELECTOR, 'div#reportEdit>div.ui-content>ul.edit-view>li.geometryinput>a')
    SEQUENCE_ON_LOAD = (MobileBy.CSS_SELECTOR, 'div#reportNew>div.ui-content>ul.edit-view>li.ui-field-contain.ui-li-static.ui-body-inherit>label[for="on_load"]')
    SEQUENCE_ON_SAVE = (MobileBy.CSS_SELECTOR, 'div#reportNew>div.ui-content>ul.edit-view>li.ui-field-contain.ui-li-static.ui-body-inherit>label[for="on_save"]')
    # MEDIA_RELEASE_FIELD = (MobileBy.CSS_SELECTOR, '')  # rich text field must be located in native view
    OPTION_LIST = (MobileBy.CSS_SELECTOR, 'div#reportNew>div.ui-content>ul.edit-view>li[name="new option list"]>div.ui-select>div')
    CLEAR_SEARCH_FIELD_BUTTON = (MobileBy.CSS_SELECTOR, 'div#reportIndex>div.ui-content>div.ui-input-search>a.ui-input-clear')
    VIEW_ON_MAP_BUTTON = (MobileBy.CSS_SELECTOR, 'div#reportView>div.ui-content>ul.ui-listview>li>a[href="#mapPage?geometry=true"]')  # button inside report details


class SentScreen:
    """A class for handling Sent screen"""
    CLEAR_SEARCH_FIELD_BUTTON = (MobileBy.CSS_SELECTOR, 'div#sentComms>div.ui-content>div.ui-input-search>a.ui-input-clear')
    # SENT_COMMUNICATIONS_EMAIL = (MobileBy.CSS_SELECTOR, '')


class ComposeScreen:
    """A class for handling Compose screen"""
    ADD_RECIPIENTS_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#messageAddRecipients"]')
    MESSAGE_EMAIL = (MobileBy.CSS_SELECTOR, 'a[href="#messageEmail"]')
    EMAIL_SUBJECT_FIELD = (MobileBy.CSS_SELECTOR, 'input#emailSubject')
    EMAIL_TEXT_FIELD = (MobileBy.CSS_SELECTOR, 'iframe[title="Rich Text Editor, emailBody"]')
    EMAIL_OK = (MobileBy.CSS_SELECTOR, '#EmailOK')
    MESSAGE_SMS = (MobileBy.CSS_SELECTOR, 'a[href="#messageSMS"]')
    SMS_TEXT_FIELD = (MobileBy.CSS_SELECTOR, '#SMSBody')
    SMS_OK = (MobileBy.CSS_SELECTOR, '#SMSOK')
    MESSAGE_VOICE = (MobileBy.CSS_SELECTOR, 'a[href="#messageVoice"]')
    VOICE_TEXT_FIELD = (MobileBy.CSS_SELECTOR, '#voiceText')
    TEXT_TO_SPEECH_BUTTON = (MobileBy.CSS_SELECTOR, '#voiceTextMethod>a')
    VOICE_OK = (MobileBy.CSS_SELECTOR, '#voiceOK')
    MESSAGE_FAX = (MobileBy.CSS_SELECTOR, 'a[href="#messageFax"]')
    FAX_DOCUMENT_BUTTON = (MobileBy.CSS_SELECTOR, '#faxDocumentMethod')
    FAX_OK_BUTTON = (MobileBy.CSS_SELECTOR, 'div#messageFax>div[data-role="footer"]>div[data-role="navbar"]>ul>li.ui-block-a>a')
    COMMS_DOCUMENTS_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#documentfolderTreeView?selector=true&id=2"]')
    ADD_CONTACTS_AND_GROUPS = (MobileBy.CSS_SELECTOR, 'a.maywrap.ui-link.ui-btn.ui-shadow.ui-corner-all')  # list of two elements - select [0]
    ADD_RESOURCES_STRUCTURE_NODES = (MobileBy.CSS_SELECTOR, 'a.maywrap.ui-link.ui-btn.ui-shadow.ui-corner-all')  # list of two elements - select [1]
    # CONTACTS_ARROW = (MobileBy.CSS_SELECTOR, 'a[href="#contactgroupTreeView?selector=true&id=4"]')
    FIRST_ELEMENT_ARROW = (MobileBy.CSS_SELECTOR, 'div#contactgroupTreeView>div.ui-content>div.main>ul>li:first-child>a.ui-btn')
    CONTACT_FOR_APPIUM_TESTS = (MobileBy.CSS_SELECTOR, 'input[data-label="A_CONTACT_FOR_APPIUM_TESTS"]')
    SEND_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#confirmSendMessage"]')
    ALERT_SEND_BUTTON = (MobileBy.CSS_SELECTOR, 'div.ui-controlgroup-controls>a#messageSend')
    RECIPIENT_FIELD = (MobileBy.CSS_SELECTOR, 'div#messagePage>div.ui-content>ul.recipients>li.recipient')
    MORE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#messagePage>div.ui-footer>div.ui-navbar>ul.ui-grid-b>li.ui-block-c>a[href="#messageMore"]')
    DISCARD_MESSAGE = (MobileBy.CSS_SELECTOR, 'div#messagePage>div#messageMore-popup>div#messageMore>ul.ui-listview>li.ui-first-child>a[href="#confirmDiscard"]')
    CONFIRM_DISCARD_MESSAGE = (MobileBy.CSS_SELECTOR, 'div#messagePage>div#confirmDiscard-popup>div#confirmDiscard>div.ng-dialog-container>div.center-text>div>a#messageDiscard')


class RisksScreen:
    """A class for handling Risks screen"""
    CREATE_RISK_REGISTER = (MobileBy.CSS_SELECTOR, 'a[href="#riskregisterNew"]')
    NAME_FOR_NEW_RISK_REGISTER = (MobileBy.CSS_SELECTOR, 'input#name')
    CREATE_NEW_CONTEXT_INPUT_FIELD = (MobileBy.CSS_SELECTOR, 'input[id="or create new context"]')
    SAVE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#riskregisterNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                          'a[href="#save"]')
    CANCEL_BUTTON = (MobileBy.CSS_SELECTOR, 'div#riskregisterNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                            'a[href="#cancel"]')
    # PREVIOUSLY_CREATED_RISK_REGISTER = (MobileBy.CSS_SELECTOR, 'div#riskRegisterIndex>div.ui-content>ul.registers>li:first-child')  # not working on iOS 10
    # PREVIOUSLY_CREATED_CONTEXT = (MobileBy.CSS_SELECTOR, 'div#riskcontextTreeView>div.ui-content>ul.contexts>li:first-child')
    # PREVIOUSLY_CREATED_RISK = (MobileBy.CSS_SELECTOR, 'div#riskcontextTreeView>div.ui-content>ul.risks>li:first-child')
    LIBRARY_CONTROL = (MobileBy.CSS_SELECTOR, 'div#riskcontrollibraryTreeView>div.ui-content>ul.category>li:first-child')
    PREVIOUSLY_CREATED_RISK_REGISTER = (MobileBy.CSS_SELECTOR, 'ul.registers.listview.ui-listview>li>a')
    PREVIOUSLY_CREATED_CONTEXT = (MobileBy.CSS_SELECTOR, 'ul.contexts.listview.ui-listview>li>a')
    PREVIOUSLY_CREATED_RISK = (MobileBy.CSS_SELECTOR, 'ul.risks.listview.ui-listview>li>a')
    RISK_REGISTERS_LIST = (MobileBy.CSS_SELECTOR, 'ul.registers.listview.ui-listview>li:first-child>a')
    NEW_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#riskcontextTreeMoreMenu"]')
    ADD_NEW_CONTEXT = (MobileBy.CSS_SELECTOR, 'a[href="#riskcontextNew?parent=0"]')
    ADD_NEW_RISK = (MobileBy.CSS_SELECTOR, 'ul.context.footer.menu.ui-listview>li.new.risk>a')
    ADD_NEW_CONTEXT_IN_EXISTING_CONTEXT = (MobileBy.CSS_SELECTOR, 'ul.context.footer.menu.ui-listview>li.new.riskcontext>a')
    ADD_NEW_LIBRARY_RISK = (MobileBy.CSS_SELECTOR, 'ul.context.footer.menu.ui-listview>li.library>a')
    SEARCH_FIELD = (MobileBy.CSS_SELECTOR, 'input#riskregisterSearch')
    NAME_FOR_NEW_CONTEXT = (MobileBy.CSS_SELECTOR, 'div#riskcontextNew>div>ul>li.ui-field-contain.ui-li-static.ui-body-inherit>div>input#name')
    NAME_FOR_NEW_RISK = (MobileBy.CSS_SELECTOR, 'div#riskNew>div>ul>li>div>input#name')
    SAVE_NEW_CONTEXT = (MobileBy.CSS_SELECTOR, 'div#riskcontextNew>div[data-role="footer"]>div>ul>li>a[href="#save"]')
    SAVE_NEW_RISK = (MobileBy.CSS_SELECTOR, 'div#riskNew>div[data-role="footer"]>div>ul>li>a[href="#save"]')
    OK_BUTTON = (MobileBy.CSS_SELECTOR, 'div#risklibraryTreeView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.ui-block-a>a')
    OK_BUTTON_IN_RISK_CONTROL_LIBRARY = (MobileBy.CSS_SELECTOR, 'div#riskcontrollibraryTreeView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.ui-block-a>a')
    MORE_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#riskViewMoreMenu"]')
    ADD_NEW_CONTROL = (MobileBy.CSS_SELECTOR, 'li.new.control>a')
    ADD_LIBRARY_CONTROL = (MobileBy.CSS_SELECTOR, 'li.library.control>a')
    MARK_AS_REVIEWED = (MobileBy.CSS_SELECTOR, 'a[href="#confirmReviewRisk"]')
    DELETE_RISK = (MobileBy.CSS_SELECTOR, 'a[href="#confirmDeleteRisk"]')
    NAME_FOR_NEW_CONTROL = (MobileBy.CSS_SELECTOR, 'div#riskcontrolNew>div>ul.edit-view.ui-listview>li>div>input#name')
    STATUS_SELECTOR = (MobileBy.CSS_SELECTOR, 'div#field-101-button>select#field-101')
    SAVE_NEW_CONTROL = (MobileBy.CSS_SELECTOR, 'div#riskcontrolNew>div[data-role="footer"]>div>ul>li>a[href="#save"]')
    VIEW_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#riskcontextTreeViewMenu"]')
    VIEW_REGISTER_BUTTON = (MobileBy.CSS_SELECTOR, 'li.root.ui-last-child>a')
    REGISTER_VIEW = (MobileBy.CSS_SELECTOR, 'div#riskregisterView>div[data-role="main"]')
    DELETE_ALERT = (MobileBy.CSS_SELECTOR, 'div#confirmDeleteRisk>div.ng-dialog-container>div[data-role="controlgroup"]>div.ui-controlgroup-controls>a:first-child')
    REVIEW_ALERT = (MobileBy.CSS_SELECTOR, 'div#confirmReviewRisk>div.ng-dialog-container>div[data-role="controlgroup"]>div.ui-controlgroup-controls>a:first-child')
    RISK_LIBRARY = (MobileBy.CSS_SELECTOR, 'div#risklibraryTreeView>div.ui-content>ul.category>li:first-child>a')
    RISK_INSIDE_LIBRARY = (MobileBy.CSS_SELECTOR, 'div#risklibraryTreeView>div.ui-content>ul.item>li:first-child')
    CLEAR_SEARCH_FIELD_BUTTON = (MobileBy.CSS_SELECTOR, 'div#riskRegisterIndex>div.ui-content>div.ui-input-search>a.ui-input-clear')


class AssetsScreen:
    """A class for handling Assets screen"""
    NAME = (MobileBy.CSS_SELECTOR, 'div#assetNew>div.ui-content>ul.edit-view>li:first-child>div.ui-input-text>input#name')
    SAVE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#assetNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                          'a[href="#save"]')
    CANCEL_BUTTON = (MobileBy.CSS_SELECTOR, 'div#assetNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>'
                                            'a[href="#cancel"]')
    NEW_BUTTON = (MobileBy.CSS_SELECTOR, 'li#openAssetTreeMore>a[href="#assetTreeMore"]')
    NEW_ASSET_BUTTON = (MobileBy.CSS_SELECTOR, 'a[href="#assetNew?parent=0"]')
    ASSET_TYPE = (MobileBy.CSS_SELECTOR, 'div#assetNew>div.ui-content>ul>li:first-child>a')  # first asset type on the list
    PREVIOUSLY_CREATED_ASSET = (MobileBy.CSS_SELECTOR, 'div#assetTreeView>div.ui-content>div.main>ul[data-role="listview"]>li:first-child>a')
    PREVIOUSLY_CREATED_ASSET_CHECKBOX = (MobileBy.CSS_SELECTOR, 'div#assetTreeView>div.ui-content>div.main>ul[data-role="listview"]>li:first-child>div.ui-checkbox')  # whole list element - not just link
    EDIT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#assetView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.edit>a')
    COST_PER_UNIT_FIELD = (MobileBy.CSS_SELECTOR, 'div#assetEdit>div.ui-content>ul.edit-view>li>div>input[id="cost per unit"]')
    SAVE_EDITED_ASSET = (MobileBy.CSS_SELECTOR, 'div#assetEdit>div[data-role="footer"]>div[data-role="navbar"]>ul>li>a[href="#save"]')
    MORE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#assetView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.ui-block-b>a[href="#assetViewMoreMenu"]')
    DELETE_THIS_ASSET = (MobileBy.CSS_SELECTOR, 'div#assetView>div#assetViewMoreMenu-popup>div#assetViewMoreMenu>ul>li.delete>a[href="#confirmDeleteAsset"]')
    NEW_CHILD_ASSET = (MobileBy.CSS_SELECTOR, 'div#assetView>div#assetViewMoreMenu-popup>div#assetViewMoreMenu>ul>li.new>a')
    DELETE_ALERT = (MobileBy.CSS_SELECTOR, 'div#assetView>div#confirmDeleteAsset-popup>div#confirmDeleteAsset>div.ng-dialog-container>div>div.ui-controlgroup-controls>a:first-child')
    CANCEL_ALERT = (MobileBy.CSS_SELECTOR, 'div#assetView>div#confirmDeleteAsset-popup>div#confirmDeleteAsset>div.ng-dialog-container>div>div.ui-controlgroup-controls>a:last-child')
    PREVIOUSLY_CREATED_CHILD_ASSET = (MobileBy.CSS_SELECTOR, 'div#assetTreeView>div.ui-content>div.main>ul.assets>li:first-child>a')
    CHILD_ASSET_INSIDE_OTHER_ASSET = (MobileBy.CSS_SELECTOR, 'div#assetTreeView>div.ui-content>div.main>ul>li:first-child>a')
    SEARCH_FIELD = (MobileBy.CSS_SELECTOR, 'div#assetTreeView>div.ui-content>div.filters>div>input[id="assetSearch"]')
    CREATE_MAPPING_DATA = (MobileBy.CSS_SELECTOR, 'div#assetNew>div.ui-content>ul.edit-view>li.geometryinput>a')
    ADD_MEDIA_BUTTON = (MobileBy.CSS_SELECTOR, 'div#assetNew>div.ui-content>ul.edit-view>li.ui-li-static.ui-body-inherit>div.addmedia.edit-mode>a')
    CLEAR_SEARCH_FIELD_BUTTON = (MobileBy.CSS_SELECTOR, 'div#assetTreeView>div.ui-content>div.filters>div.ui-input-search>a.ui-input-clear')
    VIEW_ON_MAP_BUTTON = (MobileBy.CSS_SELECTOR, 'div#assetView>div.ui-content>ul.ui-listview>li>a[href="#mapPage?geometry=true"]')  # button inside assets details


class LogsScreen(EventsScreen, AssetsScreen):
    """A class for handling New Log screen"""
    CREATE_NEW_LOG = (MobileBy.CSS_SELECTOR, 'div#logIndex>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-solo>li.ui-block-a>a[href="#logNew"]')
    SAVE_NEW_LOG = (MobileBy.CSS_SELECTOR, 'div#logNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>a[href="#save"]')
    SAVE_EDITED_LOG = (MobileBy.CSS_SELECTOR, 'div#logEdit>div[data-role="footer"]>div[data-role="navbar"]>ul>li>a[href="#save"]')
    CANCEL_BUTTON = (MobileBy.CSS_SELECTOR, 'div#logNew>div[data-role="footer"]>div[data-role="navbar"]>ul>li>a[href="#cancel"]')  # cancel button for new log
    NEW_LOG_LODGING_AGENCY_PICKER = (MobileBy.CSS_SELECTOR, 'div#logNew>div.ui-content>ul.edit-view>li:nth-child(2)>div.ui-select>div.ui-btn>select[name="lodging agency"]')  # not working on iOS 10
    EDIT_LOG_LODGING_AGENCY_PICKER = (MobileBy.CSS_SELECTOR, 'div#logEdit>div.ui-content>ul.edit-view>li:nth-child(2)>div.ui-select>div.ui-btn>select[name="lodging agency"]')
    ENTRY_FIELD = (MobileBy.CSS_SELECTOR, 'iframe[title="Rich Text Editor, entry"]')  # not working on iOS10
    TYPES_FILTER = (MobileBy.CSS_SELECTOR, 'div#logIndex>div.ui-content>div[data-role="collapsible"]>h2>a')
    FIRST_FILTER = (MobileBy.CSS_SELECTOR, 'div#logIndex>div.ui-content>div[data-role="collapsible"]>div>ul>li:first-child>a')
    SECOND_FILTER = (MobileBy.CSS_SELECTOR, 'div#logIndex>div.ui-content>div[data-role="collapsible"]>div>ul>li:nth-child(2)>a')
    THIRD_FILTER = (MobileBy.CSS_SELECTOR, 'div#logIndex>div.ui-content>div[data-role="collapsible"]>div>ul>li:nth-child(3)>a')
    FIRST_LOG_ON_THE_LIST = (MobileBy.CSS_SELECTOR, 'div#logIndex>div.ui-content>div.main>ul.logs.listview.ui-listview>li.summary-listing:first-child>a')
    EDIT_BUTTON = (MobileBy.CSS_SELECTOR, 'div#logView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.edit>a')
    MORE_BUTTON = (MobileBy.CSS_SELECTOR, 'div#logView>div[data-role="footer"]>div[data-role="navbar"]>ul.ui-grid-a>li.ui-block-b>a[href="#logViewMoreMenu"]')
    DELETE_LOG = (MobileBy.CSS_SELECTOR, 'div#logView>div.ui-popup-container>div#logViewMoreMenu>ul>li.log.delete>a')
    DELETE_ALERT = (MobileBy.CSS_SELECTOR, 'div#logView>div#confirmDeleteLog-popup>div#confirmDeleteLog>div.ng-dialog-container>div>div.ui-controlgroup-controls>a:first-child')
    EVENT_CHOOSER_FIELD = (MobileBy.CSS_SELECTOR, 'div#logNew>div.ui-content>ul.edit-view>li[name="event(s)"]>div.ui-select')  # events chooser field inside new log
    ASSET_CHOOSER_FIELD = (MobileBy.CSS_SELECTOR, 'div#logNew>div.ui-content>ul.edit-view>li[name="asset(s)"]>div.ui-select')
    FIRST_EVENT_ON_THE_LIST = EventsScreen.PREVIOUSLY_CREATED_EVENT_CHECKBOX
    FIRST_ASSET_ON_THE_LIST = AssetsScreen.PREVIOUSLY_CREATED_ASSET_CHECKBOX
    # LOG_TYPE_WITH_ALL_FIELDS = (MobileBy.CSS_SELECTOR, '')  # native element
    # LOG_TYPE_WITH_CHOOSER_FIELDS = (MobileBy.CSS_SELECTOR, '')  # native element
    LOG_CHOOSER_FIELD_INSIDE_NEW_LOG = (MobileBy.CSS_SELECTOR, 'div#logNew>div.ui-content>ul.edit-view>li[name="new log entries chooser"]>div.ui-select>div')  # inside new log
    LOG_CHOOSER_FIELD = (MobileBy.CSS_SELECTOR, 'div#logEdit>div.ui-content>ul.edit-view>li[name="new log entries chooser"]>div.ui-select>div')  # inside existing log
    PREVIOUSLY_CREATED_LOG_CHECKBOX = (MobileBy.CSS_SELECTOR, 'div#logIndex>div.ui-content>div.main>ul[data-role="listview"]>li:first-child>div.ui-checkbox')  # whole list element - not just link
    SEQUENCE_ON_LOAD = (MobileBy.CSS_SELECTOR, 'div#logNew>div.ui-content>ul.edit-view>li.ui-field-contain.ui-li-static.ui-body-inherit>label[for="on_load"]')
    SEQUENCE_ON_SAVE = (MobileBy.CSS_SELECTOR, 'div#logNew>div.ui-content>ul.edit-view>li.ui-field-contain.ui-li-static.ui-body-inherit>label[for="on_save"]')
    OPTION_LIST = (MobileBy.CSS_SELECTOR, 'div#logNew>div.ui-content>ul.edit-view>li[name="new option list"]>div.ui-select>div')
    CLEAR_SEARCH_FIELD_BUTTON = (MobileBy.CSS_SELECTOR, 'div#logIndex>div.ui-content>div.ui-input-search>a.ui-input-clear')


class SelectMediaScreen:
    """A class for handling Select Media Screen"""
    TAKE_PHOTO = (MobileBy.CSS_SELECTOR, 'div#filesystemMediaSelect>div.ui-content>div.ui-grid-a>div#filePhotoCapture>div.center-text>span.icon')
    RECORD_VIDEO = (MobileBy.CSS_SELECTOR, 'div#filesystemMediaSelect>div.ui-content>div.ui-grid-a>div#fileVideoCapture>div.center-text>span.icon')
    RECORD_AUDIO = (MobileBy.CSS_SELECTOR, 'div#filesystemMediaSelect>div.ui-content>div.ui-grid-a>div#fileAudioCapture>div.center-text>span.icon')
    VIDEO_GALLERY = (MobileBy.CSS_SELECTOR, 'div#filesystemMediaSelect>div.ui-content>div.ui-grid-a>div#fileVideoGallery>div.center-text>span.icon')
    PHOTO_GALLERY = (MobileBy.CSS_SELECTOR, 'div#filesystemMediaSelect>div.ui-content>div.ui-grid-a>div#filePhotoGallery>div.center-text>span.icon')
