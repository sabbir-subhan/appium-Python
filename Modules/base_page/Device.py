import logging
from time import sleep
from selenium.common.exceptions import *
from Modules.base_page import BasePage


class Device(BasePage):
    """A class for methods to handle iOS Device"""

    def hide_keyboard(self):

        logging.info("hide keyboard")
        try:
            done_button_ios = self.driver.find_element(*iOS.BUTTON_DONE_TO_HIDE_KEYBOARD_ios)
            if done_button_ios.is_displayed():
                done_button_ios.click()
            else:
                pass
        except NoSuchElementException:
            self.driver.hide_keyboard(key_name="Hide keyboard")

    def click_Return_button_on_keyboard(self):

        logging.info("click 'Return' on keyboard")
        self.driver.find_element(*iOS.RETURN_BUTTON_ios).click()
        sleep(1)

    def done_button(self):

        self.driver.find_element(*iOS.BUTTON_DONE_TO_HIDE_KEYBOARD_ios).click()
