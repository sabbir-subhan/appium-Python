# Test Case 2 - Logging in as a suspended account and with a wrong password

# before running this Test Case prepare needed accounts on OCA website

# test1: login_into_general_user_with_incorrect_password
# test2: login_into_general_user_with_correct_credentials
# test3: login_into_admin_account_with_correct_credentials
# test4: login_using_account_expired_1_day_ago
# test5: login_using_account_that_expires_today
# test6: login_using_account_that_will_expire_in_1_day
# test7: login_into_suspended_account

import unittest
from appium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from desired_capabilities import DesiredCapabilities
import credentials
from locators import *
from generators import RandomGenerator
import logging
logging.basicConfig(filename='OCAapp_TC2.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.getLogger().addHandler(logging.StreamHandler())


class TC2(unittest.TestCase):
    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")
        desired_capabilities = DesiredCapabilities.desired_capabilities_for_android_6
        # choose desired capabilities from desired_capabilities.py
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
        self.driver.implicitly_wait(25)  # seconds

    def tearDown(self):
        logging.info("Quitting")
        self.driver.quit()

    def test1(self):

        logging.info("starting test1: login_into_general_user_with_incorrect_password")

        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON).click()

        logging.info("typing username, password and OCA domain")

        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME).send_keys(credentials.username_test_general)

        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD).send_keys(RandomGenerator.id_generator())

        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN).send_keys(credentials.domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON).click()

        # logging.info("waiting until app will try to login")
        # sleep(10)

        logging.info("accept Terms if needed")
        try:
            logging.info("check and click on Accept button if needed")
            self.driver.find_element(*LoginScreen.ACCEPT_BUTTON).click()
            logging.info("Accept button is present")
            sleep(10)
        except NoSuchElementException:
            logging.info("Terms are already accepted - Accept button is not present")

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*LoginScreen.ALERT_MSG_INVALID)
            logging.info("Successfully try to login using incorrect credentials - message alert is present")
            self.assertIsNotNone(alert_msg)
            self.driver.find_element(*LoginScreen.OK_BUTTON)
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")

    def test2(self):

        logging.info("starting test2: login_into_general_user_with_correct_credentials")

        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON).click()

        logging.info("typing username, password and OCA domain")

        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME).send_keys(credentials.username_test_general)

        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD).send_keys(credentials.password_test_general)

        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN).send_keys(credentials.domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON).click()

        logging.info("accept Terms if needed")
        try:
            self.driver.find_element(*LoginScreen.ACCEPT_BUTTON).click()
            logging.info("Accept button is present")
            sleep(10)
        except NoSuchElementException:
            logging.info("Terms are already accepted - Accept button is not present")

        logging.info("check if Notice alert is present and click Ok button")
        try:
            self.driver.find_element(*MainMenuScreen.NOTICE_ALERT).click()
            logging.info("Notice alert is present")
        except NoSuchElementException:
            logging.info("Notice alert is not present")
            pass

        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located(MainMenuScreen.EVENTS_BUTTON), "Failed to login")
            logging.info("Successful login into general user account")
        except NoSuchElementException:
            logging.info("Failed to login")
            self.fail("Failed to login")

        # logging.info("waiting until app will login")
        # sleep(10)
        #
        # logging.info("accept Terms if needed")
        # try:
        #     logging.info("check and click on Accept button if needed")
        #     self.driver.find_element(*LoginScreen.ACCEPT_BUTTON).click()
        #     logging.info("Accept button is present")
        #     sleep(10)
        # except NoSuchElementException:
        #     logging.info("Terms are already accepted - Accept button is not present")
        #
        # logging.info("check if LOGOUT button is present")
        # logging.info("scroll down to button LOGOUT")
        # buttons = self.driver.find_elements(*MainMenuScreen.BUTTONS)
        # self.driver.scroll(buttons[22], buttons[1])
        # logout_button = self.driver.find_element(*MainMenuScreen.LOGOUT_BUTTON)
        # if logout_button is None:
        #     logging.info("Failed to login")
        # else:
        #     logging.info("Successful login")
        #     self.assertIsNotNone(logout_button)

    def test3(self):

        logging.info("starting test3: login_into_admin_account_with_correct_credentials")

        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON).click()

        logging.info("typing username, password and OCA domain")

        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME).send_keys(credentials.username_test_admin)

        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD).send_keys(credentials.password_test_admin)

        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN).send_keys(credentials.domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON).click()

        logging.info("accept Terms if needed")
        try:
            self.driver.find_element(*LoginScreen.ACCEPT_BUTTON).click()
            logging.info("Accept button is present")
            sleep(10)
        except NoSuchElementException:
            logging.info("Terms are already accepted - Accept button is not present")

        logging.info("check if Notice alert is present and click Ok button")
        try:
            self.driver.find_element(*MainMenuScreen.NOTICE_ALERT).click()
            logging.info("Notice alert is present")
        except NoSuchElementException:
            logging.info("Notice alert is not present")
            pass

        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located(MainMenuScreen.EVENTS_BUTTON), "Failed to login")
            logging.info("Successful login into admin account")
        except NoSuchElementException:
            logging.info("Failed to login")
            self.fail("Failed to login")

        # logging.info("waiting until app will login")
        # sleep(10)
        #
        # logging.info("accept Terms if needed")
        # try:
        #     logging.info("check and click on Accept button if needed")
        #     self.driver.find_element(*LoginScreen.ACCEPT_BUTTON).click()
        #     logging.info("Accept button is present")
        #     sleep(10)
        # except NoSuchElementException:
        #     logging.info("Terms are already accepted - Accept button is not present")
        #
        # logging.info("check if LOGOUT button is present")
        # logging.info("scroll down to button LOGOUT")
        # buttons = self.driver.find_elements(*MainMenuScreen.BUTTONS)
        # self.driver.scroll(buttons[22], buttons[1])
        # logout_button = self.driver.find_element(*MainMenuScreen.LOGOUT_BUTTON)
        # if logout_button is None:
        #     logging.info("Failed to login")
        # else:
        #     logging.info("Successful login")
        #     self.assertIsNotNone(logout_button)

    def test4(self):

        logging.info("starting test4: login_using_account_expired_1_day_ago")

        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON).click()

        logging.info("typing username, password and OCA domain")

        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME).send_keys(credentials.username_test_expired)

        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD).send_keys(credentials.password_test_expired)

        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN).send_keys(credentials.domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON).click()

        # logging.info("waiting until app will try to login")
        # sleep(10)

        logging.info("accept Terms if needed")
        try:
            logging.info("check and click on Accept button if needed")
            self.driver.find_element(*LoginScreen.ACCEPT_BUTTON).click()
            logging.info("Accept button is present")
            sleep(10)
        except NoSuchElementException:
            logging.info("Terms are already accepted - Accept button is not present")

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*LoginScreen.ALERT_MSG_EXPIRED)
            logging.info("Successfully try to login to account that expired 1 day ago - message alert is present")
            self.assertIsNotNone(alert_msg)
            self.driver.find_element(*LoginScreen.OK_BUTTON)
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")

    def test5(self):

        logging.info("starting test5: login_using_account_that_expires_today")

        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON).click()

        logging.info("typing username, password and OCA domain")

        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME).send_keys(credentials.username_test_expire_today)

        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD).send_keys(credentials.password_test_expire_today)

        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN).send_keys(credentials.domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON).click()

        # logging.info("waiting until app will try to login")
        # sleep(10)

        logging.info("accept Terms if needed")
        try:
            logging.info("check and click on Accept button if needed")
            self.driver.find_element(*LoginScreen.ACCEPT_BUTTON).click()
            logging.info("Accept button is present")
            sleep(10)
        except NoSuchElementException:
            logging.info("Terms are already accepted - Accept button is not present")

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*LoginScreen.ALERT_MSG_EXPIRED)
            logging.info("Successfully try to login to account that expires today - message alert is present")
            self.assertIsNotNone(alert_msg)
            self.driver.find_element(*LoginScreen.OK_BUTTON)
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")

    def test6(self):

        logging.info("starting test6: login_using_account_that_will_expire_in_1_day")

        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON).click()

        logging.info("typing username, password and OCA domain")

        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME).send_keys(credentials.username_test_expire_in_1_day)

        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD).send_keys(credentials.password_test_expire_in_1_day)

        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN).send_keys(credentials.domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON).click()

        logging.info("accept Terms if needed")
        try:
            self.driver.find_element(*LoginScreen.ACCEPT_BUTTON).click()
            logging.info("Accept button is present")
            sleep(10)
        except NoSuchElementException:
            logging.info("Terms are already accepted - Accept button is not present")

        logging.info("check if Notice alert, about expiring password is present and click Ok button")
        try:
            self.driver.find_element(*MainMenuScreen.NOTICE_ALERT).click()
            logging.info("Notice alert is present")
        except NoSuchElementException:
            logging.info("Notice alert is not present")
            pass

        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located(MainMenuScreen.EVENTS_BUTTON), "Failed to login")
            logging.info("Successful login to account that will expire in 1 day")
        except NoSuchElementException:
            logging.info("Failed to login to account that will expire in 1 day")
            self.fail("Failed to login to account that will expire in 1 day")

        # logging.info("waiting until app will try to login")
        # sleep(10)
        #
        # logging.info("accept Terms if needed")
        # try:
        #     logging.info("check and click on Accept button if needed")
        #     self.driver.find_element(*LoginScreen.ACCEPT_BUTTON).click()
        #     logging.info("Accept button is present")
        #     sleep(10)
        # except NoSuchElementException:
        #     logging.info("Terms are already accepted - Accept button is not present")
        #
        # logging.info("checking alert message")
        # try:
        #     alert_msg = self.driver.find_element(*LoginScreen.ALERT_MSG_EXPIRED)
        #     logging.info("Successfully login to account that will expire in 1 day - message alert is present")
        #     self.assertIsNotNone(alert_msg)
        #     logging.info("click Ok on alert msg")
        #     self.driver.find_element(*LoginScreen.OK_BUTTON)
        #     sleep(3)
        # except NoSuchElementException:
        #     logging.info("failed - there is no alert Notice")
        #
        # logging.info("check if LOGOUT button is present")
        # logging.info("scroll down to button LOGOUT")
        # buttons = self.driver.find_elements(*MainMenuScreen.BUTTONS)
        # self.driver.scroll(buttons[22], buttons[1])
        # logout_button = self.driver.find_element(*MainMenuScreen.LOGOUT_BUTTON)
        # if logout_button is None:
        #     logging.info("Failed to login to account that will expire in 1 day")
        # else:
        #     logging.info("Successful login to account that will expire in 1 day")
        #     self.assertIsNotNone(logout_button)

    def test7(self):

        logging.info("starting test7: login_into_suspended_account")

        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON).click()

        logging.info("typing username, password and OCA domain")

        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME).send_keys(credentials.username_test_suspended)

        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD).send_keys(credentials.password_test_suspended)

        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN).send_keys(credentials.domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON).click()

        # logging.info("waiting until app will try to login")
        # sleep(10)

        logging.info("accept Terms if needed")
        try:
            logging.info("check and click on Accept button if needed")
            self.driver.find_element(*LoginScreen.ACCEPT_BUTTON).click()
            logging.info("Accept button is present")
            sleep(10)
        except NoSuchElementException:
            logging.info("Terms are already accepted - Accept button is not present")

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*LoginScreen.ALERT_MSG_SUSPENDED)
            logging.info("Successfully try to login into suspended account - message alert is present")
            self.assertIsNotNone(alert_msg)
            self.driver.find_element(*LoginScreen.OK_BUTTON)
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TC2)
    unittest.TextTestRunner(verbosity=2).run(suite)
