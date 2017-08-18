# Test Case - Managing Reports -- OCAMOB-60

# before running this test create:
# - create Lodging agency named: "contact_group_for_tests" -- create new contact group and add "Agency" option to it
# - report type with all fields, named: "report_for_tests"
# - report type with chooser fields, named: "report_with_chooser_fields", must contain asset chooser field as a last field in form,
# - report type with on load and on save sequence (with default value = "test on load") and on save sequence, named: "report_with_on_load_sequence" (like in TC: Managing Events)
# - report type with visibility rules, named: "report_with_visibility_rules", with fields "New option list" - with options; "1", "2", "3" that options should restore 3 other fields. "field to restore",
# "New website address" with value: "http://bitnoi.se/" and "New email address" with value: "test@noggin.com" - visibility rules like in TC: Managing Events
# (option 1 restores 'field to restore', option 2 restores 'New email address', option 3 restores 'New website address')
# report type with on create approval workflow, named: "report_with_on_create_approval"
# - report type, named: "report_with_assigned_question" and workflow assigned to that - triggered on edit that report, that workflow must contain "Assign a question node" with title: "Report approval task"
#  and two possible answers: "Yes/No", (field Assign to: Contact that activated workflow: Workflow info)
# prepare Role for contact - choose contact that will be used to run test (default = Bitnoise QA)
# Go to a resource assignment and allocate yourself into a role - Contacts>Resource Assignment - Select any resource Assignment
# choose tab: Resources and click Structure button, in new window click Add - Contact role, type same new name and choose Role type as Role contacts and click OK and Save
# Choose the contact you are logged in as example Bitnoise QA - Open contact and click on Roles - You can see role allocation - Make sure that the status in IN


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
from configuration import PROJECT_ROOT


