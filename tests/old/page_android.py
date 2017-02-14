# from appium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
import os
from appium import webdriver
from selenium.common.exceptions import *
import unittest
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction
from locators_android import *
from credentials import Credentials
from credentials import ContactIdentifierPIN
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

    def take_screenshot(self, file_name):

        logging.info("taking screenshot")
        sleep(2)
        self.driver.save_screenshot(file_name)

    def reset(self):
        """This method will reset driver - so for example app will be force to logout"""
        logging.info("reset")
        self.driver.reset()


class AndroidDevice(BasePage):
    """A class for methods to handle Android Device"""

    def hide_keyboard(self):

        try:
            logging.info("hide screen keyboard")
            self.driver.hide_keyboard()
            sleep(3)
        except:
            logging.info("screen keyboard not found")

    def click_Go_button_on_keyboard(self):

        try:
            logging.info("click Go on keyboard")
            self.driver.keyevent(66)
            sleep(3)
        except NoSuchElementException:
            logging.info("keyboard not found")

    def click_back_button(self):

        logging.info("click 'Back' button")
        self.driver.press_keycode(4)
        sleep(5)

    def alert_android_allow(self):

        try:
            button_allow_location = self.driver.find_element(*Android.ANDROID_ALLOW)
            if button_allow_location.is_displayed():
                logging.info("Accept for example using location - device will store that info for later use")
                button_allow_location.click()
        except NoSuchElementException:
            pass
        try:
            button_allow_location = self.driver.find_element(*Android.ANDROID_ALLOW)
            if button_allow_location.is_displayed():
                button_allow_location.click()
        except NoSuchElementException:
            pass

    def click_set_button(self):

        logging.info("Click 'Set' button")
        set_button = self.driver.find_element(*Android.ANDROID_SET_BUTTON)
        self.assertIsNotNone(set_button, "Set button was not found")
        set_button.click()

    def click_cancel_button(self):

        logging.info("Click 'Cancel' button")
        cancel_button = self.driver.find_element(*Android.ANDROID_CANCEL_BUTTON)
        self.assertIsNotNone(cancel_button, "Cancel button was not found")
        cancel_button.click()

    def click_clear_button(self):

        logging.info("Click 'Clear' button")
        clear_button = self.driver.find_element(*Android.ANDROID_CLEAR_BUTTON)
        self.assertIsNotNone(clear_button, "Clear button was not found")
        clear_button.click()


class Common(BasePage):
    """A class for methods to handle Common buttons from different screens"""

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

    def click_save_button(self):

        logging.info("click Save button")
        save_button = self.driver.find_element(*CommonScreen.SAVE_BUTTON)
        self.assertIsNotNone(save_button, "Save button not found")
        save_button.click()
        sleep(10)

    def click_cancel_button(self):
        logging.info("click on Cancel button")
        cancel_button = self.driver.find_element(*CommonScreen.CANCEL_BUTTON)
        self.assertIsNotNone(cancel_button, "Cancel button not found")
        cancel_button.click()

    def click_ok_button(self):
        logging.info("click on 'Ok' button")
        ok_button = self.driver.find_element(*CommonScreen.OK_BUTTON)
        self.assertIsNotNone(ok_button, "Ok button not found")
        ok_button.click()

    def fill_Name_input_field(self, text):

        logging.info("fill Name input field")
        name_field = self.driver.find_element(*EventEditScreen.NAME_FIELD)
        name_field.click()
        name_field.send_keys(text)

    def scroll_down(self):
        """Method to scroll down to bottom of the screen - to 'Save' button"""

        window_size = self.driver.get_window_size()  # this returns dictionary
        start_x = window_size["width"]*0.25
        # end_x = window_size["width"]*0.75
        start_y = window_size["height"]*0.20
        end_y = window_size["height"]*0.80
        logging.info("scroll down")
        sleep(2)
        scrolls = 13
        while scrolls > 0:
            self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
            scrolls -= 1
        sleep(2)

    def scroll_up(self):
        """Method to scroll up to top of the screen"""

        window_size = self.driver.get_window_size()  # this will give You a dictionary
        start_x = window_size["width"]*0.25
        # end_x = window_size["width"]*0.75
        start_y = window_size["height"]*0.25
        end_y = window_size["height"]*0.80
        logging.info("scroll up")
        sleep(2)
        scrolls = 13
        while scrolls > 0:
            self.driver.swipe(start_x, start_y, start_x, end_y, 3000)  # each swipe is scrolling one screen
            scrolls -= 1
        sleep(1)

    def scroll_down_one_view(self):
        """Method to scroll down only one screen"""

        window_size = self.driver.get_window_size()  # this will give You a dictionary
        start_x = window_size["width"] * 0.25
        start_y = window_size["height"] * 0.15
        end_y = window_size["height"] * 0.8
        logging.info("scroll down only one screen")
        sleep(2)
        self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
        sleep(1)

    def scroll_up_one_view(self):
        """Method to scroll down only one screen"""

        window_size = self.driver.get_window_size()  # this will give You a dictionary
        start_x = window_size["width"] * 0.25
        start_y = window_size["height"] * 0.15
        end_y = window_size["height"] * 0.8
        logging.info("scroll down only one screen")
        sleep(2)
        self.driver.swipe(start_x, start_y, start_x, end_y, 3000)  # each swipe is scrolling one screen
        sleep(1)

    # def scroll_down_test(self):
    #     """Method to scroll down to bottom of the screen - to 'Save' button"""
    #
    #     logging.info("scroll down with loop")
    #     var = 1
    #     while var == 1:
    #         try:
    #             logging.info("try")
    #             save_button = self.driver.find_element(*CommonScreen.SAVE_BUTTON)
    #             if save_button.is_displayed():  # this returns always true - bug in Appium
    #                 break
    #         except NoSuchElementException:
    #             logging.info("except")
    #             window_size = self.driver.get_window_size()  # this will give You a dictionary
    #             start_x = window_size["width"]*0.25
    #             # end_x = window_size["width"]*0.75
    #             start_y = window_size["height"]*0.25
    #             end_y = window_size["height"]*0.75
    #             logging.info("scroll down")
    #             sleep(2)
    #             self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
    #             sleep(1)

    def spinner_button_on_the_right(self):

        logging.info("click spinner button on the right")
        spinner_button_on_the_right = self.driver.find_element(*CommonScreen.SPINNER_ON_THE_RIGHT)
        self.assertIsNotNone(spinner_button_on_the_right, "Spinner button on the right not found")
        spinner_button_on_the_right.click()

    def spinner_button_on_the_left(self):

        logging.info("click spinner button on the left")
        spinner_button_on_the_left = self.driver.find_element(*CommonScreen.SPINNER_ON_THE_RIGHT)
        self.assertIsNotNone(spinner_button_on_the_left, "Spinner button on the left not found")
        spinner_button_on_the_left.click()


