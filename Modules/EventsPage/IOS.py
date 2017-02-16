""" Methods for IOS to handle Events Page """

from Modules.EventsPage.EventsPage import EventsPage
import logging
from time import sleep


class IOS(EventsPage):

    def filter_events_by_Search_field(self):

        logging.info("search field - search event named: 'search'")
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).click()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).send_keys("search")

    def clear_Search_field(self):

        logging.info("clear search field")
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).click()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        sleep(1)

    def click_More_button(self):

        logging.info("clicking in More button")
        more_button = self.driver.find_element(*self.configuration.EventsScreen.MORE_BUTTON)
        self.assertIsNotNone(more_button, "More button not found")
        more_button.click()

