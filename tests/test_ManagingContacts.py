# Test Case - Managing Contacts -- OCAMOB-54

# before running this test create:

# create two types of contacts in OCA - second contact type on the list should be a "Person"


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


class TestManagingContacts(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_manage_contacts(self):

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

        # main_page.scroll_down_to_contacts_button()
        # main_page.open_CONTACTS()
        contacts_page = LoadClass.load_page('ContactsPage')
        contacts_page.setDriver(self.driver)
        # contacts_page.open_second_contact_group()  # Contacts
        # contacts_page.click_new_button()
        # contacts_page.add_new_contact_into_group()
        # contacts_page.choose_contact_type_person()
        # contacts_page.type_first_name_for_new_contact("Appium")
        # contacts_page.scroll_down_to_save_button()
        # contacts_page.save_new_contact()
        # common_page.hamburger_button()
        # main_page.check_presence_of_inbox_button()
        #
        # main_page.scroll_down_to_contacts_button()
        # main_page.open_CONTACTS()
        # contacts_page.clear_Search_field()
        # contacts_page.type_username_into_search_field()
        # common_page.click_Return_button_on_keyboard()
        # common_page.hide_keyboard()
        # contacts_page.edit_first_contact_on_the_list()
        # contacts_page.click_more_button()
        # contacts_page.delete_contact()
        # contacts_page.confirm_delete()
        #
        # contacts_page.cancel_delete()  # app bug - lack of error msg
        #
        # common_page.hamburger_button()
        # main_page.check_presence_of_inbox_button()
        #
        # main_page.scroll_down_to_contacts_button()
        # main_page.open_CONTACTS()
        # contacts_page.clear_Search_field()
        # contacts_page.type_text_into_search_field("Appium")
        # common_page.click_Return_button_on_keyboard()
        # common_page.hide_keyboard()
        # contacts_page.edit_first_contact_on_the_list()
        # contacts_page.click_edit_button()
        # contacts_page.clear_first_name()
        # contacts_page.type_first_name_for_edit_contact("delete")
        # contacts_page.fill_organisation_field("Bitnoise")
        # common_page.hide_keyboard()
        # contacts_page.scroll_down_to_save_button()
        # contacts_page.save_edited_contact()
        # contacts_page.click_more_button()
        # contacts_page.delete_contact()
        # contacts_page.confirm_delete()
        # common_page.hamburger_button()
        # main_page.check_presence_of_inbox_button()
        #
        # main_page.scroll_down_to_contacts_button()
        # main_page.open_CONTACTS()
        # contacts_page.clear_Search_field()
        # contacts_page.type_text_into_search_field("delete")
        # common_page.click_Return_button_on_keyboard()
        # common_page.hide_keyboard()
        # contacts_page.check_results_for_deleted_contact()
        # contacts_page.clear_Search_field()
        # common_page.hide_keyboard()
        # common_page.hamburger_button()
        # main_page.check_presence_of_inbox_button()
        #
        # main_page.scroll_down_to_contacts_button()
        # main_page.open_CONTACTS()
        # contacts_page.open_second_contact_group()  # Contacts
        # contacts_page.click_new_button()
        # contacts_page.add_new_contact_into_group()
        # contacts_page.choose_contact_type_person()
        # contacts_page.type_first_name_for_new_contact("Communication")
        # contacts_page.scroll_down_to_email_field()
        # contacts_page.type_email_address("test90@onet.pl")
        # contacts_page.scroll_down_to_save_button()
        # contacts_page.save_new_contact()
        #
        # contacts_page.clear_Search_field()
        # contacts_page.type_text_into_search_field("Communication")
        # common_page.click_Return_button_on_keyboard()
        # common_page.hide_keyboard()
        # contacts_page.edit_first_contact_on_the_list()
        # contacts_page.click_more_button()
        # contacts_page.click_send_communication()
        # compose_page = LoadClass.load_page('ComposePage')
        # compose_page.setDriver(self.driver)
        # compose_page.choose_email_message()
        # compose_page.type_email_subject()
        # # common_page.hide_keyboard()
        # compose_page.type_email_message()
        # common_page.hide_keyboard()
        # compose_page.click_ok_button()
        # compose_page.click_send_button()
        # compose_page.alert_send_button()
        # common_page.hamburger_button()
        # main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.clear_Search_field()
        common_page.hide_keyboard()
        contacts_page.open_second_contact_group()  # Contacts
        contacts_page.type_text_into_search_field("Communication")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.edit_first_contact_on_the_list()
        contacts_page.click_more_button()
        contacts_page.save_contact_to_device()
        common_page.alert_popup_allow()  # need new method for android

        #common_page.hamburger_button()  # first click into hamburger button is hiding popup menu
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        # create contact with only read access - logout and login to general user
        main_page.scroll_down_to_logout_button()
        main_page.click_logout_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestManagingContacts)
    unittest.TextTestRunner(verbosity=2).run(suite)
