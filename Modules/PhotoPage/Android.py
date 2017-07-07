""" Methods for Android on Photo Page """

from Modules.PhotoPage.PhotoPage import PhotoPage
import logging
from time import sleep
from Conf.desired_capabilities import DesiredCapabilities
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.ui import WebDriverWait
# from appium.webdriver.common.touch_action import TouchAction


class Android(PhotoPage):

    def click_take_new_button(self):

        self.switch_context_to_webview()

        logging.info("clicking in Take new button")
        take_new_button = self.driver.find_element(*self.configuration.PhotoScreen.TAKE_NEW_BUTTON)
        self.assertIsNotNone(take_new_button, "Take new button not found")
        take_new_button.click()
        sleep(2)

        self.switch_context_to_native()

        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        platform_version = desired_capabilities.get('platformVersion')
        if platform_version > "6":
            logging.warning("Appium is running on Android >= 6   --it is necessary to allow additional permissions and "
                            "click again 'Take new' button ")

            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.alert_popup_allow()

            try:
                self.switch_context_to_webview()
                logging.info("clicking in Take new button one more time")
                take_new_button = self.driver.find_element(*self.configuration.PhotoScreen.TAKE_NEW_BUTTON)
                take_new_button.click()
                self.switch_context_to_native()
            except NoSuchElementException:
                pass
        else:
            pass
