""" Methods for IOS9 on Gallery Page """

from Modules.GalleryPage.IOS import IOS
import logging
from selenium.common.exceptions import *


class IOS9(IOS):

    # this methods have different locators names than methods for iOS10
    def choose_element_1(self):

        logging.info("choosing element 1")
        try:
            choose_element_1 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_1_iPad)
            self.assertIsNotNone(choose_element_1, "element for iPad in gallery not found")
            choose_element_1.click()
        except NoSuchElementException:
            choose_element_1 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_1)
            self.assertIsNotNone(choose_element_1, "element in gallery not found")
            choose_element_1.click()

    def choose_video_from_gallery(self):

        logging.info("choose video from gallery")
        try:
            try:
                choose_video_from_gallery1 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_1)
                self.assertIsNotNone(choose_video_from_gallery1, "video in gallery not found")
                choose_video_from_gallery1.click()
            except NoSuchElementException:
                pass
            try:
                choose_video_from_gallery1 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_2)
                self.assertIsNotNone(choose_video_from_gallery1, "video in gallery not found")
                choose_video_from_gallery1.click()
            except NoSuchElementException:
                pass
        except NoSuchElementException:
            choose_video_from_gallery2 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_1_iPad)
            self.assertIsNotNone(choose_video_from_gallery2, "video for iPad in gallery not found")
            choose_video_from_gallery2.click()