class WelcomePage(Common):
    """A class for methods to handle WelcomePage Page"""

    def click_login_button(self):

        logging.info("click in LOGIN button")
        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located(WelcomeScreen.LOGIN_BUTTON),
                "Login button not found")
            self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON).click()
        except NoSuchElementException:
            self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_by_index).click()

    def click_settings_button(self):

        logging.info("click Settings button")
        settings_button = self.driver.find_element(*WelcomeScreen.SETTINGS_BUTTON)
        self.assertIsNotNone(settings_button)
        settings_button.click()

    def type_contact_identifier(self, test_pin):

        logging.info("type contact identifier")
        contact_identifier_field = self.driver.find_element(*WelcomeScreen.SETTINGS_CONTACT_IDENTIFIER_FIELD)
        self.assertIsNotNone(contact_identifier_field)
        action = TouchAction(self.driver)
        action.long_press(el=contact_identifier_field, duration=1000).perform()
        self.driver.keyevent(67)
        contact_identifier_field.send_keys(ContactIdentifierPIN.get_contact_identifier_pin(test_pin))

    def check_if_app_was_activated(self):

        logging.info("check if app was activated")
        alert = self.driver.find_element(*WelcomeScreen.SETTINGS_ALERT_APP_HAS_BEEN_ACTIVATED)
        self.assertIsNotNone(alert, "App was not activated")


class LoginPage(BasePage):
    """A class for methods to handle Login Page"""

    def type_username(self, username):

        username_field = self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME)
        action = TouchAction(self.driver)
        action.long_press(el=username_field, duration=1000).perform()
        self.driver.keyevent(67)
        logging.info("type username")
        username_field.send_keys(Credentials.get_username(username))

    def type_password(self, password):

        password_field = self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD)
        action = TouchAction(self.driver)
        action.long_press(el=password_field, duration=1000).perform()
        self.driver.keyevent(67)
        logging.info("type password")
        password_field.send_keys(Credentials.get_password(password))

    def type_domain_address(self, domain):

        domain_field = self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN)
        action = TouchAction(self.driver)
        action.long_press(el=domain_field, duration=1000).perform()
        self.driver.keyevent(67)
        logging.info("type domain address")
        domain_field.send_keys(Credentials.get_domain(domain))

    def click_submit_button(self):

        # switching context

        # print(self.driver.contexts)
        # print(self.driver.current_context)
        # context_name = "WEBVIEW_com.noggin.oca"
        # self.driver.switch_to.context(context_name)
        # print(self.driver.contexts)
        # print(self.driver.current_context)

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


