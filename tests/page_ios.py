import unittest
from time import sleep
# import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction
# from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.mobilecommand import MobileCommand
from appium.webdriver import WebElement
from appium.webdriver.webdriver import MobileWebElement
from locators_ios import *
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

# add coordinates for iPhones - clicking is not working because button is invisible
        logging.info("click hamburger button to go back to main menu")
        # try:
        #     hamburger_button = self.driver.find_element(*TopBar.HAMBURGER_FOR_MAIN_MENU_ios)
        #     self.assertIsNotNone(hamburger_button, "Hamburger button is not present")
        #     if hamburger_button.is_displayed():
        #         hamburger_button.click()
        #     else:
        #         pass
        #     # probably that element cannot be clicked because attribute visible is "false"
        # except NoSuchElementException:
        #     positions_for_hamburger_button = [(730, 20)]
        #     sleep(1)
        #     self.driver.tap(positions_for_hamburger_button)
        # sleep(2)
        positions_for_hamburger_button = [(730, 20)]
        sleep(1)
        self.driver.tap(positions_for_hamburger_button)


class iOSdevice(BasePage):

    def hide_keyboard(self):

        logging.info("hide keyboard")
        try:
            done_button_ios = self.driver.find_element(*iOS.BUTTON_DONE_TO_HIDE_KEYBOARD_ios)
            if done_button_ios.is_displayed():
                done_button_ios.click()
            else:
                pass
        except NoSuchElementException:
            self.driver.hide_keyboard(key_name="Hide keyboard")

    def click_Return_button_on_keyboard(self):

        logging.info("click 'Return' on keyboard")
        self.driver.find_element(*iOS.RETURN_BUTTON_ios).click()
        sleep(1)


class WelcomePage(BasePage):

    def click_login_button(self):

        sleep(10)
        # try:
        #     positions_for_hamburger_button = [(730, 20)]
        #     sleep(1)
        #     self.driver.tap(positions_for_hamburger_button)
        # except:
        #     logging.info("pass tapping into positions")
        logging.info("click in LOGIN button")
        try:
            login_button = self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_ios)
            if login_button.is_displayed():
                self.assertIsNotNone(login_button)
                login_button.click()
        except NoSuchElementException:
            pass
        try:
            login_button_by_index = self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_by_index_ios)
            if login_button_by_index.is_displayed():
                self.assertIsNotNone(login_button_by_index)
                login_button_by_index.click()
        except NoSuchElementException:
            pass


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
                self.assertIsNotNone(logout_button_ios, "logout button not found")
                logging.info("Your are already logged in - logging out")
                logout_button_ios.click()
                self.driver.find_element(*LoginScreen.SUBMIT_BUTTON_ios).click()
                sleep(5)
            else:
                pass
        except NoSuchElementException:
            logging.info("Your are already logged out")

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
            logging.info("Events button in Main Menu is present")
        except NoSuchElementException:
            logging.info("Failed to login")
            self.fail("Failed to login")

    def open_EVENTS(self):

        logging.info("clicking in Events button")
        events_button = self.driver.find_element(*MainMenuScreen.EVENTS_BUTTON_ios)
        self.assertIsNotNone(events_button)
        events_button.click()
        
    def open_LOCATION(self):

        logging.info("clicking in Location button")
        location_button = self.driver.find_element(*MainMenuScreen.LOCATION_BUTTON_ios)
        self.assertIsNotNone(location_button, "Location button not found")
        location_button.click()
        
    def open_MAP(self):

        logging.info("clicking in Map button")
        map_button = self.driver.find_element(*MainMenuScreen.MAP_BUTTON_ios)
        self.assertIsNotNone(map_button)
        map_button.click()

    def open_PHOTO(self):

        logging.info("clicking in Photo button")
        photo_button = self.driver.find_element(*MainMenuScreen.PHOTO_BUTTON_ios)
        self.assertIsNotNone(photo_button)
        photo_button.click()


