import logging
from Modules.BasePage import BasePage


class WelcomePage(BasePage):
    """A class for methods to handle Welcome Page"""

    def click_login_button(self):

        # sleep(10)
        self.driver.reset()  # reset app to avoid problems with locating elements
        # try:
        #     positions_for_hamburger_button = [(730, 20)]
        #     sleep(1)
        #     self.driver.tap(positions_for_hamburger_button)
        # except:
        #     logging.info("pass tapping into positions")
        logging.info("click in LOGIN button")
        login_button = self.driver.find_element(*self.configuration.WelcomeScreen.LOGIN_BUTTON)
        self.assertIsNotNone(login_button, "Login button not found")
        login_button.click()

        # TEST IT ON IOS 9.3

        # try:
        #     login_button = self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_ios)
        #     if login_button.is_displayed():
        #         self.assertIsNotNone(login_button, "Login button not found")
        #         login_button.click()
        # except NoSuchElementException:
        #     pass
        # try:
        #     login_button_by_index = self.driver.find_element(*WelcomeScreen.LOGIN_BUTTON_by_index_ios)
        #     if login_button_by_index.is_displayed():
        #         self.assertIsNotNone(login_button_by_index)
        #         login_button_by_index.click()
        # except NoSuchElementException:
        #     pass
        # try:
        #     username_field = self.driver.find_element(*LoginScreen.TEXTFIELD_USERNAME_ios)
        #     if username_field.is_displayed():
        #         pass
        #     else:
        #         action = TouchAction(self.driver)
        #         action.tap(element=None, x=115, y=283, count=1).perform()
        # # add coordinates for iPhones
        # except NoSuchElementException:
        #     pass

    def click_settings_button(self):

        logging.info("click Settings button")
        settings_button = self.driver.find_element(*WelcomeScreen.SETTINGS_BUTTON_ios)
        self.assertIsNotNone(settings_button)
        settings_button.click()

    def type_contact_identifier(self, test_pin):

        logging.info("type contact identifier")
        contact_identifier_field = self.driver.find_element(*WelcomeScreen.SETTINGS_CONTACT_IDENTIFIER_FIELD_ios)
        self.assertIsNotNone(contact_identifier_field)
        contact_identifier_field.clear()
        contact_identifier_field.click()
        contact_identifier_field.send_keys(ContactIdentifierPIN.get_contact_identifier_pin(test_pin))

    def check_if_app_was_activated(self):

        logging.info("check if app was activated")
        alert = self.driver.find_element(*WelcomeScreen.SETTINGS_ALERT_APP_HAS_BEEN_ACTIVATED_ios)
        self.assertIsNotNone(alert, "App was not activated")

    def click_ok_button(self):

        logging.info("click ok button")
        ok_button = self.driver.find_element(*WelcomeScreen.SETTINGS_OK_BUTTON_ios)
        self.assertIsNotNone(ok_button, "OK button not found")
        ok_button.click()