# Test Case - Load Type Data After Login -- OCAMOB-241


# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present

# Turn on airplane mode
# While offline, create an event.
# While offline, update an event.
# While offline, delete an event.

# While offline, create an asset.
# While offline, update an asset.
# While offline, delete an asset.

# While offline, create a contact group.
# While offline, update a contact group.
# While offline, delete a contact group.

# While offline, create a contact.
# While offline, update a contact.
# While offline, delete a contact.

# While offline, create a report.
# While offline, update a report.
# While offline, delete a report.

# While offline, create a task.
# While offline, update a task.
# While offline, delete a task.

# From the main menu, press Offline Sync. -- View the outgoing queue of all objects created, updated & deleted above.
# Connect to the internet. View the offline sync.  -- Objects created, updated & deleted above are applied
#  to the system. The outgoing queue empties.
# Online- Open few reports,events,Documents (all objects)  Go to Flight mode and view the objects
# -- Objects can be viewed if it is cached


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest
import os
from configuration import PROJECT_ROOT


class TestOfflineObjects(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        # path = "./screenshots"
        path = PROJECT_ROOT + "/screenshots"
        os.chdir(path)
        self.driver.save_screenshot("test_Offline_Objects" + ".png")
        os.chdir("..")

        self.driver.quit()

    def test_Offline_Objects(self):

        logging.info("starting Test Case: Offline Objects")
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

        # airplane mode on
        common_page.switch_on_airplane_mode()
        common_page.hamburger_button()

        # logging.info(" --- While offline, create an event.")
        # main_page.scroll_up_to_events_button()
        # main_page.open_EVENTS()
        # events_page = LoadClass.load_page('EventsPage')
        # events_page.setDriver(self.driver)
        # events_page.click_more_button_in_events_list()
        # events_page.click_New_event_button()
        # events_page.choose_Incident_type_of_event()
        # events_page.fill_Name_input_field("Offline Object - Event")
        # events_page.click_severity_lvl_picker()
        # events_page.choose_severity_level_5()
        # events_page.scroll_down_to_save_button()
        # events_page.click_save_new_event()
        # common_page.wait_for_app_loading()
        # events_page.check_notification_about_offline_mode()
        # events_page.ok_button_on_offline_notification_popup()
        # common_page.wait_for_app_loading()
        #
        # logging.info(" --- While offline, update an event.")
        # events_page.open_first_pending_event()
        # common_page.wait_for_app_loading()
        # events_page.click_edit_button()
        # events_page.click_severity_lvl_picker()
        # events_page.choose_severity_level_5()
        # events_page.scroll_down_to_description_field()
        # events_page.type_text_into_description_field()
        # common_page.hide_keyboard()
        # events_page.scroll_down_to_save_button()
        # events_page.click_save_new_event()
        # common_page.wait_for_app_loading()
        # events_page.check_notification_about_offline_mode()
        # events_page.ok_button_on_offline_notification_popup()
        #
        # logging.info(" --- While offline, delete an event.")
        # events_page.click_more_button_in_event_details()
        # events_page.click_Delete_button()
        # events_page.alert_confirm_delete()
        # common_page.hamburger_button()
        # main_page.check_presence_of_events_button()
        #
        # logging.info(" --- While offline, create an asset.")
        # main_page.open_ASSETS()
        # assets_page = LoadClass.load_page('AssetsPage')
        # assets_page.setDriver(self.driver)
        # assets_page.click_new_button()
        # assets_page.click_new_asset()
        # assets_page.choose_asset_type()
        # assets_page.fill_Name_input_field("Offline Object - Asset")
        # assets_page.scroll_down_to_save_button()
        # assets_page.click_save_button()
        # assets_page.check_notification_about_offline_mode()
        # assets_page.ok_button_on_offline_notification_popup()
        #
        # logging.info(" --- While offline, update an asset.")
        # assets_page.open_first_pending_asset()
        # assets_page.click_edit_button()
        # assets_page.type_cost_per_unit_for_new_asset("2")
        # common_page.hide_keyboard()
        # assets_page.scroll_down_to_save_button()
        # assets_page.click_save_button()
        # common_page.wait_for_app_loading()
        # assets_page.check_notification_about_offline_mode()
        # assets_page.ok_button_on_offline_notification_popup()
        #
        # logging.info("While offline, delete an asset.")
        # assets_page.click_more_button()
        # assets_page.click_delete_this_asset()
        # assets_page.alert_accept_delete()
        # common_page.hamburger_button()
        # main_page.check_presence_of_events_button()
        #
        # logging.info(" --- While offline, create a contact group.")
        # main_page.scroll_down_to_contacts_button()
        # main_page.open_CONTACTS()
        # contacts_page = LoadClass.load_page('ContactsPage')
        # contacts_page.setDriver(self.driver)
        # contacts_page.click_new_button()
        # contacts_page.add_new_contact_group()
        # contacts_page.choose_group_for_new_contact_group_type()  # Group
        # contacts_page.type_name_for_new_contact_group("Offline Object - Contact Group")
        # contacts_page.scroll_down_to_save_button()
        # contacts_page.save_new_contact_group()
        # common_page.wait_for_app_loading()
        # contacts_page.check_notification_about_offline_mode()
        # contacts_page.ok_button_on_offline_notification_popup_for_contact_group()
        #
        # logging.info(" --- While offline, update a contact group.")
        # contacts_page.open_first_pending_contact_group()
        # contacts_page.click_group_info_button()
        # contacts_page.click_edit_group_button()
        # contacts_page.clear_name_for_new_contact_group()
        # contacts_page.type_name_for_new_contact_group("offline_contact_group")
        # common_page.hide_keyboard()
        # contacts_page.scroll_down_to_save_button()
        # contacts_page.save_new_contact_group()
        # common_page.wait_for_app_loading()
        # contacts_page.check_notification_about_offline_mode()
        # contacts_page.ok_button_on_offline_notification_popup_for_contact_group()
        # common_page.hamburger_button()
        # main_page.check_presence_of_inbox_button()
        #
        # logging.info(" --- While offline, create a contact.")
        # main_page.scroll_down_to_contacts_button()
        # main_page.open_CONTACTS()
        # contacts_page.open_offline_contacts_group()  # offline_contact_group
        # contacts_page.click_new_button()
        # contacts_page.add_new_contact_into_group()
        # contacts_page.choose_contact_type_person()
        # contacts_page.type_first_name_for_new_contact("Offline Object - Contact")
        # contacts_page.scroll_down_to_save_button()
        # contacts_page.save_new_contact()
        # common_page.wait_for_app_loading()
        # contacts_page.check_notification_about_offline_mode()
        # contacts_page.ok_button_on_offline_notification_popup_for_contact()
        #
        # logging.info(" --- While offline, update a contact.")
        # contacts_page.open_first_pending_contact()
        # contacts_page.click_edit_button()
        # contacts_page.fill_organisation_field("Bitnoise")
        # common_page.hide_keyboard()
        # contacts_page.scroll_down_to_save_button()
        # contacts_page.save_new_contact()
        # common_page.wait_for_app_loading()
        # contacts_page.check_notification_about_offline_mode()
        # contacts_page.ok_button_on_offline_notification_popup_for_contact()
        #
        # logging.info(" --- While offline, delete a contact.")
        # contacts_page.click_contact_more_button()
        # contacts_page.delete_contact()
        # contacts_page.confirm_delete()
        #
        # logging.info(" --- While offline, delete a contact group.")
        # contacts_page.click_group_info_button()
        # contacts_page.click_group_more_button()
        # contacts_page.delete_contact_group()
        # contacts_page.confirm_delete_contact_group()
        # common_page.hamburger_button()
        # main_page.check_presence_of_inbox_button()

        logging.info(" --- While offline, create a report.")
        main_page.scroll_up_to_reports_button()
        main_page.open_REPORTS()
        reports_page = LoadClass.load_page('ReportsPage')
        reports_page.setDriver(self.driver)
        reports_page.click_create_report_button()
        reports_page.choose_report_type_with_all_fields()
        reports_page.type_title("Offline Objects - Report")
        reports_page.click_on_lodging_agency_picker()
        reports_page.choose_lodging_agency()
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_new_report()
        common_page.wait_for_app_loading()
        reports_page.check_notification_about_offline_mode()
        reports_page.ok_button_on_offline_notification_popup()

        logging.info(" --- While offline, update a report.")
        reports_page.open_first_pending_report()
        common_page.wait_for_app_loading()
        reports_page.click_edit_button()
        reports_page.type_title("--offline-edited")
        reports_page.scroll_down_to_publish_button()
        reports_page.click_publish_new_report()
        common_page.wait_for_app_loading()
        reports_page.check_notification_about_offline_mode()
        reports_page.ok_button_on_offline_notification_popup()

        logging.info(" --- While offline, delete a report.")
        reports_page.click_more_button()
        reports_page.click_delete_report()
        reports_page.alert_accept_delete()
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        logging.info(" --- While offline, create a task.")
        main_page.scroll_down_to_tasks_button()
        main_page.open_TASKS()
        tasks_page = LoadClass.load_page('TasksPage')
        tasks_page.setDriver(self.driver)
        tasks_page.create_new_task()
        tasks_page.type_title("Offline Object - Task")
        tasks_page.click_on_assigned()
        tasks_page.add_contacts_and_groups()
        contacts_page.click_first_contact_on_the_list_with_checkbox_in_offline_mode()
        tasks_page.click_ok_button()
        tasks_page.click_start_date()
        tasks_page.choose_current_date()
        tasks_page.scroll_down_to_save_button()
        tasks_page.click_save_new_task()
        common_page.wait_for_app_loading()
        tasks_page.check_notification_about_offline_mode()
        tasks_page.ok_button_on_offline_notification_popup()

        logging.info(" --- While offline, update a task.")
        tasks_page.filter_tasks_to_all_tasks()
        tasks_page.open_first_pending_task()
        tasks_page.edit_task()
        tasks_page.type_text_into_detail_field("offline mode")
        common_page.hide_keyboard()
        tasks_page.scroll_down_to_save_button()
        tasks_page.click_save_new_task()
        common_page.wait_for_app_loading()
        tasks_page.check_notification_about_offline_mode()
        tasks_page.ok_button_on_offline_notification_popup()

        logging.info(" --- While offline, delete a task.")
        tasks_page.click_more_button()
        tasks_page.click_delete_button()
        tasks_page.confirm_deleting_task()
        common_page.hamburger_button()

        logging.info(" --- From the main menu, press Offline Sync. -- View the outgoing queue of all objects created,"
                     " updated & deleted above.")
        main_page.scroll_down_to_offline_sync_button()
        main_page.open_OFFLINE_SYNC()
        common_page.take_screenshot('Offline Objects - offline sync in offline mode')
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        # airplane mode off
        common_page.switch_off_airplane_mode()
        common_page.hamburger_button()

        logging.info(" --- Connect to the internet. View the offline sync.  -- Objects created,"
                     " updated & deleted above are applied to the system. The outgoing queue empties.")
        main_page.scroll_down_to_offline_sync_button()
        main_page.open_OFFLINE_SYNC()
        common_page.take_screenshot('Offline Objects - offline sync in online mode')
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        logging.info(" --- Online - Open few reports, events, Documents (all objects)")
        main_page.scroll_up_to_events_button()
        main_page.open_EVENTS()
        events_page.open_previously_created_event()
        events_page.click_edit_button()
        common_page.hamburger_button()

        main_page.scroll_up_to_reports_button()
        main_page.open_REPORTS()
        reports_page.open_existing_report()
        reports_page.click_edit_button()
        common_page.hamburger_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.open_first_contact_group()
        contacts_page.click_first_contact_on_the_list()
        contacts_page.click_edit_button()
        common_page.hamburger_button()

        main_page.scroll_down_to_tasks_button()
        main_page.open_TASKS()
        tasks_page.click_first_task_on_the_list()
        tasks_page.edit_task()
        common_page.hamburger_button()

        # airplane mode on
        common_page.switch_on_airplane_mode()
        common_page.hamburger_button()

        logging.info(" --- Go to Flight mode and view the previously opened objects"
                     " -- Objects can be viewed if it is cached")
        main_page.scroll_up_to_events_button()
        main_page.open_EVENTS()
        events_page.open_previously_created_event()
        events_page.click_edit_button()
        common_page.hamburger_button()

        main_page.scroll_up_to_reports_button()
        main_page.open_REPORTS()
        reports_page.open_existing_report()
        reports_page.click_edit_button()
        common_page.hamburger_button()

        main_page.scroll_down_to_contacts_button()
        main_page.open_CONTACTS()
        contacts_page.open_first_contact_group()
        contacts_page.click_first_contact_on_the_list()
        contacts_page.click_edit_button()
        common_page.hamburger_button()

        main_page.scroll_down_to_tasks_button()
        main_page.open_TASKS()
        tasks_page.click_first_task_on_the_list()
        tasks_page.edit_task()
        common_page.hamburger_button()

        # airplane mode off
        common_page.switch_off_airplane_mode()
        common_page.hamburger_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOfflineObjects)
    unittest.TextTestRunner(verbosity=2).run(suite)

