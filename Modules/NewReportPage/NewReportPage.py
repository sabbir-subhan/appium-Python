"""A class for methods to handle New Report Page """

from Modules.BasePage.BasePage import BasePage
from Modules.load_class import LoadClass
import logging
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


class NewReportPage(BasePage):

    def type_title(self, text):

        self.switch_context_to_webview()

        logging.info("type title")
        title = self.driver.find_element(*self.configuration.NewReportScreen.TITLE)
        self.assertIsNotNone(title, "Title input field was not found")
        title.click()
        title.send_keys(text)

        self.switch_context_to_native()

        # new_task_page = LoadClass.load_page('NewTaskPage')
        # new_task_page.setDriver(self.driver)
        # new_task_page.type_title(text)

    def click_on_lodging_agency_picker(self):

        sleep(5)
        logging.info("click on 'Lodging Agency' picker")
        try:
            lodging_agency_picker = self.driver.find_element(*self.configuration.NewReportScreen.LODGING_AGENCY_PICKER)
        except NoSuchElementException:
            lodging_agency_picker = self.driver.find_element(*self.configuration.NewReportScreen.LODGING_AGENCY_PICKER2)
        self.assertIsNotNone(lodging_agency_picker, "Lodging Agency picker was not found")
        action = TouchAction(self.driver)
        action.tap(element=lodging_agency_picker, count=1).perform()
        sleep(1)

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
        sleep(2)
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located(self.configuration.MainMenuScreen.EVENTS_BUTTON),
            "Failed to locate description field")
