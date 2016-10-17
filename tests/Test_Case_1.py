# Test Case 1 - Log Into OCA mobile via direct Login
# open OCA app
# input login and password
# click on Submit button
# wait until app will login
# check if button "LOGOUT" is present

import os
import unittest
from appium import webdriver
from time import sleep
import logging
logging.basicConfig(filename='OCAapp_TC1.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.getLogger().addHandler(logging.StreamHandler())
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.common.exceptions import NoSuchElementException


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestCase1LogIn(unittest.TestCase):
    def setUp(self):
        desired_capabilities = {}
        desired_capabilities["platformName"] = "Android"
        desired_capabilities["platformVersion"] = "4.4"
        desired_capabilities["deviceName"] = "QUANTUM_2_400"
        desired_capabilities["app"] = PATH("E:/repos/appium_OCA_mobile_app/com.noggin.oca.apk")
        desired_capabilities["appPackage"] = "com.noggin.oca"
        desired_capabilities["appActivity"] = "com.noggin.oca.OCApp"

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
        sleep(10)

    def tearDown(self):
        logging.info("Quitting")
        self.driver.quit()

    def test_logging_into_OCA_app(self):

        username = "bitnoise"
        password = "Bitn0!$e"
        domain = "https://bitnoiseqa.nogginoca.com"

        sleep(5)
        logging.info("click in LOGIN button")
        login_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "LOGIN")]]').click()
        sleep(5)

        logging.info("typing username, password and OCA domain")
        logging.info("locating input fields")
        textfield = self.driver.find_elements_by_class_name("android.widget.EditText")

        logging.info("clear input field and type username")
        textfield[0].clear()
        textfield[0].send_keys(username)

        logging.info("clear input field and type pass")
        textfield[1].clear()
        textfield[1].send_keys(password)

        logging.info("clear input field and type domain address")
        textfield[2].clear()
        textfield[2].send_keys(domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()
        sleep(3)

        logging.info("click in Submit button")
        submit_button = self.driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='Submit']").click()

        logging.info("wait until app will login")
        sleep(20)

        logging.info("check if LOGOUT button is present")
        logging.info("scroll down to button LOGOUT")

        buttons = self.driver.find_elements_by_class_name('android.view.View')
        self.driver.scroll(buttons[21], buttons[0])
        sleep(2)
        logout_button = self.driver.find_element_by_xpath('.//android.view.View[@content-desc[contains(., "LOGOUT")]]')
        sleep(2)

        if logout_button is None:
            print("failed to login")
        else:
            print("Successful login")
            self.assertIsNotNone(logout_button)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase1LogIn)
    unittest.TextTestRunner(verbosity=2).run(suite)