class TestManagingReports(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        self.driver.save_screenshot(PROJECT_ROOT + "/screenshots/test_ManageReports.png")

        self.driver.quit()

    def test_ManageReports(self):

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
        reports_page.type_title("Large")
        reports_page.click_on_lodging_agency_picker()
        reports_page.choose_lodging_agency()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_new_report()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # From the main menu press Reports - Filter reports by type, status and keywords using the search form
        main_page.open_REPORTS()
        reports_page.filter_reports_by_type()
        reports_page.filter_reports_by_status()
        reports_page.type_text_into_search_field("Large")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        reports_page.check_result()
        reports_page.clear_Search_field()
        common_page.hide_keyboard()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Select the report you created and press Edit, Change some values and press Save
        main_page.open_REPORTS()
        reports_page.type_text_into_search_field("Large")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        reports_page.check_result()
        reports_page.edit_created_report_with_all_fields()
        common_page.wait_for_app_loading()
        reports_page.click_edit_button()
        reports_page.edit_report_title(" - edited ")
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_edited_report()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Select a report, and press More > Delete report. Press Delete at the prompt
        main_page.open_REPORTS()
        reports_page.clear_Search_field()
        common_page.hide_keyboard()
        reports_page.open_existing_report()
        common_page.wait_for_app_loading()
        reports_page.click_more_button()
        reports_page.click_delete_report()
        reports_page.alert_accept_delete()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create and update a report with chooser fields
        main_page.open_REPORTS()
        reports_page.click_create_report_button()
        reports_page.choose_report_type_with_chooser_fields()
        reports_page.type_title("chooser_fields")
        reports_page.click_on_lodging_agency_picker()
        reports_page.choose_lodging_agency()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_new_report()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_REPORTS()
        reports_page.type_text_into_search_field("chooser_fields")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        reports_page.edit_created_report_with_chooser_fields()
        common_page.wait_for_app_loading()
        reports_page.click_edit_button()
        reports_page.edit_report_title(" - edited ")
        reports_page.scroll_down_to_assets_chooser_field()
        reports_page.click_assets_chooser_field()
        reports_page.choose_asset_from_the_list()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_edited_report()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create a report and fill in some fields, but don't publish it. Instead press cancel
        main_page.open_REPORTS()
        reports_page.click_create_report_button()
        reports_page.choose_report_type_with_all_fields()
        reports_page.type_title("Appium_test")
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
        reports_page.type_title("Report_with_workflow")
        reports_page.click_on_lodging_agency_picker()
        reports_page.choose_lodging_agency()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_new_report()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Go back to the main menu > Tasks > Report Approval Task > Approve
        main_page.open_REPORTS()
        reports_page.click_create_report_button()
        reports_page.choose_report_type_with_assigned_question()
        reports_page.type_title("assigned_question")
        reports_page.click_on_lodging_agency_picker()
        reports_page.choose_lodging_agency()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_new_report()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_REPORTS()
        reports_page.filter_reports_by_any_status()
        reports_page.clear_Search_field()
        reports_page.type_text_into_search_field("assigned_question")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        reports_page.edit_created_report_with_assigned_question()
        common_page.wait_for_app_loading()
        reports_page.click_edit_button()
        reports_page.scroll_down_media_release_field()
        reports_page.type_text_into_media_release_field()
        common_page.hide_keyboard()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_edited_report()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.scroll_down_to_tasks_button()
        main_page.open_TASKS()
        tasks_page = LoadClass.load_page('TasksPage')
        tasks_page.setDriver(self.driver)
        tasks_page.filter_tasks_to_required_action()
        tasks_page.clear_Search_field()
        tasks_page.type_text_into_search_field("Report approval")  # Report with workflow is creating task with title "Report approval"
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        tasks_page.click_first_task_on_the_list()
        common_page.wait_for_app_loading()
        tasks_page.click_button_yes_for_action_required()
        tasks_page.alert_confirm_action_required()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        # From the main menu, go to Settings and set a primary role. Go back to the main menu, Report > Create Report of any type and save
        main_page.scroll_down_to_tasks_button()
        main_page.open_SETTINGS()
        settings_page = LoadClass.load_page('SettingsPage')
        settings_page.setDriver(self.driver)
        settings_page.click_primary_role()
        settings_page.choose_first_role_on_the_list()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()
        main_page.scroll_up_to_reports_button()
        main_page.open_REPORTS()
        reports_page.click_create_report_button()
        reports_page.choose_report_type_with_all_fields()
        reports_page.type_title("Primary Role")
        reports_page.click_on_lodging_agency_picker()
        reports_page.choose_lodging_agency()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_new_report()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Edit a report > Edit mapping data. Add points, circles, lines, polygons and other layers to the map
        main_page.scroll_up_to_reports_button()
        main_page.open_REPORTS()
        reports_page.filter_reports_by_any_status()
        reports_page.clear_Search_field()
        reports_page.type_text_into_search_field("Large")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        reports_page.edit_first_report_on_the_list()
        common_page.wait_for_app_loading()
        reports_page.click_edit_button()
        reports_page.edit_report_title(" - map ")
        reports_page.scroll_down_to_publish_button()
        reports_page.create_mapping_data()
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
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_edited_report()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create a report type to have an on load sequence and on save sequence in two of its fields.
        main_page.open_REPORTS()
        reports_page.click_create_report_button()
        reports_page.choose_report_type_with_on_load_sequence()
        reports_page.type_title("Report_with_on_load_sequence")
        reports_page.click_on_lodging_agency_picker()
        reports_page.choose_lodging_agency()
        reports_page.scroll_down_to_on_load_field()
        reports_page.check_on_load_and_on_save_sequences()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_new_report()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create a report that has option lists and fields with visibility rules that clears hidden fields and restores default values.
        main_page.open_REPORTS()
        reports_page.click_create_report_button()
        reports_page.choose_report_type_with_visibility_rules()
        reports_page.type_title("Report_with_visibility_rules")
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
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestManagingReports)
    unittest.TextTestRunner(verbosity=2).run(suite)
