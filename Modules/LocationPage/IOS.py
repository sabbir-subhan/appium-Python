""" Methods for IOS Location Page """

from Modules.LocationPage.LocationPage import LocationPage
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
import logging


class IOS(LocationPage):

    def check_if_start_button_was_clicked(self):

        logging.info("check if 'Start' button was clicked")
        try:
            start_button = self.driver.find_element(*self.configuration.LocationScreen.START_BUTTON)
            if start_button.is_displayed():
                self.fail("button Start was not clicked")
            else:
                pass
        except NoSuchElementException:
            logging.info("button Start was clicked")

    def choose_send_every_5_minutes_option(self):

        logging.info("choose send every '5 minutes' option")

        try:
            choose_5_minutes_option = self.driver.find_element(*self.configuration.LocationScreen.
                                                               CHOOSE_5_MINUTES_OPTION_iPad)
            self.assertIsNotNone(choose_5_minutes_option, "5 minutes option not found")
            choose_5_minutes_option.click()
        except NoSuchElementException:
            picker_wheel = self.driver.find_element(*self.configuration.CommonScreen.PICKER_WHEEL)
            picker_wheel.send_keys('5 minutes')
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.done_button()

    def choose_1_hour_option(self):

        logging.info("choose '1 hour' option")

        try:
            choose_1_hour_option = self.driver.find_element(*self.configuration.LocationScreen.
                                                            CHOOSE_1_HOUR_OPTION_iPad)
            self.assertIsNotNone(choose_1_hour_option, "1 hour option not found")
            choose_1_hour_option.click()
        except NoSuchElementException:
            picker_wheel = self.driver.find_element(*self.configuration.CommonScreen.PICKER_WHEEL)
            picker_wheel.send_keys('1 hour')
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.done_button()

