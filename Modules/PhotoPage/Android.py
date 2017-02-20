""" Methods for Android on Photo Page """

from Modules.PhotoPage.PhotoPage import PhotoPage
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import logging


class Android(PhotoPage):

    def type_description(self, description):

        WebDriverWait(self.driver, 35).until(
            expected_conditions.presence_of_element_located(self.configuration.PhotoScreen.DESCRIPTION_FIELD),
            "Failed to locate description field for photo")
        logging.info("type text into description field")
        description_field = self.driver.find_element(*self.configuration.PhotoScreen.DESCRIPTION_FIELD)
        self.assertIsNotNone(description_field, "Description field not found")
        description_field.send_keys(description)

    def click_gallery_button(self):

        logging.info("clicking in Gallery button")
        gallery_button = self.driver.find_element(*self.configuration.PhotoScreen.GALLERY_BUTTON)
        self.assertIsNotNone(gallery_button, "Gallery button not found")
        gallery_button.click()

    def click_take_new_button(self):

        logging.info("clicking in Take new button")
        take_new_button = self.driver.find_element(*self.configuration.PhotoScreen.TAKE_NEW_BUTTON)
        self.assertIsNotNone(take_new_button, "Take new button not found")
        take_new_button.click()

