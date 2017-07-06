"""A class for methods to handle Camera Page """

from Modules.BasePage.BasePage import BasePage
import logging
from time import sleep
from configuration import platform
from selenium.common.exceptions import *


class CameraPage(BasePage):

    def capture_photo(self):

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):  # iOS emulator can't capture photos but Android emulator can
            logging.info("Appium is running on emulator = skip taking photo because emulators don't "
                         "support that functionality")
            pass
        else:
            logging.info("taking photo")
            photo_capture = self.driver.find_element(*self.configuration.CameraScreen.PHOTO_CAPTURE)
            self.assertIsNotNone(photo_capture, "photo capture button not found")
            photo_capture.click()
            sleep(4)

    def capture_video(self):

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = skip recording video because emulators don't "
                         "support that functionality")
            pass
        else:

            logging.info("record/stop")
            record_new_video = self.driver.find_element(*self.configuration.CameraScreen.VIDEO_CAPTURE)
            self.assertIsNotNone(record_new_video, "video capture button not found")
            record_new_video.click()

    def stop_recording_video(self):

        CameraPage.capture_video(self)  # on iOS start and stop are the same locator

    def click_cancel(self):

        try:
            logging.info("click Cancel")
            cancel = self.driver.find_element(*self.configuration.CameraScreen.CANCEL_BUTTON)
            self.assertIsNotNone(cancel, "Cancel button not found")
            cancel.click()
        except NoSuchElementException:
            logging.info("Cancel button not found")
            pass

    def click_use_photo(self):

        try:
            logging.info("click Use Photo")
            use_photo = self.driver.find_element(*self.configuration.CameraScreen.USE_PHOTO)
            self.assertIsNotNone(use_photo, "Use photo button not found")
            use_photo.click()
        except NoSuchElementException:
            logging.info("Use photo button not found")
            pass
        sleep(1)

    def click_use_video(self):

        try:
            logging.info("click Use Video")
            use_video = self.driver.find_element(*self.configuration.CameraScreen.USE_VIDEO)
            self.assertIsNotNone(use_video, "Use video button not found")
            use_video.click()
            sleep(2)
        except NoSuchElementException:
            logging.info("Use video button not found")
            pass

    def click_retake_photo(self):

        try:
            logging.info("click Retake")
            retake_photo = self.driver.find_element(*self.configuration.CameraScreen.RETAKE)
            self.assertIsNotNone(retake_photo, "Retake button not found")
            retake_photo.click()
        except NoSuchElementException:
            logging.info("Retake button not found")
            pass

    def click_retake_video(self):

        CameraPage.click_retake_photo(self)

    def choose_photo_camera(self):

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = skip choosing camera because emulators don't "
                         "support that functionality")
            pass
        else:
            logging.info("click choose camera")
            chooser_camera = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER)
            self.assertIsNotNone(chooser_camera, "Choose camera button not found")
            chooser_camera.click()
            sleep(1)

    def choose_video_camera(self):

        CameraPage.choose_photo_camera(self)
