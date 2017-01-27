import unittest
from time import sleep
# import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from appium.webdriver.common.multi_action import MultiAction
# from appium.webdriver.mobilecommand import MobileCommand
# from appium.webdriver import WebElement
# from appium.webdriver.webdriver import MobileWebElement
#from locators_ios import *
from locators_ios10 import *
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

    # OCA top bar
    def hamburger_button(self):
        # add coordinates for iPhones - clicking is not working because button is invisible
        logging.info("click hamburger button to go back to main menu")
        try:
            hamburger_button = self.driver.find_element(*TopBar.HAMBURGER_FOR_MAIN_MENU_ios)
            if hamburger_button.is_displayed():
                self.assertIsNotNone(hamburger_button, "Hamburger button is not present")
                hamburger_button.click()
        except NoSuchElementException:
            positions_for_hamburger_button = [(730, 20)]
            sleep(1)
            self.driver.tap(positions_for_hamburger_button)


class iOSdevice(BasePage):
    """A class for methods to handle iOS Device"""

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


class Common(BasePage):
    """A class for methods to handle Common buttons from different screens"""

    def save_button(self):

        logging.info("click Save button")
        save_button = self.driver.find_element(*CommonScreen.SAVE_BUTTON_ios)
        self.assertIsNotNone(save_button, "Save button not found")
        save_button.click()
        sleep(10)

    def cancel_button(self):
        logging.info("click on Cancel button")
        cancel_button = self.driver.find_element(*CommonScreen.CANCEL_BUTTON_ios)
        self.assertIsNotNone(cancel_button, "Cancel button not found")
        cancel_button.click()

    def ok_button(self):
        logging.info("click on 'Ok' button")
        ok_button = self.driver.find_element(*CommonScreen.OK_BUTTON_ios)
        self.assertIsNotNone(ok_button, "Ok button not found")
        ok_button.click()

    def fill_Name_input_field(self, text):

        logging.info("fill Name input field")
        try:
            name_field = self.driver.find_element(*EventEditScreen.NAME_FIELD_ios)
            if name_field.is_displayed():
                name_field.click()
                name_field.send_keys(text)
        except NoSuchElementException:
            name_field_by_index = self.driver.find_element(*EventEditScreen.NAME_FIELD_by_index_ios)
            if name_field_by_index.is_displayed():
                name_field_by_index.click()
                name_field_by_index.send_keys(text)


class WelcomePage(Common):
    """A class for methods to handle Welcome Page"""

    def click_login_button(self):

        # sleep(10)
        self.driver.reset()  # reset app to avoid problems with locating elements
        # try:
        #     positions_for_hamburger_button = [(730, 20)]
        #     sleep(1)
        #     self.driver.tap(positions_for_hamburger_button)
        # except:
        #     logging.info("pass tapping into positions")
        logging.info("click in LOGIN button")
        login_button = self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_ios)
        self.assertIsNotNone(login_button, "Login button not found")
        login_button.click()

        # TEST IT ON IOS 9.3

        # try:
        #     login_button = self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_ios)
        #     if login_button.is_displayed():
        #         self.assertIsNotNone(login_button, "Login button not found")
        #         login_button.click()
        # except NoSuchElementException:
        #     pass
        # try:
        #     login_button_by_index = self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_by_index_ios)
        #     if login_button_by_index.is_displayed():
        #         self.assertIsNotNone(login_button_by_index)
        #         login_button_by_index.click()
        # except NoSuchElementException:
        #     pass
        # try:
        #     username_field = self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios)
        #     if username_field.is_displayed():
        #         pass
        #     else:
        #         action = TouchAction(self.driver)
        #         action.tap(element=None, x=115, y=283, count=1).perform()
        # # add coordinates for iPhones
        # except NoSuchElementException:
        #     pass

    def click_settings_button(self):

        logging.info("click Settings button")
        settings_button = self.driver.find_element(*WelcomeScreen.SETTINGS_BUTTON_ios)
        self.assertIsNotNone(settings_button)
        settings_button.click()

    def type_contact_identifier(self, test_pin):

        logging.info("type contact identifier")
        contact_identifier_field = self.driver.find_element(*WelcomeScreen.SETTINGS_CONTACT_IDENTIFIER_FIELD_ios)
        self.assertIsNotNone(contact_identifier_field)
        contact_identifier_field.clear()
        contact_identifier_field.click()
        contact_identifier_field.send_keys(ContactIdentifierPIN.get_contact_identifier_pin(test_pin))

    def check_if_app_was_activated(self):

        logging.info("check if app was activated")
        alert = self.driver.find_element(*WelcomeScreen.SETTINGS_ALERT_APP_HAS_BEEN_ACTIVATED_ios)
        self.assertIsNotNone(alert, "App was not activated")

    def click_ok_button(self):

        logging.info("click ok button")
        ok_button = self.driver.find_element(*WelcomeScreen.SETTINGS_OK_BUTTON_ios)
        self.assertIsNotNone(ok_button, "OK button not found")
        ok_button.click()


