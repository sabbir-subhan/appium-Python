# Test Case - Ability to access link library feature layer from mobile app -- OCAMOB-62

# before running this test create in OCA web page:

# open OCA app
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss notifications
# check if button "EVENTS" is present


import unittest
import logging
from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
from configuration import PROJECT_ROOT


class TestLinkLibraryLayer(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        self.driver.save_screenshot(PROJECT_ROOT + "/screenshots/test_LinkLibraryLayer.png")

        self.driver.quit()

    def test_LinkLibraryLayer(self):

        logging.info("starting Test Case: Link Library Layer")
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
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLinkLibraryLayer)
    unittest.TextTestRunner(verbosity=2).run(suite)
