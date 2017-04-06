""" Methods for IOS Gallery Page """

from Modules.GalleryPage.GalleryPage import GalleryPage
import logging
from time import sleep


class IOS(GalleryPage):

    def choose_element_1(self):

        sleep(2)
        # self.driver.execute_script("mobile: scroll", {"direction": "up"})

        logging.info("scroll down to Save button")
        scroll = 10
        while scroll > 0:
            logging.info("scroll to element")
            save_button = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_VIDEO_ELEMENT_1)
            if save_button.is_displayed():
                break
            else:
                logging.info("scroll up to first element")
                self.driver.execute_script("mobile: scroll", {"direction": "up"})
                scroll = scroll - 1

        sleep(1)
        logging.info("choosing element 1")
        choose_element_1 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_1)
        choose_element_1.click()

    def choose_video_from_gallery(self):

        logging.info("choose video from gallery")
        choose_video_from_gallery = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_VIDEO_ELEMENT_1)
        self.assertIsNotNone(choose_video_from_gallery, "video in gallery not found")
        choose_video_from_gallery.click()

    def click_use_button(self):

        logging.info("click 'Use' button")
        use_button = self.driver.find_element(*self.configuration.GalleryScreen.USE_BUTTON)
        self.assertIsNotNone(use_button, "use video button not found")
        use_button.click()

    def choose_videos_gallery(self):

        logging.info("choose videos gallery")
        choose_videos_gallery = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_VIDEOS_POPOVER)
        self.assertIsNotNone(choose_videos_gallery, "videos gallery not found")
        choose_videos_gallery.click()


