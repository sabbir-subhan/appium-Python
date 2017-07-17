# Test Case - Load Type Data After Login -- OCAMOB-241


# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present

# Turn on airplane mode
# After load,  user should see a badge on the offline sync icon with the counter
# Click on offline sync icon
# View the Incoming queue screen
# View Outgoing queue
# Create event offline > Add media > Add video, Audio, Images to the event in offline sync > Save the event
# Turn off airplane mode
# Check the events created offline once you are online -- Verify that the media files are saved


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest


class TestLoadTypeDataAfterLogin(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_Load_Type_Data_After_Login(self):

        logging.info("starting Test Case: Load Type Data After Login")
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

        common_page.swipe_up_to_show_control_center()
        common_page.switch_airplane_mode()  # method for iOS
        common_page.turn_on_flight_mode()  # method for Android
        common_page.swipe_down_to_hide_control_center()

        main_page.scroll_down_to_offline_sync_button()
        main_page.open_OFFLINE_SYNC()
        common_page.take_screenshot('offline_sync_in_offline_mode')

        common_page.swipe_up_to_show_control_center()
        common_page.switch_airplane_mode()  # method for iOS
        common_page.turn_on_all_network()  # method for Android
        common_page.swipe_down_to_hide_control_center()

        main_page.scroll_down_to_offline_sync_button()
        main_page.open_OFFLINE_SYNC()
        common_page.take_screenshot('offline_sync_in_online_mode')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLoadTypeDataAfterLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)
