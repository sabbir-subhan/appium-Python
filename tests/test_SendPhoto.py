# Test Case - Send Photo -- OCAMOB-43

# before run test - prepare sample photo file on device

# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present

# Click on Photo and now click Take New.
# Click the change camera button twice.
# Click on the button below Photo to take a picture.
# Click on Use Photo.
# Enter a description and press Send.

# From the main menu click on Photo.
# Click Gallery and select an existing photo.
# Enter a description and click Send.

# Click on Photo and now click Take New.
# Click the change camera button twice.
# Click on the button below Photo to take a picture.
# Press Retake and take another photo.
# Click on Use Photo.
# Enter a description and press Send.


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest
import os
from configuration import PROJECT_ROOT


class TestSendPhoto(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        path = PROJECT_ROOT + "/screenshots"
        os.chdir(path)
        self.driver.save_screenshot("test_SendPhoto" + ".png")
        os.chdir("..")

        self.driver.quit()

    def test_SendPhoto(self):

        logging.info("starting Test Case: send photo")
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
        main_page.scroll_down_to_photo_button()

        main_page.open_PHOTO()
        photo_page = LoadClass.load_page('PhotoPage')
        photo_page.setDriver(self.driver)
        photo_page.click_take_new_button()
        common_page.alert_popup_allow()
        camera_page = LoadClass.load_page('CameraPage')
        camera_page.setDriver(self.driver)
        camera_page.choose_photo_camera()
        camera_page.choose_photo_camera()
        camera_page.capture_photo()
        camera_page.click_use_photo()
        common_page.alert_popup_allow()
        photo_page.type_description("test - take a photo 1")
        photo_page.click_send_button_camera()  # click and wait for 720s
        photo_page.click_back_arrow_if_running_on_emulator()
        main_page.check_presence_of_inbox_button()
        main_page.scroll_down_to_photo_button()

        main_page.open_PHOTO()
        photo_page.check_if_photo_page_was_opened()
        common_page.push_sample_image_file()  # push sample image file for emulators
        photo_page.click_gallery_button()
        common_page.alert_popup_allow()
        gallery_page = LoadClass.load_page('GalleryPage')
        gallery_page.setDriver(self.driver)
        gallery_page.choose_element_from_gallery()
        common_page.alert_popup_allow()
        photo_page.type_description("test - photo 1 from gallery")
        photo_page.click_send_button_gallery()  # click and wait for 720s
        main_page.check_presence_of_inbox_button()
        main_page.scroll_down_to_photo_button()

        main_page.open_PHOTO()
        photo_page.click_take_new_button()
        camera_page.choose_photo_camera()
        camera_page.choose_photo_camera()
        camera_page.capture_photo()
        camera_page.click_retake_photo()
        camera_page.capture_photo()
        camera_page.click_use_photo()
        photo_page.type_description("test - take a photo 2")
        photo_page.click_send_button_camera()  # click and wait for 720s
        photo_page.click_back_arrow_if_running_on_emulator()
        main_page.check_presence_of_inbox_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSendPhoto)
    unittest.TextTestRunner(verbosity=2).run(suite)
