"""A class for methods to handle New Asset Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
import logging


class NewAssetPage(BasePage):

    def fill_Name_input_field(self, text):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.fill_Name_input_field(text)

    def scroll_down_to_save_button(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.scroll_down_to_save_button()

    def click_save_button(self):

        self.switch_context_to_webview()

        logging.info('click Save button')
        save_button = self.driver.find_element(*self.configuration.NewAssetScreen.SAVE_BUTTON)
        save_button.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

        # event_edit_page = LoadClass.load_page('EventEditPage')
        # event_edit_page.setDriver(self.driver)
        # event_edit_page.click_save_button()


