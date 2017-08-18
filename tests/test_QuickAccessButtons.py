# Test Case - Quick Access buttons on OCA app -- OCAMOB-48

# before running this test:
# prepare Lodging Agency named: "contact_group_for_tests" and configure Quick Access buttons for mobile app
# Login to OCA server>Click on Settings>Mobile Quick access Buttons>Add Quick Access buttons (see task in Jira)
# remember to firstly open some link on device/emulator - Android will ask witch browser You want to use


# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present

# Click on Activate workflow quick access
# Click on Create contact quick access link
# Click on Create Task Quick access link
# Click on Create Report Quick access link
# Click on Quick access to link
# Click on Create event,Asset,Log quick access links


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest
from time import sleep
from configuration import PROJECT_ROOT


class TestQuickAccessButtons(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        self.driver.save_screenshot(PROJECT_ROOT + "/screenshots/test_QuickAccessButtons.png")

        self.driver.quit()

    def test_QuickAccessButtons(self):

        logging.info("starting Test Case: Quick Access buttons on OCA app")
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

        main_page.click_ACTIVATE_WORKFLOW()
        main_page.click_ACTIVATE_BUTTON_on_alert()
        main_page.check_if_alert_WORKFLOW_ACTIVATED_is_present()
        main_page.check_presence_of_events_button()

        main_page.open_CREATE_CONTACT()
        new_contact_page = LoadClass.load_page('ContactsPage')
        new_contact_page.setDriver(self.driver)
        new_contact_page.type_first_name_for_new_contact("Name for new contact test")
        new_contact_page.scroll_down_to_save_button()
        new_contact_page.save_new_contact()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_CREATE_TASK()
        new_task_page = LoadClass.load_page('TasksPage')
        new_task_page.setDriver(self.driver)
        new_task_page.type_title("Title for new task test")
        new_task_page.click_on_assigned()
        new_task_page.add_contacts_and_groups()
        # new_task_page.choose_users()
        new_task_page.choose_first_contacts_group_on_the_list()
        new_task_page.click_ok_button()
        new_task_page.click_start_date()
        new_task_page.choose_current_date()
        new_task_page.scroll_down_to_save_button()
        new_task_page.click_save_new_task()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_CREATE_REPORT()
        new_report_page = LoadClass.load_page('ReportsPage')
        new_report_page.setDriver(self.driver)
        new_report_page.type_title("Title for new report test")
        new_report_page.click_on_lodging_agency_picker()
        new_report_page.choose_lodging_agency()
        new_report_page.scroll_down_to_publish_button()
        new_report_page.click_publish_new_report()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_WEBSITE_LINK()
        sleep(15)  # wait for page to load
        common_page.click_back_button()
        main_page.check_presence_of_events_button()

        main_page.open_INCIDENT()
        event_edit_page = LoadClass.load_page('EventsPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.fill_Name_input_field("Name for new incident test")
        event_edit_page.scroll_down_to_save_button()
        event_edit_page.click_save_new_event()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_CREATE_ASSETS()
        new_asset_page = LoadClass.load_page('AssetsPage')
        new_asset_page.setDriver(self.driver)
        new_asset_page.fill_Name_input_field("Name for new asset test")
        new_asset_page.scroll_down_to_save_button()
        new_asset_page.click_save_button()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_CREATE_LOG()
        new_log_page = LoadClass.load_page('LogsPage')
        new_log_page.setDriver(self.driver)
        new_log_page.click_on_lodging_agency_picker()
        new_log_page.choose_lodging_agency()
        new_log_page.scroll_down_to_entry_field()
        new_log_page.type_text_into_entry_field("Entry for new log test")
        common_page.hide_keyboard()
        new_log_page.scroll_down_to_save_button()
        new_log_page.click_save_new_log()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQuickAccessButtons)
    unittest.TextTestRunner(verbosity=2).run(suite)
