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

        logging.info("choose videos gallery")
        choose_videos_gallery = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_VIDEOS_POPOVER)
        self.assertIsNotNone(choose_videos_gallery, "videos gallery not found")
        choose_videos_gallery.click()

    def click_use_video_button(self):

        logging.info("click 'Use' button")
        use_video_button = self.driver.find_element(*self.configuration.GalleryScreen.USE_VIDEO_BUTTON)
        self.assertIsNotNone(use_video_button, "use video button not found")
        use_video_button.click()
