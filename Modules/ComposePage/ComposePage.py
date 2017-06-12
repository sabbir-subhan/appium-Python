"""A class for methods to handle Compose Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
import logging
from time import sleep
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
# from Conf.desired_capabilities import DesiredCapabilities


class ComposePage(BasePage):

    def click_ok_button(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.click_ok_button()

    def click_fax_ok_button(self):

        self.switch_context_to_webview()

        logging.info("click 'Ok' button")
        fax_ok_button = self.driver.find_element(*self.configuration.ComposeScreen.FAX_OK_BUTTON)
        self.assertIsNotNone(fax_ok_button, "Ok button not found")
        fax_ok_button.click()
        sleep(2)

        self.switch_context_to_native()

        # desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        # platform_name = desired_capabilities.get('platformName')
        # platform_version = desired_capabilities.get('platformVersion')
        # if "Android" in str(platform_name) and platform_version < "5":
        #     fax_ok_button = self.driver.find_element(*self.configuration.CommonScreen.OK_BUTTON)
        # else:
        #     fax_ok_button = self.driver.find_element(*self.configuration.ComposeScreen.FAX_OK_BUTTON)
        # self.assertIsNotNone(fax_ok_button, "Ok button not found")
        # fax_ok_button.click()
        # sleep(2)

    def click_send_button(self):

        self.switch_context_to_webview()

        logging.info("click 'Send' button")
        send_button = self.driver.find_element(*self.configuration.ComposeScreen.SEND_BUTTON)
        self.assertIsNotNone(send_button, "Send button not found")
        send_button.click()
        sleep(2)

        self.switch_context_to_native()

    def alert_send_button(self):

        self.switch_context_to_webview()

        logging.info("click 'Send' button on alert")
        send_button_on_alert = self.driver.find_element(*self.configuration.ComposeScreen.ALERT_SEND_BUTTON)
        send_button_on_alert.click()
        sleep(2)

        self.switch_context_to_native()

        logging.info("sending message")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.configuration.MainMenuScreen.INBOX_BUTTON),
            "Failed to send message")
        logging.info("Message was sent")

        # logging.info("click 'Send' button on alert")
        # desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        # platform_version = desired_capabilities.get('platformVersion')
        # if platform_version < "5":
        #     send_button_on_alert = self.driver.find_element(*self.configuration.ComposeScreen.ALERT_SEND_BUTTON_by_name)
        # else:
        #     send_button_on_alert = self.driver.find_element(*self.configuration.ComposeScreen.ALERT_SEND_BUTTON_by_id)
        # self.assertIsNotNone(send_button_on_alert, "Send button on alert not found")
        # send_button_on_alert.click()
        # sleep(2)
        # logging.info("sending message")
        # WebDriverWait(self.driver, 10).until(
        #     expected_conditions.presence_of_element_located(self.configuration.MainMenuScreen.EVENTS_BUTTON),
        #     "Failed to send message")
        # logging.info("Message was sent")

    def add_recipients(self):

        logging.info('add recipients')

        self.switch_context_to_webview()

        add_recipients_button = self.driver.find_element(*self.configuration.ComposeScreen.ADD_RECIPIENTS_BUTTON)
        self.assertIsNotNone(add_recipients_button, 'add recipients button not found')
        add_recipients_button.click()

        self.switch_context_to_native()

        sleep(2)

        # desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        # platform_name = desired_capabilities.get('platformName')
        # print('platform name: ' + str(platform_name))
        # if "iOS" in str(platform_name):
        #     self.switch_context_to_webview()
        #     add_recipients_button = self.driver.find_element(*self.configuration.ComposeScreen.ADD_RECIPIENTS_BUTTON)
        # else:
        #     add_recipients_button = self.driver.find_element(*self.configuration.ComposeScreen.ADD_RECIPIENTS_BUTTON)
        # self.assertIsNotNone(add_recipients_button, 'add recipients button not found')
        # add_recipients_button.click()
        #
        # self.switch_context_to_native()
        #
        # sleep(2)
        # add_recipients_button = self.driver.find_element(*self.configuration.ComposeScreen.ADD_RECIPIENTS_BUTTON)
        # self.assertIsNotNone(add_recipients_button, 'add recipients button not found')
        # add_recipients_button.click()

    def add_contacts_and_groups(self):

        logging.info('add contacts and groups')

        self.switch_context_to_webview()

        add_contacts_and_groups_button = self.driver.find_elements(*self.configuration.
                                                                   ComposeScreen.ADD_CONTACTS_AND_GROUPS)
        self.assertIsNotNone(add_contacts_and_groups_button, 'add recipients button not found')
        add_contacts_and_groups_button[0].click()

        self.switch_context_to_native()

        sleep(2)

    def contacts_arrow(self):

        self.switch_context_to_webview()

        logging.info('click in Contacts arrow to choose specific contact')
        contacts_arrow = self.driver.find_element(*self.configuration.ComposeScreen.CONTACTS_ARROW)
        self.assertIsNotNone(contacts_arrow, 'add recipients button not found')
        contacts_arrow.click()

        self.switch_context_to_native()

    def filter_contacts_by_search_field(self):

        logging.info("filter contacts by search field")

        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        self.assertIsNotNone(search_field, "Search field not found")
        search_field.click()
        sleep(2)
        search_field.send_keys('A_CONTACT_FOR_APPIUM_TESTS')
        sleep(1)

    def choose_contact_for_test(self):

        logging.info('choose contact for test')
        sleep(2)
        choose_contact_for_test = self.driver.find_element(*self.configuration.ComposeScreen.CONTACT_FOR_APPIUM_TESTS)
        self.assertIsNotNone(choose_contact_for_test, 'contact not found')
        choose_contact_for_test.click()

    def choose_sms_message(self):

        self.switch_context_to_webview()

        logging.info('choose sms msg')
        choose_sms_msg = self.driver.find_element(*self.configuration.ComposeScreen.MESSAGE_SMS)
        self.assertIsNotNone(choose_sms_msg, 'sms msg button not found')
        choose_sms_msg.click()

        self.switch_context_to_native()

    def type_sms_message(self):

        self.switch_context_to_webview()

        logging.info('type sms msg')
        sms_text_field = self.driver.find_element(*self.configuration.ComposeScreen.SMS_TEXT_FIELD)
        self.assertIsNotNone(sms_text_field, 'sms text field button not found')
        sms_text_field.click()
        sms_text_field.send_keys('Test SMS')

        self.switch_context_to_native()

    def choose_email_message(self):

        self.switch_context_to_webview()

        logging.info('choose email msg')
        choose_email_msg = self.driver.find_element(*self.configuration.ComposeScreen.MESSAGE_EMAIL)
        self.assertIsNotNone(choose_email_msg, 'email msg button not found')
        choose_email_msg.click()
        sleep(2)

        self.switch_context_to_native()

    def type_email_subject(self):

        self.switch_context_to_webview()

        logging.info('type email subject')
        email_subject_text_field = self.driver.find_element(*self.configuration.ComposeScreen.EMAIL_SUBJECT_FIELD)
        self.assertIsNotNone(email_subject_text_field, 'email subject field not found')
        email_subject_text_field.click()
        email_subject_text_field.send_keys('Test email subject')
        sleep(2)

        self.switch_context_to_native()

    def type_email_message(self):

        # self.switch_context_to_webview() # webview is not working on iOS10

        sleep(2)
        logging.info('type email msg')
        email_text_field = self.driver.find_element(*self.configuration.ComposeScreen.EMAIL_TEXT_FIELD)
        self.assertIsNotNone(email_text_field, 'email msg field not found')
        email_text_field.click()
        email_text_field.send_keys('Test email')

        # self.switch_context_to_native()

        # sleep(2)
        # logging.info('type email msg')
        # desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        # platform_name = desired_capabilities.get('platformName')
        # platform_version = desired_capabilities.get('platformVersion')
        # if "Android" in str(platform_name) and "6" in str(platform_version):
        #     email_text_field = self.driver.find_element(*self.configuration.ComposeScreen.EMAIL_TEXT_FIELD2)
        # else:
        #     email_text_field = self.driver.find_element(*self.configuration.ComposeScreen.EMAIL_TEXT_FIELD)
        # self.assertIsNotNone(email_text_field, 'email msg field button not found')
        # email_text_field.click()
        # email_text_field.send_keys('Test email')

    def choose_voice_message(self):

        self.switch_context_to_webview()

        logging.info('choose voice msg')
        choose_voice_msg = self.driver.find_element(*self.configuration.ComposeScreen.MESSAGE_VOICE)
        self.assertIsNotNone(choose_voice_msg, 'voice msg button not found')
        choose_voice_msg.click()

        self.switch_context_to_native()

    def click_text_to_speech(self):

        self.switch_context_to_webview()

        logging.info('click Text to speech')
        text_to_speech_button = self.driver.find_element(*self.configuration.ComposeScreen.TEXT_TO_SPEECH_BUTTON)
        self.assertIsNotNone(text_to_speech_button, 'Text to speech button not found')
        text_to_speech_button.click()

        self.switch_context_to_native()

    def type_voice_message(self):

        self.switch_context_to_webview()

        logging.info('type voice msg')
        voice_msg_text_field = self.driver.find_element(*self.configuration.ComposeScreen.VOICE_TEXT_FIELD)
        self.assertIsNotNone(voice_msg_text_field, 'voice msg field button not found')
        voice_msg_text_field.click()
        voice_msg_text_field.send_keys('Test voice msg')

        self.switch_context_to_native()

    def choose_fax_message(self):

        self.switch_context_to_webview()

        logging.info('choose fax msg')
        choose_fax_msg = self.driver.find_element(*self.configuration.ComposeScreen.MESSAGE_FAX)
        self.assertIsNotNone(choose_fax_msg, 'fax msg button not found')
        choose_fax_msg.click()
        sleep(1)

        self.switch_context_to_native()

    def choose_fax_document(self):

        self.switch_context_to_webview()

        logging.info('choose fax document button')
        fax_document_button = self.driver.find_element(*self.configuration.ComposeScreen.FAX_DOCUMENT_BUTTON)
        self.assertIsNotNone(fax_document_button, 'fax document button not found')
        fax_document_button.click()
        sleep(1)

        self.switch_context_to_native()

    def choose_comms_documents(self):

        self.switch_context_to_webview()

        logging.info('choose comms documents button')
        comms_documents_button = self.driver.find_element(*self.configuration.ComposeScreen.COMMS_DOCUMENTS_BUTTON)
        self.assertIsNotNone(comms_documents_button, 'comms documents button not found')
        comms_documents_button.click()
        sleep(1)

        self.switch_context_to_native()

    def choose_file(self):

        logging.info('choose file from documents')
        # files = self.driver.find_elements(*self.configuration.ComposeScreen.FILES_LIST)
        # self.assertIsNotNone(files, 'file in documents not found')
        # self.assertIsNotNone(files[0], 'first file in documents not found')
        # files[0].click()
        file = self.driver.find_element(*self.configuration.ComposeScreen.FAX_PDF_FILE)
        self.assertIsNotNone(file, 'file in documents not found')
        file.click()
        sleep(1)

    def check_recipient_field(self):

        self.switch_context_to_webview()

        logging.info("check recipient field")
        recipient_field = self.driver.find_element(*self.configuration.ComposeScreen.RECIPIENT_FIELD)
        self.assertIsNotNone(recipient_field, "Recipient field is empty")
        # try:
        #     text = recipient_field.get_attribute("Text")
        #     print(text)
        # except:
        #     print("except")

        self.switch_context_to_native()

    def click_more_button(self):

        self.switch_context_to_webview()

        logging.info("click More button")
        more_button = self.driver.find_element(*self.configuration.ComposeScreen.MORE_BUTTON)
        self.assertIsNotNone(more_button, "More button not found")
        more_button.click()

        self.switch_context_to_native()

    def discard_message(self):

        self.switch_context_to_webview()

        logging.info("click Discard button")
        discard_button = self.driver.find_element(*self.configuration.ComposeScreen.DISCARD_MESSAGE)
        self.assertIsNotNone(discard_button, "Discard button not found")
        discard_button.click()

        self.switch_context_to_native()

    def confirm_discard_message(self):

        self.switch_context_to_webview()

        logging.info("click Confirm Discard button on popup")
        confirm_discard_button = self.driver.find_element(*self.configuration.ComposeScreen.CONFIRM_DISCARD_MESSAGE)
        self.assertIsNotNone(confirm_discard_button, "Confirm Discard button not found")
        confirm_discard_button.click()

        self.switch_context_to_native()
