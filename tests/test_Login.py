# Test Case 1 - Log Into OCA mobile via direct Login -- OCAMOB-38

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


class test_Login(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_login(self):

        logging.info("starting Test Case 1: login into active account")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        welcome_page = LoadClass.load_page('WelcomePage')
        welcome_page.setDriver(self.driver)
        welcome_page.click_login_button()
        login_page = LoadClass.load_page('LoginPage')
        login_page.setDriver(self.driver)
        login_page.type_username('QA')  # change here login credentials (login and pass are defined in credentials.py)
        login_page.type_password('QA')  # for example use: QA, general_user, admin, expired_1_day_ago, expire_today, expire_in_1_day OR suspended
        login_page.type_domain_address('QA')
        common_page.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        main_page = LoadClass.load_page('MainPage')
        main_page.setDriver(self.driver)
        main_page.alert_expiring_password()
        main_page.dismiss_notifications()
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_Login)
    unittest.TextTestRunner(verbosity=2).run(suite)
