"""A class for methods to handle Location Page """

from Modules.BasePage.BasePage import BasePage
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import logging


class LocationPage(BasePage):
    
    def check_if_location_page_was_opened(self):

        logging.info("Location Page was opened")
        location_page_header = self.driver.find_element(*self.configuration.LocationScreen.LOCATION_PAGE_HEADER)
        self.assertIsNotNone(location_page_header, "Location Page header was not found")

    def click_send_once_now(self):

        logging.info("clicking in 'Send once now' button")
        send_once_now_button = self.driver.find_element(*self.configuration.LocationScreen.SEND_ONCE_NOW)
        self.assertIsNotNone(send_once_now_button, "Send once now button not found")
        send_once_now_button.click()

    def check_if_location_was_sent(self):

        sleep(2)
        logging.info("check if location was sent")
        try:
            WebDriverWait(self.driver, 30).until(
                expected_conditions.presence_of_element_located(self.configuration.LocationScreen.LOCATION_STATUS),
                "Failed to send location")
            logging.info("Location was sent")
        except NoSuchElementException:
            logging.info("Failed to send location")
            self.fail("Failed to send location")

    def click_send_every(self):

        logging.info("clicking in 'Send every' selector")
        send_every_button = self.driver.find_element(*self.configuration.LocationScreen.SEND_EVERY_SPINNER)
        self.assertIsNotNone(send_every_button, "Send every button not found")
        send_every_button.click()

    def check_if_5_minutes_option_was_chosen(self):

        logging.info("check if send every '5 minutes'  option was chosen")
        check_if_5_minutes_option_was_chosen = self.driver.find_element(*self.configuration.LocationScreen.
                                                                        ASSERT_5_MINUTES_OPTION)
        self.assertIsNotNone(check_if_5_minutes_option_was_chosen, "5 minutes option was not chosen")

    def click_for_the_next(self):

        logging.info("clicking in 'For the next' selector")
        for_the_next = self.driver.find_element(*self.configuration.LocationScreen.FOR_THE_NEXT_SPINNER)
        self.assertIsNotNone(for_the_next, "for the next selector not found")
        for_the_next.click()

    def check_if_1_hour_option_was_chosen(self):

        logging.info("check if '1 hour' option was chosen")
        check_if_1hour_option_was_chosen = self.driver.find_element(*self.configuration.LocationScreen.
                                                                    ASSERT_1_HOUR_OPTION)
        self.assertIsNotNone(check_if_1hour_option_was_chosen, "1 hour option was not chosen")

    def click_start_button(self):

        logging.info("click 'Start' button")
        start_button = self.driver.find_element(*self.configuration.LocationScreen.START_BUTTON)
        self.assertIsNotNone(start_button, "start button not found")
        start_button.click()
