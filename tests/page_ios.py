from selenium.common.exceptions import NoSuchElementException
import unittest
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from credentials import Credentials
import logging
logging.basicConfig(filename='/Users/lukasl/repos/appium-poc/TCs.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.getLogger().addHandler(logging.StreamHandler())


class BasePage(unittest.TestCase):
    """
    :type driver: appium.webdriver.Remote
    """

    def __init__(self, driver):

        super().__init__()
        self.driver = driver


class iOSdevice(BasePage):

    def hide_keyboard(self):

        logging.info("hide keyboard")
        try:
            done_button_ios = self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD)
            if done_button_ios.is_displayed():
                self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD).click()
        except NoSuchElementException:
            self.driver.hide_keyboard(key_name="Hide keyboard")

    def click_Return_button_on_keyboard(self):

        logging.info("click 'Return' on keyboard")
        self.driver.find_element(*iOSkeyboard.RETURN_BUTTON).click()
        sleep(1)

    def alert_allow_location(self):

        button_allow_location = self.driver.find_element(*Map.BUTTON_ALLOW_LOCATION_ios)
        if button_allow_location.is_displayed():
            logging.info("Accept using location - device will store that info for later use")
            button_allow_location.click()
        else:
            pass


class WelcomePage(BasePage):

    def click_login_button(self):

        sleep(7)
        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_ios).click()


class LoginPage(BasePage):

    def type_username(self, username):

        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).clear()
        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).send_keys(Credentials.get_username(username))

    def type_password(self, password):

        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).clear()
        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).send_keys(Credentials.get_password(password))

    def type_domain_address(self, domain):

        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).clear()
        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).send_keys(Credentials.get_domain(domain))

    def click_submit_button(self):

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON_ios).click()

    def accept_terms(self):

        logging.info("check Terms and Conditions")
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

    def alert_wrong_password(self):

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*LoginScreen.ALERT_MSG_INVALID_ios)
            self.assertIsNotNone(alert_msg)
            self.driver.find_element(*LoginScreen.OK_BUTTON_ios).click()
            logging.info("Successfully try to login using incorrect credentials - message alert is present")
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")

    def alert_expired_password(self):

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*LoginScreen.ALERT_MSG_EXPIRED_ios)
            logging.info("Successfully try to login to account that expired 1 day ago - message alert is present")
            self.assertIsNotNone(alert_msg)
            self.driver.find_element(*LoginScreen.OK_BUTTON_ios).click()
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")

    def alert_suspended_account(self):

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*LoginScreen.ALERT_MSG_SUSPENDED_ios)
            logging.info("Successfully try to login into suspended account - message alert is present")
            self.assertIsNotNone(alert_msg)
            self.driver.find_element(*LoginScreen.OK_BUTTON_ios).click()
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")


class MainPage(BasePage):

    def dismiss_ios_notifications(self):

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

    def logout_if_already_logged_in(self):

        sleep(5)
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

    def alert_expiring_password(self):

        logging.info("check if Notice alert, about expiring password, is present")
        try:
            self.driver.find_element(*LoginScreen.ALERT_MSG_WILL_EXPIRE_ios)
            self.assertIsNotNone(*LoginScreen.ALERT_MSG_WILL_EXPIRE_ios)
            logging.info("Notice alert is present")
            self.driver.find_element(*LoginScreen.OK_BUTTON_ios).click()
        except NoSuchElementException:
            logging.info("Notice alert is not present")
            pass

    def check_presence_of_events_button(self):

        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located(MainMenuScreen.EVENTS_BUTTON_ios), "Failed to login")
            logging.info("Successful login")
        except NoSuchElementException:
            logging.info("Failed to login")
            self.fail("Failed to login")

    def open_EVENTS(self):

        logging.info("clicking on Events button")
        self.driver.find_element(*MainMenuScreen.EVENTS_BUTTON_ios).click()
        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*EventsScreen.EVENTS_HEADER_ios)
        self.assertIsNotNone(events_header)


