"""A class for methods to handle Sent Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
import logging


class SentPage(BasePage):

    def search_for_sent_communications(self):

        logging.info("search_for_sent_communications")
        self.driver.find_element(*self.configuration.SentScreen.SEARCH_FIELD).click()
        self.driver.find_element(*self.configuration.SentScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.SentScreen.SEARCH_FIELD).send_keys("QA")

    def check_sent_communications(self):

        logging.info('check sent communication')
        sent_communication_email = self.driver.find_elements(*self.configuration.SentScreen.SENT_COMMUNICATIONS_EMAIL)
        self.assertIsNotNone(sent_communication_email[1], 'Short message, Email communications not found')

    def hamburger_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.hamburger_button()