class MainPage(Common):
    """A class for methods to handle Main Page"""

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

    # def logout_if_already_logged_in(self):
    #     # logout button does not have attribute content-desc
    #     sleep(5)
    #     logging.info("logout if already logged in")
    #     try:
    #         logout_button = self.driver.find_element(*MainMenuScreen.LOGOUT_BUTTON)
    #         if logout_button.is_displayed():
    #             logging.info("Your are already logged in - logging out")
    #             # scroll to logout button
    #             buttons = self.driver.find_elements(*MainMenuScreen.BUTTONS)
    #             self.driver.scroll(buttons[22], buttons[1])
    #             sleep(0.5)
    #             self.assertIsNotNone(logout_button, "logout button not found")
    #             logout_button.click()
    #             self.driver.find_element(*LoginScreen.SUBMIT_BUTTON).click()
    #             sleep(5)
    #         else:
    #             logging.info("logout button is not present")
    #     except NoSuchElementException:
    #         logging.info("Your are already logged out")

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
                expected_conditions.presence_of_element_located(MainMenuScreen.EVENTS_BUTTON),
                "Events button in Main Menu is not present")
            logging.info("Events button in Main Menu is present")
        except NoSuchElementException:
            logging.info("Events button in Main Menu is not present")
            self.fail("Events button in Main Menu is not present")

    def click_ACTIVATE_BUTTON_on_alert(self):

        logging.info("clicking in ACTIVATE button on alert")
        alert_activate_button = self.driver.find_element(*MainMenuScreen.ALERT_ACTIVATE_BUTTON)
        self.assertIsNotNone(alert_activate_button, "ACTIVATE button on alert not found")
        alert_activate_button.click()
        sleep(2)

    def check_if_alert_WORKFLOW_ACTIVATED_is_present(self):

        logging.info("check if alert 'Workflow activated' is present and click 'Ok'")
        alert_workflow_activated = self.driver.find_element(*MainMenuScreen.ALERT_WORKFLOW_ACTIVATED)
        self.assertIsNotNone(alert_workflow_activated, "alert WORKFLOW ACTIVATED is not present")
        self.driver.find_element(*LoginScreen.OK_BUTTON).click()

    def click_ACTIVATE_WORKFLOW(self):

        logging.info("clicking in ACTIVATE WORKFLOW button")
        activate_workflow_button = self.driver.find_element(*MainMenuScreen.ACTIVATE_WORKFLOW_BUTTON)
        self.assertIsNotNone(activate_workflow_button, "ACTIVATE WORKFLOW button not found")
        activate_workflow_button.click()

    def open_CREATE_CONTACT(self):

        logging.info("clicking in CREATE CONTACT button")
        create_contact_button = self.driver.find_element(*MainMenuScreen.CREATE_CONTACT_BUTTON)
        self.assertIsNotNone(create_contact_button, "CREATE CONTACT button not found")
        create_contact_button.click()

    def open_CREATE_TASK(self):

        logging.info("clicking in CREATE TASK button")
        create_task_button = self.driver.find_element(*MainMenuScreen.CREATE_TASK_BUTTON)
        self.assertIsNotNone(create_task_button, "CREATE TASK button not found")
        create_task_button.click()

    def open_CREATE_REPORT(self):

        logging.info("clicking in CREATE REPORT button")
        create_report_button = self.driver.find_element(*MainMenuScreen.CREATE_REPORT_BUTTON)
        self.assertIsNotNone(create_report_button, "CREATE REPORT button not found")
        create_report_button.click()
        sleep(2)

    def open_WEBSITE_LINK(self):

        sleep(2)
        logging.info("clicking in WEBSITE LINK button")
        website_link_button = self.driver.find_element(*MainMenuScreen.WEBSITE_LINK_BUTTON)
        self.assertIsNotNone(website_link_button, "WEBSITE LINK button not found")
        website_link_button.click()
        logging.info("wait for page to load")
        sleep(10)

    def open_INCIDENT(self):

        logging.info("clicking in INCIDENT button")
        incident_button = self.driver.find_element(*MainMenuScreen.INCIDENT_BUTTON)
        self.assertIsNotNone(incident_button, "INCIDENT button not found")
        incident_button.click()

    def open_CREATE_ASSETS(self):

        logging.info("clicking in CREATE ASSETS button")
        create_assets_button = self.driver.find_element(*MainMenuScreen.CREATE_ASSETS_BUTTON)
        self.assertIsNotNone(create_assets_button, "CREATE ASSETS button not found")
        create_assets_button.click()

    def open_CREATE_LOG(self):

        logging.info("clicking in CREATE LOG button")
        create_log_button = self.driver.find_element(*MainMenuScreen.CREATE_LOG_BUTTON)
        self.assertIsNotNone(create_log_button, "CREATE LOG button not found")
        create_log_button.click()

    def open_RISKS(self):

        logging.info("clicking in RISKS button")
        risks_button = self.driver.find_element(*MainMenuScreen.RISKS_BUTTON)
        self.assertIsNotNone(risks_button, "RISKS button not found")
        risks_button.click()

    def open_EVENTS(self):

        logging.info("clicking in Events button")
        events_button = self.driver.find_element(*MainMenuScreen.EVENTS_BUTTON)
        self.assertIsNotNone(events_button, "EVENTS button not found")
        events_button.click()
        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*EventsScreen.EVENTS_HEADER)
        self.assertIsNotNone(events_header)

    def open_LOGS(self):

        logging.info("clicking in LOGS button")
        logs_button = self.driver.find_element(*MainMenuScreen.LOGS_BUTTON)
        self.assertIsNotNone(logs_button, "LOGS button not found")
        logs_button.click()

    def open_REPORTS(self):

        logging.info("clicking in REPORTS button")
        reports_button = self.driver.find_element(*MainMenuScreen.REPORTS_BUTTON)
        self.assertIsNotNone(reports_button, "REPORTS button not found")
        reports_button.click()

    def open_MAP(self):

        logging.info("clicking in Map button")
        map_button = self.driver.find_element(*MainMenuScreen.MAP_BUTTON)
        self.assertIsNotNone(map_button, "MAP button not found")
        map_button.click()

    def open_LOCATION(self):

        logging.info("clicking in Location button")
        location_button = self.driver.find_element(*MainMenuScreen.LOCATION_BUTTON)
        self.assertIsNotNone(location_button, "Location button not found")
        location_button.click()

    def open_ASSETS(self):

        logging.info("clicking in ASSETS button")
        assets_button = self.driver.find_element(*MainMenuScreen.ASSETS_BUTTON)
        self.assertIsNotNone(assets_button, "ASSETS button not found")
        assets_button.click()

    def open_MY_MESSAGES(self):
        logging.info("clicking in MY MESSAGES button")
        my_messages_button = self.driver.find_element(*MainMenuScreen.MY_MESSAGES_BUTTON)
        self.assertIsNotNone(my_messages_button, "MY MESSAGES button not found")
        my_messages_button.click()

    def open_INBOX(self):
        logging.info("clicking in INBOX button")
        inbox_button = self.driver.find_element(*MainMenuScreen.INBOX_BUTTON)
        self.assertIsNotNone(inbox_button, "INBOX button not found")
        inbox_button.click()

    def open_COMPOSE(self):
        logging.info("clicking in COMPOSE button")
        compose_button = self.driver.find_element(*MainMenuScreen.COMPOSE_BUTTON)
        self.assertIsNotNone(compose_button, "COMPOSE button not found")
        compose_button.click()

    def open_SENT(self):
        logging.info("clicking in SENT button")
        sent_button = self.driver.find_element(*MainMenuScreen.SENT_BUTTON)
        self.assertIsNotNone(sent_button, "SENT button not found")
        sent_button.click()
        sleep(2)

    def open_PHOTO(self):

        logging.info("clicking in Photo button")
        photo_button = self.driver.find_element(*MainMenuScreen.PHOTO_BUTTON)
        self.assertIsNotNone(photo_button, "PHOTO button not found")
        photo_button.click()

    def open_VIDEO(self):

        logging.info("clicking in Video button")
        video_button = self.driver.find_element(*MainMenuScreen.VIDEO_BUTTON)
        self.assertIsNotNone(video_button, "VIDEO button not found")
        video_button.click()

    def open_SOUND(self):

        logging.info("clicking in Sound button")
        sound_button = self.driver.find_element(*MainMenuScreen.SOUND_BUTTON)
        self.assertIsNotNone(sound_button, "Sound button not found")
        sound_button.click()

    def open_TASKS(self):

        logging.info("clicking in TASKS button")
        tasks_button = self.driver.find_element(*MainMenuScreen.TASKS_BUTTON)
        self.assertIsNotNone(tasks_button, "TASKS button not found")
        tasks_button.click()

    def open_DOCUMENTS(self):

        logging.info("clicking in DOCUMENTS button")
        documents_button = self.driver.find_element(*MainMenuScreen.DOCUMENTS_BUTTON)
        self.assertIsNotNone(documents_button, "DOCUMENTS button not found")
        documents_button.click()

    def open_CONTACTS(self):

        logging.info("clicking in CONTACTS button")
        contacts_button = self.driver.find_element(*MainMenuScreen.CONTACTS_BUTTON)
        self.assertIsNotNone(contacts_button, "CONTACTS button not found")
        contacts_button.click()

    def open_ALLOCATE(self):

        logging.info("clicking in ALLOCATE button")
        allocate_button = self.driver.find_element(*MainMenuScreen.ALLOCATE_BUTTON)
        self.assertIsNotNone(allocate_button, "ALLOCATE button not found")
        allocate_button.click()

    def open_SETTINGS(self):
        logging.info("clicking in SETTINGS button")
        settings_button = self.driver.find_element(*MainMenuScreen.SETTINGS_BUTTON)
        self.assertIsNotNone(settings_button, "SETTINGS button not found")
        settings_button.click()

    def open_ACTIVATE(self):
        logging.info("clicking in ACTIVATE button")
        activate_button = self.driver.find_element(*MainMenuScreen.ACTIVATE_BUTTON)
        self.assertIsNotNone(activate_button, "ACTIVATE button not found")
        activate_button.click()

    def open_OFFLINE_SYNC(self):
        logging.info("clicking in OFFLINE SYNC button")
        offline_sync_button = self.driver.find_element(*MainMenuScreen.OFFLINE_SYNC_BUTTON)
        self.assertIsNotNone(offline_sync_button, "OFFLINE SYNC button not found")
        offline_sync_button.click()

    def open_ABOUT(self):
        logging.info("clicking in ABOUT button")
        about_button = self.driver.find_element(*MainMenuScreen.ABOUT_BUTTON)
        self.assertIsNotNone(about_button, "ABOUT button not found")
        about_button.click()


