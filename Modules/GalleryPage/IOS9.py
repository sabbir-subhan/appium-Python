""" Methods for IOS9 on Gallery Page """

from Modules.GalleryPage.IOS import IOS
import logging


class IOS9(IOS):

    def choose_element_1(self):

        logging.info("choosing element 1")
        choose_element_1 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_1)
        choose_element_1.click()

    def choose_video_from_gallery(self):

        logging.info("choose video from gallery")
        choose_video_from_gallery = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_1)
        self.assertIsNotNone(choose_video_from_gallery, "video in gallery not found")
        choose_video_from_gallery.click()



