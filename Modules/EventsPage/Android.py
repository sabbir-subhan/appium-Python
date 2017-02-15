""" Methods for Android on Events Page """

from Modules.EventsPage.EventsPage import EventsPage
from appium.webdriver.common.touch_action import TouchAction
import logging
from time import sleep
from Modules.load_class import LoadClass


class Android(EventsPage, LoadClass):

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

        # after clearing search filed on Android device - "More" button is dropped to the bottom of the events list,
        # so to avoid unnecessary scrolling Appium will tap on hamburger button to go to main menu and reopen Events

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.click_Return_button_on_keyboard()

        common_page.hide_keyboard()

        common_page.hamburger_button()
        sleep(2)
        main_page = LoadClass.load_page('MainPage')
        main_page.setDriver(self.driver)
        main_page.open_EVENTS()

    def click_More_button(self):

        sleep(1)
        logging.info("click 'More' button")
        more_button = self.driver.find_element(*self.configuration.CommonScreen.SPINNER_ON_THE_RIGHT)
        self.assertIsNotNone(more_button, "More button was not found")
        more_button.click()
        sleep(0.5)
