""" Methods to handle iOS specific actions """

import logging
from time import sleep
from selenium.common.exceptions import *
from Modules.CommonPage.CommonPage import CommonPage


class IOS(CommonPage):

    def hamburger_button(self):

        super().hamburger_button()

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

    def click_back_button(self):

        super().click_back_button()

    def alert_android_allow(self):

        super().alert_android_allow()

    def click_set_button(self):

        super().click_set_button()

    def click_device_cancel_button(self):

        super().click_device_cancel_button()

    def click_clear_button(self):

        super().click_clear_button()

    # def scroll_down(self):
    #
    #     super().scroll_down()

    # def scroll_up(self):
    #
    #     super().scroll_up()

    def scroll_up_one_view(self):

        super().scroll_up_one_view()

    def take_screenshot(self, file_name):

        super().take_screenshot(file_name)

    def reset(self):

        super().reset()

    # def click_save_button(self):
    #
    #     super().click_save_button()
    #
    # def click_cancel_button(self):
    #
    #     super().click_cancel_button()

    def click_ok_button(self):

        super().click_ok_button()