class PhotoPage(BasePage):
    
    def check_if_photo_page_was_opened(self):

        photo_page_header = self.driver.find_element(*PhotoScreen.PHOTO_PAGE_HEADER_ios)
        self.assertIsNotNone(photo_page_header, "Photo page header was not found")
        logging.info("Photo page was opened")
        
    def click_gallery_button(self):

#add coordinates for iPhones - clicking is not working because button is invisible
        logging.info("clicking in Gallery button")
        gallery_button = self.driver.find_element(*PhotoScreen.GALLERY_BUTTON_ios)
        self.assertIsNotNone(gallery_button)
        try:
            action = TouchAction(self.driver)
            action.tap(element=None, x=180, y=158, count=1).perform()
            sleep(2)
        except:
            gallery_button.click()

    def click_take_new_button(self):

        logging.info("clicking in Take new button")
        take_new_button = self.driver.find_element(*PhotoScreen.TAKE_NEW_BUTTON_ios)
        self.assertIsNotNone(take_new_button)
        try:
            action = TouchAction(self.driver)
            action.tap(element=None, x=548, y=158, count=1).perform()
            sleep(2)
        except:
            take_new_button.click()

    def type_description_of_the_photo(self, text):

        sleep(2)
        logging.info("type text into description field")
        description_field = self.driver.find_element(*PhotoScreen.DESCRIPTION_FIELD_ios)
        self.assertIsNotNone(description_field)
        description_field.click()
        description_field.send_keys(text)

    def click_send_button(self):

        logging.info("click send button")
        send_button = self.driver.find_element(*PhotoScreen.SEND_BUTTON_ios)
        self.assertIsNotNone(send_button)
        send_button.click()
        WebDriverWait(self.driver, 180).until(
            expected_conditions.presence_of_element_located(MainMenuScreen.LOCATION_BUTTON_ios),
            "Failed to send photo")
        logging.info("Photo was sent")

    def click_reset_button(self):

        logging.info("click send button")
        reset_button = self.driver.find_element(*PhotoScreen.RESET_BUTTON_ios)
        self.assertIsNotNone(reset_button)
        reset_button.click()


class GalleryPage(BasePage):

    def choose_photo_1(self):

        logging.info("choosing photo 1")
        choose_photo = self.driver.find_element(*GalleryScreen.GALLERY_PHOTO_1_ios)
        self.assertIsNotNone(choose_photo)
        choose_photo.click()


class CameraPage(BasePage):

    def take_a_photo(self):

        logging.info("taking photo")
        photo_capture = self.driver.find_element(*CameraScreen.PHOTO_CAPTURE_ios)
        self.assertIsNotNone(photo_capture)
        photo_capture.click()

    def click_cancel(self):

        logging.info("click Cancel")
        cancel = self.driver.find_element(*CameraScreen.CANCEL_BUTTON_ios)
        self.assertIsNotNone(cancel)
        cancel.click()

    def click_use_photo(self):

        logging.info("click Use Photo")
        use_photo = self.driver.find_element(*CameraScreen.USE_PHOTO_ios)
        self.assertIsNotNone(use_photo)
        use_photo.click()

    def retake_photo(self):

        logging.info("click Retake")
        retake_photo = self.driver.find_element(*CameraScreen.RETAKE_ios)
        self.assertIsNotNone(retake_photo)
        retake_photo.click()

    def choose_camera(self):

        logging.info("click choose camera")
        chooser_camera = self.driver.find_element(*CameraScreen.CAMERA_CHOOSER_ios)
        self.assertIsNotNone(chooser_camera)
        chooser_camera.click()


