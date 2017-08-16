""" Methods for IOS9 on Gallery Page """

from Modules.GalleryPage.IOS import IOS
import logging
from selenium.common.exceptions import *
from time import sleep


class IOS9(IOS):

    def choose_element_from_gallery(self):

        logging.info("choosing element from gallery")

        try:
            choose_element_1 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_1_iPad)
            self.assertIsNotNone(choose_element_1, "element for iPad in gallery not found")
            choose_element_1.click()
        except NoSuchElementException:
            choose_element_1 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT)
            self.assertIsNotNone(choose_element_1, "element in gallery not found")
            choose_element_1.click()

    def click_use_button(self):

        sleep(2)
        logging.info("click 'Use' button")
        try:
            use_button = self.driver.find_element(*self.configuration.GalleryScreen.USE_BUTTON)
        except NoSuchElementException:
            use_button = self.driver.find_element(*self.configuration.GalleryScreen.CHOOSE_BUTTON)
        self.assertIsNotNone(use_button, "use video button not found")
        use_button.click()
        sleep(2)

    # def choose_video_from_gallery(self):
    #
    #     logging.info("choose video from gallery")
    #
    #     try:
    #         choose_video_from_gallery1 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT)
    #         self.assertIsNotNone(choose_video_from_gallery1, "video in gallery not found")
    #         choose_video_from_gallery1.click()
    #     except NoSuchElementException:
    #         choose_video_from_gallery2 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_1_iPad)
    #         self.assertIsNotNone(choose_video_from_gallery2, "video for iPad in gallery not found")
    #         choose_video_from_gallery2.click()

