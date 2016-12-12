# Test Case 3 - Managing events


from appium import webdriver
from desired_capabilities import DesiredCapabilities
from page_ios import *


class TestCase3iOS(unittest.TestCase):
    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")

        # choose desired capabilities from desired_capabilities.py
        desired_capabilities = DesiredCapabilities.desired_capabilities_for_iOS_iPad

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

        self.driver.implicitly_wait(25)  # seconds

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_1_managing_events(self):

        main_page = MainPage(self.driver)
        main_page.dismiss_ios_notifications()
        main_page.logout_if_already_logged_in()
        logging.info("starting test: managing events")
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

        # moving to EVENTS
        logging.info("TC info: filter events, create first Event and delete it")
        main_page.open_EVENTS()
        events_page = EventsPage(self.driver)
        events_page.filter_events_by_Type()
        events_page.filter_events_by_Status()
        events_page.filter_events_by_Search_field()
        ios_device.click_Return_button_on_keyboard()
        ios_device.hide_keyboard()
        events_page.clear_Search_field()
        ios_device.click_Return_button_on_keyboard()
        ios_device.hide_keyboard()
        events_page.click_More_button()
        events_page.click_New_event_button()
        events_types_page = EventsTypesPage(self.driver)
        events_types_page.choose_Incident_type_of_event()
        event_edit_page = EventEditPage(self.driver)
        event_edit_page.fill_name_input_field("Test Appium iOS")
        ios_device.hide_keyboard()
        event_edit_page.click_severity_lvl_picker()
        event_edit_page.choose_severity_level_1()
        event_edit_page.save_event()
        events_page.open_previously_created_event1()
        event_details_page = EventDetailsPage(self.driver)
        event_details_page.click_edit_button()
        event_edit_page.type_text_into_description_field()
        ios_device.hide_keyboard()
        event_edit_page.save_event()
        events_page.click_More_button()
        event_details_page.click_Delete_button()
        event_details_page.alert_confirm_delete()

        logging.info("TC info: create second event and add map")
        events_page.click_More_button()
        events_page.click_New_event_button()
        events_types_page.choose_Incident_type_of_event()
        event_edit_page.fill_name_input_field("Test Appium iOS - second event")
        ios_device.hide_keyboard()
        event_edit_page.click_severity_lvl_picker()
        event_edit_page.choose_severity_level_4()
        event_edit_page.save_event()
        event_details_page.click_edit_button()
        event_edit_page.click_create_mapping_data()
        ios_device.alert_allow_location()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase3iOS)
    unittest.TextTestRunner(verbosity=2).run(suite)
