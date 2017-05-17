""" Methods for Android on Contacts Page """

from Modules.ContactsPage.ContactsPage import ContactsPage
import logging
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from Modules.load_class import LoadClass


class Android(ContactsPage):

    def scroll_down_to_write_access_level(self):
        """Method to scroll down to write access level """

        window_size = self.driver.get_window_size()  # this returns dictionary
        start_x = window_size["width"] * 0.25
        start_y = window_size["height"] * 0.20
        end_y = window_size["height"] * 0.80
        logging.info("scroll down to write access level")
        sleep(2)
        scrolls = 7
        while scrolls > 0:
            self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
            scrolls -= 1
        sleep(2)

    def scroll_down_to_save_button(self):
        """Method to scroll down to bottom of the screen """

        window_size = self.driver.get_window_size()  # this returns dictionary
        start_x = window_size["width"] * 0.25
        start_y = window_size["height"] * 0.20
        end_y = window_size["height"] * 0.80
        logging.info("scroll down to save button")
        sleep(2)
        scrolls = 7
        while scrolls > 0:
            self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
            scrolls -= 1
        sleep(2)

    def clear_Search_field(self):

        logging.info("clear search field")
        sleep(1)
        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        action = TouchAction(self.driver)
        action.long_press(el=search_field, duration=1500).perform()
        self.driver.press_keycode(67)
        # action.long_press(el=search_field, duration=1500).perform()
        # self.driver.press_keycode(67)
        sleep(1)

    def scroll_down_to_email_field(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()
        common_page.scroll_down_one_view()

    def scroll_down_to_on_load_field(self):

        logging.info("scroll down to on load field")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def scroll_down_to_option_list(self):

        logging.info("scroll down to on load field")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()