class LoginPage(BasePage):
    """A class for methods to handle Login Page"""

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
            self.assertIsNotNone(alert_msg, "Alert - wrong pass msg not found")
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
            self.assertIsNotNone(alert_msg, "Alert - expired msg not found")
            self.driver.find_element(*LoginScreen.OK_BUTTON_ios).click()
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")

    def alert_suspended_account(self):

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*LoginScreen.ALERT_MSG_SUSPENDED_ios)
            logging.info("Successfully try to login into suspended account - message alert is present")
            self.assertIsNotNone(alert_msg, "Alert - suspended msg not found")
            self.driver.find_element(*LoginScreen.OK_BUTTON_ios).click()
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")


class MainPage(BasePage):
    """A class for methods to handle Main Page"""

    def dismiss_ios_notifications(self):

        logging.info("dismiss iOS notifications")
        try:
            notification_msg_on_ios = self.driver.find_element(*LoginScreen.NOTIFICATION_ABOUT_SENDING_MESSAGES_ios)
            if notification_msg_on_ios.is_displayed():
                logging.info("click 'No' for sending notifications on iOS")
                notification_msg_on_ios = self.driver.find_element(
                    *LoginScreen.NOTIFICATION_ABOUT_SENDING_MESSAGES_ios)
                self.assertIsNotNone(notification_msg_on_ios, "Notification msg on iOS not found")
                self.driver.find_element(*LoginScreen.NO_FOR_SENDING_NOTIFICATIONS_ON_ios).click()
            else:
                pass
        except NoSuchElementException:
            pass

    def logout_if_already_logged_in(self):

        sleep(5)
        logging.info("logout if already logged in")

        # BasePage.hamburger_button(self)

        try:
            logout_button_ios = self.driver.find_element(*MainMenuScreen.LOGOUT_BUTTON_ios)
            self.assertIsNotNone(logout_button_ios, "Logout button not found")
            logging.info("Your are already logged in - logging out")
            logout_button_ios.click()
            submit_button_ios = self.driver.find_element(*LoginScreen.SUBMIT_BUTTON_ios)
            self.assertIsNotNone(submit_button_ios, "Submit button not found")
            submit_button_ios.click()
            sleep(7)
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
                expected_conditions.presence_of_element_located(MainMenuScreen.EVENTS_BUTTON_ios),
                "Events button in Main Menu is not present")
            logging.info("Events button in Main Menu is present")
        except NoSuchElementException:
            logging.info("Events button in Main Menu is not present")
            self.fail("Events button in Main Menu is not present")

    def click_ACTIVATE_BUTTON_on_alert(self):

        logging.info("clicking in ACTIVATE button on alert")
        alert_activate_button = self.driver.find_element(*MainMenuScreen.ALERT_ACTIVATE_BUTTON_ios)
        self.assertIsNotNone(alert_activate_button, "ACTIVATE button on alert not found")
        alert_activate_button.click()
        sleep(2)

    def check_if_alert_WORKFLOW_ACTIVATED_is_present(self):

        logging.info("check if alert 'Workflow activated' is present and click 'Ok'")
        alert_workflow_activated = self.driver.find_element(*MainMenuScreen.ALERT_WORKFLOW_ACTIVATED_ios)
        self.assertIsNotNone(alert_workflow_activated, "alert WORKFLOW ACTIVATED is not present")
        self.driver.find_element(*LoginScreen.OK_BUTTON_ios).click()

    def click_ACTIVATE_WORKFLOW(self):

        logging.info("clicking in ACTIVATE WORKFLOW button")
        activate_workflow_button = self.driver.find_element(*MainMenuScreen.ACTIVATE_WORKFLOW_BUTTON_ios)
        self.assertIsNotNone(activate_workflow_button, "ACTIVATE WORKFLOW button not found")
        activate_workflow_button.click()

    def open_CREATE_CONTACT(self):

        logging.info("clicking in CREATE CONTACT button")
        create_contact_button = self.driver.find_element(*MainMenuScreen.CREATE_CONTACT_BUTTON_ios)
        self.assertIsNotNone(create_contact_button, "CREATE CONTACT button not found")
        create_contact_button.click()

    def open_CREATE_TASK(self):

        logging.info("clicking in CREATE TASK button")
        create_task_button = self.driver.find_element(*MainMenuScreen.CREATE_TASK_BUTTON_ios)
        self.assertIsNotNone(create_task_button, "CREATE TASK button not found")
        create_task_button.click()

    def open_CREATE_REPORT(self):

        logging.info("clicking in CREATE REPORT button")
        create_report_button = self.driver.find_element(*MainMenuScreen.CREATE_REPORT_BUTTON_ios)
        self.assertIsNotNone(create_report_button, "CREATE REPORT button not found")
        create_report_button.click()

    def open_WEBSITE_LINK(self):

        logging.info("clicking in WEBSITE LINK button")
        website_link_button = self.driver.find_element(*MainMenuScreen.WEBSITE_LINK_BUTTON_ios)
        self.assertIsNotNone(website_link_button, "WEBSITE LINK button not found")
        website_link_button.click()

    def open_INCIDENT(self):

        logging.info("clicking in INCIDENT button")
        incident_button = self.driver.find_element(*MainMenuScreen.INCIDENT_BUTTON_ios)
        self.assertIsNotNone(incident_button, "INCIDENT button not found")
        incident_button.click()

    def open_CREATE_ASSETS(self):

        logging.info("clicking in CREATE ASSETS button")
        create_assets_button = self.driver.find_element(*MainMenuScreen.CREATE_ASSETS_BUTTON_ios)
        self.assertIsNotNone(create_assets_button, "CREATE ASSETS button not found")
        create_assets_button.click()

    def open_CREATE_LOG(self):

        logging.info("clicking in CREATE LOG button")
        create_log_button = self.driver.find_element(*MainMenuScreen.CREATE_LOG_BUTTON_ios)
        self.assertIsNotNone(create_log_button, "CREATE LOG button not found")
        create_log_button.click()

    def open_RISKS(self):

        logging.info("clicking in RISKS button")
        risks_button = self.driver.find_element(*MainMenuScreen.RISKS_BUTTON_ios)
        self.assertIsNotNone(risks_button, "RISKS button not found")
        risks_button.click()

    def open_EVENTS(self):

        logging.info("clicking in Events button")
        events_button = self.driver.find_element(*MainMenuScreen.EVENTS_BUTTON_ios)
        self.assertIsNotNone(events_button, "EVENTS button not found")
        events_button.click()
        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*EventsScreen.EVENTS_HEADER_ios)
        self.assertIsNotNone(events_header)

    def open_LOGS(self):

        logging.info("clicking in LOGS button")
        logs_button = self.driver.find_element(*MainMenuScreen.LOGS_BUTTON_ios)
        self.assertIsNotNone(logs_button, "LOGS button not found")
        logs_button.click()

    def open_REPORTS(self):

        logging.info("clicking in REPORTS button")
        reports_button = self.driver.find_element(*MainMenuScreen.REPORTS_BUTTON_ios)
        self.assertIsNotNone(reports_button, "REPORTS button not found")
        reports_button.click()
        
    def open_MAP(self):

        logging.info("clicking in Map button")
        map_button = self.driver.find_element(*MainMenuScreen.MAP_BUTTON_ios)
        self.assertIsNotNone(map_button, "MAP button not found")
        map_button.click()

    def open_LOCATION(self):

        logging.info("clicking in Location button")
        location_button = self.driver.find_element(*MainMenuScreen.LOCATION_BUTTON_ios)
        self.assertIsNotNone(location_button, "Location button not found")
        location_button.click()

    def open_ASSETS(self):

        logging.info("clicking in ASSETS button")
        assets_button = self.driver.find_element(*MainMenuScreen.ASSETS_BUTTON_ios)
        self.assertIsNotNone(assets_button, "ASSETS button not found")
        assets_button.click()

    def open_MY_MESSAGES(self):
        logging.info("clicking in MY MESSAGES button")
        my_messages_button = self.driver.find_element(*MainMenuScreen.MY_MESSAGES_BUTTON_ios)
        self.assertIsNotNone(my_messages_button, "MY MESSAGES button not found")
        my_messages_button.click()

    def open_INBOX(self):
        logging.info("clicking in INBOX button")
        inbox_button = self.driver.find_element(*MainMenuScreen.INBOX_BUTTON_ios)
        self.assertIsNotNone(inbox_button, "INBOX button not found")
        inbox_button.click()

    def open_COMPOSE(self):
        logging.info("clicking in COMPOSE button")
        compose_button = self.driver.find_element(*MainMenuScreen.COMPOSE_BUTTON_ios)
        self.assertIsNotNone(compose_button, "COMPOSE button not found")
        compose_button.click()

    def open_SENT(self):
        logging.info("clicking in SENT button")
        sent_button = self.driver.find_element(*MainMenuScreen.SENT_BUTTON_ios)
        self.assertIsNotNone(sent_button, "SENT button not found")
        sent_button.click()

    def open_PHOTO(self):

        logging.info("clicking in Photo button")
        photo_button = self.driver.find_element(*MainMenuScreen.PHOTO_BUTTON_ios)
        self.assertIsNotNone(photo_button, "PHOTO button not found")
        photo_button.click()

    def open_VIDEO(self):

        logging.info("clicking in Video button")
        video_button = self.driver.find_element(*MainMenuScreen.VIDEO_BUTTON_ios)
        self.assertIsNotNone(video_button, "VIDEO button not found")
        video_button.click()

    def open_SOUND(self):

        logging.info("clicking in Sound button")
        sound_button = self.driver.find_element(*MainMenuScreen.SOUND_BUTTON_ios)
        self.assertIsNotNone(sound_button, "Sound button not found")
        sound_button.click()

    def open_TASKS(self):

        logging.info("clicking in TASKS button")
        tasks_button = self.driver.find_element(*MainMenuScreen.TASKS_BUTTON_ios)
        self.assertIsNotNone(tasks_button, "TASKS button not found")
        tasks_button.click()

    def open_DOCUMENTS(self):

        logging.info("clicking in DOCUMENTS button")
        documents_button = self.driver.find_element(*MainMenuScreen.DOCUMENTS_BUTTON_ios)
        self.assertIsNotNone(documents_button, "DOCUMENTS button not found")
        documents_button.click()

    def open_CONTACTS(self):

        logging.info("clicking in CONTACTS button")
        contacts_button = self.driver.find_element(*MainMenuScreen.CONTACTS_BUTTON_ios)
        self.assertIsNotNone(contacts_button, "CONTACTS button not found")
        contacts_button.click()

    def open_ALLOCATE(self):

        logging.info("clicking in ALLOCATE button")
        allocate_button = self.driver.find_element(*MainMenuScreen.ALLOCATE_BUTTON_ios)
        self.assertIsNotNone(allocate_button, "ALLOCATE button not found")
        allocate_button.click()

    def open_SETTINGS(self):
        logging.info("clicking in SETTINGS button")
        settings_button = self.driver.find_element(*MainMenuScreen.SETTINGS_BUTTON_ios)
        self.assertIsNotNone(settings_button, "SETTINGS button not found")
        settings_button.click()

    def open_ACTIVATE(self):
        logging.info("clicking in ACTIVATE button")
        activate_button = self.driver.find_element(*MainMenuScreen.ACTIVATE_BUTTON_ios)
        self.assertIsNotNone(activate_button, "ACTIVATE button not found")
        activate_button.click()

    def open_OFFLINE_SYNC(self):
        logging.info("clicking in OFFLINE SYNC button")
        offline_sync_button = self.driver.find_element(*MainMenuScreen.OFFLINE_SYNC_BUTTON_ios)
        self.assertIsNotNone(offline_sync_button, "OFFLINE SYNC button not found")
        offline_sync_button.click()

    def open_ABOUT(self):
        logging.info("clicking in ABOUT button")
        about_button = self.driver.find_element(*MainMenuScreen.ABOUT_BUTTON_ios)
        self.assertIsNotNone(about_button, "ABOUT button not found")
        about_button.click()


