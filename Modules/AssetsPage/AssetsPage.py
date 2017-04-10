"""A class for methods to handle Assets Page """

from Modules.BasePage.BasePage import BasePage
import logging


class AssetsPage(BasePage):

    def click_new_button(self):

        self.switch_context_to_webview()

        logging.info('click New button')
        new_button = self.driver.find_element(*self.configuration.AssetsScreen.NEW_BUTTON)
        self.assertIsNotNone(new_button, "new button not found")
        new_button.click()

        self.switch_context_to_native()

    def click_new_asset(self):

        self.switch_context_to_webview()

        logging.info('click New asset')
        new_asset = self.driver.find_element(*self.configuration.AssetsScreen.NEW_ASSET_BUTTON)
        self.assertIsNotNone(new_asset, "new asset button not found")
        new_asset.click()

        self.switch_context_to_native()

    def choose_asset_type(self):

        self.switch_context_to_webview()

        logging.info('choosea asset type')
        asset_type = self.driver.find_element(*self.configuration.AssetsScreen.ASSET_TYPE)
        self.assertIsNotNone(asset_type, "asset type not found")
        asset_type.click()

        self.switch_context_to_native()

    def fill_Name_input_field(self, text):

        self.switch_context_to_webview()

        logging.info("type title")
        title = self.driver.find_element(*self.configuration.AssetsScreen.NAME)
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
        save_button = self.driver.find_element(*self.configuration.AssetsScreen.SAVE_BUTTON)
        save_button.click()

        self.switch_context_to_native()

        # event_edit_page = LoadClass.load_page('EventEditPage')
        # event_edit_page.setDriver(self.driver)
        # event_edit_page.click_save_button()


