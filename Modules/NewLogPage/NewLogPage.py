"""A class for methods to handle New Log Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
import logging
from time import sleep


class NewLogPage(BasePage):

    def click_on_lodging_agency_picker(self):

        logging.info("click on 'Lodging Agency' picker")
        lodging_agency_picker = self.driver.find_element(*self.configuration.NewLogScreen.LODGING_AGENCY_PICKER)
        self.assertIsNotNone(lodging_agency_picker, "Lodging Agency picker was not found")
        lodging_agency_picker.click()

    def choose_lodging_agency(self):

        new_report_page = LoadClass.load_page('NewReportPage')
        new_report_page.setDriver(self.driver)
        new_report_page.choose_lodging_agency()

    def type_text_into_entry_field(self, text):

        sleep(1)
        logging.info("type text into 'Entry' field")
        entry_field = self.driver.find_element(*self.configuration.NewLogScreen.ENTRY_FIELD)
        entry_field.click()
        entry_field.send_keys(text)

