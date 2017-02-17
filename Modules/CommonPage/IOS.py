""" Methods to handle iOS specific actions """

import logging
from time import sleep
from selenium.common.exceptions import *
from Modules.CommonPage.CommonPage import CommonPage


class IOS(CommonPage):

    def alert_popup_allow(self):

        try:
            button_allow_location = self.driver.find_element(*self.configuration.iOS.IOS_ALLOW)
            if button_allow_location.is_displayed():
                logging.info("Accept for example using location - device will store that info for later use")
                button_allow_location.click()
        except NoSuchElementException:
            pass
        try:
            button_allow_location = self.driver.find_element(*self.configuration.iOS.IOS_OK)
            if button_allow_location.is_displayed():
                button_allow_location.click()
        except NoSuchElementException:
            pass

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

    def scroll_down_one_view(self):  # scroll for iOS 10

        logging.info("scroll down one view")
        self.driver.execute_script("mobile: scroll", {"direction": "down"})


