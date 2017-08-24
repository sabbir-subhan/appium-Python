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

# Go to Compose > Drafts and select the draft named from previous step - The message you saved is loaded
# Turn on flight mode and compose a communication. View the outbox.
# Disable flight mode and turn on internet. View the outbox.
# Compose a communication without recipients and attempt to send.
# Add recipients to an empty communication and attempt to send.
# Compose a communication and add attach a photo.
# Compose a communication and attach a video.
# Compose a communication and attach audio.
# Send SMS ,Email,Push ,Voice message from a high user to a lowuser
# Repeat step for different level users
# Send SMS ,Email, Push, Voice message from high user to an other high user


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

        # From the main menu press the Compose button.
        main_page.open_COMPOSE()
        compose_page = LoadClass.load_page('ComposePage')
        compose_page.setDriver(self.driver)
        compose_page.add_recipients()
        compose_page.add_contacts_and_groups()

        # Press the + next to the recipients and add some recipient contacts and/or groups.
        compose_page.clear_Search_field()
        compose_page.type_text_into_search_field("A_CONTACT_FOR_APPIUM_TESTS")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        compose_page.choose_contact_for_test()
        compose_page.click_ok_button()

        # Compose an email and press Send. View the outgoing queue.
        compose_page.choose_email_message()
        compose_page.type_email_subject()
        compose_page.type_email_message()
        common_page.hide_keyboard()
        compose_page.click_ok_button()
        compose_page.click_send_button()
        compose_page.alert_send_button()
        common_page.hamburger_button()
        main_page.scroll_down_to_sent_button()
        main_page.open_SENT()
        common_page.take_screenshot("Sending_Communications_outgoing1")
        common_page.hamburger_button()

        # From the main menu press the Compose button.
        main_page.open_COMPOSE()

        # Press the + next to the recipients and add some recipient contacts and/or groups.
        compose_page.add_recipients()
        compose_page.add_contacts_and_groups()
        compose_page.clear_Search_field()
        compose_page.type_text_into_search_field("A_CONTACT_FOR_APPIUM_TESTS")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        compose_page.choose_contact_for_test()
        compose_page.click_ok_button()

        # Compose an SMS, text to voice and fax.
        compose_page.choose_sms_message()
        compose_page.type_sms_message()
        compose_page.click_ok_button()
        compose_page.choose_voice_message()
        compose_page.click_text_to_speech()
        compose_page.type_voice_message()
        compose_page.click_ok_button()
        compose_page.choose_fax_message()
        compose_page.choose_fax_document()
        compose_page.choose_comms_documents()
        compose_page.choose_file()
        compose_page.click_fax_ok_button()
        compose_page.click_send_button()
        compose_page.alert_send_button()

        # Go back to the main menu and press Sent. Verify the messages you sent appear here.
        common_page.hamburger_button()
        main_page.scroll_down_to_sent_button()
        main_page.open_SENT()
        common_page.take_screenshot("Sending_Communications_outgoing2")
        common_page.hamburger_button()

        # Compose a message, but this time add resource structure nodes as recipients.
        main_page.open_COMPOSE()
        compose_page.add_recipients()
        compose_page.add_resource_structure_nodes()
        compose_page.click_first_resource_structure_node_on_the_list()
        compose_page.click_ok_button()
        compose_page.choose_email_message()
        compose_page.type_email_subject()
        compose_page.type_email_message()
        common_page.hide_keyboard()
        compose_page.click_ok_button()
        compose_page.click_send_button()
        compose_page.alert_send_button()
        common_page.hamburger_button()

        # Compose a message but instead of sending it, press Save and give it a name.
        main_page.open_COMPOSE()
        compose_page.add_recipients()
        compose_page.add_contacts_and_groups()
        compose_page.clear_Search_field()
        compose_page.type_text_into_search_field("A_CONTACT_FOR_APPIUM_TESTS")
        common_page.click_Return_button_on_keyboard()
        common_page.hide_keyboard()
        compose_page.choose_contact_for_test()
        compose_page.click_ok_button()
        compose_page.choose_email_message()
        compose_page.type_email_subject()
        compose_page.type_email_message()
        common_page.hide_keyboard()
        compose_page.click_ok_button()
        compose_page.click_save_button()
        compose_page.type_name_for_message_draft("draft_msg")
        compose_page.click_save_button_inside_draft_popup()

        # Go to Compose > Drafts and select the draft named from previous step - The message you saved is loaded
        # Turn on flight mode and compose a communication. View the outbox.

        # Disable flight mode and turn on internet. View the outbox.

        # Compose a communication without recipients and attempt to send.

        # Add recipients to an empty communication and attempt to send.

        # Compose a communication and add attach a photo.
        compose_page.click_attachments_button()

        # Compose a communication and attach a video.
        # Compose a communication and attach audio.
        # Send SMS ,Email, Push, Voice message from a high user to a low user
        # Repeat step for different level users                  -------------------- ? low to high ?
        # Send SMS ,Email, Push, Voice message from high user to an other high user


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSendingCommunications)
    unittest.TextTestRunner(verbosity=2).run(suite)
