""" Methods for Android on Sound Recorder Page """

from Modules.SoundRecorderPage.SoundRecorderPage import SoundRecorderPage
import logging
from Conf.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import *
from configuration import platform


class Android(SoundRecorderPage):

    def record_sound(self):

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = skip recording sound because emulators don't "
                         "support that functionality")
            pass
        else:
            logging.info("click record button")

            desired_capabilities = DesiredCapabilities.get_desired_capabilities()
            platform_version = desired_capabilities.get('platformVersion')
            if platform_version >= "6":
                try:
                    sound_capture_android_6 = self.driver.find_element(*self.configuration.SoundRecorderScreen.
                                                                       RECORD_SOUND_android_6)
                except NoSuchElementException:
                    sound_capture_android_6 = self.driver.find_element(*self.configuration.SoundRecorderScreen.
                                                                       RECORD_SOUND_android_6_version2)
                self.assertIsNotNone(sound_capture_android_6, "sound capture button not found")
                sound_capture_android_6.click()
            elif platform_version < "5":
                sound_capture_android_4 = self.driver.find_element(*self.configuration.SoundRecorderScreen.
                                                                   RECORD_SOUND_android_4)
                self.assertIsNotNone(sound_capture_android_4, "sound capture button not found")
                sound_capture_android_4.click()
            else:
                sound_capture_android_5 = self.driver.find_element(*self.configuration.SoundRecorderScreen.
                                                                   RECORD_SOUND_android_5)
                self.assertIsNotNone(sound_capture_android_5, "sound capture button not found")
                sound_capture_android_5.click()

    def stop_recording(self):

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = skip recording sound because emulators don't "
                         "support that functionality")
            pass
        else:
            logging.info("stop recording")
            desired_capabilities = DesiredCapabilities.get_desired_capabilities()
            platform_version = desired_capabilities.get('platformVersion')
            if platform_version >= "6":
                stop_recording_android_6 = self.driver.find_element(*self.configuration.SoundRecorderScreen.
                                                                    STOP_RECORDING_android_6)
                self.assertIsNotNone(stop_recording_android_6, "stop recording button not found")
                stop_recording_android_6.click()
            elif platform_version < "5":
                stop_recording_android_4 = self.driver.find_element(*self.configuration.SoundRecorderScreen.
                                                                    STOP_RECORDING_android_4)
                self.assertIsNotNone(stop_recording_android_4, "stop recording button not found")
                stop_recording_android_4.click()
            else:
                stop_recording_android_5 = self.driver.find_element(*self.configuration.SoundRecorderScreen.
                                                                    STOP_RECORDING_android_5)
                self.assertIsNotNone(stop_recording_android_5, "stop recording button not found")
                stop_recording_android_5.click()

    def click_done_button(self):

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = skip recording sound because emulators don't "
                         "support that functionality")
            pass
        else:
            logging.info("click 'Done' button")
            desired_capabilities = DesiredCapabilities.get_desired_capabilities()
            platform_version = desired_capabilities.get('platformVersion')
            if platform_version >= "6":
                done_button_android_6 = self.driver.find_element(*self.configuration.SoundRecorderScreen.
                                                                 DONE_BUTTON_android_6)
                self.assertIsNotNone(done_button_android_6, "Done button not found")
                done_button_android_6.click()
            elif platform_version < "5":
                done_button_android_4 = self.driver.find_element(*self.configuration.SoundRecorderScreen.
                                                                 DONE_BUTTON_android_4)
                self.assertIsNotNone(done_button_android_4, "Done button not found")
                done_button_android_4.click()
            else:
                done_button_android_5 = self.driver.find_element(*self.configuration.SoundRecorderScreen.
                                                                 DONE_BUTTON_android_5)
                self.assertIsNotNone(done_button_android_5, "Done button not found")
                done_button_android_5.click()


