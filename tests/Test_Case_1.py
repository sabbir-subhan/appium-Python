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
from desired_capabilities import desired_capabilities
import credentials
from locators import *
import logging
logging.basicConfig(filename='OCAapp_TC1.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.getLogger().addHandler(logging.StreamHandler())


class TC1(unittest.TestCase):
    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

        self.driver.implicitly_wait(25)  # seconds

    def tearDown(self):
        logging.info("Quitting")
        self.driver.quit()

    def test_logging_into_OCA_app(self):

        logging.info("click in LOGIN button")
        self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON).click()
        logging.info("typing username, password and OCA domain")

        logging.info("type username")
        self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME).send_keys(credentials.QA_username)

        logging.info("type password")
        self.driver.find_element(*LoginScreen.TEXTFIELD_PASSWORD).send_keys(credentials.QA_password)

        logging.info("type domain address")
        self.driver.find_element(*LoginScreen.TEXTFIELD_DOMAIN).send_keys(credentials.domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()
        sleep(3)

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
            logging.info("Successful login")
        except NoSuchElementException:
            logging.info("Failed to login")
            self.fail("Failed to login")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TC1)
    unittest.TextTestRunner(verbosity=2).run(suite)
