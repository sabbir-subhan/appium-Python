"""A class for methods to handle Sound Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
import logging


class SoundPage(BasePage):

    def check_if_sound_page_was_opened(self):

        video_page_header = self.driver.find_element(*self.configuration.SoundScreen.SOUND_PAGE_HEADER)
        self.assertIsNotNone(video_page_header, "Sound page header was not found")
        logging.info("Sound page was opened")

    def type_description(self, description):

        welcome_page = LoadClass.load_page('PhotoPage')
        welcome_page.setDriver(self.driver)
        welcome_page.type_description(description)

    def click_send_button(self):

        welcome_page = LoadClass.load_page('PhotoPage')
        welcome_page.setDriver(self.driver)
        welcome_page.click_send_button()
