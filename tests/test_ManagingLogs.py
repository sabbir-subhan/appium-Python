# Test Case - Managing logs -- OCAMOB-59

# before running this test create:
# - log type with all fields, named: "log_with_all_fields"
# - log type with chooser fields, named: "log_with_chooser_fields", with log chooser filed as a last field in form
# - log type with on load and on save sequence (with default value = "test on load") and on save sequence, named: "log_with_on_load_sequence" (like in TC: Managing Events)
# - log type with visibility rules, named: "log_with_visibility_rules", with fields "New option list" - with options; "1", "2", "3" that options should restore 3 other fields. "field to restore",
# "New website address" with value: "http://bitnoi.se/" and "New email address" with value: "test@noggin.com" - visibility rules like in TC: Managing Events
# (option 1 restores field to restore, option 2 restores New email address field, option 3 restores New website address)


# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present

# Press Create log entry. Select a log entry type and fill in the log form with all field types (including a rich text field). Press Save.
# From the main menu press the Logs button. On the search form, filter logs by type and enter search terms.
# Select an existing log. Press Edit to update the log and press Save.
# Select an existing log. Press More > Delete log.
# Create a new log and select an event and asset.
# Create and update a log with chooser fields.
# On OCA Server (the website), configure a log type to have an on load sequence and on save sequence in two of its fields.
# On the mobile app, create logs of this type.
# Open new logs but don't save them.
# Create a log that has option lists and fields with visibility rules that clears hidden fields and restores default values.


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest


class TestManagingLogs(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_manage_logs(self):

        logging.info("starting Test Case: Managing Logs")
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

        # Press Create log entry. Select a log entry type and fill in the log form with all field types (including a rich text field). Press Save.
        main_page.open_LOGS()
        logs_page = LoadClass.load_page('LogsPage')
        logs_page.setDriver(self.driver)
        logs_page.create_new_log()
        logs_page.choose_log_type_with_all_fields()
        logs_page.click_on_lodging_agency_picker()
        logs_page.choose_lodging_agency()
        logs_page.scroll_down_to_entry_field()
        logs_page.type_text_into_entry_field("Appium log with all fields")
        common_page.hide_keyboard()
        logs_page.scroll_down_to_save_button()
        logs_page.click_save_new_log()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # From the main menu press the Logs button. On the search form, filter logs by type and enter search terms.
        main_page.open_LOGS()
        logs_page.expand_types_filter()
        logs_page.choose_second_filter()
        logs_page.expand_types_filter()
        logs_page.choose_third_filter()
        logs_page.expand_types_filter()
        logs_page.choose_first_filter()
        logs_page.type_text_into_search_field("all fields")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        logs_page.check_result()
        common_page.clear_Search_field()
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Select an existing log. Press Edit to update the log and press Save.
        main_page.open_LOGS()
        logs_page.open_first_log_on_the_list()
        logs_page.click_edit_button()
        logs_page.scroll_down_to_entry_field()
        logs_page.type_text_into_entry_field("  - edited")
        common_page.hide_keyboard()
        logs_page.scroll_down_to_save_button()
        logs_page.click_save_edited_log()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Select an existing log. Press More > Delete log.
        main_page.open_LOGS()
        logs_page.open_first_log_on_the_list()
        logs_page.click_more_button()
        logs_page.click_delete_log()
        logs_page.alert_accept_delete()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create a new log and select an event and asset.
        main_page.open_LOGS()
        logs_page.create_new_log()
        logs_page.choose_log_type_with_all_fields()
        logs_page.click_on_lodging_agency_picker()
        logs_page.choose_lodging_agency()
        logs_page.click_event_chooser_field()
        logs_page.choose_first_event_on_the_list()
        logs_page.click_asset_chooser_field()
        logs_page.choose_first_asset_on_the_list()
        logs_page.scroll_down_to_entry_field()
        logs_page.type_text_into_entry_field("Appium log with all fields")
        common_page.hide_keyboard()
        logs_page.scroll_down_to_save_button()
        logs_page.click_save_new_log()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create and update a log with chooser fields.
        main_page.open_LOGS()
        logs_page.create_new_log()
        logs_page.choose_log_type_with_chooser_fields()
        logs_page.click_on_lodging_agency_picker()
        logs_page.choose_lodging_agency()
        logs_page.scroll_down_to_entry_field()
        logs_page.type_text_into_entry_field("Log with chooser fields")
        common_page.hide_keyboard()
        logs_page.scroll_down_to_save_button()
        logs_page.click_save_new_log()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_LOGS()
        common_page.clear_Search_field()
        logs_page.type_text_into_search_field("chooser fields")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        logs_page.open_first_log_on_the_list()
        logs_page.click_edit_button()
        logs_page.scroll_down_to_save_button()
        logs_page.click_log_chooser_field()
        logs_page.choose_log_from_the_list()
        logs_page.scroll_down_to_save_button()
        logs_page.click_save_edited_log()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create log with on load sequence and on save sequence in two of its fields.
        main_page.open_LOGS()
        logs_page.create_new_log()
        logs_page.choose_log_type_with_on_load_sequence()
        logs_page.click_on_lodging_agency_picker()
        logs_page.choose_lodging_agency()
        logs_page.scroll_down_to_entry_field()
        logs_page.type_text_into_entry_field("Log with on load sequence")
        common_page.hide_keyboard()
        logs_page.check_on_load_and_on_save_sequences()
        logs_page.scroll_down_to_save_button()
        logs_page.click_save_new_log()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Open new logs but don't save them.
        main_page.open_LOGS()
        logs_page.create_new_log()
        logs_page.choose_log_type_with_all_fields()
        logs_page.click_on_lodging_agency_picker()
        logs_page.choose_lodging_agency()
        logs_page.scroll_down_to_entry_field()
        logs_page.type_text_into_entry_field("Appium test")
        common_page.hide_keyboard()
        logs_page.scroll_down_to_save_button()
        logs_page.click_cancel_new_log()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create a log that has option lists and fields with visibility rules that clears hidden fields and restores default values.
        main_page.open_LOGS()
        logs_page.create_new_log()
        logs_page.choose_log_type_with_visibility_rules()
        logs_page.click_on_lodging_agency_picker()
        logs_page.choose_lodging_agency()
        logs_page.scroll_down_to_entry_field()
        logs_page.type_text_into_entry_field("Log with visibility rules")
        common_page.hide_keyboard()
        logs_page.scroll_down_to_option_list()
        logs_page.click_on_option_list()
        logs_page.click_on_option_1()
        logs_page.check_restored_field_1()
        logs_page.click_on_option_list()
        logs_page.click_on_option_2()
        logs_page.check_restored_field_2()
        logs_page.check_hidden_field_1()
        logs_page.click_on_option_list()
        logs_page.click_on_option_3()
        logs_page.check_hidden_fields_1_and_2()
        logs_page.check_restored_field_3()
        logs_page.scroll_down_to_save_button()
        logs_page.click_save_new_log()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestManagingLogs)
    unittest.TextTestRunner(verbosity=2).run(suite)

