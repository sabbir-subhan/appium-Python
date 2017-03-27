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

    def scroll_down_to_save_button(self):

        event_edit_page = LoadClass.load_page('EventEditPage')
        event_edit_page.setDriver(self.driver)
        event_edit_page.scroll_down_to_save_button()

    def click_save_button(self):

        self.switch_context_to_webview()

        logging.info('click Save button')
        save_button = self.driver.find_element(*self.configuration.NewLogScreen.SAVE_BUTTON)
        save_button.click()

        self.switch_context_to_native()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.wait_for_app_loading()

        # event_edit_page = LoadClass.load_page('EventEditPage')
        # event_edit_page.setDriver(self.driver)
        # event_edit_page.click_save_button()
