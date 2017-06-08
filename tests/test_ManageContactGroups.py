# Test Case - Managing Contact Group -- OCAMOB-56

# before running this test create:

# create new contact group type in OCA - named: "Appium Group"
# create new contact group type in OCA - named: "Group"


# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present

# From the main menu press Contacts.

# Press New > Create new contact group.
# Select a contact group type.
# Fill in the form for the new contact group type and press save.
# Open a contact group. Select New > Create new contact group in this group.
# Select a contact group type. Fill in the form and press save.
# Open a contact group. Press Group Info > Edit.
# Make some changes and press Save.
# Press More > Delete group. Press delete on the prompt.
# Press More > Delete group. Press delete on the prompt.
# On OCA Server (the website), configure a contact group type to have an on load sequence and on save sequence in two of its fields.
# On the mobile app, create contact groups of this type.
# Open new contact groups but don't save them.
# Create an event that has option lists and fields with visibility rules that clears hidden fields and restores default values.


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest


class TestManagingContactGroup(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_managing_contact_group(self):

        logging.info("starting Test Case: Managing Contact Groups")
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

        # Press New > Create new contact group.
        contacts_page.click_new_button()
        contacts_page.add_new_contact_group()

        # Select a contact group type.
        contacts_page.choose_group_for_new_contact_group_type()

        # Fill in the form for the new contact group type and press save.
        contacts_page.type_name_for_new_contact_group("Appium contact group")


        # Open a contact group. Select New > Create new contact group in this group.
        # Select a contact group type. Fill in the form and press save.
        # Open a contact group. Press Group Info > Edit.
        # Make some changes and press Save.
        # Press More > Delete group. Press delete on the prompt.
        # Press More > Delete group. Press delete on the prompt.
        # On OCA Server (the website), configure a contact group type to have an on load sequence and on save sequence in two of its fields.
        # On the mobile app, create contact groups of this type.
        # Open new contact groups but don't save them.
        # Create an event that has option lists and fields with visibility rules that clears hidden fields and restores default values.


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestManagingContactGroup)
    unittest.TextTestRunner(verbosity=2).run(suite)
