""" Methods for IOS to handle New Log Page """

from Modules.NewLogPage.NewLogPage import NewLogPage
import logging
from time import sleep


class IOS(NewLogPage):

    def scroll_down_to_entry_field(self):

        logging.info("scroll down with loop")
        var = 20
        while var > 0:
            logging.info("check if entry field is visible")
            entry_field = self.driver.find_element(*self.configuration.NewLogScreen.ENTRY_FIELD)
            if entry_field.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                var = var - 1

    # def type_text_into_entry_field(self, text):
    #
    #     logging.info("type text into 'Entry' field")
    #     entry_field = self.driver.find_element(*self.configuration.NewLogScreen.ENTRY_FIELD)
    #     entry_field.click()
    #     sleep(1)
    #     entry_field.send_keys(text)

    def scroll_down_to_save_button(self):
        """Method to scroll down to bottom of the screen - to 'Save' button"""

        logging.info("scroll down to Save button")
        scroll = 30
        while scroll > 0:
            logging.info("check if save button is visible")
            save_button = self.driver.find_element(*self.configuration.CommonScreen.SAVE_BUTTON)
            if save_button.is_displayed():
                break
            else:
                logging.info("scroll down to save button")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                scroll = scroll - 1


