# Test Case 6 - Risks -- OCAMOB-44

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
# Click on existing Risk Register > Click on existing context > Click on New button > Click on Add new library Risk > ?

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


class TestRisk(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_manage_risks(self):

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
        common_page.hide_keyboard()
        risks_page.create_new_context()
        risks_page.scroll_down_to_save_button()
        risks_page.click_save_button()

        risks_page.open_existing_risk_register()
        risks_page.click_new_button()
        risks_page.click_add_new_context()
        risks_page.type_name_for_new_context()
        common_page.hide_keyboard()
        risks_page.scroll_down_to_save_button()
        risks_page.save_new_context()

        # Click on existing Risk Register > Click on existing context > Click on Add new Risk
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()
        main_page.open_RISKS()
        risks_page.open_existing_risk_register()
        risks_page.open_existing_context()
        risks_page.click_new_button()
        risks_page.click_add_new_risk()
        risks_page.type_name_for_new_risk()
        common_page.hide_keyboard()
        risks_page.scroll_down_to_save_button()
        risks_page.save_new_risk()

        # Click on existing Risk Register > Click on existing context > Click on New button > Click on Add new library Risk > ?
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()
        main_page.open_RISKS()
        risks_page.open_existing_risk_register()
        risks_page.open_existing_context()
        risks_page.click_new_button()
        risks_page.click_add_library_risk()
        risks_page.click_ok_button()  # ?? or some other step ?

        # Select existing Risk Register > Select existing Context > Click on existing Risk > Click On More >
        # Click Add new control > Fill in Details and Save
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()
        main_page.open_RISKS()
        risks_page.open_existing_risk_register()
        risks_page.open_existing_context()
        risks_page.open_existing_risk()
        risks_page.click_more_button()  # add method
        risks_page.click_add_new_control()  # add method
        risks_page.type_name_for_new_control()  # add method
        common_page.hide_keyboard()
        risks_page.clic_status_selector()  # add method
        risks_page.choose_status()  # add method
        risks_page.click_save_new_control()  # add method

        # Select existing Risk Register > Select existing Context > Click on existing Risk > Click on more button > Delete this risk
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()
        main_page.open_RISKS()
        risks_page.open_existing_risk_register()
        risks_page.open_existing_context()
        risks_page.open_existing_risk()
        risks_page.click_more_button()
        risks_page.click_delete_button()  # add method

        # Select existing Risk Register > Select existing Context > Click on existing Risk > Click on more > Add Library Control
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()
        main_page.open_RISKS()
        risks_page.open_existing_risk_register()
        risks_page.open_existing_context()
        risks_page.open_existing_risk()
        risks_page.click_more_button()
        risks_page.click_add_library_control()  # add method

        # Select existing Risk Register > Select existing Context > Click on existing Risk > Click on more > Mark as Reviewed
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()
        main_page.open_RISKS()
        risks_page.open_existing_risk_register()
        risks_page.open_existing_context()
        risks_page.open_existing_risk()
        risks_page.click_more_button()
        risks_page.click_mark_as_reviewed()  # add method

        # Select existing Risk register > Click View button > View Register
        common_page.hamburger_button()
        main_page.check_presence_of_events_button()
        main_page.open_RISKS()
        risks_page.open_existing_risk_register()
        risks_page.click_view_button()  # add method
        risks_page.click_view_register()  # add method


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRisk)
    unittest.TextTestRunner(verbosity=2).run(suite)
