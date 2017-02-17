""" Methods to handle iOS 9 specific actions """

from Modules.CommonPage.IOS import IOS
from time import sleep
import logging
from selenium.common.exceptions import *


class IOS9(IOS):

    def alert_popup_allow(self):

        pass  # iOS9 will auto accept alerts

    def hide_keyboard(self):

        logging.info("hide keyboard")
        try:
            done_button = self.driver.find_element(*self.configuration.iOS.BUTTON_DONE_TO_HIDE_KEYBOARD)
            if done_button.is_displayed():
                done_button.click()
            else:
                pass
        except NoSuchElementException:
            self.driver.hide_keyboard(key_name="Hide keyboard")

    def click_Return_button_on_keyboard(self):

        logging.info("click 'Return' on keyboard")
        self.driver.find_element(*self.configuration.iOS.RETURN_BUTTON).click()
        sleep(1)

    def done_button(self):

        self.driver.find_element(*self.configuration.iOS.BUTTON_DONE_TO_HIDE_KEYBOARD).click()





