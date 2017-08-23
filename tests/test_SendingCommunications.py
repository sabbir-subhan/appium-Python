# Test Case - Sending Communications  -- OCAMOB-57

# open OCA app
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss iOS notifications
# check if button "EVENTS" is present

# From the main menu press the Compose button.
# Press the + next to the recipients and add some recipient contacts and/or groups.
# Compose an email and press Send. View the outgoing queue.

# From the main menu press the Compose button.
# Press the + next to the recipients and add some recipient contacts and/or groups.
# Compose an SMS, text to voice and fax.

# Go back to the main menu and press Sent. Verify the messages you sent appear here.
# Compose a message, but this time add resource structure nodes as recipients.
# Compose a message but instead of sending it, press Save and give it a name.

# Go to Compose > Drafts and select the draft named in step 7.
# Turn on flight mode and compose a communication. View the outbox.
# Disable flight mode and turn on internet. View the outbox.
# Compose a communication without recipients and attempt to send.
# Add recipients to an empty communication and attempt to send.
# Compose a communication and add attach a photo.
# Compose a communication and attach a video.
# Compose a communication and attach audio.
# Send SMS ,Email,Push ,Voice message from a high user to a lowuser
# Repeat step for different level users
# Repeat Step 16 from high user to an other high user


from Modules.Setup import SetupTestCase
from Modules.load_class import LoadClass
import logging
import unittest
from configuration import PROJECT_ROOT


class TestSendingCommunications(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        logging.info("Quitting")

        # take screenshot on quit
        self.driver.save_screenshot(PROJECT_ROOT + "/screenshots/test_SendingCommunications.png")

        self.driver.quit()

    def test_SentCommunications(self):

        logging.info("starting Test Case: Sending Communications")
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

        main_page.open_COMPOSE()
        compose_page = LoadClass.load_page('ComposePage')
        compose_page.setDriver(self.driver)
        compose_page.add_recipients()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSendingCommunications)
    unittest.TextTestRunner(verbosity=2).run(suite)
