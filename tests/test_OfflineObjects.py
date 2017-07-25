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


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest


class TestOfflineObjects(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_Offline_Objects(self):

        logging.info("starting Test Case: Offline Objects")
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

        main_page.scroll_up_to_events_button()
        main_page.open_EVENTS()
        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.click_more_button_in_events_list()
        events_page.click_New_event_button()
        events_page.choose_Incident_type_of_event()
        events_page.fill_Name_input_field("Event in offline mode")
        events_page.click_severity_lvl_picker()
        events_page.choose_severity_level_1()
        events_page.scroll_down_to_save_button()

        common_page.swipe_up_to_show_control_center()
        common_page.switch_airplane_mode()  # method for iOS
        common_page.turn_on_all_network()  # method for Android
        common_page.swipe_down_to_hide_control_center()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLoadTypeDataAfterLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)
