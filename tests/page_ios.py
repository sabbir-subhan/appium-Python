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

    # OCA top bar
    def hamburger_button(self):
        logging.info("click hamburger button to go back to main menu")
        sleep(2)
        try:
            hamburger_button = self.driver.find_element(*EventsScreen.HAMBURGER_FOR_MAIN_MENU_ios)
            self.assertIsNotNone(hamburger_button, "Hamburger button is not present")
            # probably that element cannot be clicked because attribute visible is "false"
            hamburger_button.click()
        except NoSuchElementException:
            positions_for_hamburger_button = [(729, 23)]
            self.driver.tap(positions_for_hamburger_button)
        sleep(2)


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

        try:
            WebDriverWait(self.driver, 40).until(
                expected_conditions.presence_of_element_located(WelcomeScreen.LOGIN_BUTTON_ios),
                "Login button not found")
            logging.info("Login button found")
        except NoSuchElementException:
            logging.info("Login button not found")
            self.fail("Login button not found")
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

        logging.info("dismiss iOS notifications")
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
        logging.info("logout if already logged in")
        try:
            logout_button_ios = self.driver.find_element(*MainMenuScreen.LOGOUT_BUTTON_ios)
            if logout_button_ios.is_displayed():
                logging.info("Your are already login - logging out")
                self.driver.find_element(*MainMenuScreen.LOGOUT_BUTTON_ios).click()
                self.driver.find_element(*LoginScreen.SUBMIT_BUTTON_ios).click()
                sleep(5)
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

    def check_if_EVENTS_were_opened(self):
        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*EventsScreen.EVENTS_HEADER_ios)
        self.assertIsNotNone(events_header)

    def filter_events_by_Type(self):

        logging.info("filtering events by Type")
        self.driver.find_element(*EventsScreen.ANY_TYPE_EXPAND_ios).click()
        self.driver.find_element(*EventsScreen.CHOOSE_TYPE_INCIDENT_ios).click()
        sleep(0.5)
        self.driver.find_element(*EventsScreen.INCIDENT_TYPE_EXPAND_ios).click()
        self.driver.find_element(*EventsScreen.CHOOSE_TYPE_ANY_ios).click()
        sleep(0.5)

    def filter_events_by_Status(self):

        logging.info("filtering events by Status")
        self.driver.find_element(*EventsScreen.ANY_STATUS_EXPAND_ios).click()
        self.driver.find_element(*EventsScreen.CHOOSE_ACTIVE_STATUS_ios).click()
        sleep(0.5)
        self.driver.find_element(*EventsScreen.ACTIVE_STATUS_EXPAND_ios).click()
        self.driver.find_element(*EventsScreen.CHOOSE_INACTIVE_STATUS_ios).click()
        sleep(0.5)
        self.driver.find_element(*EventsScreen.INACTIVE_STATUS_EXPAND_ios).click()
        self.driver.find_element(*EventsScreen.CHOOSE_DRAFT_STATUS_ios).click()
        sleep(0.5)
        self.driver.find_element(*EventsScreen.DRAFT_STATUS_EXPAND_ios).click()
        self.driver.find_element(*EventsScreen.CHOOSE_ANY_STATUS_ios).click()
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

    def click_New_sub_event(self):

        logging.info("clicking on 'New sub event' button")
        new_sub_event = self.driver.find_element(*EventDetailsScreen.NEW_SUB_EVENT_ios)
        self.assertIsNotNone(new_sub_event, "New sub event button is not present")
        new_sub_event.click()
        sleep(3)

    def set_as_primary_event(self):

        logging.info("clicking on 'Set as primary' button")
        set_as_primary_button = self.driver.find_element(*EventDetailsScreen.SET_AS_PRIMARY_BUTTON_ios)
        self.assertIsNotNone(set_as_primary_button)
        set_as_primary_button.click()
        sleep(2)

    def clear_primary_event(self):

        logging.info("clicking on 'Clear primary event' button")
        clear_primary_event_button = self.driver.find_element(*EventsScreen.CLEAR_PRIMARY_EVENT_BUTTON_ios)
        self.assertIsNotNone(clear_primary_event_button)
        clear_primary_event_button.click()
        logging.info("checking notification - 'Primary event cleared'")
        notification = self.driver.find_element(*EventsScreen.NOTIFICATION_PRIMARY_EVENT_CLEARED_ios)
        self.assertIsNotNone(notification)

    def open_previously_created_event1(self):

        logging.info("open created event")
        created_event1 = self.driver.find_element(*EventsScreen.CREATED_EVENT_1_ios)
        self.assertIsNotNone(created_event1)
        created_event1.click()
        sleep(5)

    def open_previously_created_event2(self):

        logging.info("open previously created Event, Edit and Create mapping data")
        created_event2 = self.driver.find_element(*EventsScreen.CREATED_EVENT_2_ios)
        self.assertIsNotNone(created_event2)
        created_event2.click()
        sleep(5)
        
    def open_previously_created_event3(self):

        logging.info("open previously created Event, Edit and Create mapping data")
        created_event3 = self.driver.find_element(*EventsScreen.CREATED_EVENT_3_ios)
        self.assertIsNotNone(created_event3)
        created_event3.click()
        sleep(5)

    # only for events list, opened from chooser fields inside other event
    def click_on_previously_created_event_for_chooser_field(self):

        logging.info("click_on_previously_created_event_for_chooser_field")
        event_for_chooser_field = self.driver.find_element(*EventEditScreen.PREVIOUSLY_CREATED_EVENT_FOR_CHOOSER_ios)
        self.assertIsNotNone(event_for_chooser_field)
        event_for_chooser_field.click()

    def click_on_previously_created_event_for_subform_chooser(self):

        logging.info("click_on_previously_created_event_for_subform_chooser")
        event_for_subform = self.driver.find_element(*EventEditScreen.PREVIOUSLY_CREATED_EVENT_FOR_SUBFORM_CHOOSER_ios)
        self.assertIsNotNone(event_for_subform)
        event_for_subform.click()
        sleep(1)


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

    def click_into_Name_input_field(self):

        try:
            WebDriverWait(self.driver, 25).until(
                expected_conditions.presence_of_element_located(EventEditScreen.NAME_FIELD_ios),
                "Failed to locate Name input field")
        except NoSuchElementException:
            logging.info("Failed to locate Name input field")
            self.fail("Failed to locate Name input field")
        logging.info("click into Name input field")
        self.driver.find_element(*EventEditScreen.NAME_FIELD_ios).click()

    def fill_Name_input_field(self, text):

        logging.info("input Name for event")
        self.driver.find_element(*EventEditScreen.NAME_FIELD_ios).send_keys(text)

    def click_severity_lvl_picker(self):

        try:
            logging.info("click on severity level field")
            self.driver.find_element(*EventEditScreen.SEVERITY_LEVEL_SELECTOR_ios).click()
        except NoSuchElementException:
            pass

    def choose_severity_level_1(self):

        try:
            logging.info("choose_severity_lvl1")
            choose_severity_lvl1 = self.driver.find_element(*EventEditScreen.CHOOSE_SEVERITY_LVL1_iPad)
            if choose_severity_lvl1.is_displayed():
                choose_severity_lvl1.click()
            else:
                # NEED A WAY TO SCROLL WHEEL PICKER ON iPhones, scroll, tap and move, click on element,
                #  send keys are not working - this step is not required in TC
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
        
    def cancel_button(self):
        
        logging.info("click on Cancel button")
        cancel_button = self.driver.find_element(*EventEditScreen.CANCEL_BUTTON_ios)
        self.assertIsNotNone(cancel_button)
        cancel_button.click()

    # only for event type: "event_for_on_load/save_test"
    def check_on_load_and_on_save_sequences(self):

        logging.info("assert on load and on save sequence")
        sequence_onload_header = self.driver.find_element(*EventEditScreen.SEQUENCE_ONLOAD_HEADER_ios)
        self.assertIsNotNone(sequence_onload_header)
        sequence_onload_value = self.driver.find_element(*EventEditScreen.SEQUENCE_ONLOAD_VALUE_ios)
        self.assertIsNotNone(sequence_onload_value)
        sequence_onsave_header = self.driver.find_element(*EventEditScreen.SEQUENCE_ONSAVE_HEADER_ios)
        sequence_onsave_value = self.driver.find_element(*EventEditScreen.SEQUENCE_ONSAVE_VALUE_ios)
        self.assertIsNotNone(sequence_onsave_header)
        self.assertIsNotNone(sequence_onsave_value)

    def click_on_option_list(self):

        logging.info("click on option list")
        new_option_list = self.driver.find_element(*EventEditScreen.NEW_OPTION_LIST_HEADER_ios)
        self.assertIsNotNone(new_option_list)
        new_option_list.click()
        
    def check_restored_field_1(self):

        logging.info("assert restored field 1")
        field_to_restore_1_header = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_1_HEADER_ios)
        self.assertIsNotNone(field_to_restore_1_header)
        field_to_restore_1_value = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_1_VALUE_ios)
        self.assertIsNotNone(field_to_restore_1_value)
    
    def check_restored_field_2(self):

        logging.info("assert restored field 2")
        field_to_restore_2_header = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_2_HEADER_ios)
        self.assertIsNotNone(field_to_restore_2_header)
        field_to_restore_2_value = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_2_VALUE_ios)
        self.assertIsNotNone(field_to_restore_2_value)

    def check_hidden_field_1(self):

        logging.info("assert hidden field")
        try:
            field_to_restore_1_header = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_1_HEADER_ios)
            if field_to_restore_1_header.is_displayed():
                self.fail("field was not hidden correctly")
        except NoSuchElementException:
            logging.info("field is not visible = OK")
            pass

    def check_hidden_fields_1_and_2(self):

        logging.info("assert hidden fields")
        field_to_restore_1_header = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_1_HEADER_ios)
        field_to_restore_2_header = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_2_HEADER_ios)
        try:
            if field_to_restore_1_header.is_displayed():
                self.fail("field 1 was not hidden correctly")
            if field_to_restore_2_header.is_displayed():
                self.fail("field 2 was not hidden correctly")
        except NoSuchElementException:
            logging.info("fields are not visible = OK")
            pass

    # only for event type: "event_for_on_load/save_test"
    def click_button_add_row(self):

        logging.info("click button Add row")
        add_row = self.driver.find_element(*EventEditScreen.SUBFORM_FIELD_ADD_ROW_ios)
        self.assertIsNotNone(add_row)
        add_row.click()

    def click_on_event_chooser_field(self):

        logging.info("click_on_event_chooser_field")
        chooser_field_for_event = self.driver.find_element(*EventEditScreen.CHOOSER_FIELD_ios)
        self.assertIsNotNone(chooser_field_for_event)
        chooser_field_for_event.click()
        sleep(1)

    def click_on_choose_field_inside_subform(self):

        logging.info("click_on_choose_field_inside_subform")
        event_chooser_in_subform = self.driver.find_element(*EventEditScreen.NEW_EVENTS_CHOOSER_IN_SUB_FORM_ios)
        self.assertIsNotNone(event_chooser_in_subform)
        event_chooser_in_subform.click()
        sleep(1)

    def delete_chosen_event_inside_subform(self):

        sleep(1)
        logging.info("delete chosen event inside sub form")
        positions_for_delete_button = [(16, 608)]
        self.driver.tap(positions_for_delete_button)
        previously_created_event_for_subform_chooser = self.driver.find_element(
            *EventEditScreen.PREVIOUSLY_CREATED_EVENT_FOR_SUBFORM_CHOOSER_ios)
        self.assertIsNone(previously_created_event_for_subform_chooser)