class PhotoPage(BasePage):
    """A class for methods to handle Photo Page"""

    def check_if_photo_page_was_opened(self):

        logging.info("check_if_photo_page_was_opened")
        photo_page_header = self.driver.find_element(*PhotoScreen.PHOTO_PAGE_HEADER)
        self.assertIsNotNone(photo_page_header, "Photo page header was not found")
        logging.info("Photo page was opened")

    def click_gallery_button(self):

        logging.info("clicking in Gallery button")
        gallery_button = self.driver.find_element(*PhotoScreen.GALLERY_BUTTON)
        self.assertIsNotNone(gallery_button, "Gallery button not found")
        gallery_button.click()

    def click_take_new_button(self):

        logging.info("clicking in Take new button")
        take_new_button = self.driver.find_element(*PhotoScreen.TAKE_NEW_BUTTON)
        self.assertIsNotNone(take_new_button, "Take new button not found")
        take_new_button.click()

    def type_description(self, description):

        WebDriverWait(self.driver, 35).until(
            expected_conditions.presence_of_element_located(PhotoScreen.DESCRIPTION_FIELD),
            "Failed to locate description field for photo")
        logging.info("type text into description field")
        description_field = self.driver.find_element(*PhotoScreen.DESCRIPTION_FIELD)
        self.assertIsNotNone(description_field, "Description field not found")
        description_field.send_keys(description)

    def click_send_button(self):

        sleep(1)
        logging.info("click send button")
        send_button = self.driver.find_element(*PhotoScreen.SEND_BUTTON)
        self.assertIsNotNone(send_button)
        send_button.click()
        logging.info("sending file")
        sleep(1)
        WebDriverWait(self.driver, 420).until(
            expected_conditions.presence_of_element_located(MainMenuScreen.LOCATION_BUTTON),
            "Failed to send file")
        logging.info("File was sent")

    def click_reset_button(self):

        logging.info("click send button")
        reset_button = self.driver.find_element(*PhotoScreen.RESET_BUTTON)
        self.assertIsNotNone(reset_button)
        reset_button.click()


class GalleryPage(BasePage):
    """A class for methods to handle Gallery Page"""

    def choose_element_1(self):

        logging.info("choosing element 1")
        choose_element_1 = self.driver.find_element(*GalleryScreen.GALLERY_ELEMENT_1)
        self.assertIsNotNone(choose_element_1, "first element in gallery not found")
        choose_element_1.click()


class VideoPage(PhotoPage):
    """A class for methods to handle Video Page"""

    def check_if_video_page_was_opened(self):

        video_page_header = self.driver.find_element(*VideoScreen.VIDEO_PAGE_HEADER)
        self.assertIsNotNone(video_page_header, "Video page header was not found")
        logging.info("Video page was opened")

    def click_record_new_button(self):

        logging.info("clicking in 'Record new' button")
        try:
            record_new_button = self.driver.find_element(*VideoScreen.RECORD_NEW_BUTTON)
            if record_new_button.is_displayed():
                self.assertIsNotNone(record_new_button, "record new button not found")
                record_new_button.click()
        except NoSuchElementException:
            action = TouchAction(self.driver)
            action.tap(element=None, x=548, y=158, count=1).perform()
        # add coordinates for iPhones


class SoundPage(PhotoPage):
    """A class for methods to handle Sound Page"""

    def check_if_sound_page_was_opened(self):

        video_page_header = self.driver.find_element(*SoundScreen.SOUND_PAGE_HEADER)
        self.assertIsNotNone(video_page_header, "Sound page header was not found")
        logging.info("Sound page was opened")

    def click_record_sound_icon(self):

        logging.info("clicking in 'Record Sound' icon")
        try:
            record_sound_button = self.driver.find_element(*SoundScreen.RECORD_SOUND_BUTTON)
            if record_sound_button.is_displayed():
                self.assertIsNotNone(record_sound_button, "record sound button not found")
                record_sound_button.click()
        except NoSuchElementException:
            self.fail("failed to click 'Record Sound'")


class SoundRecorder(BasePage):
    """A class for methods to handle Sound Recorder"""

    def record_sound(self):

        logging.info("click record sound")
        try:
            sound_capture_android_6 = self.driver.find_element(*SoundRecorderScreen.RECORD_SOUND_android_6)
            if sound_capture_android_6.is_displayed():
                self.assertIsNotNone(sound_capture_android_6, "sound capture button not found")
                sound_capture_android_6.click()
        except NoSuchElementException:
            pass
        try:
            sound_capture_android_5 = self.driver.find_element(*SoundRecorderScreen.RECORD_SOUND_android_5)
            if sound_capture_android_5.is_displayed():
                self.assertIsNotNone(sound_capture_android_5, "sound capture button not found")
                sound_capture_android_5.click()
        except NoSuchElementException:
            pass
        try:
            sound_capture_android_4 = self.driver.find_element(*SoundRecorderScreen.RECORD_SOUND_android_4)
            if sound_capture_android_4.is_displayed():
                self.assertIsNotNone(sound_capture_android_4, "sound capture button not found")
                sound_capture_android_4.click()
        except NoSuchElementException:
            pass

    def stop_recording(self):

        logging.info("stop recording")
        try:
            stop_recording_android_6 = self.driver.find_element(*SoundRecorderScreen.STOP_RECORDING_android_6)
            if stop_recording_android_6.is_displayed():
                self.assertIsNotNone(stop_recording_android_6, "stop recording button not found")
                stop_recording_android_6.click()
        except NoSuchElementException:
            pass
        try:
            stop_recording_android_5 = self.driver.find_element(*SoundRecorderScreen.STOP_RECORDING_android_5)
            if stop_recording_android_5.is_displayed():
                self.assertIsNotNone(stop_recording_android_5, "stop recording button not found")
                stop_recording_android_5.click()
        except NoSuchElementException:
            pass
        try:
            stop_recording_android_4 = self.driver.find_element(*SoundRecorderScreen.STOP_RECORDING_android_4)
            if stop_recording_android_4.is_displayed():
                self.assertIsNotNone(stop_recording_android_4, "stop recording button not found")
                stop_recording_android_4.click()
        except NoSuchElementException:
            pass

    def click_done_button(self):

        logging.info("click click 'Done' button")
        try:
            done_button_android_6 = self.driver.find_element(*SoundRecorderScreen.DONE_BUTTON_android_6)
            if done_button_android_6.is_displayed():
                self.assertIsNotNone(done_button_android_6, "Done button not found")
                done_button_android_6.click()
        except NoSuchElementException:
            pass
        try:
            done_button_android_5 = self.driver.find_element(*SoundRecorderScreen.DONE_BUTTON_android_5)
            if done_button_android_5.is_displayed():
                self.assertIsNotNone(done_button_android_5, "Done button not found")
                done_button_android_5.click()
        except NoSuchElementException:
            pass
        try:
            done_button_android_4 = self.driver.find_element(*SoundRecorderScreen.DONE_BUTTON_android_4)
            if done_button_android_4.is_displayed():
                self.assertIsNotNone(done_button_android_4, "Done button not found")
                done_button_android_4.click()
        except NoSuchElementException:
            pass


