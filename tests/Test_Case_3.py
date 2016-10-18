# Test Case 3 - Managing events

import os
import unittest
from appium import webdriver
from time import sleep
import logging
from selenium.common.exceptions import NoSuchElementException
logging.basicConfig(filename='OCAapp_TC3.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.getLogger().addHandler(logging.StreamHandler())
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TC3(unittest.TestCase):
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
        sleep(10)

    def tearDown(self):
        logging.info("Quitting")
        self.driver.quit()

    def test_create_Event(self):

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
        self.driver.scroll(buttons[22], buttons[1])
        sleep(2)
        logout_button = self.driver.find_element_by_xpath('.//android.view.View[@content-desc[contains(., "LOGOUT")]]')
        sleep(2)
        if logout_button is None:
            print("failed to login")
        else:
            print("Successfully login")
            self.assertIsNotNone(logout_button)

        sleep(4)
        logging.info("scroll up to button EVENTS")
        buttonsup = self.driver.find_elements_by_class_name('android.view.View')
        self.driver.scroll(buttonsup[1], buttonsup[22])
        sleep(2)

        logging.info("clicking on Events button")
        events_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "EVENTS")]]').click()
        sleep(5)

        logging.info("check if Events were opened")
        events_header = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc="Events"]')
        self.assertIsNotNone(events_header)

        logging.info("clicking on 'More' button")
        more_button = self.driver.find_element_by_xpath(
            './/android.widget.Spinner[@content-desc[contains(., "More")]]').click()
        sleep(3)

        logging.info("here some wait is needed before clicking in button")
        sleep(5)

        logging.info("clicking on New event button")
        new_event_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "New event")]]').click()
        sleep(2)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TC3)
    unittest.TextTestRunner(verbosity=2).run(suite)
