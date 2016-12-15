# from appium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
from selenium.common.exceptions import NoSuchElementException
import unittest
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction
from locators_android import *
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

    # OCA top bar
    def hamburger_button(self):

        logging.info("click hamburger button to go back to main menu")
        try:
            hamburger_button = self.driver.find_element(*TopBar.HAMBURGER_FOR_MAIN_MENU)
            self.assertIsNotNone(hamburger_button, "Hamburger button is not present")
            if hamburger_button.is_displayed():
                hamburger_button.click()
            else:
                pass
            # probably that element cannot be clicked because attribute visible is "false"
        except NoSuchElementException:
            positions_for_hamburger_button = [(730, 20)]
            sleep(1)
            self.driver.tap(positions_for_hamburger_button)
        sleep(2)


class AndroidDevice(BasePage):

    def hide_keyboard(self):

        try:
            logging.info("hide screen keyboard")
            self.driver.hide_keyboard()
            sleep(3)
        except NoSuchElementException:
            logging.info("screen keyboard not found")

    def click_Go_button_on_keyboard(self):

        logging.info("click Go on keyboard")
        self.driver.keyevent(66)
        sleep(3)

    def alert_allow_location(self):

        try:
            button_allow_location = self.driver.find_element(*Android.BUTTON_ALLOW_LOCATION)
            if button_allow_location.is_displayed():
                logging.info("Accept using location - device will store that info for later use")
                button_allow_location.click()
            else:
                pass
        except NoSuchElementException:
            pass


class WelcomePage(BasePage):

    def click_login_button(self):

        logging.info("click in LOGIN button")
        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located(WelcomeScreen.LOGIN_BUTTON),
                "Login button not found")
            self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON).click()
        except NoSuchElementException:
            self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_by_index).click()


class LoginPage(BasePage):

    def type_username(self, username):

        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME).clear()
        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME).send_keys(Credentials.get_username(username))

    def type_password(self, password):

        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD).clear()
        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD).send_keys(Credentials.get_password(password))

    def type_domain_address(self, domain):

        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN).clear()
        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN).send_keys(Credentials.get_domain(domain))

    def click_submit_button(self):

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON).click()

    def accept_terms(self):

        logging.info("check Terms and Conditions")
        try:
            accept_terms_button = self.driver.find_element(*LoginScreen.ACCEPT_BUTTON)
            if accept_terms_button.is_displayed():
                self.assertIsNotNone(accept_terms_button, "accept button not found")
                logging.info("Accepting terms and conditions")
                accept_terms_button.click()
                sleep(10)
            else:
                pass
        except NoSuchElementException:
            logging.info("Terms are already accepted - Accept button is not present")

    def alert_wrong_password(self):

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*LoginScreen.ALERT_MSG_INVALID)
            self.assertIsNotNone(alert_msg)
            self.driver.find_element(*LoginScreen.OK_BUTTON).click()
            logging.info("Successfully try to login using incorrect credentials - message alert is present")
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")

    def alert_expired_password(self):

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*LoginScreen.ALERT_MSG_EXPIRED)
            logging.info("Successfully try to login to account that expired 1 day ago - message alert is present")
            self.assertIsNotNone(alert_msg)
            self.driver.find_element(*LoginScreen.OK_BUTTON).click()
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")

    def alert_suspended_account(self):

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*LoginScreen.ALERT_MSG_SUSPENDED)
            logging.info("Successfully try to login into suspended account - message alert is present")
            self.assertIsNotNone(alert_msg)
            self.driver.find_element(*LoginScreen.OK_BUTTON).click()
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")


