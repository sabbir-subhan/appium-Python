# Test Case 11 - View Inbox & Sent Communications  -- OCAMOB-49

# open OCA app
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present
# From the main menu, press the Sent button.
# Verify that communications listed show: Sender, date & time sent and method (e.g. email, SMS).
# Return to the main menu and press Compose.
# Send one of each type of communication to some recipient/s.
# Return to the main menu and press the Sent button. View the most recent communications sent.
# From the main menu press the Inbox button.


from desired_capabilities import DesiredCapabilities
from page_android import *


class test_ViewInboxSentCommunications_Android(unittest.TestCase):
    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")

        # choose desired capabilities from desired_capabilities.py
        desired_capabilities = DesiredCapabilities.desired_capabilities_for_android_6

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

        self.driver.implicitly_wait(25)  # seconds

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_login(self):

        logging.info("starting Test Case 11: View Inbox & Sent Communications")
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
        main_page.scroll_down_one_view()
        main_page.open_SENT()
        sent_page = SentPage(self.driver)
        sent_page.take_screenshot("screenshot.png")  # screenshot will be saved in /tests directory
        sent_page.hamburger_button()
        main_page.scroll_down_one_view()
        main_page.open_COMPOSE()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_ViewInboxSentCommunications_Android)
    unittest.TextTestRunner(verbosity=2).run(suite)
