""" Methods for Android on Login Page """

from Modules.LoginPage.LoginPage import LoginPage
from appium.webdriver.common.touch_action import TouchAction
from credentials import Credentials
import logging
from time import sleep


class Android(LoginPage):

    def type_username(self, username):

        username_field = self.driver.find_element(*self.configuration.LoginScreen.TEXTFIELD_USERNAME)
        action = TouchAction(self.driver)
        action.long_press(el=username_field, duration=1500).perform()
        # self.driver.keyevent(67)
        self.driver.press_keycode(67)

        self.switch_context_to_webview()

        logging.info("type username")
        username_field = self.driver.find_element(*self.configuration.LoginScreen.TEXTFIELD_USERNAME)
        username_field.send_keys(Credentials.get_username(username))
        sleep(1)

        self.switch_context_to_native()

    def type_password(self, password):

        password_field = self.driver.find_element(*self.configuration.LoginScreen.TEXTFIELD_PASSWORD)
        action = TouchAction(self.driver)
        action.long_press(el=password_field, duration=1500).perform()
        # self.driver.keyevent(67)
        self.driver.press_keycode(67)

        self.switch_context_to_webview()

        password_field = self.driver.find_element(*self.configuration.LoginScreen.TEXTFIELD_PASSWORD)
        logging.info("type password")
        password_field.send_keys(Credentials.get_password(password))

        self.switch_context_to_native()

    def type_domain_address(self, domain):

        domain_field = self.driver.find_element(*self.configuration.LoginScreen.TEXTFIELD_DOMAIN)
        action = TouchAction(self.driver)
        action.long_press(el=domain_field, duration=1500).perform()
        self.driver.press_keycode(67)

        self.switch_context_to_webview()

        domain_field = self.driver.find_element(*self.configuration.LoginScreen.TEXTFIELD_DOMAIN)
        logging.info("type domain address")
        domain_field.send_keys(Credentials.get_domain(domain))

        self.switch_context_to_native()



