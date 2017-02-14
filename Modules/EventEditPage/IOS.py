""" Methods for IOS to handle Event Edit Page"""

from Modules.EventEditPage.EventEditPage import EventEditPage
from selenium.common.exceptions import *
import logging


class IOS(EventEditPage):

    def scroll_down_to_save_button(self):
        """Method to scroll down to bottom of the screen - to 'Save' button"""

        logging.info("scroll down with loop")
        scroll = 0
        while scroll == 0:
            logging.info("check if save button is visible")
            save_button = self.driver.find_element(*self.configuration.CommonScreen.SAVE_BUTTON)
            if save_button.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                # scroll -= 1
        # else:
        #     pass

    def fill_Name_input_field(self, text):

        logging.info("fill Name input field")
        try:
            name_field = self.driver.find_element(*self.configuration.EventEditScreen.NAME_FIELD)
            if name_field.is_displayed():
                name_field.click()
                name_field.send_keys(text)
        except NoSuchElementException:
            name_field_by_index = self.driver.find_element(*self.configuration.EventEditScreen.NAME_FIELD_by_index)
            if name_field_by_index.is_displayed():
                name_field_by_index.click()
                name_field_by_index.send_keys(text)



