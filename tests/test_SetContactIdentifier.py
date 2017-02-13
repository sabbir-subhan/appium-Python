# Test Case 10 - Set Contact Identifier -- OCAMOB-40

# before test run - send invitation email from OCA web page -
#  (Contacts - Mobile - Send Invite) to obtain Contact Identifier PIN

# open OCA app
# Press Contact Identifier. Enter contact identifier and save.


import unittest
import logging
from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass


class test_Login(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        SetupTestCase.tearDown(self)

    def test_Set_Contact_Identifier(self):

        main_page = MainPage(self.driver)
        main_page.dismiss_ios_notifications()
        main_page.logout_if_already_logged_in()
        logging.info("starting Test Case 10: Set Contact Identifier")
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_settings_button()
        welcome_page.type_contact_identifier("test_pin")  # to change Contact Identifier PIN - edit it in credentials.py
        ios_device = iOSdevice(self.driver)
        ios_device.hide_keyboard()
        welcome_page.click_save_button()
        welcome_page.check_if_app_was_activated()
        welcome_page.click_ok_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_SetContactIdentifier_iOS)
    unittest.TextTestRunner(verbosity=2).run(suite)
