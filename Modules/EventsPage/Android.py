""" Methods for Android on Events Page """

from Modules.EventsPage.EventsPage import EventsPage
from Modules.AndroidDevice import AndroidDevice
from appium.webdriver.common.touch_action import TouchAction
import logging
from time import sleep


class Android(EventsPage, AndroidDevice):

    def filter_events_by_Search_field(self):

        # android 4.4.2 and 5.1 can't click correctly in "Search field" because of that
        #  Appium can't send keys into text field
        # - icon is on top of the text field and Appium is trying to send keys to it
        logging.info("search field - search event named: 'search'")
        sleep(2)
        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        search_field.click()
        logging.info("sending keys")
        self.driver.keyevent(47)  # send letter 'S'
        self.driver.keyevent(33)  # send letter 'E'
        self.driver.keyevent(29)  # send letter 'A'
        self.driver.keyevent(46)  # send letter 'R'

    def clear_Search_field(self):

        logging.info("clear search field")
        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        action = TouchAction(self.driver)
        action.long_press(el=search_field, duration=1000).perform()
        self.driver.keyevent(67)

