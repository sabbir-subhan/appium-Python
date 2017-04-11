"""A class for methods to handle Video Page """

from Modules.BasePage.BasePage import BasePage
import logging
from Modules.load_class import LoadClass
from time import sleep
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.ui


class VideoPage(BasePage):

    def check_if_video_page_was_opened(self):

        video_page_header = self.driver.find_element(*self.configuration.VideoScreen.VIDEO_PAGE_HEADER)
        self.assertIsNotNone(video_page_header, "Video page header was not found")
        logging.info("Video page was opened")

    def click_gallery_button(self):

        self.switch_context_to_webview()

        logging.info("click in Gallery button")
        gallery_button = self.driver.find_element(*self.configuration.VideoScreen.GALLERY_BUTTON)
        self.assertIsNotNone(gallery_button, "Gallery button not found")
        gallery_button.click()

        self.switch_context_to_native()

    def click_send_button(self):

        sleep(1)

        self.switch_context_to_webview()

        logging.info("click 'Send' button")
        send_button = self.driver.find_element(*self.configuration.VideoScreen.SEND_BUTTON)
        self.assertIsNotNone(send_button, "Send button not found")
        send_button.click()
        sleep(2)

        self.switch_context_to_native()

        logging.info("sending file")
        WebDriverWait(self.driver, 720).until(
            expected_conditions.presence_of_element_located(self.configuration.MainMenuScreen.INBOX_BUTTON),
            "Failed to send file")
        logging.info("File was sent")

    def click_record_new_button(self):

        self.switch_context_to_webview()

        logging.info("clicking in 'Record new' button")
        record_new_button = self.driver.find_element(*self.configuration.VideoScreen.RECORD_NEW_BUTTON)
        self.assertIsNotNone(record_new_button, "record new button not found")
        record_new_button.click()

        self.switch_context_to_native()

    def type_description(self, description):

        self.switch_context_to_webview()

        sleep(1)
        WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located(self.configuration.VideoScreen.DESCRIPTION_FIELD),
            "Failed to locate description field")
        logging.info("type text into description field")
        description_field = self.driver.find_element(*self.configuration.VideoScreen.DESCRIPTION_FIELD)
        self.assertIsNotNone(description_field, "Description field not found")

        description_field.click()
        description_field.send_keys(description)

        self.switch_context_to_native()

        sleep(1)






