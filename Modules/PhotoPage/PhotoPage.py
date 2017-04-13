"""A class for methods to handle Photo Page """

from Modules.BasePage.BasePage import BasePage
import logging
from time import sleep
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class PhotoPage(BasePage):

    def check_if_photo_page_was_opened(self):

        photo_page_header = self.driver.find_element(*self.configuration.PhotoScreen.PHOTO_PAGE_HEADER)
        self.assertIsNotNone(photo_page_header, "Photo page header was not found")
        logging.info("Photo page was opened")

    def type_description(self, description):

        self.switch_context_to_webview()

        WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located(self.configuration.PhotoScreen.DESCRIPTION_FIELD),
            "Failed to locate description field")
        logging.info("type text into description field")
        description_field = self.driver.find_element(*self.configuration.PhotoScreen.DESCRIPTION_FIELD)
        self.assertIsNotNone(description_field, "Description field not found")

        description_field.click()
        description_field.send_keys(description)

        self.switch_context_to_native()

    def click_send_button(self):

        sleep(1)

        self.switch_context_to_webview()

        logging.info("click 'Send' button")
        send_button = self.driver.find_element(*self.configuration.PhotoScreen.SEND_BUTTON)
        self.assertIsNotNone(send_button, "Send button not found")
        send_button.click()
        sleep(2)

        self.switch_context_to_native()

        logging.info("sending file")
        WebDriverWait(self.driver, 720).until(
            expected_conditions.presence_of_element_located(self.configuration.MainMenuScreen.INBOX_BUTTON),
            "Failed to send file")
        logging.info("File was sent")

    def click_gallery_button(self):

        self.switch_context_to_webview()

        logging.info("click in Gallery button")
        gallery_button = self.driver.find_element(*self.configuration.PhotoScreen.GALLERY_BUTTON)
        self.assertIsNotNone(gallery_button, "Gallery button not found")
        gallery_button.click()

        self.switch_context_to_native()

    def click_reset_button(self):

        logging.info("click 'Reset' button")
        reset_button = self.driver.find_element(*self.configuration.PhotoScreen.RESET_BUTTON)
        self.assertIsNotNone(reset_button, "Reset button not found")
        reset_button.click()

    def click_take_new_button(self):

        self.switch_context_to_webview()

        logging.info("clicking in Take new button")
        take_new_button = self.driver.find_element(*self.configuration.PhotoScreen.TAKE_NEW_BUTTON)
        self.assertIsNotNone(take_new_button, "Take new button not found")
        take_new_button.click()
        sleep(2)

        self.switch_context_to_native()