class MainPage(BasePage):

    def dismiss_android_notifications(self):

        logging.info("dismiss Android notifications")
        try:
            notification_msg_on = self.driver.find_element(*LoginScreen.NOTIFICATION_ABOUT_SENDING_MESSAGES)
            if notification_msg_on.is_displayed():
                logging.info("click 'No' for sending notifications on Android")
                notification_msg_on = self.driver.find_element(
                    *LoginScreen.NOTIFICATION_ABOUT_SENDING_MESSAGES)
                self.assertIsNotNone(notification_msg_on)
                self.driver.find_element(*LoginScreen.NO_FOR_SENDING_NOTIFICATIONS_ON).click()
            else:
                pass
        except NoSuchElementException:
            pass

    def logout_if_already_logged_in(self):

        sleep(5)
        logging.info("logout if already logged in")
        try:
            logout_button = self.driver.find_element(*MainMenuScreen.LOGOUT_BUTTON)
            self.assertIsNotNone(logout_button, "logout button not found")
            logging.info("Your are already logged in - logging out")
            logout_button.click()
            self.driver.find_element(*LoginScreen.SUBMIT_BUTTON).click()
            sleep(5)
        except NoSuchElementException:
            logging.info("Your are already logged out")

    def alert_expiring_password(self):

        logging.info("check if Notice alert, about expiring password, is present")
        try:
            self.driver.find_element(*LoginScreen.ALERT_MSG_WILL_EXPIRE)
            self.assertIsNotNone(*LoginScreen.ALERT_MSG_WILL_EXPIRE)
            logging.info("Notice alert is present")
            self.driver.find_element(*LoginScreen.OK_BUTTON).click()
        except NoSuchElementException:
            logging.info("Notice alert is not present")
            pass

    def check_presence_of_events_button(self):

        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located(MainMenuScreen.EVENTS_BUTTON), "Failed to login")
            logging.info("Successful login")
        except NoSuchElementException:
            logging.info("Failed to login")
            self.fail("Failed to login")

    def open_EVENTS(self):

        logging.info("clicking in Events button")
        events_button = self.driver.find_element(*MainMenuScreen.EVENTS_BUTTON)
        self.assertIsNotNone(events_button)
        events_button.click()
        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*EventsScreen.EVENTS_HEADER)
        self.assertIsNotNone(events_header)

    def open_LOCATION(self):

        logging.info("clicking in Events button")
        location_button = self.driver.find_element(*MainMenuScreen.LOCATION_BUTTON)
        self.assertIsNotNone(location_button)
        location_button.click()


class LocationPage(BasePage):

    def check_if_location_page_was_opened(self):

        location_page_header = self.driver.find_element(*LocationScreen.LOCATION_PAGE_HEADER)
        self.assertIsNotNone(location_page_header, "Location Page header was not found")

    def click_send_once_now(self):

        logging.info("clicking in send_once_now button")
        send_once_now_button = self.driver.find_element(*LocationScreen.SEND_ONCE_NOW)
        self.assertIsNotNone(send_once_now_button)
        send_once_now_button.click()

    def click_send_every(self):

        logging.info("clicking in send_every button")
        send_every_button = self.driver.find_element(*LocationScreen.SEND_EVERY_SPINNER)
        self.assertIsNotNone(send_every_button)
        send_every_button.click()

    def choose_1_hour_option(self):

        logging.info("choose_1_hour_option")
        choose_1_hour_option = self.driver.find_element(*LocationScreen.CHOOSE_1_HOUR_OPTION)
        self.assertIsNotNone(choose_1_hour_option)
        choose_1_hour_option.click()

    def check_if_1hour_option_was_chosen(self):

        logging.info("check_if_1hour_option_was_chosen")
        check_if_1hour_option_was_chosen = self.driver.find_element(*LocationScreen.ASSERT_1_HOUR_OPTION)
        self.assertIsNotNone(check_if_1hour_option_was_chosen)

    def check_if_button_send_once_was_pressed(self):

        logging.info("check_if_1hour_option_was_chosen")
        check_if_1hour_option_was_chosen = self.driver.find_element(*LocationScreen.ASSERT_1_HOUR_OPTION)
        self.assertIsNotNone(check_if_1hour_option_was_chosen)

    def click_start_button(self):

        logging.info("click start button")
        start_button = self.driver.find_element(*LocationScreen.START_BUTTON)
        self.assertIsNotNone(start_button)
        start_button.click()

    def check_if_start_button_was_clicked(self):

        try:
            start_button_disabled = self.driver.find_element(*LocationScreen.START_BUTTON_disabled)
            if start_button_disabled.is_displayed():
                logging.info("button Start was clicked")
            else:
                self.fail("button Start was not clicked")
        except NoSuchElementException:
            self.fail("button Start was not clicked")


