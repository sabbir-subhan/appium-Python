# Test Case - Managing Reports -- OCAMOB-60

# before running this test create:
# - Lodging agency named: "contact_group_for_tests"
# - report type with all fields, named: "report_for_tests"
# - report type with chooser fields, named: "report_with_chooser_fields"
# - report type with on load and on save sequence (with default value = "test on load") and on save sequence, named: "report_with_on_load_sequence" (like in TC: Managing Events)
# - report type with visibility rules, named: "report_with_visibility_rules", with fields "New option list" - with options; "1", "2", "3" that options should restore 3 other fields. "field to restore",
# "New website address" with value: "http://bitnoi.se/" and "New email address" with value: "test@noggin.com" - visibility rules like in TC: Managing Events
# (option 1 restores field to restore, option 2 restores New email address field, option 3 restores New website address)
# report type with on create approval workflow, named: "report_with_on_create_approval"

# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present

# From the main menu press Reports >Press Create report. From the list that appears select a report type which has all field types, including a rich text field >
# Fill in the form and press publish
# Filter reports by type, status and keywords using the search form
# Select the report you created and press Edit > Change some values and press Save
# Select a report, and press More > Delete report. Press Delete at the prompt


# BELLOW STEPS CAN NOT BE DONE USING APPIUM:
# As a high user, edit a report and leave the report form open
# Login on another device as a low user and attempt to edit the same report from step 8
# As the lower user on another device edit a different report. Leave the report form open
# As a high user, edit the same report as step 10


# Create and update a report with chooser fields
# Create a report and fill in some fields, but don't publish it. Instead press cancel
# Create a report with an on create approval workflow and press publish
# Go back to the main menu > Tasks > Report Approval Task > Approve
# From the main menu, go to Settings and set a primary role. Go back to the main menu, Report > Create Report of any type and save
# Edit a report > Edit mapping data. Add points, circles, lines, polygons and other layers to the map
# Create a report type to have an on load sequence and on save sequence in two of its fields.
# Create a report that has option lists and fields with visibility rules that clears hidden fields and restores default values.


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest


