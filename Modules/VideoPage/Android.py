""" Methods for Android on Video Page """

from Modules.VideoPage.VideoPage import VideoPage
import logging


class Android(VideoPage):

    def click_record_new_button(self):

        logging.info("clicking in 'Record new' button")
        record_new_button = self.driver.find_element(*self.configuration.VideoScreen.RECORD_NEW_BUTTON)
        self.assertIsNotNone(record_new_button, "record new button not found")
        record_new_button.click()


