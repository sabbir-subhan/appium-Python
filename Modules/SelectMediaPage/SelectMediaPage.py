"""A class for methods to handle Select Media Page """

from Modules.BasePage.BasePage import BasePage
import logging
from time import sleep
from configuration import platform
# from selenium.common.exceptions import *


class SelectMediaPage(BasePage):

    def click_take_photo(self):

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = skip taking photo because emulators don't "
                         "support that functionality")
            pass
        else:

            self.switch_context_to_webview()

            logging.info("clicking in Take Photo")
            take_photo = self.driver.find_element(*self.configuration.SelectMediaScreen.TAKE_PHOTO)
            self.assertIsNotNone(take_photo, "Take Photo button not found")
            take_photo.click()
            sleep(2)

            self.switch_context_to_native()

    def click_record_video(self):

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = skip recording video because emulators don't "
                         "support that functionality")
            pass
        else:

            self.switch_context_to_webview()

            logging.info("clicking in Record Video")
            click_record_video = self.driver.find_element(*self.configuration.SelectMediaScreen.RECORD_VIDEO)
            self.assertIsNotNone(click_record_video, "Record Video button not found")
            click_record_video.click()
            sleep(2)

            self.switch_context_to_native()

    def click_record_audio(self):

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = skip recording video because emulators don't "
                         "support that functionality")
            pass
        else:

            self.switch_context_to_webview()

            logging.info("clicking in Record Audio")
            click_record_audio = self.driver.find_element(*self.configuration.SelectMediaScreen.RECORD_AUDIO)
            self.assertIsNotNone(click_record_audio, "Record Audio button not found")
            click_record_audio.click()
            sleep(2)

            self.switch_context_to_native()

    def click_video_gallery(self):

        self.switch_context_to_webview()

        logging.info("clicking in Video Gallery")
        video_gallery = self.driver.find_element(*self.configuration.SelectMediaScreen.VIDEO_GALLERY)
        self.assertIsNotNone(video_gallery, "Video Gallery button not found")
        video_gallery.click()
        sleep(2)

        self.switch_context_to_native()

    def click_photo_gallery(self):

        self.switch_context_to_webview()

        logging.info("clicking in Photo Gallery")
        photo_gallery = self.driver.find_element(*self.configuration.SelectMediaScreen.PHOTO_GALLERY)
        self.assertIsNotNone(photo_gallery, "Photo Gallery button not found")
        photo_gallery.click()
        sleep(2)

        self.switch_context_to_native()