class TestManagingReports(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_manage_reports(self):

        logging.info("starting Test Case: Managing Reports")
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

        # Press Create report. From the list that appears select a report type which has all field types, including a rich text field
        main_page.open_REPORTS()
        reports_page = LoadClass.load_page('ReportsPage')
        reports_page.setDriver(self.driver)
        reports_page.click_create_report_button()
        reports_page.choose_report_type_with_all_fields()
        reports_page.type_title("Large Report")
        reports_page.click_on_lodging_agency_picker()
        reports_page.choose_lodging_agency()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_new_report()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # From the main menu press Reports - Filter reports by type, status and keywords using the search form
        main_page.open_REPORTS()
        reports_page.filter_reports_by_type()
        reports_page.filter_reports_by_status()
        reports_page.type_text_into_search_field()  # search for Report containing word "Large"
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        reports_page.check_result()
        reports_page.clear_Search_field()
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Select the report you created and press Edit, Change some values and press Save
        main_page.open_REPORTS()
        reports_page.type_text_into_search_field()  # search for Report containing word "Large"
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        reports_page.check_result()
        reports_page.edit_created_report_with_all_fields()
        reports_page.click_edit_button()
        reports_page.edit_report_title(" - Edited")
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_edited_report()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Select a report, and press More > Delete report. Press Delete at the prompt
        main_page.open_REPORTS()
        reports_page.clear_Search_field()
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        reports_page.open_existing_report()
        reports_page.click_more_button()
        reports_page.click_delete_report()
        reports_page.alert_accept_delete()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create and update a report with chooser fields
        main_page.open_REPORTS()
        reports_page.click_create_report_button()
        reports_page.choose_report_type_with_chooser_fields()
        reports_page.type_title("Report with chooser fields")
        reports_page.click_on_lodging_agency_picker()
        reports_page.choose_lodging_agency()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_new_report()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_REPORTS()
        reports_page.search_for_report_with_chooser_fields()  # search for Report containing word "chooser fields"
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        reports_page.edit_created_report_with_chooser_fields()
        reports_page.click_edit_button()
        reports_page.edit_report_title(" - edited")
        reports_page.scroll_down_to_assets_chooser_field()
        reports_page.click_assets_chooser_field()
        reports_page.choose_asset_from_the_list()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_edited_report()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create a report and fill in some fields, but don't publish it. Instead press cancel
        main_page.open_REPORTS()
        reports_page.click_create_report_button()
        reports_page.choose_report_type_with_all_fields()
        reports_page.type_title("Appium test")
        reports_page.click_on_lodging_agency_picker()
        reports_page.choose_lodging_agency()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_cancel_new_report()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create a report with an on create approval workflow and press publish
        main_page.open_REPORTS()
        reports_page.click_create_report_button()
        reports_page.choose_report_type_with_on_create_approval_workflow()
        reports_page.type_title("Report with workflow")
        reports_page.click_on_lodging_agency_picker()
        reports_page.choose_lodging_agency()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_new_report()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Go back to the main menu > Tasks > Report Approval Task > Approve           ??????????????????????????
        main_page.scroll_down_to_tasks_button()
        main_page.open_TASKS()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        # From the main menu, go to Settings and set a primary role. Go back to the main menu, Report > Create Report of any type and save        ??????????????????????????

        # Edit a report > Edit mapping data. Add points, circles, lines, polygons and other layers to the map
        main_page.open_REPORTS()
        reports_page.filter_reports_by_active_status()
        reports_page.edit_first_report_on_the_list()
        reports_page.click_edit_button()
        reports_page.edit_report_title(" - map")
        reports_page.scroll_down_to_publish_button()
        reports_page.create_mapping_data()
        common_page.alert_popup_allow()
        map_page = LoadClass.load_page('MapPage')
        map_page.setDriver(self.driver)
        map_page.click_tool_button()
        map_page.click_point_button()
        map_page.click_default_button()
        map_page.click_in_map_area_1()
        map_page.click_tool_button()
        map_page.click_line_button()
        map_page.click_default_button()
        map_page.click_in_map_area_2()
        map_page.double_click_in_map_area_3()
        map_page.click_tool_button()
        map_page.click_circle_button()
        map_page.click_default_button()
        map_page.click_in_map_area_2()
        map_page.click_tool_button()
        map_page.click_polygon_button()
        map_page.click_default_button()
        map_page.click_in_map_area_1()
        map_page.click_in_map_area_2()
        map_page.double_click_in_map_area_3()
        map_page.save_map()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_edited_report()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create a report type to have an on load sequence and on save sequence in two of its fields.
        main_page.open_REPORTS()
        reports_page.click_create_report_button()
        reports_page.choose_report_type_with_on_load_sequence()
        reports_page.type_title("Report with on load sequence")
        reports_page.click_on_lodging_agency_picker()
        reports_page.choose_lodging_agency()
        reports_page.scroll_down_to_on_load_field()
        reports_page.check_on_load_and_on_save_sequences()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_new_report()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create a report that has option lists and fields with visibility rules that clears hidden fields and restores default values.
        main_page.open_REPORTS()
        reports_page.click_create_report_button()
        reports_page.choose_report_type_with_visibility_rules()
        reports_page.type_title("Report with visibility rules")
        reports_page.click_on_lodging_agency_picker()
        reports_page.choose_lodging_agency()

        reports_page.scroll_down_to_option_list()
        reports_page.click_on_option_list()
        reports_page.click_on_option_1()
        reports_page.check_restored_field_1()
        reports_page.click_on_option_list()
        reports_page.click_on_option_2()
        reports_page.check_restored_field_2()
        reports_page.check_hidden_field_1()
        reports_page.click_on_option_list()
        reports_page.click_on_option_3()
        reports_page.check_hidden_fields_1_and_2()
        reports_page.check_restored_field_3()

        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_new_report()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestManagingReports)
    unittest.TextTestRunner(verbosity=2).run(suite)
