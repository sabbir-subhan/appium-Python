"""A class for methods to handle Gallery Page """

from Modules.BasePage.BasePage import BasePage
import logging


class GalleryPage(BasePage):

    def choose_element_1(self):

        logging.info("choosing element 1")
        choose_element_1 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_1)
        self.assertIsNotNone(choose_element_1, "first element in gallery not found")
        choose_element_1.click()

    def choose_videos_gallery(self):

        pass

    def click_use_button(self):

        pass






