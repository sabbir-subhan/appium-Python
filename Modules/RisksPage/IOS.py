"""A class for methods to handle Risks Page on iOS"""

from Modules.RisksPage.RisksPage import RisksPage
from Modules.load_class import LoadClass
import logging
from selenium.common.exceptions import *
from time import sleep


class IOS(RisksPage):

    def click_status_selector(self):

        logging.info("click status selector")
        click_status_selector = self.driver.find_element(*self.configuration.RisksScreen.STATUS_SELECTOR)
        self.assertIsNotNone(click_status_selector, "status selector not found")
        click_status_selector.click()
        sleep(1)

    def scroll_down_to_save_button(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.scroll_down_to_save_button()

    def choose_status_implemented(self):

        logging.info("choose status implemented")
        try:
            choose_status_implemented = self.driver.find_element(*self.configuration.RisksScreen.CHOOSE_STATUS_IMPLEMENTED_iPad)
            self.assertIsNotNone(choose_status_implemented, "choose status implemented not found")
            choose_status_implemented.click()
        except NoSuchElementException:
            picker_wheel = self.driver.find_element(*self.configuration.CommonScreen.PICKER_WHEEL)
            picker_wheel.send_keys('Implemented')
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.done_button()
