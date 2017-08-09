""" Methods for IOS on Login Page """

from credentials import Credentials
from Modules.LoginPage.LoginPage import LoginPage
import logging
from time import sleep


class IOS(LoginPage):

    def type_username(self, username):

        sleep(2)
        logging.info("clear username field")
        self.driver.find_element(*self.configuration.LoginScreen.TEXTFIELD_USERNAME).click()
        self.driver.find_element(*self.configuration.LoginScreen.TEXTFIELD_USERNAME).clear()
        logging.info("type username")
        self.driver.find_element(*self.configuration.LoginScreen.TEXTFIELD_USERNAME).\
            send_keys(Credentials.get_username(username))

    def type_password(self, password):

        logging.info("clear password field")
        self.driver.find_element(*self.configuration.LoginScreen.TEXTFIELD_PASSWORD).click()
        self.driver.find_element(*self.configuration.LoginScreen.TEXTFIELD_PASSWORD).clear()
        logging.info("type password")
        self.driver.find_element(*self.configuration.LoginScreen.TEXTFIELD_PASSWORD).\
            send_keys(Credentials.get_password(password))

    def type_domain_address(self, domain):

        logging.info("clear domain field")
        domain_textfield = self.driver.find_element(*self.configuration.LoginScreen.TEXTFIELD_DOMAIN)
        domain_textfield.clear()
        domain_textfield.click()
        domain_textfield.clear()
        domain_textfield.click()
        domain_textfield.clear()
        logging.info("type domain address")
        domain_textfield.click()
        domain_textfield.send_keys(Credentials.get_domain(domain))


