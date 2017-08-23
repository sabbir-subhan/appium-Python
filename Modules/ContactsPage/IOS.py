""" Methods for IOS to handle Contacts Page """

from Modules.ContactsPage.ContactsPage import ContactsPage
from Modules.load_class import LoadClass
import logging
from configuration import platform
# from selenium.common.exceptions import *
# from time import sleep
# from appium.webdriver.common.touch_action import TouchAction


class IOS(ContactsPage):

    def type_text_into_search_field(self, text):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.type_text_into_search_field(text)

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

    def scroll_down_to_address_input_field(self):

        """Method to scroll down to address input field"""

        logging.info("scroll down to address input field")
        scroll = 5
        while scroll > 0:
            logging.info("check if address input field is visible")
            save_button = self.driver.find_element(*self.configuration.ContactsScreen.ADDRESS_FIELD)
            if save_button.is_displayed():
                break
            else:
                logging.info("scroll down to address input field")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                scroll = scroll - 1

    def clear_name_for_offline_contact_group(self):

        self.switch_context_to_webview()

        logging.info("clear name for offline contact group")

        if "emulator" in platform:  # there is no automatic way to disable networking on iOS emulators
            first_name = self.driver.find_element(*self.configuration.ContactsScreen.CLEAR_NAME_FOR_EDITED_CONTACT_GROUP)
            self.assertIsNotNone(first_name, "Name clear field button was not found")
            first_name.click()
        else:
            first_name = self.driver.find_element(*self.configuration.ContactsScreen.CLEAR_NAME_FOR_NEW_CONTACT_GROUP)
            self.assertIsNotNone(first_name, "Name clear field button was not found")
            first_name.click()

        self.switch_context_to_native()

    def type_name_for_offline_contact_group(self, text):

        self.switch_context_to_webview()

        logging.info("Type Name for offline contact group")

        if "emulator" in platform:  # there is no automatic way to disable networking on iOS emulators
            name_field = self.driver.find_element(*self.configuration.ContactsScreen.NAME_FIELD_FOR_EDITED_CONTACT_GROUP)
            self.assertIsNotNone(name_field, "name field not found")
            name_field.click()
            name_field.send_keys(text)
        else:
            name_field = self.driver.find_element(*self.configuration.ContactsScreen.NAME_FIELD_FOR_NEW_CONTACT_GROUP)
            self.assertIsNotNone(name_field, "name field not found")
            name_field.click()
            name_field.send_keys(text)

        self.switch_context_to_native()

    def save_offline_contact_group(self):

        self.switch_context_to_webview()

        logging.info('click Save button')

        if "emulator" in platform:  # there is no automatic way to disable networking on iOS emulators
            save_button = self.driver.find_element(*self.configuration.ContactsScreen.SAVE_EDITED_CONTACT_GROUP)
            self.assertIsNot(save_button, "save button not found")
            save_button.click()
        else:
            save_button = self.driver.find_element(*self.configuration.ContactsScreen.SAVE_NEW_CONTACT_GROUP)
            self.assertIsNot(save_button, "save button not found")
            save_button.click()

        self.switch_context_to_native()

    def save_offline_contact(self):

        self.switch_context_to_webview()

        logging.info('click Save button')

        if "emulator" in platform:  # there is no automatic way to disable networking on iOS emulators
            save_button = self.driver.find_element(*self.configuration.ContactsScreen.SAVE_EDITED_CONTACT)
            self.assertIsNot(save_button, "save button not found")
            save_button.click()
        else:
            save_button = self.driver.find_element(*self.configuration.ContactsScreen.SAVE_NEW_CONTACT)
            self.assertIsNot(save_button, "save button not found")
            save_button.click()

        self.switch_context_to_native()

    def open_first_pending_contact_group(self):    # pending contact group in offline mode

        logging.info("open first pending contact group on the list")

        if "emulator" in platform:  # there is no automatic way to disable networking on iOS emulators
            contacts_page = LoadClass.load_page('ContactsPage')
            contacts_page.setDriver(self.driver)
            contacts_page.clear_Search_field()
            contacts_page.type_text_into_search_field("Offline Object - Contact Group")
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.click_Return_button_on_keyboard()
            common_page.hide_keyboard()
            contacts_page.open_first_contact_group()
        else:
            self.switch_context_to_webview()
            first_pending_contact_group = self.driver.find_element(*self.configuration.ContactsScreen.FIRST_PENDING_CONTACT_GROUP)
            self.assertIsNotNone(first_pending_contact_group, "first pending contact group, not found")
            first_pending_contact_group.click()
            self.switch_context_to_native()

    def open_offline_contacts_group(self):  # offline_contact_group

        logging.info('open offline contacts group = "offline_contact_group" ')

        if "emulator" in platform:  # there is no automatic way to disable networking on iOS emulators
            contacts_page = LoadClass.load_page('ContactsPage')
            contacts_page.setDriver(self.driver)
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            main_page = LoadClass.load_page('MainPage')
            main_page.setDriver(self.driver)
            common_page.hamburger_button()
            main_page.check_presence_of_inbox_button()
            main_page.scroll_down_to_contacts_button()
            main_page.open_CONTACTS()
            contacts_page.clear_Search_field()
            contacts_page.type_text_into_search_field("offline_contact_group")
            common_page.click_Return_button_on_keyboard()
            common_page.hide_keyboard()
            contacts_page.open_first_contact_group()
        else:
            self.switch_context_to_native()
            offline_contacts_group = self.driver.find_element(*self.configuration.ContactsScreen.OFFLINE_CONTACTS_GROUP)
            self.assertIsNotNone(offline_contacts_group, "offline contacts group not found")
            offline_contacts_group.click()
 
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    def open_first_pending_contact(self):    # pending contact in offline mode

        logging.info("open first pending contact on the list")

        if "emulator" in platform:  # there is no automatic way to disable networking on iOS emulators
            contacts_page = LoadClass.load_page('ContactsPage')
            contacts_page.setDriver(self.driver)
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            # main_page = LoadClass.load_page('MainPage')
            # main_page.setDriver(self.driver)
            # common_page.hamburger_button()
            # main_page.check_presence_of_inbox_button()
            # main_page.scroll_down_to_contacts_button()
            # main_page.open_CONTACTS()
            contacts_page.clear_Search_field()
            # contacts_page.type_text_into_search_field("offline_contact_group")
            contacts_page.type_text_into_search_field("Offline Object - Contact")
            common_page.click_Return_button_on_keyboard()
            common_page.hide_keyboard()
            contacts_page.click_first_contact_on_the_list()
        else:
            self.switch_context_to_webview()
            first_pending_contact = self.driver.find_element(*self.configuration.ContactsScreen.FIRST_PENDING_CONTACT)
            self.assertIsNotNone(first_pending_contact, "first pending contact not found")
            first_pending_contact.click()
            self.switch_context_to_native()

        self.switch_context_to_native()


