# Test Case - Contact groups folders visible for low level users using mobile app  -- OCAMOB-331

# before running this test create:

# create new contact type in OCA, named: "Group"


# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present

# From the main menu press Contacts.

# Create new contact group
# Create new contact in that group

# Create second contact group with Read Access Level set to: Only Administrators
# Create new contact in that group

# Logout and log in as a low user
# Filter contact groups to find first group without Read Access Level restrictions and create new contact in that group
# Filter contact groups to find second group with Read Access Level set to: Only Administrators -- low user should not
# see that group/result of search should be empty


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest
import os


class TestContactGroupsVisibility(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        path = "./screenshots"
        os.chdir(path)
        self.driver.save_screenshot("test_ContactGroupsVisibility" + ".png")
        os.chdir("..")

        self.driver.quit()

    def test_ContactGroupsVisibility(self):

        logging.info("starting Test Case: Contact Groups Visibility")
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
        contacts_page.click_new_button()
        contacts_page.add_new_contact_group()
        contacts_page.choose_group_for_new_contact_group_type()  # Group
        contacts_page.type_name_for_new_contact_group("for_all_users")
        contacts_page.scroll_down_to_save_button()
        contacts_page.save_new_contact_group()

        contacts_page.click_new_button()
        contacts_page.add_new_contact_group()
        contacts_page.choose_group_for_new_contact_group_type()  # Group
        contacts_page.type_name_for_new_contact_group("only_high_users")
        contacts_page.scroll_down_to_write_access_level()
        contacts_page.click_read_access_level_for_new_group()
        contacts_page.option_list_administrators_only()
        contacts_page.save_new_contact_group()

        contacts_page.clear_Search_field()
        contacts_page.type_text_into_search_field("for_all_users")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.open_first_contact_group()
        contacts_page.click_new_button()
        contacts_page.add_new_contact_into_group()
        contacts_page.choose_contact_type_person()
        contacts_page.type_first_name_for_new_contact("low_user")
        contacts_page.scroll_down_to_save_button()
        contacts_page.save_new_contact()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.clear_Search_field()
        contacts_page.type_text_into_search_field("only_high_users")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.open_first_contact_group()
        contacts_page.click_new_button()
        contacts_page.add_new_contact_into_group()
        contacts_page.choose_contact_type_person()
        contacts_page.type_first_name_for_new_contact("high_user")
        contacts_page.scroll_down_to_save_button()
        contacts_page.save_new_contact()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

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
        contacts_page.type_text_into_search_field("for_all_users")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.open_first_contact_group()
        contacts_page.click_new_button()
        contacts_page.add_new_contact_into_group()
        contacts_page.choose_contact_type_person()
        contacts_page.type_first_name_for_new_contact("created_by_low_user")
        contacts_page.scroll_down_to_save_button()
        contacts_page.save_new_contact()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.clear_Search_field()
        contacts_page.type_text_into_search_field("only_high_users")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        contacts_page.check_first_contact_group_on_the_list()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestContactGroupsVisibility)
    unittest.TextTestRunner(verbosity=2).run(suite)
