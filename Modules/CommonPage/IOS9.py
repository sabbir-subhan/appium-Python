""" Methods to handle iOS 9 specific actions """

from Modules.CommonPage.IOS import IOS
from time import sleep
import logging
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from Modules.load_class import LoadClass
from appium.webdriver.common.touch_action import TouchAction


class IOS9(IOS):

    def swipe_up_to_show_control_center(self):  # this will bring control center

        logging.info("swipe up to show control center")
        window_size = self.driver.get_window_size()  # this returns dictionary
        el = self.driver.find_element(*self.configuration.CommonScreen.WEB_VIEW)
        action = TouchAction(self.driver)
        start_x = window_size["width"] * 0.5
        start_y = window_size["height"]
        end_x = window_size["width"] * 0.5
        end_y = window_size["height"] * 0.5
        action.press(el, start_x, start_y).wait(1000).move_to(el, end_x, end_y).release().perform()
        sleep(1)

    def swipe_up_to_hide_notifications(self):

        logging.info("swipe up to hide notifications")
        window_size = self.driver.get_window_size()  # this returns dictionary
        start_x = window_size["width"] * 0.5
        start_y = window_size["height"] - 1
        self.driver.swipe(start_x=start_x, start_y=start_y, end_x=start_x, end_y=-10, duration=1000)
        # action.press(el, start_x, start_y).wait(1000).move_to(el, end_x, end_y).release().perform()
        sleep(1)

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
        # try/except because on iPhone with iOS9 after clicking on "clear search field" button keyboard is not
        # displayed automatically

        try:
            logging.info("click 'Return' on keyboard")
            self.driver.find_element(*self.configuration.iOS.RETURN_BUTTON).click()
            sleep(1)
        except NoSuchElementException:
            pass

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

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

    def wait_for_app_loading(self):

        # pass
        # logging.info("wait for app loading")
        WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element_located(self.configuration.CommonScreen.LOADING),
            "app is still loading - check internet connection")





