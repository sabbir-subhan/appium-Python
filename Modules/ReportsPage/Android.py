""" Methods for Android on Reports Page """

from Modules.ReportsPage.ReportsPage import ReportsPage
import logging
from time import sleep
from Modules.load_class import LoadClass


class Android(ReportsPage):

    def scroll_down_to_assets_chooser_field(self):

        logging.info("scroll down to assets chooser field")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()
        common_page.scroll_down_one_view()

    def choose_lodging_agency(self):

        logging.info("choose Lodging Agency")
        lodging_agency = self.driver.find_element(*self.configuration.ReportsScreen.LODGING_AGENCY)
        self.assertIsNotNone(lodging_agency, "Lodging Agency inside picker was not found")
        lodging_agency.click()
        sleep(1)

    def scroll_down_to_publish_button(self):

        logging.info("scroll down to Publish button")
        window_size = self.driver.get_window_size()  # this returns dictionary
        start_x = window_size["width"]*0.25
        # end_x = window_size["width"]*0.75
        start_y = window_size["height"]*0.20
        end_y = window_size["height"]*0.80
        logging.info("scrolling down to Publish button")
        sleep(1)
        scrolls = 10
        while scrolls > 0:
            self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
            scrolls = scrolls - 1
        sleep(2)

    def scroll_down_to_on_load_field(self):

        logging.info("scroll down to on load field")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def scroll_down_to_option_list(self):

        logging.info("scroll down to option list")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def scroll_down_media_release_field(self):

        logging.info("scroll down to media release field")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def type_text_into_media_release_field(self):

        sleep(1)
        media_release_field = self.driver.find_element(*self.configuration.ReportsScreen.MEDIA_RELEASE_FIELD)
        media_release_field.click()
        sleep(1)
        logging.info("sending keys")
        self.driver.press_keycode(48)  # send letter 'T'
        self.driver.press_keycode(33)  # send letter 'E'
        self.driver.press_keycode(52)  # send letter 'X'
        self.driver.press_keycode(48)  # send letter 'T'

