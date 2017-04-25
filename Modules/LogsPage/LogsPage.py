"""A class for methods to handle Logs Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
import logging
from time import sleep


class LogsPage(BasePage):

    def click_on_lodging_agency_picker(self):

        logging.info("click on 'Lodging Agency' picker")
        try:
            lodging_agency_picker = self.driver.find_element(*self.configuration.NewLogScreen.LODGING_AGENCY_PICKER)  # different locator than in New Report Page
        except NoSuchElementException:
            lodging_agency_picker = self.driver.find_element(*self.configuration.NewLogScreen.LODGING_AGENCY_PICKER2)
        self.assertIsNotNone(lodging_agency_picker, "Lodging Agency picker was not found")
        lodging_agency_picker.click()
        sleep(1)

    def choose_lodging_agency(self):

        new_report_page = LoadClass.load_page('ReportsPage')
        new_report_page.setDriver(self.driver)
        new_report_page.choose_lodging_agency()

    # def scroll_down_to_save_button(self):
    #
    #     event_edit_page = LoadClass.load_page('EventEditPage')
    #     event_edit_page.setDriver(self.driver)
    #     event_edit_page.scroll_down_to_save_button()

    def click_save_button(self):

        self.switch_context_to_webview()

        logging.info('click Save button')
        save_button = self.driver.find_element(*self.configuration.NewLogScreen.SAVE_BUTTON)
        save_button.click()

        self.switch_context_to_native()

        # event_edit_page = LoadClass.load_page('EventEditPage')
        # event_edit_page.setDriver(self.driver)
        # event_edit_page.click_save_button()

    def type_text_into_entry_field(self, text):

        # webview is not working on iOS10

        logging.info("type text into 'Entry' field")
        sleep(1)
        entry_field = self.driver.find_element(*self.configuration.NewLogScreen.ENTRY_FIELD)
        entry_field.click()
        sleep(1)
        entry_field.send_keys(text)

    def expand_types_filter(self):

        self.switch_context_to_webview()

        logging.info("click to expand types filter")

        types_filter = self.driver.find_element(*self.configuration.TYPES_FILTER)
        self.assertIsNotNone(types_filter, "types filter not found")
        types_filter.click()

        self.switch_context_to_native()

    def choose_first_filter(self):

        self.switch_context_to_webview()

        logging.info("choose first filter")

        first_filter = self.driver.find_element(*self.configuration.FIRST_FILTER)
        self.assertIsNotNone(first_filter, "first filter not found")
        first_filter.click()

        self.switch_context_to_native()

    def choose_second_filter(self):

        self.switch_context_to_webview()

        logging.info("choose second filter")

        second_filter = self.driver.find_element(*self.configuration.SECOND_FILTER)
        self.assertIsNotNone(second_filter, "second filter not found")
        second_filter.click()

        self.switch_context_to_native()

    def choose_third_filter(self):

        self.switch_context_to_webview()

        logging.info("choose third filter")

        third_filter = self.driver.find_element(*self.configuration.THIRD_FILTER)
        self.assertIsNotNone(third_filter, "third filter not found")
        third_filter.click()

        self.switch_context_to_native()

    def type_text_into_search_field(self):

        logging.info("filter logs by search field")

        search_field = self.driver.find_element(*self.configuration.EventsScreen.SEARCH_FIELD)
        self.assertIsNotNone(search_field, "Search field not found")
        search_field.click()
        search_field.send_keys("Appium log with all fields")
        sleep(1)
