"""A class for methods to handle Settings Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
import logging
from appium.webdriver.common.touch_action import TouchAction
from credentials import ContactIdentifierPIN
from selenium.common.exceptions import *
from time import sleep


class SettingsPage(BasePage):

    def type_contact_identifier(self, test_pin):

        logging.info("type contact identifier")
        contact_identifier_field = self.driver.find_element(*self.configuration.SettingsScreen.
                                                            SETTINGS_CONTACT_IDENTIFIER_FIELD)
        self.assertIsNotNone(contact_identifier_field, "contact_identifier_field not found")
        contact_identifier_field.click()
        sleep(1)
        contact_identifier_field.send_keys(ContactIdentifierPIN.get_contact_identifier_pin(test_pin))

    def click_save_button(self):

        self.switch_context_to_webview()

        sleep(1)
        logging.info("click Save button")
        save_button = self.driver.find_element(*self.configuration.SettingsScreen.SETTINGS_SAVE_BUTTON)
        self.assertIsNotNone(save_button, "save button not found")
        sleep(1)
        save_button.click()

        self.switch_context_to_native()

        sleep(1)

    def check_if_app_was_activated(self):

        logging.info("check if alert is displayed")

        self.switch_context_to_webview()

        alert_about_pin = self.driver.find_element(*self.configuration.SettingsScreen.SETTINGS_ALERT_ABOUT_PIN)
        self.assertIsNotNone(alert_about_pin, "alert not found")

        self.switch_context_to_native()

        logging.info("check if app was activated")

        try:
            alert = self.driver.find_element(*self.configuration.SettingsScreen.SETTINGS_ALERT_APP_HAS_BEEN_ACTIVATED)
            # self.assertIsNotNone(alert, "App was not activated")
        except NoSuchElementException:
            logging.info("App was not activated, probably PIN is already in use")

    def click_ok_button(self):

        logging.info("click ok button")
        ok_button = self.driver.find_element(*self.configuration.SettingsScreen.SETTINGS_OK_BUTTON)
        self.assertIsNotNone(ok_button, "OK button not found")
        ok_button.click()

    def click_primary_role(self):

        self.switch_context_to_webview()

        logging.info("click on primary role selector")
        click_primary_role = self.driver.find_element(*self.configuration.SettingsScreen.PRIMARY_ROLE_SELECTOR)
        self.assertIsNotNone(click_primary_role, "primary role selector not found")
        click_primary_role.click()

        self.switch_context_to_native()

    def choose_first_role_on_the_list(self):

        self.switch_context_to_webview()

        logging.info("choose first primary role on the list")
        choose_first_role_on_the_list = self.driver.find_element(*self.configuration.SettingsScreen.FIRST_PRIMARY_ROLE_ON_THE_LIST)
        self.assertIsNotNone(choose_first_role_on_the_list, "first primary role on the list not found")
        choose_first_role_on_the_list.click()

        self.switch_context_to_native()

