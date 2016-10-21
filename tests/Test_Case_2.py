# Test Case 2 - Logging in as a suspended account and with a wrong password

# test1: login_into_general_user_with_incorrect_password
# test2: login_into_general_user_with_correct_credentials
# test3: login_into_admin_account_with_correct_credentials
# test4: login_using_account_expired_1_day_ago
# test5: login_using_account_that_expires_today
# test6: login_using_account_that_will_expire_in_1_day
# test7: login_into_suspended_account

import os
import unittest
from appium import webdriver
from time import sleep
import string
import random
from selenium.common.exceptions import NoSuchElementException
import logging
logging.basicConfig(filename='OCAapp_TC2.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.getLogger().addHandler(logging.StreamHandler())


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
        self.driver = webdriver.Remote("http://localhost:4727/wd/hub", desired_capabilities)
        self.driver.implicitly_wait(20)  # seconds

        # credentials:

        # domain
        self.domain = "https://bitnoiseqa.nogginoca.com"

        # General user - active:
        self.username_test_general = "test_general"
        self.password_test_general = "test_general"

        # Admin - test_admin - active:
        self.username_test_admin = "test_admin"
        self.password_test_admin = "test_admin"

        # General user - test_expired_1_day_ago
        self.username_test_expired = "test_expired"
        self.password_test_expired = "test_expired"

        # General user - test_expire_today
        self.username_test_expire_today = "test_expire_today"
        self.password_test_expire_today = "test_expire_today"

        # General user - test_expire_in_1_day
        self.username_test_expire_in_1_day = "test_expire_in_1_day"
        self.password_test_expire_in_1_day = "test_expire_in_1_day"

        # General user - test - suspended:
        self.username_test_suspended = "test_suspended"
        self.password_test_suspended = "test_suspended"

    def tearDown(self):
        logging.info("Quitting")
        self.driver.quit()

    # random generator to fill password field
    def id_generator(self, size=7, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def test1(self):

        logging.info("starting test1: login_into_general_user_with_incorrect_password")

        logging.info("click in LOGIN button")
        login_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "LOGIN")]]').click()

        logging.info("typing username, password and OCA domain")
        logging.info("locating input fields")
        textfield = self.driver.find_elements_by_class_name("android.widget.EditText")

        logging.info("type username")
        textfield[0].send_keys(self.username_test_general)

        logging.info("type pass")
        textfield[1].send_keys(self.id_generator())

        logging.info("type domain address")
        textfield[2].send_keys(self.domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()

        logging.info("click in Submit button")
        submit_button = self.driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='Submit']").click()

        logging.info("waiting until app will try to login")
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

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element_by_xpath(
                './/android.view.View[@content-desc[contains(., "Invalid")]]')
            logging.info("Successfully try to login using incorrect credentials - message alert is present")
            self.assertIsNotNone(alert_msg)
            logging.info("click Ok on alert msg")
            click_ok = self.driver.find_element_by_xpath(
                './/android.view.View[@content-desc="Ok"]').click()
            sleep(3)
        except NoSuchElementException:
            logging.info("failed - there is no alert message")

    def test2(self):

        logging.info("starting test2: login_into_general_user_with_correct_credentials")

        logging.info("click in LOGIN button")
        login_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "LOGIN")]]').click()

        logging.info("typing username, password and OCA domain")
        logging.info("locating input fields")
        textfield = self.driver.find_elements_by_class_name("android.widget.EditText")

        logging.info("type username")
        textfield[0].clear()
        textfield[0].send_keys(self.username_test_general)

        logging.info("type pass")
        textfield[1].clear()
        textfield[1].send_keys(self.username_test_general)

        logging.info("type domain address")
        textfield[2].clear()
        textfield[2].send_keys(self.domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()

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
        self.driver.scroll(buttons[21], buttons[1])
        logout_button = self.driver.find_element_by_xpath('.//android.view.View[@content-desc[contains(., "LOGOUT")]]')

        if logout_button is None:
            logging.info("failed to login")
        else:
            logging.info("Successful login")
            self.assertIsNotNone(logout_button)

    def test3(self):

        logging.info("starting test3: login_into_admin_account_with_correct_credentials")

        logging.info("click in LOGIN button")
        login_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "LOGIN")]]').click()

        logging.info("typing username, password and OCA domain")
        logging.info("locating input fields")
        textfield = self.driver.find_elements_by_class_name("android.widget.EditText")

        logging.info("type username")
        textfield[0].send_keys(self.username_test_admin)

        logging.info("type pass")
        textfield[1].send_keys(self.password_test_admin)

        logging.info("type domain address")
        textfield[2].send_keys(self.domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()

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
        self.driver.scroll(buttons[21], buttons[1])
        logout_button = self.driver.find_element_by_xpath('.//android.view.View[@content-desc[contains(., "LOGOUT")]]')

        if logout_button is None:
            logging.info("failed to login")
        else:
            logging.info("Successful login")
            self.assertIsNotNone(logout_button)

    def test4(self):

        logging.info("starting test4: login_using_account_expired_1_day_ago")

        logging.info("click in LOGIN button")
        login_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "LOGIN")]]').click()

        logging.info("typing username, password and OCA domain")
        logging.info("locating input fields")
        textfield = self.driver.find_elements_by_class_name("android.widget.EditText")

        logging.info("type username")
        textfield[0].send_keys(self.username_test_expired)

        logging.info("type pass")
        textfield[1].send_keys(self.password_test_expired)

        logging.info("type domain address")
        textfield[2].send_keys(self.domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()

        logging.info("click in Submit button")
        submit_button = self.driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='Submit']").click()

        logging.info("waiting until app will try to login")
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

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element_by_xpath(
                './/android.view.View[@content-desc[contains(., "Your temporary account has been expired")]]')
            logging.info("Successfully try to login to account that expired 1 day ago - message alert is present")
            self.assertIsNotNone(alert_msg)
            logging.info("click Ok on alert msg")
            click_ok = self.driver.find_element_by_xpath(
                './/android.view.View[@content-desc="Ok"]').click()
            sleep(3)
        except NoSuchElementException:
            logging.info("failed - there is no alert message")

    def test5(self):

        logging.info("starting test5: login_using_account_that_expires_today")

        logging.info("click in LOGIN button")
        login_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "LOGIN")]]').click()

        logging.info("typing username, password and OCA domain")
        logging.info("locating input fields")
        textfield = self.driver.find_elements_by_class_name("android.widget.EditText")

        logging.info("type username")
        textfield[0].send_keys(self.username_test_expire_today)

        logging.info("type pass")
        textfield[1].send_keys(self.password_test_expire_today)

        logging.info("type domain address")
        textfield[2].send_keys(self.domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()

        logging.info("click in Submit button")
        submit_button = self.driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='Submit']").click()

        logging.info("waiting until app will try to login")
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

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element_by_xpath(
                './/android.view.View[@content-desc[contains(., "Your temporary account has been expired")]]')
            logging.info("Successfully try to login to account that expires today - message alert is present")
            self.assertIsNotNone(alert_msg)
            logging.info("click Ok on alert msg")
            click_ok = self.driver.find_element_by_xpath(
                './/android.view.View[@content-desc="Ok"]').click()
            sleep(3)
        except NoSuchElementException:
            logging.info("failed - there is no alert message")

    def test6(self):

        logging.info("starting test6: login_using_account_that_will_expire_in_1_day")

        logging.info("click in LOGIN button")
        login_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "LOGIN")]]').click()

        logging.info("typing username, password and OCA domain")
        logging.info("locating input fields")
        textfield = self.driver.find_elements_by_class_name("android.widget.EditText")

        logging.info("type username")
        textfield[0].send_keys(self.username_test_expire_in_1_day)

        logging.info("type pass")
        textfield[1].send_keys(self.password_test_expire_in_1_day)

        logging.info("type domain address")
        textfield[2].send_keys(self.domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()

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

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element_by_xpath(
                './/android.view.View[@content-desc[contains(., "The password '
                'for the current user is about to expire")]]')
            logging.info("Successfully try to login to account that expires today - message alert is present")
            self.assertIsNotNone(alert_msg)
            logging.info("click Ok on alert Notice")
            click_ok = self.driver.find_element_by_xpath(
                './/android.view.View[@content-desc="Ok"]').click()
            sleep(3)
        except NoSuchElementException:
            logging.info("failed - there is no alert Notice")

        logging.info("check if LOGOUT button is present")
        logging.info("scroll down to button LOGOUT")

        buttons = self.driver.find_elements_by_class_name('android.view.View')
        self.driver.scroll(buttons[21], buttons[1])
        logout_button = self.driver.find_element_by_xpath('.//android.view.View[@content-desc[contains(., "LOGOUT")]]')

        if logout_button is None:
            logging.info("failed to login to login to account that will expire in 1 day")
        else:
            logging.info("Successful login to account that will expire in 1 day")
            self.assertIsNotNone(logout_button)

    def test7(self):

        logging.info("starting test7: login_into_suspended_account")

        logging.info("click in LOGIN button")
        login_button = self.driver.find_element_by_xpath(
            './/android.view.View[@content-desc[contains(., "LOGIN")]]').click()

        logging.info("typing username, password and OCA domain")
        logging.info("locating input fields")
        textfield = self.driver.find_elements_by_class_name("android.widget.EditText")

        logging.info("type username")
        textfield[0].send_keys(self.username_test_suspended)

        logging.info("type pass")
        textfield[1].send_keys(self.password_test_suspended)

        logging.info("type domain address")
        textfield[2].send_keys(self.domain)

        logging.info("hide screen keyboard")
        self.driver.hide_keyboard()

        logging.info("click in Submit button")
        submit_button = self.driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='Submit']").click()

        logging.info("wait until app will try to login")
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

        logging.info("checking alert message")
        try:
            alert_msg = self.driver.find_element_by_xpath(
                './/android.view.View[@content-desc[contains(., "Your account is currently inactive")]]')
            logging.info("Successfully try to login into suspended account - message alert is present")
            self.assertIsNotNone(alert_msg)
            logging.info("click Ok on alert msg")
            click_ok = self.driver.find_element_by_xpath(
                './/android.view.View[@content-desc="Ok"]').click()
            sleep(3)
        except NoSuchElementException:
            logging.info("failed - there is no alert msg")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TC2)
    unittest.TextTestRunner(verbosity=2).run(suite)
