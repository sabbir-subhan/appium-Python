""" Methods for IOS to handle Sent Page """

from Modules.SentPage.SentPage import SentPage
import logging
from Modules.load_class import LoadClass


class IOS(SentPage):

    def type_text_into_search_field(self, text):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.type_text_into_search_field(text)

    def search_for_sent_communications(self):

        logging.info("search_for_sent_communications")
        self.driver.find_element(*self.configuration.SentScreen.SEARCH_FIELD).click()
        self.driver.find_element(*self.configuration.SentScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.SentScreen.SEARCH_FIELD).send_keys("QA")

