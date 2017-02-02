# Test Case 6 - Risk -- OCAMOB-44

# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present
# From the main menu click on Risks.
# Create a new Risk Register


from desired_capabilities import DesiredCapabilities
from page_android import *


class test_Risk_Android(unittest.TestCase):
    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")

        # choose desired capabilities from desired_capabilities.py
        desired_capabilities = DesiredCapabilities.desired_capabilities_for_android_6

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

        self.driver.implicitly_wait(25)  # seconds

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_manage_risks(self):

        logging.info("starting Test Case 6: Risk")
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
        main_page.open_RISKS()
        risks_page = RisksPage(self.driver)
        risks_page.click_new_risk_register()
        risk_register_edit_page = RiskRegisterEditPage(self.driver)
        risk_register_edit_page.fill_Name_input_field("New Risk Register - test Android")
        android_device.hide_keyboard()
        risk_register_edit_page.scroll_down_one_view()
        risk_register_edit_page.click_save_button()
        risks_page.open_existing_risk_register()
        risks_page.click_new_button()
        risks_page.click_add_new_context()
        context_edit_page = ContextEditPage(self.driver)
        context_edit_page.fill_Name_input_field("New context - test Android")
        android_device.hide_keyboard()
        context_edit_page.scroll_down_one_view()
        context_edit_page.click_save_button()
        context_page = ContextPage(self.driver)
        context_page.open_existing_context()
        context_page.click_new_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_Risk_Android)
    unittest.TextTestRunner(verbosity=2).run(suite)
