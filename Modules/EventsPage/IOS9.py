""" Methods for IOS 9 to handle Events Page"""

from Modules.EventsPage.IOS import IOS
import logging
from Modules.load_class import LoadClass
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.ui import WebDriverWait
# from appium.webdriver.common.touch_action import TouchAction


class IOS9(IOS):

    def scroll_down_to_save_button(self):

        pass

    def scroll_down_to_event_chooser_field(self):

        pass

    def scroll_down_to_add_row_button(self):

        pass

    def scroll_down_to_option_list(self):

        pass

    def scroll_down_to_description_field(self):

        pass

    def click_save_new_event(self):

        logging.info("click Save button")

        self.switch_context_to_webview()
        save_button = self.driver.find_element(*self.configuration.EventEditScreen.SAVE_BUTTON_NEW_EVENT)
        self.assertIsNotNone(save_button, "Save button not found")
        save_button.click()
        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    def click_save_edited_event(self):

        self.switch_context_to_webview()
        save_button = self.driver.find_element(*self.configuration.EventEditScreen.SAVE_BUTTON_EDIT_EVENT)
        self.assertIsNotNone(save_button, "Save button not found")
        save_button.click()
        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

