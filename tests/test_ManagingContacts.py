# Test Case - Managing Contacts -- OCAMOB-54

# before running this test create:

# create new contact type in OCA, named: "Person"
# - contact type with on load and on save sequence (with default value = "test on load") and on save sequence, named: "contact_with_on_load_sequence" (like in TC: Managing Events)
# - contact type with visibility rules, named: "contact_with_visibility_rules", with fields "New option list" - with options; "1", "2", "3" that options should restore 3 other fields. "field to restore",
# "New website address" with value: "http://bitnoi.se/" and "New email address" with value: "test@noggin.com" - visibility rules like in TC: Managing Events
# (option 1 restores 'field to restore', option 2 restores 'New email address', option 3 restores 'New website address')


# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present

# From the main menu press Contacts.
# Press a contact group.
# Press New > Add new contact in this group.
# Press a contact type.
# Fill in the fields in the form and press Save.

# Open your own contact details. Click More > Delete Contact.

# Open an existing contact that is not your contact.
# Press Edit. Make changes to the fields in the form. Press Save.
# Press More > Delete. Press Delete on the prompt that appears. Search for the contact.

# Press More > Send communication. Add a message type and send.
# Open a contact. Press More > Save to device. Press OK on the prompt.
# Open a contact you have read access to but not write access.
# Open a contact group. Select New > Import contact from device contacts.
# Select a device contact and a contact type.
# On OCA Server (the website), configure a contact type to have an on load sequence and on save sequence in two of its fields.
# On the mobile app, create contacts of this type.
# Open new contacts but don't save them.
# Create a contact that has option lists and fields with visibility rules that clears hidden fields and restores default values.

from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest
from configuration import PROJECT_ROOT


