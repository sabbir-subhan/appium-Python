# Test Case - Read Only Properties -- OCAMOB-33

# before running test case:

# Go to setting > OCA designer > Create object types: Asset, Reports, Event, Risk
# for each new type add the following:
#   - option list: name = Is Read only ?, Options = Yes A, Yes B, No,
#  Maximum selected options = Height of field = 3, Default value = (None)
#   - *Options may come from a central list or a user-defined list

# Add the 2 sets of the following fields
# - phone number ("New phone number" input field should be visible on top of the form - on the first screen after creating new object)
# - option list
# - single-line text
# - multi-line text
# - rich text
# - fax number
# - cell number
# - email address
# - website address
# - location
# - date
# - date & time
# - date & optional time
# - number
# - sub form
# - single-line text inside the sub form

# DEFAULT VALUES: new_phone_number with value: +61212345111, new fax number with value: +61212345222,
# new email address with value: testbitnoise@gmail.com,
# new website address with value: http://www.google.com, new single line text with value: test_appium_single_line,
# new multi line text with value: test_appium_multi_line

# Make the 1st set of fields Read only if Is Read only ? = Yes A.
# Make the 2nd set of fields visible only if Is Read only ? = Yes B.
# Set up default values for all fields in both sets.


# TEST CASE STEPS:

# open OCA app
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss notifications
# check if button "EVENTS" is present

# create new Asset -> Do not select any options for is read only Y/N ->
# Verify that the second set of fields is hidden
# Set is Read only = Yes A and Yes B
# Check that the first set of fields is still Read only while set to their default values.
# Change the value of fields in the second set of fields and save the Asset
# Edit the details of created Asset and Check that the first set of fields is still Read only
# Uncheck all checkboxes in Is Read only ?, check "No" and then save the Asset

# Repeat the steps for Event
# Repeat the steps for Report
# Repeat the steps for Risk

import unittest
import logging
from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
from configuration import PROJECT_ROOT


