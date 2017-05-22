""" Methods to handle Android specific actions """

import logging
from time import sleep
from selenium.common.exceptions import *
from Modules.CommonPage.CommonPage import CommonPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from Conf.desired_capabilities import DesiredCapabilities
from appium.webdriver.common.touch_action import TouchAction


class Android(CommonPage):

    def clear_Search_field(self):

        logging.info("clear search field")

        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        search_field.click()
        sleep(1)
        action = TouchAction(self.driver)
        action.long_press(el=search_field, duration=1500).perform()
        self.driver.press_keycode(67)
        sleep(0.5)
        try:
            action.long_press(el=search_field, duration=1500).perform()
            self.driver.press_keycode(67)
        except:
            pass

        # search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        # search_field.click()
        # sleep(1)
        # while len(search_field.text) > 0:
        #     action = TouchAction(self.driver)
        #     action.long_press(el=search_field, duration=1500).perform()
        #     self.driver.press_keycode(67)
        #     sleep(0.5)
        # sleep(0.5)

    # OCA top bar
    # def hamburger_button(self):
    #
    #     sleep(1)
    #     logging.info("click hamburger button to go back to main menu")

        # desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        # platform_version = desired_capabilities.get('platformVersion')
        # # if platform_version < "5":
        # hamburger_button = self.driver.find_element(*self.configuration.TopBar.HAMBURGER_FOR_MAIN_MENU_by_xpath)
        # # else:
        # #     hamburger_button = self.driver.find_element(*self.configuration.TopBar.HAMBURGER_FOR_MAIN_MENU_by_id)
        # self.assertIsNotNone(hamburger_button, "Hamburger button is not present")
        # location = hamburger_button.location
        # print(location)
        # x = location["x"]
        # y = location["y"]
        # print(x)
        # print(y)
        # positions = [(x, y)]
        # self.driver.tap(positions)
        # hamburger_button.click()
        # sleep(5)

    def alert_popup_allow(self):

        logging.info('search for alert and click "Allow" if found')
        try:
            button_allow_location = self.driver.find_element(*self.configuration.Android.ANDROID_ALLOW)
            if button_allow_location.is_displayed():
                # logging.info("Accept for example using location - device will store that info for later use")
                button_allow_location.click()
        except:
            pass
        try:
            button_allow_location = self.driver.find_element(*self.configuration.Android.ANDROID_ALLOW)
            if button_allow_location.is_displayed():
                button_allow_location.click()
        except:
            pass

    def hide_keyboard(self):

        try:
            logging.info("hide screen keyboard")
            self.driver.hide_keyboard()
            sleep(1)
        except:
            logging.info("screen keyboard not found")

    def click_Return_button_on_keyboard(self):

        try:
            logging.info("click Go on keyboard")
            self.driver.press_keycode(66)
            sleep(3)
        except NoSuchElementException:
            logging.info("keyboard not found")

    def scroll_down_one_view(self):
        """Method to scroll down only one screen"""

        window_size = self.driver.get_window_size()  # this will give You a dictionary
        start_x = window_size["width"] * 0.25
        start_y = window_size["height"] * 0.15
        if window_size["height"] <= 800:
            end_y = window_size["height"] * 0.6
        else:
            end_y = window_size["height"] * 0.8
        logging.info("scroll down only one screen")
        sleep(2)
        self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
        sleep(1)

    def click_back_button(self):
        """ Method to handle back button for Android """

        logging.info("click 'Back' button")
        self.driver.press_keycode(4)
        # self.driver.keyevent(4)
        # self.driver.back()
        sleep(4)
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located(self.configuration.MainMenuScreen.INBOX_BUTTON),
            "Failed to locate Inbox button")

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

    def additional_appium_actions(self):

        # print(self.driver.contexts)
        # self.driver.refresh()  # Method has not yet been implemented
        print(self.driver.page_source)
        self.driver.press_keycode(3)  # Press Home Key
        self.driver.press_keycode(187)  # KEYCODE_APP_SWITCH
        self.driver.find_element_by_accessibility_id('OCA')  # maximize app

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

    def scroll_up(self):
        """Method to scroll up to top of the screen """

        window_size = self.driver.get_window_size()  # this returns dictionary
        start_x = window_size["width"] * 0.25
        start_y = window_size["height"] * 0.20
        end_y = window_size["height"] * 0.80
        logging.info("scroll up")
        sleep(2)
        scrolls = 3  # number of swipes
        while scrolls > 0:
            self.driver.swipe(start_x, start_y, start_x, end_y, 3000)  # each swipe is scrolling one screen
            scrolls = scrolls - 1
        sleep(2)

    def scroll_down(self):
        """Method to scroll down to bottom of the screen """

        window_size = self.driver.get_window_size()  # this returns dictionary
        start_x = window_size["width"] * 0.25
        start_y = window_size["height"] * 0.20
        end_y = window_size["height"] * 0.80
        logging.info("scroll down")
        sleep(2)
        scrolls = 3  # number of swipes
        while scrolls > 0:
            self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
            scrolls = scrolls - 1
        sleep(2)

