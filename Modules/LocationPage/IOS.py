""" Methods for IOS Location Page """

from Modules.LocationPage.LocationPage import LocationPage
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
import logging
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class IOS(LocationPage):

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
            WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(self.configuration.iOS.IOS_ALLOW), "alert allow not found")
        except TimeoutException:
            pass
        try:
            button_allow_location = self.driver.find_element(*self.configuration.iOS.IOS_ALLOW)
            button_allow_location.click()
        except NoSuchElementException:
            pass

    def check_if_start_button_was_clicked(self):  # some problem on iOS10 - app is crashing

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
            choose_5_minutes_option = self.driver.find_element(*self.configuration.LocationScreen.CHOOSE_5_MINUTES_OPTION_iPad)
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

