# Test Case - Offline sync view default to edit mode not view mode by default  -- OCAMOB-242

# before running this test:
# Login to OCA server, Click on OCA designer, Click on Mobile Dashboards Add quick access links to create all objects:
# Events, Assets, Reports, Contact, Log, Send communication


# Login to OCA app:
# open OCA app
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss notifications
# check if button "EVENTS" is present

# Create event using the quick access link
# switch to airplane mode
# quick access link to create event > Add mandatory fields > Save
# click on the Hamburger menu icon and Select  on event created
# - View mode of the event is displayed. Click on Edit to edit the event displayed.
# - User is able to view all the offline events under pending events
# - clicking on the pending item should result into jumping to the view mode
# Repeat steps for low use account type


import unittest
import logging
from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
from configuration import PROJECT_ROOT


class TestOfflineSyncViewMode(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        self.driver.save_screenshot(PROJECT_ROOT + "/screenshots/test_OfflineSyncViewMode.png")

        self.driver.quit()

    def test_OfflineSyncViewMode_high_user(self):

        logging.info("starting Test Case: Offline Sync View Mode for high user")
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

        # Create event using the quick access link
        main_page.open_INCIDENT()
        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.fill_Name_input_field("OfflineSyncViewMode_online")
        events_page.scroll_down_to_save_button()
        events_page.click_save_new_event()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_COMPOSE()
        compose_page = LoadClass.load_page('ComposePage')
        compose_page.setDriver(self.driver)
        compose_page.add_recipients()
        compose_page.add_contacts_and_groups()
        compose_page.clear_Search_field()
        compose_page.type_text_into_search_field("A_CONTACT_FOR_APPIUM_TESTS")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        compose_page.click_first_contact_on_the_list_with_checkbox()
        compose_page.click_ok_button()
        compose_page.choose_email_message()
        compose_page.type_email_subject()
        compose_page.type_email_message()
        common_page.hide_keyboard()
        compose_page.click_email_ok_button()
        compose_page.click_send_button()
        compose_page.alert_send_button()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        # Go to offline mode
        # airplane mode on
        common_page.switch_on_airplane_mode()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create event using the quick access link
        main_page.open_INCIDENT()
        common_page.wait_for_app_loading()
        common_page.offline_retry_button()
        events_page.fill_Name_input_field("OfflineSyncViewMode_offline")
        events_page.scroll_down_to_save_button()
        events_page.click_save_new_event()
        common_page.check_popup_about_unfilled_fields()
        events_page.check_notification_about_offline_mode()
        events_page.ok_button_on_offline_notification_popup()
        common_page.wait_for_app_loading()

        # Click on the Hamburger menu icon and click on events
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()
        main_page.scroll_up_to_events_button()
        main_page.open_EVENTS()
        events_page.open_first_pending_event()
        common_page.wait_for_app_loading()
        events_page.click_edit_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Repeat steps for Assets
        main_page.open_CREATE_ASSETS()
        assets_page = LoadClass.load_page('AssetsPage')
        assets_page.setDriver(self.driver)
        assets_page.fill_Name_input_field("OfflineSyncViewMode_offline")
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        assets_page.check_notification_about_offline_mode()
        assets_page.ok_button_on_offline_notification_popup()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.scroll_up_to_events_button()
        main_page.open_ASSETS()
        assets_page.open_first_pending_asset()
        common_page.wait_for_app_loading()
        assets_page.click_edit_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Repeat steps for Reports
        main_page.open_CREATE_REPORT()
        reports_page = LoadClass.load_page('ReportsPage')
        reports_page.setDriver(self.driver)
        reports_page.type_title("OfflineSyncViewMode_offline")
        reports_page.click_on_lodging_agency_picker()
        reports_page.choose_lodging_agency()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_new_report()
        common_page.check_popup_about_unfilled_fields()
        reports_page.ok_button_on_offline_notification_popup()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_REPORTS()
        reports_page.open_first_pending_report()
        common_page.wait_for_app_loading()
        reports_page.click_edit_button()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        # Repeat steps for Contact (firstly create Contact Group)
        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page = LoadClass.load_page('ContactsPage')
        contacts_page.setDriver(self.driver)
        contacts_page.click_new_button()
        contacts_page.add_new_contact_group()
        contacts_page.choose_group_for_new_contact_group_type()  # Group
        contacts_page.type_name_for_new_contact_group("OfflineSyncViewMode_offline")
        contacts_page.scroll_down_to_save_button()
        contacts_page.save_new_contact_group()
        common_page.wait_for_app_loading()
        contacts_page.check_notification_about_offline_mode()
        contacts_page.ok_button_on_offline_notification_popup_for_contact_group()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.open_first_pending_contact_group()
        contacts_page.click_new_button()
        contacts_page.add_new_contact_into_group()
        contacts_page.choose_contact_type_person()
        contacts_page.type_first_name_for_new_contact("OfflineSyncViewMode_offline")
        contacts_page.scroll_down_to_save_button()
        contacts_page.save_new_contact()
        common_page.wait_for_app_loading()
        contacts_page.check_notification_about_offline_mode()
        contacts_page.ok_button_on_offline_notification_popup_for_contact()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        # Repeat steps for Logs
        main_page.scroll_up_to_events_button()
        main_page.open_CREATE_LOG()
        logs_page = LoadClass.load_page('LogsPage')
        logs_page.setDriver(self.driver)
        logs_page.click_on_lodging_agency_picker()
        logs_page.choose_lodging_agency()
        logs_page.scroll_down_to_entry_field()
        logs_page.type_text_into_entry_field("OfflineSyncViewMode_offline")
        common_page.hide_keyboard()
        logs_page.scroll_down_to_save_button()
        logs_page.click_save_new_log()
        common_page.check_popup_about_unfilled_fields()
        logs_page.ok_button_on_offline_notification_popup()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Repeat steps for Send communication
        main_page.open_COMPOSE()
        compose_page.add_recipients()
        compose_page.add_contacts_and_groups()
        compose_page.clear_Search_field()
        compose_page.type_text_into_search_field("A_CONTACT_FOR_APPIUM_TESTS")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        compose_page.click_first_contact_on_the_list_with_checkbox()
        compose_page.click_ok_button()
        compose_page.choose_email_message()
        compose_page.type_email_subject()
        compose_page.type_email_message()
        common_page.hide_keyboard()
        compose_page.click_email_ok_button()
        compose_page.click_send_button()
        compose_page.alert_send_button()
        compose_page.check_offline_notification_alert()
        compose_page.ok_button_on_alert()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # airplane mode off
        common_page.switch_off_airplane_mode()
        common_page.hamburger_button()

    def test_OfflineSyncViewMode_low_user(self):

        logging.info("starting Test Case: Offline Sync View Mode for low user")
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
        login_page.type_username('general_user')
        login_page.type_password('general_user')
        common_page.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        common_page.wait_for_app_loading()
        main_page = LoadClass.load_page('MainPage')
        main_page.setDriver(self.driver)
        main_page.alert_expiring_password()
        main_page.dismiss_notifications()
        main_page.check_presence_of_events_button()

        # Create event using the quick access link
        main_page.open_INCIDENT()
        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.fill_Name_input_field("OfflineSyncViewMode_online")
        events_page.scroll_down_to_save_button()
        events_page.click_save_new_event()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_COMPOSE()
        compose_page = LoadClass.load_page('ComposePage')
        compose_page.setDriver(self.driver)
        compose_page.add_recipients()
        compose_page.add_contacts_and_groups()
        compose_page.clear_Search_field()
        compose_page.type_text_into_search_field("A_CONTACT_FOR_APPIUM_TESTS")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        compose_page.click_first_contact_on_the_list_with_checkbox()
        compose_page.click_ok_button()
        compose_page.choose_email_message()
        compose_page.type_email_subject()
        compose_page.type_email_message()
        common_page.hide_keyboard()
        compose_page.click_email_ok_button()
        compose_page.click_send_button()
        compose_page.alert_send_button()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        # Go to offline mode
        # airplane mode on
        common_page.switch_on_airplane_mode()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Create event using the quick access link
        main_page.open_INCIDENT()
        common_page.wait_for_app_loading()
        common_page.offline_retry_button()
        events_page.fill_Name_input_field("OfflineSyncViewMode_offline")
        events_page.scroll_down_to_save_button()
        events_page.click_save_new_event()
        common_page.check_popup_about_unfilled_fields()
        events_page.check_notification_about_offline_mode()
        events_page.ok_button_on_offline_notification_popup()
        common_page.wait_for_app_loading()

        # Click on the Hamburger menu icon and click on events
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()
        main_page.scroll_up_to_events_button()
        main_page.open_EVENTS()
        events_page.open_first_pending_event()
        common_page.wait_for_app_loading()
        events_page.click_edit_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Repeat steps for Assets
        main_page.open_CREATE_ASSETS()
        assets_page = LoadClass.load_page('AssetsPage')
        assets_page.setDriver(self.driver)
        assets_page.fill_Name_input_field("OfflineSyncViewMode_offline")
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        assets_page.check_notification_about_offline_mode()
        assets_page.ok_button_on_offline_notification_popup()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.scroll_up_to_events_button()
        main_page.open_ASSETS()
        assets_page.open_first_pending_asset()
        common_page.wait_for_app_loading()
        assets_page.click_edit_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Repeat steps for Reports
        main_page.open_CREATE_REPORT()
        reports_page = LoadClass.load_page('ReportsPage')
        reports_page.setDriver(self.driver)
        reports_page.type_title("OfflineSyncViewMode_offline")
        reports_page.click_on_lodging_agency_picker()
        reports_page.choose_lodging_agency()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_new_report()
        common_page.check_popup_about_unfilled_fields()
        reports_page.ok_button_on_offline_notification_popup()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.open_REPORTS()
        reports_page.open_first_pending_report()
        common_page.wait_for_app_loading()
        reports_page.click_edit_button()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        # Repeat steps for Contact (firstly create Contact Group)
        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page = LoadClass.load_page('ContactsPage')
        contacts_page.setDriver(self.driver)
        contacts_page.click_new_button()
        contacts_page.add_new_contact_group()
        contacts_page.choose_group_for_new_contact_group_type()  # Group
        contacts_page.type_name_for_new_contact_group("OfflineSyncViewMode_offline")
        contacts_page.scroll_down_to_save_button()
        contacts_page.save_new_contact_group()
        common_page.wait_for_app_loading()
        contacts_page.check_notification_about_offline_mode()
        contacts_page.ok_button_on_offline_notification_popup_for_contact_group()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.open_first_pending_contact_group()
        contacts_page.click_new_button()
        contacts_page.add_new_contact_into_group()
        contacts_page.choose_contact_type_person()
        contacts_page.type_first_name_for_new_contact("OfflineSyncViewMode_offline")
        contacts_page.scroll_down_to_save_button()
        contacts_page.save_new_contact()
        common_page.wait_for_app_loading()
        contacts_page.check_notification_about_offline_mode()
        contacts_page.ok_button_on_offline_notification_popup_for_contact()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        # Repeat steps for Logs
        main_page.scroll_up_to_events_button()
        main_page.open_CREATE_LOG()
        logs_page = LoadClass.load_page('LogsPage')
        logs_page.setDriver(self.driver)
        logs_page.click_on_lodging_agency_picker()
        logs_page.choose_lodging_agency()
        logs_page.scroll_down_to_entry_field()
        logs_page.type_text_into_entry_field("OfflineSyncViewMode_offline")
        common_page.hide_keyboard()
        logs_page.scroll_down_to_save_button()
        logs_page.click_save_new_log()
        common_page.check_popup_about_unfilled_fields()
        logs_page.ok_button_on_offline_notification_popup()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Repeat steps for Send communication
        main_page.open_COMPOSE()
        compose_page = LoadClass.load_page('ComposePage')
        compose_page.setDriver(self.driver)
        compose_page.add_recipients()
        compose_page.add_contacts_and_groups()
        compose_page.clear_Search_field()
        compose_page.type_text_into_search_field("A_CONTACT_FOR_APPIUM_TESTS")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        compose_page.click_first_contact_on_the_list_with_checkbox()
        compose_page.click_ok_button()
        compose_page.choose_email_message()
        compose_page.type_email_subject()
        compose_page.type_email_message()
        common_page.hide_keyboard()
        compose_page.click_email_ok_button()
        compose_page.click_send_button()
        compose_page.alert_send_button()
        compose_page.check_offline_notification_alert()
        compose_page.ok_button_on_alert()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # airplane mode off
        common_page.switch_off_airplane_mode()
        common_page.hamburger_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOfflineSyncViewMode)
    unittest.TextTestRunner(verbosity=2).run(suite)
