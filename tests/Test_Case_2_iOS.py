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
logging.basicConfig(filename='/Users/lukasl/repos/appium-poc/OCAapp_TC2.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.getLogger().addHandler(logging.StreamHandler())


class TC2ios(unittest.TestCase):
    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")
        desired_capabilities = DesiredCapabilities.desired_capabilities_for_iOS_iPad

        # choose desired capabilities from desired_capabilities.py
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
        self.driver.implicitly_wait(25)  # seconds

    def tearDown(self):
        logging.info("Quitting")
        self.driver.quit()

    def test1(self):

        sleep(10)

        # click "No" for sending notification massages - device stores info about it
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

        sleep(5)
        logging.info("starting test1: login_into_general_user_with_incorrect_password")

        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_ios).click()

        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).clear()
        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).send_keys(credentials.username_test_general)

        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).clear()
        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).send_keys(RandomGenerator.id_generator())

        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).clear()
        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).send_keys(credentials.domain)
        logging.info("hide keyboard")
        try:
            done_button_ios = self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD)
            if done_button_ios.is_displayed():
                self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD).click()
        except NoSuchElementException:
            self.driver.hide_keyboard(key_name="Hide keyboard")

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON_ios).click()

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*LoginScreen.ALERT_MSG_INVALID_ios)
            self.assertIsNotNone(alert_msg)
            self.driver.find_element(*LoginScreen.OK_BUTTON_ios).click()
            logging.info("Successfully try to login using incorrect credentials - message alert is present")
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")

    def test2(self):

        sleep(3)

        # click "No" for sending notification massages - device stores info about it
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

        sleep(2)
        logging.info("starting test2: login_into_general_user_with_correct_credentials")

        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_ios).click()

        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).clear()
        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).send_keys(credentials.username_test_general)

        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).clear()
        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).send_keys(credentials.password_test_general)

        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).clear()
        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).send_keys(credentials.domain)
        logging.info("hide keyboard")
        try:
            done_button_ios = self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD)
            if done_button_ios.is_displayed():
                self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD).click()
        except NoSuchElementException:
            self.driver.hide_keyboard(key_name="Hide keyboard")

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON_ios).click()

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

        logging.info("check if Notice alert, about expiring password, is present")
        try:
            self.driver.find_element(*LoginScreen.ALERT_MSG_WILL_EXPIRE_ios)
            self.assertIsNotNone(*LoginScreen.ALERT_MSG_WILL_EXPIRE_ios)
            logging.info("Notice alert is present")
            self.driver.find_element(*LoginScreen.OK_BUTTON_ios).click()
        except NoSuchElementException:
            logging.info("Notice alert is not present")
            pass

        # click "No" for sending notification massages - device stores info about it
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

        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located(MainMenuScreen.EVENTS_BUTTON_ios), "Failed to login")
            logging.info("Successful login into general user account")
        except NoSuchElementException:
            logging.info("Failed to login")
            self.fail("Failed to login")

    def test3(self):

        sleep(10)
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

        sleep(5)
        logging.info("starting test3: login_into_admin_account_with_correct_credentials")

        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_ios).click()

        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).clear()
        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).send_keys(credentials.username_test_admin)

        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).clear()
        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).send_keys(credentials.password_test_admin)

        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).clear()
        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).send_keys(credentials.domain)
        logging.info("hide keyboard")
        try:
            done_button_ios = self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD)
            if done_button_ios.is_displayed():
                self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD).click()
        except NoSuchElementException:
            self.driver.hide_keyboard(key_name="Hide keyboard")

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON_ios).click()

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

        logging.info("check if Notice alert, about expiring password, is present")
        try:
            self.driver.find_element(*LoginScreen.ALERT_MSG_WILL_EXPIRE_ios)
            self.assertIsNotNone(*LoginScreen.ALERT_MSG_WILL_EXPIRE_ios)
            logging.info("Notice alert is present")
            self.driver.find_element(*LoginScreen.OK_BUTTON_ios).click()
        except NoSuchElementException:
            logging.info("Notice alert is not present")
            pass

        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located(MainMenuScreen.EVENTS_BUTTON_ios), "Failed to login")
            logging.info("Successful login into admin account")
        except NoSuchElementException:
            logging.info("Failed to login")
            self.fail("Failed to login")

    def test4(self):

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

        sleep(5)
        logging.info("starting test4: login_using_account_expired_1_day_ago")

        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_ios).click()

        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).clear()
        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).send_keys(credentials.username_test_expired)

        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).clear()
        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).send_keys(credentials.password_test_expired)

        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).clear()
        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).send_keys(credentials.domain)
        logging.info("hide keyboard")
        try:
            done_button_ios = self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD)
            if done_button_ios.is_displayed():
                self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD).click()
        except NoSuchElementException:
            self.driver.hide_keyboard(key_name="Hide keyboard")

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON_ios).click()

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

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*LoginScreen.ALERT_MSG_EXPIRED_ios)
            logging.info("Successfully try to login to account that expired 1 day ago - message alert is present")
            self.assertIsNotNone(alert_msg)
            self.driver.find_element(*LoginScreen.OK_BUTTON_ios).click()
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")

    def test5(self):

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

        sleep(2)
        logging.info("starting test5: login_using_account_that_expires_today")

        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_ios).click()

        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).clear()
        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).send_keys(credentials.username_test_expire_today)

        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).clear()
        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).send_keys(credentials.password_test_expire_today)

        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).clear()
        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).send_keys(credentials.domain)
        logging.info("hide keyboard")
        try:
            done_button_ios = self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD)
            if done_button_ios.is_displayed():
                self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD).click()
        except NoSuchElementException:
            self.driver.hide_keyboard(key_name="Hide keyboard")

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON_ios).click()

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

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*LoginScreen.ALERT_MSG_EXPIRED_ios)
            logging.info("Successfully try to login to account that expires today - message alert is present")
            self.assertIsNotNone(alert_msg)
            self.driver.find_element(*LoginScreen.OK_BUTTON_ios).click()
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")

    def test6(self):

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

        sleep(2)
        logging.info("starting test6: login_using_account_that_will_expire_in_1_day")

        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_ios).click()

        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).clear()
        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).send_keys(
            credentials.username_test_expire_in_1_day)

        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).clear()
        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).send_keys(
            credentials.password_test_expire_in_1_day)

        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).clear()
        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).send_keys(credentials.domain)
        logging.info("hide keyboard")
        try:
            done_button_ios = self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD)
            if done_button_ios.is_displayed():
                self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD).click()
        except NoSuchElementException:
            self.driver.hide_keyboard(key_name="Hide keyboard")

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON_ios).click()

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

        logging.info("check if Notice alert, about expiring password, is present and click Ok button")
        try:
            self.driver.find_element(*LoginScreen.ALERT_MSG_WILL_EXPIRE_ios)
            self.assertIsNotNone(*LoginScreen.ALERT_MSG_WILL_EXPIRE_ios)
            logging.info("Notice alert is present")
            self.driver.find_element(*LoginScreen.OK_BUTTON_ios).click()
        except NoSuchElementException:
            logging.info("Notice alert is not present")
            self.fail("Notice alert is not present")
            pass

        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located(MainMenuScreen.EVENTS_BUTTON_ios), "Failed to login")
            logging.info("Successful login to account that will expire in 1 day")
        except NoSuchElementException:
            logging.info("Failed to login to account that will expire in 1 day")
            self.fail("Failed to login to account that will expire in 1 day")

    def test7(self):

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

        sleep(5)
        logging.info("starting test7: login_into_suspended_account")

        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_ios).click()

        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).clear()
        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).send_keys(credentials.username_test_suspended)

        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).clear()
        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).send_keys(credentials.password_test_suspended)

        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).clear()
        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).send_keys(credentials.domain)
        logging.info("hide keyboard")
        try:
            done_button_ios = self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD)
            if done_button_ios.is_displayed():
                self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD).click()
        except NoSuchElementException:
            self.driver.hide_keyboard(key_name="Hide keyboard")

        logging.info("click in Submit button")
        self.driver.find_element(*LoginScreen.SUBMIT_BUTTON_ios).click()

        # suspended account will not see Accept Terms screen

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element(*LoginScreen.ALERT_MSG_SUSPENDED_ios)
            logging.info("Successfully try to login into suspended account - message alert is present")
            self.assertIsNotNone(alert_msg)
            self.driver.find_element(*LoginScreen.OK_BUTTON_ios).click()
        except NoSuchElementException:
            logging.info("failed - there is no alert message")
            self.fail("failed - there is no alert message")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TC2ios)
    unittest.TextTestRunner(verbosity=2).run(suite)
