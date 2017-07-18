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
# After load,  user should see a badge on the offline sync icon with the counter
# Click on offline sync icon
# View the Incoming queue screen
# View Outgoing queue
# Create event offline > Add media > Add video, Audio, Images to the event in offline sync > Save the event
# Turn off airplane mode
# Check the events created offline once you are online -- Verify that the media files are saved


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest
from time import sleep


class TestLoadTypeDataAfterLogin(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_Load_Type_Data_After_Login(self):

        logging.info("starting Test Case: Load Type Data After Login")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        welcome_page = LoadClass.load_page('WelcomePage')
        welcome_page.setDriver(self.driver)

        # common_page.swipe_down_to_show_notifications()  # for test
        # common_page.swipe_down_to_show_notifications()  # for test
        # common_page.turn_on_flight_mode()  # for test
        # common_page.swipe_up_to_hide_notifications()  # for test

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

        main_page.scroll_down_to_offline_sync_button()
        main_page.open_OFFLINE_SYNC()
        common_page.take_screenshot('Offline_sync_in_online_mode')
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        common_page.swipe_up_to_show_control_center()
        common_page.switch_airplane_mode()  # method for iOS
        common_page.turn_on_flight_mode()  # method for Android
        common_page.swipe_down_to_hide_control_center()

        main_page.scroll_up_to_events_button()
        main_page.open_EVENTS()
        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.click_more_button_in_events_list()
        events_page.click_New_event_button()
        events_page.choose_Incident_type_of_event()
        events_page.fill_Name_input_field("Event in offline mode")
        events_page.click_severity_lvl_picker()
        events_page.choose_severity_level_1()
        events_page.scroll_down_to_save_button()

        events_page.click_add_media()
        select_media_page = LoadClass.load_page('SelectMediaPage')
        select_media_page.setDriver(self.driver)
        common_page.push_sample_image_file()
        select_media_page.click_photo_gallery()
        common_page.alert_popup_allow()
        gallery_page = LoadClass.load_page('GalleryPage')
        gallery_page.setDriver(self.driver)
        gallery_page.choose_element_1()
        common_page.alert_popup_allow()
        events_page.scroll_down_to_save_button()

        events_page.click_add_media()
        common_page.push_sample_video_file()
        select_media_page.click_video_gallery()
        common_page.alert_popup_allow()
        gallery_page.choose_video_from_gallery()
        common_page.alert_popup_allow()
        events_page.scroll_down_to_save_button()

        events_page.click_add_media()
        select_media_page.click_record_audio()
        common_page.alert_popup_allow()
        sound_recorder = LoadClass.load_page('SoundRecorderPage')
        sound_recorder.setDriver(self.driver)
        sound_recorder.record_sound()
        sleep(1)  # time for recording sound
        sound_recorder.stop_recording()
        sound_recorder.click_done_button()
        events_page.click_back_arrow_if_running_on_emulators()

        events_page.scroll_down_to_save_button()
        events_page.click_save_new_event()
        events_page.check_notification_about_offline_mode()
        events_page.ok_button_on_offline_notification_popup()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        main_page.scroll_down_to_offline_sync_button()
        main_page.open_OFFLINE_SYNC()
        common_page.take_screenshot('Offline_sync_in_offline_mode')
        common_page.hamburger_button()
        main_page.check_presence_of_inbox_button()

        common_page.swipe_up_to_show_control_center()
        common_page.switch_airplane_mode()  # method for iOS
        common_page.turn_on_all_network()  # method for Android
        common_page.swipe_down_to_hide_control_center()

        main_page.scroll_up_to_events_button()
        main_page.open_EVENTS()
        events_page.clear_Search_field()
        events_page.type_text_into_search_field("offline mode")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLoadTypeDataAfterLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)
