""" Methods for IOS to handle Event Edit Page"""

from Modules.EventEditPage.EventEditPage import EventEditPage
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
import logging


class IOS(EventEditPage, LoadClass):

    def scroll_down(self):
        """Method to scroll down to bottom of the screen - to 'Save' button"""

        logging.info("scroll down to Save button")
        scroll = 0
        while scroll == 0:
            logging.info("check if save button is visible")
            save_button = self.driver.find_element(*self.configuration.CommonScreen.SAVE_BUTTON)
            if save_button.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                # scroll -= 1
        # else:
        #     pass

    def scroll_up(self):

        super().scroll_up()

    def fill_Name_input_field(self, text):

        logging.info("fill Name input field")
        try:
            name_field = self.driver.find_element(*self.configuration.EventEditScreen.NAME_FIELD)
            if name_field.is_displayed():
                name_field.click()
                name_field.send_keys(text)
        except NoSuchElementException:
            name_field_by_index = self.driver.find_element(*self.configuration.EventEditScreen.NAME_FIELD_by_index)
            if name_field_by_index.is_displayed():
                name_field_by_index.click()
                name_field_by_index.send_keys(text)

    def choose_severity_level_1(self):

        logging.info("choose_severity_lvl1")
        try:
            choose_severity_lvl1 = self.driver.find_element(*self.configuration.EventEditScreen.
                                                            CHOOSE_SEVERITY_LVL1_iPad)
            self.assertIsNotNone(choose_severity_lvl1, "choose_severity_lvl1 not found")
            choose_severity_lvl1.click()
        except NoSuchElementException:
            picker_wheel = self.driver.find_element(*self.configuration.CommonScreen.PICKER_WHEEL)
            picker_wheel.send_keys('Severity 1')
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.done_button()

    def choose_severity_level_2(self):

        logging.info("choose_severity_lvl2")
        try:
            choose_severity_lvl2 = self.driver.find_element(*self.configuration.EventEditScreen.
                                                            CHOOSE_SEVERITY_LVL2_iPad)
            self.assertIsNotNone(choose_severity_lvl2, "choose_severity_lvl2 not found")
            choose_severity_lvl2.click()
        except NoSuchElementException:
            picker_wheel = self.driver.find_element(*self.configuration.CommonScreen.PICKER_WHEEL)
            picker_wheel.send_keys('Severity 2')
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.done_button()

    def choose_severity_level_3(self):

        logging.info("choose_severity_lvl3")
        try:
            choose_severity_lvl3 = self.driver.find_element(*self.configuration.EventEditScreen.
                                                            CHOOSE_SEVERITY_LVL3_iPad)
            self.assertIsNotNone(choose_severity_lvl3, "choose_severity_lvl3 not found")
            choose_severity_lvl3.click()
        except NoSuchElementException:
            picker_wheel = self.driver.find_element(*self.configuration.CommonScreen.PICKER_WHEEL)
            picker_wheel.send_keys('Severity 3')
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.done_button()

    def choose_severity_level_4(self):

        logging.info("choose_severity_lvl4")
        try:
            choose_severity_lvl4 = self.driver.find_element(*self.configuration.EventEditScreen.
                                                            CHOOSE_SEVERITY_LVL4_iPad)
            self.assertIsNotNone(choose_severity_lvl4, "choose_severity_lvl4 not found")
            choose_severity_lvl4.click()
        except NoSuchElementException:
            picker_wheel = self.driver.find_element(*self.configuration.CommonScreen.PICKER_WHEEL)
            picker_wheel.send_keys('Severity 4')
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.done_button()

    def choose_severity_level_5(self):

        logging.info("choose_severity_lvl5")
        try:
            choose_severity_lvl5 = self.driver.find_element(*self.configuration.EventEditScreen.
                                                            CHOOSE_SEVERITY_LVL5_iPad)
            self.assertIsNotNone(choose_severity_lvl5, "choose_severity_lvl5 not found")
            choose_severity_lvl5.click()
        except NoSuchElementException:
            picker_wheel = self.driver.find_element(*self.configuration.CommonScreen.PICKER_WHEEL)
            picker_wheel.send_keys('Severity 5')
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.done_button()

    def click_save_button(self):

        super().click_save_button()

    def click_cancel_button(self):

        super().click_cancel_button()



