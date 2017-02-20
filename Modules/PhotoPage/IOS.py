""" Methods for IOS to handle Photo Page """

from Modules.PhotoPage.PhotoPage import PhotoPage
import logging
from time import sleep


class IOS(PhotoPage):

    def type_description(self, description):

        sleep(2)
        logging.info("type text into description field")
        description_field = self.driver.find_element(*self.configuration.PhotoScreen.DESCRIPTION_FIELD)
        self.assertIsNotNone(description_field, "Description field not found")
        description_field.click()
        description_field.send_keys(description)

    def click_gallery_button(self):

        logging.info("clicking in 'Gallery' button")
        gallery_button = self.driver.find_element(*self.configuration.PhotoScreen.GALLERY_BUTTON)
        gallery_button.click()

    def click_take_new_button(self):

        logging.info("clicking in 'Take new' button")
        take_new_button = self.driver.find_element(*self.configuration.PhotoScreen.TAKE_NEW_BUTTON)
        take_new_button.click()



