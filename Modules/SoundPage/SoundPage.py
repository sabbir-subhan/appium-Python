"""A class for methods to handle Sound Page """

from Modules.BasePage.BasePage import BasePage
import logging


class SoundPage(BasePage):

    def check_if_sound_page_was_opened(self):

        video_page_header = self.driver.find_element(*self.configuration.SoundScreen.SOUND_PAGE_HEADER)
        self.assertIsNotNone(video_page_header, "Sound page header was not found")
        logging.info("Sound page was opened")
