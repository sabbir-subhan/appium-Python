""" Methods to handle iOS specific actions """

import logging
from time import sleep
from selenium.common.exceptions import *
from Modules.CommonPage.CommonPage import CommonPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from Modules.load_class import LoadClass


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
    # def hamburger_button(self):
    #
    #     self.switch_context_to_webview()
    #
    #     logging.info("click hamburger button to go back to main menu - IOS")
    #     hamburger_button = self.driver.find_element(*self.configuration.TopBar.HAMBURGER_FOR_MAIN_MENU)
    #     hamburger_button.click()
    #     # window_size = self.driver.get_window_size()  # this returns dictionary
    #     # logging.info(window_size)
    #     # position_x = window_size["width"] * 0.98
    #     # position_y = window_size["height"] * 0.04
    #     # logging.info(position_x)
    #     # logging.info(position_y)
    #     # positions = [(position_x, position_y)]
    #     # self.driver.tap(positions)
    #     sleep(5)
    #
    #     self.switch_context_to_native()

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

        logging.info('search for alert and click "Allow" if found')
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
        try:
            button_allow_location = self.driver.find_element(*self.configuration.iOS.IOS_OK)  # sometimes iOS is asking two times
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

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    def done_button(self):

        self.driver.find_element(*self.configuration.iOS.BUTTON_DONE_TO_HIDE_KEYBOARD).click()

    def scroll_down_one_view(self):  # scroll for iOS 10

        logging.info("scroll down one view")
        self.driver.execute_script("mobile: scroll", {"direction": "down"})
        sleep(1)
        self.driver.execute_script("mobile: scroll", {"direction": "down"})  # sometimes one is not enough

    def clear_Search_field(self):

        # logging.info("clear search field")
        # search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        # # search_field.click()
        # # sleep(0.5)
        # timeout = time.time() + 60 * 2  # 2 minutes from now
        # while len(search_field.text) > 0:
        #     search_field.click()
        #     search_field.clear()
        #     IOS.hide_keyboard(self)
        #     if time.time() > timeout:
        #         break
        #     sleep(1)
        logging.info("clear search field")
        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        search_field.click()
        sleep(0.5)
        search_field.clear()
        try:
            search_field.click()
            search_field.clear()
        except:
            pass