class OptionList(BasePage):

    def click_on_option_1(self):

        logging.info("choose '1' in option list")
        option_1 = self.driver.find_element(*EventEditScreen.OPTION_LIST_VALUE_1_ios)
        self.assertIsNotNone(option_1)
        option_1.click()
        
    def click_on_option_2(self):

        logging.info("choose '2' in option list")
        option_2 = self.driver.find_element(*EventEditScreen.OPTION_LIST_VALUE_2_ios)
        self.assertIsNotNone(option_2)
        option_2.click()
        
    def click_on_option_3(self):

        logging.info("choose '3' in option list")
        option_3 = self.driver.find_element(*EventEditScreen.OPTION_LIST_VALUE_3_ios)
        self.assertIsNotNone(option_3)
        option_3.click()


class MapPage(BasePage):

    def wait_for_map_to_load(self):
        logging.info("Waiting for map to load")
        try:
            WebDriverWait(self.driver, 25).until(
                expected_conditions.presence_of_element_located(Map.MAP_AREA_12_ios),
                "Failed to load map")
            logging.info("Map was successfully loaded")
        except NoSuchElementException:
            logging.info("Failed to load map")
            self.fail("Map was not found")

    def click_tool_button(self):

        logging.info("click tool button")
        tool_button = self.driver.find_element(*Map.TOOL_BUTTON_ios)
        self.assertIsNotNone(tool_button, "Tool button is not present")
        tool_button.click()

    def click_point_button(self):

        logging.info("click point button")
        point_button = self.driver.find_element(*Map.POINT_BUTTON_ios)
        self.assertIsNotNone(point_button)
        point_button.click()

    def click_line_button(self):

        logging.info("click line button")
        line_button = self.driver.find_element(*Map.LINE_BUTTON_ios)
        self.assertIsNotNone(line_button)
        line_button.click()

    def click_circle_button(self):

        circle_button = self.driver.find_element(*Map.CIRCLE_BUTTON_ios)
        self.assertIsNotNone(circle_button)
        circle_button.click()
        
    def click_polygon_button(self):

        polygon_button = self.driver.find_element(*Map.CIRCLE_BUTTON_ios)
        self.assertIsNotNone(polygon_button)
        polygon_button.click()

    def click_default_button(self):

        default_button = self.driver.find_element(*Map.DEFAULT_BUTTON_ios)
        self.assertIsNotNone(default_button)
        default_button.click()

    def click_in_map_area_12(self):

        try:
            self.driver.find_element(*Map.MAP_AREA_12_ios)
        except NoSuchElementException:
            positions_for_point = [(283, 457)]
            self.driver.tap(positions_for_point)

    def click_in_map_area_13(self):

        try:
            self.driver.find_element(*Map.MAP_AREA_13_ios)
        except NoSuchElementException:
            positions_for_line1 = [(290, 440)]
            self.driver.tap(positions_for_line1)

    def click_in_map_area_17(self):

        try:
            self.driver.find_element(*Map.MAP_AREA_17_ios)
        except NoSuchElementException:
            positions_for_line2 = [(340, 470)]
            self.driver.tap(positions_for_line2, 1)
            self.driver.tap(positions_for_line2, 1)

    def click_in_map_area_18(self):

        try:
            self.driver.find_element(*Map.MAP_AREA_18_ios)
        except NoSuchElementException:
            positions_for_circle = [(310, 360)]
            self.driver.tap(positions_for_circle)

    def save_map(self):

        logging.info("Save map")
        save_map_button = self.driver.find_element(*Map.SAVE_MAP_BUTTON_ios)
        self.assertIsNotNone(save_map_button)
        save_map_button.click()
        sleep(3)


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

    def alert_confirm_delete(self):

        logging.info("confirm delete")
        delete_confirm_button = self.driver.find_element(*EventDetailsScreen.DELETE_CONFIRM_BUTTON_ios)
        self.assertIsNotNone(delete_confirm_button)
        delete_confirm_button.click()
        sleep(5)
