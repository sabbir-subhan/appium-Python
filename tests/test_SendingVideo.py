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


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest
from time import sleep


class test_SendingVideo(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_send_video(self):

        logging.info("starting Test Case: Sending Video")
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
        main_page = LoadClass.load_page('MainPage')
        main_page.setDriver(self.driver)
        main_page.alert_expiring_password()
        main_page.dismiss_notifications()
        main_page.check_presence_of_events_button()

        main_page.scroll_down_to_video_button()
        main_page.open_VIDEO()
        video_page = LoadClass.load_page('VideoPage')
        video_page.setDriver(self.driver)
        video_page.check_if_video_page_was_opened()
        video_page.click_gallery_button()
        gallery_video_page = LoadClass.load_page('GalleryPage')
        gallery_video_page.setDriver(self.driver)
        common_page.alert_popup_allow()
        gallery_video_page.choose_videos_gallery()
        gallery_video_page.choose_video_from_gallery()
        gallery_video_page.click_use_button()
        video_page.type_description("test - video 1 from gallery")
        common_page.hide_keyboard()
        video_page.click_send_button()  # click and wait for 600s
        main_page.open_VIDEO()
        video_page.click_record_new_button()
        camera_page = LoadClass.load_page('CameraPage')
        camera_page.setDriver(self.driver)
        camera_page.capture_video()
        sleep(1)  # time for recording video
        camera_page.capture_video()
        camera_page.click_use_video()
        video_page.type_description("test - video 1")
        common_page.hide_keyboard()
        video_page.click_send_button()  # click and wait for 600s
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
        video_page.type_description("test- video 2")
        common_page.hide_keyboard()
        video_page.click_send_button()  # click and wait for 600s
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_SendingVideo)
    unittest.TextTestRunner(verbosity=2).run(suite)






