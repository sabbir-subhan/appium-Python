# Before running test - enable allow access to Camera and Photos in iOS settings for OCA app

# Test Case 5 - Send Photo -- OCAMOB-43

# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present
# From the main menu click on Photo.
# Click Gallery and select an existing photo.
# Enter a description and click Send.
# Click on Photo and now click Take New. (step 4)
# Click the change camera button on the bottom right  twice.
# Click on the button below Photo to take a picture.
# Click on Use Photo.
# Enter a description and press Send.
# Repeat steps 4 & 6.
# Press Retake and take another photo.
# Repeat steps 7 & 8.

from appium import webdriver
from desired_capabilities import DesiredCapabilities
from page_ios import *


class TestCase1iOS(unittest.TestCase):
    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")

        # choose desired capabilities from desired_capabilities.py
        desired_capabilities = DesiredCapabilities.desired_capabilities_for_iOS_iPad

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

        self.driver.implicitly_wait(15)  # seconds

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_login(self):

        main_page = MainPage(self.driver)
        main_page.dismiss_ios_notifications()
        main_page.logout_if_already_logged_in()
        logging.info("starting Test Case 1: login into active account")
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
        main_page.open_PHOTO()
        photo_page = PhotoPage(self.driver)
        photo_page.check_if_photo_page_was_opened()
        photo_page.click_gallery_button()
        # cos
        photo_page.click_take_new_button()
        camera_page = CameraPage(self.driver)
        camera_page.choose_camera()
        camera_page.choose_camera()
        camera_page.take_a_photo()
        camera_page.click_use_photo()
        #photo_page.
        #step9


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase1iOS)
    unittest.TextTestRunner(verbosity=2).run(suite)