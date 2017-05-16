"""A class for methods to handle Contacts Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
import logging
from time import sleep
from credentials import Credentials


class ContactsPage(BasePage):

    def type_first_name_for_new_contact(self, text):

        sleep(1)
        self.switch_context_to_webview()

        logging.info("type first name")
        first_name = self.driver.find_element(*self.configuration.ContactsScreen.FIRST_NAME_FOR_NEW_CONTACT)
        self.assertIsNotNone(first_name, "First name input field was not found")
        first_name.click()
        first_name.send_keys(text)

        self.switch_context_to_native()

    def type_first_name_for_edit_contact(self, text):

        sleep(1)
        self.switch_context_to_webview()

        logging.info("type first name")
        first_name = self.driver.find_element(*self.configuration.ContactsScreen.FIRST_NAME_FOR_EDIT_CONTACT)
        self.assertIsNotNone(first_name, "First name input field was not found")
        first_name.click()
        first_name.send_keys(text)

        self.switch_context_to_native()

    def clear_first_name(self):

        self.switch_context_to_webview()

        logging.info("clear first name")
        first_name = self.driver.find_element(*self.configuration.ContactsScreen.FIRST_NAME_FOR_EDIT_CONTACT)
        self.assertIsNotNone(first_name, "First name input field was not found")
        first_name.clear()

        self.switch_context_to_native()

    def scroll_down_to_save_button(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.scroll_down_to_save_button()

    def save_new_contact(self):

        self.switch_context_to_webview()

        logging.info('click Save button')
        save_button = self.driver.find_element(*self.configuration.ContactsScreen.SAVE_NEW_CONTACT)
        save_button.click()

        self.switch_context_to_native()

    def save_edited_contact(self):

        self.switch_context_to_webview()

        logging.info('click Save button')
        save_button = self.driver.find_element(*self.configuration.ContactsScreen.SAVE_EDITED_CONTACT)
        save_button.click()

        self.switch_context_to_native()

    def open_first_contact_group(self):
        
        self.switch_context_to_webview()
        
        logging.info("open contact group")
        first_contact_group = self.driver.find_element(*self.configuration.ContactsScreen.FIRST_CONTACT_GROUP)
        self.assertIsNotNone(first_contact_group, "first contact group not found")
        first_contact_group.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    def open_second_contact_group(self):

        self.switch_context_to_webview()

        logging.info("open contact group")
        second_contact_group = self.driver.find_element(*self.configuration.ContactsScreen.SECOND_CONTACT_GROUP)
        self.assertIsNotNone(second_contact_group, "second contact group not found")
        second_contact_group.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    def open_third_contact_group(self):

        self.switch_context_to_webview()

        logging.info("open contact group")
        third_contact_group = self.driver.find_element(*self.configuration.ContactsScreen.THIRD_CONTACT_GROUP)
        self.assertIsNotNone(third_contact_group, "third contact group not found")
        third_contact_group.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    def click_new_button(self):

        self.switch_context_to_webview()

        logging.info("click New button")
        new_button = self.driver.find_element(*self.configuration.ContactsScreen.NEW_BUTTON)
        self.assertIsNotNone(new_button, "new button not found")
        new_button.click()

        self.switch_context_to_native()

    def add_new_contact_group(self):

        self.switch_context_to_webview()

        logging.info("click add new contact group in this group")
        new_contact_group = self.driver.find_element(*self.configuration.ContactsScreen.ADD_NEW_CONTACT_GROUP)
        self.assertIsNotNone(new_contact_group, "add new contact group in this group not found")
        new_contact_group.click()

        self.switch_context_to_native()

    def add_new_contact_into_group(self):

        self.switch_context_to_webview()

        logging.info("click add new contact in this group")
        new_contact = self.driver.find_element(*self.configuration.ContactsScreen.ADD_NEW_CONTACT_INTO_GROUP)
        self.assertIsNotNone(new_contact, "add new contact in this group not found")
        new_contact.click()

        self.switch_context_to_native()

    def import_contact_from_device_to_this_group(self):

        self.switch_context_to_webview()

        logging.info("click import contact from device to this group")
        new_contact_group = self.driver.find_element(*self.configuration.ContactsScreen.IMPORT_CONTACT_FROM_DEVICE_INTO_GROUP)
        self.assertIsNotNone(new_contact_group, "import contact from device to this group not found")
        new_contact_group.click()

        self.switch_context_to_native()

    def choose_contact_type_person(self):

        logging.info("click contact type = Person")
        new_contact_group = self.driver.find_element(*self.configuration.ContactsScreen.CONTACT_TYPE_PERSON)
        self.assertIsNotNone(new_contact_group, "contact type not found")
        new_contact_group.click()

    def type_username_into_search_field(self):

        logging.info("filter contacts by search field")

        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        self.assertIsNotNone(search_field, "Search field not found")
        search_field.click()
        sleep(2)
        search_field.send_keys(Credentials.QA_username)
        sleep(1)

    def type_text_into_search_field(self, text):

        logging.info("filter contacts by search field")

        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        self.assertIsNotNone(search_field, "Search field not found")
        search_field.click()
        sleep(2)
        search_field.send_keys(text)
        sleep(1)

    def edit_first_contact_on_the_list(self):

        self.switch_context_to_webview()

        logging.info('edit first contact on the list')
        first_contact_on_the_list = self.driver.find_elements(*self.configuration.ContactsScreen.FIRST_CONTACT_ON_THE_LIST)
        self.assertIsNotNone(first_contact_on_the_list, 'first contact on the list, not found')
        first_contact_on_the_list[0].click()
        sleep(2)

        self.switch_context_to_native()

    def click_more_button(self):

        self.switch_context_to_webview()

        logging.info("click More button")
        more_button = self.driver.find_element(*self.configuration.ContactsScreen.CONTACT_MORE_BUTTON)
        self.assertIsNotNone(more_button, "More button not found")
        more_button.click()

        self.switch_context_to_native()
    
    def delete_contact(self):

        self.switch_context_to_webview()

        logging.info("click delete button")
        delete_button = self.driver.find_element(*self.configuration.ContactsScreen.DELETE_CONTACT)
        self.assertIsNotNone(delete_button, "delete button not found")
        delete_button.click()

        self.switch_context_to_native()

    def confirm_delete(self):

        self.switch_context_to_webview()

        logging.info("click confirm delete")
        delete_button = self.driver.find_element(*self.configuration.ContactsScreen.CONFIRM_DELETE)
        self.assertIsNotNone(delete_button, "delete button not found")
        delete_button.click()

        self.switch_context_to_native()

    def cancel_delete(self):

        self.switch_context_to_webview()

        logging.info("click cancel button on popup")
        delete_button = self.driver.find_element(*self.configuration.ContactsScreen.CANCEL_DELETE)
        self.assertIsNotNone(delete_button, "cancel button not found")
        delete_button.click()

        self.switch_context_to_native()
        
    def click_edit_button(self):

        self.switch_context_to_webview()

        logging.info("click edit button")
        edit_button = self.driver.find_element(*self.configuration.ContactsScreen.CONTACT_EDIT_BUTTON)
        self.assertIsNotNone(edit_button, "edit button not found")
        edit_button.click()

        self.switch_context_to_native()

    def fill_organisation_field(self, text):

        self.switch_context_to_webview()

        logging.info("fill organisation field")
        organisation_field = self.driver.find_element(*self.configuration.ContactsScreen.ORGANISATION_FIELD)
        self.assertIsNotNone(organisation_field, "organisation field not found")
        organisation_field.send_keys(text)

        self.switch_context_to_native()

    def clear_Search_field(self):

        logging.info("clear search field")
        sleep(1)
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).click()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()  # each clear is clearing one character
        sleep(1)

    def check_results_for_deleted_contact(self):  # this method will search for contact with first name: "delete"

        logging.info("check results for deleted contact")
        try:
            deleted_contact = self.driver.find_element(*self.configuration.ContactsScreen.DELETED_CONTACT)
            if deleted_contact.is_displayed():
                self.fail("Contact was not deleted correctly")
            else:
                pass
        except NoSuchElementException:
            logging.info("Contact not found = OK")
            pass

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

    def type_email_address(self, text):

        self.switch_context_to_webview()

        logging.info("type email address")
        email_address = self.driver.find_elements(*self.configuration.ContactsScreen.EMAIL_FIELD)
        self.assertIsNotNone(email_address, "Email input field was not found")
        email_address[0].click()
        email_address[0].send_keys(text)

        self.switch_context_to_native()

    def click_send_communication(self):

        self.switch_context_to_webview()

        logging.info("click send communication button")
        click_send_communication = self.driver.find_element(*self.configuration.ContactsScreen.SEND_COMMUNICATION)
        self.assertIsNotNone(click_send_communication, "send communication button not found")
        click_send_communication.click()

        self.switch_context_to_native()

    def save_contact_to_device(self):

        self.switch_context_to_webview()

        logging.info("click save to device button")
        save_contact_to_device = self.driver.find_element(*self.configuration.ContactsScreen.SAVE_TO_DEVICE)
        self.assertIsNotNone(save_contact_to_device, "save to device button not found")
        save_contact_to_device.click()

        self.switch_context_to_native()





