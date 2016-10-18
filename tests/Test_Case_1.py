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
from selenium.common.exceptions import NoSuchElementException
import logging
logging.basicConfig(filename='OCAapp_TC1.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.getLogger().addHandler(logging.StreamHandler())


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TC1(unittest.TestCase):
    def setUp(self):
        desired_capabilities = {}
        desired_capabilities["platformName"] = "Android"
        desired_capabilities["platformVersion"] = "4.4"
        desired_capabilities["deviceName"] = "QUANTUM_2_400"
        desired_capabilities["app"] = PATH("E:/repos/appium_OCA_mobile_app/testing-oca-mobile-app/com.noggin.oca.apk")
        desired_capabilities["appPackage"] = "com.noggin.oca"
        desired_capabilities["appActivity"] = "com.noggin.oca.OCApp"

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
        self.driver.implicitly_wait(20)  # seconds

        # credentials:

        # domain
        self.domain = "https://bitnoiseqa.nogginoca.com"

        # User - active:
        self.username = "bitnoise"
        self.password = "Bitn0!$e"

    def tearDown(self):
        logging.info("Quitting")
        self.driver.quit()

    def test_logging_into_OCA_app(self):

        logging.info("click in LOGIN button")
        login_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "LOGIN")]]').click()

        logging.info("typing username, password and OCA domain")
        logging.info("locating input fields")
        textfield = self.driver.find_elements_by_class_name("android.widget.EditText")

        logging.info("clear input field and type username")
        textfield[0].clear()
        textfield[0].send_keys(self.username)

        logging.info("clear input field and type pass")
        textfield[1].clear()
        textfield[1].send_keys(self.password)

        logging.info("clear input field and type domain address")
        textfield[2].clear()
        textfield[2].send_keys(self.domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()
        sleep(3)

        logging.info("click in Submit button")
        submit_button = self.driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='Submit']").click()

        logging.info("wait until app will login")
        sleep(10)

        logging.info("accept Terms if needed")
        try:
            logging.info("check and click on Accept button if needed")
            accept_button = self.driver.find_element_by_xpath('.//android.widget.Button'
                                                              '[@content-desc="Accept"]').click()
            logging.info("Accept button is present")
            sleep(10)
        except NoSuchElementException:
            logging.info("Terms are already accepted - Accept button is not present")

        logging.info("check if LOGOUT button is present")
        logging.info("scroll down to button LOGOUT")

        buttons = self.driver.find_elements_by_class_name('android.view.View')
        self.driver.scroll(buttons[22], buttons[1])
        logout_button = self.driver.find_element_by_xpath('.//android.view.View[@content-desc[contains(., "LOGOUT")]]')

        if logout_button is None:
            logging.info("Failed to login")
        else:
            logging.info("Successful login")
            self.assertIsNotNone(logout_button)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TC1)
    unittest.TextTestRunner(verbosity=2).run(suite)
