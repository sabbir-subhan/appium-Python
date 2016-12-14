# Test Case 2 - Logging in as a suspended account and with a wrong password  -- OCAMOB-76

# before running this Test Case prepare needed accounts on OCA website

# test1: login_into_general_user_with_incorrect_password
# test2: login_into_general_user_with_correct_credentials
# test3: login_into_admin_account_with_correct_credentials
# test4: login_using_account_expired_1_day_ago
# test5: login_using_account_that_expires_today
# test6: login_using_account_that_will_expire_in_1_day
# test7: login_into_suspended_account


from appium import webdriver
from desired_capabilities import DesiredCapabilities
from page_ios import *


class TestCase2iOS(unittest.TestCase):
    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")

        # choose desired capabilities from desired_capabilities.py
        desired_capabilities = DesiredCapabilities.desired_capabilities_for_iOS_iPad

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

        self.driver.implicitly_wait(10)  # seconds

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_1_login_into_general_user_account_with_incorrect_password(self):

        main_page = MainPage(self.driver)
        main_page.dismiss_ios_notifications()
        main_page.logout_if_already_logged_in()
        logging.info("starting test1: login_into_general_user__account_with_incorrect_password")
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.type_username('QA')
        login_page.type_password('random')
        login_page.type_domain_address('QA')
        ios_keyboard = iOSdevice(self.driver)
        ios_keyboard.hide_keyboard()
        login_page.click_submit_button()
        login_page.alert_wrong_password()

    def test_2_login_into_general_user_account(self):

        main_page = MainPage(self.driver)
        main_page.dismiss_ios_notifications()
        main_page.logout_if_already_logged_in()
        logging.info("starting test2: login_into_general_user_account_with_correct_credentials")
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.type_username('general_user')
        login_page.type_password('general_user')
        login_page.type_domain_address('QA')
        ios_keyboard = iOSdevice(self.driver)
        ios_keyboard.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        main_page.alert_expiring_password()
        main_page.dismiss_ios_notifications()
        main_page.check_presence_of_events_button()

    def test_3_login_into_admin_account(self):

        main_page = MainPage(self.driver)
        main_page.dismiss_ios_notifications()
        main_page.logout_if_already_logged_in()
        logging.info("starting test3: login_into_admin_account_with_correct_credentials")
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.type_username('admin')
        login_page.type_password('admin')
        login_page.type_domain_address('QA')
        ios_keyboard = iOSdevice(self.driver)
        ios_keyboard.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        main_page.alert_expiring_password()
        main_page.dismiss_ios_notifications()
        main_page.check_presence_of_events_button()

    def test_4_login_using_account_expired_1_day_ago(self):

        main_page = MainPage(self.driver)
        main_page.dismiss_ios_notifications()
        main_page.logout_if_already_logged_in()
        logging.info("starting test4: login_using_account_expired_1_day_ago")
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.type_username('expired_1_day_ago')
        login_page.type_password('expired_1_day_ago')
        login_page.type_domain_address('QA')
        ios_keyboard = iOSdevice(self.driver)
        ios_keyboard.hide_keyboard()
        login_page.click_submit_button()
        login_page.alert_expired_password()

    def test_5_login_using_account_that_expires_today(self):

        main_page = MainPage(self.driver)
        main_page.dismiss_ios_notifications()
        main_page.logout_if_already_logged_in()
        logging.info("starting test5: login_using_account_that_expires_today")
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.type_username('expire_today')
        login_page.type_password('expire_today')
        login_page.type_domain_address('QA')
        ios_keyboard = iOSdevice(self.driver)
        ios_keyboard.hide_keyboard()
        login_page.click_submit_button()
        login_page.alert_expired_password()

    def test_6_login_using_account_that_will_expire_in_1_day(self):

        main_page = MainPage(self.driver)
        main_page.dismiss_ios_notifications()
        main_page.logout_if_already_logged_in()
        logging.info("starting test6: login_using_account_that_will_expire_in_1_day")
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.type_username('expire_in_1_day')
        login_page.type_password('expire_in_1_day')
        login_page.type_domain_address('QA')
        ios_keyboard = iOSdevice(self.driver)
        ios_keyboard.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        main_page.alert_expiring_password()
        main_page.dismiss_ios_notifications()
        main_page.check_presence_of_events_button()

    def test_7_login_into_suspended_account(self):

        main_page = MainPage(self.driver)
        main_page.dismiss_ios_notifications()
        main_page.logout_if_already_logged_in()
        logging.info("starting test7: login_into_suspended_account")
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.type_username('suspended')
        login_page.type_password('suspended')
        login_page.type_domain_address('QA')
        ios_keyboard = iOSdevice(self.driver)
        ios_keyboard.hide_keyboard()
        login_page.click_submit_button()
        login_page.alert_suspended_account()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase2iOS)
    unittest.TextTestRunner(verbosity=2).run(suite)
