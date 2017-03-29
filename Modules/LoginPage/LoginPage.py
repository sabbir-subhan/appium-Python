"""A class for methods to handle Login Page """

from time import sleep
import logging
from selenium.common.exceptions import *
from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass


class LoginPage(BasePage):

    def click_submit_button(self):

        self.switch_context_to_webview()

        logging.info("click in Submit button")
        self.driver.find_element(*self.configuration.LoginScreen.SUBMIT_BUTTON).click()
        sleep(2)

        # common_page = LoadClass.load_page('CommonPage')
        # common_page.setDriver(self.driver)
        # common_page.wait_for_app_loading()

        self.switch_context_to_native()

    def accept_terms(self):

        self.switch_context_to_webview()

        try:
            accept_terms_button = self.driver.find_element(*self.configuration.LoginScreen.ACCEPT_BUTTON)
            if accept_terms_button.is_displayed():
                self.assertIsNotNone(accept_terms_button, "accept button not found")
                logging.info("Accepting terms and conditions")
                accept_terms_button.click()
                sleep(5)
            else:
                pass
        except NoSuchElementException:
            logging.info("Terms are already accepted - Accept button is not present")

        self.switch_context_to_native()

    def alert_wrong_password(self):

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*self.configuration.LoginScreen.ALERT_MSG_INVALID)
            self.assertIsNotNone(alert_msg, "Alert - wrong pass msg not found")
            self.driver.find_element(*self.configuration.LoginScreen.OK_BUTTON).click()
            logging.info("Successfully try to login using incorrect credentials - message alert is present")
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")

    def alert_expired_password(self):

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*self.configuration.LoginScreen.ALERT_MSG_EXPIRED)
            logging.info("Successfully try to login to account that expired 1 day ago - message alert is present")
            self.assertIsNotNone(alert_msg, "Alert - expired msg not found")
            self.driver.find_element(*self.configuration.LoginScreen.OK_BUTTON).click()
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")

    def alert_suspended_account(self):

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*self.configuration.LoginScreen.ALERT_MSG_SUSPENDED)
            logging.info("Successfully try to login into suspended account - message alert is present")
            self.assertIsNotNone(alert_msg, "Alert - suspended msg not found")
            self.driver.find_element(*self.configuration.LoginScreen.OK_BUTTON).click()
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")
