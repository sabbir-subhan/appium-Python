# Test Case - Send Audio to OCA -- OCAMOB-51

# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present
# From the main menu, click Sound
# Press the microphone icon.
# Press the red recording button to start recording sound. Press it again to stop. Press done to finish.
# Enter a description and press send.


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest
from time import sleep


class TestSendAudio(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_send_sound(self):

        logging.info("starting Test Case: Send Audio to OCA")
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
        common_page.wait_for_app_loading()
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

        main_page.scroll_down_to_sound_button()
        main_page.open_SOUND()
        sound_page = LoadClass.load_page('SoundPage')
        sound_page.setDriver(self.driver)
        sound_page.check_if_sound_page_was_opened()
        sound_page.click_record_sound_icon()
        sound_recorder = LoadClass.load_page('SoundRecorderPage')
        sound_recorder.setDriver(self.driver)
        common_page.alert_popup_allow()
        sound_recorder.record_sound()
        sleep(2)  # time for recording sound
        sound_recorder.stop_recording()
        sound_recorder.click_done_button()
        common_page.alert_popup_allow()
        sound_page.type_description("test - sound")
        # common_page.hide_keyboard()
        sound_page.click_send_button()  # click and wait for 600s
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSendAudio)
    unittest.TextTestRunner(verbosity=2).run(suite)
