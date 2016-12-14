# Test Case 1 - Log Into OCA mobile via direct Login -- OCAMOB-38
# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present


from appium import webdriver
from desired_capabilities import DesiredCapabilities
from page_ios import *


class TestCase1iOS(unittest.TestCase):
    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")

        # choose desired capabilities from desired_capabilities.py
        desired_capabilities = DesiredCapabilities.desired_capabilities_for_iOS_iPad

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

        self.driver.implicitly_wait(10)  # seconds

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
        ios_keyboard = iOSdevice(self.driver)
        ios_keyboard.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        main_page.alert_expiring_password()
        main_page.dismiss_ios_notifications()
        main_page.check_presence_of_events_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase1iOS)
    unittest.TextTestRunner(verbosity=2).run(suite)
