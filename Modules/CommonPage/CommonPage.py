"""A class for methods to handle Common Page """

from Modules.BasePage.BasePage import BasePage
import logging
from time import sleep
from selenium.common.exceptions import *


class CommonPage(BasePage):

    # OCA top bar
    def hamburger_button(self):
        # add coordinates for iPhones - clicking is not working because button is invisible
        logging.info("click hamburger button to go back to main menu")
        try:
            hamburger_button = self.driver.find_element(*self.configuration.TopBar.HAMBURGER_FOR_MAIN_MENU)
            if hamburger_button.is_displayed():
                self.assertIsNotNone(hamburger_button, "Hamburger button is not present")
                hamburger_button.click()
        except NoSuchElementException:
            positions_for_hamburger_button = [(730, 20)]
            sleep(1)
            self.driver.tap(positions_for_hamburger_button)

    def hide_keyboard(self):

        pass

    def click_Return_button_on_keyboard(self):

        pass

    def done_button(self):

        pass

    def scroll_down_one_view(self):

        pass

    def click_back_button(self):

        pass

    def alert_android_allow(self):

        pass

    def click_set_button(self):

        pass

    def click_device_cancel_button(self):

        logging.info("Click 'Cancel' button")
        cancel_button = self.driver.find_element(*self.configuration.Android.ANDROID_CANCEL_BUTTON)
        self.assertIsNotNone(cancel_button, "Cancel button was not found")
        cancel_button.click()

    def click_clear_button(self):

        pass

    # def scroll_down(self):
    #
    #     pass

    # def scroll_up(self):
    #
    #     pass

    def scroll_up_one_view(self):

        pass

    def take_screenshot(self, file_name):

        logging.info("taking screenshot")
        sleep(2)
        self.driver.save_screenshot(file_name)

    def reset(self):
        """This method will reset driver - so for example app will be force to logout"""
        logging.info("reset")
        self.driver.reset()

    # def click_save_button(self):
    #
    #     logging.info("click Save button")
    #     save_button = self.driver.find_element(*self.configuration.CommonScreen.SAVE_BUTTON)
    #     self.assertIsNotNone(save_button, "Save button not found")
    #     save_button.click()
    #     sleep(10)
    #
    # def click_cancel_button(self):
    #
    #     logging.info("click on Cancel button")
    #     cancel_button = self.driver.find_element(*self.configuration.CommonScreen.CANCEL_BUTTON)
    #     self.assertIsNotNone(cancel_button, "Cancel button not found")
    #     cancel_button.click()

    def click_ok_button(self):

        logging.info("click on 'Ok' button")
        ok_button = self.driver.find_element(*self.configuration.CommonScreen.OK_BUTTON)
        self.assertIsNotNone(ok_button, "Ok button not found")
        ok_button.click()