class PhotoPage(BasePage):
    """A class for methods to handle Photo Page"""

    def check_if_photo_page_was_opened(self):

        photo_page_header = self.driver.find_element(*PhotoScreen.PHOTO_PAGE_HEADER_ios)
        self.assertIsNotNone(photo_page_header, "Photo page header was not found")
        logging.info("Photo page was opened")

    def type_description(self, description):

        sleep(2)
        logging.info("type text into description field")
        description_field = self.driver.find_element(*PhotoScreen.DESCRIPTION_FIELD_ios)
        self.assertIsNotNone(description_field, "Description field not found")
        description_field.click()
        description_field.send_keys(description)

    def click_gallery_button(self):

        # add coordinates for iPhones - clicking is not working because button is invisible
        logging.info("clicking in 'Gallery' button")
        try:
            action = TouchAction(self.driver)
            action.tap(element=None, x=180, y=158, count=1).perform()
        except NoSuchElementException:
            gallery_button = self.driver.find_element(*PhotoScreen.GALLERY_BUTTON_ios)
            if gallery_button.is_displayed():
                self.assertIsNotNone(gallery_button, "Gallery button not found")
                gallery_button.click()

    def click_take_new_button(self):
        # add coordinates for iPhones
        logging.info("clicking in 'Take new' button")
        try:
            action = TouchAction(self.driver)
            action.tap(element=None, x=548, y=158, count=1).perform()
            # take_new_button = self.driver.find_element(*PhotoScreen.TAKE_NEW_BUTTON_ios)
            # if take_new_button.is_displayed():
            #     self.assertIsNotNone(take_new_button, "Take new button not found")
            #     take_new_button.click()
        except NoSuchElementException:
            self.fail("could not tap 'Take new' button")

    def click_send_button(self):

        sleep(1)
        logging.info("click 'Send' button")
        send_button = self.driver.find_element(*PhotoScreen.SEND_BUTTON_ios)
        self.assertIsNotNone(send_button, "Send button not found")
        send_button.click()
        sleep(2)
        logging.info("sending file")
        WebDriverWait(self.driver, 420).until(
            expected_conditions.presence_of_element_located(MainMenuScreen.EVENTS_BUTTON_ios),
            "Failed to send file")
        logging.info("File was sent")

    def click_reset_button(self):

        logging.info("click 'Reset' button")
        reset_button = self.driver.find_element(*PhotoScreen.RESET_BUTTON_ios)
        self.assertIsNotNone(reset_button, "Reset button not found")
        reset_button.click()


