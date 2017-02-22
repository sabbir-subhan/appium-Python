""" Methods for IOS Gallery Page """

from Modules.GalleryPage.GalleryPage import GalleryPage
import logging


class IOS(GalleryPage):

    def click_use_button(self):

        logging.info("click Choose button")
        use_button = self.driver.find_element(*self.configuration.GalleryScreen.CHOOSE_BUTTON)
        self.assertIsNotNone(use_button, "use video button not found")
        use_button.click()
