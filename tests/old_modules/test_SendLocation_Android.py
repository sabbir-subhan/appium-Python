# Test Case 4 - Send location to OCA -- OCAMOB-41

# before running this test, enable location on device

# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# Click on location and touch send once now
# Setup sending location every 5 minutes for an hour


from desired_capabilities import DesiredCapabilities
from page_android import *


class test_SendLocation_Android(unittest.TestCase):
    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")

        # choose desired capabilities from desired_capabilities.py
        desired_capabilities = DesiredCapabilities.desired_capabilities_for_android_4

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

        self.driver.implicitly_wait(15)  # seconds

    def tearDown(self):

        logging.info("Quitting")

        self.driver.quit()

    def test_send_location(self):

        logging.info("starting Test Case 4: send location")
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
        main_page.open_LOCATION()
        location_page = LocationPage(self.driver)
        location_page.check_if_location_page_was_opened()
        location_page.click_send_once_now()
        location_page.check_if_location_was_sent()
        location_page.click_send_every()
        location_page.choose_send_every_5_minutes_option()
        location_page.check_if_5_minutes_option_was_chosen()
        location_page.click_for_the_next()
        location_page.choose_1_hour_option()
        location_page.check_if_1_hour_option_was_chosen()
        location_page.click_start_button()
        location_page.check_if_start_button_was_clicked()
        location_page.check_if_location_was_sent()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_SendLocation_Android)
    unittest.TextTestRunner(verbosity=2).run(suite)
