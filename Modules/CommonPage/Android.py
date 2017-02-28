""" Methods to handle Android specific actions """

import logging
from time import sleep
from selenium.common.exceptions import *
from Modules.CommonPage.CommonPage import CommonPage
# from Conf.desired_capabilities import DesiredCapabilities


class Android(CommonPage):

    # OCA top bar
    def hamburger_button(self):

        logging.info("click hamburger button to go back to main menu")
        hamburger_button = self.driver.find_element(*self.configuration.TopBar.HAMBURGER_FOR_MAIN_MENU)
        if hamburger_button.is_displayed():
            self.assertIsNotNone(hamburger_button, "Hamburger button is not present")
            hamburger_button.click()
        else:
            self.fail("Hamburger button not found")
        sleep(4)

    def alert_popup_allow(self):

        try:
            button_allow_location = self.driver.find_element(*self.configuration.Android.ANDROID_ALLOW)
            if button_allow_location.is_displayed():
                # logging.info("Accept for example using location - device will store that info for later use")
                button_allow_location.click()
        except NoSuchElementException:
            pass
        try:
            button_allow_location = self.driver.find_element(*self.configuration.Android.ANDROID_ALLOW)
            if button_allow_location.is_displayed():
                button_allow_location.click()
        except NoSuchElementException:
            pass

    def hide_keyboard(self):

        try:
            logging.info("hide screen keyboard")
            self.driver.hide_keyboard()
            sleep(3)
        except:
            logging.info("screen keyboard not found")

    def click_Return_button_on_keyboard(self):

        try:
            logging.info("click Go on keyboard")
            self.driver.keyevent(66)
            sleep(3)
        except NoSuchElementException:
            logging.info("keyboard not found")

    def scroll_down_one_view(self):
        """Method to scroll down only one screen"""

        window_size = self.driver.get_window_size()  # this will give You a dictionary
        start_x = window_size["width"] * 0.25
        start_y = window_size["height"] * 0.15
        end_y = window_size["height"] * 0.8
        logging.info("scroll down only one screen")
        sleep(2)
        self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
        sleep(1)

    def click_back_button(self):

        logging.info("click 'Back' button")
        self.driver.press_keycode(4)
        sleep(5)

    def click_set_button(self):

        logging.info("Click 'Set' button")
        set_button = self.driver.find_element(*self.configuration.Android.ANDROID_SET_BUTTON)
        self.assertIsNotNone(set_button, "Set button was not found")
        set_button.click()

    def click_device_cancel_button(self):

        logging.info("Click 'Cancel' button")
        cancel_button = self.driver.find_element(*self.configuration.Android.ANDROID_CANCEL_BUTTON)
        self.assertIsNotNone(cancel_button, "Cancel button was not found")
        cancel_button.click()

    def click_clear_button(self):

        logging.info("Click 'Clear' button")
        clear_button = self.driver.find_element(*self.configuration.Android.ANDROID_CLEAR_BUTTON)
        self.assertIsNotNone(clear_button, "Clear button was not found")
        clear_button.click()

    def scroll_up_one_view(self):
        """Method to scroll down only one screen"""

        window_size = self.driver.get_window_size()  # this will give You a dictionary
        start_x = window_size["width"] * 0.25
        start_y = window_size["height"] * 0.15
        end_y = window_size["height"] * 0.8
        logging.info("scroll down only one screen")
        sleep(2)
        self.driver.swipe(start_x, start_y, start_x, end_y, 3000)  # each swipe is scrolling one screen
        sleep(1)

    # @staticmethod
    # def get_platform_version():
    #
    #     desired_capabilities = DesiredCapabilities.get_desired_capabilities()
    #     logging.info(desired_capabilities)
    #     platform_version = desired_capabilities.get('platformVersion')
    #     logging.info(platform_version)

        # if platform_version == "6.0.1":
        #     print(":)")
        # else:
        #     print("x")
