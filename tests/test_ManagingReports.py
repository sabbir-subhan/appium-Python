# Test Case - Managing Reports -- OCAMOB-60

# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present
# From the main menu click on Assets

# From the main menu press Reports
# Filter reports by type, status and keywords using the search form
# Press Create report. From the list that appears select a report type which has all field types, including a rich text field
# Fill in the form and press publish
# Select the report you created and press Edit
# Change some values and press Save
# Select a report, and press More > Delete report. Press Delete at the prompt
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
from time import sleep


class TestManagingReports(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_manage_reports(self):

        logging.info("starting Test Case: Assets")
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

        # Assets > New > New Asset > Select Type > Create and save
        main_page.open_ASSETS()
        assets_page = LoadClass.load_page('AssetsPage')
        assets_page.setDriver(self.driver)
        assets_page.click_new_button()
        assets_page.click_new_asset()
        assets_page.choose_asset_type()
        assets_page.fill_Name_input_field("Asset test")
        # common_page.hide_keyboard()
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # From the main menu press Reports - Filter reports by type, status and keywords using the search form
        main_page.open_REPORTS()
        reports_page = LoadClass.load_page('ReportsPage')
        reports_page.setDriver(self.driver)
        reports_page.filter_reports_by_type()
        reports_page.filter_reports_by_status()
        reports_page.filter_reports_by_search_field()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestManagingReports)
    unittest.TextTestRunner(verbosity=2).run(suite)
