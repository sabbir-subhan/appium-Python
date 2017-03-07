"""A class for methods to handle New Contact Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
import logging


class NewContactPage(BasePage):

    def type_first_name(self, text):

        logging.info("type first name")
        first_name = self.driver.find_element(*self.configuration.NewContactScreen.FIRST_NAME)
        self.assertIsNotNone(first_name, "First name input field was not found")
        first_name.click()
        first_name.send_keys(text)

    def scroll_down_to_save_button(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.scroll_down_to_save_button()

    def click_save_button(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.click_save_button()