class EventsPage(BasePage):

    def check_if_EVENTS_were_opened(self):

        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*EventsScreen.EVENTS_HEADER)
        self.assertIsNotNone(events_header)

    def filter_events_by_Type(self):

        sleep(1)
        logging.info("filtering events by Type")
        self.driver.find_element(*EventsScreen.ANY_TYPE_EXPAND).click()
        self.driver.find_element(*EventsScreen.CHOOSE_TYPE_INCIDENT).click()
        sleep(1)
        self.driver.find_element(*EventsScreen.INCIDENT_TYPE_EXPAND).click()
        self.driver.find_element(*EventsScreen.CHOOSE_TYPE_ANY).click()
        sleep(1)

    def filter_events_by_Status(self):

        sleep(1)
        logging.info("filtering events by Status")
        self.driver.find_element(*EventsScreen.ANY_STATUS_EXPAND).click()
        self.driver.find_element(*EventsScreen.CHOOSE_ACTIVE_STATUS).click()
        sleep(1)
        self.driver.find_element(*EventsScreen.ACTIVE_STATUS_EXPAND).click()
        self.driver.find_element(*EventsScreen.CHOOSE_INACTIVE_STATUS).click()
        sleep(1)
        self.driver.find_element(*EventsScreen.INACTIVE_STATUS_EXPAND).click()
        self.driver.find_element(*EventsScreen.CHOOSE_DRAFT_STATUS).click()
        sleep(1)
        self.driver.find_element(*EventsScreen.DRAFT_STATUS_EXPAND).click()
        self.driver.find_element(*EventsScreen.CHOOSE_ANY_STATUS).click()
        sleep(1)

    def filter_events_by_Search_field(self):

        logging.info("search field - search event named: 'search'")
        self.driver.find_element(*EventsScreen.SEARCH_FIELD).click()
        self.driver.find_element(*EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*EventsScreen.SEARCH_FIELD).send_keys("search")

    def clear_Search_field(self):

        logging.info("clear search field")
        search_field = self.driver.find_element(*EventsScreen.SEARCH_FIELD)
        search_field.click()
        self.driver.keyevent(67)
        self.driver.keyevent(67)
        self.driver.keyevent(67)
        self.driver.keyevent(67)
        self.driver.keyevent(67)
        self.driver.keyevent(67)
        # search_field_string = self.driver.find_element(*EventsScreen.SEARCH_FIELD).get_attribute("content-desc")
        # len_of_the_string = len(search_field_string)
        # delete_character = self.driver.keyevent(67)  # it will delete only one character
        # clear_as_many_characters_needed = delete_character * len_of_the_string

    def click_More_button(self):

        sleep(1)
        logging.info("clicking in 'More' button")
        more_button = self.driver.find_element(*EventsScreen.MORE_BUTTON)
        self.assertIsNotNone(more_button, "More button was not found")
        more_button.click()

    def click_New_event_button(self):

        sleep(1)
        logging.info("clicking in New event button")
        new_event_button = self.driver.find_element(*EventsScreen.NEW_EVENT_BUTTON)
        self.assertIsNotNone(new_event_button, "New Event button not found")
        new_event_button.click()
        sleep(0.5)

    def click_New_sub_event(self):

        logging.info("clicking in 'New sub event' button")
        new_sub_event = self.driver.find_element(*EventDetailsScreen.NEW_SUB_EVENT)
        self.assertIsNotNone(new_sub_event, "New sub event button is not present")
        new_sub_event.click()
        sleep(3)

    def set_as_primary_event(self):

        logging.info("clicking in 'Set as primary' button")
        set_as_primary_button = self.driver.find_element(*EventDetailsScreen.SET_AS_PRIMARY_BUTTON)
        self.assertIsNotNone(set_as_primary_button)
        set_as_primary_button.click()
        sleep(2)

    def clear_primary_event(self):

        logging.info("clicking in 'Clear primary event' button")
        clear_primary_event_button = self.driver.find_element(*EventsScreen.CLEAR_PRIMARY_EVENT_BUTTON)
        self.assertIsNotNone(clear_primary_event_button)
        clear_primary_event_button.click()
        logging.info("checking notification - 'Primary event cleared'")
        notification = self.driver.find_element(*EventsScreen.NOTIFICATION_PRIMARY_EVENT_CLEARED)
        self.assertIsNotNone(notification)

    def open_previously_created_event1(self):

        logging.info("open created event")
        created_event1 = self.driver.find_element(*EventsScreen.CREATED_EVENT_1)
        self.assertIsNotNone(created_event1)
        created_event1.click()
        sleep(5)

    def open_previously_created_event2(self):

        logging.info("open previously created Event, Edit and Create mapping data")
        created_event2 = self.driver.find_element(*EventsScreen.CREATED_EVENT_2)
        self.assertIsNotNone(created_event2)
        created_event2.click()
        sleep(5)

    def open_previously_created_event3(self):

        logging.info("open previously created Event, Edit and Create mapping data")
        created_event3 = self.driver.find_element(*EventsScreen.CREATED_EVENT_3)
        self.assertIsNotNone(created_event3)
        created_event3.click()
        sleep(5)

    # only for events list, opened from chooser fields inside other event
    def click_on_previously_created_event_for_chooser_field(self):

        logging.info("click_on_previously_created_event_for_chooser_field")
        event_for_chooser_field = self.driver.find_element(*EventEditScreen.PREVIOUSLY_CREATED_EVENT_FOR_CHOOSER)
        self.assertIsNotNone(event_for_chooser_field)
        event_for_chooser_field.click()

    def click_on_previously_created_event_for_subform_chooser(self):

        logging.info("click_on_previously_created_event_for_subform_chooser")
        event_for_subform = self.driver.find_element(*EventEditScreen.PREVIOUSLY_CREATED_EVENT_FOR_SUBFORM_CHOOSER)
        self.assertIsNotNone(event_for_subform)
        event_for_subform.click()
        sleep(1)


