# Test Case - Managing Contacts -- OCAMOB-54

# before running this test create:

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

    def test_manage_logs(self):

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


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestManagingContacts)
    unittest.TextTestRunner(verbosity=2).run(suite)
