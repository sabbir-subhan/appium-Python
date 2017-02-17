""" Methods for Android on Location Page """

from Modules.LocationPage.LocationPage import LocationPage
from selenium.common.exceptions import *
import logging


class Android(LocationPage):

    def check_if_start_button_was_clicked(self):

        try:
            start_button_disabled = self.driver.find_element(*self.configuration.LocationScreen.START_BUTTON_disabled)
            if start_button_disabled.is_displayed():
                logging.info("button Start was clicked")
            else:
                self.fail("button Start was not clicked")
        except NoSuchElementException:
            self.fail("button Start was not clicked")

    def choose_send_every_5_minutes_option(self):

        logging.info("choose send every '5 minutes' option")
        choose_5_minutes_option = self.driver.find_element(*self.configuration.LocationScreen.CHOOSE_5_MINUTES_OPTION)
        self.assertIsNotNone(choose_5_minutes_option)
        choose_5_minutes_option.click()

    def choose_1_hour_option(self):

        logging.info("choose '1 hour' option")
        choose_1_hour_option = self.driver.find_element(*self.configuration.LocationScreen.CHOOSE_1_HOUR_OPTION)
        self.assertIsNotNone(choose_1_hour_option)
        choose_1_hour_option.click()





