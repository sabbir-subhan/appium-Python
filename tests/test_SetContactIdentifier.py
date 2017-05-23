# Test Case - Set Contact Identifier -- OCAMOB-40

# before test run - send invitation email from OCA web page -
#  (Contacts - Mobile - Send Invite) to obtain Contact Identifier PIN

# open OCA app
# Press Contact Identifier. Enter contact identifier and save.


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest


class TestSetContactIdentifier(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_Set_Contact_Identifier(self):

        logging.info("starting Test Case: Set Contact Identifier")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        welcome_page = LoadClass.load_page('WelcomePage')
        welcome_page.setDriver(self.driver)
        welcome_page.logout()  # logout if already logged in
        welcome_page.open_SETTINGS()
        settings_page = LoadClass.load_page('SettingsPage')
        settings_page.setDriver(self.driver)
        settings_page.type_contact_identifier("test_pin")  # to change Contact Identifier PIN - edit it in credentials.py
        common_page.hide_keyboard()
        settings_page.click_save_button()
        settings_page.check_if_app_was_activated()
        settings_page.click_ok_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSetContactIdentifier)
    unittest.TextTestRunner(verbosity=2).run(suite)
