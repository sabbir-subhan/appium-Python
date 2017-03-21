""" Methods for IOS to handle Compose Page"""

from Modules.ComposePage.ComposePage import ComposePage
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
import logging


class IOS(ComposePage):

    def choose_contact_for_test(self):

        logging.info('choose contact for test')
        scroll = 0
        while scroll == 0:
            logging.info("check if contact is visible")
            choose_contact_for_test = self.driver.find_element(
                *self.configuration.ComposeScreen.CONTACT_FOR_APPIUM_TESTS)
            if choose_contact_for_test.is_displayed():
                break
            else:
                logging.info("scroll down to save button")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
        choose_contact_for_test = self.driver.find_element(*self.configuration.ComposeScreen.CONTACT_FOR_APPIUM_TESTS)
        self.assertIsNotNone(choose_contact_for_test, 'add recipients button not found')
        choose_contact_for_test.click()
