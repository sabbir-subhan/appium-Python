"""A class for methods to handle Common Page """

from Modules.BasePage.BasePage import BasePage
import logging
from time import sleep
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import os
from configuration import PROJECT_ROOT
from Modules.load_class import LoadClass
# from importlib import import_module
# from configuration import ENVIRONMENT_TEST
import base64
from appium.webdriver.common.touch_action import TouchAction


class CommonPage(BasePage):

    def swipe_up(self):

        logging.info("swipe up")
        sleep(1)
        window_size = self.driver.get_window_size()  # this returns dictionary
        logging.info(window_size)

        height_max = window_size["height"]

        # print(height_max)
        # print(type(height_max))
        # sleep(2)
        # self.driver.swipe(start_x=50, start_y=height_max, end_x=50, end_y=10, duration=800)
        sleep(1)

        start_x = 50
        start_y = height_max
        end_x = 50
        end_y = height_max * 0.5
        el = self.driver.find_element(*self.configuration.CommonScreen.WEB_VIEW)
        action = TouchAction(self.driver)
        action.press(el, start_x, start_y).wait(100).move_to(el, end_x - start_x, end_y - start_y).release().perform()

    def swipe_down(self):

        logging.info("swipe down")
        sleep(1)

        self.driver.swipe(start_x=50, start_y=0, end_x=50, end_y=200, duration=800)
        sleep(1)

    def push_sample_files(self):  # push sample photo and video files for executing TCs on emulators - not working

        sleep(2)

        logging.info("push video file to the emulator")
        path1 = "sample_video.mp4"
        # path1 = os.path.join(PROJECT_ROOT, "sample_video.mp4")
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
        # self.driver.push_file(path2, "jpeg")
        sleep(5)

        # if "emulator" in platform:
        #     logging.info("push video file to the emulator")
        #     path1 = "sample_video.mp4"
        #     # path1 = os.path.join(PROJECT_ROOT, "sample_video.mp4")
        #     # self.driver.push_file(path, "mp4")
        #     with open(file=path1, mode='rb') as myfile1:
        #         encoded_file = base64.b64encode(myfile1.read())
        #     # We need to decode to get rid of the b'' bytes literal for the upload to work
        #     sleep(1)
        #     self.driver.push_file(path1, encoded_file.decode())
        #     # On the device, the file appears in the correct format
        #     sleep(5)
        #     logging.info("push image file to the emulator")
        #     path2 = os.path.join(PROJECT_ROOT, "sample_image.jpg")
        #     with open(file=path2, mode='rb') as myfile2:
        #         encoded_file = base64.b64encode(myfile2.read())
        #     sleep(1)
        #     self.driver.push_file(path2, encoded_file.decode())
        #     # self.driver.push_file(path2, "jpeg")
        #     sleep(5)
        # else:
        #     pass

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
        sleep(1)
        path = "./screenshots"
        os.chdir(path)
        self.driver.save_screenshot(file_name + ".png")
        os.chdir("..")

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


