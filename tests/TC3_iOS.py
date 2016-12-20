# Test Case 3 - Managing events  -- OCAMOB-64


from appium import webdriver
from desired_capabilities import DesiredCapabilities
from page_ios import *


class TestCase3iOS(unittest.TestCase):
    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")

        # choose desired capabilities from desired_capabilities.py
        desired_capabilities = DesiredCapabilities.desired_capabilities_for_iOS_iPad

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

        self.driver.implicitly_wait(20)  # seconds

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_1_managing_events(self):

        # login
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
        events_page.check_if_EVENTS_were_opened()
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
        event_edit_page.click_into_Name_input_field()
        event_edit_page.fill_Name_input_field("Test Appium iOS")
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

    def test_2_managing_events(self):
        # remember to run test 1 first

        main_page = MainPage(self.driver)
        logging.info("TC info: create second event and add map")
        main_page.open_EVENTS()
        events_page = EventsPage(self.driver)
        events_page.check_if_EVENTS_were_opened()
        events_page.click_More_button()
        events_page.click_New_event_button()
        events_types_page = EventsTypesPage(self.driver)
        events_types_page.choose_Incident_type_of_event()
        event_edit_page = EventEditPage(self.driver)
        event_edit_page.click_into_Name_input_field()
        event_edit_page.fill_Name_input_field("Test Appium iOS - second event")
        ios_device = iOSdevice(self.driver)
        ios_device.hide_keyboard()
        event_edit_page.click_severity_lvl_picker()
        event_edit_page.choose_severity_level_4()
        event_edit_page.save_event()
        events_page.check_if_EVENTS_were_opened()
        events_page.open_previously_created_event2()
        event_details_page = EventDetailsPage(self.driver)
        event_details_page.click_edit_button()
        event_edit_page.click_create_mapping_data()
        # ios_device.alert_allow_location()
        map_page = MapPage(self.driver)
        map_page.wait_for_map_to_load()
        map_page.click_tool_button()
        map_page.click_point_button()
        map_page.click_default_button()
        map_page.click_in_map_area_12()
        map_page.click_tool_button()
        map_page.click_line_button()
        map_page.click_default_button()
        map_page.click_in_map_area_17()
        map_page.double_click_in_map_area_18()
        map_page.click_tool_button()
        map_page.click_circle_button()
        map_page.click_default_button()
        map_page.click_in_map_area_17()
        map_page.click_tool_button()
        map_page.click_polygon_button()
        map_page.click_default_button()
        map_page.click_in_map_area_13()
        map_page.click_in_map_area_17()
        map_page.double_click_in_map_area_18()
        map_page.save_map()
        event_edit_page.save_event()

    def test_3_managing_events(self):
        # remember to run test 1 first

        logging.info("TC info: crete sub event, set event as primary and after that clear it. Next create, "
                     "but do not save; events with on load/save sequence and with hidden fields"
                     " and another with chooser fields")
        top_bar = BasePage(self.driver)
        top_bar.hamburger_button()
        main_page = MainPage(self.driver)
        main_page.open_EVENTS()
        events_page = EventsPage(self.driver)
        events_page.check_if_EVENTS_were_opened()
        events_page.click_More_button()
        events_page.click_New_event_button()
        events_types_page = EventsTypesPage(self.driver)
        events_types_page.choose_Incident_type_of_event()
        event_edit_page = EventEditPage(self.driver)
        event_edit_page.click_into_Name_input_field()
        event_edit_page.fill_Name_input_field("Test ios to create sub event")
        ios_device = iOSdevice(self.driver)
        ios_device.hide_keyboard()
        event_edit_page.click_severity_lvl_picker()
        event_edit_page.choose_severity_level_3()
        event_edit_page.save_event()
        events_page.check_if_EVENTS_were_opened()
        events_page.open_previously_created_event3()
        events_page.click_More_button()
        events_page.click_New_sub_event()
        events_types_page.choose_Incident_type_of_event()
        event_edit_page.click_into_Name_input_field()
        event_edit_page.fill_Name_input_field("Test iOS to create sub event")
        ios_device.hide_keyboard()
        event_edit_page.click_severity_lvl_picker()
        event_edit_page.choose_severity_level_2()
        event_edit_page.save_event()
        events_page.click_More_button()
        events_page.set_as_primary_event()
        top_bar.hamburger_button()
        main_page.open_EVENTS()
        events_page.check_if_EVENTS_were_opened()
        events_page.click_More_button()
        events_page.clear_primary_event()

        logging.info("create new type of event, but do not save it - event with on load and on save sequence"
                     " and with hidden fields")
        main_page.open_EVENTS()
        events_page.check_if_EVENTS_were_opened()
        events_page.click_More_button()
        events_page.click_New_event_button()
        events_types_page.choose_Event_for_on_load_save_type_of_event()
        event_edit_page.check_on_load_and_on_save_sequences()
        event_edit_page.click_on_option_list()
        option_list_in_event = OptionList(self.driver)
        option_list_in_event.click_on_option_1()
        event_edit_page.check_restored_field_1()
        event_edit_page.click_on_option_list()
        option_list_in_event.click_on_option_2()
        event_edit_page.check_restored_field_2()
        event_edit_page.check_hidden_field_1()
        event_edit_page.click_on_option_list()
        option_list_in_event.click_on_option_3()
        event_edit_page.check_hidden_fields_1_and_2()
        event_edit_page.cancel_button()

        logging.info("create new type of event, but do not save it - event with chooser field for another event "
                     "and sub form with chooser field")
        events_page.check_if_EVENTS_were_opened()
        events_page.click_More_button()
        events_page.click_New_event_button()
        events_types_page.choose_Event_for_chooser_fields_type_of_event()
        event_edit_page.click_on_event_chooser_field()
        events_page.click_on_previously_created_event_for_chooser_field()
        event_edit_page.click_button_add_row()
        event_edit_page.click_on_choose_field_inside_subform()
        events_page.click_on_previously_created_event_for_subform_chooser()
        event_edit_page.delete_chosen_event_inside_subform()
        event_edit_page.cancel_button()
        events_page.check_if_EVENTS_were_opened()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase3iOS)
    unittest.TextTestRunner(verbosity=2).run(suite)
