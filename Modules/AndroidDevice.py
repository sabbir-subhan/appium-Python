import logging
from time import sleep
from selenium.common.exceptions import *
from Modules.BasePage.BasePage import BasePage


class AndroidDevice(BasePage):
    """ A class for methods to handle Android Device """

    def hide_keyboard(self):

        try:
            logging.info("hide screen keyboard")
            self.driver.hide_keyboard()
            sleep(3)
        except:
            logging.info("screen keyboard not found")

    def click_Go_button_on_keyboard(self):

        try:
            logging.info("click Go on keyboard")
            self.driver.keyevent(66)
            sleep(3)
        except NoSuchElementException:
            logging.info("keyboard not found")

    def click_back_button(self):

        logging.info("click 'Back' button")
        self.driver.press_keycode(4)
        sleep(5)

    def alert_android_allow(self):

        try:
            button_allow_location = self.driver.find_element(*self.configuration.Android.ANDROID_ALLOW)
            if button_allow_location.is_displayed():
                logging.info("Accept for example using location - device will store that info for later use")
                button_allow_location.click()
        except NoSuchElementException:
            pass
        try:
            button_allow_location = self.driver.find_element(*self.configuration.Android.ANDROID_ALLOW)
            if button_allow_location.is_displayed():
                button_allow_location.click()
        except NoSuchElementException:
            pass

    def click_set_button(self):

        logging.info("Click 'Set' button")
        set_button = self.driver.find_element(*self.configuration.Android.ANDROID_SET_BUTTON)
        self.assertIsNotNone(set_button, "Set button was not found")
        set_button.click()

    def click_cancel_button(self):

        logging.info("Click 'Cancel' button")
        cancel_button = self.driver.find_element(*self.configuration.Android.ANDROID_CANCEL_BUTTON)
        self.assertIsNotNone(cancel_button, "Cancel button was not found")
        cancel_button.click()

    def click_clear_button(self):

        logging.info("Click 'Clear' button")
        clear_button = self.driver.find_element(*self.configuration.Android.ANDROID_CLEAR_BUTTON)
        self.assertIsNotNone(clear_button, "Clear button was not found")
        clear_button.click()

    def scroll_down(self):
        """Method to scroll down to bottom of the screen - to 'Save' button"""

        window_size = self.driver.get_window_size()  # this returns dictionary
        start_x = window_size["width"]*0.25
        # end_x = window_size["width"]*0.75
        start_y = window_size["height"]*0.20
        end_y = window_size["height"]*0.80
        logging.info("scroll down")
        sleep(2)
        scrolls = 13
        while scrolls > 0:
            self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
            scrolls -= 1
        sleep(2)

    def scroll_up(self):
        """Method to scroll up to top of the screen"""

        window_size = self.driver.get_window_size()  # this will give You a dictionary
        start_x = window_size["width"]*0.25
        # end_x = window_size["width"]*0.75
        start_y = window_size["height"]*0.25
        end_y = window_size["height"]*0.80
        logging.info("scroll up")
        sleep(2)
        scrolls = 13
        while scrolls > 0:
            self.driver.swipe(start_x, start_y, start_x, end_y, 3000)  # each swipe is scrolling one screen
            scrolls -= 1
        sleep(1)

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
