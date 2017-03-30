""" A class for methods to handle Event Edit Page """

import logging
from Modules.BasePage.BasePage import BasePage
from time import sleep
from selenium.common.exceptions import *
from Conf.desired_capabilities import DesiredCapabilities


class EventEditPage(BasePage):

    def fill_Name_input_field(self, text):

        self.switch_context_to_webview()

        logging.info("fill Name input field")
        name_field = self.driver.find_element(*self.configuration.EventEditScreen.NAME_FIELD)
        name_field.click()
        name_field.send_keys(text)

        self.switch_context_to_native()

    def type_text_into_description_field(self):

        #self.switch_context_to_webview()

        sleep(4)
        logging.info("type some text into description field")
        self.driver.find_element(*self.configuration.EventEditScreen.DESCRIPTION_FIELD).click()
        self.driver.find_element(*self.configuration.EventEditScreen.DESCRIPTION_FIELD).send_keys("test appium")

        #self.switch_context_to_native()

    def click_severity_lvl_picker(self):

        # self.switch_context_to_webview()
        #
        # logging.info("click on severity level field")
        # self.driver.find_element(*self.configuration.EventEditScreen.SEVERITY_LEVEL_SELECTOR).click()
        #
        # self.switch_context_to_native()

        logging.info("click on severity level field")
        # self.driver.find_element(*self.configuration.EventEditScreen.SEVERITY_LEVEL_SELECTOR).click()
        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        platform_name = desired_capabilities.get('platformName')
        platform_version = desired_capabilities.get('platformVersion')
        if platform_name == "ANDROID" and platform_version < "5":
            self.driver.find_element(*self.configuration.EventEditScreen.SEVERITY_LEVEL_SELECTOR2).click()
        else:
            self.driver.find_element(*self.configuration.EventEditScreen.SEVERITY_LEVEL_SELECTOR).click()

    # only for event type: "event_for_on_load/save_test"
    def check_on_load_and_on_save_sequences(self):

        logging.info("assert on load and on save sequence")
        sequence_onload_header = self.driver.find_element(*self.configuration.EventEditScreen.SEQUENCE_ONLOAD_HEADER)
        self.assertIsNotNone(sequence_onload_header)
        sequence_onload_value = self.driver.find_element(*self.configuration.EventEditScreen.SEQUENCE_ONLOAD_VALUE)
        self.assertIsNotNone(sequence_onload_value)
        sequence_onsave_header = self.driver.find_element(*self.configuration.EventEditScreen.SEQUENCE_ONSAVE_HEADER)
        sequence_onsave_value = self.driver.find_element(*self.configuration.EventEditScreen.SEQUENCE_ONSAVE_VALUE)
        self.assertIsNotNone(sequence_onsave_header)
        self.assertIsNotNone(sequence_onsave_value)

    def click_create_mapping_data(self):

        sleep(2)
        logging.info("create mapping data")
        create_mapping_data_button = self.driver.find_element(*self.configuration.EventEditScreen.CREATE_MAPPING_DATA)
        self.assertIsNotNone(create_mapping_data_button, "Button for creating map data is not present")
        create_mapping_data_button.click()

    def check_restored_field_1(self):

        logging.info("assert restored field 1")
        field_to_restore_1_header = self.driver.find_element(*self.configuration.EventEditScreen.
                                                             FIELD_TO_RESTORE_1_HEADER)
        self.assertIsNotNone(field_to_restore_1_header)
        field_to_restore_1_value = self.driver.find_element(*self.configuration.EventEditScreen.
                                                            FIELD_TO_RESTORE_1_VALUE)
        self.assertIsNotNone(field_to_restore_1_value)

    def check_restored_field_2(self):

        logging.info("assert restored field 2")
        field_to_restore_2_header = self.driver.find_element(*self.configuration.EventEditScreen.
                                                             FIELD_TO_RESTORE_2_HEADER)
        self.assertIsNotNone(field_to_restore_2_header)
        field_to_restore_2_value = self.driver.find_element(*self.configuration.EventEditScreen.
                                                            FIELD_TO_RESTORE_2_VALUE)
        self.assertIsNotNone(field_to_restore_2_value)

    def check_hidden_field_1(self):

        logging.info("assert hidden field")
        try:
            field_to_restore_1_header = self.driver.find_element(*self.configuration.EventEditScreen.
                                                                 FIELD_TO_RESTORE_1_HEADER)
            if field_to_restore_1_header.is_displayed():
                self.fail("field was not hidden correctly")
            else:
                pass
        except NoSuchElementException:
            logging.info("field is not visible = OK")
            pass

    def check_hidden_fields_1_and_2(self):

        logging.info("assert hidden fields")
        try:
            field_to_restore_1_header = self.driver.find_element(*self.configuration.EventEditScreen.
                                                                 FIELD_TO_RESTORE_1_HEADER)
            field_to_restore_2_header = self.driver.find_element(*self.configuration.EventEditScreen.
                                                                 FIELD_TO_RESTORE_2_HEADER)
            if field_to_restore_1_header.is_displayed():
                self.fail("field 1 was not hidden correctly")
            if field_to_restore_2_header.is_displayed():
                self.fail("field 2 was not hidden correctly")
            else:
                pass
        except NoSuchElementException:
            logging.info("fields are not visible = OK")
            pass

    def click_on_choose_field_inside_subform(self):

        sleep(5)
        logging.info("click_on_choose_field_inside_subform")
        event_chooser_in_subform = self.driver.find_element(*self.configuration.EventEditScreen.
                                                            NEW_EVENTS_CHOOSER_IN_SUB_FORM)
        self.assertIsNotNone(event_chooser_in_subform, "event chooser in subform not found")
        event_chooser_in_subform.click()
        sleep(5)

    def click_save_new_event(self):

        self.switch_context_to_webview()

        sleep(1)
        logging.info("click Save button")
        sleep(1)
        save_button = self.driver.find_element(*self.configuration.EventEditScreen.SAVE_BUTTON_NEW_EVENT)
        self.assertIsNotNone(save_button, "Save button not found")
        save_button.click()
        sleep(10)

        self.switch_context_to_native()

    def click_save_edited_event(self):

        self.switch_context_to_webview()

        sleep(1)
        logging.info("click Save button")
        sleep(1)
        save_button = self.driver.find_element(*self.configuration.EventEditScreen.SAVE_BUTTON_EDIT_EVENT)
        self.assertIsNotNone(save_button, "Save button not found")
        save_button.click()
        sleep(10)

        self.switch_context_to_native()

    def click_cancel_button(self):

        logging.info("click on Cancel button")
        cancel_button = self.driver.find_element(*self.configuration.CommonScreen.CANCEL_BUTTON)
        self.assertIsNotNone(cancel_button, "Cancel button not found")
        cancel_button.click()
        sleep(4)

    def click_on_event_chooser_field(self):

        logging.info("click_on_event_chooser_field")
        chooser_field_for_event = self.driver.find_element(*self.configuration.EventEditScreen.CHOOSER_FIELD)
        self.assertIsNotNone(chooser_field_for_event, "chooser_field_for_event not found")
        chooser_field_for_event.click()
        sleep(1)