class EventsPage(BasePage):

    def filter_events_by_Type(self):

        logging.info("filtering events by Type")
        any_type_expand = self.driver.find_element(*EventsScreen.ANY_TYPE_EXPAND_ios).click()
        choose_type_incident = self.driver.find_element(*EventsScreen.CHOOSE_TYPE_INCIDENT_ios).click()
        sleep(0.5)
        incident_type_expand = self.driver.find_element(*EventsScreen.INCIDENT_TYPE_EXPAND_ios).click()
        choose_type_any = self.driver.find_element(*EventsScreen.CHOOSE_TYPE_ANY_ios).click()
        sleep(0.5)

    def filter_events_by_Status(self):

        logging.info("filtering events by Status")
        any_status_expand = self.driver.find_element(*EventsScreen.ANY_STATUS_EXPAND_ios).click()
        choose_active_status = self.driver.find_element(*EventsScreen.CHOOSE_ACTIVE_STATUS_ios).click()
        sleep(0.5)
        active_status_expand = self.driver.find_element(*EventsScreen.ACTIVE_STATUS_EXPAND_ios).click()
        choose_inactive_status = self.driver.find_element(*EventsScreen.CHOOSE_INACTIVE_STATUS_ios).click()
        sleep(0.5)
        inactive_status_expand = self.driver.find_element(*EventsScreen.INACTIVE_STATUS_EXPAND_ios).click()
        choose_draft_status = self.driver.find_element(*EventsScreen.CHOOSE_DRAFT_STATUS_ios).click()
        sleep(0.5)
        draft_status_expand = self.driver.find_element(*EventsScreen.DRAFT_STATUS_EXPAND_ios).click()
        choose_any_status = self.driver.find_element(*EventsScreen.CHOOSE_ANY_STATUS_ios).click()
        sleep(0.5)

    def filter_events_by_Search_field(self):

        logging.info("search field - search event named: 'search'")
        self.driver.find_element(*EventsScreen.SEARCH_FIELD_ios).click()
        self.driver.find_element(*EventsScreen.SEARCH_FIELD_ios).clear()
        self.driver.find_element(*EventsScreen.SEARCH_FIELD_ios).send_keys("search")

    def clear_Search_field(self):

        logging.info("clear search field")
        self.driver.find_element(*EventsScreen.SEARCH_FIELD_ios).click()
        self.driver.find_element(*EventsScreen.SEARCH_FIELD_ios).clear()
        sleep(1)

    def click_More_button(self):

        logging.info("clicking on 'More' button")
        self.driver.find_element(*EventsScreen.MORE_BUTTON_ios).click()

    def click_New_event_button(self):

        logging.info("clicking on New event button")
        self.driver.find_element(*EventsScreen.NEW_EVENT_BUTTON_ios).click()
        sleep(0.5)

    def open_previously_created_event1(self):

        logging.info("open created event")
        created_event = self.driver.find_element(*EventsScreen.CREATED_EVENT_1_ios).click()
        sleep(5)

    def open_previously_created_event2(self):

        logging.info("open previously created Event, Edit and Create mapping data")
        created_event = self.driver.find_element(*EventsScreen.CREATED_EVENT_2_ios).click()
        sleep(5)


class EventsTypesPage(BasePage):

    def choose_Incident_type_of_event(self):

        event_type_incident = self.driver.find_element(*TypesOfEventsScreen.INCIDENT_TYPE_OF_EVENT_ios)
        self.assertIsNotNone(event_type_incident)
        logging.info("choosing Incident type of new event")
        event_type_incident.click()

    def choose_Event_for_on_load_save_type_of_event(self):

        event_type_onload = self.driver.find_element(*TypesOfEventsScreen.EVENT_FOR_ON_LOAD_SAVE_ios)
        self.assertIsNotNone(event_type_onload)
        logging.info("choose type of event = event_for_on_load/save_test")
        event_type_onload.click()

    def choose_Event_for_chooser_fields_type_of_event(self):

        event_type_chooser = self.driver.find_element(*TypesOfEventsScreen.EVENT_FOR_CHOOSER_FIELDS_ios)
        self.assertIsNotNone(event_type_chooser)
        logging.info("choose type of event = event for chooser fields")
        event_type_chooser.click()


