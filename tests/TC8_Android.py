# Test Case 8 - Send Audio to OCA -- OCAMOB-51


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


from appium import webdriver
from desired_capabilities import DesiredCapabilities
from page_android import *


class TestCase8Android(unittest.TestCase):
    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")

        # choose desired capabilities from desired_capabilities.py
        desired_capabilities = DesiredCapabilities.desired_capabilities_for_android_6

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

        self.driver.implicitly_wait(20)  # seconds

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_send_sound(self):

        logging.info("starting Test Case 8: Send Audio to OCA")
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.type_username('QA')
        login_page.type_password('QA')
        login_page.type_domain_address('QA')
        android_device = AndroidDevice(self.driver)
        android_device.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        main_page = MainPage(self.driver)
        main_page.alert_expiring_password()
        main_page.dismiss_android_notifications()
        main_page.check_presence_of_events_button()
        main_page.open_SOUND()
        sound_page = SoundPage(self.driver)
        sound_page.check_if_sound_page_was_opened()
        sound_page.click_record_sound_icon()
        sound_recorder = SoundRecorder(self.driver)
        sound_recorder.record_sound()
        sleep(0.2)  # time for recording sound
        sound_recorder.stop_recording()
        sound_recorder.click_done_button()
        android_device.alert_android_allow()
        sound_page.type_description("test Android - sound")
        android_device.hide_keyboard()
        sound_page.click_send_button()
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase8Android)
    unittest.TextTestRunner(verbosity=2).run(suite)
