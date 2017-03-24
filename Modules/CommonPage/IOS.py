""" Methods to handle iOS specific actions """

import logging
from time import sleep
from selenium.common.exceptions import *
from Modules.CommonPage.CommonPage import CommonPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class IOS(CommonPage):

    def click_back_button(self):
        """ Method to handle back button in Safari Browser """
        # Appium can't access another app directly, only tapping on specific coordinates will work

        logging.info("click 'Back to OCA' button")

        window_size = self.driver.get_window_size()  # this returns dictionary
        logging.info(window_size)
        width = window_size["width"]
        # height = window_size["height"]

        sleep(4)
        if width > 376:
            position_x = window_size["width"] * 0.008
            position_y = window_size["height"] * 0.009
            logging.info(position_x)
            logging.info(position_y)
            positions = [(position_x, position_y)]
            self.driver.tap(positions)
            sleep(2)
        else:
            position_x = window_size["width"] * 0.03
            position_y = window_size["height"] * 0.02
            logging.info(position_x)
            logging.info(position_y)
            positions = [(position_x, position_y)]
            self.driver.tap(positions)
            sleep(2)

        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located(self.configuration.MainMenuScreen.EVENTS_BUTTON),
            "Failed to locate Events button")

    # OCA top bar
    def hamburger_button(self):

        self.switch_context_to_webview()

        logging.info("click hamburger button to go back to main menu - IOS")
        hamburger_button = self.driver.find_element(*self.configuration.TopBar.HAMBURGER_FOR_MAIN_MENU)
        hamburger_button.click()
        # window_size = self.driver.get_window_size()  # this returns dictionary
        # logging.info(window_size)
        # position_x = window_size["width"] * 0.98
        # position_y = window_size["height"] * 0.04
        # logging.info(position_x)
        # logging.info(position_y)
        # positions = [(position_x, position_y)]
        # self.driver.tap(positions)
        sleep(5)

        self.switch_context_to_native()

    # # OCA top bar
    # def hamburger_button(self):
    #
    #     # logging.info("close and reopen app to avoid problems with locating elements")
    #     # self.driver.reset()
    #
    #     logging.info("click hamburger button to go back to main menu - IOS ")
    #     sleep(2)
    #     hamburger_button = self.driver.find_element(*self.configuration.TopBar.HAMBURGER_FOR_MAIN_MENU)
    #     self.assertIsNotNone(hamburger_button, "Hamburger button is not present")
    #     location = hamburger_button.location
    #     print(location)
    #     x = location["x"]
    #     y = location["y"]
    #     print(x)
    #     print(y)
    #     positions = [(x, y)]
    #     self.driver.tap(positions)
    #     sleep(5)

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
        try:
            button_allow_location = self.driver.find_element(*self.configuration.iOS.IOS_ALLOW)  # sometimes iOS is asking two times
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



