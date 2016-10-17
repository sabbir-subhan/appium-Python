# Test Case 2 - Logging in as a suspended account and with a wrong password

# test number 1: login with incorrect credentials
# open OCA app
# input wrong login and password
# click on Submit button
# wait until app will try to login
# check if alert about wrong credentials is present

# test number 2: login into suspended account
# open OCA app
# input correct login and password
# click on Submit button
# wait until app will try to login
# check if alert about suspended account is present

import os
import unittest
from appium import webdriver
from time import sleep
import string
import random
import logging
logging.basicConfig(filename='OCAapp_TC2.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.getLogger().addHandler(logging.StreamHandler())
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.common.exceptions import NoSuchElementException


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TC2(unittest.TestCase):
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

    def test_login_into_suspended_account(self):

        logging.info("starting first test case: test_login_into_suspended_account")

        username = "test"
        password = "test"
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

        logging.info("wait until app will try to login")
        sleep(15)

        alert_msg = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "Your account is currently inactive")]]')

        if alert_msg is None:
            print("failed to login")
        else:
            print("Successfully try to login into suspended account - message alert is present")
            self.assertIsNotNone(alert_msg)

        sleep(5)
        logging.info("click on 'OK' button")
        ok_button = self.driver.find_element_by_xpath(
            "//android.view.View[@content-desc='Ok']").click()
        sleep(3)

    def test_login_using_incorrect_credentials(self):

        logging.info("starting second test case: test_login_using_incorrect_credentials")

        domain = "https://bitnoiseqa.nogginoca.com"

        # using random generator to fill username and password fields
        def id_generator(size=7, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))

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
        textfield[0].send_keys(id_generator())

        logging.info("clear input field and type pass")
        textfield[1].clear()
        textfield[1].send_keys(id_generator())

        logging.info("clear input field and type domain address")
        textfield[2].clear()
        textfield[2].send_keys(domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()
        sleep(3)

        logging.info("click in Submit button")
        submit_button = self.driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='Submit']").click()

        logging.info("waiting until app will try to login")
        sleep(15)

        alert_msg = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "Invalid ")]]')

        if alert_msg is None:
            print("failed to login")
        else:
            print("Successfully try to login using incorrect credentials - message alert is present")
            self.assertIsNotNone(alert_msg)

        sleep(5)
        logging.info("click on 'OK' button")
        ok_button = self.driver.find_element_by_xpath(
            "//android.view.View[@content-desc='Ok']").click()
        sleep(3)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TC2)
    unittest.TextTestRunner(verbosity=2).run(suite)
