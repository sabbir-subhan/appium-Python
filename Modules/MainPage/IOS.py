""" Methods for IOS to handle Main Page"""

from Modules.MainPage.MainPage import MainPage
import logging


class IOS(MainPage):

    def scroll_down_to_sound_button(self):

        logging.info("scroll down with loop")
        var = 1
        while var == 1:
            logging.info("check if sound button is visible")
            save_button = self.driver.find_element(*self.configuration.MainScreen.SOUND_BUTTON)
            if save_button.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
