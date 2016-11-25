# Test Case 3 - Managing events

import unittest
from appium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction
# from appium.webdriver.common.multi_action import MultiAction
from desired_capabilities import DesiredCapabilities
import credentials
from locators import *
# from generators import RandomGenerator
import logging
logging.basicConfig(filename='OCAapp_TC3.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.getLogger().addHandler(logging.StreamHandler())


class TC3ios(unittest.TestCase):
    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")
        desired_capabilities = DesiredCapabilities.desired_capabilities_for_iOS_iPad

        # choose desired capabilities from desired_capabilities.py
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
        self.driver.implicitly_wait(25)  # seconds

    def tearDown(self):
        logging.info("Quitting")
        self.driver.quit()

    def login(self):

        sleep(2)
        try:
            logout_button_ios = self.driver.find_element(*MainMenuScreen.LOGOUT_BUTTON_ios)
            if logout_button_ios.is_displayed():
                logging.info("Your are already login - logging out")
                self.driver.find_element(*MainMenuScreen.LOGOUT_BUTTON_ios).click()
                self.driver.find_element(*LoginScreen.SUBMIT_BUTTON_ios).click()
            else:
                pass
        except NoSuchElementException:
            pass

        logging.info("starting def with login")
        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_ios).click()

        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).clear()
        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).send_keys(credentials.QA_username)

        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).clear()
        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).send_keys(credentials.QA_password)

        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).clear()
        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).send_keys(credentials.domain)

        # TRY TO USE ONLY key_name  ON BOTH IPHONE4, 5, 6, AND IPAD
        try:
            done_button_ios = self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD)
            if done_button_ios.is_displayed():
                logging.info("hide screen keyboard")
                self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD).click()
            else:
                self.driver.hide_keyboard(key_name="Hide keyboard")
        except NoSuchElementException:
            pass

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON_ios).click()

        try:
            accept_terms_button = self.driver.find_element(*LoginScreen.ACCEPT_BUTTON_ios)
            if accept_terms_button.is_displayed():
                self.driver.find_element(*LoginScreen.ACCEPT_BUTTON_ios).click()
                logging.info("Accepting terms and conditions")
                sleep(10)
            else:
                logging.info("Terms are already accepted - Accept button is not present")
        except NoSuchElementException:
            pass

        try:
            notification_msg_on_ios = self.driver.find_element(*LoginScreen.NOTIFICATION_ABOUT_SENDING_MESSAGES_ios)
            if notification_msg_on_ios.is_displayed():
                logging.info("click 'No' for sending notifications on iOS")
                notification_msg_on_ios = self.driver.find_element(
                    *LoginScreen.NOTIFICATION_ABOUT_SENDING_MESSAGES_ios)
                self.assertIsNotNone(notification_msg_on_ios)
                self.driver.find_element(*LoginScreen.NO_FOR_SENDING_NOTIFICATIONS_ON_ios).click()
            else:
                pass
        except NoSuchElementException:
            pass

        # THERE IS PROBLEM WITH DISPLAYING ALERT ON IOS - it's visible only for few seconds
        # logging.info("check if Notice alert, about expiring password is present and click Ok button")
        # try:
        #     self.driver.find_element(*LoginScreen.ALERT_MSG_WILL_EXPIRE_ios)
        #     logging.info("Notice alert is present")
        #     self.driver.find_element(*LoginScreen.NOTICE_ALERT_OK_BUTTON_ios).click()
        # except NoSuchElementException:
        #     logging.info("Notice alert is not present")
        #     pass

        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located(MainMenuScreen.EVENTS_BUTTON_ios), "Failed to login")
            logging.info("Successful login")
        except NoSuchElementException:
            logging.info("Failed to login")
            self.fail("Failed to login")

    def scroll_down(self):

        logging.info("scroll down to find element")
        element_on_the_list = None
        try:
            element_on_the_list = self.driver.find_element(*EventEditScreen.SAVE_BUTTON_ios)
            # that is element what You are looking for
        except Exception as e:
            element_to_scroll = self.driver.find_element(*EventEditScreen.ELEMENT_TO_SCROLL_ios)
            # that is id/xpath/name of whole list
            scrollobject = dict(direction="down", name="Save", element=element_to_scroll)
            self.driver.execute_script("mobile: scrollTo", scrollobject)

        # if element_on_the_list is None:
        #     element_on_the_list = self.driver.find_element_by_xpath(*EventEditScreen.SAVE_BUTTON_ios)

    def test1(self):
        logging.info("TC info: filter events, create first Event and delete it")

        self.login()

        sleep(3)
        logging.info("clicking on Events button")
        self.driver.find_element(*MainMenuScreen.EVENTS_BUTTON_ios).click()

        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*EventsScreen.EVENTS_HEADER_ios)
        self.assertIsNotNone(events_header)

        logging.info("filtering events by Type")
        any_type_expand = self.driver.find_element(*EventsScreen.ANY_TYPE_EXPAND_ios).click()
        choose_type_incident = self.driver.find_element(*EventsScreen.CHOOSE_TYPE_INCIDENT_ios).click()
        #sleep(1)
        incident_type_expand = self.driver.find_element(*EventsScreen.INCIDENT_TYPE_EXPAND_ios).click()
        choose_type_any = self.driver.find_element(*EventsScreen.CHOOSE_TYPE_ANY_ios).click()
        #sleep(1)

        logging.info("filtering events by Status")
        any_status_expand = self.driver.find_element(*EventsScreen.ANY_STATUS_EXPAND_ios).click()
        choose_active_status = self.driver.find_element(*EventsScreen.CHOOSE_ACTIVE_STATUS_ios).click()
        #sleep(1)
        active_status_expand = self.driver.find_element(*EventsScreen.ACTIVE_STATUS_EXPAND_ios).click()
        choose_inactive_status = self.driver.find_element(*EventsScreen.CHOOSE_INACTIVE_STATUS_ios).click()
        #sleep(1)
        inactive_status_expand = self.driver.find_element(*EventsScreen.INACTIVE_STATUS_EXPAND_ios).click()
        choose_draft_status = self.driver.find_element(*EventsScreen.CHOOSE_DRAFT_STATUS_ios).click()
        #sleep(1)
        draft_status_expand = self.driver.find_element(*EventsScreen.DRAFT_STATUS_EXPAND_ios).click()
        choose_any_status = self.driver.find_element(*EventsScreen.CHOOSE_ANY_STATUS_ios).click()
        #sleep(1)

        logging.info("search field - search event named: 'search'")
        self.driver.find_element(*EventsScreen.SEARCH_FIELD_ios).click()
        self.driver.find_element(*EventsScreen.SEARCH_FIELD_ios).clear()
        self.driver.find_element(*EventsScreen.SEARCH_FIELD_ios).send_keys("search")

        logging.info("click 'Return' on keyboard")
        self.driver.find_element(*iOSkeyboard.RETURN_BUTTON).click()

        #sleep(1)
        logging.info("hide keyboard")
        self.driver.hide_keyboard(key_name="Hide keyboard")

        logging.info("clear search field")
        self.driver.find_element(*EventsScreen.SEARCH_FIELD_ios).click()
        self.driver.find_element(*EventsScreen.SEARCH_FIELD_ios).clear()

        self.driver.find_element(*iOSkeyboard.RETURN_BUTTON).click()
        self.driver.hide_keyboard(key_name="Hide keyboard")

        logging.info("clicking on 'More' button")
        self.driver.find_element(*EventsScreen.MORE_BUTTON_ios).click()

        logging.info("clicking on New event button")
        self.driver.find_element(*EventsScreen.NEW_EVENT_BUTTON_ios).click()
        #sleep(3)

        try:
            event_type = self.driver.find_element(*TypesOfEventsScreen.INCIDENT_TYPE_OF_EVENT_ios).click()
            logging.info("choosing Incident type of new event")
        except NoSuchElementException:
            pass

        logging.info("filling form to create new event")
        logging.info("input Name")
        self.driver.find_element(*EventEditScreen.NAME_FIELD_ios).click()
        name_field = self.driver.find_element(*EventEditScreen.NAME_FIELD_ios).send_keys("Test Appium ios")
        self.driver.hide_keyboard(key_name="Hide keyboard")

        logging.info("click on severity level field")
        severity_level_selector = self.driver.find_element(*EventEditScreen.SEVERITY_LEVEL_SELECTOR_ios).click()
        #sleep(2)

        logging.info("choose_severity_lvl1")
        choose_severity_lvl = self.driver.find_element(*EventEditScreen.CHOOSE_SEVERITY_LVL1_ios).click()

        #action = TouchAction(self.driver)
        self.scroll_down()

        logging.info("Save event")
        save_button = self.driver.find_element(*EventEditScreen.SAVE_BUTTON_ios).click()
        sleep(2)

        logging.info("open created event")
        created_event = self.driver.find_element(*EventsScreen.CREATED_EVENT_1_ios).click()
        #sleep(5)

        logging.info("edit previously created event")
        edit_button = self.driver.find_element(*EventDetailsScreen.EDIT_BUTTON_ios).click()
        #sleep(5)

        logging.info("scroll down to Description field")
        element_on_the_list = None
        try:
            element_on_the_list = self.driver.find_element(*EventEditScreen.DESCRIPTION_FIELD_ios)
            # that is element what You are looking for
        except Exception as e:
            element_to_scroll = self.driver.find_element(*EventEditScreen.ELEMENT_TO_SCROLL_ios)
            # that is id/xpath/name of whole list
            scrollobject = dict(direction="down", name="Save", element=element_to_scroll)
            self.driver.execute_script("mobile: scrollTo", scrollobject)

        try:
            logging.info("type some text into description field")
            self.driver.find_element(*EventEditScreen.DESCRIPTION_FIELD_ios).click()
            self.driver.find_element(*EventEditScreen.DESCRIPTION_FIELD_ios).send_keys("test ios")
            self.driver.hide_keyboard(key_name="Hide keyboard")
        except NoSuchElementException:
            logging.info("text field couldn't be selected")
            pass

        self.scroll_down()

        logging.info("Save event")
        save_button = self.driver.find_element(*EventEditScreen.SAVE_BUTTON_ios).click()

        sleep(3)
        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element(*EventsScreen.MORE_BUTTON_ios).click()
        #sleep(3)

        logging.info("clicking on 'Delete event' button")
        delete__event_button = self.driver.find_element(*EventDetailsScreen.DELETE_EVENT_BUTTON_ios).click()
        logging.info("confirm delete")
        delete_confirm_button = self.driver.find_element(*EventDetailsScreen.DELETE_CONFIRM_BUTTON_ios).click()
        sleep(5)

    def test2(self):
        logging.info("TC info: create second event and add map")

        self.login()

        #sleep(3)
        logging.info("clicking on Events button")
        EVENTS_BUTTON_ios = self.driver.find_element(*MainMenuScreen.EVENTS_BUTTON_ios).click()

        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*EventsScreen.EVENTS_HEADER_ios)
        self.assertIsNotNone(events_header)

        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element(*EventsScreen.MORE_BUTTON_ios).click()

        logging.info("clicking on New event button")
        new_event_button = self.driver.find_element(*EventsScreen.NEW_EVENT_BUTTON_ios).click()
        sleep(3)

        try:
            event_type = self.driver.find_element(*TypesOfEventsScreen.INCIDENT_TYPE_OF_EVENT_ios).click()
            logging.info("choosing Incident type of new event")
        except NoSuchElementException:
            pass

        logging.info("filling form to create new event")
        logging.info("input Name")
        name_field = self.driver.find_element(*EventEditScreen.NAME_FIELD_ios).send_keys(
            "Test Appium ios - second event")

        logging.info("hide keyboard")
        self.driver.hide_keyboard(key_name="Hide keyboard")

        logging.info("click on severity level field")
        severity_level_selector = self.driver.find_element(*EventEditScreen.SEVERITY_LEVEL_SELECTOR_ios).click()
        sleep(2)

        logging.info("choose_severity_lvl4")
        choose_severity_lvl = self.driver.find_element(*EventEditScreen.CHOOSE_SEVERITY_LVL4_ios).click()

        # logging.info("choose time and date")
        # time_date = self.driver.find_element(*EventEditScreen.TIME_DATE).click()
        # set_button = self.driver.find_element(*EventEditScreen.SET_BUTTON).click()

        action = TouchAction(self.driver)
        self.scroll_down()

        logging.info("Save event")
        save_button = self.driver.find_element(*EventEditScreen.SAVE_BUTTON_ios).click()
        sleep(10)

        logging.info("open previously created Event, Edit and Create mapping data")
        logging.info("open created event")
        created_event = self.driver.find_element(*EventsScreen.CREATED_EVENT_2_ios).click()
        sleep(5)

        logging.info("edit previously created event")
        edit_button = self.driver.find_element(*EventDetailsScreen.EDIT_BUTTON_ios).click()
        sleep(5)

        self.scroll_down()

        create_mapping_data_buton = self.driver.find_element(*EventEditScreen.CREATE_MAPPING_DATA_ios).click()
        logging.info("wait for map")
        sleep(10)
        logging.info("add point into the map")
        tool_button = self.driver.find_element(*Map.TOOL_BUTTON_ios).click()
        poin_button = self.driver.find_element(*Map.POINT_BUTTON_ios).click()
        poin_default_button = self.driver.find_element(*Map.POINT_DEFAULT_BUTTON_ios).click()
        add_point_into_map = self.driver.find_element(*Map.ADD_POINT_INTO_MAP_ios).click()
        sleep(1)
        logging.info("add line into the map")
        tool_button = self.driver.find_element(*Map.TOOL_BUTTON_ios).click()
        line_button = self.driver.find_element(*Map.LINE_BUTTON_ios).click()
        line_default_button = self.driver.find_element(*Map.LINE_DEFAULT_BUTTON_ios).click()
        add_line1 = self.driver.find_element(*Map.ADD_LINE1_ios).click()
        add_line2 = self.driver.find_element(*Map.ADD_LINE2_ios).click()
        action.tap(add_line2).perform()
        action.tap(add_line2).perform()
        sleep(3)

        logging.info("add circle into the map")
        tool_button = self.driver.find_element(*Map.TOOL_BUTTON_ios).click()
        circle_button = self.driver.find_element(*Map.CIRCLE_BUTTON_ios).click()
        circle_default_button = self.driver.find_element(*Map.CIRCLE_DEFAULT_BUTTON_ios).click()
        add_circle_on_map = self.driver.find_element(*Map.ADD_CIRCLE_INTO_MAP_ios).click()
        sleep(1)

        logging.info("add polygon into the map")
        tool_button = self.driver.find_element(*Map.TOOL_BUTTON_ios).click()
        polygon_button = self.driver.find_element(*Map.POLYGON_BUTTON_ios).click()
        polygon_default_button = self.driver.find_element(*Map.POLYGON_DEFAULT_BUTTON_ios).click()
        add_polygon1 = self.driver.find_element(*Map.ADD_POLYGON1_ios).click()
        add_polygon2 = self.driver.find_element(*Map.ADD_POLYGON2_ios).click()
        add_polygon3 = self.driver.find_element(*Map.ADD_POLYGON3_ios).click()
        action.tap(add_polygon3).perform()
        action.tap(add_polygon3).perform()
        sleep(3)
        # self.driver.save_screenshot("screen.png")

        logging.info("Save map")
        save_map_button = self.driver.find_element(*Map.SAVE_MAP_BUTTON_ios).click()
        sleep(3)
        logging.info("Save event")
        save_button = self.driver.find_element(*EventEditScreen.SAVE_BUTTON_ios).click()
        sleep(5)

    def test3(self):
        logging.info("TC info: crete sub event, set event as primary and after that clear it")

        self.login()

        sleep(3)
        logging.info("clicking on Events button")
        EVENTS_BUTTON_ios = self.driver.find_element(*MainMenuScreen.EVENTS_BUTTON_ios).click()

        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*EventsScreen.EVENTS_HEADER_ios)
        self.assertIsNotNone(events_header)

        # before creating sub event - normal event is necessary
        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element(*EventsScreen.MORE_BUTTON_ios).click()

        logging.info("clicking on New event button")
        new_event_button = self.driver.find_element(*EventsScreen.NEW_EVENT_BUTTON_ios).click()
        sleep(3)

        try:
            event_type = self.driver.find_element(*TypesOfEventsScreen.INCIDENT_TYPE_OF_EVENT_ios).click()
            logging.info("choosing Incident type of new event")
        except NoSuchElementException:
            pass

        logging.info("filling form to create new event")
        logging.info("input Name")
        name_field = self.driver.find_element(*EventEditScreen.NAME_FIELD_ios).send_keys("Test ios to create sub event")

        logging.info("hide keyboard")
        self.driver.hide_keyboard(key_name="Hide keyboard")

        logging.info("click on severity level field")
        severity_level_selector = self.driver.find_element(*EventEditScreen.SEVERITY_LEVEL_SELECTOR_ios).click()
        sleep(2)

        logging.info("choose_severity_lvl3")
        choose_severity_lvl = self.driver.find_element(*EventEditScreen.CHOOSE_SEVERITY_LVL3_ios).click()

        # logging.info("choose time and date")
        # time_date = self.driver.find_element(*EventEditScreen.TIME_DATE).click()
        # set_button = self.driver.find_element(*EventEditScreen.SET_BUTTON).click()

        self.scroll_down()

        logging.info("Save event")
        save_button = self.driver.find_element(*EventEditScreen.SAVE_BUTTON_ios).click()
        sleep(5)

        logging.info("open created event")
        created_event = self.driver.find_element(*EventsScreen.CREATED_EVENT_3_ios).click()
        sleep(5)

        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element(*EventsScreen.MORE_BUTTON_ios).click()

        logging.info("clicking on 'New sub event' button")
        new_sub_event = self.driver.find_element(*EventDetailsScreen.NEW_SUB_EVENT_ios).click()
        sleep(3)

        try:
            event_type = self.driver.find_element(*TypesOfEventsScreen.INCIDENT_TYPE_OF_EVENT_ios).click()
            logging.info("choosing Incident type of new event")
        except NoSuchElementException:
            pass

        logging.info("input Name for new sub event")
        name_field = self.driver.find_element(*EventEditScreen.NAME_FIELD_ios).send_keys("Test ios to create sub event")

        logging.info("hide keyboard")
        self.driver.hide_keyboard(key_name="Hide keyboard")

        logging.info("click on severity level field")
        severity_level_selector = self.driver.find_element(*EventEditScreen.SEVERITY_LEVEL_SELECTOR_ios).click()
        sleep(2)

        logging.info("choose_severity_lvl2")
        choose_severity_lvl = self.driver.find_element(*EventEditScreen.CHOOSE_SEVERITY_LVL2_ios).click()

        # logging.info("choose time and date")
        # time_date = self.driver.find_element(*EventEditScreen.TIME_DATE).click()
        # set_button = self.driver.find_element(*EventEditScreen.SET_BUTTON).click()

        self.scroll_down()

        logging.info("Save event")
        save_button = self.driver.find_element(*EventEditScreen.SAVE_BUTTON_ios).click()
        sleep(5)

        logging.info("open any of previously created events")
        created_event = self.driver.find_element(*EventsScreen.CREATED_EVENT_1_ios).click()
        sleep(5)

        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element(*EventsScreen.MORE_BUTTON_ios).click()

        logging.info("clicking on 'Set as primary' button")
        set_as_primary_button = self.driver.find_element(*EventDetailsScreen.SET_AS_PRIMARY_BUTTON_ios).click()
        sleep(2)

        logging.info("go back to main menu")
        arrow_back = self.driver.find_element(*EventsScreen.GO_BACK_TO_MAIN_MENU_ARROW_BUTTON_ios).click()
        sleep(2)

        logging.info("clicking on Events button")
        EVENTS_BUTTON_ios = self.driver.find_element(*MainMenuScreen.EVENTS_BUTTON_ios).click()

        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*EventsScreen.EVENTS_HEADER_ios)
        self.assertIsNotNone(events_header)

        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element(*EventsScreen.MORE_BUTTON_ios).click()
        sleep(5)

        logging.info("clicking on 'Clear primary event' button")
        clear_primary_event_button = self.driver.find_element(*EventsScreen.CLEAR_PRIMARY_EVENT_BUTTON_ios).click()

        logging.info("checking notification - 'Primary event cleared'")
        notification = self.driver.find_element(*EventsScreen.NOTIFICATION_PRIMARY_EVENT_CLEARED_ios)
        self.assertIsNotNone(notification)

        sleep(5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TC3ios)
    unittest.TextTestRunner(verbosity=2).run(suite)
