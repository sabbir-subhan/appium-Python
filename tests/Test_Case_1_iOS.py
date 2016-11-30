# Test Case 1 - Log Into OCA mobile via direct Login
# open OCA app
# input login and password
# click on Submit button
# check if button "EVENTS" is present


import unittest
from appium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from desired_capabilities import DesiredCapabilities
import credentials
from locators import *
import logging
logging.basicConfig(filename='OCAapp_TC1.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.getLogger().addHandler(logging.StreamHandler())


class TC1ios(unittest.TestCase):
    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")

        # choose desired capabilities from desired_capabilities.py
        desired_capabilities = DesiredCapabilities.desired_capabilities_for_iOS_iPad

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

        self.driver.implicitly_wait(25)  # seconds

    def tearDown(self):
        logging.info("Quitting")
        self.driver.quit()

    def test_logging_into_OCA_app(self):

        sleep(2)

        def notification():
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

        sleep(2)
        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_ios).click()

        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).clear()
        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios).send_keys(credentials.QA_username)

        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).clear()
        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD_ios).send_keys(credentials.QA_password)

        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).click()
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).clear()
        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN_ios).send_keys(credentials.domain)

        try:
            done_button_ios = self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD)
            if done_button_ios.is_displayed():
                logging.info("hide screen keyboard")
                self.driver.find_element(*iOSkeyboard.BUTTON_DONE_TO_HIDE_KEYBOARD).click()
            else:
                pass
        except NoSuchElementException:
            pass

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

        # click "No" for sending notification massages - device stores info about it
        notification()

        sleep(2)

        # THERE IS PROBLEM WITH DISPLAYING ALERT ON IOS - it's visible only for few seconds
        # logging.info("check if Notice alert, about expiring password is present and click Ok button")
        # try:
        #     self.driver.find_element(*LoginScreen.ALERT_MSG_WILL_EXPIRE_ios)
        #     logging.info("Notice alert is present")
        #     self.driver.find_element(*LoginScreen.NOTICE_ALERT_OK_BUTTON_ios).click()
        # except NoSuchElementException:
        #     logging.info("Notice alert is not present")
        #     pass

        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located(MainMenuScreen.EVENTS_BUTTON_ios), "Failed to login")
            logging.info("Successful login")
        except NoSuchElementException:
            logging.info("Failed to login")
            self.fail("Failed to login")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TC1ios)
    unittest.TextTestRunner(verbosity=2).run(suite)
