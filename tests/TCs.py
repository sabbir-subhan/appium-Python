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
from page_ios import *


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

    def test_login(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.type_username()
        login_page.type_password()
        login_page.type_domain_address()
        hiding_keyboard = iOSdevice(self.driver)
        hiding_keyboard.hide_keyboard()
        login_page.click_submit_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TC1ios)
    unittest.TextTestRunner(verbosity=2).run(suite)
