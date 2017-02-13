import logging
from time import sleep
from selenium.common.exceptions import *
from Modules.BasePage.BasePage import BasePage


class iOSDevice(BasePage):
    """A class for methods to handle iOS Device"""

    def hide_keyboard(self):

        logging.info("hide keyboard")
        try:
            done_button_ios = self.driver.find_element(*self.configuration.iOS.BUTTON_DONE_TO_HIDE_KEYBOARD)
            if done_button_ios.is_displayed():
                done_button_ios.click()
            else:
                pass
        except NoSuchElementException:
            self.driver.hide_keyboard(key_name="Hide keyboard")

    def click_Return_button_on_keyboard(self):

        logging.info("click 'Return' on keyboard")
        self.driver.find_element(*self.configuration.iOS.RETURN_BUTTON_ios).click()
        sleep(1)

    def done_button(self):

        self.driver.find_element(*self.configuration.iOS.BUTTON_DONE_TO_HIDE_KEYBOARD_ios).click()

    def scroll_down_one_view(self):  # scroll for iOS 10

        logging.info("scroll down one view")
        self.driver.execute_script("mobile: scroll", {"direction": "down"})

