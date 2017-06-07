"""A class for methods to handle Common Page """

from Modules.BasePage.BasePage import BasePage
import logging
from time import sleep
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import os
from configuration import platform, PROJECT_ROOT
from Modules.load_class import LoadClass
# from importlib import import_module
# from configuration import ENVIRONMENT_TEST
import base64


class CommonPage(BasePage):

    def push_files(self):  # not working

        sleep(2)
        if "emulator" in platform:
            logging.info("push video file to the emulator")
            path1 = os.path.join(PROJECT_ROOT, "sample_video.mp4")
            # self.driver.push_file(path, "mp4")
            with open(file=path1, mode='rb') as myfile1:
                encoded_file = base64.b64encode(myfile1.read())
            # We need to decode to get rid of the b'' bytes literal for the upload to work
            sleep(1)
            self.driver.push_file(path1, encoded_file.decode())
            # On the device, the file appears in the correct format
            sleep(5)
            logging.info("push image file to the emulator")
            path2 = os.path.join(PROJECT_ROOT, "sample_image.jpg")
            with open(file=path2, mode='rb') as myfile2:
                encoded_file = base64.b64encode(myfile2.read())
            sleep(1)
            self.driver.push_file(path2, encoded_file.decode())
            # self.driver.push_file(path2, "jpg")
            sleep(5)
        else:
            pass

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

        # logging.info("wait for app loading")
        WebDriverWait(self.driver, 20).until(
            expected_conditions.invisibility_of_element_located(self.configuration.CommonScreen.LOADING),
            "app is still loading - check internet connection")




