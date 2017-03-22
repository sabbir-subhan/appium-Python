""" Methods for IOS to handle Compose Page"""

from Modules.ComposePage.ComposePage import ComposePage
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
import logging
from time import sleep


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
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
        choose_contact_for_test = self.driver.find_element(*self.configuration.ComposeScreen.CONTACT_FOR_APPIUM_TESTS)
        self.assertIsNotNone(choose_contact_for_test, 'contact not found')
        location = choose_contact_for_test.location
        print(location)
        x = location["x"]
        y = location["y"]
        positions = [(x, y)]
        self.driver.tap(positions)

    def choose_comms_documents(self):

        logging.info('choose comms documents button')
        comms_documents_button = self.driver.find_element(*self.configuration.ComposeScreen.COMMS_DOCUMENTS_BUTTON)
        self.assertIsNotNone(comms_documents_button, 'comms documents button not found')
        location = comms_documents_button.location
        print(location)
        x = location["x"]
        y = location["y"]
        positions = [(x, y)]
        self.driver.tap(positions)
        sleep(1)

