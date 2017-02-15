""" A class for methods to handle Event Edit Page """

import logging
from Modules.BasePage.BasePage import BasePage
from time import sleep


class EventEditPage(BasePage):

    def scroll_down(self):

        pass

    def scroll_up(self):

        pass

    def fill_Name_input_field(self, text):

        pass

    def click_severity_lvl_picker(self):

        logging.info("click on severity level field")
        self.driver.find_element(*self.configuration.EventEditScreen.SEVERITY_LEVEL_SELECTOR).click()

    def choose_severity_level_1(self):

        pass

    def choose_severity_level_2(self):

        pass

    def choose_severity_level_3(self):

        pass

    def choose_severity_level_4(self):

        pass

    def choose_severity_level_5(self):

        pass

    def click_save_button(self):

        logging.info("click Save button")
        save_button = self.driver.find_element(*self.configuration.CommonScreen.SAVE_BUTTON)
        self.assertIsNotNone(save_button, "Save button not found")
        save_button.click()
        sleep(10)

    def click_cancel_button(self):

        logging.info("click on Cancel button")
        cancel_button = self.driver.find_element(*self.configuration.CommonScreen.CANCEL_BUTTON)
        self.assertIsNotNone(cancel_button, "Cancel button not found")
        cancel_button.click()







