# Test Case 3 - Managing events  -- OCAMOB-64

# before test run - prepare events types on OCA web page

# - 3 types of events (Incident, event_for_chooser_fields, event_for_on_load/save_test)
# - option list inside "Central list templates" with values; "1", "2", "3"
# that list is added as a option list to event type: event_for_on_load/save_test
# - two sequences for events (on load and on save) - that sequences are added to event type: event_for_on_load/save_test
# - EVENT TYPE: event_for_on_load/save_test, should have two single line fields with properties
# "Sequential prefix" pinpointing to correct sequences ("sequence_onload" with vaule: "test on load",
# and second; "sequence_onsave" with value: "test on save") and two fields with visibility rules
# ("field to restore" with value: "value for field 1" and visibility rule pointing to "New option list"
# with value "1",and second field; "New email address" with value: "test@noggin.com" and visibility
# rule pointing to "new option list" with value "2")
# - EVENT TYPE: event_for_chooser_fields, should have "event chooser" field (name: "New events chooser")
# with property "Minimum selected options" set to "1", and second event chooser field inside sub form
# with name: "New events chooser inside sub form"


from appium import webdriver
from desired_capabilities import DesiredCapabilities
from page_android import *


class test_ManagingEvents_Android(unittest.TestCase):
    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")

        # choose desired capabilities from desired_capabilities.py
        desired_capabilities = DesiredCapabilities.desired_capabilities_for_android_6

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

        self.driver.implicitly_wait(30)  # seconds

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_managing_events(self):

        logging.info("starting Test Case 3: managing events")
        top_bar = BasePage(self.driver)
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.type_username('QA')
        login_page.type_password('QA')
        login_page.type_domain_address('QA')
        android_device = AndroidDevice(self.driver)
        android_device.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        main_page = MainPage(self.driver)
        main_page.alert_expiring_password()
        main_page.dismiss_android_notifications()
        main_page.check_presence_of_events_button()

        logging.info("TC info: filter events, create first Event and delete it")
        main_page.open_EVENTS()
        events_page = EventsPage(self.driver)
        events_page.filter_events_by_Type()
        events_page.filter_events_by_Status()
        events_page.filter_events_by_Search_field()  # it's not working on android 4.4.2 and 5.1 - Appium can't send keys to Search field
        android_device.click_Go_button_on_keyboard()
        android_device.hide_keyboard()
        events_page.clear_Search_field()
        android_device.click_Go_button_on_keyboard()
        android_device.hide_keyboard()
        top_bar.hamburger_button()
        main_page.open_EVENTS()
        events_page.click_More_button()
        events_page.click_New_event_button()
        events_types_page = EventsTypesPage(self.driver)
        events_types_page.choose_Incident_type_of_event()
        event_edit_page = EventEditPage(self.driver)
        event_edit_page.fill_Name_input_field("Test Appium Android")
        android_device.hide_keyboard()
        event_edit_page.click_severity_lvl_picker()
        event_edit_page.choose_severity_level_1()
        event_edit_page.scroll_down()
        event_edit_page.save_button()
        events_page.open_previously_created_event1()
        event_details_page = EventDetailsPage(self.driver)
        event_details_page.click_edit_button()
        event_edit_page.scroll_down_one_view()
        event_edit_page.type_text_into_description_field()  # this step will be passed on older android devices to avoid errors
        android_device.hide_keyboard()
        event_edit_page.scroll_down()
        event_edit_page.save_button()
        events_page.click_More_button()
        event_details_page.click_Delete_button()
        event_details_page.alert_confirm_delete()

        logging.info("TC info: create second event and add map")
        events_page.check_if_EVENTS_were_opened()
        events_page.click_More_button()
        events_page.click_New_event_button()
        events_types_page.choose_Incident_type_of_event()
        event_edit_page.fill_Name_input_field("Test Appium Android - second event")
        android_device.hide_keyboard()
        event_edit_page.click_severity_lvl_picker()
        event_edit_page.choose_severity_level_4()
        event_edit_page.scroll_down()
        event_edit_page.save_button()
        events_page.check_if_EVENTS_were_opened()
        events_page.open_previously_created_event2()
        event_details_page.click_edit_button()
        event_edit_page.scroll_down()
        event_edit_page.click_create_mapping_data()
        android_device.alert_android_allow()
        map_page = MapPage(self.driver)
        map_page.wait_for_map_to_load()
        map_page.click_tool_button()
        map_page.click_point_button()
        map_page.click_default_button()
        map_page.click_in_map_area_9()
        map_page.click_tool_button()
        map_page.click_line_button()
        map_page.click_default_button()
        map_page.click_in_map_area_3()
        map_page.double_click_in_map_area_6()
        map_page.click_tool_button()
        map_page.click_circle_button()
        map_page.click_default_button()
        map_page.click_in_map_area_9()
        map_page.click_tool_button()
        map_page.click_polygon_button()
        map_page.click_default_button()
        map_page.click_in_map_area_9()
        map_page.click_in_map_area_3()
        map_page.double_click_in_map_area_6()
        map_page.save_map()
        event_edit_page.save_button()

        logging.info("TC info: crete sub event, set event as primary and after that clear it. Next create, "
                     "but do not save; events with on load/save sequence and with hidden fields"
                     " and another with chooser fields")
        top_bar.hamburger_button()
        main_page.open_EVENTS()
        events_page.click_More_button()
        events_page.click_New_event_button()
        events_types_page.choose_Incident_type_of_event()
        event_edit_page.fill_Name_input_field("Test Android to create sub event")
        android_device.hide_keyboard()
        event_edit_page.click_severity_lvl_picker()
        event_edit_page.choose_severity_level_3()
        event_edit_page.scroll_down()
        event_edit_page.save_button()
        events_page.check_if_EVENTS_were_opened()
        events_page.open_previously_created_event3()
        events_page.click_More_button()
        events_page.click_New_sub_event()
        events_types_page.choose_Incident_type_of_event()
        event_edit_page.fill_Name_input_field("Test Android sub event")
        android_device.hide_keyboard()
        event_edit_page.click_severity_lvl_picker()
        event_edit_page.choose_severity_level_2()
        event_edit_page.scroll_down()
        event_edit_page.save_button()
        events_page.click_More_button()
        events_page.set_as_primary_event()
        top_bar.hamburger_button()
        main_page.open_EVENTS()
        events_page.click_More_button()
        events_page.clear_primary_event()

        logging.info("create new type of event, but do not save it - event with on load and on save sequence"
                     " and with hidden fields")
        events_page.click_More_button()
        events_page.click_New_event_button()
        events_types_page.choose_Event_for_on_load_save_type_of_event()
        event_edit_page.fill_Name_input_field("Test Event with on load and on save sequence")
        android_device.hide_keyboard()
        event_edit_page.scroll_down_one_view()
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
        event_edit_page.scroll_down()
        event_edit_page.cancel_button()

        logging.info("create new type of event, but do not save it - event with chooser field for another event "
                     "and sub form with chooser field")
        events_page.check_if_EVENTS_were_opened()
        events_page.click_More_button()
        events_page.click_New_event_button()
        events_types_page.choose_Event_for_chooser_fields_type_of_event()
        event_edit_page.fill_Name_input_field("Test Event with chooser fields")
        android_device.hide_keyboard()
        event_edit_page.scroll_down_one_view()
        event_edit_page.click_on_event_chooser_field()
        events_page.click_on_previously_created_event_for_chooser_field()
        event_edit_page.click_button_add_row()
        event_edit_page.click_on_choose_field_inside_subform()
        events_page.click_on_previously_created_event_for_subform_chooser()
        event_edit_page.delete_chosen_event_inside_subform()
        event_edit_page.scroll_down()
        event_edit_page.cancel_button()
        events_page.check_if_EVENTS_were_opened()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_ManagingEvents_Android)
    unittest.TextTestRunner(verbosity=2).run(suite)