class TestManagingContacts(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        self.driver.save_screenshot(PROJECT_ROOT + "/screenshots/test_ManageContacts.png")

        self.driver.quit()

    def test_ManageContacts(self):

        logging.info("starting Test Case: Managing Contacts")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        welcome_page = LoadClass.load_page('WelcomePage')
        welcome_page.setDriver(self.driver)
        welcome_page.click_login_button()
        login_page = LoadClass.load_page('LoginPage')
        login_page.setDriver(self.driver)
        login_page.type_domain_address('QA')
        common_page.hide_keyboard()
        login_page.click_submit_button()
        login_page.type_username('QA')
        login_page.type_password('QA')
        common_page.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        common_page.wait_for_app_loading()
        main_page = LoadClass.load_page('MainPage')
        main_page.setDriver(self.driver)
        main_page.alert_expiring_password()
        main_page.dismiss_notifications()
        main_page.check_presence_of_events_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page = LoadClass.load_page('ContactsPage')
        contacts_page.setDriver(self.driver)
        contacts_page.open_contacts_group()  # Contacts
        contacts_page.click_new_button()
        contacts_page.add_new_contact_into_group()
        contacts_page.choose_contact_type_person()
        contacts_page.type_first_name_for_new_contact("Appium")
        contacts_page.scroll_down_to_save_button()
        contacts_page.save_new_contact()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.clear_Search_field()
        contacts_page.type_username_into_search_field()
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.click_first_contact_on_the_list()
        contacts_page.click_contact_more_button()
        contacts_page.delete_contact()
        contacts_page.confirm_delete()

        contacts_page.cancel_delete()  # app bug - lack of error msg

        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.clear_Search_field()
        contacts_page.type_text_into_search_field("Appium")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.click_first_contact_on_the_list()
        contacts_page.click_edit_button()
        contacts_page.clear_first_name()
        contacts_page.type_first_name_for_edit_contact("delete")
        contacts_page.fill_organisation_field("Bitnoise")
        common_page.hide_keyboard()
        contacts_page.scroll_down_to_save_button()
        contacts_page.save_edited_contact()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        contacts_page.click_contact_more_button()
        contacts_page.delete_contact()
        contacts_page.confirm_delete()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.clear_Search_field()
        contacts_page.type_text_into_search_field("delete")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.check_results_for_deleted_contact()
        contacts_page.clear_Search_field()
        common_page.hide_keyboard()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.clear_Search_field()
        common_page.hide_keyboard()
        contacts_page.open_contacts_group()  # Contacts
        contacts_page.click_new_button()
        contacts_page.add_new_contact_into_group()
        contacts_page.choose_contact_type_person()
        contacts_page.type_first_name_for_new_contact("Communication")
        contacts_page.scroll_down_to_email_field()
        contacts_page.type_email_address("test90@onet.pl")
        contacts_page.scroll_down_to_write_access_level()
        contacts_page.click_write_access_level_for_new_contact()
        contacts_page.option_list_administrators_only()
        contacts_page.scroll_down_to_save_button()
        contacts_page.save_new_contact()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.clear_Search_field()
        contacts_page.type_text_into_search_field("Communication")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.click_first_contact_on_the_list()
        contacts_page.click_contact_more_button()
        contacts_page.click_send_communication()
        compose_page = LoadClass.load_page('ComposePage')
        compose_page.setDriver(self.driver)
        compose_page.choose_email_message()
        compose_page.type_email_subject()
        compose_page.type_email_message()
        common_page.hide_keyboard()
        compose_page.click_email_ok_button()
        compose_page.click_send_button()
        compose_page.alert_send_button()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.clear_Search_field()
        common_page.hide_keyboard()
        contacts_page.type_text_into_search_field("Communication")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.click_first_contact_on_the_list()
        contacts_page.click_contact_more_button()
        contacts_page.save_contact_to_device()
        common_page.alert_popup_allow()
        contacts_page.hide_popup()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        # logout and login to general user to open contact details with only read access and check for 'Edit' button
        main_page.scroll_down_to_logout_button()
        main_page.click_logout_button()
        login_page.click_submit_button()
        common_page.wait_for_app_loading()
        welcome_page.click_login_button()
        login_page.click_submit_button()
        login_page.type_username('general_user')
        login_page.type_password('general_user')
        common_page.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        common_page.wait_for_app_loading()
        main_page.alert_expiring_password()
        main_page.dismiss_notifications()
        main_page.check_presence_of_events_button()
        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.clear_Search_field()
        contacts_page.type_text_into_search_field("Communication")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.click_first_contact_on_the_list()
        contacts_page.check_if_edit_button_is_visible()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        # Open a contact group. Select New > Import contact from device contacts.
        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.clear_Search_field()
        common_page.hide_keyboard()
        contacts_page.open_contacts_group()  # Contacts
        contacts_page.click_new_button()
        contacts_page.import_contact_from_device_to_this_group()
        common_page.alert_popup_allow()
        contacts_page.clear_Search_field()
        contacts_page.type_text_into_search_field("Communication")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.choose_first_contact_on_the_list_to_import_from_device()
        contacts_page.choose_contact_type_person()
        contacts_page.check_imported_contact_first_name_value()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        # Create contact with on load and on save sequence in two of its fields.
        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.clear_Search_field()
        common_page.hide_keyboard()
        contacts_page.open_contacts_group()  # Contacts
        contacts_page.click_new_button()
        contacts_page.add_new_contact_into_group()
        contacts_page.choose_contact_type_with_on_load_and_on_save_sequence()
        contacts_page.type_first_name_for_new_contact("on_load_sequence")
        contacts_page.scroll_down_to_on_load_field()
        contacts_page.check_on_load_and_on_save_sequences()
        contacts_page.scroll_down_to_save_button()
        contacts_page.save_new_contact()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.clear_Search_field()
        contacts_page.type_text_into_search_field("on_load")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.click_first_contact_on_the_list()
        contacts_page.click_edit_button()

        contacts_page.scroll_down_to_save_button()
        contacts_page.cancel_edited_contact()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        # Create contact with visibility rules.
        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.clear_Search_field()
        common_page.hide_keyboard()
        contacts_page.open_contacts_group()  # Contacts
        contacts_page.click_new_button()
        contacts_page.add_new_contact_into_group()
        contacts_page.choose_contact_type_with_visibility_rules()
        contacts_page.type_first_name_for_new_contact("visibility_rules")
        contacts_page.scroll_down_to_option_list()
        contacts_page.click_on_option_list()
        contacts_page.click_on_option_1()
        contacts_page.check_restored_field_1()
        contacts_page.click_on_option_list()
        contacts_page.click_on_option_2()
        contacts_page.check_restored_field_2()
        contacts_page.check_hidden_field_1()
        contacts_page.click_on_option_list()
        contacts_page.click_on_option_3()
        contacts_page.check_hidden_fields_1_and_2()
        contacts_page.check_restored_field_3()
        contacts_page.scroll_down_to_save_button()
        contacts_page.save_new_contact()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestManagingContacts)
    unittest.TextTestRunner(verbosity=2).run(suite)
