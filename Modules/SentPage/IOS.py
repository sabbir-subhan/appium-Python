""" Methods for IOS to handle Sent Page """

from Modules.SentPage.SentPage import SentPage
import logging


class IOS(SentPage):

    def search_for_sent_communications(self):

        logging.info("search_for_sent_communications")
        self.driver.find_element(*self.configuration.SentScreen.SEARCH_FIELD).click()
        self.driver.find_element(*self.configuration.SentScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.SentScreen.SEARCH_FIELD).send_keys("QA")