class GalleryPage(BasePage):
    """A class for methods to handle Gallery Page"""

    def choose_element_1(self):

        logging.info("choosing element 1")
        choose_element_1 = self.driver.find_element(*GalleryScreen.GALLERY_ELEMENT_1_ios)
        self.assertIsNotNone(choose_element_1, "first element in gallery not found")
        choose_element_1.click()

    def choose_videos_gallery(self):

        logging.info("choose videos gallery")
        choose_videos_gallery = self.driver.find_element(*GalleryScreen.GALLERY_VIDEOS_POPOVER_ios)
        self.assertIsNotNone(choose_videos_gallery, "videos gallery not found")
        choose_videos_gallery.click()

    def click_use_video_button(self):

        logging.info("click 'Use' button")
        use_video_button = self.driver.find_element(*GalleryScreen.USE_VIDEO_BUTTON_ios)
        self.assertIsNotNone(use_video_button, "use video button not found")
        use_video_button.click()


class VideoPage(PhotoPage):
    """A class for methods to handle Video Page"""

    def check_if_video_page_was_opened(self):

        video_page_header = self.driver.find_element(*VideoScreen.VIDEO_PAGE_HEADER_ios)
        self.assertIsNotNone(video_page_header, "Video page header was not found")
        logging.info("Video page was opened")

    def click_record_new_button(self):

        logging.info("clicking in 'Record new' button")
        # try:
        #     record_new_button = self.driver.find_element(*VideoScreen.RECORD_NEW_BUTTON_ios)
        #     if record_new_button.is_displayed():
        #         self.assertIsNotNone(record_new_button, "record new button not found")
        #         record_new_button.click()
        # except NoSuchElementException:
        #     action = TouchAction(self.driver)
        #     action.tap(element=None, x=548, y=158, count=1).perform()

        # add coordinates for iPhones
        action = TouchAction(self.driver)
        action.tap(element=None, x=563, y=182, count=1).perform()


