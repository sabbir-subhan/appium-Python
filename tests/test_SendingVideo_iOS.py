# Test Case 7 - Sending Video -- OCAMOB-45

# before run test - prepare sample video file on device

# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present
# From the main menu, click Video.
# Click Gallery, and select a video that has already been recorded.
# Enter a description and press the Send button.
# Click Video and now select Record New. (step 4)
# Press the button under video to start recording a video. Press the button again to stop recording.
# Press Use Video to select the video.
# Enter a description and press the Send button.
# Repeat steps 4 & 5.
# Press retake, and record a new video.
# Repeat steps 6 & 7.

from appium import webdriver
from desired_capabilities import DesiredCapabilities
from page_ios import *


class test_SendingVideo_iOS(unittest.TestCase):
    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")

        # choose desired capabilities from desired_capabilities.py
        desired_capabilities = DesiredCapabilities.desired_capabilities_for_iOS_iPad

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

        self.driver.implicitly_wait(15)  # seconds

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_send_video(self):

        main_page = MainPage(self.driver)
        main_page.dismiss_ios_notifications()
        main_page.logout_if_already_logged_in()
        logging.info("starting Test Case 7: Sending Video")
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.type_username('QA')
        login_page.type_password('QA')
        login_page.type_domain_address('QA')
        ios_device = iOSdevice(self.driver)
        ios_device.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        main_page.alert_expiring_password()
        main_page.dismiss_ios_notifications()
        main_page.check_presence_of_events_button()
        main_page.open_VIDEO()
        video_page = VideoPage(self.driver)
        video_page.check_if_video_page_was_opened()
        video_page.click_gallery_button()
        gallery_video_page = GalleryPage(self.driver)
        gallery_video_page.choose_videos_gallery()
        gallery_video_page.choose_element_1()
        gallery_video_page.click_use_video_button()
        video_page.type_description("test iOS - video 1 from gallery")
        ios_device.hide_keyboard()
        video_page.click_send_button()
        main_page.open_VIDEO()
        video_page.click_record_new_button()
        camera_page = CameraPage(self.driver)
        camera_page.capture_video()
        sleep(1)  # time for recording video
        camera_page.capture_video()
        camera_page.click_use_video()
        video_page.type_description("test iOS - video 1")
        ios_device.hide_keyboard()
        video_page.click_send_button()
        main_page.open_VIDEO()
        video_page.click_record_new_button()
        camera_page.capture_video()
        sleep(1)  # time for recording video
        camera_page.capture_video()
        camera_page.click_retake()
        camera_page.capture_video()
        sleep(1)  # time for recording video
        camera_page.capture_video()
        camera_page.click_use_video()
        video_page.type_description("test iOS - video 2")
        video_page.click_send_button()
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_SendingVideo_iOS)
    unittest.TextTestRunner(verbosity=2).run(suite)
