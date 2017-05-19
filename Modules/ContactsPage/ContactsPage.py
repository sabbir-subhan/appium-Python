"""A class for methods to handle Contacts Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
import logging
from time import sleep
from credentials import Credentials
from appium.webdriver.common.touch_action import TouchAction


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

    def scroll_down_to_write_access_level(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.scroll_down_to_write_access_level()

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

        sleep(1)
        logging.info("open contact group")
        second_contact_group = self.driver.find_element(*self.configuration.ContactsScreen.SECOND_CONTACT_GROUP)
        self.assertIsNotNone(second_contact_group, "second contact group not found")
        second_contact_group.click()

        self.switch_context_to_native()
        sleep(0.5)

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

        self.switch_context_to_native()
        sleep(2)

    def click_more_button(self):

        sleep(1)
        self.switch_context_to_webview()

        logging.info("click More button")
        more_button = self.driver.find_element(*self.configuration.ContactsScreen.CONTACT_MORE_BUTTON)
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

    def check_if_edit_button_is_visible(self):

        logging.info("check if edit button is visible")
        try:
            edit_button = self.driver.find_element(*self.configuration.EventDetailsScreen.EDIT_BUTTON)
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

    def hide_popup(self):

        logging.info("touch middle of the screen to hide popup")
        sleep(0.5)
        action = TouchAction(self.driver)
        screen_size = self.driver.get_window_size(windowHandle='current')  # it creates dictionary
        start_x = screen_size["width"] * 0.5
        start_y = screen_size["height"] * 0.5
        action.tap(element=None, x=start_x, y=start_y, count=1).perform()
        sleep(0.5)

    def click_write_access_level(self):

        self.switch_context_to_webview()

        logging.info("click write access level")
        click_write_access_level = self.driver.find_element(*self.configuration.ContactsScreen.WRITE_ACCESS_LEVEL)
        self.assertIsNotNone(click_write_access_level, "write access level not found")
        click_write_access_level.click()

        self.switch_context_to_native()

    def choose_administrators_only_as_write_access_level(self):

        self.switch_context_to_webview()

        logging.info("choose 'administrators only' as write access level")
        choose_administrators_only_as_write_access_level = self.driver.find_element(*self.configuration.ContactsScreen.CHOOSE_ADMINISTRATORS_ONLY_AS_WRITE_ACCESS_LEVEL)
        self.assertIsNotNone(choose_administrators_only_as_write_access_level, "write access level not found")
        choose_administrators_only_as_write_access_level.click()

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

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.click_on_option_1()

    def click_on_option_2(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.click_on_option_2()

    def click_on_option_3(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.click_on_option_3()

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

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.check_hidden_field_1()

    def check_hidden_fields_1_and_2(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.check_hidden_fields_1_and_2()


