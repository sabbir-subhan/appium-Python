""" Methods for Android on Sent Page """

from Modules.SentPage.SentPage import SentPage
import logging
from time import sleep


class Android(SentPage):

    def search_for_sent_communications(self):

        logging.info("search field - search event named: 'QA'")
        sleep(2)
        search_field = self.driver.find_element(*self.configuration.SentScreen.SEARCH_FIELD)
        search_field.click()
        logging.info("sending keys")
        self.driver.keyevent(45)  # send letter 'Q'
        self.driver.keyevent(29)  # send letter 'A'
