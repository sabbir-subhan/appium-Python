"""A class for methods to handle Welcome Page """

import logging
from Modules.BasePage.BasePage import BasePage
# from credentials import ContactIdentifierPIN
from time import sleep
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class WelcomePage(BasePage):

    def click_login_button(self):

        sleep(4)
        logging.info("click LOGIN button")

        WebDriverWait(self.driver, 25).until(
            expected_conditions.presence_of_element_located(self.configuration.WelcomeScreen.LOGIN_BUTTON),
            "Login button not found")

        self.switch_context_to_webview()

        login_button = self.driver.find_element(*self.configuration.WelcomeScreen.LOGIN_BUTTON)
        self.assertIsNotNone(login_button, "Login button not found")
        login_button.click()
        sleep(2)

        self.switch_context_to_native()

        sleep(2)

    def open_LOCATION(self):

        self.switch_context_to_webview()

        logging.info("click Location button")
        location_button = self.driver.find_element(*self.configuration.WelcomeScreen.LOCATION_BUTTON)
        self.assertIsNotNone(location_button, "Location button not found")
        location_button.click()

        self.switch_context_to_native()

    def open_MY_MESSAGES(self):

        self.switch_context_to_webview()

        logging.info("click MY MESSAGES button")
        my_messages_button = self.driver.find_element(*self.configuration.WelcomeScreen.MY_MESSAGES_BUTTON)
        self.assertIsNotNone(my_messages_button, "MY MESSAGES button not found")
        my_messages_button.click()

        self.switch_context_to_native()

    def open_PHOTO(self):

        self.switch_context_to_webview()

        logging.info("click Photo button")
        photo_button = self.driver.find_element(*self.configuration.WelcomeScreen.PHOTO_BUTTON)
        self.assertIsNotNone(photo_button, "PHOTO button not found")
        photo_button.click()

        self.switch_context_to_native()

    def open_VIDEO(self):

        self.switch_context_to_webview()

        logging.info("click Video button")
        video_button = self.driver.find_element(*self.configuration.WelcomeScreen.VIDEO_BUTTON)
        self.assertIsNotNone(video_button, "VIDEO button not found")
        video_button.click()

        self.switch_context_to_native()

    def open_SOUND(self):

        self.switch_context_to_webview()

        logging.info("click Sound button")
        sound_button = self.driver.find_element(*self.configuration.WelcomeScreen.SOUND_BUTTON)
        self.assertIsNotNone(sound_button, "Sound button not found")
        sound_button.click()

        self.switch_context_to_native()

    def open_SETTINGS(self):

        self.switch_context_to_webview()

        logging.info("click SETTINGS button")
        settings_button = self.driver.find_element(*self.configuration.WelcomeScreen.SETTINGS_BUTTON)
        self.assertIsNotNone(settings_button, "SETTINGS button not found")
        settings_button.click()

        self.switch_context_to_native()

    def open_ABOUT(self):

        self.switch_context_to_webview()

        logging.info("clicking in ABOUT button")
        about_button = self.driver.find_element(*self.configuration.WelcomeScreen.ABOUT_BUTTON)
        self.assertIsNotNone(about_button, "ABOUT button not found")
        about_button.click()

        self.switch_context_to_native()

    # def click_settings_ok_button(self):
    #
    #     logging.info("click Settings button")
    #     settings_button = self.driver.find_element(*self.configuration.WelcomeScreen.SETTINGS_OK_BUTTON)
    #     self.assertIsNotNone(settings_button)
    #     settings_button.click()

    # def type_contact_identifier(self, test_pin):
    #
    #     logging.info("type contact identifier")
    #     contact_identifier_field = self.driver.find_element(*self.configuration.WelcomeScreen.
    #                                                         SETTINGS_CONTACT_IDENTIFIER_FIELD)
    #     self.assertIsNotNone(contact_identifier_field)
    #     contact_identifier_field.clear()
    #     contact_identifier_field.click()
    #     contact_identifier_field.send_keys(ContactIdentifierPIN.get_contact_identifier_pin(test_pin))
    #
    # def check_if_app_was_activated(self):
    #
    #     logging.info("check if app was activated")
    #     alert = self.driver.find_element(*self.configuration.WelcomeScreen.SETTINGS_ALERT_APP_HAS_BEEN_ACTIVATED)
    #     self.assertIsNotNone(alert, "App was not activated")

    # def click_ok_button(self):
    #
    #     logging.info("click ok button")
    #     ok_button = self.driver.find_element(*self.configuration.WelcomeScreen.SETTINGS_OK_BUTTON)
    #     self.assertIsNotNone(ok_button, "OK button not found")
    #     ok_button.click()
