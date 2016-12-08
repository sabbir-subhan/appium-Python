# Test Case 3 - Managing events

import unittest
from appium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from desired_capabilities import DesiredCapabilities
import credentials
from locators import *
from generators import RandomGenerator
import logging
logging.basicConfig(filename='/Users/lukasl/repos/appium-poc/OCAapp_TC3.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.getLogger().addHandler(logging.StreamHandler())


class TC3android(unittest.TestCase):
    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")

        # choose desired capabilities from desired_capabilities.py
        desired_capabilities = DesiredCapabilities.desired_capabilities_for_android_6

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
        self.driver.implicitly_wait(25)  # seconds

    def tearDown(self):
        logging.info("Quitting")
        self.driver.quit()

    def login(self):
        logging.info("starting def with login")
        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON).click()

        logging.info("typing username, password and OCA domain")

        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME).send_keys(credentials.QA_username)

        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD).send_keys(credentials.QA_password)

        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN).send_keys(credentials.domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON).click()

        logging.info("accept Terms if needed")
        try:
            self.driver.find_element(*LoginScreen.ACCEPT_BUTTON).click()
            logging.info("Accept button is present")
            sleep(10)
        except NoSuchElementException:
            logging.info("Terms are already accepted - Accept button is not present")

        logging.info("check if Notice alert is present and click Ok button")
        try:
            self.driver.find_element(*LoginScreen.NOTICE_ALERT_OK_BUTTON).click()
            logging.info("Notice alert is present")
        except NoSuchElementException:
            logging.info("Notice alert is not present")
            pass

        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located(MainMenuScreen.EVENTS_BUTTON), "Failed to login")
            logging.info("Successful login")
        except NoSuchElementException:
            logging.info("Failed to login")
            self.fail("Failed to login")

    def scroll_down(self):

        logging.info("scroll down")
        action = TouchAction(self.driver)

        elm1 = self.driver.find_element(*EventEditScreen.FINISHED_HEADER)
        action.press(elm1).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)
        elm2 = self.driver.find_element(*EventEditScreen.LEADAGENCY_HEADER)
        action.press(elm2).perform()
        action.move_to(x=0, y=100).perform()
        sleep(3)
        elm3 = self.driver.find_element(*EventEditScreen.IMPACT_HEADER)
        action.press(elm3).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm4 = self.driver.find_element(*EventEditScreen.CAUSE_HEADER)
        action.press(elm4).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm5 = self.driver.find_element(*EventEditScreen.SITUATION_HEADER)
        action.press(elm5).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm6 = self.driver.find_element(*EventEditScreen.ISSUES_HEADER)
        action.press(elm6).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm7 = self.driver.find_element(*EventEditScreen.OBJECTIVES_HEADER)
        action.press(elm7).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm8 = self.driver.find_element(*EventEditScreen.STRATEGIES_HEADER)
        action.press(elm8).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm9 = self.driver.find_element(*EventEditScreen.TACTICS_HEADER)
        action.press(elm9).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm10 = self.driver.find_element(*EventEditScreen.COMMUNICATIONS_HEADER)
        action.press(elm10).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm11 = self.driver.find_element(*EventEditScreen.RELATED_HEADER)
        action.press(elm11).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)

    def test1(self):
        logging.info("TC info: filter events, create first Event and delete it")

        self.login()

        sleep(3)
        logging.info("clicking on Events button")
        events_button = self.driver.find_element(*MainMenuScreen.EVENTS_BUTTON).click()

        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*EventsScreen.EVENTS_HEADER)
        self.assertIsNotNone(events_header)

        logging.info("filtering events by Type")
        any_type_expand = self.driver.find_element(*EventsScreen.ANY_TYPE_EXPAND).click()
        choose_type_incident = self.driver.find_element(*EventsScreen.CHOOSE_TYPE_INCIDENT).click()
        sleep(1)
        incident_type_expand = self.driver.find_element(*EventsScreen.INCIDENT_TYPE_EXPAND).click()
        choose_type_any = self.driver.find_element(*EventsScreen.CHOOSE_TYPE_ANY).click()
        sleep(1)

        logging.info("filtering events by Status")
        any_status_expand = self.driver.find_element(*EventsScreen.ANY_STATUS_EXPAND).click()
        choose_active_status = self.driver.find_element(*EventsScreen.CHOOSE_ACTIVE_STATUS).click()
        sleep(1)
        active_status_expand = self.driver.find_element(*EventsScreen.ACTIVE_STATUS_EXPAND).click()
        choose_inactive_status = self.driver.find_element(*EventsScreen.CHOOSE_INACTIVE_STATUS).click()
        sleep(1)
        inactive_status_expand = self.driver.find_element(*EventsScreen.INACTIVE_STATUS_EXPAND).click()
        choose_draft_status = self.driver.find_element(*EventsScreen.CHOOSE_DRAFT_STATUS).click()
        sleep(1)
        draft_status_expand = self.driver.find_element(*EventsScreen.DRAFT_STATUS_EXPAND).click()
        choose_any_status = self.driver.find_element(*EventsScreen.CHOOSE_ANY_STATUS).click()
        sleep(2)

        logging.info("search field - search event named: 'search'")
        search_field = self.driver.find_element(*EventsScreen.SEARCH_FIELD)
        search_field.send_keys("search")
        sleep(3)
        logging.info("click Go on keyboard")
        self.driver.keyevent(66)
        sleep(3)
        logging.info("click on Events header to see results and hide keyboard")
        events_header_after_search = self.driver.find_element(*EventsScreen.EVENTS_HEADER_AFTER_SEARCH).click()

        logging.info("clear search field")
        self.driver.find_element(*EventsScreen.SEARCH_FIELD).click()
        self.driver.keyevent(67)
        self.driver.keyevent(67)
        self.driver.keyevent(67)
        self.driver.keyevent(67)
        self.driver.keyevent(67)
        self.driver.keyevent(67)
        sleep(1)
        logging.info("click on Events header to hide keyboard")
        events_header_after_search = self.driver.find_element(*EventsScreen.EVENTS_HEADER_AFTER_SEARCH).click()
        sleep(3)

        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element(*EventsScreen.MORE_BUTTON).click()

        logging.info("clicking on New event button")
        new_event_button = self.driver.find_element(*EventsScreen.NEW_EVENT_BUTTON).click()
        sleep(3)

        try:
            event_type = self.driver.find_element(*TypesOfEventsScreen.INCIDENT_TYPE_OF_EVENT).click()
            logging.info("choosing Incident type of new event")
        except NoSuchElementException:
            pass

        logging.info("filling form to create new event")
        logging.info("input Name")
        name_field = self.driver.find_element(*EventEditScreen.NAME_FIELD).send_keys("Test Appium")
        self.driver.hide_keyboard()

        logging.info("click on severity level field")
        severity_level_selector = self.driver.find_element(*EventEditScreen.SEVERITY_LEVEL_SELECTOR).click()
        sleep(2)

        logging.info("choose_severity_lvl1")
        choose_severity_lvl = self.driver.find_element(*EventEditScreen.CHOOSE_SEVERITY_LVL1).click()

        logging.info("click on finished_field")
        finished_field = self.driver.find_element(*EventEditScreen.FINISHED_FIELD).click()

        logging.info("choose time and date")
        time_date = self.driver.find_element(*EventEditScreen.TIME_DATE).click()
        set_button = self.driver.find_element(*EventEditScreen.SET_BUTTON).click()

        action = TouchAction(self.driver)
        self.scroll_down()

        logging.info("Save event")
        save_button = self.driver.find_element(*EventEditScreen.SAVE_BUTTON).click()
        sleep(10)

        logging.info("open created event")
        created_event = self.driver.find_element(*EventsScreen.CREATED_EVENT_1).click()
        sleep(5)

        logging.info("edit previously created event")
        edit_button = self.driver.find_element(*EventDetailsScreen.EDIT_BUTTON).click()
        sleep(5)

        logging.info("scroll down to Description field")
        elm1 = self.driver.find_element(*EventEditScreen.FINISHED_HEADER)
        action.press(elm1).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)
        elm2 = self.driver.find_element(*EventEditScreen.LEADAGENCY_HEADER)
        action.press(elm2).perform()
        action.move_to(x=0, y=100).perform()
        sleep(3)

        try:
            logging.info("type some text into description field")
            description_field = self.driver.find_element(*EventEditScreen.DESCRIPTION_FIELD).send_keys("test")
            sleep(2)
            self.driver.hide_keyboard()
        except NoSuchElementException:
            logging.info("text field couldn't be selected")
            pass

        elm3 = self.driver.find_element(*EventEditScreen.IMPACT_HEADER)
        action.press(elm3).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm4 = self.driver.find_element(*EventEditScreen.CAUSE_HEADER)
        action.press(elm4).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm5 = self.driver.find_element(*EventEditScreen.SITUATION_HEADER)
        action.press(elm5).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm6 = self.driver.find_element(*EventEditScreen.ISSUES_HEADER)
        action.press(elm6).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm7 = self.driver.find_element(*EventEditScreen.OBJECTIVES_HEADER)
        action.press(elm7).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm8 = self.driver.find_element(*EventEditScreen.STRATEGIES_HEADER)
        action.press(elm8).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm9 = self.driver.find_element(*EventEditScreen.TACTICS_HEADER)
        action.press(elm9).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm10 = self.driver.find_element(*EventEditScreen.COMMUNICATIONS_HEADER)
        action.press(elm10).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)
        elm11 = self.driver.find_element(*EventEditScreen.RELATED_HEADER)
        action.press(elm11).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)

        logging.info("Save event")
        save_button = self.driver.find_element(*EventEditScreen.SAVE_BUTTON).click()

        logging.info("clicking on 'More' button")
        more_button =self.driver.find_element(*EventsScreen.MORE_BUTTON).click()
        sleep(3)

        logging.info("clicking on 'Delete event' button")
        delete__event_button = self.driver.find_element(*EventDetailsScreen.DELETE_EVENT_BUTTON).click()

        logging.info("confirm delete")
        delete_confirm_button = self.driver.find_element(*EventDetailsScreen.DELETE_CONFIRM_BUTTON).click()
        sleep(5)

    def test2(self):
        logging.info("TC info: create second event and add map")

        self.login()

        sleep(3)
        logging.info("clicking on Events button")
        events_button = self.driver.find_element(*MainMenuScreen.EVENTS_BUTTON).click()

        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*EventsScreen.EVENTS_HEADER)
        self.assertIsNotNone(events_header)

        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element(*EventsScreen.MORE_BUTTON).click()

        logging.info("clicking on New event button")
        new_event_button = self.driver.find_element(*EventsScreen.NEW_EVENT_BUTTON).click()
        sleep(3)

        try:
            event_type = self.driver.find_element(*TypesOfEventsScreen.INCIDENT_TYPE_OF_EVENT).click()
            logging.info("choosing Incident type of new event")
        except NoSuchElementException:
            pass

        logging.info("filling form to create new event")
        logging.info("input Name")
        name_field = self.driver.find_element(*EventEditScreen.NAME_FIELD).send_keys("Test Appium - second event")
        self.driver.hide_keyboard()

        logging.info("click on severity level field")
        severity_level_selector = self.driver.find_element(*EventEditScreen.SEVERITY_LEVEL_SELECTOR).click()
        sleep(2)

        logging.info("choose_severity_lvl4")
        choose_severity_lvl = self.driver.find_element(*EventEditScreen.CHOOSE_SEVERITY_LVL4).click()

        logging.info("click on finished_field")
        finished_field = self.driver.find_element(*EventEditScreen.FINISHED_FIELD).click()

        logging.info("choose time and date")
        time_date = self.driver.find_element(*EventEditScreen.TIME_DATE).click()
        set_button = self.driver.find_element(*EventEditScreen.SET_BUTTON).click()

        action = TouchAction(self.driver)
        self.scroll_down()

        logging.info("Save event")
        save_button = self.driver.find_element(*EventEditScreen.SAVE_BUTTON).click()
        sleep(10)

        logging.info("open previously created Event, Edit and Create mapping data")
        logging.info("open created event")
        created_event = self.driver.find_element(*EventsScreen.CREATED_EVENT_2).click()
        sleep(5)

        logging.info("edit previously created event")
        edit_button = self.driver.find_element(*EventDetailsScreen.EDIT_BUTTON).click()
        sleep(5)

        self.scroll_down()

        create_mapping_data_button = self.driver.find_element(*EventEditScreen.CREATE_MAPPING_DATA).click()
        logging.info("wait for map")
        sleep(10)

        logging.info("add point into the map")
        tool_button = self.driver.find_element(*Map.TOOL_BUTTON)
        self.assertIsNotNone(tool_button, "Tool button is not present")
        tool_button.click()
        point_button = self.driver.find_element(*Map.POINT_BUTTON).click()
        point_default_button = self.driver.find_element(*Map.DEFAULT_BUTTON).click()
        add_point_into_map = self.driver.find_element(*Map.ADD_POINT_INTO_MAP)
        action.tap(add_point_into_map).perform()

        logging.info("add line into the map")
        tool_button = self.driver.find_element(*Map.TOOL_BUTTON).click()
        line_button = self.driver.find_element(*Map.LINE_BUTTON).click()
        line_default_button = self.driver.find_element(*Map.DEFAULT_BUTTON).click()
        add_line1 = self.driver.find_element(*Map.ADD_LINE1)
        add_line2 = self.driver.find_element(*Map.ADD_LINE2)
        action.tap(add_line1).perform()
        sleep(3)
        action.tap(add_line2).perform()
        action.tap(add_line2).perform()

        logging.info("add circle into the map")
        tool_button = self.driver.find_element(*Map.TOOL_BUTTON).click()
        circle_button = self.driver.find_element(*Map.CIRCLE_BUTTON).click()
        circle_default_button = self.driver.find_element(*Map.DEFAULT_BUTTON).click()
        add_circle_on_map = self.driver.find_element(*Map.ADD_CIRCLE_INTO_MAP)
        action.tap(add_circle_on_map).perform()

        logging.info("add polygon into the map")
        tool_button = self.driver.find_element(*Map.TOOL_BUTTON).click()
        polygon_button = self.driver.find_element(*Map.POLYGON_BUTTON).click()
        polygon_default_button = self.driver.find_element(*Map.DEFAULT_BUTTON).click()
        add_polygon1 = self.driver.find_element(*Map.ADD_POLYGON1)
        action.tap(add_polygon1).perform()
        add_polygon2 = self.driver.find_element(*Map.ADD_POLYGON2)
        action.tap(add_polygon2).perform()
        add_polygon3 = self.driver.find_element(*Map.ADD_POLYGON3)
        sleep(3)
        action.tap(add_polygon3).perform()
        action.tap(add_polygon3).perform()
        # self.driver.save_screenshot("screen.png")

        logging.info("Save map")
        save_map_button = self.driver.find_element(*Map.SAVE_MAP_BUTTON).click()
        sleep(3)
        edit_mapping_data_button = self.driver.find_element(*EventEditScreen.EDIT_MAPPING_DATA)
        self.assertTrue(edit_mapping_data_button, "Map was not saved correctly")
        logging.info("Save event")
        save_button = self.driver.find_element(*EventEditScreen.SAVE_BUTTON).click()
        sleep(5)

    def test3(self):
        logging.info("TC info: crete sub event, set event as primary and after that clear it")

        self.login()

        sleep(3)
        logging.info("clicking on Events button")
        events_button = self.driver.find_element(*MainMenuScreen.EVENTS_BUTTON).click()

        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*EventsScreen.EVENTS_HEADER)
        self.assertIsNotNone(events_header)

        # before creating sub event - normal event is necessary
        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element(*EventsScreen.MORE_BUTTON).click()

        logging.info("clicking on New event button")
        new_event_button = self.driver.find_element(*EventsScreen.NEW_EVENT_BUTTON).click()
        sleep(3)

        try:
            event_type = self.driver.find_element(*TypesOfEventsScreen.INCIDENT_TYPE_OF_EVENT).click()
            logging.info("choosing Incident type of new event")
        except NoSuchElementException:
            pass

        logging.info("filling form to create new event")
        logging.info("input Name")
        name_field = self.driver.find_element(*EventEditScreen.NAME_FIELD).send_keys("Test to create sub event")
        self.driver.hide_keyboard()

        logging.info("click on severity level field")
        severity_level_selector = self.driver.find_element(*EventEditScreen.SEVERITY_LEVEL_SELECTOR).click()
        sleep(2)

        logging.info("choose_severity_lvl3")
        choose_severity_lvl = self.driver.find_element(*EventEditScreen.CHOOSE_SEVERITY_LVL3).click()

        logging.info("click on finished_field")
        finished_field = self.driver.find_element(*EventEditScreen.FINISHED_FIELD).click()

        logging.info("choose time and date")
        time_date = self.driver.find_element(*EventEditScreen.TIME_DATE).click()
        set_button = self.driver.find_element(*EventEditScreen.SET_BUTTON).click()

        self.scroll_down()

        logging.info("Save event")
        save_button = self.driver.find_element(*EventEditScreen.SAVE_BUTTON).click()
        sleep(5)

        logging.info("open created event")
        created_event = self.driver.find_element(*EventsScreen.CREATED_EVENT_3).click()
        sleep(5)

        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element(*EventsScreen.MORE_BUTTON).click()

        logging.info("clicking on 'New sub event' button")
        new_sub_event = self.driver.find_element(*EventDetailsScreen.NEW_SUB_EVENT).click()
        sleep(3)

        try:
            event_type = self.driver.find_element(*TypesOfEventsScreen.INCIDENT_TYPE_OF_EVENT).click()
            logging.info("choosing Incident type of new event")
        except NoSuchElementException:
            pass

        logging.info("input Name for new sub event")
        name_field = self.driver.find_element(*EventEditScreen.NAME_FIELD).send_keys("Test Appium - sub event")
        self.driver.hide_keyboard()

        logging.info("click on severity level field")
        severity_level_selector = self.driver.find_element(*EventEditScreen.SEVERITY_LEVEL_SELECTOR).click()
        sleep(2)

        logging.info("choose_severity_lvl2")
        choose_severity_lvl = self.driver.find_element(*EventEditScreen.CHOOSE_SEVERITY_LVL2).click()

        logging.info("click on finished_field")
        finished_field = self.driver.find_element(*EventEditScreen.FINISHED_FIELD).click()

        logging.info("choose time and date")
        time_date = self.driver.find_element(*EventEditScreen.TIME_DATE).click()
        set_button = self.driver.find_element(*EventEditScreen.SET_BUTTON).click()

        self.scroll_down()

        logging.info("Save event")
        save_button = self.driver.find_element(*EventEditScreen.SAVE_BUTTON).click()
        sleep(5)

        # logging.info("open any of previously created events")
        # created_event = self.driver.find_element(*EventsScreen.CREATED_EVENT_1).click()
        # sleep(5)

        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element(*EventsScreen.MORE_BUTTON).click()

        logging.info("clicking on 'Set as primary' button")
        set_as_primary_button = self.driver.find_element(*EventDetailsScreen.SET_AS_PRIMARY_BUTTON).click()
        sleep(2)

        logging.info("go back to main menu")
        arrow_back = self.driver.find_element(*EventsScreen.GO_BACK_TO_MAIN_MENU_ARROW_BUTTON).click()
        sleep(2)

        logging.info("clicking on Events button")
        events_button = self.driver.find_element(*MainMenuScreen.EVENTS_BUTTON).click()

        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*EventsScreen.EVENTS_HEADER)
        self.assertIsNotNone(events_header)

        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element(*EventsScreen.MORE_BUTTON).click()
        sleep(5)

        logging.info("clicking on 'Clear primary event' button")
        clear_primary_event_button = self.driver.find_element(*EventsScreen.CLEAR_PRIMARY_EVENT_BUTTON).click()

        logging.info("checking notification - 'Primary event cleared'")
        notification = self.driver.find_element(*EventsScreen.NOTIFICATION_PRIMARY_EVENT_CLEARED)
        self.assertIsNotNone(notification)

        logging.info("check if Events are opene")
        self.assertIsNotNone(events_header)

        logging.info("create new type of event, but do not save it - event with on load and on save sequence"
                     " and hidden fields")
        sleep(1)
        self.driver.find_element(*EventsScreen.MORE_BUTTON).click()
        self.driver.find_element(*EventsScreen.NEW_EVENT_BUTTON).click()

        logging.info("choose type of event = event_for_on_load/save_test")
        self.driver.find_element(*TypesOfEventsScreen.EVENT_FOR_ON_LOAD_SAVE).click()

        logging.info("assert on load and on save sequence")
        sequence_onload_header = self.driver.find_element(*EventEditScreen.SEQUENCE_ONLOAD_HEADER)
        self.assertIsNotNone(sequence_onload_header)
        sequence_onload_value = self.driver.find_element(*EventEditScreen.SEQUENCE_ONLOAD_VALUE)
        self.assertIsNotNone(sequence_onload_value)
        sequence_onsave_header = self.driver.find_element(*EventEditScreen.SEQUENCE_ONSAVE_HEADER)
        sequence_onsave_value = self.driver.find_element(*EventEditScreen.SEQUENCE_ONSAVE_VALUE)
        self.assertIsNotNone(sequence_onsave_header)
        self.assertIsNotNone(sequence_onsave_value)

        logging.info("scroll down")
        action = TouchAction(self.driver)
        elm3 = self.driver.find_element(*EventEditScreen.LEADAGENCY_HEADER)
        action.press(elm3).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)

        logging.info("add hidden fields, click on option list")
        new_option_list = self.driver.find_element(*EventEditScreen.NEW_OPTION_LIST_HEADER).click()
        logging.info("choose '1' in option list")
        self.driver.find_element(*EventEditScreen.OPTION_LIST_VALUE_1).click()
        sleep(0.5)
        field_to_restore_1_header = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_1_HEADER)
        self.assertIsNotNone(field_to_restore_1_header)
        field_to_restore_1_value = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_1_VALUE)
        self.assertIsNotNone(field_to_restore_1_value)
        sleep(1)
        logging.info("click on option list")
        new_option_list = self.driver.find_element(*EventEditScreen.NEW_OPTION_LIST_HEADER).click()
        sleep(0.5)
        logging.info("choose '2' in option list")
        self.driver.find_element(*EventEditScreen.OPTION_LIST_VALUE_2).click()
        sleep(3)
        logging.info("assert restored field")
        field_to_restore_2_header = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE__2_HEADER)
        self.assertIsNotNone(field_to_restore_2_header)
        field_to_restore_2_value = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_2_VALUE)
        self.assertIsNotNone(field_to_restore_2_value)

        logging.info("assert hidden field")
        try:
            # field_to_restore_1_header = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_1_HEADER)
            if field_to_restore_1_header.is_displayed():
                self.fail("field was not hidden correctly")
        except:
            logging.info("field is not visible = OK")
            pass

        logging.info("click on option list")
        new_option_list = self.driver.find_element(*EventEditScreen.NEW_OPTION_LIST_HEADER).click()
        logging.info("choose '3' in option list")
        self.driver.find_element(*EventEditScreen.OPTION_LIST_VALUE_3).click()

        logging.info("assert hidden fields")
        try:
            if field_to_restore_1_header.is_displayed():
                self.fail("field was not hidden correctly")
            if field_to_restore_2_header.is_displayed():
                self.fail("field was not hidden correctly")
        except:
            logging.info("fields are not visible = OK")
            pass

        logging.info("scroll down")
        elm3 = self.driver.find_element(*EventEditScreen.RELATED_HEADER)
        action.press(elm3).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)

        logging.info("click on Cancel button")
        self.driver.find_element(*EventEditScreen.CANCEL_BUTTON).click()

        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*EventsScreen.EVENTS_HEADER)
        self.assertIsNotNone(events_header)

        logging.info("create new type of event, but do not save it - event with chooser field for another event "
                     "and sub form with chooser field")
        logging.info("click More button")
        self.driver.find_element(*EventsScreen.MORE_BUTTON).click()

        logging.info("click New Event button")
        self.driver.find_element(*EventsScreen.NEW_EVENT_BUTTON).click()

        logging.info("choose type of event = event for chooser fields")
        self.driver.find_element(*TypesOfEventsScreen.EVENT_FOR_CHOOSER_FIELDS).click()

        logging.info("scroll down")
        elm3 = self.driver.find_element(*EventEditScreen.LEADAGENCY_HEADER)
        action.press(elm3).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)

        logging.info("choose previously created event for chooser field")
        self.driver.find_element(*EventEditScreen.CHOOSER_FIELD).click()
        sleep(1)
        self.driver.find_element(*EventEditScreen.PREVIOUSLY_CREATED_EVENT_FOR_CHOOSER).click()

        logging.info("choose event inside sub form")
        self.driver.find_element(*EventEditScreen.SUBFORM_FIELD_ADD_ROW).click()
        self.driver.find_element(*EventEditScreen.NEW_EVENTS_CHOOSER_IN_SUB_FORM).click()
        sleep(1)
        previously_created_event_for_subform_chooser = self.driver.find_element(
            *EventEditScreen.PREVIOUSLY_CREATED_EVENT_FOR_CHOOSER).click()
        sleep(1)
        logging.info("clear sub for with event chooser")
        self.driver.find_element(*EventEditScreen.DELETE_SUB_EVENT_FROM_CHOOSER).click()
        self.assertIsNone(previously_created_event_for_subform_chooser)

        logging.info("scroll down")
        elm3 = self.driver.find_element(*EventEditScreen.RELATED_HEADER)
        action.press(elm3).perform()
        action.move_to(x=0, y=100).perform()
        sleep(1)

        logging.info("click on Cancel button")
        self.driver.find_element(*EventEditScreen.CANCEL_BUTTON).click()

        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*EventsScreen.EVENTS_HEADER)
        self.assertIsNotNone(events_header)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TC3android)
    unittest.TextTestRunner(verbosity=2).run(suite)
