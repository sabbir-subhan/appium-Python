# Test Case - User unable edit and save events in offline mode  -- OCAMOB-325

# before running test case:

# Login to OCA server, Click on OCA designer, Click on Mobile Dashboards Add quick access links to create all objects:
# Events, Assets, Reports, Contact, Log, Send communication
# Quick access links should be configured like in TC: QuickAccessButtons

# Login to OCA app:
# open OCA app
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss notifications
# check if button "EVENTS" is present

# Create event using the quick access link
# Go to offline mode
# Create event using the quick access link
# Click on the Hamburger menu icon and click on events
# Click on the event created above
# Repeat steps for Assets
# Repeat steps for Reports
# Repeat steps for Logs
# Create Assets, Reports, Logs, Events using the other types


import unittest
import logging
from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
from configuration import PROJECT_ROOT
from time import sleep


class TestEditAndSaveObjectsInOfflineMode(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        self.driver.save_screenshot(PROJECT_ROOT + "/screenshots/test_EditAndSaveObjectsInOfflineMode.png")

        self.driver.quit()

    def test_EditAndSaveObjectsInOfflineMode(self):

        logging.info("starting Test Case: Edit And Save Objects In Offline Mode")
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
        events_page.fill_Name_input_field("Incident_online")
        events_page.scroll_down_to_save_button()
        events_page.click_save_new_event()
        common_page.check_popup_about_unfilled_fields()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Go to offline mode
        # airplane mode on
        common_page.switch_on_airplane_mode()
        common_page.hamburger_button()

        # Create event using the quick access link
        main_page.open_INCIDENT()
        # common_page.wait_for_app_loading()  # for Android 8 emulator
        events_page.fill_Name_input_field("Incident_offline")
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

        # Repeat steps for Assets
        main_page.open_CREATE_ASSETS()
        assets_page = LoadClass.load_page('AssetsPage')
        assets_page.setDriver(self.driver)
        assets_page.click_new_button()
        assets_page.click_new_asset()
        assets_page.choose_asset_type()
        assets_page.fill_Name_input_field("Offline Object - Asset")
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()
        assets_page.check_notification_about_offline_mode()
        assets_page.ok_button_on_offline_notification_popup()
        common_page.wait_for_app_loading()
        
        common_page.hamburger_button()
        main_page.scroll_up_to_events_button()
        main_page.open_ASSETS()
        assets_page.open_first_pending_asset()
        assets_page.click_edit_button()

        # Repeat steps for Reports
        # Repeat steps for Logs
        # Create Assets, Reports, Logs, Events using the other types  ?

        # airplane mode off
        common_page.switch_off_airplane_mode()
        common_page.hamburger_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEditAndSaveObjectsInOfflineMode)
    unittest.TextTestRunner(verbosity=2).run(suite)
