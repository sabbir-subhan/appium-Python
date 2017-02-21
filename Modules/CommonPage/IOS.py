""" Methods to handle iOS specific actions """

import logging
from time import sleep
from selenium.common.exceptions import *
from Modules.CommonPage.CommonPage import CommonPage


class IOS(CommonPage):

    def click_back_button(self):
        """ Method to handle back button in Safari Browser """
        # Appium can't access another app directly, only tapping on specific coordinates will work

        logging.info("wait for page to load")
        sleep(10)
        logging.info("click 'Back to OCA' button")
        # positions = [(15, 7)]
        # self.driver.tap(positions)

        window_size = self.driver.get_window_size()  # this returns dictionary
        logging.info(window_size)
        position_x = window_size["width"] * 0.04
        position_y = window_size["height"] * 0.03
        logging.info(position_x)
        logging.info(position_y)
        sleep(2)
        positions = [(position_x, position_y)]
        self.driver.tap(positions)

    # OCA top bar
    def hamburger_button(self):

        logging.info("close and reopen app to avoid problems with locating elements")
        self.driver.reset()

        logging.info("click hamburger button to go back to main menu - IOS ")
        sleep(1)
        hamburger_button = self.driver.find_element(*self.configuration.TopBar.HAMBURGER_FOR_MAIN_MENU)
        # self.assertIsNotNone(hamburger_button, "Hamburger button is not present")  #button is invisible by appium
        # but version 1.6.3 can click it
        hamburger_button.click()
        # try:
        #     hamburger_button = self.driver.find_element(*self.configuration.TopBar.HAMBURGER_FOR_MAIN_MENU)
        #     if hamburger_button.is_displayed():
        #         self.assertIsNotNone(hamburger_button, "Hamburger button is not present")
        #         hamburger_button.click()
        # except ElementNotVisibleException:
        #     logging.info("except")
        #     window_size = self.driver.get_window_size()  # this returns dictionary
        #     logging.info(window_size)
        #     position_x = window_size["width"] * 0.98
        #     position_y = window_size["height"] * 0.04
        #     logging.info(position_x)
        #     logging.info(position_y)
        #     positions = [(position_x, position_y)]
        #     self.driver.tap(positions)
        sleep(4)

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
        sleep(1)
        self.driver.execute_script("mobile: scroll", {"direction": "down"})  # sometimes one is not enough