class CameraPage(BasePage):
    """A class for methods to handle Camera"""

    def capture(self):

        logging.info("capture photo/video")
        try:
            photo_capture1 = self.driver.find_element(*CameraScreen.CAPTURE_BUTTON_ANDROID_6)
            if photo_capture1.is_displayed():
                self.assertIsNotNone(photo_capture1)
                photo_capture1.click()
        except NoSuchElementException:
            photo_capture2 = self.driver.find_element(*CameraScreen.CAPTURE_BUTTON_ANDROID_4_and_5)
            if photo_capture2.is_displayed():
                self.assertIsNotNone(photo_capture2)
                photo_capture2.click()

    def click_cancel(self):

        logging.info("click Cancel")
        cancel = self.driver.find_element(*CameraScreen.CANCEL_PHOTO_BUTTON)
        self.assertIsNotNone(cancel)
        cancel.click()

    def click_use(self):

        logging.info("Use Photo")
        try:
            use_photo1 = self.driver.find_element(*CameraScreen.USE_PHOTO_ANDROID4)
            if use_photo1.is_displayed():
                self.assertIsNotNone(use_photo1)
                action = TouchAction(self.driver)
                action.tap(element=use_photo1, count=1).perform()
        except NoSuchElementException:
            pass
        try:
            use_photo2 = self.driver.find_element(*CameraScreen.USE_PHOTO_ANDROID5)
            if use_photo2.is_displayed():
                self.assertIsNotNone(use_photo2)
                action = TouchAction(self.driver)
                action.tap(element=use_photo2, count=1).perform()
        except NoSuchElementException:
            pass
        try:
            use_photo3 = self.driver.find_element(*CameraScreen.USE_PHOTO_ANDROID6)
            if use_photo3.is_displayed():
                self.assertIsNotNone(use_photo3)
                action = TouchAction(self.driver)
                action.tap(element=use_photo3, count=1).perform()
        except NoSuchElementException:
            pass

    def click_retake(self):

        logging.info("Retake")
        try:
            retake_photo_android_4 = self.driver.find_element(*CameraScreen.RETAKE_ANDROID_4)
            if retake_photo_android_4.is_displayed():
                self.assertIsNotNone(retake_photo_android_4)
                retake_photo_android_4.click()
        except NoSuchElementException:
            pass
        try:
            retake_photo_android_5 = self.driver.find_element(*CameraScreen.RETAKE_ANDROID_5)
            if retake_photo_android_5.is_displayed():
                self.assertIsNotNone(retake_photo_android_5)
                retake_photo_android_5.click()
        except NoSuchElementException:
            pass
        try:
            retake_photo_android_6 = self.driver.find_element(*CameraScreen.RETAKE_ANDROID_6)
            if retake_photo_android_6.is_displayed():
                self.assertIsNotNone(retake_photo_android_6)
                retake_photo_android_6.click()
        except NoSuchElementException:
            pass

    def choose_camera(self):

        logging.info("click choose camera")
        try:
            chooser_camera = self.driver.find_element(*CameraScreen.CAMERA_CHOOSER)
            if chooser_camera.is_displayed():
                self.assertIsNotNone(chooser_camera)
                chooser_camera.click()
        except NoSuchElementException:
            pass
        try:
            chooser_camera2 = self.driver.find_element(*CameraScreen.CAMERA_CHOOSER2)
            if chooser_camera2.is_displayed():
                self.assertIsNotNone(chooser_camera2)
                chooser_camera2.click()
        except NoSuchElementException:
            pass
        try:
            chooser_camera_for_android_4 = self.driver.find_element(*CameraScreen.CAMERA_CHOOSER_ANDROID4)
            if chooser_camera_for_android_4.is_displayed():
                self.assertIsNotNone(chooser_camera_for_android_4)
                chooser_camera_for_android_4.click()
        except NoSuchElementException:
            pass


class LocationPage(BasePage):
    """A class for methods to handle Location Page"""

    def check_if_location_page_was_opened(self):

        location_page_header = self.driver.find_element(*LocationScreen.LOCATION_PAGE_HEADER)
        self.assertIsNotNone(location_page_header, "Location Page header was not found")

    def click_send_once_now(self):

        logging.info("clicking in 'Send once now' button")
        send_once_now_button = self.driver.find_element(*LocationScreen.SEND_ONCE_NOW)
        self.assertIsNotNone(send_once_now_button)
        send_once_now_button.click()

    def check_if_location_was_sent(self):

        sleep(5)
        logging.info("check if location was sent")
        # location_status = self.driver.find_element(*LocationScreen.LOCATION_STATUS_ios)
        # self.assertIsNotNone(location_status)
        try:
            WebDriverWait(self.driver, 65).until(
                expected_conditions.presence_of_element_located(LocationScreen.LOCATION_STATUS),
                "Failed to send location")
            logging.info("Location was sent")
        except NoSuchElementException:
            logging.info("Failed to send location")
            self.fail("Failed to send location")

    def click_send_every(self):

        logging.info("clicking in 'Send every' selector")
        send_every_button = self.driver.find_element(*LocationScreen.SEND_EVERY_SPINNER)
        self.assertIsNotNone(send_every_button)
        send_every_button.click()

    def choose_send_every_5_minutes_option(self):

        logging.info("choose send every '5 minutes' option")
        choose_5_minutes_option = self.driver.find_element(*LocationScreen.CHOOSE_5_MINUTES_OPTION)
        self.assertIsNotNone(choose_5_minutes_option)
        choose_5_minutes_option.click()

    def check_if_5_minutes_option_was_chosen(self):

        logging.info("check if send every '5 minutes'  option was chosen")
        check_if_5_minutes_option_was_chosen = self.driver.find_element(*LocationScreen.ASSERT_5_MINUTES_OPTION)
        self.assertIsNotNone(check_if_5_minutes_option_was_chosen)

    def click_for_the_next(self):

        logging.info("clicking in 'For the next' selector")
        for_the_next = self.driver.find_element(*LocationScreen.FOR_THE_NEXT_SPINNER)
        self.assertIsNotNone(for_the_next)
        for_the_next.click()

    def choose_1_hour_option(self):

        logging.info("choose '1 hour' option")
        choose_1_hour_option = self.driver.find_element(*LocationScreen.CHOOSE_1_HOUR_OPTION)
        self.assertIsNotNone(choose_1_hour_option)
        choose_1_hour_option.click()

    def check_if_1_hour_option_was_chosen(self):

        logging.info("check if '1 hour' option was chosen")
        check_if_1hour_option_was_chosen = self.driver.find_element(*LocationScreen.ASSERT_1_HOUR_OPTION)
        self.assertIsNotNone(check_if_1hour_option_was_chosen)

    # def check_if_button_send_once_was_pressed(self):
    #
    #     logging.info("check_if_1hour_option_was_chosen")
    #     check_if_1hour_option_was_chosen = self.driver.find_element(*LocationScreen.)
    #     self.assertIsNotNone(check_if_1hour_option_was_chosen)

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


