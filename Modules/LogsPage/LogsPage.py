"""A class for methods to handle Logs Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
import logging
from time import sleep


class LogsPage(BasePage):

    def create_new_log(self):

        self.switch_context_to_webview()

        logging.info('click Create New Log button')
        create_new_log = self.driver.find_element(*self.configuration.LogsScreen.CREATE_NEW_LOG)
        self.assertIsNotNone(create_new_log, "create new log button not found")
        create_new_log.click()

        self.switch_context_to_native()

    def choose_log_type_with_all_fields(self):

        logging.info('choose log type = "log_with_all_fields" - containing all fields')
        choose_log_type = self.driver.find_element(*self.configuration.LogsScreen.LOG_TYPE_WITH_ALL_FIELDS)
        self.assertIsNotNone(choose_log_type, 'log type = "log_with_all_fields" - containing all fields not found')
        choose_log_type.click()
        sleep(1)

    def choose_log_type_with_chooser_fields(self):

        logging.info('choose log type = "log_with_chooser_fields" - containing chooser fields')
        choose_log_type = self.driver.find_element(*self.configuration.LogsScreen.LOG_TYPE_WITH_CHOOSER_FIELDS)
        self.assertIsNotNone(choose_log_type, 'log type = "log_with_chooser_fields" - containing chooser fields not found')
        choose_log_type.click()
        sleep(1)
        
    def choose_log_type_with_on_load_sequence(self):

        logging.info('choose log type = "with_on_load_sequence"')
        choose_log_type = self.driver.find_element(*self.configuration.LogsScreen.LOG_TYPE_WITH_ON_LOAD_SEQUENCE)
        self.assertIsNotNone(choose_log_type, 'log type = "with_on_create_approval_workflow" not found')
        choose_log_type.click()
        sleep(1)

    def choose_log_type_with_visibility_rules(self):

        logging.info('choose log type = "with_visibility_rules"')
        choose_log_type = self.driver.find_element(*self.configuration.LogsScreen.LOG_TYPE_WITH_VISIBILITY_RULES)
        self.assertIsNotNone(choose_log_type, 'log type = "with_visibility_rules" not found')
        choose_log_type.click()
        sleep(1)

    def click_on_lodging_agency_picker(self):

        sleep(1)
        self.switch_context_to_webview()

        sleep(1)
        logging.info("click on 'Lodging Agency' picker")
        lodging_agency_picker = self.driver.find_element(*self.configuration.LogsScreen.NEW_LOG_LODGING_AGENCY_PICKER)
        self.assertIsNotNone(lodging_agency_picker, "lodging agency picker not found")
        lodging_agency_picker.click()

        self.switch_context_to_native()

    def click_on_lodging_agency_picker_inside_created_log(self):

        sleep(1)
        self.switch_context_to_webview()

        sleep(1)
        logging.info("click on 'Lodging Agency' picker")
        lodging_agency_picker = self.driver.find_element(*self.configuration.LogsScreen.EDIT_LOG_LODGING_AGENCY_PICKER)
        self.assertIsNotNone(lodging_agency_picker, "lodging agency picker not found")
        lodging_agency_picker.click()

        self.switch_context_to_native()

    def choose_lodging_agency(self, text):

        reports_page = LoadClass.load_page('ReportsPage')
        reports_page.setDriver(self.driver)
        reports_page.choose_lodging_agency(text)

    def click_save_new_log(self):

        self.switch_context_to_webview()

        logging.info('click Save button')
        save_button = self.driver.find_element(*self.configuration.LogsScreen.SAVE_NEW_LOG)
        self.assertIsNotNone(save_button, "save button not found")
        save_button.click()

        self.switch_context_to_native()

    def click_save_edited_log(self):

        self.switch_context_to_webview()

        logging.info('click Save button')
        save_button = self.driver.find_element(*self.configuration.LogsScreen.SAVE_EDITED_LOG)
        self.assertIsNotNone(save_button, "save button not found")
        save_button.click()

        self.switch_context_to_native()

    def type_text_into_entry_field(self, text):

        # webview is not working on iOS10

        logging.info("type text into 'Entry' field")
        sleep(1)
        entry_field = self.driver.find_element(*self.configuration.LogsScreen.ENTRY_FIELD)
        entry_field.click()
        sleep(1)
        entry_field.send_keys(text)

    def expand_types_filter(self):

        self.switch_context_to_webview()

        logging.info("click to expand types filter")

        types_filter = self.driver.find_element(*self.configuration.LogsScreen.TYPES_FILTER)
        self.assertIsNotNone(types_filter, "types filter not found")
        types_filter.click()

        self.switch_context_to_native()

    def choose_first_filter(self):

        self.switch_context_to_webview()

        logging.info("choose first filter")

        first_filter = self.driver.find_element(*self.configuration.LogsScreen.FIRST_FILTER)
        self.assertIsNotNone(first_filter, "first filter not found")
        first_filter.click()

        self.switch_context_to_native()

    def choose_second_filter(self):

        self.switch_context_to_webview()

        logging.info("choose second filter")

        second_filter = self.driver.find_element(*self.configuration.LogsScreen.SECOND_FILTER)
        self.assertIsNotNone(second_filter, "second filter not found")
        second_filter.click()

        self.switch_context_to_native()

    def choose_third_filter(self):

        self.switch_context_to_webview()

        logging.info("choose third filter")

        third_filter = self.driver.find_element(*self.configuration.LogsScreen.THIRD_FILTER)
        self.assertIsNotNone(third_filter, "third filter not found")
        third_filter.click()

        self.switch_context_to_native()

    def type_text_into_search_field(self, text):

        logging.info("filter logs by search field")

        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        self.assertIsNotNone(search_field, "Search field not found")
        search_field.click()
        sleep(2)
        search_field.send_keys(text)
        sleep(1)

    def clear_Search_field(self):

        logging.info("clear search field")
        sleep(1)
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).click()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()  # each clear is clearing one character
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        sleep(1)

    def check_result(self):  # this method will search for report containing "all fields" word in title

        logging.info("check result")
        sleep(4)
        created_log = self.driver.find_elements(*self.configuration.LogsScreen.CREATED_LOG_WITH_ALL_FIELDS)
        self.assertIsNotNone(created_log[0], "Log not found")

    def open_first_log_on_the_list(self):

        self.switch_context_to_webview()

        logging.info('open first log on the list')
        edit_created_log = self.driver.find_element(*self.configuration.LogsScreen.FIRST_LOG_ON_THE_LIST)
        self.assertIsNotNone(edit_created_log, 'previously created log, not found')
        edit_created_log.click()
        sleep(2)

        self.switch_context_to_native()

        # logging.info('open first log on the list')
        # edit_created_log = self.driver.find_elements(*self.configuration.LogsScreen.CREATED_REPORT_WITH_ALL_FIELDS)
        # self.assertIsNotNone(edit_created_log, 'previously created log, not found')
        # edit_created_log[0].click()
        # sleep(2)

    def click_more_button(self):

        self.switch_context_to_webview()

        logging.info("click more button")
        click_more_button = self.driver.find_element(*self.configuration.LogsScreen.MORE_BUTTON)
        self.assertIsNotNone(click_more_button, "More button not found")
        click_more_button.click()

        self.switch_context_to_native()

    def click_delete_log(self):

        self.switch_context_to_webview()

        logging.info("click delete log")
        click_delete_log = self.driver.find_element(*self.configuration.LogsScreen.DELETE_LOG)
        self.assertIsNotNone(click_delete_log, "Delete log button not found")
        click_delete_log.click()

        self.switch_context_to_native()

    def alert_accept_delete(self):

        self.switch_context_to_webview()

        logging.info("alert accept delete")
        alert_accept_delete = self.driver.find_element(*self.configuration.LogsScreen.DELETE_ALERT)
        self.assertIsNotNone(alert_accept_delete, "Delete button on alert not found")
        alert_accept_delete.click()

        self.switch_context_to_native()

    def click_edit_button(self):

        self.switch_context_to_webview()

        logging.info("click edit button")

        edit = self.driver.find_element(*self.configuration.LogsScreen.EDIT_BUTTON)
        self.assertIsNotNone(edit, "edit button not found")
        edit.click()
        sleep(2)

        self.switch_context_to_native()
        
    def click_event_chooser_field(self):
        
        self.switch_context_to_webview()

        logging.info("click event chooser field")

        click_event_chooser_field = self.driver.find_element(*self.configuration.LogsScreen.EVENT_CHOOSER_FIELD)
        self.assertIsNotNone(click_event_chooser_field, "event chooser field not found")
        click_event_chooser_field.click()
        sleep(2)

        self.switch_context_to_native()

    def click_asset_chooser_field(self):
        
        self.switch_context_to_webview()

        logging.info("click asset chooser field")

        click_asset_chooser_field = self.driver.find_element(*self.configuration.LogsScreen.ASSET_CHOOSER_FIELD)
        self.assertIsNotNone(click_asset_chooser_field, "asset chooser field not found")
        click_asset_chooser_field.click()
        sleep(2)

        self.switch_context_to_native()

    def choose_first_event_on_the_list(self):
        
        self.switch_context_to_webview()

        logging.info("choose first event on the list")

        choose_first_event_on_the_list = self.driver.find_element(*self.configuration.LogsScreen.FIRST_EVENT_ON_THE_LIST)
        self.assertIsNotNone(choose_first_event_on_the_list, "event not found")
        choose_first_event_on_the_list.click()
        sleep(2)

        self.switch_context_to_native()

    def choose_first_asset_on_the_list(self):

        self.switch_context_to_webview()

        logging.info("choose first asset on the list")

        choose_first_asset_on_the_list = self.driver.find_element(*self.configuration.LogsScreen.FIRST_ASSET_ON_THE_LIST)
        self.assertIsNotNone(choose_first_asset_on_the_list, "asset not found")
        choose_first_asset_on_the_list.click()
        sleep(2)

        self.switch_context_to_native()

    def click_log_chooser_field(self):

        sleep(2)
        self.switch_context_to_webview()

        logging.info("click log chooser field")
        log_chooser_field = self.driver.find_element(*self.configuration.LogsScreen.LOG_CHOOSER_FIELD)  # inside existing log
        self.assertIsNotNone(log_chooser_field, "log chooser field not found")
        log_chooser_field.click()
        sleep(1)

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

    def choose_log_from_the_list(self):

        self.switch_context_to_webview()

        logging.info("choose first log on the list")

        choose_first_log = self.driver.find_element(*self.configuration.LogsScreen.PREVIOUSLY_CREATED_LOG_CHECKBOX)
        self.assertIsNotNone(choose_first_log, "first log on the list not found")
        choose_first_log.click()
        sleep(2)

        self.switch_context_to_native()

    def check_on_load_and_on_save_sequences(self):

        self.switch_context_to_webview()

        logging.info("assert on load and on save sequence")
        sequence_on_load = self.driver.find_element(*self.configuration.LogsScreen.SEQUENCE_ON_LOAD)
        self.assertIsNotNone(sequence_on_load)

        sequence_on_save = self.driver.find_element(*self.configuration.LogsScreen.SEQUENCE_ON_SAVE)
        self.assertIsNotNone(sequence_on_save)

        self.switch_context_to_native()

        sleep(1)
        sequence_on_load_value = self.driver.find_element(*self.configuration.EventEditScreen.SEQUENCE_ONLOAD_VALUE)
        self.assertIsNotNone(sequence_on_load_value)

        # sequence_on_save_value = self.driver.find_element(*self.configuration.EventEditScreen.SEQUENCE_ONSAVE_VALUE)
        # self.assertIsNotNone(sequence_on_save_value)

    def click_cancel_new_log(self):

        self.switch_context_to_webview()

        logging.info("click Cancel button")
        cancel_button = self.driver.find_element(*self.configuration.LogsScreen.CANCEL_BUTTON)  # cancel button for new log
        self.assertIsNotNone(cancel_button, "Cancel button was not found")
        cancel_button.click()
        sleep(2)

        self.switch_context_to_native()

    def click_on_option_list(self):

        self.switch_context_to_webview()

        logging.info("click on Option list")
        option_list = self.driver.find_element(*self.configuration.LogsScreen.OPTION_LIST)
        self.assertIsNotNone(option_list, "option list not found")
        option_list.click()

        self.switch_context_to_native()

    def click_on_option_1(self):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.click_on_option_1()

    def click_on_option_2(self):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.click_on_option_2()

    def click_on_option_3(self):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.click_on_option_3()

    def check_restored_field_1(self):

        logging.info("assert restored field 1")

        self.switch_context_to_webview()

        field_to_restore_1_header = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_1_HEADER)
        self.assertIsNotNone(field_to_restore_1_header)

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

        field_to_restore_1_value = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_1_VALUE)
        self.assertIsNotNone(field_to_restore_1_value)

    def check_restored_field_2(self):

        logging.info("assert restored field 2")

        self.switch_context_to_webview()

        field_to_restore_2_header = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_2_HEADER)
        self.assertIsNotNone(field_to_restore_2_header)

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

        field_to_restore_2_value = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_2_VALUE)
        self.assertIsNotNone(field_to_restore_2_value)

    def check_restored_field_3(self):

        logging.info("assert restored field 3")

        self.switch_context_to_webview()

        field_to_restore_3_header = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_3_HEADER)
        self.assertIsNotNone(field_to_restore_3_header)

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

        field_to_restore_3_value = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_3_VALUE)
        self.assertIsNotNone(field_to_restore_3_value)

    def check_hidden_field_1(self):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.check_hidden_field_1()

    def check_hidden_fields_1_and_2(self):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.check_hidden_fields_1_and_2()

