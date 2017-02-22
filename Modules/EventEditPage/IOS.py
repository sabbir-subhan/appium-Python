""" Methods for IOS to handle Event Edit Page"""

from Modules.EventEditPage.EventEditPage import EventEditPage
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
import logging
from time import sleep


class IOS(EventEditPage):

    def scroll_down_to_save_button(self):
        """Method to scroll down to bottom of the screen - to 'Save' button"""

        logging.info("scroll down to Save button")
        scroll = 0
        while scroll == 0:
            logging.info("check if save button is visible")
            save_button = self.driver.find_element(*self.configuration.CommonScreen.SAVE_BUTTON)
            if save_button.is_displayed():
                break
            else:
                logging.info("scroll down to save button")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
                # scroll -= 1
        # else:
        #     pass

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

    def scroll_down_to_description_field(self):

        logging.info("scroll down to description field")
        var = 1
        while var == 1:
            logging.info("check if description field is visible")
            description_field = self.driver.find_element(*self.configuration.EventEditScreen.DESCRIPTION_FIELD)
            if description_field.is_displayed():
                break
            else:
                logging.info("scroll down to description field")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})

    def type_text_into_description_field(self):

        try:
            logging.info("type some text into description field")
            self.driver.find_element(*self.configuration.EventEditScreen.DESCRIPTION_FIELD).click()
            self.driver.find_element(*self.configuration.EventEditScreen.DESCRIPTION_FIELD).send_keys("test ios")
        except NoSuchElementException:
            logging.info("text field couldn't be selected")
            pass

    def scroll_down_to_option_list(self):

        logging.info("scroll down to option_list")
        var = 1
        while var == 1:
            logging.info("check if option list is visible")
            option_list = self.driver.find_element(*self.configuration.EventEditScreen.NEW_OPTION_LIST_HEADER)
            if option_list.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})

    def click_on_option_list(self):

        logging.info("click on option list")
        new_option_list = self.driver.find_element(*self.configuration.EventEditScreen.NEW_OPTION_LIST_HEADER)
        self.assertIsNotNone(new_option_list)
        new_option_list.click()

    def scroll_down_to_add_row_button(self):

        logging.info("scroll down with loop")
        var = 1
        while var == 1:
            logging.info("check if add row button is visible")
            save_button = self.driver.find_element(*self.configuration.EventEditScreen.SUBFORM_FIELD_ADD_ROW)
            if save_button.is_displayed():
                break
            else:
                logging.info("scroll down to add row button")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})

    # only for event type: "event_for_on_load/save_test"
    def click_button_add_row(self):

        logging.info("click button Add row")
        add_row = self.driver.find_element(*self.configuration.EventEditScreen.SUBFORM_FIELD_ADD_ROW)
        self.assertIsNotNone(add_row, "add_row button not found")
        add_row.click()

    def scroll_down_to_event_chooser_field(self):

        logging.info("scroll down with loop")
        var = 1
        while var == 1:
            logging.info("check if event_chooser_field is visible")
            save_button = self.driver.find_element(*self.configuration.EventEditScreen.CHOOSER_FIELD)
            if save_button.is_displayed():
                break
            else:
                logging.info("scroll down")
                self.driver.execute_script("mobile: scroll", {"direction": "down"})

    def delete_chosen_event_inside_subform(self):

        logging.info("delete chosen event inside sub form")
        sleep(1)
        try:
            delete_x = self.driver.find_element(*self.configuration.EventEditScreen.DELETE_SUB_EVENT_FROM_CHOOSER)
            if delete_x.is_displayed():
                self.assertIsNotNone(delete_x)
                delete_x.click()
            else:
                pass
        except NoSuchElementException:
            positions_for_delete_button = [(16, 608)]
            self.driver.tap(positions_for_delete_button)
            try:
                previously_created_event_for_subform_chooser = self.driver.find_element(
                    *self.configuration.EventEditScreen.PREVIOUSLY_CREATED_EVENT_FOR_SUBFORM_CHOOSER)
                self.assertIsNone(previously_created_event_for_subform_chooser)
            except NoSuchElementException:
                pass

    def click_on_option_1(self):

        logging.info("choose '1' in option list")
        option_1 = self.driver.find_element(*self.configuration.EventEditScreen.OPTION_LIST_VALUE_1)
        self.assertIsNotNone(option_1, "option list - option '1' not found")
        option_1.click()

    def click_on_option_2(self):

        logging.info("choose '2' in option list")
        option_2 = self.driver.find_element(*self.configuration.EventEditScreen.OPTION_LIST_VALUE_2)
        self.assertIsNotNone(option_2, "option list - option '2' not found")
        option_2.click()

    def click_on_option_3(self):

        logging.info("choose '3' in option list")
        option_3 = self.driver.find_element(*self.configuration.EventEditScreen.OPTION_LIST_VALUE_3)
        self.assertIsNotNone(option_3, "option list - option '3' not found")
        option_3.click()





