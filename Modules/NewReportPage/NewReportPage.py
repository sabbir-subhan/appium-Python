"""A class for methods to handle New Report Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
import logging
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


class NewReportPage(BasePage):

    def type_title(self, text):

        new_task_page = LoadClass.load_page('NewTaskPage')
        new_task_page.setDriver(self.driver)
        new_task_page.type_title(text)

    def click_on_lodging_agency_picker(self):

        sleep(5)
        logging.info("click on 'Lodging Agency' picker")
        lodging_agency_picker = self.driver.find_element(*self.configuration.NewReportScreen.LODGING_AGENCY_PICKER)
        self.assertIsNotNone(lodging_agency_picker, "Lodging Agency picker was not found")
        action = TouchAction(self.driver)
        action.tap(element=lodging_agency_picker, count=1).perform()

    def choose_lodging_agency(self):

        logging.info("choose Lodging Agency")
        lodging_agency = self.driver.find_element(*self.configuration.NewReportScreen.LODGING_AGENCY)
        self.assertIsNotNone(lodging_agency, "Lodging Agency inside picker was not found")
        lodging_agency.click()

    def click_publish_button(self):

        logging.info("click Publish button")
        publish_button = self.driver.find_element(*self.configuration.NewReportScreen.PUBLISH_BUTTON)
        self.assertIsNotNone(publish_button, "Publish button was not found")
        sleep(1)
        action = TouchAction(self.driver)
        action.tap(element=publish_button, count=1).perform()

