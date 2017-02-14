""" Methods for IOS to handle Events Page """

from Modules.EventsPage.EventsPage import EventsPage
import logging
from time import sleep


class IOS(EventsPage):

    def filter_events_by_Search_field(self):

        logging.info("search field - search event named: 'search'")
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD_ios).click()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD_ios).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD_ios).send_keys("search")

    def clear_Search_field(self):

        logging.info("clear search field")
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD_ios).click()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD_ios).clear()
        sleep(1)

