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

    def click_send_button(self):

        sleep(1)
        logging.info("click 'Send' button")
        send_button = self.driver.find_element(*self.configuration.PhotoScreen.SEND_BUTTON)
        self.assertIsNotNone(send_button, "Send button not found")
        send_button.click()
        sleep(2)
        logging.info("sending file")
        WebDriverWait(self.driver, 420).until(
            expected_conditions.presence_of_element_located(self.configuration.MainMenuScreen.EVENTS_BUTTON),
            "Failed to send file")
        logging.info("File was sent")

    def click_reset_button(self):

        logging.info("click 'Reset' button")
        reset_button = self.driver.find_element(*self.configuration.PhotoScreen.RESET_BUTTON)
        self.assertIsNotNone(reset_button, "Reset button not found")
        reset_button.click()