class SoundPage(PhotoPage):
    """A class for methods to handle Sound Page"""

    def check_if_sound_page_was_opened(self):

        video_page_header = self.driver.find_element(*SoundScreen.SOUND_PAGE_HEADER_ios)
        self.assertIsNotNone(video_page_header, "Sound page header was not found")
        logging.info("Sound page was opened")

    def click_record_sound_icon(self):

        logging.info("clicking in 'Record Sound' icon")
        try:
            # add coordinates for iPhones
            action = TouchAction(self.driver)
            action.tap(element=None, x=180, y=158, count=1).perform()
        except NoSuchElementException:
            record_sound_button = self.driver.find_element(*SoundScreen.RECORD_SOUND_BUTTON_ios)
            if record_sound_button.is_displayed():
                self.assertIsNotNone(record_sound_button, "record sound button not found")
                record_sound_button.click()
        #         logging.info("2")
        # try:
        #     action = TouchAction(self.driver)
        #     action.tap(element=None, x=182, y=138, count=1).perform()
        #     logging.info("3")
        # except:
        #     action = TouchAction(self.driver)
        #     action.tap(element=None, x=182, y=141, count=1).perform()
        #     logging.info("4")


class SoundRecorder(BasePage):
    """A class for methods to handle Sound Recorder"""

    def record_sound(self):

        logging.info("click record sound")
        sound_capture = self.driver.find_element(*SoundRecorderScreen.RECORD_SOUND_ios)
        self.assertIsNotNone(sound_capture, "sound capture button not found")
        sound_capture.click()

    def click_done_button(self):

        logging.info("click click 'Done' button")
        done_button = self.driver.find_element(*SoundRecorderScreen.DONE_BUTTON_ios)
        self.assertIsNotNone(done_button, "Done button not found")
        done_button.click()


