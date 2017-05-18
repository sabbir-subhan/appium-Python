""" Methods for IOS to handle Contacts Page """

from Modules.ContactsPage.ContactsPage import ContactsPage
from Modules.load_class import LoadClass
import logging
from selenium.common.exceptions import *
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


class IOS(ContactsPage):

    def scroll_down_to_email_field(self):

        """Method to scroll down to email field"""

        logging.info("scroll down to email field")
        scroll = 5
        while scroll > 0:
            logging.info("check if email field is visible")
            save_button = self.driver.find_element(*self.configuration.ContactsScreen.EMAIL_FIELD)
            if save_button.is_displayed():
                break
            else:
                logging.info("scroll down to email field")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                scroll = scroll - 1

    def scroll_down_to_on_load_field(self):

        reports_page = LoadClass.load_page('ReportsPage')
        reports_page.setDriver(self.driver)
        reports_page.scroll_down_to_on_load_field()

    def scroll_down_to_option_list(self):

        reports_page = LoadClass.load_page('ReportsPage')
        reports_page.setDriver(self.driver)
        reports_page.scroll_down_to_option_list()
