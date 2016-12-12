from selenium.common.exceptions import NoSuchElementException
from time import sleep
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


class AndroidDevice(BasePage):

    def hide_keyboard(self):

        logging.info("hide keyboard")
        try:
            logging.info("hide screen keyboard")
            self.driver.hide_keyboard()
            sleep(3)
        except NoSuchElementException:
            pass


class WelcomePage(BasePage):

    def click_login_button(self):

        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON).click()


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
                self.driver.find_element(*LoginScreen.ACCEPT_BUTTON).click()
                logging.info("Accepting terms and conditions")
                sleep(10)
            else:
                logging.info("Terms are already accepted - Accept button is not present")
        except NoSuchElementException:
            pass


class MainPage(BasePage):

    def logout_if_already_logged_in(self):

        try:
            logout_button = self.driver.find_element(*MainMenuScreen.LOGOUT_BUTTON)
            if logout_button.is_displayed():
                logging.info("Your are already login - logging out")
                self.driver.find_element(*MainMenuScreen.LOGOUT_BUTTON).click()
                self.driver.find_element(*LoginScreen.SUBMIT_BUTTON).click()
            else:
                pass
        except NoSuchElementException:
            pass

    def alert_expiring_password(self):

        logging.info("check if Notice alert, about expiring password, is present")
        try:
            self.driver.find_element(*LoginScreen.ALERT_MSG_WILL_EXPIRE)
            self.driver.assertIsNotNone(*LoginScreen.ALERT_MSG_WILL_EXPIRE)
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
            self.driver.fail("Failed to login")
