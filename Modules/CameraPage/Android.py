""" Methods for Android on Camera Page """

from Modules.CameraPage.CameraPage import CameraPage
import logging
from Conf.desired_capabilities import DesiredCapabilities
from time import sleep
from selenium.common.exceptions import *
from configuration import platform
from appium.webdriver.common.touch_action import TouchAction
from distutils.version import LooseVersion


class Android(CameraPage):

    def capture_photo(self):

        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        platform_version = desired_capabilities.get('platformVersion')
        logging.info("capture")
        # sleep(4)
        action = TouchAction(self.driver)
        if LooseVersion(platform_version) > LooseVersion("6"):  # platform_version > "6":
            try:
                photo_capture1 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_6)
            except NoSuchElementException:
                photo_capture1 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_6_version2)
            self.assertIsNotNone(photo_capture1)
            # photo_capture1.click()
            action.tap(element=photo_capture1, count=1).perform()
            # sleep(4)
        else:
            try:
                photo_capture3 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_4_and_5)  # also for Android 6
            except NoSuchElementException:
                photo_capture3 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_6_version2)
            self.assertIsNotNone(photo_capture3)
            action.tap(element=photo_capture3, count=1).perform()
            # photo_capture3.click()
            # sleep(4)

        # if platform_version > "5" and "6" in str(platform_version):
        #     try:
        #         photo_capture1 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_6)
        #     except NoSuchElementException:
        #         photo_capture1 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_6_version2)
        #     self.assertIsNotNone(photo_capture1)
        #     photo_capture1.click()
        # elif platform_version >= "7":
        #     sleep(2)
        #     photo_capture2 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_6)
        #     self.assertIsNotNone(photo_capture2)
        #     sleep(4)
        #     photo_capture2.click()
        #     sleep(4)
        # else:
        #     photo_capture3 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_4_and_5)
        #     self.assertIsNotNone(photo_capture3)
        #     photo_capture3.click()
        # sleep(2)

    def capture_video(self):

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = skip recording video because emulators don't "
                         "support that functionality")
            pass
        else:
            desired_capabilities = DesiredCapabilities.get_desired_capabilities()
            platform_version = desired_capabilities.get('platformVersion')
            logging.info("start recording")
            # sleep(4)
            if LooseVersion("5") < LooseVersion(platform_version) < LooseVersion("7"):  # platform_version > "5" and "6" in str(platform_version):
                try:
                    video_capture1 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_6)
                except NoSuchElementException:
                    video_capture1 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_6_version2)
                self.assertIsNotNone(video_capture1, "video capture for Android 6 not found")
                video_capture1.click()
            elif LooseVersion(platform_version) >= LooseVersion("7"):  # platform_version >= "7":
                # sleep(2)
                video_capture2 = self.driver.find_element(*self.configuration.CameraScreen.RECORD_BUTTON_ANDROID_7)
                self.assertIsNotNone(video_capture2, "video capture for Android 7 not found")
                # sleep(4)
                video_capture2.click()
                # sleep(4)
            else:
                # sleep(1)
                video_capture3 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_4_and_5)
                self.assertIsNotNone(video_capture3, "video capture for Android 4, 5 not found")
                video_capture3.click()
            # sleep(2)

    def stop_recording_video(self):

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = skip recording video because emulators don't "
                         "support that functionality")
            pass
        else:
            desired_capabilities = DesiredCapabilities.get_desired_capabilities()
            platform_version = desired_capabilities.get('platformVersion')
            logging.info("stop recording")
            # sleep(4)
            if LooseVersion("5") < LooseVersion(platform_version) < LooseVersion("7"):  # platform_version > "5" and "6" in str(platform_version):
                try:
                    stop_recording1 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_6)
                except NoSuchElementException:
                    stop_recording1 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_6_version2)
                self.assertIsNotNone(stop_recording1, "video stop recording for Android 6 not found")
                stop_recording1.click()
            elif LooseVersion(platform_version) >= LooseVersion("7"):  # platform_version >= "7":
                # sleep(2)
                stop_recording2 = self.driver.find_element(*self.configuration.CameraScreen.STOP_BUTTON_ANDROID_7)
                self.assertIsNotNone(stop_recording2, "video stop recording for Android 7 not found")
                # sleep(4)
                stop_recording2.click()
                # sleep(4)
            else:
                stop_recording3 = self.driver.find_element(*self.configuration.CameraScreen.CAPTURE_BUTTON_ANDROID_4_and_5)
                self.assertIsNotNone(stop_recording3, "video stop recording for Android 4, 5 not found")
                stop_recording3.click()
            # sleep(2)

    def click_cancel(self):

        logging.info("click Cancel")
        cancel = self.driver.find_element(*self.configuration.CameraScreen.CANCEL_PHOTO_BUTTON)
        self.assertIsNotNone(cancel)
        cancel.click()

    def click_use_photo(self):

        logging.info("Use")

        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        platform_version = desired_capabilities.get('platformVersion')
        action = TouchAction(self.driver)
        # sleep(1)
        if LooseVersion("6") <= LooseVersion(platform_version) < LooseVersion("7"):  # platform_version >= "6" and platform_version < "7":
            logging.info("Use - Android >= 6 and < 7")
            use_photo3 = self.driver.find_element(*self.configuration.CameraScreen.USE_PHOTO_ANDROID6)
            self.assertIsNotNone(use_photo3)
            # use_photo3.click()
            action.tap(element=use_photo3, count=1).perform()
            # sleep(1)
            # try:
            #     use_photo3 = self.driver.find_element(*self.configuration.CameraScreen.USE_PHOTO_ANDROID6)
            # except NoSuchElementException:
            #     use_photo3 = self.driver.find_element(*self.configuration.CameraScreen.USE_PHOTO_ANDROID6_version2)
            # self.assertIsNotNone(use_photo3)
            # action.tap(element=use_photo3, count=1).perform()
        elif LooseVersion(platform_version) >= LooseVersion("7"):  # platform_version >= "7":
            logging.info("Use - Android > 7")
            use_photo4 = self.driver.find_element(*self.configuration.CameraScreen.USE_PHOTO_ANDROID7)
            self.assertIsNotNone(use_photo4)
            # use_photo4.click()
            action.tap(element=use_photo4, count=1).perform()
            # sleep(1)
        elif LooseVersion("5") <= LooseVersion(platform_version) < LooseVersion("6"):  # platform_version >= "5" and platform_version < "6":
            logging.info("Use - Android >= 5 and < 6")
            try:
                use_photo2 = self.driver.find_element(*self.configuration.CameraScreen.USE_PHOTO_ANDROID5)
            except NoSuchElementException:
                use_photo2 = self.driver.find_element(*self.configuration.CameraScreen.USE_PHOTO_ANDROID6)
            self.assertIsNotNone(use_photo2)
            # use_photo2.click()
            action.tap(element=use_photo2, count=1).perform()
            # sleep(1)
        else:
            logging.info("Use - Android < 5")
            use_photo1 = self.driver.find_element(*self.configuration.CameraScreen.USE_PHOTO_ANDROID4)
            self.assertIsNotNone(use_photo1)
            # use_photo1.click()
            action.tap(element=use_photo1, count=1).perform()
        #     sleep(1)
        # sleep(4)

    def click_use_video(self):

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = skip recording video because emulators don't "
                         "support that functionality")
            pass
        else:
            Android.click_use_photo(self)

    def click_retake_photo(self):

        logging.info("Retake")
        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        platform_version = desired_capabilities.get('platformVersion')
        if LooseVersion(platform_version) >= LooseVersion("6"):  # platform_version >= "6":
            try:
                retake_photo_android_6 = self.driver.find_element(*self.configuration.CameraScreen.RETAKE_ANDROID_6)
            except NoSuchElementException:
                retake_photo_android_6 = self.driver.find_element(*self.configuration.CameraScreen.RETAKE_ANDROID_6_version2)
            self.assertIsNotNone(retake_photo_android_6)
            retake_photo_android_6.click()
        elif LooseVersion(platform_version) < LooseVersion("5"):  # platform_version < "5":
            retake_photo_android_4 = self.driver.find_element(*self.configuration.CameraScreen.RETAKE_ANDROID_4)
            self.assertIsNotNone(retake_photo_android_4)
            retake_photo_android_4.click()
        else:
            try:
                retake_photo_android_5 = self.driver.find_element(*self.configuration.CameraScreen.RETAKE_ANDROID_5)
            except NoSuchElementException:
                retake_photo_android_5 = self.driver.find_element(*self.configuration.CameraScreen.RETAKE_ANDROID_5_emulator)
            self.assertIsNotNone(retake_photo_android_5)
            retake_photo_android_5.click()

    def click_retake_video(self):

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = skip recording video because emulators don't "
                         "support that functionality")
            pass
        else:
            logging.info("Retake")
            desired_capabilities = DesiredCapabilities.get_desired_capabilities()
            platform_version = desired_capabilities.get('platformVersion')
            if LooseVersion(platform_version) >= LooseVersion("6"):  # platform_version >= "6":
                try:
                    retake_photo_android_6 = self.driver.find_element(*self.configuration.CameraScreen.RETAKE_ANDROID_6)
                except NoSuchElementException:
                    retake_photo_android_6 = self.driver.find_element(*self.configuration.CameraScreen.RETAKE_ANDROID_6_version2)
                self.assertIsNotNone(retake_photo_android_6)
                retake_photo_android_6.click()
            elif LooseVersion(platform_version) < LooseVersion("5"):  # platform_version < "5":
                retake_photo_android_4 = self.driver.find_element(*self.configuration.CameraScreen.RETAKE_ANDROID_4)
                self.assertIsNotNone(retake_photo_android_4)
                retake_photo_android_4.click()
            else:
                retake_photo_android_5 = self.driver.find_element(*self.configuration.CameraScreen.RETAKE_ANDROID_5)
                self.assertIsNotNone(retake_photo_android_5)
                retake_photo_android_5.click()

    def choose_photo_camera(self):

        logging.info("click choose camera")

        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        platform_version = desired_capabilities.get('platformVersion')
        if LooseVersion("5") < LooseVersion(platform_version) < LooseVersion("6"):  # platform_version > "5" and platform_version < "6":
            try:
                chooser_camera_android = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER_ANDROID5)
            except NoSuchElementException:
                chooser_camera_android = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER_ANDROID_6)
            self.assertIsNotNone(chooser_camera_android)
            chooser_camera_android.click()
        elif LooseVersion(platform_version) < LooseVersion("5"):  # platform_version < "5":
            chooser_camera_android4 = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER_ANDROID4)
            self.assertIsNotNone(chooser_camera_android4)
            chooser_camera_android4.click()
        elif LooseVersion(platform_version) >= LooseVersion("7"):  # platform_version >= "7":
            chooser_camera_android = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER_ANDROID7)
            self.assertIsNotNone(chooser_camera_android)
            chooser_camera_android.click()
        else:
            try:
                chooser_camera_android = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER_ANDROID6)
            except NoSuchElementException:
                chooser_camera_android = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER_ANDROID_6)
            self.assertIsNotNone(chooser_camera_android)
            chooser_camera_android.click()
        # sleep(1)

    def choose_video_camera(self):

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = skip choosing camera because emulators don't "
                         "support that functionality")
            pass
        else:
            logging.info("click choose camera")
            desired_capabilities = DesiredCapabilities.get_desired_capabilities()
            platform_version = desired_capabilities.get('platformVersion')
            if LooseVersion(platform_version) >= LooseVersion("7"):  # platform_version >= "7":
                chooser_camera_android7 = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER_ANDROID7)
                self.assertIsNotNone(chooser_camera_android7)
                chooser_camera_android7.click()
            elif LooseVersion("5") < LooseVersion(platform_version) < LooseVersion("7"):  # platform_version > "5" and "6" in str(platform_version):
                try:
                    chooser_camera_android6 = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER_ANDROID6)
                except NoSuchElementException:
                    chooser_camera_android6 = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER_ANDROID_6)
                self.assertIsNotNone(chooser_camera_android6)
                chooser_camera_android6.click()
            elif LooseVersion(platform_version) < LooseVersion("7"):  # platform_version < "5":
                chooser_camera_android4 = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER_ANDROID4)
                self.assertIsNotNone(chooser_camera_android4)
                chooser_camera_android4.click()
            else:
                chooser_camera_android5 = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER_ANDROID5)
                self.assertIsNotNone(chooser_camera_android5)
                chooser_camera_android5.click()


