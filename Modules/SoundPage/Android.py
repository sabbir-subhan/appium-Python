""" Methods for Android on Sound Page """

from Modules.SoundPage.SoundPage import SoundPage
from selenium.common.exceptions import *
import logging


class Android(SoundPage):

    def click_record_sound_icon(self):

        logging.info("clicking in 'Record Sound' icon")
        try:
            record_sound_button = self.driver.find_element(*self.configuration.SoundScreen.RECORD_SOUND_BUTTON)
            if record_sound_button.is_displayed():
                self.assertIsNotNone(record_sound_button, "record sound button not found")
                record_sound_button.click()
        except NoSuchElementException:
            self.fail("failed to click 'Record Sound'")

