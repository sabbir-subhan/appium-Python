"""A class for methods to handle Events Page """

from Modules.BasePage.BasePage import BasePage
from time import sleep
import logging
from selenium.common.exceptions import *
from Modules.load_class import LoadClass


class EventsPage(BasePage):

    def clear_primary_event(self):

        logging.info("clicking in 'Clear primary event' button")
        sleep(1)
        clear_primary_event_button = self.driver.find_element(*self.configuration.EventsScreen.
                                                              CLEAR_PRIMARY_EVENT_BUTTON)
        self.assertIsNotNone(clear_primary_event_button, "Clear primary event button not found")
        clear_primary_event_button.click()
        # try:
        #     logging.info("checking notification - 'Primary event cleared'")
        #     WebDriverWait(self.driver, 25).until(
        #         expected_conditions.presence_of_element_located(self.configuration.EventsScreen.NOTIFICATION_PRIMARY_EVENT_CLEARED),
        #         "Notification is not present")
        #     # sleep(1)
        #     # notification = self.driver.find_element(*self.configuration.EventsScreen.NOTIFICATION_PRIMARY_EVENT_CLEARED)
        #     # self.assertIsNotNone(notification)
        # except NoSuchElementException:
        #     logging.info("notification not found")

    # def filter_events_by_Search_field(self):
    #
    #     self.switch_context_to_webview()
    #
    #     logging.info("search field - search event named: 'search'")
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).click()
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).send_keys("search")
    #
    #     self.switch_context_to_native()
    #
    # def clear_Search_field(self):
    #
    #     self.switch_context_to_webview()
    #
    #     logging.info("clear search field")
    #     search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
    #     search_field.clear()
    #
    #     self.switch_context_to_native()
    #
    # def filter_events_to_find_previous_event(self):
    #
    #     self.switch_context_to_webview()
    #
    #     logging.info("search field - search event named: 'app'")
    #     sleep(2)
    #     search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
    #     search_field.click()
    #     search_field.send_keys("app")
    #
    #     self.switch_context_to_native()

    def click_more_button_in_events_list(self):

        self.switch_context_to_webview()

        logging.info("click 'More' button")
        more_button = self.driver.find_element(*self.configuration.EventsScreen.MORE_BUTTON)
        self.assertIsNotNone(more_button, "More button was not found")
        more_button.click()

        self.switch_context_to_native()

    def click_more_button_in_event_details(self):

        self.switch_context_to_webview()

        sleep(1)
        logging.info("click 'More' button")
        more_button = self.driver.find_element(*self.configuration.EventDetailsScreen.MORE_BUTTON)
        self.assertIsNotNone(more_button, "More button was not found")
        more_button.click()

        self.switch_context_to_native()

    # def click_More_button(self):
    #
    #     sleep(2)
    #     logging.info("click 'More' button")
    #     more_button = self.driver.find_element(*self.configuration.EventsScreen.MORE_BUTTON)
    #     self.assertIsNotNone(more_button, "More button was not found")
    #     more_button.click()
    #     sleep(0.5)

    def check_if_EVENTS_were_opened(self):

        sleep(2)
        logging.info("check if Events were opened")
        events_header = self.driver.find_element(*self.configuration.EventsScreen.EVENTS_HEADER)
        self.assertIsNotNone(events_header)

    # def filter_events_by_Type(self):
    # 
    #     sleep(1)
    #     logging.info("filtering events by Type")
    #     self.driver.find_element(*self.configuration.EventsScreen.ANY_TYPE_EXPAND).click()
    #     self.driver.find_element(*self.configuration.EventsScreen.CHOOSE_TYPE_INCIDENT).click()
    #     sleep(1)
    #     self.driver.find_element(*self.configuration.EventsScreen.INCIDENT_TYPE_EXPAND).click()
    #     self.driver.find_element(*self.configuration.EventsScreen.CHOOSE_TYPE_ANY).click()
    #     sleep(1)
    # 
    # def filter_events_by_Status(self):
    # 
    #     sleep(1)
    #     logging.info("filtering events by Status")
    #     self.driver.find_element(*self.configuration.EventsScreen.ANY_STATUS_EXPAND).click()
    #     self.driver.find_element(*self.configuration.EventsScreen.CHOOSE_ACTIVE_STATUS).click()
    #     sleep(1)
    #     self.driver.find_element(*self.configuration.EventsScreen.ACTIVE_STATUS_EXPAND).click()
    #     self.driver.find_element(*self.configuration.EventsScreen.CHOOSE_INACTIVE_STATUS).click()
    #     sleep(1)
    #     self.driver.find_element(*self.configuration.EventsScreen.INACTIVE_STATUS_EXPAND).click()
    #     self.driver.find_element(*self.configuration.EventsScreen.CHOOSE_DRAFT_STATUS).click()
    #     sleep(1)
    #     self.driver.find_element(*self.configuration.EventsScreen.DRAFT_STATUS_EXPAND).click()
    #     self.driver.find_element(*self.configuration.EventsScreen.CHOOSE_ANY_STATUS).click()
    #     sleep(1)

    def filter_events_by_type(self):

        self.switch_context_to_webview()

        logging.info("filter events by type")

        expand_type_filters = self.driver.find_element(*self.configuration.EventsScreen.TYPE_FILTER)
        self.assertIsNotNone(expand_type_filters, "type filter not found")
        expand_type_filters.click()

        choose_second_type = self.driver.find_element(*self.configuration.EventsScreen.SECOND_TYPE)
        self.assertIsNotNone(choose_second_type, "second status not found")
        choose_second_type.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

        self.switch_context_to_webview()

        expand_type_filters = self.driver.find_element(*self.configuration.EventsScreen.TYPE_FILTER)
        self.assertIsNotNone(expand_type_filters, "type filter not found")
        expand_type_filters.click()

        choose_third_type = self.driver.find_element(*self.configuration.EventsScreen.THIRD_TYPE)
        self.assertIsNotNone(choose_third_type, "third status not found")
        choose_third_type.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

        self.switch_context_to_webview()

        expand_type_filters = self.driver.find_element(*self.configuration.EventsScreen.TYPE_FILTER)
        self.assertIsNotNone(expand_type_filters, "type filter not found")
        expand_type_filters.click()

        choose_fourth_type = self.driver.find_element(*self.configuration.EventsScreen.FOURTH_TYPE)
        self.assertIsNotNone(choose_fourth_type, "fourth status not found")
        choose_fourth_type.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

        self.switch_context_to_webview()

        expand_type_filters = self.driver.find_element(*self.configuration.EventsScreen.TYPE_FILTER)
        self.assertIsNotNone(expand_type_filters, "type filter not found")
        expand_type_filters.click()

        choose_first_type = self.driver.find_element(*self.configuration.EventsScreen.FIRST_TYPE)
        self.assertIsNotNone(choose_first_type, "first status not found")
        choose_first_type.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    def filter_events_by_status(self):

        self.switch_context_to_webview()

        logging.info("filter events by status")

        expand_status_filters = self.driver.find_element(*self.configuration.EventsScreen.STATUS_FILTER)
        self.assertIsNotNone(expand_status_filters, "status filter not found")
        expand_status_filters.click()

        choose_second_status = self.driver.find_element(*self.configuration.EventsScreen.SECOND_STATUS)
        self.assertIsNotNone(choose_second_status, "second status not found")
        choose_second_status.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

        self.switch_context_to_webview()

        expand_status_filters = self.driver.find_element(*self.configuration.EventsScreen.STATUS_FILTER)
        self.assertIsNotNone(expand_status_filters, "status filter not found")
        expand_status_filters.click()

        choose_third_status = self.driver.find_element(*self.configuration.EventsScreen.THIRD_STATUS)
        self.assertIsNotNone(choose_third_status, "third status not found")
        choose_third_status.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

        self.switch_context_to_webview()

        expand_status_filters = self.driver.find_element(*self.configuration.EventsScreen.STATUS_FILTER)
        self.assertIsNotNone(expand_status_filters, "status filter not found")
        expand_status_filters.click()

        choose_fourth_status = self.driver.find_element(*self.configuration.EventsScreen.FOURTH_STATUS)
        self.assertIsNotNone(choose_fourth_status, "fourth status not found")
        choose_fourth_status.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

        self.switch_context_to_webview()

        expand_status_filters = self.driver.find_element(*self.configuration.EventsScreen.STATUS_FILTER)
        self.assertIsNotNone(expand_status_filters, "status filter not found")
        expand_status_filters.click()

        choose_first_status = self.driver.find_element(*self.configuration.EventsScreen.FIRST_STATUS)
        self.assertIsNotNone(choose_first_status, "first status not found")
        choose_first_status.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

        # self.switch_context_to_native()

    def filter_events_by_active_status(self):

        self.switch_context_to_webview()

        logging.info("filter events by active status")

        expand_status_filters = self.driver.find_element(*self.configuration.EventsScreen.STATUS_FILTER)
        self.assertIsNotNone(expand_status_filters, "status filter not found")
        expand_status_filters.click()

        choose_second_status = self.driver.find_element(*self.configuration.EventsScreen.SECOND_STATUS)
        self.assertIsNotNone(choose_second_status, "second status not found")
        choose_second_status.click()
        sleep(1)

        self.switch_context_to_native()

    def filter_events_by_any_status(self):

        self.switch_context_to_webview()

        logging.info("filter events by any status")

        expand_status_filters = self.driver.find_element(*self.configuration.EventsScreen.STATUS_FILTER)
        self.assertIsNotNone(expand_status_filters, "status filter not found")
        expand_status_filters.click()

        choose_second_status = self.driver.find_element(*self.configuration.EventsScreen.FIRST_STATUS)
        self.assertIsNotNone(choose_second_status, "second status not found")
        choose_second_status.click()
        sleep(1)

        self.switch_context_to_native()

    def click_New_event_button(self):

        self.switch_context_to_webview()

        sleep(1)
        logging.info("clicking in New event button")
        new_event_button = self.driver.find_element(*self.configuration.EventsScreen.NEW_EVENT_BUTTON)
        self.assertIsNotNone(new_event_button, "New Event button not found")
        new_event_button.click()
        sleep(0.5)

        self.switch_context_to_native()

    def click_New_sub_event(self):

        logging.info("clicking in 'New sub event' button")
        new_sub_event = self.driver.find_element(*self.configuration.EventDetailsScreen.NEW_SUB_EVENT)
        self.assertIsNotNone(new_sub_event, "New sub event button is not present")
        new_sub_event.click()
        sleep(3)

    def open_previously_created_event_checkbox(self):

        self.switch_context_to_webview()

        sleep(4)
        logging.info("open created event")
        created_event = self.driver.find_element(*self.configuration.EventsScreen.PREVIOUSLY_CREATED_EVENT_CHECKBOX)
        created_event.click()
        sleep(5)

        self.switch_context_to_native()

    def open_previously_created_event(self):  # first event on the list

        self.switch_context_to_webview()

        sleep(4)
        logging.info("open created event")
        # created_event = self.driver.find_elements(*self.configuration.EventsScreen.PREVIOUSLY_CREATED_EVENT)
        # created_event[0].click()
        # sleep(5)

        # created_event = self.driver.find_elements(*self.configuration.EventsScreen.PREVIOUSLY_CREATED_EVENT)
        # created_event[0].click()
        created_event = self.driver.find_element(*self.configuration.EventsScreen.PREVIOUSLY_CREATED_EVENT)
        created_event.click()
        # sleep(5)

        self.switch_context_to_native()

        # sleep(2)
        # logging.info("open created event")
        # created_event = self.driver.find_element(*self.configuration.EventsScreen.PREVIOUSLY_CREATED_EVENT)
        # self.assertIsNotNone(created_event, "Previously created event not found")
        # created_event.click()
        # sleep(5)

    # def open_previously_created_event2(self):
    #
    #     logging.info("open previously created Event, Edit and Create mapping data")
    #     created_event2 = self.driver.find_element(*self.configuration.EventsScreen.CREATED_EVENT_2)
    #     self.assertIsNotNone(created_event2, "Created event 2 not found")
    #     created_event2.click()
    #     sleep(5)

    # def open_previously_created_event3(self):
    #
    #     logging.info("open previously created Event, Edit and Create mapping data")
    #     created_event3 = self.driver.find_element(*self.configuration.EventsScreen.CREATED_EVENT_3)
    #     self.assertIsNotNone(created_event3, "Created event 3 not found")
    #     created_event3.click()
    #     sleep(5)

    # only for events list, opened from chooser fields inside other event
    # def click_on_previously_created_event_for_chooser_field(self):
    #
    #     sleep(5)
    #     logging.info("click_on_previously_created_event_for_chooser_field")
    #     event_for_chooser_field = self.driver.find_element(*self.configuration.EventEditScreen.
    #                                                        PREVIOUSLY_CREATED_EVENT_FOR_CHOOSER)
    #     self.assertIsNotNone(event_for_chooser_field, "event_for_chooser_field not found")
    #     event_for_chooser_field.click()
    #     sleep(5)
    #
    # def click_on_previously_created_event_for_subform_chooser(self):
    #
    #     sleep(10)
    #     logging.info("click_on_previously_created_event_for_subform_chooser")
    #     event_for_subform = self.driver.find_element(*self.configuration.EventEditScreen.
    #                                                  PREVIOUSLY_CREATED_EVENT_FOR_CHOOSER)
    #     self.assertIsNotNone(event_for_subform, "event_for_subform not found")
    #     event_for_subform.click()
    #     sleep(5)

    # def event_details_More_button(self):
    #
    #     self.switch_context_to_webview()
    #
    #     logging.info("click 'More' button")
    #     more_button = self.driver.find_element(*self.configuration.EventDetailsScreen.MORE_BUTTON)
    #     self.assertIsNotNone(more_button, "More button was not found")
    #     more_button.click()
    #     sleep(0.5)
    #
    #     self.switch_context_to_native()

    def click_edit_button(self):

        logging.info("edit previously created event")

        try:
            self.driver.find_element(*self.configuration.EventDetailsScreen.EVENT_INFO_BUTTON).click()
        except NoSuchElementException:
            pass

        self.switch_context_to_webview()

        sleep(1)
        edit_button = self.driver.find_element(*self.configuration.EventDetailsScreen.EDIT_BUTTON)
        self.assertIsNotNone(edit_button, "edit button not found")
        edit_button.click()
        sleep(2)

        self.switch_context_to_native()

        sleep(2)

    def set_as_primary_event(self):

        self.switch_context_to_webview()

        logging.info("clicking in 'Set as primary' button")
        set_as_primary_button = self.driver.find_element(*self.configuration.EventDetailsScreen.
                                                         SET_AS_PRIMARY_BUTTON)
        self.assertIsNotNone(set_as_primary_button, "Set as primary button not found")
        set_as_primary_button.click()
        sleep(2)

        self.switch_context_to_native()

    def click_Delete_button(self):

        self.switch_context_to_webview()

        logging.info("clicking in 'Delete event' button")
        delete_event_button = self.driver.find_element(*self.configuration.EventDetailsScreen.DELETE_EVENT_BUTTON)
        self.assertIsNotNone(delete_event_button, "delete event button not found")
        delete_event_button.click()

        self.switch_context_to_native()

    def alert_confirm_delete(self):

        logging.info("confirm delete")
        delete_confirm_button = self.driver.find_element(*self.configuration.EventDetailsScreen.DELETE_CONFIRM_BUTTON)
        self.assertIsNotNone(delete_confirm_button, "confirm delete button not found")
        delete_confirm_button.click()
        sleep(7)

    def click_button_add_row(self):

        self.switch_context_to_webview()

        logging.info("click button Add row")
        add_row = self.driver.find_element(*self.configuration.EventEditScreen.SUBFORM_FIELD_ADD_ROW)
        self.assertIsNotNone(add_row, "add_row button not found")
        add_row.click()

        self.switch_context_to_native()

    def delete_chosen_event_inside_subform(self):

        self.switch_context_to_webview()

        sleep(1)
        logging.info("delete chosen event inside sub form")
        delete_button_inside_sub_form = self.driver.find_element(*self.configuration.EventEditScreen.
                                                                 DELETE_SUB_EVENT_FROM_CHOOSER)
        self.assertIsNotNone(delete_button_inside_sub_form, "delete button inside sub form not found")
        delete_button_inside_sub_form.click()

        self.switch_context_to_native()

        sleep(2)

    def fill_Name_input_field(self, text):

        self.switch_context_to_webview()

        logging.info("fill Name input field")
        name_field = self.driver.find_element(*self.configuration.EventEditScreen.NAME_FIELD)
        name_field.click()
        name_field.send_keys(text)

        self.switch_context_to_native()

    def type_text_into_description_field(self):

        self.switch_context_to_webview()  # webview is not working on iOS10

        sleep(2)
        logging.info("type some text into description field")
        description_field = self.driver.find_element(*self.configuration.EventEditScreen.DESCRIPTION_FIELD)
        description_field.click()
        description_field.send_keys("test appium")

        self.switch_context_to_native()

        # sleep(4)
        # logging.info("type some text into description field")
        # self.driver.find_element(*self.configuration.EventEditScreen.DESCRIPTION_FIELD).click()
        # self.driver.find_element(*self.configuration.EventEditScreen.DESCRIPTION_FIELD).send_keys("test appium")

    def click_severity_lvl_picker(self):  # not working for iOS 10

        sleep(1)

        self.switch_context_to_webview()

        logging.info("click on severity level field")
        self.driver.find_element(*self.configuration.EventEditScreen.SEVERITY_LEVEL_SELECTOR).click()

        self.switch_context_to_native()

        # self.driver.find_element(*self.configuration.EventEditScreen.SEVERITY_LEVEL_SELECTOR).click()
        # desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        # platform_name = desired_capabilities.get('platformName')
        # platform_version = desired_capabilities.get('platformVersion')
        # if platform_name == "ANDROID" and platform_version < "5":
        #     self.driver.find_element(*self.configuration.EventEditScreen.SEVERITY_LEVEL_SELECTOR2).click()
        # else:
        #     self.driver.find_element(*self.configuration.EventEditScreen.SEVERITY_LEVEL_SELECTOR).click()

    # only for event type: "event_for_on_load/save_test"

    def click_severity_lvl_picker_for_edit_event(self):

        sleep(1)

        self.switch_context_to_webview()

        logging.info("click on severity level field")
        severity_picker = self.driver.find_element(*self.configuration.EventEditScreen.
                                                   SEVERITY_LEVEL_SELECTOR_EDIT_EVENT)
        self.assertIsNotNone(severity_picker, "severity picker for edited event not found")
        severity_picker.click()

        self.switch_context_to_native()

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

        self.switch_context_to_webview()

        logging.info("create mapping data")
        try:
            create_mapping_data_button = self.driver.find_element(*self.configuration.EventEditScreen.CREATE_MAPPING_DATA_NEW)
        except NoSuchElementException:
            create_mapping_data_button = self.driver.find_element(*self.configuration.EventEditScreen.CREATE_MAPPING_DATA_EDIT)
        self.assertIsNotNone(create_mapping_data_button, "Button for creating map data is not present")
        create_mapping_data_button.click()

        self.switch_context_to_native()

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
                logging.info("hidden field 1 is not displayed")
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
            if field_to_restore_1_header.is_displayed() or field_to_restore_2_header.is_displayed():
                self.fail("fields 1 and 2 were not hidden correctly")
            else:
                logging.info("hidden fields 1 and 2 are not displayed")
                pass
        except NoSuchElementException:
            logging.info("fields are not visible = OK")
            pass

    def click_on_choose_field_inside_subform(self):

        self.switch_context_to_webview()

        sleep(2)
        logging.info("click_on_choose_field_inside_subform")
        event_chooser_in_subform = self.driver.find_element(*self.configuration.EventEditScreen.
                                                            NEW_EVENTS_CHOOSER_IN_SUB_FORM)
        self.assertIsNotNone(event_chooser_in_subform, "event chooser in subform not found")
        event_chooser_in_subform.click()
        sleep(2)

        self.switch_context_to_native()
        # sleep(5)
        # logging.info("click_on_choose_field_inside_subform")
        # event_chooser_in_subform = self.driver.find_element(*self.configuration.EventEditScreen.
        #                                                     NEW_EVENTS_CHOOSER_IN_SUB_FORM)
        # self.assertIsNotNone(event_chooser_in_subform, "event chooser in subform not found")
        # event_chooser_in_subform.click()
        # sleep(5)

    def click_save_button(self):

        sleep(1)
        logging.info("click Save button")
        sleep(1)
        save_button = self.driver.find_element(*self.configuration.EventEditScreen.SAVE_BUTTON)
        self.assertIsNotNone(save_button, "Save button not found")
        save_button.click()
        sleep(2)

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    def click_save_new_event(self):

        self.switch_context_to_webview()

        sleep(1)
        logging.info("click Save button")
        sleep(1)
        save_button = self.driver.find_element(*self.configuration.EventEditScreen.SAVE_BUTTON_NEW_EVENT)
        self.assertIsNotNone(save_button, "Save button not found")
        save_button.click()
        sleep(2)

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    def click_save_edited_event(self):

        self.switch_context_to_webview()

        sleep(1)
        logging.info("click Save button")
        sleep(1)
        save_button = self.driver.find_element(*self.configuration.EventEditScreen.SAVE_BUTTON_EDIT_EVENT)
        self.assertIsNotNone(save_button, "Save button not found")
        save_button.click()
        sleep(2)

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    # def click_cancel_button(self):
    #
    #     logging.info("click on Cancel button")
    #     cancel_button = self.driver.find_element(*self.configuration.CommonScreen.CANCEL_BUTTON)
    #     self.assertIsNotNone(cancel_button, "Cancel button not found")
    #     cancel_button.click()
    #     sleep(4)

    def click_cancel_button(self):

        self.switch_context_to_webview()

        logging.info("click on Cancel button")
        cancel_button = self.driver.find_element(*self.configuration.EventEditScreen.CANCEL_BUTTON)
        self.assertIsNotNone(cancel_button, "Cancel button not found")
        cancel_button.click()
        sleep(4)

        self.switch_context_to_native()

    def click_cancel_button_for_edited_event(self):

        self.switch_context_to_webview()

        logging.info("click on Cancel button")
        cancel_button = self.driver.find_element(*self.configuration.EventEditScreen.CANCEL_BUTTON_EDIT_EVENT)
        self.assertIsNotNone(cancel_button, "Cancel button not found")
        cancel_button.click()
        sleep(4)

        self.switch_context_to_native()

    def click_on_event_chooser_field(self):

        logging.info("click_on_event_chooser_field")
        chooser_field_for_event = self.driver.find_element(*self.configuration.EventEditScreen.CHOOSER_FIELD)
        self.assertIsNotNone(chooser_field_for_event, "chooser_field_for_event not found")
        chooser_field_for_event.click()
        sleep(1)

    def choose_Incident_type_of_event(self):

        event_type_incident = self.driver.find_element(*self.configuration.TypesOfEventsScreen.INCIDENT_TYPE_OF_EVENT)
        self.assertIsNotNone(event_type_incident, "event type Incident not found")
        logging.info("choosing Incident type of new event")
        event_type_incident.click()

    def choose_Event_for_on_load_save_type_of_event(self):

        event_type_onload = self.driver.find_element(*self.configuration.TypesOfEventsScreen.EVENT_FOR_ON_LOAD_SAVE)
        self.assertIsNotNone(event_type_onload, "event type onload not found")
        logging.info("choose type of event = event_for_on_load/save_test")
        event_type_onload.click()

    def choose_Event_for_chooser_fields_type_of_event(self):

        event_type_chooser = self.driver.find_element(*self.configuration.TypesOfEventsScreen.EVENT_FOR_CHOOSER_FIELDS)
        self.assertIsNotNone(event_type_chooser, "event type chooser not found")
        logging.info("choose type of event = event for chooser fields")
        event_type_chooser.click()
        sleep(5)

    def type_text_into_search_field(self, text):

        logging.info("filter events by search field")

        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        self.assertIsNotNone(search_field, "Search field not found")
        search_field.click()
        sleep(1)
        search_field.send_keys(text)
        sleep(1)

    def clear_Search_field(self):

        self.switch_context_to_webview()

        try:
            clear_search_field_button = self.driver.find_element(*self.configuration.EventsScreen.CLEAR_SEARCH_FIELD_BUTTON)
            if clear_search_field_button.is_displayed():
                logging.info("clear Search field by clicking clear button")
                self.assertIsNotNone(clear_search_field_button, "clear search field button not found")
                clear_search_field_button.click()
                sleep(2)
        except:
            pass

        self.switch_context_to_native()

    def check_if_view_on_map_button_is_present(self):

        self.switch_context_to_webview()

        logging.info("check if view on map button is present")
        view_on_map_button = self.driver.find_element(*self.configuration.EventsScreen.VIEW_ON_MAP_BUTTON)
        self.assertIsNotNone(view_on_map_button, "view on map button not found")

        self.switch_context_to_native()

    def click_view_on_map_button(self):

        self.switch_context_to_webview()

        logging.info("click view on map button is present")
        view_on_map_button = self.driver.find_element(*self.configuration.EventsScreen.VIEW_ON_MAP_BUTTON)
        self.assertIsNotNone(view_on_map_button, "view on map button not found")
        view_on_map_button.click()

        self.switch_context_to_native()
