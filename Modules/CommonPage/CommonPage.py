"""A class for methods to handle Common Page """

from Modules.BasePage.BasePage import BasePage
import logging
from time import sleep
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import os
from Modules.load_class import LoadClass
from configuration import platform
from configuration import PROJECT_ROOT
from selenium.common.exceptions import NoSuchElementException


class CommonPage(BasePage):

    def back_arrow(self):

        self.switch_context_to_webview()

        logging.info("click back arrow")

        back_arrow = self.driver.find_element(*self.configuration.TopBar.BACK_ARROW)
        self.assertIsNotNone(back_arrow, "back arrow not found")
        back_arrow.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    def hamburger_button(self):

        self.switch_context_to_webview()

        sleep(1)
        logging.info("click hamburger button to go back to main menu")

        hamburger_button = self.driver.find_element(*self.configuration.TopBar.HAMBURGER_FOR_MAIN_MENU)
        hamburger_button.click()

        sleep(5)

        self.switch_context_to_native()

    def click_device_cancel_button(self):

        logging.info("Click 'Cancel' button")
        cancel_button = self.driver.find_element(*self.configuration.Android.ANDROID_CANCEL_BUTTON)
        self.assertIsNotNone(cancel_button, "Cancel button was not found")
        cancel_button.click()

    def take_screenshot(self, file_name):  # pass file name to this method, without extension

        logging.info("taking screenshot")
        sleep(1)
        path = PROJECT_ROOT + "/screenshots"
        os.chdir(path)
        self.driver.save_screenshot(file_name + ".png")
        sleep(1)
        os.chdir("..")
        sleep(2)

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

    # def wait_for_app_loading(self):
    #
    #     # logging.info("wait for app loading")
    #     sleep(1)
    #     platform_for_test = str(platform)
    #     if "emulator" in platform_for_test:
    #         sleep(5)
    #     else:
    #         pass
    #     WebDriverWait(self.driver, 25).until(
    #         expected_conditions.invisibility_of_element_located(self.configuration.CommonScreen.LOADING),
    #         "app is still loading - check internet connection")

    def wait_for_app_loading(self):

        sleep(1)

        self.switch_context_to_webview()

        try:
            loading_animation = self.driver.find_element(*self.configuration.CommonScreen.LOADING)
            while loading_animation.is_displayed():
                logging.info("wait for app loading")
                sleep(2)
        except NoSuchElementException:
            logging.info("loading animation not found")
            pass

        self.switch_context_to_native()

    # def additional_wait_for_emulators_in_airplane_mode(self):  # android emulator in airplane mode need a long time to load offline object lists
    #
    #     platform_for_test = str(platform)
    #     if "emulator" in platform_for_test:
    #         logging.info("wait for app loading")
    #
    #         # while expected_conditions.visibility_of_element_located(self.configuration.CommonScreen.LOADING):  # not working
    #         #     logging.info("inside while")
    #         #     try:
    #         #         logging.info("inside try")
    #         #         self.driver.find_element(*self.configuration.CommonScreen.LOADING)
    #         #     except NoSuchElementException:
    #         #         break
    #         #     sleep(2)
    #         #     logging.info("after sleep")
    #         #     if expected_conditions.invisibility_of_element_located(self.configuration.CommonScreen.LOADING):  # looks like this condition is not working properly
    #         #         break
    #         #     else:
    #         #         logging.info("waiting")
    #         #         continue
    #         # logging.info("after while loop")
    #
    #         self.switch_context_to_webview()
    #
    #         try:
    #             loading_animation = self.driver.find_element(*self.configuration.CommonScreen.LOADING)
    #             while loading_animation.is_displayed():
    #                 logging.info("waiting")
    #                 sleep(2)
    #         except NoSuchElementException:
    #             logging.info("loading animation not found")
    #             pass
    #
    #         self.switch_context_to_native()
    #         sleep(1)


