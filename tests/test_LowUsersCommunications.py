# Test Case - Low level user should be able to send communication to a low level user  -- OCAMOB-419


# before running test case:

# Create two low level users: "A_CONTACT_FOR_APPIUM_TESTS" and "test_general" or change names of the contacts in this script
# Create high user: test_admin or change name of the contact in this script
# Login to OCA server -> Click on Settings > Settings>Security > Under Access levels set the write access level to administrators only(high access)


# Login to the OCA app with low user
# open OCA app
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present

# Click on inbox and select a email > Click on Forward > Select an other low user created above > Send
# Forward an other email to a high access user
# Send Sms/Voice from low level user to an other low level user


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest
from configuration import PROJECT_ROOT


class TestLowUsersCommunications(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        self.driver.save_screenshot(PROJECT_ROOT + "/screenshots/test_LowUsersCommunications.png")

        self.driver.quit()

    def test_LowUsersCommunications(self):

        logging.info("starting Test Case: Low Users Communications")
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

        main_page.open_COMPOSE()
        compose_page = LoadClass.load_page('ComposePage')
        compose_page.setDriver(self.driver)
        compose_page.add_recipients()
        compose_page.add_contacts_and_groups()
        compose_page.clear_Search_field()
        compose_page.type_text_into_search_field("A_CONTACT_FOR_APPIUM_TESTS")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        compose_page.click_first_contact_on_the_list_with_checkbox()
        compose_page.click_ok_button()
        compose_page.choose_email_message()
        compose_page.type_email_subject()
        compose_page.type_email_message()
        common_page.hide_keyboard()
        compose_page.click_email_ok_button()
        compose_page.click_send_button()
        compose_page.alert_send_button()
        common_page.wait_for_app_loading()
        common_page.hamburger_button()

        # Click on inbox and select a email > Click on Forward > Select an other low user created above > Send
        main_page.open_INBOX()
        inbox_page = LoadClass.load_page('InboxPage')
        inbox_page.setDriver(self.driver)
        inbox_page.open_first_msg_on_the_list()
        

        # Forward an other email to a high access user

        # Send Sms/Voice from low level user to an other low level user


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLowUsersCommunications)
    unittest.TextTestRunner(verbosity=2).run(suite)
