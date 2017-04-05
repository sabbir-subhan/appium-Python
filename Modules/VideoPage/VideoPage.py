"""A class for methods to handle Video Page """

from Modules.BasePage.BasePage import BasePage
import logging
from Modules.load_class import LoadClass
from time import sleep
from selenium.webdriver.support import expected_conditions
import selenium.webdriver.support.ui


class VideoPage(BasePage):

    def check_if_video_page_was_opened(self):

        video_page_header = self.driver.find_element(*self.configuration.VideoScreen.VIDEO_PAGE_HEADER)
        self.assertIsNotNone(video_page_header, "Video page header was not found")
        logging.info("Video page was opened")

    def click_gallery_button(self):

        photo_page = LoadClass.load_page('PhotoPage')
        photo_page.setDriver(self.driver)
        photo_page.click_gallery_button()

    def click_send_button(self):

        # photo_page = LoadClass.load_page('PhotoPage')
        # photo_page.setDriver(self.driver)
        # photo_page.click_send_button()

        self.switch_context_to_webview()

        sleep(1)
        logging.info("click 'Send' button")
        send_button = self.driver.find_element(*self.configuration.VideoScreen.SEND_BUTTON)
        self.assertIsNotNone(send_button, "Send button not found")
        send_button.click()

        self.switch_context_to_native()

        sleep(2)
        logging.info("sending file")
        selenium.webdriver.support.ui.WebDriverWait(self.driver, 600).until(
            expected_conditions.presence_of_element_located(self.configuration.MainMenuScreen.EVENTS_BUTTON),
            "Failed to send file")
        logging.info("File was sent")

    def click_record_new_button(self):

        logging.info("clicking in 'Record new' button")
        record_new_button = self.driver.find_element(*self.configuration.VideoScreen.RECORD_NEW_BUTTON)
        self.assertIsNotNone(record_new_button, "record new button not found")
        record_new_button.click()

    def type_description(self, description):

        photo_page = LoadClass.load_page('PhotoPage')
        photo_page.setDriver(self.driver)
        photo_page.type_description(description)






