""" Methods for IOS to handle Sound Recorder Page """

from Modules.SoundRecorderPage.SoundRecorderPage import SoundRecorderPage
import logging
from configuration import platform


class IOS(SoundRecorderPage):

    def record_sound(self):

        logging.info("Appium is running on: " + str(platform))

        if "emulator" in str(platform):
            logging.info("Appium is running on emulator = skip recording sound because emulators don't "
                         "support that functionality")
            pass
        else:

            logging.info("click record/stop button")
            sound_capture = self.driver.find_element(*self.configuration.SoundRecorderScreen.RECORD_SOUND)
            self.assertIsNotNone(sound_capture, "sound capture button not found")
            sound_capture.click()

    def stop_recording(self):

        IOS.record_sound(self)

    def click_done_button(self):

        # try:
        logging.info("click click 'Done' button")
        done_button = self.driver.find_element(*self.configuration.SoundRecorderScreen.DONE_BUTTON)
        self.assertIsNotNone(done_button, "Done button not found")
        done_button.click()
        # except:
        #     logging.info("Done button not found")
        #     pass


