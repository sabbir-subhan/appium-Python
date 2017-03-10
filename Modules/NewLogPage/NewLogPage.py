"""A class for methods to handle New Log Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
import logging
from time import sleep


class NewLogPage(BasePage):

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

        new_report_page = LoadClass.load_page('NewReportPage')
        new_report_page.setDriver(self.driver)
        new_report_page.choose_lodging_agency()

    def type_text_into_entry_field(self, text):

        sleep(1)
        window_size = self.driver.get_window_size()  # this will give You a dictionary
        start_x = window_size["width"] * 0.25
        start_y = window_size["height"] * 0.15
        end_y = window_size["height"] * 0.6
        logging.info("scroll down only one screen")
        self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
        logging.info("type text into 'Entry' field")
        try:
            entry_field = self.driver.find_element(*self.configuration.NewLogScreen.ENTRY_FIELD)
        except NoSuchElementException:
            try:
                entry_field = self.driver.find_element(*self.configuration.NewLogScreen.ENTRY_FIELD2)
            except NoSuchElementException:
                entry_field = self.driver.find_element(*self.configuration.NewLogScreen.ENTRY_FIELD3)
        entry_field.click()
        sleep(1)
        entry_field.send_keys(text)

    def scroll_down_to_save_button(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.scroll_down_to_save_button()

    def click_save_button(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.click_save_button()
