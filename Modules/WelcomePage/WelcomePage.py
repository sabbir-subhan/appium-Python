"""A class for methods to handle Welcome Page """

import logging
from Modules.BasePage.BasePage import BasePage
from credentials import ContactIdentifierPIN


class WelcomePage(BasePage):

    def click_login_button(self):

        pass

    def click_settings_button(self):

        logging.info("click Settings button")
        settings_button = self.driver.find_element(*self.configuration.WelcomeScreen.SETTINGS_OK_BUTTON)
        self.assertIsNotNone(settings_button)
        settings_button.click()

    def type_contact_identifier(self, test_pin):

        logging.info("type contact identifier")
        contact_identifier_field = self.driver.find_element(*self.configuration.WelcomeScreen.
                                                            SETTINGS_CONTACT_IDENTIFIER_FIELD)
        self.assertIsNotNone(contact_identifier_field)
        contact_identifier_field.clear()
        contact_identifier_field.click()
        contact_identifier_field.send_keys(ContactIdentifierPIN.get_contact_identifier_pin(test_pin))

    def check_if_app_was_activated(self):

        logging.info("check if app was activated")
        alert = self.driver.find_element(*self.configuration.WelcomeScreen.SETTINGS_ALERT_APP_HAS_BEEN_ACTIVATED)
        self.assertIsNotNone(alert, "App was not activated")

    def click_ok_button(self):

        logging.info("click ok button")
        ok_button = self.driver.find_element(*self.configuration.WelcomeScreen.SETTINGS_OK_BUTTON)
        self.assertIsNotNone(ok_button, "OK button not found")
        ok_button.click()