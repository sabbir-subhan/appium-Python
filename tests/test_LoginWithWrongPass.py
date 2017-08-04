# Test Case - Logging in as a suspended account and with a wrong password  -- OCAMOB-76

# before running this Test Case prepare needed accounts on OCA website

# test1: login_into_general_user_with_incorrect_password
# test2: login_into_general_user_with_correct_credentials
# test3: login_into_admin_account_with_correct_credentials
# test4: login_using_account_expired_1_day_ago
# test5: login_using_account_that_expires_today
# test6: login_using_account_that_will_expire_in_1_day
# test7: login_into_suspended_account


import unittest
import logging
from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import os
from configuration import PROJECT_ROOT


class TestLoginWithWrongPass(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        path = PROJECT_ROOT + "/screenshots"
        os.chdir(path)
        self.driver.save_screenshot("test_LoginWithWrongPass" + ".png")
        os.chdir("..")

        self.driver.quit()

    def test_1_login_into_general_user_account_with_incorrect_password(self):

        logging.info("starting test 1: login into general user account with incorrect password")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        welcome_page = LoadClass.load_page('WelcomePage')
        welcome_page.setDriver(self.driver)
        welcome_page.click_login_button()
        login_page = LoadClass.load_page('LoginPage')
        login_page.setDriver(self.driver)
        login_page.type_domain_address('QA')
        login_page.click_submit_button()
        login_page.type_username('QA')
        login_page.type_password('random')
        common_page.hide_keyboard()
        login_page.click_submit_button()
        login_page.alert_wrong_password()

    def test_2_login_into_general_user_account(self):

        logging.info("starting test 2: login into general user account with correct credentials")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        welcome_page = LoadClass.load_page('WelcomePage')
        welcome_page.setDriver(self.driver)
        welcome_page.click_login_button()
        login_page = LoadClass.load_page('LoginPage')
        login_page.setDriver(self.driver)
        login_page.type_domain_address('QA')
        login_page.click_submit_button()
        login_page.type_username('general_user')
        login_page.type_password('general_user')
        common_page.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        common_page.wait_for_app_loading()
        main_page = LoadClass.load_page('MainPage')
        main_page.setDriver(self.driver)
        main_page.alert_expiring_password()
        main_page.dismiss_notifications()
        main_page.check_presence_of_events_button()

    def test_3_login_into_admin_account(self):

        logging.info("starting test 3: login into admin account with correct credentials")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        welcome_page = LoadClass.load_page('WelcomePage')
        welcome_page.setDriver(self.driver)
        welcome_page.click_login_button()
        login_page = LoadClass.load_page('LoginPage')
        login_page.setDriver(self.driver)
        login_page.type_domain_address('QA')
        login_page.click_submit_button()
        login_page.type_username('admin')
        login_page.type_password('admin')
        common_page.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        common_page.wait_for_app_loading()
        main_page = LoadClass.load_page('MainPage')
        main_page.setDriver(self.driver)
        main_page.alert_expiring_password()
        main_page.dismiss_notifications()
        main_page.check_presence_of_events_button()

    def test_4_login_using_account_expired_1_day_ago(self):

        logging.info("starting test 4: login using account expired 1 day ago")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        welcome_page = LoadClass.load_page('WelcomePage')
        welcome_page.setDriver(self.driver)
        welcome_page.click_login_button()
        login_page = LoadClass.load_page('LoginPage')
        login_page.setDriver(self.driver)
        login_page.type_domain_address('QA')
        login_page.click_submit_button()
        login_page.type_username('expired_1_day_ago')
        login_page.type_password('expired_1_day_ago')
        common_page.hide_keyboard()
        login_page.click_submit_button()
        login_page.alert_expired_password()

    def test_5_login_using_account_that_expires_today(self):

        logging.info("starting test 5: login using account that expires today")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        welcome_page = LoadClass.load_page('WelcomePage')
        welcome_page.setDriver(self.driver)
        welcome_page.click_login_button()
        login_page = LoadClass.load_page('LoginPage')
        login_page.setDriver(self.driver)
        login_page.type_domain_address('QA')
        login_page.click_submit_button()
        login_page.type_username('expire_today')
        login_page.type_password('expire_today')
        common_page.hide_keyboard()
        login_page.click_submit_button()
        login_page.alert_expired_password()

    def test_6_login_using_account_that_will_expire_in_1_day(self):

        logging.info("starting test 6: login using account that will expire in 1 day")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        welcome_page = LoadClass.load_page('WelcomePage')
        welcome_page.setDriver(self.driver)
        welcome_page.click_login_button()
        login_page = LoadClass.load_page('LoginPage')
        login_page.setDriver(self.driver)
        login_page.type_domain_address('QA')
        login_page.click_submit_button()
        login_page.type_username('expire_in_1_day')
        login_page.type_password('expire_in_1_day')
        common_page.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        common_page.wait_for_app_loading()
        main_page = LoadClass.load_page('MainPage')
        main_page.setDriver(self.driver)
        main_page.alert_expiring_password()
        main_page.dismiss_notifications()
        main_page.check_presence_of_events_button()

    def test_7_login_into_suspended_account(self):

        logging.info("starting test 7: login into suspended account")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        welcome_page = LoadClass.load_page('WelcomePage')
        welcome_page.setDriver(self.driver)
        welcome_page.click_login_button()
        login_page = LoadClass.load_page('LoginPage')
        login_page.setDriver(self.driver)
        login_page.type_domain_address('QA')
        login_page.click_submit_button()
        login_page.type_username('suspended')
        login_page.type_password('suspended')
        common_page.hide_keyboard()
        login_page.click_submit_button()
        login_page.alert_suspended_account()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLoginWithWrongPass)
    unittest.TextTestRunner(verbosity=2).run(suite)
