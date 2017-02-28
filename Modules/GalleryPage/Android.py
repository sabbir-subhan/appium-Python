"""A class for methods to handle Gallery Page on Android"""

from Modules.GalleryPage.GalleryPage import GalleryPage
import logging
from Modules.load_class import LoadClass
from selenium.common.exceptions import *


class Android(GalleryPage):

    def choose_element_1(self):

        logging.info("choosing element 1 - Android")
        try:
            choose_element_1 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_1)
            self.assertIsNotNone(choose_element_1, "first element in gallery not found")
            choose_element_1.click()
        except NoSuchElementException:
            window_size = self.driver.get_window_size()  # this will give You a dictionary
            logging.info(window_size)
            x = window_size["width"] * 0.30
            logging.info(x)
            y = window_size["height"] * 0.30
            logging.info(y)
            position = [(x, y)]
            self.driver.tap(position)
            # choose_element_1_android7 = self.driver.find_element(*self.configuration.GalleryScreen.
            #                                                      GALLERY_ELEMENT_1_android7)
            # self.assertIsNotNone(choose_element_1_android7, "first element in gallery not found")
            # logging.info("A TU NIE")
            # choose_element_1_android7.click()

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
