"""A class for methods to handle New Contact Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
import logging


class NewContactPage(BasePage):

    def type_first_name(self, text):

        self.switch_context_to_webview()

        logging.info("type first name")
        first_name = self.driver.find_element(*self.configuration.NewContactScreen.FIRST_NAME)
        self.assertIsNotNone(first_name, "First name input field was not found")
        first_name.click()
        first_name.send_keys(text)

        self.switch_context_to_native()

    def scroll_down_to_save_button(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.scroll_down_to_save_button()

    def click_save_button(self):

        self.switch_context_to_webview()

        logging.info('click Save button')
        save_button = self.driver.find_element(*self.configuration.NewContactScreen.SAVE_BUTTON)
        save_button.click()

        self.switch_context_to_native()

        # event_edit_page = LoadClass.load_page('EventEditPage')
        # event_edit_page.setDriver(self.driver)
        # event_edit_page.click_save_button()


