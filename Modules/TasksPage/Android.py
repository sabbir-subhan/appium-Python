""" Methods for Android on Tasks Page """

from Modules.TasksPage.TasksPage import TasksPage
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
import logging


class Android(TasksPage):

    def choose_current_date(self):

        logging.info('choose current date')
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.click_set_button()

    def click_start_date(self):

        logging.info("Choose Start Date")
        try:
            start_date = self.driver.find_element(*self.configuration.TasksScreen.START_DATE)
        except NoSuchElementException:
            start_date = self.driver.find_element(*self.configuration.TasksScreen.START_DATE2)
        self.assertIsNotNone(start_date, "Start Date field not found")
        start_date.click()

