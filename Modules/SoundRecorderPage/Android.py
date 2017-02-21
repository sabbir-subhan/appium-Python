""" Methods for Android on Sound Recorder Page """

from Modules.SoundRecorderPage.SoundRecorderPage import SoundRecorderPage
from selenium.common.exceptions import *
import logging


class Android(SoundRecorderPage):

    def record_sound(self):

        logging.info("click record sound")
        try:
            sound_capture_android_6 = self.driver.find_element(*self.configuration.SoundRecorderScreen.
                                                               RECORD_SOUND_android_6)
            if sound_capture_android_6.is_displayed():
                self.assertIsNotNone(sound_capture_android_6, "sound capture button not found")
                sound_capture_android_6.click()
        except NoSuchElementException:
            pass
        try:
            sound_capture_android_5 = self.driver.find_element(*self.configuration.SoundRecorderScreen.
                                                               RECORD_SOUND_android_5)
            if sound_capture_android_5.is_displayed():
                self.assertIsNotNone(sound_capture_android_5, "sound capture button not found")
                sound_capture_android_5.click()
        except NoSuchElementException:
            pass
        try:
            sound_capture_android_4 = self.driver.find_element(*self.configuration.SoundRecorderScreen.
                                                               RECORD_SOUND_android_4)
            if sound_capture_android_4.is_displayed():
                self.assertIsNotNone(sound_capture_android_4, "sound capture button not found")
                sound_capture_android_4.click()
        except NoSuchElementException:
            pass

    def stop_recording(self):

        logging.info("stop recording")
        try:
            stop_recording_android_6 = self.driver.find_element(*self.configuration.SoundRecorderScreen.
                                                                STOP_RECORDING_android_6)
            if stop_recording_android_6.is_displayed():
                self.assertIsNotNone(stop_recording_android_6, "stop recording button not found")
                stop_recording_android_6.click()
        except NoSuchElementException:
            pass
        try:
            stop_recording_android_5 = self.driver.find_element(*self.configuration.SoundRecorderScreen.
                                                                STOP_RECORDING_android_5)
            if stop_recording_android_5.is_displayed():
                self.assertIsNotNone(stop_recording_android_5, "stop recording button not found")
                stop_recording_android_5.click()
        except NoSuchElementException:
            pass
        try:
            stop_recording_android_4 = self.driver.find_element(*self.configuration.SoundRecorderScreen.
                                                                STOP_RECORDING_android_4)
            if stop_recording_android_4.is_displayed():
                self.assertIsNotNone(stop_recording_android_4, "stop recording button not found")
                stop_recording_android_4.click()
        except NoSuchElementException:
            pass

    def click_done_button(self):

        logging.info("click click 'Done' button")
        try:
            done_button_android_6 = self.driver.find_element(*self.configuration.SoundRecorderScreen.
                                                             DONE_BUTTON_android_6)
            if done_button_android_6.is_displayed():
                self.assertIsNotNone(done_button_android_6, "Done button not found")
                done_button_android_6.click()
        except NoSuchElementException:
            pass
        try:
            done_button_android_5 = self.driver.find_element(*self.configuration.SoundRecorderScreen.
                                                             DONE_BUTTON_android_5)
            if done_button_android_5.is_displayed():
                self.assertIsNotNone(done_button_android_5, "Done button not found")
                done_button_android_5.click()
        except NoSuchElementException:
            pass
        try:
            done_button_android_4 = self.driver.find_element(*self.configuration.SoundRecorderScreen.
                                                             DONE_BUTTON_android_4)
            if done_button_android_4.is_displayed():
                self.assertIsNotNone(done_button_android_4, "Done button not found")
                done_button_android_4.click()
        except NoSuchElementException:
            pass