class EventsPage(Common):
    """A class for methods to handle Events Page"""

    def check_if_EVENTS_were_opened(self):

        sleep(2)
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

        # android 4.4.2 and 5.1 can't click correctly in "Search field" because of that
        #  Appium can't send keys into text field
        # - icon is on top of the text field and Appium is trying to send keys to it
        logging.info("search field - search event named: 'search'")
        sleep(2)
        search_field = self.driver.find_element(*EventsScreen.SEARCH_FIELD)
        search_field.click()
        logging.info("sending keys")
        self.driver.keyevent(47)  # send letter 'S'
        self.driver.keyevent(33)  # send letter 'E'
        self.driver.keyevent(29)  # send letter 'A'
        self.driver.keyevent(46)  # send letter 'R'

    def clear_Search_field(self):

        logging.info("clear search field")
        search_field = self.driver.find_element(*EventsScreen.SEARCH_FIELD)
        action = TouchAction(self.driver)
        action.long_press(el=search_field, duration=1000).perform()
        self.driver.keyevent(67)

    def click_More_button(self):

        sleep(1)
        logging.info("click 'More' button")
        Common.spinner_button_on_the_right(self)
        # more_button = self.driver.find_element(*CommonScreen.SPINNER_ON_THE_RIGHT)
        # self.assertIsNotNone(more_button, "More button was not found")
        # more_button.click()
        sleep(0.5)

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
        # logging.info("checking notification - 'Primary event cleared'")
        # notification = self.driver.find_element(*EventsScreen.NOTIFICATION_PRIMARY_EVENT_CLEARED)
        # self.assertIsNotNone(notification)

    def open_previously_created_event1(self):

        logging.info("open created event")
        created_event1 = self.driver.find_element(*EventsScreen.CREATED_EVENT_1)
        self.assertIsNotNone(created_event1)
        created_event1.click()
        sleep(5)

    def open_previously_created_event2(self):

        logging.info("open previously created Event")
        created_event2 = self.driver.find_element(*EventsScreen.CREATED_EVENT_2)
        self.assertIsNotNone(created_event2)
        created_event2.click()
        sleep(5)

    def open_previously_created_event3(self):

        logging.info("open previously created Event")
        created_event3 = self.driver.find_element(*EventsScreen.CREATED_EVENT_3)
        self.assertIsNotNone(created_event3)
        created_event3.click()
        sleep(5)

    # only for events list, opened from chooser fields inside other event
    def click_on_previously_created_event_for_chooser_field(self):

        sleep(5)
        logging.info("click_on_previously_created_event_for_chooser_field")
        event_for_chooser_field = self.driver.find_element(*EventEditScreen.PREVIOUSLY_CREATED_EVENT_FOR_CHOOSER)
        self.assertIsNotNone(event_for_chooser_field)
        event_for_chooser_field.click()
        sleep(5)

    def click_on_previously_created_event_for_subform_chooser(self):

        sleep(10)
        logging.info("click_on_previously_created_event_for_subform_chooser")
        event_for_subform = self.driver.find_element(*EventEditScreen.PREVIOUSLY_CREATED_EVENT_FOR_SUBFORM_CHOOSER)
        self.assertIsNotNone(event_for_subform)
        event_for_subform.click()
        # sleep(1)
        # try:
        #     event_for_subform.click()
        # except NoSuchElementException:
        #     action = TouchAction(self.driver)
        #     action.tap(element=event_for_subform, count=1).perform()
        sleep(5)


class EventsTypesPage(BasePage):
    """A class for methods to handle Events Types Page"""

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
        sleep(5)


