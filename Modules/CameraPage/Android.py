""" Methods for Android on Camera Page """

from Modules.CameraPage.CameraPage import CameraPage
from selenium.common.exceptions import *
from appium.webdriver.common.touch_action import TouchAction
import logging
from Conf.desired_capabilities import DesiredCapabilities


class Android(CameraPage):

    def capture_photo(self):

        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        # logging.info(desired_capabilities)
        platform_version = desired_capabilities.get('platformVersion')
        # logging.info(platform_version)
        logging.info("capture")
        if platform_version >= "6":
            photo_capture1 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_6)
            self.assertIsNotNone(photo_capture1)
            photo_capture1.click()
        else:
            photo_capture2 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_4_and_5)
            self.assertIsNotNone(photo_capture2)
            photo_capture2.click()
        # try:
        #     photo_capture1 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_6)
        #     self.assertIsNotNone(photo_capture1)
        #     photo_capture1.click()
        # except NoSuchElementException:
        #     photo_capture2 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_4_and_5)
        #     self.assertIsNotNone(photo_capture2)
        #     photo_capture2.click()

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
            use_photo3 = self.driver.find_element(*self.configuration.CameraScreen.USE_PHOTO_ANDROID6)
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
        # try:
        #     use_photo1 = self.driver.find_element(*self.configuration.CameraScreen.USE_PHOTO_ANDROID4)
        #     self.assertIsNotNone(use_photo1)
        #     action = TouchAction(self.driver)
        #     action.tap(element=use_photo1, count=1).perform()
        # except NoSuchElementException:
        #     pass
        # try:
        #     use_photo2 = self.driver.find_element(*self.configuration.CameraScreen.USE_PHOTO_ANDROID5)
        #     self.assertIsNotNone(use_photo2)
        #     action = TouchAction(self.driver)
        #     action.tap(element=use_photo2, count=1).perform()
        # except NoSuchElementException:
        #     pass
        # try:
        #     use_photo3 = self.driver.find_element(*self.configuration.CameraScreen.USE_PHOTO_ANDROID6)
        #     self.assertIsNotNone(use_photo3)
        #     action = TouchAction(self.driver)
        #     action.tap(element=use_photo3, count=1).perform()
        # except NoSuchElementException:
        #     pass

    def click_use_video(self):

        Android.click_use_photo(self)

    def click_retake(self):

        logging.info("Retake")
        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        platform_version = desired_capabilities.get('platformVersion')
        if platform_version >= "6":
            retake_photo_android_6 = self.driver.find_element(*self.configuration.CameraScreen.RETAKE_ANDROID_6)
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
        # try:
        #     retake_photo_android_4 = self.driver.find_element(*self.configuration.CameraScreen.RETAKE_ANDROID_4)
        #     self.assertIsNotNone(retake_photo_android_4)
        #     retake_photo_android_4.click()
        # except NoSuchElementException:
        #     pass
        # try:
        #     retake_photo_android_5 = self.driver.find_element(*self.configuration.CameraScreen.RETAKE_ANDROID_5)
        #     self.assertIsNotNone(retake_photo_android_5)
        #     retake_photo_android_5.click()
        # except NoSuchElementException:
        #     pass
        # try:
        #     retake_photo_android_6 = self.driver.find_element(*self.configuration.CameraScreen.RETAKE_ANDROID_6)
        #     self.assertIsNotNone(retake_photo_android_6)
        #     retake_photo_android_6.click()
        # except NoSuchElementException:
        #     pass

    def choose_camera(self):

        logging.info("click choose camera")
        try:
            chooser_camera = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER)
            self.assertIsNotNone(chooser_camera)
            chooser_camera.click()
        except NoSuchElementException:
            pass
        try:
            chooser_camera2 = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER2)
            self.assertIsNotNone(chooser_camera2)
            chooser_camera2.click()
        except NoSuchElementException:
            pass
        try:
            chooser_camera_for_android_4 = self.driver.find_element(*self.configuration.CameraScreen.
                                                                    CAMERA_CHOOSER_ANDROID4)
            self.assertIsNotNone(chooser_camera_for_android_4)
            chooser_camera_for_android_4.click()
        except NoSuchElementException:
            pass

