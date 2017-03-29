"""A class for methods to handle Risks Page """

from Modules.BasePage.BasePage import BasePage
import logging


class RisksPage(BasePage):

    def create_risk_register(self):

        self.switch_context_to_webview()

        logging.info("create risk register")
        create_risk_register_button = self.driver.find_element(*self.configuration.RisksScreen.CREATE_RISK_REGISTER)
        self.assertIsNotNone(create_risk_register_button, "Create Risk Register button not found")
        create_risk_register_button.click()

    def type_name_for_new_risk_register(self):

        self.switch_context_to_webview()

        logging.info("type Name for new risk register")
        name = self.driver.find_element(*self.configuration.RisksScreen.NAME_FOR_NEW_RISK_REGISTER)
        self.assertIsNotNone(name, "name input field was not found")
        name.click()
        name.send_keys('Appium - new risk register')

    def create_new_context(self):

        self.switch_context_to_webview()

        logging.info("type name for new context")
        name = self.driver.find_element(*self.configuration.RisksScreen.CREATE_NEW_CONTEXT_INPUT_FIELD)
        self.assertIsNotNone(name, "input field was not found")
        name.click()
        name.send_keys('Appium - new context')

        self.switch_context_to_native()

    def click_save_button(self):

        self.switch_context_to_webview()

        logging.info("click save button")
        click_save_button = self.driver.find_element(*self.configuration.RisksScreen.SAVE_BUTTON)
        self.assertIsNotNone(click_save_button, "Save button not found")
        click_save_button.click()

    def open_existing_risk_register(self):

        logging.info("open first risk register on the list")
        open_existing_risk_register = self.driver.find_element(*self.configuration.RisksScreen.
                                                               FIRST_RISK_REGISTER_ON_THE_LIST)
        self.assertIsNotNone(open_existing_risk_register, "open existing Risk Register")
        open_existing_risk_register.click()

    def click_new_button(self):

        self.switch_context_to_webview()

        logging.info("click new button")
        click_new_button = self.driver.find_element(*self.configuration.RiskScreen.NEW_BUTTON)
        self.assertIsNotNone(click_new_button, "New button not found")
        click_new_button.click()

        self.switch_context_to_native()

    def click_add_new_context(self):

        logging.info("click add new context")
        click_add_new_context = self.driver.find_element(*self.configuration.RisksScreen.ADD_NEW_CONTEXT)
        self.assertIsNotNone(click_add_new_context, "Add new context button not found")
        click_add_new_context.click()

