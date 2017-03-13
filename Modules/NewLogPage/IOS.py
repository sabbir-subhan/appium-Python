""" Methods for IOS to handle New Log Page """

from Modules.NewLogPage.NewLogPage import NewLogPage
import logging
from time import sleep


class IOS(NewLogPage):

    def scroll_down_to_entry_field(self):

        logging.info("scroll down with loop")
        var = 1
        while var == 1:
            logging.info("check if entry field is visible")
            entry_field = self.driver.find_element(*self.configuration.NewLogScreen.ENTRY_FIELD)
            if entry_field.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})

    def type_text_into_entry_field(self, text):

        logging.info("type text into 'Entry' field")
        entry_field = self.driver.find_element(*self.configuration.NewLogScreen.ENTRY_FIELD)
        entry_field.click()
        sleep(1)
        entry_field.send_keys(text)

