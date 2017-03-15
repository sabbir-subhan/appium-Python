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


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest


class test_ViewInboxSentCommunications(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_login(self):

        logging.info("starting Test Case: View Inbox & Sent Communications")
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

        main_page.scroll_down_one_view()
        main_page.open_SENT()
        sent_page = LoadClass.load_page('SentPage')
        sent_page.setDriver(self.driver)
        #sent_page.take_screenshot("screenshot.png")  # screenshot will be saved in /tests directory
        sent_page.hamburger_button()
        main_page.scroll_down_one_view()
        main_page.open_COMPOSE()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_ViewInboxSentCommunications)
    unittest.TextTestRunner(verbosity=2).run(suite)
