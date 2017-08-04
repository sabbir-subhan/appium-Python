# Test Case - Managing events  -- OCAMOB-64

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


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest
import os
from configuration import PROJECT_ROOT


class TestManagingEvents(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        path = PROJECT_ROOT + "/screenshots"
        os.chdir(path)
        self.driver.save_screenshot("test_ManagingEvents" + ".png")
        os.chdir("..")

        self.driver.quit()

    def test_ManagingEvents(self):

        logging.info("starting Test Case: Managing Events")
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
        common_page.wait_for_app_loading()
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

        logging.info("TC info: filter events, create first Event and delete it")
        main_page.scroll_up_to_events_button()
        main_page.open_EVENTS()
        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.filter_events_by_type()
        events_page.filter_events_by_status()
        events_page.clear_Search_field()
        events_page.type_text_into_search_field("search")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        events_page.clear_Search_field()
        common_page.hide_keyboard()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.scroll_up_to_events_button()
        main_page.open_EVENTS()
        events_page.click_more_button_in_events_list()
        events_page.click_New_event_button()
        events_page.choose_Incident_type_of_event()
        events_page.fill_Name_input_field("First event")
        events_page.click_severity_lvl_picker()
        events_page.choose_severity_level_1()
        events_page.scroll_down_to_save_button()
        events_page.click_save_new_event()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.scroll_up_to_events_button()
        main_page.open_EVENTS()
        events_page.clear_Search_field()
        events_page.type_text_into_search_field("First event")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        events_page.open_previously_created_event()
        common_page.wait_for_app_loading()
        events_page.click_edit_button()
        events_page.click_severity_lvl_picker_for_edit_event()
        events_page.choose_severity_level_5()
        events_page.scroll_down_to_description_field()
        events_page.type_text_into_description_field()
        common_page.hide_keyboard()
        events_page.scroll_down_to_save_button()
        events_page.click_save_edited_event()
        events_page.click_more_button_in_event_details()
        events_page.click_Delete_button()
        events_page.alert_confirm_delete()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        logging.info("TC info: create second event and add map")
        main_page.scroll_up_to_events_button()
        main_page.open_EVENTS()
        events_page.click_more_button_in_events_list()
        events_page.click_New_event_button()
        events_page.choose_Incident_type_of_event()
        events_page.fill_Name_input_field("Second event")
        events_page.click_severity_lvl_picker()
        events_page.choose_severity_level_4()
        events_page.scroll_down_to_save_button()
        events_page.click_save_new_event()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.scroll_up_to_events_button()
        main_page.open_EVENTS()
        events_page.clear_Search_field()
        events_page.type_text_into_search_field("Second event")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        events_page.open_previously_created_event()
        common_page.wait_for_app_loading()
        events_page.click_edit_button()
        events_page.scroll_down_to_save_button()
        events_page.click_create_mapping_data_for_existing_event()
        common_page.alert_popup_allow()
        map_page = LoadClass.load_page('MapPage')
        map_page.setDriver(self.driver)
        map_page.wait_for_map_to_load()
        map_page.click_tool_button()
        map_page.click_point_button()
        map_page.click_point_default_button()
        map_page.click_in_map_area_1()
        map_page.click_tool_button()
        map_page.click_line_button()
        map_page.click_line_default_button()
        map_page.click_in_map_area_2()
        map_page.double_tap_on_map()
        map_page.click_tool_button()
        map_page.click_circle_button()
        map_page.click_circle_default_button()
        map_page.click_in_map_area_2()
        map_page.click_tool_button()
        map_page.click_polygon_button()
        map_page.click_polygon_default_button()
        map_page.click_in_map_area_1()
        map_page.click_in_map_area_2()
        map_page.double_tap_on_map()
        map_page.save_map()
        events_page.scroll_down_to_save_button()
        events_page.click_save_edited_event()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        logging.info("TC info: crete sub event, set event as primary and after that clear it. Next create, "
                     "but do not save; events with on load/save sequence and with hidden fields"
                     " and another with chooser fields")

        main_page.scroll_up_to_events_button()
        main_page.open_EVENTS()
        events_page.open_previously_created_event()
        common_page.wait_for_app_loading()
        events_page.click_more_button_in_event_details()
        events_page.click_New_sub_event()
        events_page.choose_Incident_type_of_event()
        events_page.fill_Name_input_field("Appium sub event")
        events_page.click_severity_lvl_picker()
        events_page.choose_severity_level_2()
        events_page.scroll_down_to_save_button()
        events_page.click_save_new_event()
        events_page.click_more_button_in_event_details()
        events_page.set_as_primary_event()
        common_page.hamburger_button()

        main_page.scroll_up_to_events_button()
        main_page.open_EVENTS()
        events_page.click_more_button_in_events_list()
        events_page.clear_primary_event()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        logging.info("create new type of event, but do not save it - event with on load and on save sequence"
                     " and with hidden fields")
        main_page.scroll_up_to_events_button()
        main_page.open_EVENTS()
        events_page.click_more_button_in_events_list()
        events_page.click_New_event_button()
        events_page.choose_Event_for_on_load_save_type_of_event()
        events_page.scroll_down_to_option_list()
        events_page.check_on_load_and_on_save_sequences()
        events_page.click_on_option_list()
        events_page.click_on_option_1()
        events_page.check_restored_field_1()
        events_page.click_on_option_list()
        events_page.click_on_option_2()
        events_page.check_restored_field_2()
        events_page.check_hidden_field_1()
        events_page.click_on_option_list()
        events_page.click_on_option_3()
        events_page.check_hidden_fields_1_and_2()
        events_page.scroll_down_to_save_button()
        events_page.click_cancel_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        logging.info("create new type of event, but do not save it - event with chooser field for another event "
                     "and sub form with chooser field")
        main_page.scroll_up_to_events_button()
        main_page.open_EVENTS()
        events_page.click_more_button_in_events_list()
        events_page.click_New_event_button()
        events_page.choose_Event_for_chooser_fields_type_of_event()
        events_page.scroll_down_to_event_chooser_field()
        events_page.click_on_event_chooser_field()
        events_page.open_previously_created_event_checkbox()
        events_page.scroll_down_to_add_row_button()
        events_page.click_button_add_row()
        events_page.click_on_choose_field_inside_subform()
        events_page.open_previously_created_event_checkbox()
        events_page.delete_chosen_event_inside_subform()
        events_page.scroll_down_to_save_button()
        events_page.click_cancel_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestManagingEvents)
    unittest.TextTestRunner(verbosity=2).run(suite)

