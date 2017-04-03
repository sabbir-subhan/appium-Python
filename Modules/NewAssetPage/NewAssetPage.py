"""A class for methods to handle New Asset Page """

from Modules.BasePage.BasePage import BasePage
import logging


class NewAssetPage(BasePage):

    def fill_Name_input_field(self, text):

        self.switch_context_to_webview()

        logging.info("type title")
        title = self.driver.find_element(*self.configuration.NewAssetScreen.NAME)
        self.assertIsNotNone(title, "Title input field was not found")
        title.click()
        title.send_keys(text)

        self.switch_context_to_native()

        # event_edit_page = LoadClass.load_page('EventEditPage')
        # event_edit_page.setDriver(self.driver)
        # event_edit_page.fill_Name_input_field(text)

    # def scroll_down_to_save_button(self):
    #
    #     event_edit_page = LoadClass.load_page('EventEditPage')
    #     event_edit_page.setDriver(self.driver)
    #     event_edit_page.scroll_down_to_save_button()

    def click_save_button(self):

        self.switch_context_to_webview()

        logging.info('click Save button')
        save_button = self.driver.find_element(*self.configuration.NewAssetScreen.SAVE_BUTTON)
        save_button.click()

        self.switch_context_to_native()

        # event_edit_page = LoadClass.load_page('EventEditPage')
        # event_edit_page.setDriver(self.driver)
        # event_edit_page.click_save_button()


