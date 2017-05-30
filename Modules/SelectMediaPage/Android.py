""" Methods for Android on Select Media Page """

from Modules.SelectMediaPage.SelectMediaPage import SelectMediaPage
from time import sleep
import logging
# from appium.webdriver.common.touch_action import TouchAction
# from Conf.desired_capabilities import DesiredCapabilities
# from selenium.common.exceptions import *
# from configuration import platform


class Android(SelectMediaPage):

    def click_take_photo(self):

        self.switch_context_to_webview()

        logging.info("clicking in Take Photo")
        take_photo = self.driver.find_element(*self.configuration.SelectMediaScreen.TAKE_PHOTO)
        self.assertIsNotNone(take_photo, "Take Photo button not found")
        take_photo.click()
        sleep(2)

        self.switch_context_to_native()