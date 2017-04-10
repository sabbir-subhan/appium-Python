# Test Case - Send location to OCA -- OCAMOB-41

# before running this test, enable location on device

# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# Click on location and touch send once now
# Setup sending location every 5 minutes for an hour


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest


class TestSendLocation(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_send_location(self):

        logging.info("starting Test Case: Send location to OCA")
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
        main_page = LoadClass.load_page('MainPage')
        main_page.setDriver(self.driver)
        main_page.alert_expiring_password()
        main_page.dismiss_notifications()
        main_page.check_presence_of_events_button()

        main_page.open_LOCATION()
        location_page = LoadClass.load_page('LocationPage')
        location_page.setDriver(self.driver)
        location_page.check_if_location_page_was_opened()
        location_page.click_send_once_now()
        location_page.check_if_location_was_sent()
        location_page.click_send_every()
        location_page.choose_send_every_5_minutes_option()
        location_page.check_if_5_minutes_option_was_chosen()
        location_page.click_for_the_next()
        location_page.choose_1_hour_option()
        location_page.check_if_1_hour_option_was_chosen()
        location_page.click_start_button()
        location_page.check_if_start_button_was_clicked()
        location_page.check_if_location_was_sent()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSendLocation)
    unittest.TextTestRunner(verbosity=2).run(suite)
