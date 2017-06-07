""" Methods for Android on Location Page """

from Modules.LocationPage.LocationPage import LocationPage
from selenium.common.exceptions import *
import logging
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class Android(LocationPage):

    def alert_allow_location(self):

        logging.info("Check alert allow location")
        # try:
        #     WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(self.configuration.iOS.IOS_ALLOW), "alert allow not found")
        #     # WebDriverWait(self.driver, 50).until(expected_conditions.presence_of_element_located(self.configuration.iOS.IOS_ALLOW), "alert allow not found")
        #     button_allow_location = self.driver.find_element(*self.configuration.iOS.IOS_ALLOW)
        #     button_allow_location.click()
        # except NoSuchElementException:
        #     pass
        try:
            WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(self.configuration.Android.ANDROID_ALLOW), "alert allow not found")
        except TimeoutException:
            pass
        try:
            button_allow_location = self.driver.find_element(*self.configuration.Android.ANDROID_ALLOW)
            button_allow_location.click()
        except NoSuchElementException:
            pass

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





