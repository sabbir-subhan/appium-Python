"""A class for methods to handle Gallery Page on Android"""

from Modules.GalleryPage.GalleryPage import GalleryPage
import logging
from Modules.load_class import LoadClass
from Conf.desired_capabilities import DesiredCapabilities
# from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from selenium.common.exceptions import *


class Android(GalleryPage):

    def choose_element_1(self):

        logging.info("choosing element 1 - Android")

        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        platform_version = desired_capabilities.get('platformVersion')
        if platform_version >= "7":
            # gallery_elements_android7 = self.driver.find_elements(*self.configuration.GalleryScreen.
            #                                                       GALLERY_ELEMENTS_android7)
            gallery_elements_android7 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_1_android7)
            gallery_elements_android7.click()
            sleep(1)

            # photo_page = LoadClass.load_page('PhotoPage')
            # photo_page.setDriver(self.driver)
            # photo_page.click_gallery_button()

            # try:
            #     photo_page = LoadClass.load_page('PhotoPage')
            #     photo_page.setDriver(self.driver)
            #     photo_page.click_gallery_button()
            # except No:
            #     video_page = LoadClass.load_page('VideoPage')
            #     video_page.setDriver(self.driver)
            #     video_page.click_gallery_button()

            # location = gallery_elements_android7[0].location
            # logging.info(location)
            # x = location["x"]
            # y = location["y"]
            # logging.info(x)
            # logging.info(y)
            # positions = [(x, y)]
            # sleep(2)
            # self.driver.tap(positions)

            # common_page = LoadClass.load_page('CommonPage')
            # common_page.setDriver(self.driver)
            # common_page.alert_popup_allow()
            #
            # photo_page = LoadClass.load_page('PhotoPage')
            # photo_page.setDriver(self.driver)
            # photo_page.click_gallery_button()
            #
            # self.driver.tap(positions)
            # # action = TouchAction(self.driver)
            # # action.tap(element=gallery_elements_android7[0], x=x, y=y, count=1).perform()
        else:
            choose_element_1 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_1)
            choose_element_1.click()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.alert_popup_allow()
        # try:  # on Android 6 sometimes it is necessary to reopen gallery after allowing access to photos/videos
        #     photo_page = LoadClass.load_page('PhotoPage')
        #     photo_page.setDriver(self.driver)
        #     photo_page.click_gallery_button()
        #     common_page = LoadClass.load_page('CommonPage')
        #     common_page.setDriver(self.driver)
        #     common_page.alert_popup_allow()
        #     Android.choose_element_1(self)
        # except:
        #     pass

    def choose_video_from_gallery(self):

        # gallery_page = LoadClass.load_page('GalleryPage')
        # gallery_page.setDriver(self.driver)
        # gallery_page.choose_element_1()
        logging.info("choosing element 1 - Android")
        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        platform_version = desired_capabilities.get('platformVersion')
        if platform_version >= "7":
            gallery_elements_android7 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_1_android7)
            gallery_elements_android7.click()
            sleep(1)
        else:
            choose_element_1 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_1)
            choose_element_1.click()
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.alert_popup_allow()
        sleep(1)

    def choose_videos_gallery(self):

        try:
            choose_recent = self.driver.find_element(*self.configuration.GalleryScreen.RECENT_BUTTON_IN_SIDE_MENU)
            logging.info("if Videos gallery is not visible, click 'Recent' button")
            self.assertIsNotNone(choose_recent, "Recent button not found")
            choose_recent.click()
        except NoSuchElementException:
            show_roots = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_SHOW_ROOTS)
            logging.info("click 'Show roots' button")
            self.assertIsNotNone(show_roots, "Show roots button not found")
            show_roots.click()
            sleep(0.5)
            choose_recent = self.driver.find_element(*self.configuration.GalleryScreen.RECENT_BUTTON_IN_SIDE_MENU)
            logging.info("if Videos gallery is not visible, click 'Recent' button")
            self.assertIsNotNone(choose_recent, "Recent button not found")
            choose_recent.click()

        # try:
        #     choose_videos_gallery = self.driver.find_element(*self.configuration.GalleryScreen.VIDEOS_BUTTON_IN_GALLERY)
        #     self.assertIsNotNone(choose_videos_gallery, "Videos gallery not found")
        #     logging.info("choose videos gallery if it is visible")
        #     choose_videos_gallery.click()
        # except NoSuchElementException:
        #     pass
        # sleep(1)
        # try:
        #     camera_videos = self.driver.find_element(*self.configuration.GalleryScreen.VIDEOS)
        #     self.assertIsNotNone(camera_videos, "Camera videos not found")
        #     logging.info("choose Camera videos if it is visible")
        #     camera_videos.click()
        # except NoSuchElementException:
        #     pass
        # sleep(1)
        # try:
        #     # choose_gallery = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_BUTTON_IN_SIDE_MENU)
        #     # logging.info("if Videos gallery is not visible, click 'Gallery' button")
        #     # self.assertIsNotNone(choose_gallery, "Gallery not found")
        #     # choose_gallery.click()
        #     choose_recent = self.driver.find_element(*self.configuration.GalleryScreen.RECENT_BUTTON_IN_SIDE_MENU)
        #     logging.info("if Videos gallery is not visible, click 'Recent' button")
        #     self.assertIsNotNone(choose_recent, "Recent button not found")
        #     choose_recent.click()
        # except NoSuchElementException:
        #     pass

    def choose_photos_gallery(self):

        logging.info("choose photos gallery if it is visible")
        try:
            # choose_photos_gallery = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_BUTTON_IN_SIDE_MENU)
            # self.assertIsNotNone(choose_photos_gallery, "Photos gallery not found")
            # choose_photos_gallery.click()
            choose_recent = self.driver.find_element(*self.configuration.GalleryScreen.RECENT_BUTTON_IN_SIDE_MENU)
            self.assertIsNotNone(choose_recent, "Recent button not found")
            choose_recent.click()
        except NoSuchElementException:
            pass
        sleep(1)

