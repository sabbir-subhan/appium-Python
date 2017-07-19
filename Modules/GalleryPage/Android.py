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

        logging.info("choose videos gallery if it is visible")
        try:
            choose_videos_gallery = self.driver.find_element(*self.configuration.GalleryScreen.VIDEOS_BUTTON_IN_GALLERY)
            self.assertIsNotNone(choose_videos_gallery, "Videos gallery not found")
            choose_videos_gallery.click()
        except NoSuchElementException:
            pass
        sleep(1)
        try:
            logging.info("choose Camera videos if it is visible")
            camera_videos = self.driver.find_element(*self.configuration.GalleryScreen.VIDEOS)
            self.assertIsNotNone(camera_videos, "Camera videos not found")
            camera_videos.click()
        except NoSuchElementException:
            pass
        sleep(1)
        try:
            logging.info("if Videos gallery is not visible, click 'Gallery' button")
            choose_gallery = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_BUTTON_IN_SIDE_MENU)
            self.assertIsNotNone(choose_gallery, "Gallery not found")
            choose_gallery.click()
        except NoSuchElementException:
            pass

        # choose_videos_gallery = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_BUTTON_IN_SIDE_MENU)
        # self.assertIsNotNone(choose_videos_gallery, "gallery not found")
        # choose_videos_gallery.click()
        # sleep(1)
        # try:
        #     videos = self.driver.find_element(*self.configuration.GalleryScreen.VIDEOS)
        #     self.assertIsNotNone(videos, "videos not found")
        # except NoSuchElementException:
        #     videos = self.driver.find_element(*self.configuration.GalleryScreen.VIDEOS2)
        #     self.assertIsNotNone(videos, "videos not found")
        # size = videos.size
        # logging.error(size)
        #
        # x = self.driver.find_element_by_xpath('//android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.view.View[1]/com.sec.samsung.gallery.glview.composeView.PositionControllerBase.ThumbObject[1]')
        # location = x.location
        # print(location)

        # action = TouchAction(self.driver)
        # source = self.driver.page_source
        # logging.warning(source)
        # bounds = source.__getattribute__("bounds")
        # logging.error(bounds)
        # bounds2 = source.__getitem__("bounds")
        # logging.error(bounds2)
        # action.tap(x=70, y=375, count=1).perform()
        # sleep(0.5)

        # # bounds = videos.get_attribute("bounds")
        # # logging.error(bounds)
        # # bounds2 = videos.get_property("bounds")
        # # logging.error(bounds2)
        #
        # action.tap(x=64, y=372, count=1).perform()
        # videos.click()
        #
        # action.tap(element=videos, count=1).perform()
        #
        # sleep(2)

    def choose_photos_gallery(self):

        logging.info("choose photos gallery if it is visible")
        try:
            choose_photos_gallery = self.driver.find_element(
                *self.configuration.GalleryScreen.GALLERY_BUTTON_IN_SIDE_MENU)
            self.assertIsNotNone(choose_photos_gallery, "Photos gallery not found")
            choose_photos_gallery.click()
        except NoSuchElementException:
            pass
        sleep(1)