class LocationPage(BasePage):

    def check_if_location_page_was_opened(self):

        logging.info("Location Page was opened")
        location_page_header = self.driver.find_element(*LocationScreen.LOCATION_PAGE_HEADER_ios)
        self.assertIsNotNone(location_page_header, "Location Page header was not found")
    
    def click_send_once_now(self):
        
        logging.info("clicking in 'Send once now' button")
        send_once_now_button = self.driver.find_element(*LocationScreen.SEND_ONCE_NOW_ios)
        self.assertIsNotNone(send_once_now_button)
        send_once_now_button.click()

    def check_if_location_was_sent(self):

        sleep(2)
        logging.info("check if location was sent")
        # location_status = self.driver.find_element(*LocationScreen.LOCATION_STATUS_ios)
        # self.assertIsNotNone(location_status)
        try:
            WebDriverWait(self.driver, 30).until(
                expected_conditions.presence_of_element_located(LocationScreen.LOCATION_STATUS_ios),
                "Failed to send location")
            logging.info("Location was sent")
        except NoSuchElementException:
            logging.info("Failed to send location")
            self.fail("Failed to send location")

    def click_send_every(self):

        logging.info("clicking in 'Send every' selector")
        send_every_button = self.driver.find_element(*LocationScreen.SEND_EVERY_SPINNER_ios)
        self.assertIsNotNone(send_every_button)
        send_every_button.click()

    def choose_send_every_5_minutes_option(self):

        logging.info("choose send every '5 minutes' option")
        choose_5_minutes_option = self.driver.find_element(*LocationScreen.CHOOSE_5_MINUTES_OPTION_iPad)
        self.assertIsNotNone(choose_5_minutes_option)
        choose_5_minutes_option.click()

    def check_if_5_minutes_option_was_chosen(self):

        logging.info("check if send every '5 minutes'  option was chosen")
        check_if_5_minutes_option_was_chosen = self.driver.find_element(*LocationScreen.ASSERT_5_MINUTES_OPTION_ios)
        self.assertIsNotNone(check_if_5_minutes_option_was_chosen)

    def click_for_the_next(self):

        logging.info("clicking in 'For the next' selector")
        for_the_next = self.driver.find_element(*LocationScreen.FOR_THE_NEXT_SPINNER_ios)
        self.assertIsNotNone(for_the_next)
        for_the_next.click()

    def choose_1_hour_option(self):

        logging.info("choose '1 hour' option")
        choose_1_hour_option = self.driver.find_element(*LocationScreen.CHOOSE_1_HOUR_OPTION_iPad)
        self.assertIsNotNone(choose_1_hour_option)
        choose_1_hour_option.click()

    def check_if_1_hour_option_was_chosen(self):

        logging.info("check if '1 hour' option was chosen")
        check_if_1hour_option_was_chosen = self.driver.find_element(*LocationScreen.ASSERT_1_HOUR_OPTION_ios)
        self.assertIsNotNone(check_if_1hour_option_was_chosen)

    def click_start_button(self):

        logging.info("click 'Start' button")
        start_button = self.driver.find_element(*LocationScreen.START_BUTTON_ios)
        self.assertIsNotNone(start_button)
        start_button.click()

    def check_if_start_button_was_clicked(self):

        logging.info("check if 'Start' button was clicked")
        try:
            start_button = self.driver.find_element(*LocationScreen.START_BUTTON_ios)
            if start_button.is_displayed():
                self.fail("button Start was not clicked")
            else:
                pass
        except NoSuchElementException:
            logging.info("button Start was clicked")


