"""A class for methods to handle Reports Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
import logging
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


class ReportsPage(BasePage):

    def type_title(self, text):

        self.switch_context_to_webview()

        logging.info("type title")
        title = self.driver.find_element(*self.configuration.ReportsScreen.TITLE)
        self.assertIsNotNone(title, "Title input field was not found")
        title.click()
        title.send_keys(text)

        self.switch_context_to_native()

        # new_task_page = LoadClass.load_page('NewTaskPage')
        # new_task_page.setDriver(self.driver)
        # new_task_page.type_title(text)

    def click_on_lodging_agency_picker(self):

        # self.switch_context_to_webview()
        #
        # logging.info("click on 'Lodging Agency' picker")
        # lodging_agency_picker = self.driver.find_element(*self.configuration.ReportsScreen.LODGING_AGENCY_PICKER)
        # self.assertIsNotNone(lodging_agency_picker, "Lodging Agency picker was not found")
        # sleep(1)
        # lodging_agency_picker.click()
        # sleep(2)
        #
        # self.switch_context_to_native()

        sleep(5)
        logging.info("click on 'Lodging Agency' picker")
        try:
            lodging_agency_picker = self.driver.find_element(*self.configuration.ReportsScreen.LODGING_AGENCY_PICKER)
        except NoSuchElementException:
            lodging_agency_picker = self.driver.find_element(*self.configuration.ReportsScreen.LODGING_AGENCY_PICKER2)
        self.assertIsNotNone(lodging_agency_picker, "Lodging Agency picker was not found")
        action = TouchAction(self.driver)
        action.tap(element=lodging_agency_picker, count=1).perform()
        sleep(1)

    def click_publish_new_report(self):

        self.switch_context_to_webview()

        logging.info("click Publish button")
        publish_button = self.driver.find_element(*self.configuration.ReportsScreen.PUBLISH_NEW_REPORT)
        self.assertIsNotNone(publish_button, "Publish button was not found")
        publish_button.click()
        # sleep(1)
        # action = TouchAction(self.driver)
        # action.tap(element=publish_button, count=1).perform()
        sleep(2)
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located(self.configuration.MainMenuScreen.EVENTS_BUTTON),
            "Failed to locate description field")

        self.switch_context_to_native()

    def click_cancel_new_report(self):

        self.switch_context_to_webview()

        logging.info("click Cancel button")
        cancel_button = self.driver.find_element(*self.configuration.ReportsScreen.CANCEL_NEW_REPORT)
        self.assertIsNotNone(cancel_button, "Cancel button was not found")
        cancel_button.click()
        sleep(2)

        self.switch_context_to_native()

    def click_publish_edited_report(self):

        self.switch_context_to_webview()

        logging.info("click Publish button")
        publish_button = self.driver.find_element(*self.configuration.ReportsScreen.PUBLISH_EDITED_REPORT)
        self.assertIsNotNone(publish_button, "Publish button was not found")
        publish_button.click()
        # sleep(1)
        # action = TouchAction(self.driver)
        # action.tap(element=publish_button, count=1).perform()
        sleep(2)
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located(self.configuration.MainMenuScreen.EVENTS_BUTTON),
            "Failed to locate description field")

        self.switch_context_to_native()

    def click_cancel_edited_report(self):

        self.switch_context_to_webview()

        logging.info("click Cancel button")
        cancel_button = self.driver.find_element(*self.configuration.ReportsScreen.CANCEL_EDITED_REPORT)
        self.assertIsNotNone(cancel_button, "Cancel button was not found")
        cancel_button.click()
        sleep(2)

        self.switch_context_to_native()

    def filter_reports_by_type(self):

        self.switch_context_to_webview()

        logging.info("filter reports by type")

        expand_type_filters = self.driver.find_element(*self.configuration.ReportsScreen.TYPE_FILTER)
        expand_type_filters.click()

        choose_second_type = self.driver.find_element(*self.configuration.ReportsScreen.SECOND_TYPE)
        choose_second_type.click()
        sleep(1)

        expand_type_filters = self.driver.find_element(*self.configuration.ReportsScreen.TYPE_FILTER)
        expand_type_filters.click()

        choose_third_type = self.driver.find_element(*self.configuration.ReportsScreen.THIRD_TYPE)
        choose_third_type.click()
        sleep(1)

        expand_type_filters = self.driver.find_element(*self.configuration.ReportsScreen.TYPE_FILTER)
        expand_type_filters.click()

        choose_fourth_type = self.driver.find_element(*self.configuration.ReportsScreen.FOURTH_TYPE)
        choose_fourth_type.click()
        sleep(1)

        expand_type_filters = self.driver.find_element(*self.configuration.ReportsScreen.TYPE_FILTER)
        expand_type_filters.click()

        choose_first_type = self.driver.find_element(*self.configuration.ReportsScreen.FIRST_TYPE)
        choose_first_type.click()
        sleep(1)

        self.switch_context_to_native()
    
    def filter_reports_by_status(self):

        self.switch_context_to_webview()

        logging.info("filter reports by status")

        expand_status_filters = self.driver.find_element(*self.configuration.ReportsScreen.STATUS_FILTER)
        expand_status_filters.click()

        choose_second_status = self.driver.find_element(*self.configuration.ReportsScreen.SECOND_STATUS)
        choose_second_status.click()
        sleep(1)

        expand_status_filters = self.driver.find_element(*self.configuration.ReportsScreen.STATUS_FILTER)
        expand_status_filters.click()

        choose_third_status = self.driver.find_element(*self.configuration.ReportsScreen.THIRD_STATUS)
        choose_third_status.click()
        sleep(1)

        expand_status_filters = self.driver.find_element(*self.configuration.ReportsScreen.STATUS_FILTER)
        expand_status_filters.click()

        choose_fourth_status = self.driver.find_element(*self.configuration.ReportsScreen.FOURTH_STATUS)
        choose_fourth_status.click()
        sleep(1)

        expand_status_filters = self.driver.find_element(*self.configuration.ReportsScreen.STATUS_FILTER)
        expand_status_filters.click()

        choose_first_status = self.driver.find_element(*self.configuration.ReportsScreen.FIRST_STATUS)
        choose_first_status.click()
        sleep(1)

        self.switch_context_to_native()

    def filter_reports_by_active_status(self):

        self.switch_context_to_webview()

        logging.info("filter reports by active status")

        expand_status_filters = self.driver.find_element(*self.configuration.ReportsScreen.STATUS_FILTER)
        expand_status_filters.click()

        choose_second_status = self.driver.find_element(*self.configuration.ReportsScreen.SECOND_STATUS)
        choose_second_status.click()
        sleep(1)

        self.switch_context_to_native()

    def type_text_into_search_field(self):

        logging.info("filter reports by search field")

        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        self.assertIsNotNone(search_field, "Search field not found")
        search_field.click()
        sleep(2)
        search_field.send_keys("Large")
        sleep(1)

    def search_for_report_with_chooser_fields(self):

        logging.info("filter reports using search field to find report with chooser fields")

        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        self.assertIsNotNone(search_field, "Search field not found")
        search_field.click()
        sleep(2)
        search_field.send_keys("chooser fields")
        sleep(1)

    def check_result(self):  # this method will search for report containing "Large" word in title

        logging.info("check result")
        sleep(1)
        created_report = self.driver.find_elements(*self.configuration.ReportsScreen.CREATED_REPORT_WITH_ALL_FIELDS)
        self.assertIsNotNone(created_report[1], "Report not found")

    def clear_Search_field(self):

        logging.info("clear search field")
        sleep(1)
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).click()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()  # each clear is clearing one character
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
        sleep(1)

    def click_create_report_button(self):

        self.switch_context_to_webview()

        logging.info("click create report button")
        create_report = self.driver.find_element(*self.configuration.ReportsScreen.CREATE_REPORT_BUTTON)
        create_report.click()

        self.switch_context_to_native()

    def choose_report_type_with_all_fields(self):

        logging.info('choose report type = "report_for_tests" - containing all fields')
        choose_report_type = self.driver.find_element(*self.configuration.ReportsScreen.REPORT_TYPE_WITH_ALL_FIELDS)
        self.assertIsNotNone(choose_report_type, 'report type = "report_for_tests" - containing all fields not found')
        choose_report_type.click()
        sleep(1)

    def choose_report_type_with_chooser_fields(self):

        logging.info('choose report type = "report_with_chooser_fields" - containing chooser fields')
        choose_report_type = self.driver.find_element(*self.configuration.ReportsScreen.REPORT_TYPE_WITH_CHOOSER_FIELDS)
        self.assertIsNotNone(choose_report_type, 'choose report type = "report_with_chooser_fields" - containing chooser fields not found')
        choose_report_type.click()
        sleep(1)

    def choose_report_type_with_on_create_approval_workflow(self):

        logging.info('choose report type = "with_on_create_approval_workflow"')
        choose_report_type = self.driver.find_element(*self.configuration.ReportsScreen.REPORT_TYPE_WITH_ON_CREATE_APPROVAL_WORKFLOW)
        self.assertIsNotNone(choose_report_type, 'report type = "with_on_create_approval_workflow" not found')
        choose_report_type.click()
        sleep(1)

    def choose_report_type_with_on_load_sequence(self):

        logging.info('choose report type = "with_on_load_sequence"')
        choose_report_type = self.driver.find_element(*self.configuration.ReportsScreen.REPORT_TYPE_WITH_ON_LOAD_SEQUENCE)
        self.assertIsNotNone(choose_report_type, 'report type = "with_on_create_approval_workflow" not found')
        choose_report_type.click()
        sleep(1)

    def choose_report_type_with_visibility_rules(self):

        logging.info('choose report type = "with visibility rules"')
        choose_report_type = self.driver.find_element(*self.configuration.ReportsScreen.REPORT_TYPE_WITH_VISIBILITY_RULES)
        self.assertIsNotNone(choose_report_type, 'report type = "with visibility rules" not found')
        choose_report_type.click()
        sleep(1)

    def edit_created_report_with_all_fields(self):

        logging.info('edit created report, containing word "Large"')
        edit_created_report = self.driver.find_elements(*self.configuration.ReportsScreen.CREATED_REPORT_WITH_ALL_FIELDS)
        self.assertIsNotNone(edit_created_report, 'previously created report containing word "Large", not found')
        edit_created_report[0].click()
        sleep(2)

    def edit_created_report_with_chooser_fields(self):

        logging.info('edit created report, containing words "chooser fields"')
        edit_created_report = self.driver.find_elements(*self.configuration.ReportsScreen.CREATED_REPORT_WITH_CHOOSER_FIELDS)
        self.assertIsNotNone(edit_created_report, 'previously created report, containing words "chooser fields", not found')
        edit_created_report[0].click()
        sleep(2)

    def edit_first_report_on_the_list(self):

        self.switch_context_to_webview()

        logging.info('edit first report on the list')
        edit_created_report = self.driver.find_elements(*self.configuration.ReportsScreen.FIRST_REPORT_ON_THE_LIST)
        self.assertIsNotNone(edit_created_report, 'previously created report, not found')
        edit_created_report[0].click()
        sleep(2)

        self.switch_context_to_native()

    def click_edit_button(self):

        self.switch_context_to_webview()

        logging.info("click edit button")

        edit = self.driver.find_element(*self.configuration.ReportsScreen.EDIT_BUTTON)
        self.assertIsNotNone(edit, "edit button not found")
        edit.click()
        sleep(2)

        self.switch_context_to_native()

    def open_existing_report(self):

        self.switch_context_to_webview()

        logging.info("open first report on the list")

        open_existing_report = self.driver.find_element(*self.configuration.ReportsScreen.FIRST_REPORT_ON_THE_LIST)
        self.assertIsNotNone(open_existing_report, "existing report not found")
        open_existing_report.click()
        sleep(1)

        self.switch_context_to_native()

    def click_more_button(self):

        self.switch_context_to_webview()

        logging.info("click more button")
        click_more_button = self.driver.find_element(*self.configuration.ReportsScreen.MORE_BUTTON)
        self.assertIsNotNone(click_more_button, "More button not found")
        click_more_button.click()

        self.switch_context_to_native()

    def click_delete_report(self):

        self.switch_context_to_webview()

        logging.info("click delete report")
        click_delete_report = self.driver.find_element(*self.configuration.ReportsScreen.DELETE_REPORT)
        self.assertIsNotNone(click_delete_report, "Delete report button not found")
        click_delete_report.click()

        self.switch_context_to_native()

    def alert_accept_delete(self):

        self.switch_context_to_webview()

        logging.info("alert accept delete")
        alert_accept_delete = self.driver.find_element(*self.configuration.ReportsScreen.DELETE_ALERT)
        self.assertIsNotNone(alert_accept_delete, "Delete button on alert not found")
        alert_accept_delete.click()

        self.switch_context_to_native()

    def edit_report_title(self, text):

        self.switch_context_to_webview()

        logging.info("type title")
        title = self.driver.find_element(*self.configuration.ReportsScreen.EDIT_REPORT_TITLE)
        self.assertIsNotNone(title, "Title input field was not found")
        title.click()
        title.send_keys(text)

        self.switch_context_to_native()

    def click_assets_chooser_field(self):

        self.switch_context_to_webview()

        logging.info("click assets chooser field")
        assets_chooser_field = self.driver.find_element(*self.configuration.ReportsScreen.ASSETS_CHOOSER_FIELD)
        assets_chooser_field.click()
        sleep(2)

        self.switch_context_to_native()

    def choose_asset_from_the_list(self):

        self.switch_context_to_webview()

        logging.info("choose first asset on the list")

        choose_first_asset = self.driver.find_element(*self.configuration.AssetsScreen.PREVIOUSLY_CREATED_ASSET_CHECKBOX)
        self.assertIsNotNone(choose_first_asset, "first asset on the list not found")
        choose_first_asset.click()
        sleep(2)

        self.switch_context_to_native()

    def create_mapping_data(self):

        self.switch_context_to_webview()

        logging.info("click create mapping data")
        create_mapping_data = self.driver.find_element(*self.configuration.ReportsScreen.CREATE_MAPPING_DATA)
        self.assertIsNotNone(create_mapping_data, "create mapping data button not found")
        create_mapping_data.click()

        self.switch_context_to_native()
        sleep(2)

    def check_on_load_and_on_save_sequences(self):

        self.switch_context_to_webview()

        logging.info("assert on load and on save sequence")
        sequence_on_load = self.driver.find_element(*self.configuration.ReportsScreen.SEQUENCE_ON_LOAD)
        self.assertIsNotNone(sequence_on_load)

        sequence_on_save = self.driver.find_element(*self.configuration.ReportsScreen.SEQUENCE_ON_SAVE)
        self.assertIsNotNone(sequence_on_save)

        self.switch_context_to_native()

        sequence_on_load_value = self.driver.find_element(*self.configuration.EventEditScreen.SEQUENCE_ONLOAD_VALUE)
        self.assertIsNotNone(sequence_on_load_value)

        sequence_on_save_value = self.driver.find_element(*self.configuration.EventEditScreen.SEQUENCE_ONSAVE_VALUE)
        self.assertIsNotNone(sequence_on_save_value)

    def click_on_option_list(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.click_on_option_list()

    def click_on_option_1(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.click_on_option_1()

    def click_on_option_2(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.click_on_option_2()

    def click_on_option_3(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.click_on_option_3()

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

    def check_restored_field_3(self):

        logging.info("assert restored field 3")
        field_to_restore_3_header = self.driver.find_element(*self.configuration.EventEditScreen.
                                                             FIELD_TO_RESTORE_3_HEADER)
        self.assertIsNotNone(field_to_restore_3_header)

        field_to_restore_3_value = self.driver.find_element(*self.configuration.EventEditScreen.
                                                            FIELD_TO_RESTORE_3_VALUE)
        self.assertIsNotNone(field_to_restore_3_value)

    def check_hidden_field_1(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.check_hidden_field_1()

    def check_hidden_fields_1_and_2(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.check_hidden_fields_1_and_2()

