""" Methods for IOS to handle Compose Page"""

from Modules.ComposePage.ComposePage import ComposePage
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
import logging
from time import sleep
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


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

    def alert_send_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.switch_context_to_webview()

        logging.info("click 'Send' button on alert")
        send_button_on_alert = self.driver.find_element(*self.configuration.ComposeScreen.ALERT_SEND_BUTTON)
        send_button_on_alert.click()
        sleep(2)

        common_page.switch_context_to_native()

        logging.info("sending message")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.configuration.MainMenuScreen.EVENTS_BUTTON),
            "Failed to send message")
        logging.info("Message was sent")

