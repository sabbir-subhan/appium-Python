# Test Case - Create objects from Mapping layer -- OCAMOB-53

# before running this test create:

# - Login to the OCA server > Click on OCA designer > Symbology and Colour Coding > Add more symbology - new point symbol name: "point2"
# - Login to oca server > Click on mapping > > Layers > Add > Drawing > Ok > Draw geometry (draw some shape using line tool) > Save map as "FOR MOBILE"
# - other Saved maps that are needed for TC: All active events, All assets, All contacts, All tasks - for proper TC execution
# in OCA app should be present one event, asset, task and contact with mapping data or address data
# (Contact with address is created in TC: Contacts Directory, Event with mapping data is created in TC: Managing Events,
# Report with mapping data is created in TC: Managing Reports)

# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present

# From the main menu press Maps.
# Maps > Layers > Select layers > Tools > Plot a point, line, circle or polygon > Create > Event > Type > Save
# Maps > Layers > Select layers > Tools > Plot a point, line, circle or polygon > Create > Asset > Type > Save
# Maps > Layers > Select layers > Tools > Plot a point, line, circle or polygon > Create > Report > Type > Save
# Maps > Layers > Select layers > Tools > Plot a point, line, circle or polygon > Create > Task > Type > Save

# Navigate to Events > Check the type of Event created above
# Navigate to Reports > Check the type of Report created above
# Navigate to Assets > Check the type of created above

# View attributes on Map Geometry - Click on Event > Create a new event > Click on Create mapping data >
# Click on Tool > Add Geometry>Save - Edit event > Click on mapping data > Click on Geometry > View attributes

# Click on Map > Click on layers > Click on Saved map > Click on geometry > Click on View attributes

# Click on map > Click on Layers > Click on saved map > Add map > Click on Geometry > Click on View Event

# Click on map > Click on layers > Click on saved map > saved map > Select an asset map > click on view Asset

# Click on map > Click on layers > Click on saved map > saved map > Select an Contact map > click on view Contact

# Click on map > Click on layers > Click on saved map > saved map > Select an Task map > click on view Task

# Duplicate Geometry Click on map >Add geometry>Click on Duplicate>select the type>Click on the geometry again and drag


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest
import os


