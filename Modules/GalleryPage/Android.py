"""A class for methods to handle Gallery Page on Android"""

from Modules.GalleryPage.GalleryPage import GalleryPage
import logging
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
from Conf.desired_capabilities import DesiredCapabilities


class Android(GalleryPage):

    def choose_element_1(self):

        logging.info("choosing element 1 - Android")
        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        platform_version = desired_capabilities.get('platformVersion')
        if platform_version >= "7":
            choose_element_1_android7 = self.driver.find_element(*self.configuration.GalleryScreen.
                                                                 GALLERY_ELEMENT_1_android7)
            choose_element_1_android7.click()  # for some reason it is not working with Android 7
            # location = choose_element_1_android7.location
            # print(location)
            # x = location["x"]
            # y = location["y"]
            # print(x)
            # print(y)
            # positions = [(x, y)]
            # print(positions)
            # self.driver.tap(positions)  # not working, also Touch Action is not working in Android 7 Gallery
        else:
            choose_element_1 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_1)
            choose_element_1.click()
        # else:
        # try:
        #     choose_element_1 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_1)
        #     choose_element_1.click()
        # except NoSuchElementException:
        #     window_size = self.driver.get_window_size()  # this will give You a dictionary
        #     logging.info(window_size)
        #     x = window_size["width"] * 0.30
        #     logging.info(x)
        #     y = window_size["height"] * 0.30
        #     logging.info(y)
        #     position = [(x, y)]
        #     self.driver.tap(position)
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.alert_popup_allow()
        # try:  # on android it is necessary to reopen gallery after allowing access to photos/videos
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

        common_page = LoadClass.load_page('GalleryPage')
        common_page.setDriver(self.driver)
        common_page.choose_element_1()

