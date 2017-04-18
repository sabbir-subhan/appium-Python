""" Methods for IOS Gallery Page """

from Modules.GalleryPage.GalleryPage import GalleryPage
import logging
from time import sleep


class IOS(GalleryPage):

    def choose_element_1(self):  # iOS10 is opening gallery focused on latest element

        sleep(2)
        logging.info("choosing element from gallery")
        choose_element_1 = self.driver.find_element(*self.configuration.GalleryScreen.LAST_ELEMENT)
        choose_element_1.click()
        sleep(1)

        # scroll = 15
        # while scroll > 0:
        #     logging.info("scroll to element")
        #     element_in_photo_gallery = self.driver.find_element(*self.configuration.GalleryScreen.FIRST_PHOTO_GALLERY_ELEMENT)
        #     if element_in_photo_gallery.is_displayed():
        #         logging.info("end scrolling")
        #         break
        #     else:
        #         logging.info("scroll up to first element")
        #         self.driver.execute_script("mobile: scroll", {"direction": "up"})
        #         scroll = scroll - 1
        # sleep(1)
        # logging.info("choosing element from gallery")
        # try:
        #     choose_element_1 = self.driver.find_element(*self.configuration.GalleryScreen.FIRST_PHOTO_GALLERY_ELEMENT)
        #     choose_element_1.click()
        #     sleep(1)
        # except:
        #     choose_element = self.driver.find_elements(*self.configuration.GalleryScreen.GALLERY_ELEMENTS)
        #     choose_element[1].click()
        #     sleep(1)

    def choose_video_from_gallery(self):

        sleep(2)
        logging.info("choose video from gallery")
        choose_video_from_gallery = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_VIDEO_ELEMENT_1)
        self.assertIsNotNone(choose_video_from_gallery, "video in gallery not found")
        choose_video_from_gallery.click()

    def click_use_button(self):

        sleep(2)
        logging.info("click 'Use' button")
        use_button = self.driver.find_element(*self.configuration.GalleryScreen.USE_BUTTON)
        self.assertIsNotNone(use_button, "use video button not found")
        use_button.click()
        sleep(2)

    def choose_videos_gallery(self):

        sleep(2)
        logging.info("choose videos gallery")
        choose_videos_gallery = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_VIDEOS_POPOVER)
        self.assertIsNotNone(choose_videos_gallery, "videos gallery not found")
        choose_videos_gallery.click()


