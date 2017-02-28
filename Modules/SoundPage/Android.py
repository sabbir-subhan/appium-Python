""" Methods for Android on Sound Page """

from Modules.SoundPage.SoundPage import SoundPage
import logging


class Android(SoundPage):

    def click_record_sound_icon(self):

        logging.info("clicking in 'Record Sound' icon")
        record_sound_button = self.driver.find_element(*self.configuration.SoundScreen.RECORD_SOUND_BUTTON)
        if record_sound_button.is_displayed():
            self.assertIsNotNone(record_sound_button, "record sound button not found")
            record_sound_button.click()


