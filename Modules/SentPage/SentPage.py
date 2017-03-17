"""A class for methods to handle Sent Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
import logging


class SentPage(BasePage):

    def check_sent_communications(self):

        logging.info('check sent communication')
        sent_communication_email = self.driver.find_elements(*self.configuration.SentScreen.SENT_COMMUNICATIONS_EMAIL)
        self.assertIsNotNone(sent_communication_email[1], 'Short message, Email communications not found')

