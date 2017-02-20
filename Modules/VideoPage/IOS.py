""" Methods for IOS to handle Video Page """

from Modules.VideoPage.VideoPage import VideoPage
import logging


class IOS(VideoPage):

    def click_record_new_button(self):

        logging.info("clicking in 'Record new' button")
        record_new_button = self.driver.find_element(*self.configuration.VideoScreen.RECORD_NEW_BUTTON)
        record_new_button.click()