class EventEditPage(BasePage):

    def fill_name_input_field(self, text):

        logging.info("filling form to create new event - input Name")
        self.driver.find_element(*EventEditScreen.NAME_FIELD_ios).click()
        # name_field = self.driver.find_element(*EventEditScreen.NAME_FIELD_ios).send_keys("Test Appium iOS")
        name_field = self.driver.find_element(*EventEditScreen.NAME_FIELD_ios).send_keys(text)

    def click_severity_lvl_picker(self):

        try:
            logging.info("click on severity level field")
            severity_level_selector = self.driver.find_element(*EventEditScreen.SEVERITY_LEVEL_SELECTOR_ios).click()
        except NoSuchElementException:
            pass

    def choose_severity_level_1(self):

        try:
            logging.info("choose_severity_lvl1")
            choose_severity_lvl1 = self.driver.find_element(*EventEditScreen.CHOOSE_SEVERITY_LVL1_iPad)
            if choose_severity_lvl1.is_displayed():
                choose_severity_lvl1.click()
            else:
                # NEED A WAY TO SCROLL WHEEL PICKER ON iPhones, scroll, tap and move, click on element, send keys are not working - this step is not required in TC
                # try to use self.driver.swipe
                pass
        except NoSuchElementException:
            pass
        sleep(1)

    def choose_severity_level_2(self):

        try:
            logging.info("choose_severity_lvl2")
            choose_severity_lvl2 = self.driver.find_element(*EventEditScreen.CHOOSE_SEVERITY_LVL2_iPad)
            if choose_severity_lvl2.is_displayed():
                choose_severity_lvl2.click()
            else:
                pass
        except NoSuchElementException:
            pass
        sleep(1)
        
    def choose_severity_level_3(self):

        try:
            logging.info("choose_severity_lvl3")
            choose_severity_lvl3 = self.driver.find_element(*EventEditScreen.CHOOSE_SEVERITY_LVL3_iPad)
            if choose_severity_lvl3.is_displayed():
                choose_severity_lvl3.click()
            else:
                pass
        except NoSuchElementException:
            pass
        sleep(1)
        
    def choose_severity_level_4(self):
        
        try:
            logging.info("choose_severity_lvl4")
            choose_severity_lvl4 = self.driver.find_element(*EventEditScreen.CHOOSE_SEVERITY_LVL4_iPad)
            if choose_severity_lvl4.is_displayed():
                choose_severity_lvl4.click()
            else:
                pass
        except NoSuchElementException:
            pass
        sleep(1)
        
    def type_text_into_description_field(self):

        try:
            logging.info("type some text into description field")
            self.driver.find_element(*EventEditScreen.DESCRIPTION_FIELD_ios).click()
            self.driver.find_element(*EventEditScreen.DESCRIPTION_FIELD_ios).send_keys("test ios")
        except NoSuchElementException:
            logging.info("text field couldn't be selected")
            pass

    def click_create_mapping_data(self):

        logging.info("create mapping data")
        create_mapping_data_button = self.driver.find_element(*EventEditScreen.CREATE_MAPPING_DATA_ios)
        self.assertIsNotNone(create_mapping_data_button, "Button for creating map data is not present")
        create_mapping_data_button.click()

    def save_event(self):

        logging.info("Save event")
        save_button = self.driver.find_element(*EventEditScreen.SAVE_BUTTON_ios)
        self.assertIsNotNone(save_button)
        save_button.click()
        sleep(5)


class Map(BasePage):

    def click_tool_button(self):

        tool_button = self.driver.find_element(*Map.TOOL_BUTTON_ios)
        self.assertIsNotNone(tool_button, "Tool button is not present")
        tool_button.click()


class EventDetailsPage(BasePage):

    def click_edit_button(self):

        logging.info("edit previously created event")
        edit_button = self.driver.find_element(*EventDetailsScreen.EDIT_BUTTON_ios)
        self.assertIsNotNone(edit_button)
        edit_button.click()
        sleep(2)

    def click_Delete_button(self):

        logging.info("clicking on 'Delete event' button")
        delete__event_button = self.driver.find_element(*EventDetailsScreen.DELETE_EVENT_BUTTON_ios)
        self.assertIsNotNone(delete__event_button)
        delete__event_button.click()

    # def click_More_button(self):
    #
    #     sleep(1)
    #     logging.info("clicking on 'More' button")
    #     more_button = self.driver.find_element(*EventsScreen.MORE_BUTTON_ios)
    #     self.assertIsNotNone(more_button)
    #     more_button.click()
    #     sleep(1)

    def alert_confirm_delete(self):

        logging.info("confirm delete")
        delete_confirm_button = self.driver.find_element(*EventDetailsScreen.DELETE_CONFIRM_BUTTON_ios)
        self.assertIsNotNone(delete_confirm_button)
        delete_confirm_button.click()
        sleep(5)


