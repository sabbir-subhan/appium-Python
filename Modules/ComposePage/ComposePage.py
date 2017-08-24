"""A class for methods to handle Compose Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
import logging
from time import sleep
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


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

    def click_send_button(self):

        self.switch_context_to_webview()

        logging.info("click 'Send' button")
        send_button = self.driver.find_element(*self.configuration.ComposeScreen.SEND_BUTTON)
        self.assertIsNotNone(send_button, "Send button not found")
        send_button.click()
        sleep(2)

        self.switch_context_to_native()

    def click_save_button(self):

        self.switch_context_to_webview()

        logging.info("click 'Save' button")
        send_button = self.driver.find_element(*self.configuration.ComposeScreen.SAVE_BUTTON)
        self.assertIsNotNone(send_button, "Save button not found")
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

    def add_recipients(self):

        logging.info('add recipients')

        self.switch_context_to_webview()

        add_recipients_button = self.driver.find_element(*self.configuration.ComposeScreen.ADD_RECIPIENTS_BUTTON)
        self.assertIsNotNone(add_recipients_button, 'add recipients button not found')
        add_recipients_button.click()

        self.switch_context_to_native()

        sleep(2)

    def add_contacts_and_groups(self):

        logging.info('add contacts and groups')

        self.switch_context_to_webview()

        add_contacts_and_groups_button = self.driver.find_elements(*self.configuration.
                                                                   ComposeScreen.ADD_CONTACTS_AND_GROUPS)
        self.assertIsNotNone(add_contacts_and_groups_button, 'add recipients button not found')
        add_contacts_and_groups_button[0].click()

        self.switch_context_to_native()

        sleep(2)

    def add_resource_structure_nodes(self):

        logging.info('add resource structure nodes')

        self.switch_context_to_webview()

        add_resource_structure_nodes = self.driver.find_elements(*self.configuration.ComposeScreen.ADD_RESOURCES_STRUCTURE_NODES)
        self.assertIsNotNone(add_resource_structure_nodes, 'add resource structure nodes button not found')
        # add_resource_structure_nodes[0].click()
        add_resource_structure_nodes[1].click()

        self.switch_context_to_native()

        sleep(2)

    def click_first_resource_structure_node_on_the_list(self):

        self.switch_context_to_webview()

        logging.info("Choose first structure node on the list")
        click_first_resource_structure_node_on_the_list = self.driver.find_element(*self.configuration.TeamRoleScreen.FIRST_STRUCTURE_NODE_ON_THE_LIST)  # first - child
        self.assertIsNotNone(click_first_resource_structure_node_on_the_list, "Structure node not found")
        click_first_resource_structure_node_on_the_list.click()

        self.switch_context_to_native()

    def click_second_resource_structure_node_on_the_list(self):

        self.switch_context_to_webview()

        logging.info("Choose second structure node on the list")
        click_second_resource_structure_node_on_the_list = self.driver.find_element(*self.configuration.TeamRoleScreen.SECOND_STRUCTURE_NODE_ON_THE_LIST)  # second - child
        self.assertIsNotNone(click_second_resource_structure_node_on_the_list, "Structure node not found")
        click_second_resource_structure_node_on_the_list.click()

        self.switch_context_to_native()

    def click_last_resource_structure_node_on_the_list(self):

        self.switch_context_to_webview()

        logging.info("Choose last structure node on the list")
        click_last_resource_structure_node_on_the_list = self.driver.find_element(*self.configuration.TeamRoleScreen.LAST_STRUCTURE_NODE_ON_THE_LIST)  # last- child
        self.assertIsNotNone(click_last_resource_structure_node_on_the_list, "Structure node not found")
        click_last_resource_structure_node_on_the_list.click()

        self.switch_context_to_native()

    def first_element_arrow_button(self):

        self.switch_context_to_webview()

        logging.info('click in arrow button of the first element on the list')
        contacts_arrow = self.driver.find_element(*self.configuration.ComposeScreen.FIRST_ELEMENT_ARROW)
        self.assertIsNotNone(contacts_arrow, 'arrow button for the first element on the list not found')
        contacts_arrow.click()

        self.switch_context_to_native()

    def type_text_into_search_field(self, text):

        contacts_page = LoadClass.load_page('ContactsPage')
        contacts_page.setDriver(self.driver)
        contacts_page.type_text_into_search_field(text)

    def clear_Search_field(self):

        self.switch_context_to_webview()

        try:
            clear_search_field_button = self.driver.find_element(*self.configuration.ContactsScreen.CLEAR_SEARCH_FIELD_BUTTON)
            if clear_search_field_button.is_displayed():
                logging.info("clear Search field by clicking clear button")
                self.assertIsNotNone(clear_search_field_button, "clear search field button not found")
                clear_search_field_button.click()
                sleep(2)
        except NoSuchElementException:
            pass

        self.switch_context_to_native()

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

    def click_attachments_button(self):  # Attachments button inside email msg

        self.switch_context_to_webview()

        logging.info("click Attachments button")
        attachment_button = self.driver.find_element(*self.configuration.ComposeScreen.EMAIL_ATTACHMENTS)
        self.assertIsNotNone(attachment_button, "Attachments button not found")
        attachment_button.click()

        self.switch_context_to_native()

    def type_name_for_message_draft(self, text):

        self.switch_context_to_webview()

        logging.info("type name for message draft")
        input_field_for_draft_msg = self.driver.find_element(*self.configuration.ComposeScreen.SAVE_DRAFT_INPUT_NAME)
        self.assertIsNotNone(input_field_for_draft_msg, "Attachments button not found")
        input_field_for_draft_msg.click()
        input_field_for_draft_msg.send_keys(text)

        self.switch_context_to_native()

    def click_save_button_inside_draft_popup(self):

        self.switch_context_to_webview()

        logging.info("click Save button inside draft popup")
        save_button_inside_draft_popup = self.driver.find_element(*self.configuration.ComposeScreen.SAVE_BUTTON_INSIDE_DRAFT_POPUP)
        self.assertIsNotNone(save_button_inside_draft_popup, "Save button inside draft popup, not found")
        save_button_inside_draft_popup.click()

        self.switch_context_to_native()


