"""A class for methods to handle Gallery Page on Android"""

from Modules.GalleryPage.GalleryPage import GalleryPage
import logging
from Modules.load_class import LoadClass


class Android(GalleryPage):

    def choose_element_1(self):

        logging.info("choosing element 1")
        choose_element_1 = self.driver.find_element(*self.configuration.GalleryScreen.GALLERY_ELEMENT_1)
        self.assertIsNotNone(choose_element_1, "first element in gallery not found")
        choose_element_1.click()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.alert_popup_allow()

        try:  # on android it is necessary to reopen gallery after allowing access to photos/videos
            photo_page = LoadClass.load_page('PhotoPage')
            photo_page.setDriver(self.driver)
            photo_page.click_gallery_button()
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.alert_popup_allow()
            Android.choose_element_1(self)
        except:
            pass
