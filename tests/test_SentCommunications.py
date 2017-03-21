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


class test_SentCommunications(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")
        self.driver.quit()

    def test_sent_communications(self):

        current = self.driver.current_context
        logging.info('current context is: ' + current)
        contexts = self.driver.contexts
        logging.info(contexts)
        self.driver.switch_to.context(contexts[1])
        current_after_switch = self.driver.current_context
        logging.info('current context is: ' + current_after_switch)

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

        main_page.scroll_down_to_sent_button()
        main_page.open_SENT()
        sent_page = LoadClass.load_page('SentPage')
        sent_page.setDriver(self.driver)
        sent_page.check_sent_communications()
        common_page.hamburger_button()
        main_page.open_COMPOSE()
        compose_page = LoadClass.load_page('ComposePage')
        compose_page.setDriver(self.driver)
        compose_page.add_recipients()
        compose_page.add_contacts_and_groups()
        compose_page.contacts_arrow()
        compose_page.choose_contact_for_test()
        compose_page.click_ok_button()
        compose_page.choose_sms_message()
        compose_page.type_sms_message()
        common_page.hide_keyboard()
        compose_page.click_ok_button()
        compose_page.choose_email_message()
        compose_page.type_email_subject()
        common_page.hide_keyboard()
        compose_page.type_email_message()
        common_page.hide_keyboard()
        compose_page.click_ok_button()
        compose_page.choose_voice_message()
        compose_page.click_text_to_speech()
        compose_page.type_voice_message()
        common_page.hide_keyboard()
        compose_page.click_ok_button()
        compose_page.choose_fax_message()
        compose_page.choose_fax_document()
        compose_page.choose_comms_documents()
        compose_page.choose_file()
        compose_page.click_fax_ok_button()
        compose_page.click_send_button()
        compose_page.alert_send_button()
        common_page.hamburger_button()
        main_page.scroll_down_to_sent_button()
        main_page.open_SENT()
        common_page.hamburger_button()
        main_page.open_INBOX()
        inbox_page = LoadClass.load_page('InboxPage')
        inbox_page.setDriver(self.driver)
        common_page.hamburger_button()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_SentCommunications)
    unittest.TextTestRunner(verbosity=2).run(suite)
