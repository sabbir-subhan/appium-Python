""" Methods for Android on Event Edit Page """

from Modules.EventEditPage.EventEditPage import EventEditPage
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import logging


class Android(EventEditPage):

    def fill_Name_input_field(self, text):

        logging.info("fill Name input field")
        name_field = self.driver.find_element(*self.configuration.EventEditScreen.NAME_FIELD)
        name_field.click()
        name_field.send_keys(text)

