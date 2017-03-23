"""A class for methods to handle Common Page """

from Modules.BasePage.BasePage import BasePage
import logging
from time import sleep
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from importlib import import_module
from configuration import ENVIRONMENT_TEST


class CommonPage(BasePage):

    def click_device_cancel_button(self):

        logging.info("Click 'Cancel' button")
        cancel_button = self.driver.find_element(*self.configuration.Android.ANDROID_CANCEL_BUTTON)
        self.assertIsNotNone(cancel_button, "Cancel button was not found")
        cancel_button.click()

    def take_screenshot(self, file_name):

        logging.info("taking screenshot")
        sleep(2)
        self.driver.save_screenshot(file_name)

    def reset(self):
        """This method will reset driver - so for example app will be force to logout"""

        logging.info("reset")
        self.driver.reset()

    def click_ok_button(self):

        logging.info("click on 'Ok' button")
        ok_button = self.driver.find_element(*self.configuration.CommonScreen.OK_BUTTON)
        self.assertIsNotNone(ok_button, "Ok button not found")
        ok_button.click()
        sleep(1)

    def wait_for_app_loading(self):

        # on iOS that element have visible: false
        logging.info("wait")
        WebDriverWait(self.driver, 35).until(
            expected_conditions.invisibility_of_element_located(self.configuration.CommonScreen.LOADING),
            "loading animation is present")

    def switch_context_to_webview(self):

        print("switching context")

        self.configuration = import_module('Conf.locators_for_webview')  # NOT WORKING

        current = self.driver.current_context
        print('current context is: ' + current)
        contexts = self.driver.contexts
        print(contexts)
        self.driver.switch_to.context(contexts[1])
        current_after_switch = self.driver.current_context
        print('current context is: ' + current_after_switch)

    def switch_context_to_native(self):

        print("switching context")

        self.configuration = import_module('Conf.locators_' + ENVIRONMENT_TEST)

        current = self.driver.current_context
        print('current context is: ' + current)
        contexts = self.driver.contexts
        print(contexts)
        self.driver.switch_to.context(contexts[0])
        current_after_switch = self.driver.current_context
        print('current context is: ' + current_after_switch)
