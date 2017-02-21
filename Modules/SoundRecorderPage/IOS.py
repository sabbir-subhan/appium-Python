""" Methods for IOS to handle Sound Recorder Page """

from Modules.SoundRecorderPage.SoundRecorderPage import SoundRecorderPage
import logging


class IOS(SoundRecorderPage):

    def record_sound(self):

        logging.info("click record sound")
        sound_capture = self.driver.find_element(*self.configuration.SoundRecorderScreen.RECORD_SOUND)
        self.assertIsNotNone(sound_capture, "sound capture button not found")
        sound_capture.click()

    def click_done_button(self):

        logging.info("click click 'Done' button")
        done_button = self.driver.find_element(*self.configuration.SoundRecorderScreen.DONE_BUTTON)
        self.assertIsNotNone(done_button, "Done button not found")
        done_button.click()