class EventEditPage(Common):
    """A class for methods to handle Event Edit Page"""

    def fill_Name_input_field(self, text):
        logging.info("input Name input field")
        name_field = self.driver.find_element(*EventEditScreen.NAME_FIELD)
        self.assertIsNotNone(name_field)
        name_field.click()
        name_field.send_keys(text)

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
        logging.info("type some text into description field")
        self.driver.find_element(*EventEditScreen.DESCRIPTION_FIELD).send_keys("test Android")

    def click_create_mapping_data(self):

        logging.info("create mapping data")
        create_mapping_data_button = self.driver.find_element(*EventEditScreen.CREATE_MAPPING_DATA)
        self.assertIsNotNone(create_mapping_data_button, "Button for creating map data is not present")
        create_mapping_data_button.click()

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

        sleep(4)
        logging.info("click on option list")
        action = TouchAction(self.driver)
        screen_size = self.driver.get_window_size(windowHandle='current')  # it creates dictionary
        if screen_size['width'] < 1000:
            action.tap(element=None, x=250, y=530, count=1).perform()  # coordinates for clicking into "Option List"
        else:
            action.tap(element=None, x=700, y=1430, count=1).perform()
        # try:
        #     option_list = self.driver.find_element(*EventEditScreen.NEW_OPTION_LIST_HEADER)
        #     self.assertIsNotNone(option_list)
        #     option_list.click()
        # except NoSuchElementException:
        #     action = TouchAction(self.driver)
        #     action.tap(element=None, x=700, y=1430, count=1).perform()
        # try:
        #     option_list.click()
        # except NoSuchElementException:
        #     action.tap(element=None, x=700, y=1700, count=1).perform()
        #     self.fail("appium could not click on option list")
        # action.tap(element=option_list, count=1).perform()
        # header after opening option list
        header_after_opening_option_list = self.driver.find_element(*EventEditScreen.HEADER_ON_OPTION_LIST_PAGE)
        self.assertIsNotNone(header_after_opening_option_list)
        # try:
        #     if new_option_list.is_displayed():
        #         new_option_list.click()
        #     elif new_option_list.is_displayed():
        #         action.long_press(new_option_list, duration=500).perform()
        #     elif new_option_list.is_enabled():
        #         action.press(new_option_list).perform()
        #     else:
        #         action.tap(element=new_option_list, count=1).perform()
        # except NoSuchElementException:
        #     pass

    def check_restored_field_1(self):

        sleep(4)
        try:
            logging.info("assert restored field 1")
            field_to_restore_1_header = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_1_HEADER)
            self.assertIsNotNone(field_to_restore_1_header)
            field_to_restore_1_value = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_1_VALUE)
            self.assertIsNotNone(field_to_restore_1_value)
        except NoSuchElementException:
            logging.info("unable to check restored field 1")

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

        try:
            field_to_restore_1_header = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_1_HEADER)
            field_to_restore_2_header = self.driver.find_element(*EventEditScreen.FIELD_TO_RESTORE_2_HEADER)
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

        sleep(1)
        logging.info("click button Add row")
        add_row = self.driver.find_element(*EventEditScreen.SUBFORM_FIELD_ADD_ROW)
        self.assertIsNotNone(add_row, "add_row button not found")
        action = TouchAction(self.driver)
        action.tap(element=add_row, count=1).perform()
        # add_row.click()

    def click_on_event_chooser_field(self):

        logging.info("click_on_event_chooser_field")
        chooser_field_for_event = self.driver.find_element(*EventEditScreen.CHOOSER_FIELD)
        self.assertIsNotNone(chooser_field_for_event, "chooser_field_for_event not found")
        chooser_field_for_event.click()
        sleep(1)

    def click_on_choose_field_inside_subform(self):

        sleep(5)
        logging.info("click_on_choose_field_inside_subform")
        event_chooser_in_subform = self.driver.find_element(*EventEditScreen.NEW_EVENTS_CHOOSER_IN_SUB_FORM)
        self.assertIsNotNone(event_chooser_in_subform, "event chooser in subform not found")
        event_chooser_in_subform.click()
        sleep(5)

    def delete_chosen_event_inside_subform(self):

        sleep(5)
        logging.info("delete chosen event inside sub form")
        delete_button_inside_sub_form = self.driver.find_element(*EventEditScreen.DELETE_SUB_EVENT_FROM_CHOOSER)
        self.assertIsNotNone(delete_button_inside_sub_form, "delete button inside sub form not found")
        delete_button_inside_sub_form.click()
        sleep(5)
        try:
            previously_created_event_for_subform_chooser = self.driver.find_element(
                *EventEditScreen.PREVIOUSLY_CREATED_EVENT_FOR_SUBFORM_CHOOSER)
            self.assertIsNone(previously_created_event_for_subform_chooser)
        except NoSuchElementException:
            pass


class OptionList(BasePage):
    """A class for methods to handle Option List inside form to create event"""

    def click_on_option_1(self):

        sleep(1)
        logging.info("choose '1' in option list")
        option_1 = self.driver.find_element(*EventEditScreen.OPTION_LIST_VALUE_1)
        self.assertIsNotNone(option_1, "option list - option '1' not found")
        action = TouchAction(self.driver)
        try:
            action.tap(element=option_1, count=1).perform()
        except:
            option_1.click()

    def click_on_option_2(self):

        logging.info("choose '2' in option list")
        option_2 = self.driver.find_element(*EventEditScreen.OPTION_LIST_VALUE_2)
        self.assertIsNotNone(option_2, "option list - option '2' not found")
        action = TouchAction(self.driver)
        try:
            action.tap(element=option_2, count=1).perform()
        except:
            option_2.click()

    def click_on_option_3(self):

        logging.info("choose '3' in option list")
        option_3 = self.driver.find_element(*EventEditScreen.OPTION_LIST_VALUE_3)
        self.assertIsNotNone(option_3, "option list - option '3' not found")
        action = TouchAction(self.driver)
        try:
            action.tap(element=option_3, count=1).perform()
        except:
            option_3.click()


