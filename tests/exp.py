# Test Case 1 - Log Into OCA mobile via direct Login -- OCAMOB-38

# open OCA app
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss notifications
# check if button "EVENTS" is present


from methods import *
from setup import SetupTestCase


class test_Login(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        SetupTestCase.tearDown(self)

    def test_login(self):

        # main_page = MainPage(self.driver)
        # main_page.dismiss_ios_notifications()
        # main_page.scroll_down_one_view()
        # main_page.logout_if_already_logged_in()
        logging.info("starting Test Case 1: login into active account")
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.type_username('QA')  # change here login credentials (login and pass are defined in credentials.py)
        login_page.type_password('QA')  # for example use: QA, general_user, admin, expired_1_day_ago, expire_today, expire_in_1_day OR suspended
        login_page.type_domain_address('QA')
        ios_device = iOSdevice(self.driver)
        ios_device.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        main_page = MainPage(self.driver)
        main_page.alert_expiring_password()
        main_page.dismiss_ios_notifications()
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_Login)
    unittest.TextTestRunner(verbosity=2).run(suite)
