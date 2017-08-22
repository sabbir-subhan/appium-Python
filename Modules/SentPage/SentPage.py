"""A class for methods to handle Sent Page """

from Modules.BasePage.BasePage import BasePage
import logging
from time import sleep
from selenium.common.exceptions import *
from Modules.load_class import LoadClass


class SentPage(BasePage):

    def check_sent_communications(self):

        logging.info('check sent communication')
        try:
            sent_communication_email = self.driver.find_elements(*self.configuration.SentScreen.SENT_COMMUNICATIONS_EMAIL)
            self.assertIsNotNone(sent_communication_email[0], 'Short message, Email communications not found')
            # self.assertIsNotNone(sent_communication_email[1], 'Short message, Email communications not found')
            logging.info("sent communication is present")
        except NoSuchElementException and IndexError:
            logging.warning("Short message, Email communications not found")

    # def check_sent_communications(self):
    #
    #     logging.info('check sent communication')
    #     try:
    #         sent_communication_email = self.driver.find_elements(*self.configuration.SentScreen.SENT_COMMUNICATIONS_EMAIL)
    #         self.assertIsNotNone(sent_communication_email[0], 'Short message, Email communications not found')
    #         # self.assertIsNotNone(sent_communication_email[1], 'Short message, Email communications not found')
    #         logging.info("sent communication is present")
    #     except NoSuchElementException and IndexError:
    #         logging.warning("Short message, Email communications not found")

    def clear_Search_field(self):

        self.switch_context_to_webview()

        try:
            clear_search_field_button = self.driver.find_element(*self.configuration.SentScreen.CLEAR_SEARCH_FIELD_BUTTON)
            if clear_search_field_button.is_displayed():
                logging.info("clear Search field by clicking clear button")
                self.assertIsNotNone(clear_search_field_button, "clear search field button not found")
                clear_search_field_button.click()
                sleep(2)
        except NoSuchElementException:
            pass

        self.switch_context_to_native()

    def type_text_into_search_field(self, text):

        # logging.info("filter contacts by search field")
        #
        # search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        # self.assertIsNotNone(search_field, "Search field not found")
        # search_field.click()
        # sleep(2)
        # search_field.send_keys(text)
        # sleep(1)
        
        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.type_text_into_search_field(text)
