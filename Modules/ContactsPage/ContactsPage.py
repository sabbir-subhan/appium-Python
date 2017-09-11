"""A class for methods to handle Contacts Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
import logging
from time import sleep
from credentials import Credentials
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


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

    def click_address_field(self):

        sleep(1)
        self.switch_context_to_webview()

        logging.info("type address")
        address = self.driver.find_elements(*self.configuration.ContactsScreen.ADDRESS_FIELD)
        self.assertIsNotNone(address[0], "Address input field was not found")
        address[0].click()

        self.switch_context_to_native()

    def type_address_number(self, text):

        sleep(1)
        self.switch_context_to_webview()

        logging.info("type address number")
        address_number = self.driver.find_element(*self.configuration.ContactsScreen.ADDRESS_NUMBER)
        self.assertIsNotNone(address_number, "Address number input field was not found")
        address_number.click()
        address_number.send_keys(text)

        self.switch_context_to_native()

    def type_address_street(self, text):

        sleep(1)
        self.switch_context_to_webview()

        logging.info("type address street")
        address_street = self.driver.find_element(*self.configuration.ContactsScreen.ADDRESS_STREET)
        self.assertIsNotNone(address_street, "Address street input field was not found")
        address_street.click()
        address_street.send_keys(text)

        self.switch_context_to_native()

    def type_address_post_code(self, text):

        sleep(1)
        self.switch_context_to_webview()

        logging.info("type address post code")
        address_post_code = self.driver.find_element(*self.configuration.ContactsScreen.ADDRESS_POST_CODE)
        self.assertIsNotNone(address_post_code, "Address post code input field was not found")
        address_post_code.click()
        address_post_code.send_keys(text)

        self.switch_context_to_native()

    def type_address_country(self, text):

        sleep(1)
        self.switch_context_to_webview()

        logging.info("type address country")
        address_country = self.driver.find_element(*self.configuration.ContactsScreen.ADDRESS_COUNTRY)
        self.assertIsNotNone(address_country, "Address country input field was not found")
        address_country.click()
        address_country.send_keys(text)

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
        self.assertIsNotNone(first_name, "First name clear button was not found")
        first_name.click()

        self.switch_context_to_native()

    def clear_name_for_edited_contact_group(self):

        self.switch_context_to_webview()

        logging.info("clear name for edited contact group")
        first_name = self.driver.find_element(*self.configuration.ContactsScreen.CLEAR_NAME_FOR_EDITED_CONTACT_GROUP)
        self.assertIsNotNone(first_name, "Name clear field button was not found")
        first_name.click()

        self.switch_context_to_native()

    def clear_name_for_new_contact_group(self):

        self.switch_context_to_webview()

        logging.info("clear name for new contact group")

        first_name = self.driver.find_element(*self.configuration.ContactsScreen.CLEAR_NAME_FOR_NEW_CONTACT_GROUP)
        self.assertIsNotNone(first_name, "Name clear field button was not found")
        first_name.click()

        self.switch_context_to_native()

    def clear_name_for_offline_contact_group(self):

        ContactsPage.clear_name_for_new_contact_group(self)

        # self.switch_context_to_webview()
        #
        # logging.info("clear name for offline contact group")
        # first_name = self.driver.find_element(*self.configuration.ContactsScreen.CLEAR_NAME_FOR_NEW_CONTACT_GROUP)
        # self.assertIsNotNone(first_name, "Name clear field button was not found")
        # first_name.click()
        #
        # self.switch_context_to_native()

    # def clear_name_for_new_contact_group(self):
    #
    #     self.switch_context_to_webview()
    #
    #     logging.info("clear name for new contact group")
    #     try:
    #         first_name = self.driver.find_element(*self.configuration.ContactsScreen.CLEAR_NAME_FOR_NEW_CONTACT_GROUP)
    #         self.assertIsNotNone(first_name, "Name clear field button was not found")
    #         first_name.click()
    #     except NoSuchElementException and ElementNotVisibleException and WebDriverException:
    #         first_name = self.driver.find_element(*self.configuration.ContactsScreen.CLEAR_NAME_FOR_EDITED_CONTACT_GROUP)
    #         self.assertIsNotNone(first_name, "Name clear field button was not found")
    #         first_name.click()
    #
    #     self.switch_context_to_native()

    def scroll_down_to_write_access_level(self):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.scroll_down_to_write_access_level()

    def scroll_down_to_save_button(self):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.scroll_down_to_save_button()

    def save_offline_contact(self):

        self.switch_context_to_webview()

        logging.info('click Save button')
        save_button = self.driver.find_element(*self.configuration.ContactsScreen.SAVE_NEW_CONTACT)
        self.assertIsNot(save_button, "save button not found")
        save_button.click()

        self.switch_context_to_native()

    def save_new_contact(self):

        self.switch_context_to_webview()

        logging.info('click Save button')
        save_button = self.driver.find_element(*self.configuration.ContactsScreen.SAVE_NEW_CONTACT)
        self.assertIsNot(save_button, "save button not found")
        save_button.click()

        self.switch_context_to_native()

    def save_edited_contact(self):

        self.switch_context_to_webview()

        logging.info('click Save button')
        save_button = self.driver.find_element(*self.configuration.ContactsScreen.SAVE_EDITED_CONTACT)
        save_button.click()

        self.switch_context_to_native()

    def cancel_new_contact(self):

        self.switch_context_to_webview()

        logging.info('click Cancel button')
        cancel_button = self.driver.find_element(*self.configuration.ContactsScreen.CANCEL_NEW_CONTACT)
        cancel_button.click()

        self.switch_context_to_native()

    def cancel_edited_contact(self):

        self.switch_context_to_webview()

        logging.info('click Cancel button')
        cancel_button = self.driver.find_element(*self.configuration.ContactsScreen.CANCEL_EDITED_CONTACT)
        cancel_button.click()

        self.switch_context_to_native()
        sleep(1)

    def open_first_contact_group(self):

        self.switch_context_to_webview()

        sleep(1)
        logging.info("open first contact group")
        first_contact_group = self.driver.find_element(*self.configuration.ContactsScreen.FIRST_CONTACT_GROUP)
        self.assertIsNotNone(first_contact_group, "first contact group not found")
        first_contact_group.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    # def open_second_contact_group(self):  # Contacts
    #
    #     self.switch_context_to_webview()
    #
    #     sleep(1)
    #     logging.info("open second contact group - Contacts")
    #     second_contact_group = self.driver.find_element(*self.configuration.ContactsScreen.SECOND_CONTACT_GROUP)
    #     self.assertIsNotNone(second_contact_group, "second contact group not found")
    #     second_contact_group.click()
    #
    #     self.switch_context_to_native()
    #     sleep(0.5)
    #
    #     common_page = LoadClass.load_page('CommonPage')
    #     common_page.setDriver(self.driver)
    #     common_page.wait_for_app_loading()

    def open_contacts_group(self):  # Contacts

        sleep(1)
        logging.info("open contacts group")
        second_contact_group = self.driver.find_element(*self.configuration.ContactsScreen.CONTACTS_GROUP)
        self.assertIsNotNone(second_contact_group, "contacts group not found")
        second_contact_group.click()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    def open_mailing_list_group(self):  # Mailing list unsubscribes

        sleep(1)
        logging.info("open Mailing list unsubscribes group")
        second_contact_group = self.driver.find_element(*self.configuration.ContactsScreen.MAILING_LIST_GROUP)
        self.assertIsNotNone(second_contact_group, "Mailing list unsubscribes group not found")
        second_contact_group.click()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    def open_users_group(self):  # Users

        sleep(1)
        logging.info("open Users group")
        second_contact_group = self.driver.find_element(*self.configuration.ContactsScreen.USERS_GROUP)
        self.assertIsNotNone(second_contact_group, "Users group not found")
        second_contact_group.click()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    def open_offline_contacts_group(self):  # offline_contact_group

        sleep(1)
        logging.info('open offline contacts group = "offline_contact_group" ')
        offline_contacts_group = self.driver.find_element(*self.configuration.ContactsScreen.OFFLINE_CONTACTS_GROUP)
        self.assertIsNotNone(offline_contacts_group, "offline contacts group not found")
        offline_contacts_group.click()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    # def open_third_contact_group(self):  # Mailing list unsubscribes
    #
    #     self.switch_context_to_webview()
    #
    #     sleep(1)
    #     logging.info("open third contact group - Mailing list unsubscribes")
    #     third_contact_group = self.driver.find_element(*self.configuration.ContactsScreen.THIRD_CONTACT_GROUP)
    #     self.assertIsNotNone(third_contact_group, "third contact group not found")
    #     third_contact_group.click()
    #
    #     self.switch_context_to_native()
    #
    #     common_page = LoadClass.load_page('CommonPage')
    #     common_page.setDriver(self.driver)
    #     common_page.wait_for_app_loading()

    def click_new_button(self):

        self.switch_context_to_webview()

        logging.info("click New button")
        new_button = self.driver.find_element(*self.configuration.ContactsScreen.NEW_BUTTON)
        self.assertIsNotNone(new_button, "new button not found")
        new_button.click()

        self.switch_context_to_native()

    def click_group_info_button(self):

        self.switch_context_to_webview()

        logging.info("click Group info button")
        group_info_button = self.driver.find_element(*self.configuration.ContactsScreen.GROUP_INFO_BUTTON)
        self.assertIsNotNone(group_info_button, "Group info button not found")
        group_info_button.click()

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

    def choose_first_contact_on_the_list_to_import_from_device(self):

        self.switch_context_to_webview()

        logging.info("choose first contact on the list to import from device")
        choose_first_contact_on_the_list_to_import_from_device = self.driver.find_element(*self.configuration.ContactsScreen.FIRST_CONTACT_ON_THE_LIST_TO_IMPORT_FROM_DEVICE)
        self.assertIsNotNone(choose_first_contact_on_the_list_to_import_from_device, "first contact on the list to import from device not found")
        choose_first_contact_on_the_list_to_import_from_device.click()

        self.switch_context_to_native()
        sleep(2)

    def choose_contact_type_person(self):

        logging.info("click contact type = Person")
        contact_type_person = self.driver.find_element(*self.configuration.ContactsScreen.CONTACT_TYPE_PERSON)
        self.assertIsNotNone(contact_type_person, "contact type 'Person' not found")
        contact_type_person.click()

    def choose_contact_type_contact_with_rich_text(self):

        logging.info("click contact type = contact_with_rich_text")
        contact_with_rich_text = self.driver.find_element(*self.configuration.ContactsScreen.CONTACT_TYPE_CONTACT_WITH_RICH_TEXT)
        self.assertIsNotNone(contact_with_rich_text, "contact type 'contact_with_rich_text' not found")
        contact_with_rich_text.click()

    def choose_contact_type_with_on_load_and_on_save_sequence(self):

        logging.info("click contact type = contact_with_on_load_and_on_save_sequence")
        contact_type_with_on_load_sequence = self.driver.find_element(*self.configuration.ContactsScreen.CONTACT_TYPE_WITH_ON_LOAD_SEQUENCE)
        self.assertIsNotNone(contact_type_with_on_load_sequence, "contact type 'contact_with_on_load_and_on_save_sequence' not found")
        contact_type_with_on_load_sequence.click()

    def choose_contact_type_with_visibility_rules(self):

        logging.info("click contact type = contact_with_visibility_rules")
        contact_type_with_visibility_rules = self.driver.find_element(*self.configuration.ContactsScreen.CONTACT_TYPE_WITH_VISIBILITY_RULES)
        self.assertIsNotNone(contact_type_with_visibility_rules, "contact type 'contact_with_visibility_rules' not found")
        contact_type_with_visibility_rules.click()

    def type_username_into_search_field(self):

        logging.info("filter contacts by search field")

        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        self.assertIsNotNone(search_field, "Search field not found")
        search_field.click()
        sleep(2)
        search_field.send_keys(Credentials.QA_username)
        sleep(1)

    def type_text_into_search_field(self, text):

        logging.info("type text into search field")

        self.switch_context_to_webview()

        search_field = self.driver.find_element(*self.configuration.ContactsScreen.SEARCH_FIELD)
        self.assertIsNotNone(search_field, "Search field not found")
        search_field.click()
        sleep(1)
        search_field.send_keys(text)
        sleep(1)

        self.switch_context_to_native()

    # def type_text_into_search_field(self, text):

        # logging.info("type text into search field")

        # search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        # self.assertIsNotNone(search_field, "Search field not found")
        # search_field.click()
        # sleep(2)
        # search_field.send_keys(text)
        # sleep(1)

        # events_page = LoadClass.load_page('EventsPage')
        # events_page.setDriver(self.driver)
        # events_page.type_text_into_search_field(text)

    def click_first_contact_on_the_list(self):

        sleep(1)
        self.switch_context_to_webview()
        sleep(1)
        logging.info('click first contact on the list')
        first_contact_on_the_list = self.driver.find_element(*self.configuration.ContactsScreen.FIRST_CONTACT_ON_THE_LIST)  # first-child
        self.assertIsNotNone(first_contact_on_the_list, 'first contact on the list, not found')
        first_contact_on_the_list.click()

        self.switch_context_to_native()

    def open_first_pending_contact(self):    # pending contact in offline mode

        self.switch_context_to_webview()

        logging.info("open first pending contact on the list")
        first_pending_contact = self.driver.find_element(*self.configuration.ContactsScreen.FIRST_PENDING_CONTACT)
        self.assertIsNotNone(first_pending_contact, "first pending contact not found")
        first_pending_contact.click()

        self.switch_context_to_native()

    def open_first_pending_contact_group(self):    # pending contact group in offline mode

        self.switch_context_to_webview()

        logging.info("open first pending contact group on the list")
        first_pending_contact_group = self.driver.find_element(*self.configuration.ContactsScreen.FIRST_PENDING_CONTACT_GROUP)
        self.assertIsNotNone(first_pending_contact_group, "first pending contact group, not found")
        first_pending_contact_group.click()

        self.switch_context_to_native()

    def click_first_contact_on_the_list_with_checkbox(self):

        sleep(1)
        self.switch_context_to_webview()

        logging.info('click first contact on the list with checkbox')
        first_contact_on_the_list = self.driver.find_element(*self.configuration.ContactsScreen.FIRST_CONTACT_ON_THE_LIST_WITH_CHECKBOX)  # first-child
        self.assertIsNotNone(first_contact_on_the_list, 'first contact on the list, not found')
        first_contact_on_the_list.click()

        self.switch_context_to_native()

    def click_first_contact_on_the_list_with_checkbox_in_offline_mode(self):

        sleep(1)
        self.switch_context_to_webview()

        try:
            logging.info('click first contact on the list with checkbox in offline mode')
            first_contact_on_the_list = self.driver.find_element(*self.configuration.ContactsScreen.FIRST_CONTACT_ON_THE_LIST_WITH_CHECKBOX_IN_OFFLINE_MODE)  # first-child
            self.assertIsNotNone(first_contact_on_the_list, 'first contact on the list in offline mode, not found')
            first_contact_on_the_list.click()
        except NoSuchElementException:
            ContactsPage.click_first_contact_on_the_list_with_checkbox(self)

        self.switch_context_to_native()

    def click_first_contact_group_on_the_list(self):

        self.switch_context_to_webview()

        logging.info('click first contact group on the list')
        first_contact_group_on_the_list = self.driver.find_element(*self.configuration.ContactsScreen.FIRST_CONTACT_GROUP_ON_THE_LIST_WITH_CHECKBOX)  # first-child
        self.assertIsNotNone(first_contact_group_on_the_list, 'first contact group on the list, not found')
        first_contact_group_on_the_list.click()

        self.switch_context_to_native()

    def click_contact_more_button(self):

        sleep(1)
        self.switch_context_to_webview()

        logging.info("click More button")
        more_button = self.driver.find_element(*self.configuration.ContactsScreen.CONTACT_MORE_BUTTON)
        self.assertIsNotNone(more_button, "More button not found")
        more_button.click()

        self.switch_context_to_native()

    def click_group_more_button(self):

        sleep(1)
        self.switch_context_to_webview()

        logging.info("click More button")
        more_button = self.driver.find_element(*self.configuration.ContactsScreen.CONTACT_GROUP_MORE_BUTTON)
        self.assertIsNotNone(more_button, "More button not found")
        more_button.click()

        self.switch_context_to_native()

    def click_more_button_to_hide_popup(self):

        pass
    
    def delete_contact(self):

        self.switch_context_to_webview()

        logging.info("click delete button")
        delete_button = self.driver.find_element(*self.configuration.ContactsScreen.DELETE_CONTACT)
        self.assertIsNotNone(delete_button, "delete button not found")
        delete_button.click()

        self.switch_context_to_native()

    def delete_contact_group(self):

        self.switch_context_to_webview()

        logging.info("click delete button")
        delete_button = self.driver.find_element(*self.configuration.ContactsScreen.DELETE_CONTACT_GROUP)
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

    def confirm_delete_contact_group(self):

        self.switch_context_to_webview()

        logging.info("click confirm delete")
        delete_button = self.driver.find_element(*self.configuration.ContactsScreen.CONFIRM_DELETE_GROUP)
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

        sleep(1)

    def check_if_edit_button_is_visible(self):

        logging.info("check if edit button is visible")
        try:
            edit_button = self.driver.find_element(*self.configuration.EventDetailsScreen.EDIT_BUTTON)
            sleep(1)
            if edit_button.is_displayed():
                self.fail("Edit button is visible but it should not, because of write access level set to"
                          " 'administrators only'")
            else:
                pass
        except NoSuchElementException:
            logging.info("Edit button not found = OK")
            pass

    def fill_organisation_field(self, text):

        self.switch_context_to_webview()

        logging.info("fill organisation field")
        organisation_field = self.driver.find_element(*self.configuration.ContactsScreen.ORGANISATION_FIELD)
        self.assertIsNotNone(organisation_field, "organisation field not found")
        organisation_field.send_keys(text)

        self.switch_context_to_native()

    # def clear_Search_field(self):
    #
    #     logging.info("clear search field")
    #     # self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).click()
    #     # sleep(1)
    #     # self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
    #     # sleep(2)
    #
    #     field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
    #     field.click()
    #     # print(field.text)
    #     while len(field.text) > 0:
    #         field.clear()
    #
    #     # if len(field.text) > 0:
    #     #     field.clear()
    #     # else:
    #     #     pass
    #     sleep(1)

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

        logging.info("click send communication button for Contact")
        click_send_communication = self.driver.find_element(*self.configuration.ContactsScreen.CONTACT_SEND_COMMUNICATION)
        self.assertIsNotNone(click_send_communication, "send communication button not found")
        click_send_communication.click()

        self.switch_context_to_native()

    def group_send_communication(self):

        self.switch_context_to_webview()

        logging.info("click send communication button for Contact Group")
        click_send_communication = self.driver.find_element(*self.configuration.ContactsScreen.GROUP_SEND_COMMUNICATION)
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

    def hide_popup(self):

        logging.info("touch middle of the screen to hide popup")
        sleep(0.5)
        action = TouchAction(self.driver)
        screen_size = self.driver.get_window_size(windowHandle='current')  # it creates dictionary
        start_x = screen_size["width"] * 0.5
        start_y = screen_size["height"] * 0.5
        action.tap(element=None, x=start_x, y=start_y, count=1).perform()
        sleep(0.5)

    def click_read_access_level_for_new_group(self):  # for new contact group

        self.switch_context_to_webview()

        logging.info("click read access level")
        click_read_access_level = self.driver.find_element(*self.configuration.ContactsScreen.READ_ACCESS_LEVEL_FOR_NEW_GROUP)
        self.assertIsNotNone(click_read_access_level, "read access level not found")
        click_read_access_level.click()

        self.switch_context_to_native()

    def click_write_access_level_for_new_contact(self):  # for new contact

        self.switch_context_to_webview()

        logging.info("click write access level for new contact")
        click_write_access_level = self.driver.find_element(*self.configuration.ContactsScreen.WRITE_ACCESS_LEVEL_FOR_NEW_CONTACT)
        self.assertIsNotNone(click_write_access_level, "write access level not found")
        click_write_access_level.click()

        self.switch_context_to_native()

    def option_list_administrators_only(self):

        self.switch_context_to_webview()

        logging.info("choose 'administrators only' from option list")
        sleep(1)
        option_list_administrators_only = self.driver.find_element(*self.configuration.ContactsScreen.OPTION_LIST_ADMINISTRATORS_ONLY)
        self.assertIsNotNone(option_list_administrators_only, "administrators only access level not found")
        sleep(1)
        option_list_administrators_only.click()
        sleep(1)

        self.switch_context_to_native()

    def check_imported_contact_first_name_value(self):

        sleep(1)
        logging.info("check imported contact first name value - it should be: 'Communication' ")
        check_imported_contact_first_name_value = self.driver.find_element(*self.configuration.ContactsScreen.IMPORTED_CONTACT_FIRST_NAME_VALUE)
        self.assertIsNotNone(check_imported_contact_first_name_value, "first name value not found")

    def check_on_load_and_on_save_sequences(self):

        self.switch_context_to_webview()

        logging.info("assert on load and on save sequence")
        sequence_on_load = self.driver.find_element(*self.configuration.ContactsScreen.SEQUENCE_ON_LOAD)
        self.assertIsNotNone(sequence_on_load, "on load sequence not found")

        sequence_on_save = self.driver.find_element(*self.configuration.ContactsScreen.SEQUENCE_ON_SAVE)
        self.assertIsNotNone(sequence_on_save, "on save sequence not found")

        self.switch_context_to_native()

        sequence_on_load_value = self.driver.find_element(*self.configuration.EventEditScreen.SEQUENCE_ONLOAD_VALUE)
        self.assertIsNotNone(sequence_on_load_value, "on load sequence value not found")

        sequence_on_save_value = self.driver.find_element(*self.configuration.ContactsScreen.SEQUENCE_ONSAVE_VALUE)
        self.assertIsNotNone(sequence_on_save_value, "on save sequence value not found")

    def click_on_option_list(self):

        self.switch_context_to_webview()

        logging.info("click on Option list")
        option_list = self.driver.find_element(*self.configuration.ContactsScreen.OPTION_LIST)
        self.assertIsNotNone(option_list, "option list not found")
        option_list.click()

        self.switch_context_to_native()

    def click_on_option_1(self):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.click_on_option_1()

    def click_on_option_2(self):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.click_on_option_2()

    def click_on_option_3(self):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.click_on_option_3()

    def check_restored_field_1(self):

        logging.info("assert restored field 1")

        self.switch_context_to_webview()

        field_to_restore_1_header = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_1_HEADER)
        self.assertIsNotNone(field_to_restore_1_header)

        self.switch_context_to_native()

        sleep(1)
        field_to_restore_1_value = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_1_VALUE)
        self.assertIsNotNone(field_to_restore_1_value, "field to restore 1 value not found")

    def check_restored_field_2(self):

        logging.info("assert restored field 2")

        self.switch_context_to_webview()

        field_to_restore_2_header = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_2_HEADER)
        self.assertIsNotNone(field_to_restore_2_header)

        self.switch_context_to_native()

        sleep(1)
        field_to_restore_2_value = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_2_VALUE)
        self.assertIsNotNone(field_to_restore_2_value, "field to restore 2 value not found")

    def check_restored_field_3(self):

        logging.info("assert restored field 3")

        self.switch_context_to_webview()

        field_to_restore_3_header = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_3_HEADER)
        self.assertIsNotNone(field_to_restore_3_header)

        self.switch_context_to_native()

        sleep(1)
        field_to_restore_3_value = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_3_VALUE)
        self.assertIsNotNone(field_to_restore_3_value, "field to restore 3 value not found")

    def check_hidden_field_1(self):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.check_hidden_field_1()

    def check_hidden_fields_1_and_2(self):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.check_hidden_fields_1_and_2()

    def clear_Search_field(self):

        self.switch_context_to_webview()

        try:
            clear_search_field_button = self.driver.find_element(*self.configuration.ContactsScreen.CLEAR_SEARCH_FIELD_BUTTON)
            if clear_search_field_button.is_displayed():
                logging.info("clear Search field by clicking clear button")
                self.assertIsNotNone(clear_search_field_button, "clear search field button not found")
                clear_search_field_button.click()
                sleep(2)
        except NoSuchElementException:
            pass

        self.switch_context_to_native()

    def choose_group_for_new_contact_group_type(self):  # Group

        logging.info("choose new contact group type = 'Group' ")
        choose_group_for_new_contact_group_type = self.driver.find_element(*self.configuration.ContactsScreen.NEW_CONTACT_GROUP_TYPE_GROUP)
        self.assertIsNotNone(choose_group_for_new_contact_group_type, "new contact group type = 'Group' not found")
        choose_group_for_new_contact_group_type.click()

    def choose_group_type_with_on_load_and_on_save_sequence(self):  # contact_group_with_visibility_rules

        logging.info("choose new contact group type = 'contact_group_with_visibility_rules' ")
        choose_group_type_with_on_load_and_on_save_sequence = self.driver.find_element(*self.configuration.ContactsScreen.NEW_CONTACT_GROUP_WITH_ON_LOAD_SEQUENCE)
        self.assertIsNotNone(choose_group_type_with_on_load_and_on_save_sequence, "new contact group type = 'contact_group_with_visibility_rules' not found")
        choose_group_type_with_on_load_and_on_save_sequence.click()

    def choose_group_with_rich_text_type(self):  # contact_group_with_rich_text

        logging.info("choose new contact group type = 'contact_group_with_rich_text' ")
        choose_group_with_rich_text_type = self.driver.find_element(*self.configuration.ContactsScreen.NEW_CONTACT_GROUP_TYPE_CONTACT_GROUP_WITH_RICH_TEXT)
        self.assertIsNotNone(choose_group_with_rich_text_type, "new contact group type = 'contact_group_with_rich_text' not found")
        choose_group_with_rich_text_type.click()

    def type_name_for_new_contact_group(self, text):

        self.switch_context_to_webview()

        logging.info("Type Name for new contact group")
        name_field = self.driver.find_element(*self.configuration.ContactsScreen.NAME_FIELD_FOR_NEW_CONTACT_GROUP)
        self.assertIsNotNone(name_field, "name field not found")
        name_field.click()
        name_field.send_keys(text)

        self.switch_context_to_native()

    def type_name_for_offline_contact_group(self, text):

        ContactsPage.type_name_for_new_contact_group(self, text)

        # self.switch_context_to_webview()
        #
        # logging.info("Type Name for offline contact group")
        # name_field = self.driver.find_element(*self.configuration.ContactsScreen.NAME_FIELD_FOR_NEW_CONTACT_GROUP)
        # self.assertIsNotNone(name_field, "name field not found")
        # name_field.click()
        # name_field.send_keys(text)
        #
        # self.switch_context_to_native()

    def type_name_for_edited_contact_group(self, text):

        self.switch_context_to_webview()

        logging.info("Type Name for edited contact group")
        name_field = self.driver.find_element(*self.configuration.ContactsScreen.NAME_FIELD_FOR_EDITED_CONTACT_GROUP)
        self.assertIsNotNone(name_field, "name field not found")
        name_field.click()
        name_field.send_keys(text)

        self.switch_context_to_native()

    def save_offline_contact_group(self):

        ContactsPage.save_new_contact_group(self)

        # self.switch_context_to_webview()
        #
        # logging.info('click Save button')
        # save_button = self.driver.find_element(*self.configuration.ContactsScreen.SAVE_NEW_CONTACT_GROUP)
        # self.assertIsNot(save_button, "save button not found")
        # save_button.click()
        #
        # self.switch_context_to_native()

    def save_new_contact_group(self):

        self.switch_context_to_webview()

        logging.info('click Save button')
        save_button = self.driver.find_element(*self.configuration.ContactsScreen.SAVE_NEW_CONTACT_GROUP)
        self.assertIsNot(save_button, "save button not found")
        save_button.click()

        self.switch_context_to_native()

    def save_edited_contact_group(self):

        self.switch_context_to_webview()

        logging.info('click Save button')
        save_button = self.driver.find_element(*self.configuration.ContactsScreen.SAVE_EDITED_CONTACT_GROUP)
        self.assertIsNot(save_button, "save button not found")
        save_button.click()

        self.switch_context_to_native()

    def cancel_new_contact_group(self):

        self.switch_context_to_webview()

        logging.info('click Cancel button')
        cancel_button = self.driver.find_element(*self.configuration.ContactsScreen.CANCEL_NEW_CONTACT_GROUP)
        cancel_button.click()

        self.switch_context_to_native()

    def click_edit_group_button(self):

        self.switch_context_to_webview()

        logging.info('click Edit group button')
        save_button = self.driver.find_element(*self.configuration.ContactsScreen.EDIT_GROUP_BUTTON)
        save_button.click()

        self.switch_context_to_native()

    def check_first_contact_group_on_the_list(self):

        self.switch_context_to_webview()

        sleep(1)
        logging.info("check first contact group")
        try:
            check_first_contact_group_on_the_list = self.driver.find_element(*self.configuration.ContactsScreen.FIRST_CONTACT_GROUP)
            if check_first_contact_group_on_the_list.is_displayed():
                self.fail("first contact group on the list is displayed")
            else:
                pass
        except NoSuchElementException:
            logging.info("first contact group on the list not found = OK")

        self.switch_context_to_native()

    def check_notification_about_offline_mode(self):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.check_notification_about_offline_mode()

    def ok_button_on_offline_notification_popup_for_contact(self):

        self.switch_context_to_webview()

        logging.info("click Ok button on offline notification popup")
        try:
            ok_button = self.driver.find_element(*self.configuration.ContactsScreen.OK_BUTTON_ON_OFFLINE_NOTIFICATION_POPUP_FOR_NEW_CONTACT)
            self.assertIsNotNone(ok_button, "ok button not found")
            ok_button.click()
        except NoSuchElementException:
            logging.warning("offline notification popup not present")
        sleep(1)

        self.switch_context_to_native()

    def ok_button_on_offline_notification_popup_for_contact_group(self):

        self.switch_context_to_webview()

        logging.info("click Ok button on offline notification popup")
        try:
            ok_button = self.driver.find_element(*self.configuration.ContactsScreen.OK_BUTTON_ON_OFFLINE_NOTIFICATION_POPUP_FOR_NEW_CONTACT_GROUP)
            self.assertIsNotNone(ok_button, "ok button not found")
            ok_button.click()
        except NoSuchElementException:
            logging.warning("offline notification popup not present")
        sleep(1)

        self.switch_context_to_native()

    def check_presence_of_image_inside_rich_text_field_for_contact_group(self):

        logging.info("View object screen - check presence of image inside rich text field")

        self.switch_context_to_webview()

        self.driver.switch_to.frame(self.driver.find_element(
            *self.configuration.ContactsScreen.RICH_TEXT_IFRAME_VIEW_CONTACT_GROUP))
        image = self.driver.find_element(*self.configuration.ContactsScreen.RICH_TEXT_IFRAME_IMG_TAG)
        self.assertIsNotNone(image, "image tag not found")

        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            self.configuration.ContactsScreen.RICH_TEXT_IFRAME_IMAGE_NAME_CONTACT_GROUP))

        self.driver.switch_to.default_content()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.get_page_source()

        self.switch_context_to_native()

    def check_presence_of_image_inside_rich_text_field_for_contact(self):

        logging.info("View object screen - check presence of image inside rich text field")

        self.switch_context_to_webview()

        self.driver.switch_to.frame(self.driver.find_element(
            *self.configuration.ContactsScreen.RICH_TEXT_IFRAME_VIEW_CONTACT))
        image = self.driver.find_element(*self.configuration.ContactsScreen.RICH_TEXT_IFRAME_IMG_TAG)
        self.assertIsNotNone(image, "image tag not found")

        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            self.configuration.ContactsScreen.RICH_TEXT_IFRAME_IMAGE_NAME_CONTACT))

        self.driver.switch_to.default_content()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.get_page_source()

        self.switch_context_to_native()