class EventsTypesPage(BasePage):

    def choose_Incident_type_of_event(self):

        event_type_incident = self.driver.find_element(*TypesOfEventsScreen.INCIDENT_TYPE_OF_EVENT)
        self.assertIsNotNone(event_type_incident)
        logging.info("choosing Incident type of new event")
        event_type_incident.click()

    def choose_Event_for_on_load_save_type_of_event(self):

        event_type_onload = self.driver.find_element(*TypesOfEventsScreen.EVENT_FOR_ON_LOAD_SAVE)
        self.assertIsNotNone(event_type_onload)
        logging.info("choose type of event = event_for_on_load/save_test")
        event_type_onload.click()

    def choose_Event_for_chooser_fields_type_of_event(self):

        event_type_chooser = self.driver.find_element(*TypesOfEventsScreen.EVENT_FOR_CHOOSER_FIELDS)
        self.assertIsNotNone(event_type_chooser)
        logging.info("choose type of event = event for chooser fields")
        event_type_chooser.click()


class EventEditPage(BasePage):

    def click_into_Name_input_field(self):

        name_field = self.driver.find_element(*EventEditScreen.NAME_FIELD)
        self.assertIsNotNone(name_field)
        name_field.click()

    def fill_Name_input_field(self, text):

        logging.info("input Name for event")
        self.driver.find_element(*EventEditScreen.NAME_FIELD).send_keys(text)

    def click_severity_lvl_picker(self):

        try:
            logging.info("click on severity level field")
            self.driver.find_element(*EventEditScreen.SEVERITY_LEVEL_SELECTOR).click()
        except NoSuchElementException:
            pass

    def choose_severity_level_1(self):

        try:
            logging.info("choose_severity_lvl1")
            choose_severity_lvl1 = self.driver.find_element(*EventEditScreen.CHOOSE_SEVERITY_LVL1)
            if choose_severity_lvl1.is_displayed():
                choose_severity_lvl1.click()
            else:
                pass
        except NoSuchElementException:
            pass
        sleep(1)

    def choose_severity_level_2(self):

        try:
            logging.info("choose_severity_lvl2")
            choose_severity_lvl2 = self.driver.find_element(*EventEditScreen.CHOOSE_SEVERITY_LVL2)
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
            choose_severity_lvl3 = self.driver.find_element(*EventEditScreen.CHOOSE_SEVERITY_LVL3)
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
            choose_severity_lvl4 = self.driver.find_element(*EventEditScreen.CHOOSE_SEVERITY_LVL4)
            if choose_severity_lvl4.is_displayed():
                choose_severity_lvl4.click()
            else:
                pass
        except NoSuchElementException:
            pass
        sleep(1)

    def type_text_into_description_field(self):

        sleep(1)
        try:
            logging.info("type some text into description field")
            self.driver.find_element(*EventEditScreen.DESCRIPTION_FIELD).click()
            self.driver.find_element(*EventEditScreen.DESCRIPTION_FIELD).send_keys("test Android")
        except NoSuchElementException:
            self.fail("text field couldn't be selected")

    def click_create_mapping_data(self):

        logging.info("create mapping data")
        create_mapping_data_button = self.driver.find_element(*EventEditScreen.CREATE_MAPPING_DATA)
        self.assertIsNotNone(create_mapping_data_button, "Button for creating map data is not present")
        create_mapping_data_button.click()

    def save_event(self):

        logging.info("Save event")
        save_button = self.driver.find_element(*EventEditScreen.SAVE_BUTTON)
        self.assertIsNotNone(save_button)
        save_button.click()
        sleep(5)

    def cancel_button(self):

        logging.info("click on Cancel button")
        cancel_button = self.driver.find_element(*EventEditScreen.CANCEL_BUTTON)
        self.assertIsNotNone(cancel_button)
        cancel_button.click()

    # only for event type: "event_for_on_load/save_test"
    def check_on_load_and_on_save_sequences(self):

        logging.info("assert on load and on save sequence")
        sequence_onload_header = self.driver.find_element(*EventEditScreen.SEQUENCE_ONLOAD_HEADER)
        self.assertIsNotNone(sequence_onload_header)
        sequence_onload_value = self.driver.find_element(*EventEditScreen.SEQUENCE_ONLOAD_VALUE)
        self.assertIsNotNone(sequence_onload_value)
        sequence_onsave_header = self.driver.find_element(*EventEditScreen.SEQUENCE_ONSAVE_HEADER)
        sequence_onsave_value = self.driver.find_element(*EventEditScreen.SEQUENCE_ONSAVE_VALUE)
        self.assertIsNotNone(sequence_onsave_header)
        self.assertIsNotNone(sequence_onsave_value)

    def click_on_option_list(self):

        logging.info("click on option list")
        new_option_list = self.driver.find_element(*EventEditScreen.NEW_OPTION_LIST_HEADER)
        self.assertIsNotNone(new_option_list)
        new_option_list.click()

    def check_restored_field_1(self):

        logging.info("assert restored field 1")
        field_to_restore_1_header = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_1_HEADER)
        self.assertIsNotNone(field_to_restore_1_header)
        field_to_restore_1_value = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_1_VALUE)
        self.assertIsNotNone(field_to_restore_1_value)

    def check_restored_field_2(self):

        logging.info("assert restored field 2")
        field_to_restore_2_header = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_2_HEADER)
        self.assertIsNotNone(field_to_restore_2_header)
        field_to_restore_2_value = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_2_VALUE)
        self.assertIsNotNone(field_to_restore_2_value)

    def check_hidden_field_1(self):

        logging.info("assert hidden field")
        try:
            field_to_restore_1_header = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_1_HEADER)
            if field_to_restore_1_header.is_displayed():
                self.fail("field was not hidden correctly")
            else:
                pass
        except NoSuchElementException:
            logging.info("field is not visible = OK")
            pass

    def check_hidden_fields_1_and_2(self):

        logging.info("assert hidden fields")
        field_to_restore_1_header = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_1_HEADER)
        field_to_restore_2_header = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_2_HEADER)
        try:
            if field_to_restore_1_header.is_displayed():
                self.fail("field 1 was not hidden correctly")
            if field_to_restore_2_header.is_displayed():
                self.fail("field 2 was not hidden correctly")
            else:
                pass
        except NoSuchElementException:
            logging.info("fields are not visible = OK")
            pass

    # only for event type: "event_for_on_load/save_test"
    def click_button_add_row(self):

        logging.info("click button Add row")
        add_row = self.driver.find_element(*EventEditScreen.SUBFORM_FIELD_ADD_ROW)
        self.assertIsNotNone(add_row, "add_row button not found")
        add_row.click()

    def click_on_event_chooser_field(self):

        logging.info("click_on_event_chooser_field")
        chooser_field_for_event = self.driver.find_element(*EventEditScreen.CHOOSER_FIELD)
        self.assertIsNotNone(chooser_field_for_event, "chooser_field_for_event not found")
        chooser_field_for_event.click()
        sleep(1)

    def click_on_choose_field_inside_subform(self):

        logging.info("click_on_choose_field_inside_subform")
        event_chooser_in_subform = self.driver.find_element(*EventEditScreen.NEW_EVENTS_CHOOSER_IN_SUB_FORM)
        self.assertIsNotNone(event_chooser_in_subform, "event_chooser_in_subform not found")
        event_chooser_in_subform.click()
        sleep(1)

    def delete_chosen_event_inside_subform(self):

        sleep(1)
        logging.info("delete chosen event inside sub form")
        delete_button_inside_sub_form = self.driver.find_element(*EventEditScreen.DELETE_SUB_EVENT_FROM_CHOOSER)
        self.assertIsNotNone(delete_button_inside_sub_form, "delete_button_inside_sub_form not found")
        delete_button_inside_sub_form.click()
        previously_created_event_for_subform_chooser = self.driver.find_element(
            *EventEditScreen.PREVIOUSLY_CREATED_EVENT_FOR_SUBFORM_CHOOSER)
        self.assertIsNone(previously_created_event_for_subform_chooser)

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

    def scroll_down_to_description_field(self):

        logging.info("scroll down to description field")
        action = TouchAction(self.driver)

        elm1 = self.driver.find_element(*EventEditScreen.FINISHED_HEADER)
        action.press(elm1).perform()
        action.move_to(x=0, y=100).perform()
        sleep(2)
        elm2 = self.driver.find_element(*EventEditScreen.LEADAGENCY_HEADER)
        action.press(elm2).perform()
        action.move_to(x=0, y=100).perform()
        sleep(3)


