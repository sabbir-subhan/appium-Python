import logging
from Modules.BasePage import BasePage


class EventEditPage(BasePage):
    """A class for methods to handle Event Edit Page"""

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
