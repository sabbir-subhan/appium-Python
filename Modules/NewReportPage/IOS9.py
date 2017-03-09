""" Methods for IOS9 on New Report Page """

from Modules.NewReportPage.IOS import IOS
from Modules.load_class import LoadClass
import logging
from selenium.common.exceptions import *


class IOS9(IOS):

    def scroll_down_to_publish_button(self):

        pass

    def choose_lodging_agency(self):

        logging.info("choose Lodging Agency")
        try:
            choose_lodging_agency = self.driver.find_element(*self.configuration.NewReportScreen.LODGING_AGENCY)
            self.assertIsNotNone(choose_lodging_agency, "Lodging Agency inside picker was not found")
            choose_lodging_agency.click()
        except NoSuchElementException:
            picker_wheel = self.driver.find_element(*self.configuration.CommonScreen.PICKER_WHEEL)
            picker_wheel.send_keys('contact_group_for_tests')
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.done_button()


        






