""" Methods for IOS to handle Assets Page """

from Modules.AssetsPage.AssetsPage import AssetsPage
import logging


class IOS(AssetsPage):

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

    def scroll_down(self):

        logging.info("scroll down")
        self.driver.execute_script("mobile: scroll", {"direction": "down"})
        self.driver.execute_script("mobile: scroll", {"direction": "down"})
        self.driver.execute_script("mobile: scroll", {"direction": "down"})
        
    def scroll_up(self):

        logging.info("scroll up")
        self.driver.execute_script("mobile: scroll", {"direction": "up"})
        self.driver.execute_script("mobile: scroll", {"direction": "up"})
        self.driver.execute_script("mobile: scroll", {"direction": "up"})