class TestReadOnlyProperties(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        self.driver.save_screenshot(PROJECT_ROOT + "/screenshots/test_ReadOnlyProperties.png")

        self.driver.quit()

    def test_ReadOnlyProperties(self):

        logging.info("starting Test Case: Read Only Properties")
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

        # # create new Asset -> Do not select any options for is read only Y/N
        # logging.info('-------------------- MOVING TO "Assets"')
        # main_page.open_ASSETS()
        assets_page = LoadClass.load_page('AssetsPage')
        assets_page.setDriver(self.driver)
        # assets_page.click_new_button()
        # assets_page.click_new_asset()
        # assets_page.choose_asset_type_with_option_list()
        # assets_page.fill_Name_input_field("Read_only")
        #
        # # Verify that the second set of fields is hidden
        # assets_page.scroll_down_to_add_media_button()
        # assets_page.check_invisibility_of_second_set_of_fields()
        # assets_page.scroll_up_to_name_field()
        #
        # # Set is Read only = Yes A and Yes B
        # assets_page.read_only_option_list()
        # assets_page.option_list_option_yes_a()
        # assets_page.option_list_option_yes_b()
        # assets_page.save_option_list()
        #
        # # Check that the first set of fields is still Read only while set to their default values.
        # assets_page.check_if_first_set_of_fields_in_asset_with_option_list_is_disabled()
        # assets_page.check_fields_for_values_and_read_only_property()
        #
        # # Change the value of fields in the second set of fields and save the Asset
        # assets_page.scroll_up_to_name_field()
        # assets_page.fill_new_single_line_text2("test")
        # assets_page.fill_new_phone_number2("+61212345678")
        # assets_page.fill_new_multi_line_text2("test")
        # assets_page.fill_new_fax_number2("+61212345678")
        # assets_page.fill_new_email_address2("test90@onet.pl")
        # assets_page.fill_new_website_address2("http://www.google.com")
        # assets_page.fill_new_rich_text2(" test")
        # assets_page.fill_new_number2(" +61212345678 ")
        # assets_page.fill_new_mobile_number2("+61212345678")
        # assets_page.scroll_down_to_save_button()
        # assets_page.click_save_button()
        # common_page.check_popup_about_unfilled_fields()
        # common_page.wait_for_app_loading()
        # common_page.hamburger_button()
        # main_page.check_presence_of_events_button()
        #
        # # Edit the details of created Asset and Check that the first set of fields is still Read only
        # main_page.open_ASSETS()
        # assets_page.clear_Search_field()
        # assets_page.type_text_into_search_field("Read_only")
        # common_page.click_Return_button_on_keyboard()
        # common_page.hide_keyboard()
        # assets_page.open_existing_asset()
        # common_page.wait_for_app_loading()
        # assets_page.click_edit_button()
        # assets_page.check_if_first_set_of_fields_in_asset_with_option_list_is_disabled()
        #
        # # Uncheck all checkboxes in Is Read only ?, check "No" and then save the Asset
        # assets_page.fill_name_for_edited_asset(" edit")
        # assets_page.read_only_option_list()
        # assets_page.option_list_option_yes_a()
        # assets_page.option_list_option_yes_b()
        # assets_page.option_list_option_no()
        # assets_page.save_option_list()
        # assets_page.scroll_down_to_save_button()
        # assets_page.save_edited_asset()
        # common_page.check_popup_about_unfilled_fields()
        # common_page.wait_for_app_loading()
        # common_page.hamburger_button()
        # main_page.check_presence_of_events_button()
        #
        # main_page.open_ASSETS()
        # assets_page.clear_Search_field()
        # assets_page.type_text_into_search_field("Read_only edit")
        # common_page.click_Return_button_on_keyboard()
        # common_page.hide_keyboard()
        # assets_page.open_existing_asset()
        # common_page.wait_for_app_loading()
        # assets_page.click_edit_button()
        # assets_page.read_only_option_list()
        # assets_page.option_list_option_no()
        # assets_page.option_list_option_yes_a()
        # assets_page.option_list_option_yes_b()
        # assets_page.save_option_list()
        # assets_page.scroll_up_to_name_field()
        # assets_page.check_if_first_set_of_fields_in_asset_with_option_list_is_disabled()
        # assets_page.check_fields_for_values_and_read_only_property()
        # common_page.hamburger_button()
        # main_page.check_presence_of_events_button()

        # Repeat the steps for Event
        logging.info('-------------------- MOVING TO "Events"')
        # create new Event -> Do not select any options for is read only Y/N
        main_page.open_EVENTS()
        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.click_more_button_in_events_list()
        events_page.click_New_event_button()
        events_page.choose_event_type_with_option_list()
        events_page.fill_Name_input_field("Read_only")

        # Verify that the second set of fields is hidden
        common_page.scroll_down_to_add_media_button()
        assets_page.check_invisibility_of_second_set_of_fields()
        common_page.scroll_up_to_name_field()

        # Set is Read only = Yes A and Yes B
        events_page.read_only_option_list()
        assets_page.option_list_option_yes_a()
        assets_page.option_list_option_yes_b()
        assets_page.save_option_list()

        # Check that the first set of fields is still Read only while set to their default values.
        assets_page.check_if_first_set_of_fields_in_asset_with_option_list_is_disabled()
        assets_page.check_fields_for_values_and_read_only_property()

        # Change the value of fields in the second set of fields and save the Event
        common_page.scroll_up_to_name_field()
        events_page.fill_new_single_line_text2("test")
        events_page.fill_new_phone_number2("+61212345678")
        events_page.fill_new_multi_line_text2("test")
        events_page.fill_new_fax_number2("+61212345678")
        events_page.fill_new_email_address2("test90@onet.pl")
        events_page.fill_new_website_address2("http://www.google.com")
        events_page.fill_new_number2(" +61212345678 ")
        events_page.fill_new_mobile_number2("+61212345678")
        events_page.scroll_down_to_save_button()
        events_page.click_save_button()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Edit the details of created Event and Check that the first set of fields is still Read only
        main_page.open_EVENTS()
        events_page.clear_Search_field()
        events_page.type_text_into_search_field("Read_only")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        events_page.open_previously_created_event()
        common_page.wait_for_app_loading()
        events_page.click_edit_button()
        assets_page.check_if_first_set_of_fields_in_asset_with_option_list_is_disabled()

        # Uncheck all checkboxes in Is Read only ?, check "No" and then save the Event
        events_page.fill_name_for_edited_event(" edit")
        events_page.read_only_option_list()
        assets_page.option_list_option_yes_a()
        assets_page.option_list_option_yes_b()
        assets_page.option_list_option_no()
        assets_page.save_option_list()
        events_page.scroll_down_to_save_button()
        events_page.click_save_button()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_EVENTS()
        events_page.clear_Search_field()
        events_page.type_text_into_search_field("Read_only edit")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        events_page.open_previously_created_event()
        common_page.wait_for_app_loading()
        events_page.click_edit_button()
        events_page.read_only_option_list()
        assets_page.option_list_option_no()
        assets_page.option_list_option_yes_a()
        assets_page.option_list_option_yes_b()
        assets_page.save_option_list()
        assets_page.check_if_first_set_of_fields_in_asset_with_option_list_is_disabled()
        assets_page.check_fields_for_values_and_read_only_property()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Repeat the steps for Report
        logging.info('-------------------- MOVING TO "Reports"')
        main_page.open_REPORTS()
        reports_page = LoadClass.load_page('ReportsPage')
        reports_page.setDriver(self.driver)
        reports_page.click_create_report_button()
        reports_page.choose_report_type_with_option_list()
        reports_page.type_title("Read_only")
        reports_page.click_on_lodging_agency_picker()
        reports_page.choose_lodging_agency()

        # Verify that the second set of fields is hidden
        assets_page.scroll_down_to_add_media_button()
        assets_page.check_invisibility_of_second_set_of_fields()
        assets_page.scroll_up_to_name_field()

        # Set is Read only = Yes A and Yes B
        reports_page.read_only_option_list()
        assets_page.option_list_option_yes_a()
        assets_page.option_list_option_yes_b()
        assets_page.save_option_list()

        # Check that the first set of fields is still Read only while set to their default values.
        assets_page.check_if_first_set_of_fields_in_asset_with_option_list_is_disabled()
        assets_page.check_fields_for_values_and_read_only_property()

        # Change the value of fields in the second set of fields and save the Report
        common_page.scroll_up_to_name_field()
        reports_page.fill_new_single_line_text2("test")
        reports_page.fill_new_phone_number2("+61212345678")
        reports_page.fill_new_multi_line_text2("test")
        reports_page.fill_new_fax_number2("+61212345678")
        reports_page.fill_new_email_address2("test90@onet.pl")
        reports_page.fill_new_website_address2("http://www.google.com")
        reports_page.fill_new_number2(" +61212345678 ")
        reports_page.fill_new_mobile_number2("+61212345678")

        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_new_report()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Edit the details of created Report and check that the first set of fields is still Read only
        main_page.open_REPORTS()
        reports_page.clear_Search_field()
        reports_page.type_text_into_search_field("Read_only")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        reports_page.edit_first_report_on_the_list()
        common_page.wait_for_app_loading()
        reports_page.click_edit_button()
        assets_page.check_if_first_set_of_fields_in_asset_with_option_list_is_disabled()

        # Uncheck all checkboxes in Is Read only ?, check "No" and then save the Report
        reports_page.type_title_for_edited_report(" edit")
        reports_page.read_only_option_list()
        assets_page.option_list_option_yes_a()
        assets_page.option_list_option_yes_b()
        assets_page.option_list_option_no()
        assets_page.save_option_list()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_edited_report()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_REPORTS()
        reports_page.clear_Search_field()
        reports_page.type_text_into_search_field("Read_only edit")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        reports_page.edit_first_report_on_the_list()
        common_page.wait_for_app_loading()
        reports_page.click_edit_button()
        reports_page.read_only_option_list()
        assets_page.option_list_option_no()
        assets_page.option_list_option_yes_a()
        assets_page.option_list_option_yes_b()
        assets_page.save_option_list()
        assets_page.check_if_first_set_of_fields_in_asset_with_option_list_is_disabled()
        assets_page.check_fields_for_values_and_read_only_property()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Repeat the steps for Risk
        logging.info('-------------------- MOVING TO "Risks"')
        main_page.open_RISKS()
        risks_page = LoadClass.load_page('RisksPage')
        risks_page.setDriver(self.driver)
        risks_page.create_risk_register()
        risks_page.type_name_for_new_risk_register('Read_only_register')
        risks_page.create_new_context()
        risks_page.scroll_down_to_save_button()
        risks_page.click_save_button()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()

        risks_page.open_existing_risk_register()
        common_page.wait_for_app_loading()
        risks_page.click_new_button()
        risks_page.click_add_new_context()
        risks_page.type_name_for_new_context('Read_only_context')
        common_page.hide_keyboard()
        risks_page.scroll_down_to_save_button()
        risks_page.save_new_context()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Click on existing Risk Register > Click on existing context > Click on Add new Risk
        main_page.open_RISKS()
        risks_page.clear_Search_field()
        risks_page.type_text_into_search_field("Read_only_register")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        risks_page.open_existing_risk_register()
        common_page.wait_for_app_loading()
        risks_page.open_existing_context()
        common_page.wait_for_app_loading()
        risks_page.click_new_button()
        risks_page.click_add_new_risk()
        risks_page.choose_risk_with_option_list()
        risks_page.type_name_for_new_risk('Read_only')
        common_page.hide_keyboard()

        # Verify that the second set of fields is hidden
        common_page.scroll_down_to_add_media_button()
        assets_page.check_invisibility_of_second_set_of_fields()
        common_page.scroll_up_to_name_field()

        # Set is Read only = Yes A and Yes B
        risks_page.read_only_option_list()
        assets_page.option_list_option_yes_a()
        assets_page.option_list_option_yes_b()
        assets_page.save_option_list()

        # Check that the first set of fields is still Read only while set to their default values.
        assets_page.check_if_first_set_of_fields_in_asset_with_option_list_is_disabled()
        assets_page.check_fields_for_values_and_read_only_property()

        # Change the value of fields in the second set of fields and save the Risk
        common_page.scroll_up_to_name_field()
        risks_page.fill_new_single_line_text2("test")
        risks_page.fill_new_phone_number2("+61212345678")
        risks_page.fill_new_multi_line_text2("test")
        risks_page.fill_new_fax_number2("+61212345678")
        risks_page.fill_new_email_address2("test90@onet.pl")
        risks_page.fill_new_website_address2("http://www.google.com")
        risks_page.fill_new_number2(" +61212345678 ")
        risks_page.fill_new_mobile_number2("+61212345678")
        risks_page.scroll_down_to_save_button()
        risks_page.save_new_risk()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()

        # Edit the details of created Risk and check that the first set of fields is still Read only
        risks_page.open_existing_risk()
        common_page.wait_for_app_loading()
        risks_page.click_edit_button()
        assets_page.check_if_first_set_of_fields_in_asset_with_option_list_is_disabled()

        # Uncheck all checkboxes in Is Read only ?, check "No" and then save the Risk
        risks_page.type_name_for_edit_risk(" edit")
        risks_page.read_only_option_list()
        assets_page.option_list_option_yes_a()
        assets_page.option_list_option_yes_b()
        assets_page.option_list_option_no()
        assets_page.save_option_list()
        risks_page.scroll_down_to_save_button()
        risks_page.click_save_button()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()

        # main_page.open_RISKS()
        risks_page.clear_Search_field()
        risks_page.type_text_into_search_field("Read_only edit")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        risks_page.open_existing_risk()
        common_page.wait_for_app_loading()
        risks_page.click_edit_button()
        risks_page.read_only_option_list()
        assets_page.option_list_option_no()
        assets_page.option_list_option_yes_a()
        assets_page.option_list_option_yes_b()
        assets_page.save_option_list()
        assets_page.check_if_first_set_of_fields_in_asset_with_option_list_is_disabled()
        assets_page.check_fields_for_values_and_read_only_property()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReadOnlyProperties)
    unittest.TextTestRunner(verbosity=2).run(suite)