class TestCreateObjectsFromMappingLayer(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        path = "./screenshots"
        os.chdir(path)
        self.driver.save_screenshot("test_CreateObjectsFromMappingLayer" + ".png")
        os.chdir("..")

        self.driver.quit()

    def test_CreateObjectsFromMappingLayer(self):

        logging.info("starting Test Case: Create objects from Mapping layer")
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

        # Maps > Layers > Select layers > Tools > Plot a point > Create > Event > Type > Save
        main_page.open_MAP()
        common_page.alert_popup_allow()
        map_page = LoadClass.load_page("MapPage")
        map_page.setDriver(self.driver)
        map_page.wait_for_map_to_load()
        map_page.click_layers_button()
        map_page.choose_first_layer_from_the_list()
        map_page.click_done_button()
        common_page.wait_for_app_loading()
        map_page.click_plot_button()
        map_page.click_tool_button()
        map_page.click_point_button()
        map_page.click_point_default_button()
        map_page.click_in_map_area_1()
        map_page.save_map()
        map_page.choose_second_plot_object()
        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.choose_Incident_type_of_event()
        events_page.fill_Name_input_field("Mapping")
        events_page.click_severity_lvl_picker()
        events_page.choose_severity_level_1()
        events_page.scroll_down_to_save_button()
        events_page.click_save_new_event()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Maps > Layers > Select layers > Tools > Plot a line > Create > Asset > Type > Save
        main_page.open_MAP()
        map_page.wait_for_map_to_load()
        map_page.click_layers_button()
        map_page.choose_second_layer_from_the_list()
        map_page.click_done_button()
        common_page.wait_for_app_loading()
        map_page.click_plot_button()
        map_page.click_tool_button()
        map_page.click_point_default_button()
        map_page.click_in_map_area_1()
        map_page.click_tool_button()
        map_page.click_line_button()
        map_page.click_line_default_button()
        map_page.click_in_map_area_2()
        map_page.double_tap_on_map()
        map_page.save_map()
        map_page.choose_first_plot_object()
        assets_page = LoadClass.load_page('AssetsPage')
        assets_page.setDriver(self.driver)
        assets_page.choose_asset_type()
        assets_page.fill_Name_input_field("Mapping")
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Maps > Layers > Select layers > Tools > Plot a circle > Create > Report > Type > Save
        main_page.open_MAP()
        map_page.wait_for_map_to_load()
        map_page.click_layers_button()
        map_page.choose_third_layer_from_the_list()
        map_page.click_done_button()
        common_page.wait_for_app_loading()
        map_page.click_plot_button()
        map_page.click_tool_button()
        map_page.click_circle_button()
        map_page.click_circle_default_button()
        map_page.click_in_map_area_2()
        map_page.save_map()
        map_page.choose_third_plot_object()
        reports_page = LoadClass.load_page('ReportsPage')
        reports_page.setDriver(self.driver)
        reports_page.choose_report_type_with_all_fields()
        reports_page.type_title("Mapping")
        reports_page.click_on_lodging_agency_picker()
        reports_page.choose_lodging_agency()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_new_report()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Maps > Layers > Select layers > Tools > Plot a polygon > Create > Task > Type > Save
        main_page.open_MAP()
        map_page.wait_for_map_to_load()
        map_page.click_layers_button()
        map_page.choose_first_layer_from_the_list()
        map_page.click_done_button()
        common_page.wait_for_app_loading()
        map_page.click_plot_button()
        map_page.click_tool_button()
        map_page.click_point_button()
        map_page.click_point_default_button()
        map_page.click_in_map_area_1()
        map_page.click_tool_button()
        map_page.click_polygon_button()
        map_page.click_polygon_default_button()
        map_page.click_in_map_area_1()
        map_page.click_in_map_area_2()
        map_page.double_tap_on_map()
        map_page.save_map()
        map_page.choose_fourth_plot_object()
        tasks_page = LoadClass.load_page('TasksPage')
        tasks_page.setDriver(self.driver)
        tasks_page.type_title("Mapping")
        tasks_page.click_on_assigned()
        tasks_page.add_contacts_and_groups()
        # tasks_page.choose_users()
        tasks_page.choose_first_contacts_group_on_the_list()
        tasks_page.click_ok_button()
        tasks_page.click_start_date()
        tasks_page.choose_current_date()
        tasks_page.scroll_down_to_save_button()
        tasks_page.click_save_new_task()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Navigate to Events > Check the type of Event created above
        main_page.open_EVENTS()
        events_page.clear_Search_field()
        events_page.type_text_into_search_field("Mapping")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        events_page.open_previously_created_event()
        common_page.wait_for_app_loading()
        events_page.check_if_view_on_map_button_is_present()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Navigate to Reports > Check the type of Report created above
        main_page.open_REPORTS()
        reports_page.clear_Search_field()
        reports_page.type_text_into_search_field("Mapping")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        reports_page.open_existing_report()
        common_page.wait_for_app_loading()
        reports_page.check_if_view_on_map_button_is_present()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Navigate to Assets > Check the type of created above
        main_page.open_ASSETS()
        assets_page.clear_Search_field()
        assets_page.type_text_into_search_field("Mapping")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        assets_page.open_existing_asset()
        common_page.wait_for_app_loading()
        assets_page.check_if_view_on_map_button_is_present()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Navigate to Tasks > Check the type of created above
        main_page.scroll_down_to_tasks_button()
        main_page.open_TASKS()
        tasks_page.clear_Search_field()
        tasks_page.type_text_into_search_field("Mapping")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        tasks_page.click_first_task_on_the_list()
        common_page.wait_for_app_loading()
        tasks_page.check_if_view_on_map_button_is_present()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        # Click on Event > Create a new event > Click on Create mapping data > Click on Tool >
        # Add Geometry > Save map -> Edit event > Click on mapping data > Click on Geometry > View attributes
        main_page.scroll_up_to_events_button()
        main_page.open_EVENTS()
        common_page.wait_for_app_loading()
        events_page.click_more_button_in_events_list()
        events_page.click_New_event_button()
        events_page.choose_Incident_type_of_event()
        events_page.fill_Name_input_field("Mapping2")
        events_page.click_severity_lvl_picker()
        events_page.choose_severity_level_1()
        events_page.scroll_down_to_save_button()
        events_page.click_create_mapping_data()
        map_page.wait_for_map_to_load()
        map_page.click_tool_button()
        map_page.click_point_button()
        map_page.click_point_default_button()
        map_page.click_in_map_area_1()
        map_page.save_map()
        events_page.scroll_down_to_save_button()
        events_page.click_save_new_event()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_EVENTS()
        events_page.clear_Search_field()
        events_page.type_text_into_search_field("Mapping2")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        events_page.open_previously_created_event()
        common_page.wait_for_app_loading()
        events_page.click_view_on_map_button()
        common_page.wait_for_app_loading()
        map_page.check_presents_of_added_layer()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Click on Map > Click on layers > Click on Saved map > Choose map for mobile
        main_page.open_MAP()
        map_page.wait_for_map_to_load()
        map_page.click_layers_button()
        map_page.click_saved_maps_button()
        map_page.choose_map_for_mobile()
        common_page.wait_for_app_loading()
        map_page.check_presents_of_added_layer_for_mobile()

        # Click on map > Click on Layers > Click on saved map > Add map > Click on Geometry > Click on View Event
        map_page.click_layers_button()
        map_page.click_saved_maps_button()
        map_page.choose_map_all_active_events()
        common_page.wait_for_app_loading()
        map_page.check_presents_of_added_layer()
        map_page.click_on_added_layer()
        map_page.click_view_layer_attributes()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Click on map > Click on layers > Click on saved map > Select an asset map > click on view Asset
        main_page.open_MAP()
        map_page.wait_for_map_to_load()
        map_page.click_layers_button()
        map_page.click_saved_maps_button()
        map_page.choose_map_all_assets()
        common_page.wait_for_app_loading()
        map_page.check_presents_of_added_layer()
        map_page.click_on_added_layer()
        map_page.click_view_layer_attributes()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Click on map > Click on layers > Click on saved map > Select an Contact map > click on view Contact
        main_page.open_MAP()
        map_page.wait_for_map_to_load()
        map_page.click_layers_button()
        map_page.click_saved_maps_button()
        map_page.choose_map_all_contacts()
        common_page.wait_for_app_loading()
        map_page.check_presents_of_added_layer()
        map_page.click_on_added_layer()
        map_page.click_view_layer_attributes()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Click on map > Click on layers > Click on saved map > Select an Task map > click on view Task
        main_page.open_MAP()
        map_page.wait_for_map_to_load()
        map_page.click_layers_button()
        map_page.click_saved_maps_button()
        map_page.choose_map_all_tasks()
        common_page.wait_for_app_loading()
        map_page.check_presents_of_added_layer()
        map_page.click_on_added_layer()
        map_page.click_view_layer_attributes()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Click on map > Add geometry > Click on added geometry > click Duplicate button >
        # select the type > Click on the geometry again and drag
        main_page.open_MAP()
        map_page.wait_for_map_to_load()
        map_page.click_plot_button()
        map_page.click_tool_button()
        map_page.click_point_default_button()  # point selector is already expanded
        map_page.click_in_map_area_1()
        map_page.check_presents_of_added_layer()
        map_page.click_on_added_layer()
        map_page.click_duplicate_button()
        map_page.click_point_2_button()
        map_page.click_on_duplicated_geometry()
        map_page.drag_and_drop_duplicated_geometry()
        common_page.take_screenshot("Map_drag_and_drop")
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCreateObjectsFromMappingLayer)
    unittest.TextTestRunner(verbosity=2).run(suite)
