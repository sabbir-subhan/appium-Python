""" Methods for IOS to handle Events Page """

from Modules.EventsPage.EventsPage import EventsPage
from selenium.common.exceptions import *
import logging
from time import sleep


class IOS(EventsPage):

    def filter_events_by_Search_field(self):

        logging.info("search field - search event named: 'search'")
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).click()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).send_keys("search")

    def filter_events_to_find_previous_event(self):

        logging.info("search field - search event named: 'app'")
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).click()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).send_keys("app")

    def clear_Search_field(self):

        logging.info("clear search field")
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).click()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        sleep(1)

    def click_More_button(self):

        sleep(1)
        logging.info("clicking in More button")
        more_button = self.driver.find_element(*self.configuration.EventsScreen.MORE_BUTTON)
        self.assertIsNotNone(more_button, "More button not found")

        location = more_button.location
        print(location)
        x = location["x"]
        y = location["y"]
        print(x)
        print(y)
        positions = [(x, y)]
        self.driver.tap(positions)

        # more_button.click()

    def clear_primary_event(self):

        logging.info("clicking in 'Clear primary event' button")
        clear_primary_event_button = self.driver.find_element(*self.configuration.EventsScreen.
                                                              CLEAR_PRIMARY_EVENT_BUTTON)
        self.assertIsNotNone(clear_primary_event_button, "Clear primary event button not found")
        clear_primary_event_button.click()
        try:
            logging.info("checking notification - 'Primary event cleared'")
            sleep(1)
            notification = self.driver.find_element(*self.configuration.EventsScreen.NOTIFICATION_PRIMARY_EVENT_CLEARED)
            self.assertIsNotNone(notification)
        except NoSuchElementException:
            logging.info("notification not found")