class MapPage(BasePage):
    """A class for methods to handle Map"""

    def wait_for_map_to_load(self):

        logging.info("Waiting for map to load")
        try:
            WebDriverWait(self.driver, 30).until(
                expected_conditions.presence_of_element_located(Map.MAP_AREA_6),
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

        polygon_button = self.driver.find_element(*Map.POLYGON_BUTTON)
        self.assertIsNotNone(polygon_button, "polygon button not found")
        polygon_button.click()

    def click_default_button(self):

        default_button = self.driver.find_element(*Map.DEFAULT_BUTTON)
        self.assertIsNotNone(default_button, "default button not found")
        default_button.click()

    def click_in_map_area_9(self):

        logging.info("click on map")
        action = TouchAction(self.driver)
        screen_size = self.driver.get_window_size(windowHandle='current')  # it creates dictionary
        try:
            if screen_size['width'] > 1400:
                action.tap(element=None, x=600, y=900, count=1).perform()
            else:
                logging.info("executing tap on map - width < 1400")
                action.tap(element=None, x=300, y=450, count=1).perform()
        except NoSuchElementException:
            map9 = self.driver.find_element(*Map.MAP_AREA_9)
            action.tap(element=map9, count=1).perform()
        sleep(1)

    def click_in_map_area_3(self):

        logging.info("click on map")
        action = TouchAction(self.driver)
        screen_size = self.driver.get_window_size(windowHandle='current')
        try:
            if screen_size['width'] > 1400:
                action.tap(element=None, x=300, y=1600, count=1).perform()
            else:
                logging.info("executing tap on map - width < 1400")
                action.tap(element=None, x=150, y=400, count=1).perform()
        except NoSuchElementException:
            map3 = self.driver.find_element(*Map.MAP_AREA_3)
            action.tap(element=map3, count=1).perform()
        sleep(1)

    def double_click_in_map_area_6(self):

        logging.info("double click on map")
        action = TouchAction(self.driver)
        screen_size = self.driver.get_window_size(windowHandle='current')
        try:
            if screen_size['width'] > 1400:
                action.tap(element=None, x=1200, y=1900, count=2).perform()
            else:
                logging.info("executing tap on map - width < 1400")
                action.tap(element=None, x=100, y=600, count=2).perform()
        except NoSuchElementException:
            map6 = self.driver.find_element(*Map.MAP_AREA_6)
            action.tap(element=map6, count=2).perform()
        sleep(1)

    def save_map(self):

        logging.info("Save map")
        save_map_button = self.driver.find_element(*Map.SAVE_MAP_BUTTON)
        self.assertIsNotNone(save_map_button, "save map button not found")
        save_map_button.click()
        sleep(3)


class EventDetailsPage(BasePage):
    """A class for methods to handle Event Details Page"""

    def click_edit_button(self):

        logging.info("edit previously created event")
        edit_button = self.driver.find_element(*EventDetailsScreen.EDIT_BUTTON)
        self.assertIsNotNone(edit_button, "edit button not found")
        edit_button.click()
        # sleep(2)

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


class NewContactPage(Common):
    """A class for methods to handle New Contact Page"""

    def type_first_name(self, text):

        logging.info("type first name")
        first_name = self.driver.find_element(*NewContactScreen.FIRST_NAME)
        self.assertIsNotNone(first_name, "First name input field was not found")
        first_name.click()
        first_name.send_keys(text)


class NewTaskPage(AndroidDevice, Common):
    """A class for methods to handle New Task Page"""

    def type_title(self, text):

        logging.info("type title")
        title = self.driver.find_element(*NewTaskScreen.TITLE)
        self.assertIsNotNone(title, "Title input field was not found")
        title.click()
        title.send_keys(text)

    def click_on_assigned(self):

        logging.info("click on Assigned field")
        assigned = self.driver.find_element(*NewTaskScreen.ASSIGNED)
        self.assertIsNotNone(assigned, "Assigned field was not found")
        assigned.click()

    def add_contacts(self):

        logging.info("Add Assignees")
        assignees = self.driver.find_element(*NewTaskScreen.ADD_CONTACTS_AND_GROUPS)
        self.assertIsNotNone(assignees, "Assignees field was not found")
        assignees.click()

    def choose_users(self):

        logging.info("Choose Users")
        assignees = self.driver.find_element(*NewTaskScreen.CHOOSE_USERS)
        self.assertIsNotNone(assignees, "Users option list was not found")
        assignees.click()

    def choose_start_date(self):

        logging.info("Choose Start Date")
        start_date = self.driver.find_element(*NewTaskScreen.START_DATE)
        self.assertIsNotNone(start_date, "Start Date field was not found")
        start_date.click()


class NewReportPage(NewTaskPage):
    """A class for methods to handle New Report Page"""

    def type_title(self, text):

        NewTaskPage.type_title(self, text)

    def click_on_lodging_agency_picker(self):

        logging.info("choose Lodging Agency - second position on the list")
        lodging_agency_picker = self.driver.find_element(*NewReportScreen.LODGING_AGENCY_PICKER)
        self.assertIsNotNone(lodging_agency_picker, "Lodging Agency picker was not found")
        lodging_agency_picker.click()

    def choose_lodging_agency(self):

        logging.info("choose Lodging Agency")
        lodging_agency = self.driver.find_element(*NewReportScreen.LODGING_AGENCY)
        self.assertIsNotNone(lodging_agency, "Lodging Agency inside picker was not found")
        lodging_agency.click()

    def click_publish_button(self):

        logging.info("click Publish button")
        publish_button = self.driver.find_element(*NewReportScreen.PUBLISH_BUTTON)
        self.assertIsNotNone(publish_button, "Publish button was not found")
        sleep(1)
        action = TouchAction(self.driver)
        action.tap(element=publish_button, count=1).perform()
        # publish_button.click()


# Appium can't access another app directly only tapping on specific coordinates will work
class ChromeBrowserPage(BasePage):
    """A class for methods to handle Chrome Browser Page"""


class NewAssetPage(Common):
    """A class for methods to handle New Asset Page"""

    def fill_Name_input_field(self, text):

        Common.fill_Name_input_field(self, text)


class NewLogPage(NewReportPage):
    """A class for methods to handle New Log Page"""

    def click_on_lodging_agency_picker(self):

        logging.info("click on 'Lodging Agency' picker")
        lodging_agency_picker = self.driver.find_element(*NewLogScreen.LODGING_AGENCY_PICKER)
        self.assertIsNotNone(lodging_agency_picker, "Lodging Agency picker was not found")
        lodging_agency_picker.click()

    def choose_lodging_agency(self):

        NewReportPage.choose_lodging_agency(self)

    def type_text_into_entry_field(self, text):

        sleep(1)
        logging.info("type text into 'Entry' field")
        entry_field = self.driver.find_element(*NewLogScreen.ENTRY_FIELD)
        entry_field.click()
        entry_field.send_keys(text)


class RisksPage(Common):
    """A class for methods to handle Risks Page"""

    def click_new_risk_register(self):

        logging.info("create risk register")
        create_risk_register_button = self.driver.find_element(*RisksScreen.CREATE_RISK_REGISTER)
        self.assertIsNotNone(create_risk_register_button, "Create Risk Register button not found")
        create_risk_register_button.click()

    def open_existing_risk_register(self):

        logging.info("open first risk register on the list")
        open_existing_risk_register = self.driver.find_element(*RisksScreen.FIRST_RISK_REGISTER_ON_THE_LIST)
        self.assertIsNotNone(open_existing_risk_register, "open existing Risk Register")
        open_existing_risk_register.click()

    def click_new_button(self):

        logging.info("click new button")
        Common.spinner_button_on_the_right(self)
        # click_new_button = self.driver.find_element(*CommonScreen.SPINNER_ON_THE_RIGHT)
        # self.assertIsNotNone(click_new_button, "New button not found")
        # click_new_button.click()

    def click_add_new_context(self):

        logging.info("click add new context")
        click_add_new_context = self.driver.find_element(*RisksScreen.ADD_NEW_CONTEXT)
        self.assertIsNotNone(click_add_new_context, "Add new context button not found")
        click_add_new_context.click()


class RiskRegisterEditPage(EventEditPage):
    """A class for methods to handle Risk Register Edit Page"""

    def fill_Name_input_field(self, text):

        EventEditPage.fill_Name_input_field(self, text)


class ContextEditPage(Common):
    """A class for methods to handle Context Edit Page"""

    def fill_Name_input_field(self, text):
        logging.info("input Name input field")
        name_field = self.driver.find_element(*ContextEditScreen.NAME_FIELD)
        self.assertIsNotNone(name_field)
        name_field.click()
        name_field.send_keys(text)


class ContextPage(Common):
    """A class for methods to handle Context Page"""

    def open_existing_context(self):

        logging.info("open existing context")
        open_existing_context = self.driver.find_element(*ContextScreen.FIRST_CONTEXT_ON_THE_LIST)
        self.assertIsNotNone(open_existing_context, "open existing context")
        open_existing_context.click()

    def click_new_button(self):

        logging.info("click new button")
        Common.spinner_button_on_the_right(self)


class SentPage(Common):
    """A class for methods to handle Sent Page"""





