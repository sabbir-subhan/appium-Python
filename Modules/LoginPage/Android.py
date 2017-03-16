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
        self.driver.keyevent(67)
        logging.info("type username")
        username_field.send_keys(Credentials.get_username(username))
        sleep(1)

    def type_password(self, password):

        password_field = self.driver.find_element(*self.configuration.LoginScreen.TEXTFIELD_PASSWORD)
        action = TouchAction(self.driver)
        action.long_press(el=password_field, duration=1500).perform()
        self.driver.keyevent(67)
        logging.info("type password")
        password_field.send_keys(Credentials.get_password(password))

    def type_domain_address(self, domain):

        domain_field = self.driver.find_element(*self.configuration.LoginScreen.TEXTFIELD_DOMAIN)
        action = TouchAction(self.driver)
        action.long_press(el=domain_field, duration=1500).perform()
        self.driver.keyevent(67)
        sleep(1)
        logging.info("type domain address")
        domain_field.send_keys(Credentials.get_domain(domain))

