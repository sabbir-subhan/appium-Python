""" Methods to handle iOS 9 specific actions """

from Modules.CommonPage.IOS import IOS
from time import sleep
import logging
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class IOS9(IOS):

    # # OCA top bar
    # def hamburger_button(self):
    #
    #     logging.info("click hamburger button to go back to main menu - IOS 9")
    #     window_size = self.driver.get_window_size()  # this returns dictionary
    #     logging.info(window_size)
    #     position_x = window_size["width"] * 0.98
    #     position_y = window_size["height"] * 0.04
    #     logging.info(position_x)
    #     logging.info(position_y)
    #     positions = [(position_x, position_y)]
    #     self.driver.tap(positions)
    #     sleep(4)

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
        sleep(1)

    def click_Return_button_on_keyboard(self):

        logging.info("click 'Return' on keyboard")
        self.driver.find_element(*self.configuration.iOS.RETURN_BUTTON).click()
        sleep(1)

    def done_button(self):

        self.driver.find_element(*self.configuration.iOS.BUTTON_DONE_TO_HIDE_KEYBOARD).click()

    def scroll_down_one_view(self):  # iOS 9 don't need scroll

        pass

    def click_back_button(self):
        """ Method to handle back button in Safari Browser """
        # Appium can't access another app directly, only tapping on specific coordinates will work

        logging.info("click 'Back to OCA' button")

        window_size = self.driver.get_window_size()  # this returns dictionary
        logging.info(window_size)

        position_x = window_size["width"] * 0.008  # works for iPad
        position_y = window_size["height"] * 0.009

        logging.info(position_x)
        logging.info(position_y)
        positions = [(position_x, position_y)]
        sleep(2)
        self.driver.tap(positions, duration=1200)  # for iOS10 - 'Support for this gesture is not yet implemented'
        sleep(2)
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located(self.configuration.MainMenuScreen.EVENTS_BUTTON),
            "Failed to locate Events button")






