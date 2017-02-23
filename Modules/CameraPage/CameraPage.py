"""A class for methods to handle Camera Page """

from Modules.BasePage.BasePage import BasePage
import logging
from time import sleep


class CameraPage(BasePage):

    def capture_photo(self):

        logging.info("taking photo")
        photo_capture = self.driver.find_element(*self.configuration.CameraScreen.PHOTO_CAPTURE)
        self.assertIsNotNone(photo_capture, "photo capture button not found")
        photo_capture.click()
        sleep(4)

    def capture_video(self):

        logging.info("recording new video")
        record_new_video = self.driver.find_element(*self.configuration.CameraScreen.VIDEO_CAPTURE)
        self.assertIsNotNone(record_new_video, "video capture button not found")
        record_new_video.click()

    def click_cancel(self):

        logging.info("click Cancel")
        cancel = self.driver.find_element(*self.configuration.CameraScreen.CANCEL_BUTTON)
        self.assertIsNotNone(cancel, "Cancel button not found")
        cancel.click()

    def click_use_photo(self):

        logging.info("click Use Photo")
        use_photo = self.driver.find_element(*self.configuration.CameraScreen.USE_PHOTO)
        self.assertIsNotNone(use_photo, "Use photo button not found")
        use_photo.click()

    def click_use_video(self):

        logging.info("click Use Video")
        use_video = self.driver.find_element(*self.configuration.CameraScreen.USE_VIDEO)
        self.assertIsNotNone(use_video, "Use video button not found")
        use_video.click()
        sleep(2)

    def click_retake(self):

        logging.info("click Retake")
        retake_photo = self.driver.find_element(*self.configuration.CameraScreen.RETAKE)
        self.assertIsNotNone(retake_photo, "Retake button not found")
        retake_photo.click()

    def choose_camera(self):

        logging.info("click choose camera")
        chooser_camera = self.driver.find_element(*self.configuration.CameraScreen.CAMERA_CHOOSER)
        self.assertIsNotNone(chooser_camera, "Choose camera button not found")
        chooser_camera.click()


