"""A class for methods to handle Gallery Page on Android"""

from Modules.GalleryPage.GalleryPage import GalleryPage
import logging
from Modules.load_class import LoadClass
from Conf.desired_capabilities import DesiredCapabilities
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


class Android(GalleryPage):

    def choose_element_1(self):

        logging.info("choosing element 1 - Android")

        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        platform_version = desired_capabilities.get('platformVersion')
        if platform_version >= "7":
            gallery_elements_android7 = self.driver.find_elements(*self.configuration.GalleryScreen.
                                                                  GALLERY_ELEMENTS_android7)
            location = gallery_elements_android7[1].location
            logging.info(location)
            x = location["x"]
            y = location["y"]
            logging.info(x)
            logging.info(y)
            positions = [(x, y)]
            self.driver.tap(positions)
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

        common_page = LoadClass.load_page('GalleryPage')
        common_page.setDriver(self.driver)
        common_page.choose_element_1()

