"""A class for methods to handle Risks Page on IOS9 """

from Modules.RisksPage.IOS import IOS
import logging
from time import sleep


class IOS9(IOS):

    def scroll_down_to_save_button(self):

        pass

    # def click_status_selector(self):
    #
    #     self.switch_context_to_webview()
    #
    #     logging.info("click status selector")
    #     click_status_selector = self.driver.find_element(*self.configuration.RisksScreen.STATUS_SELECTOR)
    #     self.assertIsNotNone(click_status_selector, "status selector not found")
    #     click_status_selector.click()
    #     sleep(1)
    #
    #     self.switch_context_to_native()
