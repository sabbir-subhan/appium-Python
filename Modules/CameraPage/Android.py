""" Methods for Android on Camera Page """

from Modules.CameraPage.CameraPage import CameraPage
from appium.webdriver.common.touch_action import TouchAction
import logging
from Conf.desired_capabilities import DesiredCapabilities
from time import sleep
from selenium.common.exceptions import *


class Android(CameraPage):

    def capture_photo(self):

        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        # logging.info(desired_capabilities)
        platform_version = desired_capabilities.get('platformVersion')
        # logging.info(platform_version)
        logging.info("capture")
        sleep(4)
        if platform_version >= "6":
            try:
                photo_capture1 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_6)
            except NoSuchElementException:
                photo_capture1 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_6_version2)
            self.assertIsNotNone(photo_capture1)
            photo_capture1.click()
        elif platform_version >= "7":
            sleep(2)
            photo_capture2 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_6)
            self.assertIsNotNone(photo_capture2)
            sleep(4)
            photo_capture2.click()
            sleep(4)
        else:
            photo_capture3 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_4_and_5)
            self.assertIsNotNone(photo_capture3)
            photo_capture3.click()
        sleep(2)

    def capture_video(self):

        Android.capture_photo(self)

    def click_cancel(self):

        logging.info("click Cancel")
        cancel = self.driver.find_element(*self.configuration.CameraScreen.CANCEL_PHOTO_BUTTON)
        self.assertIsNotNone(cancel)
        cancel.click()

    def click_use_photo(self):

        logging.info("Use")

        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        platform_version = desired_capabilities.get('platformVersion')
        if platform_version >= "6":
            try:
                use_photo3 = self.driver.find_element(*self.configuration.CameraScreen.USE_PHOTO_ANDROID6)
            except NoSuchElementException:
                use_photo3 = self.driver.find_element(*self.configuration.CameraScreen.USE_PHOTO_ANDROID6_version2)
            self.assertIsNotNone(use_photo3)
            action = TouchAction(self.driver)
            action.tap(element=use_photo3, count=1).perform()
        elif platform_version < "5":
            use_photo1 = self.driver.find_element(*self.configuration.CameraScreen.USE_PHOTO_ANDROID4)
            self.assertIsNotNone(use_photo1)
            action = TouchAction(self.driver)
            action.tap(element=use_photo1, count=1).perform()
        else:
            use_photo2 = self.driver.find_element(*self.configuration.CameraScreen.USE_PHOTO_ANDROID5)
            self.assertIsNotNone(use_photo2)
            action = TouchAction(self.driver)
            action.tap(element=use_photo2, count=1).perform()
        sleep(5)

    def click_use_video(self):

        Android.click_use_photo(self)

    def click_retake(self):

        logging.info("Retake")
        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        platform_version = desired_capabilities.get('platformVersion')
        if platform_version >= "6":
            try:
                retake_photo_android_6 = self.driver.find_element(*self.configuration.CameraScreen.RETAKE_ANDROID_6)
            except NoSuchElementException:
                retake_photo_android_6 = self.driver.find_element(*self.configuration.CameraScreen.RETAKE_ANDROID_6_version2)
            self.assertIsNotNone(retake_photo_android_6)
            retake_photo_android_6.click()
        elif platform_version < "5":
            retake_photo_android_4 = self.driver.find_element(*self.configuration.CameraScreen.RETAKE_ANDROID_4)
            self.assertIsNotNone(retake_photo_android_4)
            retake_photo_android_4.click()
        else:
            retake_photo_android_5 = self.driver.find_element(*self.configuration.CameraScreen.RETAKE_ANDROID_5)
            self.assertIsNotNone(retake_photo_android_5)
            retake_photo_android_5.click()

    def choose_camera(self):

        logging.info("click choose camera")
        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        platform_version = desired_capabilities.get('platformVersion')
        if platform_version >= "7":
            chooser_camera_android7 = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER_ANDROID7)
            self.assertIsNotNone(chooser_camera_android7)
            chooser_camera_android7.click()
        elif platform_version > "5" and "6" in str(platform_version):
            try:
                chooser_camera_android6 = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER_ANDROID6)
            except NoSuchElementException:
                chooser_camera_android6 = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER_ANDROID_6)
            self.assertIsNotNone(chooser_camera_android6)
            chooser_camera_android6.click()
        elif platform_version < "5":
            chooser_camera_android4 = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER_ANDROID4)
            self.assertIsNotNone(chooser_camera_android4)
            chooser_camera_android4.click()
        else:
            chooser_camera_android5 = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER_ANDROID5)
            self.assertIsNotNone(chooser_camera_android5)
            chooser_camera_android5.click()