class CameraPage(BasePage):
    """A class for methods to handle Camera"""

    def take_a_photo(self):

        logging.info("taking photo")
        photo_capture = self.driver.find_element(*CameraScreen.PHOTO_CAPTURE_ios)
        self.assertIsNotNone(photo_capture, "photo capture button not found")
        photo_capture.click()

    def capture_video(self):

        logging.info("recording new video")
        record_new_video = self.driver.find_element(*CameraScreen.VIDEO_CAPTURE_ios)
        self.assertIsNotNone(record_new_video, "video capture button not found")
        record_new_video.click()

    def click_cancel(self):

        logging.info("click Cancel")
        cancel = self.driver.find_element(*CameraScreen.CANCEL_BUTTON_ios)
        self.assertIsNotNone(cancel, "Cancel button not found")
        cancel.click()

    def click_use_photo(self):

        logging.info("click Use Photo")
        use_photo = self.driver.find_element(*CameraScreen.USE_PHOTO_ios)
        self.assertIsNotNone(use_photo, "Use photo button not found")
        use_photo.click()

    def click_use_video(self):

        logging.info("click Use Video")
        use_video = self.driver.find_element(*CameraScreen.USE_VIDEO_ios)
        self.assertIsNotNone(use_video, "Use video button not found")
        use_video.click()
        sleep(2)

    def click_retake(self):

        logging.info("click Retake")
        retake_photo = self.driver.find_element(*CameraScreen.RETAKE_ios)
        self.assertIsNotNone(retake_photo, "Retake button not found")
        retake_photo.click()

    def choose_camera(self):

        logging.info("click choose camera")
        chooser_camera = self.driver.find_element(*CameraScreen.CAMERA_CHOOSER_ios)
        self.assertIsNotNone(chooser_camera, "Choose camera button not found")
        chooser_camera.click()


class LocationPage(BasePage):
    """A class for methods to handle Location Page"""

    def check_if_location_page_was_opened(self):

        logging.info("Location Page was opened")
        location_page_header = self.driver.find_element(*LocationScreen.LOCATION_PAGE_HEADER_ios)
        self.assertIsNotNone(location_page_header, "Location Page header was not found")
    
    def click_send_once_now(self):
        
        logging.info("clicking in 'Send once now' button")
        send_once_now_button = self.driver.find_element(*LocationScreen.SEND_ONCE_NOW_ios)
        self.assertIsNotNone(send_once_now_button, "Send once now button not found")
        send_once_now_button.click()

    def check_if_location_was_sent(self):

        sleep(2)
        logging.info("check if location was sent")
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
        self.assertIsNotNone(send_every_button, "Send every button not found")
        send_every_button.click()

    def choose_send_every_5_minutes_option(self):

        logging.info("choose send every '5 minutes' option")
        choose_5_minutes_option = self.driver.find_element(*LocationScreen.CHOOSE_5_MINUTES_OPTION_iPad)
        self.assertIsNotNone(choose_5_minutes_option, "5 minutes option not found")
        choose_5_minutes_option.click()

    def check_if_5_minutes_option_was_chosen(self):

        logging.info("check if send every '5 minutes'  option was chosen")
        check_if_5_minutes_option_was_chosen = self.driver.find_element(*LocationScreen.ASSERT_5_MINUTES_OPTION_ios)
        self.assertIsNotNone(check_if_5_minutes_option_was_chosen, "5 minutes option was not chosen")

    def click_for_the_next(self):

        logging.info("clicking in 'For the next' selector")
        for_the_next = self.driver.find_element(*LocationScreen.FOR_THE_NEXT_SPINNER_ios)
        self.assertIsNotNone(for_the_next, "for the next selector not found")
        for_the_next.click()

    def choose_1_hour_option(self):

        logging.info("choose '1 hour' option")
        choose_1_hour_option = self.driver.find_element(*LocationScreen.CHOOSE_1_HOUR_OPTION_iPad)
        self.assertIsNotNone(choose_1_hour_option, "1 hour option not found")
        choose_1_hour_option.click()

    def check_if_1_hour_option_was_chosen(self):

        logging.info("check if '1 hour' option was chosen")
        check_if_1hour_option_was_chosen = self.driver.find_element(*LocationScreen.ASSERT_1_HOUR_OPTION_ios)
        self.assertIsNotNone(check_if_1hour_option_was_chosen, "1 hour option was not chosen")

    def click_start_button(self):

        logging.info("click 'Start' button")
        start_button = self.driver.find_element(*LocationScreen.START_BUTTON_ios)
        self.assertIsNotNone(start_button, "start button not found")
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
    """A class for methods to handle Events Page"""

    def check_if_EVENTS_were_opened(self):

        sleep(2)
        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*EventsScreen.EVENTS_HEADER_ios)
        self.assertIsNotNone(events_header, "Events header not found")

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
        self.assertIsNotNone(set_as_primary_button, "Set as primary button not found")
        set_as_primary_button.click()
        sleep(2)

    def clear_primary_event(self):

        logging.info("clicking in 'Clear primary event' button")
        clear_primary_event_button = self.driver.find_element(*EventsScreen.CLEAR_PRIMARY_EVENT_BUTTON_ios)
        self.assertIsNotNone(clear_primary_event_button, "Clear primary event button not found")
        clear_primary_event_button.click()
        logging.info("checking notification - 'Primary event cleared'")
        notification = self.driver.find_element(*EventsScreen.NOTIFICATION_PRIMARY_EVENT_CLEARED_ios)
        self.assertIsNotNone(notification)

    def open_previously_created_event1(self):

        logging.info("open created event")
        created_event1 = self.driver.find_element(*EventsScreen.CREATED_EVENT_1_ios)
        self.assertIsNotNone(created_event1, "Created event 1 not found")
        created_event1.click()
        sleep(5)

    def open_previously_created_event2(self):

        logging.info("open previously created Event, Edit and Create mapping data")
        created_event2 = self.driver.find_element(*EventsScreen.CREATED_EVENT_2_ios)
        self.assertIsNotNone(created_event2, "Created event 2 not found")
        created_event2.click()
        sleep(5)
        
    def open_previously_created_event3(self):

        logging.info("open previously created Event, Edit and Create mapping data")
        created_event3 = self.driver.find_element(*EventsScreen.CREATED_EVENT_3_ios)
        self.assertIsNotNone(created_event3, "Created event 3 not found")
        created_event3.click()
        sleep(5)

    # only for events list, opened from chooser fields inside other event
    def click_on_previously_created_event_for_chooser_field(self):

        logging.info("click_on_previously_created_event_for_chooser_field")
        event_for_chooser_field = self.driver.find_element(*EventEditScreen.PREVIOUSLY_CREATED_EVENT_FOR_CHOOSER_ios)
        self.assertIsNotNone(event_for_chooser_field, "event_for_chooser_field not found")
        event_for_chooser_field.click()

    def click_on_previously_created_event_for_subform_chooser(self):

        logging.info("click_on_previously_created_event_for_subform_chooser")
        event_for_subform = self.driver.find_element(*EventEditScreen.PREVIOUSLY_CREATED_EVENT_FOR_SUBFORM_CHOOSER_ios)
        self.assertIsNotNone(event_for_subform, "event_for_subform not found")
        event_for_subform.click()
        sleep(1)