class EventsPage(BasePage):

    def check_if_EVENTS_were_opened(self):

        sleep(2)
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

        logging.info("clicking in More button")
        more_button = self.driver.find_element(*EventsScreen.MORE_BUTTON_ios)
        self.assertIsNotNone(more_button, "More button not found")
        more_button.click()

    def click_New_event_button(self):

        logging.info("clicking in New event button")
        new_event_button = self.driver.find_element(*EventsScreen.NEW_EVENT_BUTTON_ios)
        self.assertIsNotNone(new_event_button, "New Event button not found")
        new_event_button.click()
        sleep(0.5)

    def click_New_sub_event(self):

        logging.info("clicking in 'New sub event' button")
        new_sub_event = self.driver.find_element(*EventDetailsScreen.NEW_SUB_EVENT_ios)
        self.assertIsNotNone(new_sub_event, "New sub event button is not present")
        new_sub_event.click()
        sleep(3)

    def set_as_primary_event(self):

        logging.info("clicking in 'Set as primary' button")
        set_as_primary_button = self.driver.find_element(*EventDetailsScreen.SET_AS_PRIMARY_BUTTON_ios)
        self.assertIsNotNone(set_as_primary_button)
        set_as_primary_button.click()
        sleep(2)

    def clear_primary_event(self):

        logging.info("clicking in 'Clear primary event' button")
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

        logging.info("click into Name input field")
        try:
            name_field = self.driver.find_element(*EventEditScreen.NAME_FIELD_ios)
            name_field.click()
        except NoSuchElementException:
            self.driver.find_element(*EventEditScreen.NAME_FIELD_by_index_ios).click()

    def fill_Name_input_field(self, text):

        logging.info("input Name for event")
        try:
            self.driver.find_element(*EventEditScreen.NAME_FIELD_ios).send_keys(text)
        except NoSuchElementException:
            self.driver.find_element(*EventEditScreen.NAME_FIELD_by_index_ios).send_keys(text)

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
        self.assertIsNotNone(save_button, "Save button not found")
        save_button.click()
        sleep(10)
        
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
            else:
                pass
        except NoSuchElementException:
            logging.info("field is not visible = OK")
            pass

    def check_hidden_fields_1_and_2(self):

        logging.info("assert hidden fields")
        try:
            field_to_restore_1_header = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_1_HEADER_ios)
            field_to_restore_2_header = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_2_HEADER_ios)
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
        add_row = self.driver.find_element(*EventEditScreen.SUBFORM_FIELD_ADD_ROW_ios)
        self.assertIsNotNone(add_row, "add_row button not found")
        add_row.click()

    def click_on_event_chooser_field(self):

        logging.info("click_on_event_chooser_field")
        chooser_field_for_event = self.driver.find_element(*EventEditScreen.CHOOSER_FIELD_ios)
        self.assertIsNotNone(chooser_field_for_event, "chooser_field_for_event not found")
        chooser_field_for_event.click()
        sleep(1)

    def click_on_choose_field_inside_subform(self):

        logging.info("click_on_choose_field_inside_subform")
        event_chooser_in_subform = self.driver.find_element(*EventEditScreen.NEW_EVENTS_CHOOSER_IN_SUB_FORM_ios)
        self.assertIsNotNone(event_chooser_in_subform, "event_chooser_in_subform not found")
        event_chooser_in_subform.click()
        sleep(1)

    def delete_chosen_event_inside_subform(self):

        logging.info("delete chosen event inside sub form")
        sleep(1)
        try:
            delete_x = self.driver.find_element(*EventEditScreen.DELETE_SUB_EVENT_FROM_CHOOSER_ios)
            if delete_x.is_displayed():
                self.assertIsNotNone(delete_x)
                delete_x.click()
            else:
                pass
        except NoSuchElementException:
            positions_for_delete_button = [(16, 608)]
            self.driver.tap(positions_for_delete_button)
            try:
                previously_created_event_for_subform_chooser = self.driver.find_element(
                    *EventEditScreen.PREVIOUSLY_CREATED_EVENT_FOR_SUBFORM_CHOOSER_ios)
                self.assertIsNone(previously_created_event_for_subform_chooser)
            except NoSuchElementException:
                pass


