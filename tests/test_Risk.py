# Test Case 6 - Risks -- OCAMOB-44

# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present
# From the main menu click on Risks.
# Create a new Risk Register
# Click on Risk >Click on Existing library >Click Add Control
# CClick on Risk Register>Click on new>Click on Add new Context
# Click on Risk Register>Click on New>Click on Add new Risk
# Click on Risk Register>Click on New>Click on Add new library Risk
# Click on Risk>Select a Risk Register>Select a Context>Click on Context>Click on more >Add new control
# Click on Risk>Select a Risk Register>Select a Context>Click on Context>Click on more >Delete this risk
# Click on Risk>Select a Risk Register>Select a Context>Click on Context>Click on more >Add Library Control
# Click on Risk>Select a Risk Register>Select a Context>Click on Context>Click on more >Mark as Reviewed
# Click on Risk >Risk register>View>View Register


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

    def test_manage_risks(self):

        main_page = MainPage(self.driver)
        main_page.dismiss_ios_notifications()
        main_page.logout_if_already_logged_in()
        logging.info("starting Test Case 6: Risk")
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.type_username('QA')
        login_page.type_password('QA')
        login_page.type_domain_address('QA')
        ios_device = iOSdevice(self.driver)
        ios_device.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        main_page.alert_expiring_password()
        main_page.dismiss_ios_notifications()
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_Risk_iOS)
    unittest.TextTestRunner(verbosity=2).run(suite)
