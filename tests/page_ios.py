from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from credentials import Credentials
import logging
logging.basicConfig(filename='/Users/lukasl/repos/appium-poc/TCs.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.getLogger().addHandler(logging.StreamHandler())


class BasePage(object):
    """
    :type driver: appium.webdriver.Remote|unittest.TestCase

    """

    def __init__(self, driver):

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


class WelcomePage(BasePage):

    def click_login_button(self):

        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_ios).click()


class LoginPage(BasePage):

    def type_username(self):

        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).clear()
        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).send_keys(Credentials.QA_username)

    def type_password(self):

        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).clear()
        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).send_keys(Credentials.QA_password)

    def type_domain_address(self):

        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).clear()
        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).send_keys(Credentials.domain)

    def click_submit_button(self):

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON_ios).click()


class MainPage(BasePage):

    def dismiss_ios_notifications(self):
        try:
            notification_msg_on_ios = self.driver.find_element(*LoginScreen.NOTIFICATION_ABOUT_SENDING_MESSAGES_ios)
            if notification_msg_on_ios.is_displayed():
                logging.info("click 'No' for sending notifications on iOS")
                notification_msg_on_ios = self.driver.find_element(
                    *LoginScreen.NOTIFICATION_ABOUT_SENDING_MESSAGES_ios)
                self.driver.assertIsNotNone(notification_msg_on_ios)
                self.driver.find_element(*LoginScreen.NO_FOR_SENDING_NOTIFICATIONS_ON_ios).click()
            else:
                pass
        except NoSuchElementException:
            pass