class OptionList(BasePage):

    def click_on_option_1(self):

        logging.info("choose '1' in option list")
        option_1 = self.driver.find_element(*EventEditScreen.OPTION_LIST_VALUE_1)
        self.assertIsNotNone(option_1, "option list - option '1' not found")
        option_1.click()

    def click_on_option_2(self):

        logging.info("choose '2' in option list")
        option_2 = self.driver.find_element(*EventEditScreen.OPTION_LIST_VALUE_2)
        self.assertIsNotNone(option_2, "option list - option '2' not found")
        option_2.click()

    def click_on_option_3(self):

        logging.info("choose '3' in option list")
        option_3 = self.driver.find_element(*EventEditScreen.OPTION_LIST_VALUE_3)
        self.assertIsNotNone(option_3, "option list - option '3' not found")
        option_3.click()


class MapPage(BasePage):

    def wait_for_map_to_load(self):

        logging.info("Waiting for map to load")
        try:
            WebDriverWait(self.driver, 25).until(
                expected_conditions.presence_of_element_located(Map.MAP_AREA_3),
                "Failed to load map")
            logging.info("Map was successfully loaded")
        except NoSuchElementException:
            logging.info("Failed to load map")
            self.fail("Map was not found")

    def click_tool_button(self):

        logging.info("click tool button")
        tool_button = self.driver.find_element(*Map.TOOL_BUTTON)
        self.assertIsNotNone(tool_button, "Tool button is not present")
        tool_button.click()

    def click_point_button(self):

        logging.info("click point button")
        point_button = self.driver.find_element(*Map.POINT_BUTTON)
        self.assertIsNotNone(point_button, "point button not found")
        point_button.click()

    def click_line_button(self):

        logging.info("click line button")
        line_button = self.driver.find_element(*Map.LINE_BUTTON)
        self.assertIsNotNone(line_button, "line button not found")
        line_button.click()

    def click_circle_button(self):

        circle_button = self.driver.find_element(*Map.CIRCLE_BUTTON)
        self.assertIsNotNone(circle_button, "circle button not found")
        circle_button.click()

    def click_polygon_button(self):

        polygon_button = self.driver.find_element(*Map.CIRCLE_BUTTON)
        self.assertIsNotNone(polygon_button, "polygon button not found")
        polygon_button.click()

    def click_default_button(self):

        default_button = self.driver.find_element(*Map.DEFAULT_BUTTON)
        self.assertIsNotNone(default_button, "default button not found")
        default_button.click()

    def click_in_map_area_3(self):

        try:
            self.driver.find_element(*Map.MAP_AREA_3).click()
        except NoSuchElementException:
            positions = [(283, 457)]
            self.driver.tap(positions)

    def click_in_map_area_5(self):

        try:
            self.driver.find_element(*Map.MAP_AREA_5).click()
        except NoSuchElementException:
            positions = [(290, 440)]
            self.driver.tap(positions)

    def click_in_map_area_6(self):

        try:
            self.driver.find_element(*Map.MAP_AREA_6).click()
        except NoSuchElementException:
            positions = [(340, 470)]
            self.driver.tap(positions)

    def save_map(self):

        logging.info("Save map")
        save_map_button = self.driver.find_element(*Map.SAVE_MAP_BUTTON)
        self.assertIsNotNone(save_map_button, "save map button not found")
        save_map_button.click()
        sleep(3)


class EventDetailsPage(BasePage):

    def click_edit_button(self):

        logging.info("edit previously created event")
        edit_button = self.driver.find_element(*EventDetailsScreen.EDIT_BUTTON)
        self.assertIsNotNone(edit_button, "edit button not found")
        edit_button.click()
        sleep(2)

    def click_Delete_button(self):

        logging.info("clicking in 'Delete event' button")
        delete_event_button = self.driver.find_element(*EventDetailsScreen.DELETE_EVENT_BUTTON)
        self.assertIsNotNone(delete_event_button, "delete event button not found")
        delete_event_button.click()

    def alert_confirm_delete(self):

        logging.info("confirm delete")
        delete_confirm_button = self.driver.find_element(*EventDetailsScreen.DELETE_CONFIRM_BUTTON)
        self.assertIsNotNone(delete_confirm_button, "confirm delete button not found")
        delete_confirm_button.click()
        sleep(5)