class EventsTypesPage(BasePage):
    """A class for methods to handle Events Types Page"""

    def choose_Incident_type_of_event(self):

        event_type_incident = self.driver.find_element(*TypesOfEventsScreen.INCIDENT_TYPE_OF_EVENT_ios)
        self.assertIsNotNone(event_type_incident, "event_type_incident not found")
        logging.info("choosing Incident type of new event")
        event_type_incident.click()

    def choose_Event_for_on_load_save_type_of_event(self):

        event_type_onload = self.driver.find_element(*TypesOfEventsScreen.EVENT_FOR_ON_LOAD_SAVE_ios)
        self.assertIsNotNone(event_type_onload, "event_type_onload not found")
        logging.info("choose type of event = event_for_on_load/save_test")
        event_type_onload.click()

    def choose_Event_for_chooser_fields_type_of_event(self):

        event_type_chooser = self.driver.find_element(*TypesOfEventsScreen.EVENT_FOR_CHOOSER_FIELDS_ios)
        self.assertIsNotNone(event_type_chooser, "event_type_chooser not found")
        logging.info("choose type of event = event for chooser fields")
        event_type_chooser.click()


class EventEditPage(Common):
    """A class for methods to handle Event Edit Page"""

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
                self.assertIsNotNone(choose_severity_lvl1, "choose_severity_lvl1 not found")
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
                self.assertIsNotNone(choose_severity_lvl2, "choose_severity_lvl2 not found")
                choose_severity_lvl2.click()
        except NoSuchElementException:
            pass
        sleep(1)
        
    def choose_severity_level_3(self):

        try:
            logging.info("choose_severity_lvl3")
            choose_severity_lvl3 = self.driver.find_element(*EventEditScreen.CHOOSE_SEVERITY_LVL3_iPad)
            if choose_severity_lvl3.is_displayed():
                self.assertIsNotNone(choose_severity_lvl3, "choose_severity_lvl3 not found")
                choose_severity_lvl3.click()
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
    """A class for methods to handle Option List inside form to create event"""

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
    """A class for methods to handle Map"""

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


