# Test Case - Risks -- OCAMOB-44

# before running this test create:
# - On OCA web page create Risk library with Risk inside it
# - On OCA web page create Control library for risks

# open OCA app
# dismiss iOS notifications
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present

# From the main menu click on Risks.
# Click on Create a new Risk Register > Enter the details >Save
# Click on existing Risk Register > Click on new button > Click on Add new Context
# Click on existing Risk Register > Click on existing context > Click on New button > Click on Add new Risk
# Select a Risk Register > Select a context > New > Select risk library > Select risk from the list
# Select existing Risk Register > Select existing Context > Click on existing Risk > Click On More >
# Click Add new control > Fill in Details and Save
# Select existing Risk Register > Select existing Context > Click on existing Risk > Click on more button > Delete this risk
# Select existing Risk Register > Select existing Context > Click on existing Risk > Click on more > Add Library Control
# Select existing Risk Register > Select existing Context > Click on existing Risk > Click on more > Mark as Reviewed
# Select existing Risk register > Click View button > View Register


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest
import os


class TestRisk(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        path = "./screenshots"
        os.chdir(path)
        self.driver.save_screenshot("test_Risk" + ".png")
        os.chdir("..")

        self.driver.quit()

    def test_Risk(self):

        logging.info("starting Test Case: Risk")
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
        common_page.wait_for_app_loading()
        main_page = LoadClass.load_page('MainPage')
        main_page.setDriver(self.driver)
        main_page.alert_expiring_password()
        main_page.dismiss_notifications()
        main_page.check_presence_of_events_button()

        main_page.open_RISKS()
        risks_page = LoadClass.load_page('RisksPage')
        risks_page.setDriver(self.driver)
        risks_page.create_risk_register()
        risks_page.type_name_for_new_risk_register()
        risks_page.create_new_context()
        risks_page.scroll_down_to_save_button()
        risks_page.click_save_button()
        common_page.wait_for_app_loading()

        risks_page.open_existing_risk_register()
        risks_page.click_new_button()
        risks_page.click_add_new_context()
        risks_page.type_name_for_new_context()
        common_page.hide_keyboard()
        risks_page.scroll_down_to_save_button()
        risks_page.save_new_context()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Click on existing Risk Register > Click on existing context > Click on Add new Risk
        main_page.open_RISKS()
        risks_page.open_existing_risk_register()
        risks_page.open_existing_context()
        risks_page.click_new_button()
        risks_page.click_add_new_risk()
        risks_page.type_name_for_new_risk()
        common_page.hide_keyboard()
        risks_page.scroll_down_to_save_button()
        risks_page.save_new_risk()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Select a Risk Register > Select a context > New > Select risk library > Select risk from the list
        main_page.open_RISKS()
        risks_page.open_existing_risk_register()
        risks_page.open_existing_context()
        risks_page.click_new_button()
        risks_page.click_add_library_risk()
        risks_page.select_risk_library()
        risks_page.select_risk_inside_library()
        risks_page.click_ok_button()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Select existing Risk Register > Select existing Context > Click on existing Risk > Click On More >
        # Click Add new control > Fill in Details and Save
        main_page.open_RISKS()
        risks_page.open_existing_risk_register()
        risks_page.open_existing_context()
        risks_page.open_existing_risk()
        risks_page.click_more_button()
        risks_page.click_add_new_control()
        risks_page.type_name_for_new_control()
        risks_page.click_status_selector()
        risks_page.choose_status_implemented()
        risks_page.click_save_new_control()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Select existing Risk Register > Select existing Context > Click on existing Risk > Click on more button > Delete this risk
        main_page.open_RISKS()
        risks_page.open_existing_risk_register()
        risks_page.open_existing_context()
        risks_page.open_existing_risk()
        risks_page.click_more_button()
        risks_page.click_delete_risk()
        risks_page.alert_accept_delete()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Select existing Risk Register > Select existing Context > Click on existing Risk > Click on more > Add Library Control
        main_page.open_RISKS()
        risks_page.open_existing_risk_register()
        risks_page.open_existing_context()
        risks_page.open_existing_risk()
        risks_page.click_more_button()
        risks_page.click_add_library_control()
        risks_page.select_library_control_from_the_list()
        risks_page.click_ok_button_in_risk_control_library()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Select existing Risk Register > Select existing Context > Click on existing Risk > Click on more > Mark as Reviewed
        main_page.open_RISKS()
        risks_page.open_existing_risk_register()
        risks_page.open_existing_context()
        risks_page.open_existing_risk()
        risks_page.click_more_button()
        risks_page.click_mark_as_reviewed()
        risks_page.alert_accept_review()
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()

        # Select existing Risk register > Click View button > View Register
        main_page.open_RISKS()
        risks_page.open_existing_risk_register()
        risks_page.click_view_button()
        risks_page.click_view_register()
        risks_page.check_if_register_view_was_opened()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRisk)
    unittest.TextTestRunner(verbosity=2).run(suite)