class OptionList(BasePage):

    def click_on_option_1(self):

        logging.info("choose '1' in option list")
        option_1 = self.driver.find_element(*EventEditScreen.OPTION_LIST_VALUE_1_ios)
        self.assertIsNotNone(option_1, "option list - option '1' not found")
        option_1.click()
        
    def click_on_option_2(self):

        logging.info("choose '2' in option list")
        option_2 = self.driver.find_element(*EventEditScreen.OPTION_LIST_VALUE_2_ios)
        self.assertIsNotNone(option_2, "option list - option '2' not found")
        option_2.click()
        
    def click_on_option_3(self):

        logging.info("choose '3' in option list")
        option_3 = self.driver.find_element(*EventEditScreen.OPTION_LIST_VALUE_3_ios)
        self.assertIsNotNone(option_3, "option list - option '3' not found")
        option_3.click()


class MapPage(BasePage):

    def click_plot_button(self):

        logging.info("click Plot button")
        plot_button = self.driver.find_element(*Map.PLOT_BUTTON_ios)
        self.assertIsNotNone(plot_button)
        plot_button.click()

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
        self.assertIsNotNone(point_button, "point button not found")
        point_button.click()

    def click_line_button(self):

        logging.info("click line button")
        line_button = self.driver.find_element(*Map.LINE_BUTTON_ios)
        self.assertIsNotNone(line_button, "line button not found")
        line_button.click()

    def click_circle_button(self):

        circle_button = self.driver.find_element(*Map.CIRCLE_BUTTON_ios)
        self.assertIsNotNone(circle_button, "circle button not found")
        circle_button.click()
        
    def click_polygon_button(self):

        polygon_button = self.driver.find_element(*Map.POLYGON_BUTTON_ios)
        self.assertIsNotNone(polygon_button, "polygon button not found")
        polygon_button.click()

    def click_default_button(self):

        default_button = self.driver.find_element(*Map.DEFAULT_BUTTON_ios)
        self.assertIsNotNone(default_button, "default button not found")
        default_button.click()
        sleep(1)

    def click_in_map_area_12(self):

        logging.info("click on map")
        position = [(350, 550)]
        self.driver.tap(position)
        # self.driver.find_element(*Map.MAP_AREA_12_ios).click()
        sleep(1)

    def click_in_map_area_13(self):

        logging.info("click on map")
        position = [(300, 500)]
        self.driver.tap(position)
        # self.driver.find_element(*Map.MAP_AREA_13_ios).click()
        sleep(1)

    def click_in_map_area_17(self):

        logging.info("click on map")
        position = [(0, 0)]
        self.driver.tap(position)
        # self.driver.find_element(*Map.MAP_AREA_17_ios).click()
        sleep(1)

    def double_click_in_map_area_18(self):

        logging.info("double click on map")
        action = TouchAction(self.driver)
        action.tap(element=None, x=450, y=350, count=2).perform()
        # self.driver.find_element(*Map.MAP_AREA_18_ios).click()
        sleep(1)

    def save_map(self):

        logging.info("Save map")
        save_map_button = self.driver.find_element(*Map.SAVE_MAP_BUTTON_ios)
        self.assertIsNotNone(save_map_button, "save map button not found")
        save_map_button.click()
        sleep(3)


class EventDetailsPage(BasePage):

    def click_edit_button(self):

        logging.info("edit previously created event")
        edit_button = self.driver.find_element(*EventDetailsScreen.EDIT_BUTTON_ios)
        self.assertIsNotNone(edit_button, "edit button not found")
        edit_button.click()
        sleep(2)

    def click_Delete_button(self):

        logging.info("clicking in 'Delete event' button")
        delete_event_button = self.driver.find_element(*EventDetailsScreen.DELETE_EVENT_BUTTON_ios)
        self.assertIsNotNone(delete_event_button, "delete event button not found")
        delete_event_button.click()

    def alert_confirm_delete(self):

        logging.info("confirm delete")
        delete_confirm_button = self.driver.find_element(*EventDetailsScreen.DELETE_CONFIRM_BUTTON_ios)
        self.assertIsNotNone(delete_confirm_button, "confirm delete button not found")
        delete_confirm_button.click()
        sleep(5)
