"""A class for methods to handle Reports Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
import logging
from time import sleep
# from appium.webdriver.common.touch_action import TouchAction
# # from selenium.webdriver.support import expected_conditions
# # from selenium.webdriver.support.ui import WebDriverWait
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

    def type_title_for_edited_report(self, text):

        self.switch_context_to_webview()

        sleep(1)
        logging.info("type Title")
        name = self.driver.find_element(*self.configuration.ReportsScreen.TITLE_EDITED)
        self.assertIsNotNone(name, "Title input field was not found")
        name.click()
        name.send_keys(text)

        self.switch_context_to_native()

    def type_title_offline(self, text):

        self.switch_context_to_webview()

        logging.info("type title")
        title = self.driver.find_element(*self.configuration.ReportsScreen.TITLE)
        self.assertIsNotNone(title, "Title input field was not found")
        title.click()
        title.send_keys(text)

        self.switch_context_to_native()

    def type_text_into_media_release_field(self):

        # self.switch_context_to_webview()

        logging.info("type text")
        media_release_field = self.driver.find_element(*self.configuration.ReportsScreen.MEDIA_RELEASE_FIELD)
        self.assertIsNotNone(media_release_field, "Media release input field was not found")
        media_release_field.click()
        media_release_field.send_keys("text")

        # self.switch_context_to_native()

    def click_on_lodging_agency_picker(self):

        sleep(1)
        self.switch_context_to_webview()

        sleep(1)
        logging.info("click on 'Lodging Agency' picker")
        lodging_agency_picker = self.driver.find_element(*self.configuration.ReportsScreen.NEW_REPORT_LODGING_AGENCY_PICKER)
        self.assertIsNotNone(lodging_agency_picker, "lodging agency picker not found")
        lodging_agency_picker.click()

        self.switch_context_to_native()

    def click_on_lodging_agency_picker_inside_created_report(self):

        sleep(1)
        self.switch_context_to_webview()

        sleep(1)
        logging.info("click on 'Lodging Agency' picker")
        lodging_agency_picker = self.driver.find_element(*self.configuration.ReportsScreen.EDIT_REPORT_LODGING_AGENCY_PICKER)
        self.assertIsNotNone(lodging_agency_picker, "lodging agency picker not found")
        lodging_agency_picker.click()

        self.switch_context_to_native()

    def click_publish_new_report(self):

        self.switch_context_to_webview()

        try:
            logging.info("click Publish button")
            publish_button = self.driver.find_element(*self.configuration.ReportsScreen.PUBLISH_NEW_REPORT)
            self.assertIsNotNone(publish_button, "Publish button was not found")
            publish_button.click()
        except NoSuchElementException and WebDriverException:  # for IOS emulators in offline mode
            ReportsPage.click_publish_edited_report(self)

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

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

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
        self.assertIsNotNone(expand_type_filters, "type filter not found")
        expand_type_filters.click()

        choose_second_type = self.driver.find_element(*self.configuration.ReportsScreen.SECOND_TYPE)
        self.assertIsNotNone(choose_second_type, "second status not found")
        choose_second_type.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

        self.switch_context_to_webview()

        expand_type_filters = self.driver.find_element(*self.configuration.ReportsScreen.TYPE_FILTER)
        self.assertIsNotNone(expand_type_filters, "type filter not found")
        expand_type_filters.click()

        choose_third_type = self.driver.find_element(*self.configuration.ReportsScreen.THIRD_TYPE)
        self.assertIsNotNone(choose_third_type, "third status not found")
        choose_third_type.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

        self.switch_context_to_webview()

        expand_type_filters = self.driver.find_element(*self.configuration.ReportsScreen.TYPE_FILTER)
        self.assertIsNotNone(expand_type_filters, "type filter not found")
        expand_type_filters.click()

        choose_fourth_type = self.driver.find_element(*self.configuration.ReportsScreen.FOURTH_TYPE)
        self.assertIsNotNone(choose_fourth_type, "fourth status not found")
        choose_fourth_type.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

        self.switch_context_to_webview()

        expand_type_filters = self.driver.find_element(*self.configuration.ReportsScreen.TYPE_FILTER)
        self.assertIsNotNone(expand_type_filters, "type filter not found")
        expand_type_filters.click()

        choose_first_type = self.driver.find_element(*self.configuration.ReportsScreen.FIRST_TYPE)
        self.assertIsNotNone(choose_first_type, "first status not found")
        choose_first_type.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()
    
    def filter_reports_by_status(self):

        self.switch_context_to_webview()

        logging.info("filter reports by status")

        expand_status_filters = self.driver.find_element(*self.configuration.ReportsScreen.STATUS_FILTER)
        self.assertIsNotNone(expand_status_filters, "status filter not found")
        expand_status_filters.click()

        choose_second_status = self.driver.find_element(*self.configuration.ReportsScreen.SECOND_STATUS)
        self.assertIsNotNone(choose_second_status, "second status not found")
        choose_second_status.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

        self.switch_context_to_webview()

        expand_status_filters = self.driver.find_element(*self.configuration.ReportsScreen.STATUS_FILTER)
        self.assertIsNotNone(expand_status_filters, "status filter not found")
        expand_status_filters.click()

        choose_third_status = self.driver.find_element(*self.configuration.ReportsScreen.THIRD_STATUS)
        self.assertIsNotNone(choose_third_status, "third status not found")
        choose_third_status.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

        self.switch_context_to_webview()

        expand_status_filters = self.driver.find_element(*self.configuration.ReportsScreen.STATUS_FILTER)
        self.assertIsNotNone(expand_status_filters, "status filter not found")
        expand_status_filters.click()

        choose_fourth_status = self.driver.find_element(*self.configuration.ReportsScreen.FOURTH_STATUS)
        self.assertIsNotNone(choose_fourth_status, "fourth status not found")
        choose_fourth_status.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

        self.switch_context_to_webview()

        expand_status_filters = self.driver.find_element(*self.configuration.ReportsScreen.STATUS_FILTER)
        self.assertIsNotNone(expand_status_filters, "status filter not found")
        expand_status_filters.click()

        choose_first_status = self.driver.find_element(*self.configuration.ReportsScreen.FIRST_STATUS)
        self.assertIsNotNone(choose_first_status, "first status not found")
        choose_first_status.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

        # self.switch_context_to_native()

    def filter_reports_by_active_status(self):

        self.switch_context_to_webview()

        logging.info("filter reports by active status")

        expand_status_filters = self.driver.find_element(*self.configuration.ReportsScreen.STATUS_FILTER)
        self.assertIsNotNone(expand_status_filters, "status filter not found")
        expand_status_filters.click()

        choose_second_status = self.driver.find_element(*self.configuration.ReportsScreen.SECOND_STATUS)
        self.assertIsNotNone(choose_second_status, "second status not found")
        choose_second_status.click()
        sleep(1)

        self.switch_context_to_native()

    def filter_reports_by_any_status(self):

        self.switch_context_to_webview()

        logging.info("filter reports by any status")

        expand_status_filters = self.driver.find_element(*self.configuration.ReportsScreen.STATUS_FILTER)
        self.assertIsNotNone(expand_status_filters, "status filter not found")
        expand_status_filters.click()

        choose_second_status = self.driver.find_element(*self.configuration.ReportsScreen.FIRST_STATUS)
        self.assertIsNotNone(choose_second_status, "second status not found")
        choose_second_status.click()
        sleep(1)

        self.switch_context_to_native()

    def type_text_into_search_field(self, text):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.type_text_into_search_field(text)

        # logging.info("filter reports by search field")
        #
        # search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        # self.assertIsNotNone(search_field, "Search field not found")
        # search_field.click()
        # sleep(2)
        # search_field.send_keys(text)
        # sleep(1)
    #
    # def search_for_report_with_chooser_fields(self):
    #
    #     logging.info("filter reports using search field to find report with chooser fields")
    #
    #     search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
    #     self.assertIsNotNone(search_field, "Search field not found")
    #     search_field.click()
    #     sleep(2)
    #     search_field.send_keys("chooser fields")
    #     sleep(1)
    #
    # def search_for_report_with_assigned_question(self):
    #
    #     logging.info("filter reports using search field to find report with assigned question")
    #
    #     search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
    #     self.assertIsNotNone(search_field, "Search field not found")
    #     search_field.click()
    #     sleep(2)
    #     search_field.send_keys("Report with approval")
    #     sleep(1)

    def check_result(self):  # this method will search for report containing "Large" word in title

        logging.info("check result")
        sleep(1)
        created_report = self.driver.find_elements(*self.configuration.ReportsScreen.CREATED_REPORT_WITH_ALL_FIELDS)
        # self.assertIsNotNone(created_report[1], "Report not found")
        self.assertIsNotNone(created_report[0], "Report not found")

    # def clear_Search_field(self):
    #
    #     logging.info("clear search field")
    #     sleep(1)
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).click()
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()  # each clear is clearing one character
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
    #     self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD).clear()
    #     sleep(1)

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

    def choose_report_type_with_assigned_question(self):

        logging.info('choose report type = "with_assigned_question"')
        choose_report_type = self.driver.find_element(*self.configuration.ReportsScreen.REPORT_TYPE_WITH_ASSIGNED_QUESTION)
        self.assertIsNotNone(choose_report_type, 'report type = "with_assigned_question" not found')
        choose_report_type.click()
        sleep(1)

    def choose_report_type_with_option_list(self):

        logging.info('choose report type = "with_option_list"')
        choose_report_type = self.driver.find_element(*self.configuration.ReportsScreen.REPORT_TYPE_WITH_OPTION_LIST)
        self.assertIsNotNone(choose_report_type, 'report type = "with_option_list" not found')
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

    def edit_created_report_with_assigned_question(self):

        logging.info('edit created report, containing words "assigned question"')
        sleep(1)
        edit_created_report = self.driver.find_elements(*self.configuration.ReportsScreen.CREATED_REPORT_WITH_ASSIGNED_QUESTION)
        self.assertIsNotNone(edit_created_report, 'previously created report, containing words "chooser fieldsassigned question", not found')
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

    def open_first_pending_report(self):    # pending report in offline mode

        self.switch_context_to_webview()

        try:  # appium can't enable airplane mode on IOS emulators
            logging.info("open first pending report on the list")
            first_pending_report = self.driver.find_element(*self.configuration.ReportsScreen.FIRST_PENDING_REPORT)
            self.assertIsNotNone(first_pending_report, "first pending report not found")
            first_pending_report.click()
        except NoSuchElementException:
            ReportsPage.open_existing_report(self)

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

        sleep(1)
        self.switch_context_to_webview()

        logging.info("click assets chooser field")
        assets_chooser_field = self.driver.find_element(*self.configuration.ReportsScreen.ASSETS_CHOOSER_FIELD)
        self.assertIsNotNone(assets_chooser_field, "assets chooser field not found")
        assets_chooser_field.click()
        sleep(1)

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

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
        self.assertIsNotNone(sequence_on_load, "on load sequence not found")

        sequence_on_save = self.driver.find_element(*self.configuration.ReportsScreen.SEQUENCE_ON_SAVE)
        self.assertIsNotNone(sequence_on_save, "on save sequence not found")

        self.switch_context_to_native()

        sequence_on_load_value = self.driver.find_element(*self.configuration.EventEditScreen.SEQUENCE_ONLOAD_VALUE)
        self.assertIsNotNone(sequence_on_load_value, "on load sequence value not found")

        sequence_on_save_value = self.driver.find_element(*self.configuration.EventEditScreen.SEQUENCE_ONSAVE_VALUE)
        self.assertIsNotNone(sequence_on_save_value, "on save sequence value not found")

    def click_on_option_list(self):

        self.switch_context_to_webview()

        logging.info("click on Option list")
        option_list = self.driver.find_element(*self.configuration.ReportsScreen.OPTION_LIST)
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

        sleep(2)
        field_to_restore_1_value = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_1_VALUE)
        self.assertIsNotNone(field_to_restore_1_value, "field to restore 1 value not found")
        # field1 = self.driver.find_element_by_css_selector('div#reportNew>div.ui-content>ul>li.ui-field-contain.ui-li-static.ui-body-inherit>div.ui-input-text>input[id="field to restore"]')
        # field1.click()
        # print(field1.text)
        # self.assertEqual(field1.text, "value for field 1", "value for restored field not found")

        # assets_page = LoadClass.load_page('AssetsPage')
        # assets_page.setDriver(self.driver)
        # assets_page.check_restored_field_1()

    def check_restored_field_2(self):

        logging.info("assert restored field 2")

        self.switch_context_to_webview()

        field_to_restore_2_header = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_2_HEADER)
        self.assertIsNotNone(field_to_restore_2_header)

        self.switch_context_to_native()

        # common_page = LoadClass.load_page('CommonPage')
        # common_page.setDriver(self.driver)
        # common_page.scroll_down_one_view()

        sleep(1)
        field_to_restore_2_value = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_2_VALUE)
        self.assertIsNotNone(field_to_restore_2_value, "field to restore 2 value not found")

        # assets_page = LoadClass.load_page('AssetsPage')
        # assets_page.setDriver(self.driver)
        # assets_page.check_restored_field_2()

    def check_restored_field_3(self):

        logging.info("assert restored field 3")

        self.switch_context_to_webview()

        field_to_restore_3_header = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_3_HEADER)
        self.assertIsNotNone(field_to_restore_3_header)

        self.switch_context_to_native()

        # common_page = LoadClass.load_page('CommonPage')
        # common_page.setDriver(self.driver)
        # common_page.scroll_down_one_view()

        sleep(1)
        field_to_restore_3_value = self.driver.find_element(*self.configuration.EventEditScreen.FIELD_TO_RESTORE_3_VALUE)
        self.assertIsNotNone(field_to_restore_3_value, "field to restore 3 value not found")

        # assets_page = LoadClass.load_page('AssetsPage')
        # assets_page.setDriver(self.driver)
        # assets_page.check_restored_field_3()

    def check_hidden_field_1(self):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.check_hidden_field_1()

    def check_hidden_fields_1_and_2(self):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.check_hidden_fields_1_and_2()

    def clear_Search_field(self):

        self.switch_context_to_webview()

        try:
            clear_search_field_button = self.driver.find_element(*self.configuration.ReportsScreen.CLEAR_SEARCH_FIELD_BUTTON)
            if clear_search_field_button.is_displayed():
                logging.info("clear Search field by clicking clear button")
                self.assertIsNotNone(clear_search_field_button, "clear search field button not found")
                clear_search_field_button.click()
                sleep(2)
        except NoSuchElementException:
            pass

        self.switch_context_to_native()

    def check_if_view_on_map_button_is_present(self):

        self.switch_context_to_webview()

        logging.info("check if view on map button is present")
        view_on_map_button = self.driver.find_element(*self.configuration.ReportsScreen.VIEW_ON_MAP_BUTTON)
        self.assertIsNotNone(view_on_map_button, "view on map button not found")

        self.switch_context_to_native()

    def ok_button_on_offline_notification_popup(self):

        self.switch_context_to_webview()

        logging.info("click Ok button on offline notification popup")
        try:
            ok_button = self.driver.find_element(*self.configuration.ReportsScreen.OK_BUTTON_ON_OFFLINE_NOTIFICATION_POPUP)
            self.assertIsNotNone(ok_button, "ok button not found")
            ok_button.click()
        except NoSuchElementException:
            logging.warning("offline notification popup not present")
        sleep(1)

        self.switch_context_to_native()

    def check_notification_about_offline_mode(self):

        events_page = LoadClass.load_page('EventsPage')
        events_page.setDriver(self.driver)
        events_page.check_notification_about_offline_mode()

    def read_only_option_list(self):

        self.switch_context_to_webview()

        logging.info("click option list - Is Read Only ?")

        try:
            option_list = self.driver.find_element(*self.configuration.ReportsScreen.OPTION_LIST_READ_ONLY)
            if option_list.is_displayed():
                self.assertIsNotNone(option_list, "option list - Is Read Only ?, not found")
                option_list.click()
            else:
                raise ValueError("element not displayed")
        except NoSuchElementException and ValueError:
            option_list = self.driver.find_element(*self.configuration.ReportsScreen.OPTION_LIST_READ_ONLY_EDIT)
            if option_list.is_displayed():
                self.assertIsNotNone(option_list, "option list - Is Read Only ?, not found")
                option_list.click()
            else:
                self.fail("Read Only option list, not found")

        self.switch_context_to_native()

    def fill_new_single_line_text2(self, text):

        logging.info("fill new single line text 2 field")

        self.switch_context_to_webview()

        field = self.driver.find_element(*self.configuration.ReportsScreen.NEW_SINGLE_LINE_TEXT2)
        self.assertIsNotNone(field, "input field not found")
        field.click()
        field.clear()
        field.send_keys(text)

        self.switch_context_to_native()

    def fill_new_phone_number2(self, text):

        logging.info("fill new phone number 2 field")

        self.switch_context_to_webview()

        field = self.driver.find_element(*self.configuration.ReportsScreen.NEW_PHONE_NUMBER2)
        self.assertIsNotNone(field, "input field not found")
        field.click()
        field.clear()
        field.send_keys(text)

        self.switch_context_to_native()

    def fill_new_multi_line_text2(self, text):

        logging.info("fill new multi line text 2 field")

        self.switch_context_to_webview()

        field = self.driver.find_element(*self.configuration.ReportsScreen.NEW_MULTI_LINE_TEXT2)
        self.assertIsNotNone(field, "input field not found")
        field.click()
        field.clear()
        field.send_keys(text)

        self.switch_context_to_native()

    def fill_new_fax_number2(self, text):

        logging.info("fill new fax number 2 field")

        self.switch_context_to_webview()

        field = self.driver.find_element(*self.configuration.ReportsScreen.NEW_FAX_NUMBER2)
        self.assertIsNotNone(field, "input field not found")
        field.click()
        field.clear()
        field.send_keys(text)

        self.switch_context_to_native()

    def fill_new_mobile_number2(self, text):

        logging.info("fill new mobile number 2 field")

        self.switch_context_to_webview()

        field = self.driver.find_element(*self.configuration.ReportsScreen.NEW_MOBILE_NUMBER2)
        self.assertIsNotNone(field, "input field not found")
        field.click()
        field.clear()
        field.send_keys(text)

        self.switch_context_to_native()

    def fill_new_email_address2(self, text):

        logging.info("fill new email address 2 field")

        self.switch_context_to_webview()

        field = self.driver.find_element(*self.configuration.ReportsScreen.NEW_EMAIL_ADDRESS2)
        self.assertIsNotNone(field, "input field not found")
        field.click()
        field.clear()
        field.send_keys(text)

        self.switch_context_to_native()

    def fill_new_rich_text2(self, text):

        logging.info("fill new rich text 2 field")

        self.switch_context_to_webview()

        field = self.driver.find_element(*self.configuration.ReportsScreen.NEW_RICH_TEXT2)
        self.assertIsNotNone(field, "input field not found")
        field.send_keys(text)

        self.switch_context_to_native()

    def fill_new_number2(self, text):

        logging.info("fill new number 2 field")

        self.switch_context_to_webview()

        field = self.driver.find_element(*self.configuration.ReportsScreen.NEW_NUMBER2)
        self.assertIsNotNone(field, "input field not found")
        field.click()
        field.clear()
        field.send_keys(text)

        self.switch_context_to_native()

    def fill_new_website_address2(self, text):

        logging.info("fill new website address 2 field")

        self.switch_context_to_webview()

        field = self.driver.find_element(*self.configuration.ReportsScreen.NEW_WEBSITE_ADDRESS2)
        self.assertIsNotNone(field, "input field not found")
        field.click()
        field.clear()
        field.send_keys(text)

        self.switch_context_to_native()

    def scroll_down_one_view(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

