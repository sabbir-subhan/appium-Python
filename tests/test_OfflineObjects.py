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

# While offline, create a contact.
# While offline, update a contact.
# While offline, delete a contact.

# While offline, create a report.
# While offline, update a report.
# While offline, delete a report.

# While offline, create a task.
# While offline, update a task.
# While offline, delete a task.

# While offline, create a contact group.
# While offline, update a contact group.
# While offline, delete a contact group.

# From the main menu, press Offline Sync. -- View the outgoing queue of all objects created, updated & deleted above.
# Connect to the internet. View the offline sync.  -- Objects created, updated & deleted above are applied
#  to the system. The outgoing queue empties.
# Online- Open few reports,events,Documents (all objects)  Go to Flight mode and view the objects
# -- Objects can be viewed if it is cached


from Modules.AppiumTestResult import AppiumTestResult
from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest
import os


class TestOfflineObjects(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        path = "./screenshots"
        os.chdir(path)
        self.driver.save_screenshot("test_Offline_Objects" + ".png")
        os.chdir("..")

        self.driver.quit()

    #     logging.info("Quitting")
    #
    #     hasattr(self, '_outcome')
    #     result = self.defaultTestResult()  # these 2 methods have no side effects
    #     self._feedErrorsToResult(result, self._outcome.errors)
    #     error = self.list2reason(result.errors)
    #     failure = self.list2reason(result.failures)
    #     ok = not error and not failure
    #
    #     self.driver.quit()
    #
    #     # demo:   report short info immediately (not important)
    #     if not ok:
    #         typ, text = ('ERROR', error) if error else ('FAIL', failure)
    #         msg = [x for x in text.split('\n')[1:] if not x.startswith(' ')][0]
    #         print("\n%s: %s\n     %s" % (typ, self.id(), msg))
    #
    # def list2reason(self, exc_list):
    #     if exc_list and exc_list[-1][0] is self:
    #         return exc_list[-1][1]

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

        # While offline, create an event.
        main_page.scroll_up_to_events_button()
        main_page.open_EVENTS()
        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.click_more_button_in_events_list()
        events_page.click_New_event_button()
        events_page.choose_Incident_type_of_event()
        events_page.fill_Name_input_field("Offline Object 1")
        events_page.click_severity_lvl_picker()
        events_page.choose_severity_level_5()
        events_page.scroll_down_to_save_button()
        events_page.click_save_new_event()
        events_page.check_notification_about_offline_mode()
        events_page.ok_button_on_offline_notification_popup()
        common_page.wait_for_app_loading()

        # While offline, update an event.
        events_page.open_first_pending_event()
        common_page.wait_for_app_loading()
        events_page.click_edit_button()
        events_page.click_severity_lvl_picker()
        events_page.choose_severity_level_5()
        events_page.scroll_down_to_description_field()
        events_page.type_text_into_description_field()
        common_page.hide_keyboard()
        events_page.scroll_down_to_save_button()
        events_page.click_save_new_event()
        events_page.check_notification_about_offline_mode()
        events_page.ok_button_on_offline_notification_popup()

        # # While offline, delete an event.
        # events_page.click_more_button_in_event_details()
        # events_page.click_Delete_button()
        # events_page.alert_confirm_delete()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # While offline, create an asset.
        main_page.open_ASSETS()
        assets_page = LoadClass.load_page('AssetsPage')
        assets_page.setDriver(self.driver)
        assets_page.click_new_button()
        assets_page.click_new_asset()
        assets_page.choose_asset_type()
        assets_page.fill_Name_input_field("Asset test")
        assets_page.scroll_down_to_save_button()
        assets_page.click_save_button()

        # While offline, update an asset.
        # While offline, delete an asset.

        # airplane mode off
        common_page.switch_off_airplane_mode()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOfflineObjects)
    unittest.TextTestRunner(resultclass=AppiumTestResult, verbosity=2).run(suite)