class NewContactPage(Common):
    """A class for methods to handle New Contact Page"""

    def type_first_name(self, text):

        logging.info("type first name")
        first_name = self.driver.find_element(*NewContactScreen.FIRST_NAME_ios)
        self.assertIsNotNone(first_name, "First name input field was not found")
        first_name.click()
        first_name.send_keys(text)


class NewTaskPage(Common):
    """A class for methods to handle New Task Page"""

    def type_title(self, text):

        logging.info("type title")
        title = self.driver.find_element(*NewTaskScreen.TITLE_ios)
        self.assertIsNotNone(title, "Title input field was not found")
        title.click()
        title.send_keys(text)

    def click_on_assigned(self):

        logging.info("click on Assigned field")
        assigned = self.driver.find_element(*NewTaskScreen.ASSIGNED_ios)
        self.assertIsNotNone(assigned, "Assigned field was not found")
        assigned.click()

    def add_contacts(self):

        logging.info("Add Assignees")
        assignees = self.driver.find_element(*NewTaskScreen.ADD_CONTACTS_AND_GROUPS_ios)
        self.assertIsNotNone(assignees, "Assignees field was not found")
        assignees.click()

    def choose_users(self):

        logging.info("Choose Users")
        assignees = self.driver.find_element(*NewTaskScreen.CHOOSE_USERS_ios)
        self.assertIsNotNone(assignees, "Users option list was not found")
        assignees.click()

    def choose_start_date(self):

        logging.info("Choose Start Date")
        start_date = self.driver.find_element(*NewTaskScreen.START_DATE_ios)
        self.assertIsNotNone(start_date, "Start Date field was not found")
        start_date.click()

    def hide_date_picker(self):

        logging.info("hide date picker")
        hide_date_picker = self.driver.find_element(*NewTaskScreen.HIDE_DATE_PICKER_ios)
        self.assertIsNotNone(hide_date_picker, "Completed Date field was not found")
        hide_date_picker.click()


class NewReportPage(NewTaskPage):
    """A class for methods to handle New Report Page"""

    def type_title(self, text):

        NewTaskPage.type_title(self, text)

    def click_on_lodging_agency_picker(self):

        sleep(5)
        logging.info("click on 'Lodging Agency' picker")
        lodging_agency_picker = self.driver.find_element(*NewReportScreen.LODGING_AGENCY_PICKER_ios)
        self.assertIsNotNone(lodging_agency_picker, "Lodging Agency picker was not found")
        # lodging_agency_picker.click()
        action = TouchAction(self.driver)
        action.tap(element=lodging_agency_picker, count=1).perform()

    def choose_lodging_agency(self):

        logging.info("choose Lodging Agency - second position on the list")
        lodging_agency = self.driver.find_element(*NewReportScreen.LODGING_AGENCY_ios)
        self.assertIsNotNone(lodging_agency, "Lodging Agency inside picker was not found")
        lodging_agency.click()

    def click_publish_button(self):

        logging.info("click Publish button")
        publish_button = self.driver.find_element(*NewReportScreen.PUBLISH_BUTTON_ios)
        self.assertIsNotNone(publish_button, "Publish button was not found")
        publish_button.click()


# Appium can't access another app directly only tapping on specific coordinates will work
class SafariBrowserPage(BasePage):
    """A class for methods to handle Safari Browser Page"""

    def click_back_to_oca(self):

        logging.info("wait for page to load")
        sleep(10)
        logging.info("click 'Back to OCA' button")
        # add coordinates for iPhones
        positions = [(15, 7)]
        self.driver.tap(positions, duration=500)
        # sleep(2)


class EventDetailsPage(BasePage):
    """A class for methods to handle Event Details Page"""

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


class NewAssetPage(Common):
    """A class for methods to handle New Asset Page"""

    def fill_Name_input_field(self, text):

        Common.fill_Name_input_field(self, text)


class NewLogPage(NewReportPage):
    """A class for methods to handle New Log Page"""

    def click_on_lodging_agency_picker(self):

        logging.info("click on 'Lodging Agency' picker")
        lodging_agency_picker = self.driver.find_element(*NewLogScreen.LODGING_AGENCY_PICKER_ios)
        self.assertIsNotNone(lodging_agency_picker, "Lodging Agency picker was not found")
        lodging_agency_picker.click()

    def choose_lodging_agency(self):

        NewReportPage.choose_lodging_agency(self)

    def type_text_into_entry_field(self, text):

        sleep(5)
        logging.info("type text into 'Entry' field")
        entry_field = self.driver.find_element(*NewLogScreen.ENTRY_FIELD_ios)
        entry_field.click()
        entry_field.send_keys(text)
