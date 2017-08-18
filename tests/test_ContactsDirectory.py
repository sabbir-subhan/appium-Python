# Test Case - Contacts Directory -- OCAMOB-52

# before running this test create:

# create new contact type in OCA, named: "Person"


# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present

# From the main menu press Contacts.

# Create new contact with address data (contact can be used in TC: Create Objects From Mapping Layer)

# Enter part of a name of an existing contact into the search box and press return/search.
# Press the "x" on the right of the search box.
# Press a contact group.
# Keep opening contact groups until contacts appear.


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest
from configuration import PROJECT_ROOT


class TestContactsDirectory(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        self.driver.save_screenshot(PROJECT_ROOT + "/screenshots/test_ContactsDirectory.png")

        self.driver.quit()

    def test_ContactsDirectory(self):

        logging.info("starting Test Case: Contacts Directory")
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
        contacts_page.type_first_name_for_new_contact("Contact")
        contacts_page.scroll_down_to_address_input_field()
        contacts_page.click_address_field()
        contacts_page.type_address_number("580")
        contacts_page.type_address_street("George")
        contacts_page.type_address_post_code("2121")
        contacts_page.type_address_country("Australia")
        contacts_page.scroll_down_to_save_button()
        contacts_page.save_new_contact()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.clear_Search_field()
        contacts_page.type_text_into_search_field("580 George")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.clear_Search_field()
        contacts_page.type_text_into_search_field("Contacts")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.open_contacts_group()  # Contacts
        common_page.back_arrow()
        contacts_page.clear_Search_field()
        contacts_page.type_text_into_search_field("Users")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.open_users_group()  # Users
        common_page.back_arrow()
        contacts_page.clear_Search_field()
        contacts_page.type_text_into_search_field("Mailing list unsubscribes")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.open_mailing_list_group()  # Mailing list unsubscribes
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestContactsDirectory)
    unittest.TextTestRunner(verbosity=2).run(suite)

