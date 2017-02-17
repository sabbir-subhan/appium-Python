""" Methods for Android on Event Edit Page """

from Modules.EventEditPage.EventEditPage import EventEditPage
from Modules.load_class import LoadClass
import logging
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import *


class Android(EventEditPage, LoadClass):

    def scroll_down_to_save_button(self):
        """Method to scroll down to bottom of the screen """

        window_size = self.driver.get_window_size()  # this returns dictionary
        start_x = window_size["width"]*0.25
        # end_x = window_size["width"]*0.75
        start_y = window_size["height"]*0.20
        end_y = window_size["height"]*0.80
        logging.info("scroll down to save button")
        sleep(2)
        scrolls = 13
        while scrolls > 0:
            self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
            scrolls -= 1
        sleep(2)

    # def scroll_down_to_save_button(self):
    #     """Method to scroll down to bottom of the screen - to 'Save' button"""
    #
    #     logging.info("scroll down to Save button")
    #     scroll = 0
    #     while scroll == 0:
    #         logging.info("check if save button is visible")
    #         save_button = self.driver.find_element(*self.configuration.CommonScreen.SAVE_BUTTON)
    #         if save_button.is_displayed():  # BUG IN APPIUM ON ANDROID - is.displayed() - ALWAYS RETURNS true
    #             break
    #         else:
    #             logging.info("scroll down to save button")
    #             window_size = self.driver.get_window_size()  # this returns dictionary
    #             start_x = window_size["width"] * 0.25
    #             # end_x = window_size["width"]*0.75
    #             start_y = window_size["height"] * 0.20
    #             end_y = window_size["height"] * 0.80
    #             sleep(2)
    #             self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
    #             sleep(2)

    def scroll_up(self):
        """Method to scroll up to top of the screen"""

        window_size = self.driver.get_window_size()  # this will give You a dictionary
        start_x = window_size["width"]*0.25
        # end_x = window_size["width"]*0.75
        start_y = window_size["height"]*0.25
        end_y = window_size["height"]*0.80
        logging.info("scroll up")
        sleep(2)
        scrolls = 13
        while scrolls > 0:
            self.driver.swipe(start_x, start_y, start_x, end_y, 3000)  # each swipe is scrolling one screen
            scrolls -= 1
        sleep(1)

    def fill_Name_input_field(self, text):

        logging.info("fill Name input field")
        name_field = self.driver.find_element(*self.configuration.EventEditScreen.NAME_FIELD)
        name_field.click()
        name_field.send_keys(text)

    def choose_severity_level_1(self):

        logging.info("choose_severity_lvl1")
        choose_severity_lvl1 = self.driver.find_element(*self.configuration.EventEditScreen.CHOOSE_SEVERITY_LVL1)
        choose_severity_lvl1.click()
        sleep(1)

    def choose_severity_level_2(self):

        logging.info("choose_severity_lvl2")
        choose_severity_lvl2 = self.driver.find_element(*self.configuration.EventEditScreen.CHOOSE_SEVERITY_LVL2)
        choose_severity_lvl2.click()
        sleep(1)

    def choose_severity_level_3(self):

        logging.info("choose_severity_lvl3")
        choose_severity_lvl3 = self.driver.find_element(*self.configuration.EventEditScreen.CHOOSE_SEVERITY_LVL3)
        choose_severity_lvl3.click()
        sleep(1)

    def choose_severity_level_4(self):

        logging.info("choose_severity_lvl4")
        choose_severity_lvl4 = self.driver.find_element(*self.configuration.EventEditScreen.CHOOSE_SEVERITY_LVL4)
        choose_severity_lvl4.click()
        sleep(1)
        
    def choose_severity_level_5(self):

        logging.info("choose_severity_lvl5")
        choose_severity_lvl5 = self.driver.find_element(*self.configuration.EventEditScreen.CHOOSE_SEVERITY_LVL5)
        choose_severity_lvl5.click()
        sleep(1)

    def scroll_down_to_description_field(self):

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def type_text_into_description_field(self):

        sleep(4)
        logging.info("type some text into description field")
        description_field = self.driver.find_element(*self.configuration.EventEditScreen.DESCRIPTION_FIELD)
        sleep(1)
        description_field.send_keys("test Android")
        sleep(2)

    def click_on_option_list(self):

        sleep(4)
        logging.info("click on option list")
        action = TouchAction(self.driver)
        screen_size = self.driver.get_window_size(windowHandle='current')  # it creates dictionary
        if screen_size['width'] < 1000:
            action.tap(element=None, x=250, y=530, count=1).perform()  # coordinates for clicking into "Option List"
        else:
            action.tap(element=None, x=700, y=1430, count=1).perform()
        header_after_opening_option_list = self.driver.find_element(*self.configuration.EventEditScreen.
                                                                    HEADER_ON_OPTION_LIST_PAGE)
        self.assertIsNotNone(header_after_opening_option_list)

    # only for event type: "event_for_on_load/save_test"
    def click_button_add_row(self):

        sleep(1)
        logging.info("click button Add row")
        add_row = self.driver.find_element(*self.configuration.EventEditScreen.SUBFORM_FIELD_ADD_ROW)
        self.assertIsNotNone(add_row, "add_row button not found")
        action = TouchAction(self.driver)
        action.tap(element=add_row, count=1).perform()
        # add_row.click()

    def delete_chosen_event_inside_subform(self):

        sleep(5)
        logging.info("delete chosen event inside sub form")
        delete_button_inside_sub_form = self.driver.find_element(*self.configuration.EventEditScreen.
                                                                 DELETE_SUB_EVENT_FROM_CHOOSER)
        self.assertIsNotNone(delete_button_inside_sub_form, "delete button inside sub form not found")
        delete_button_inside_sub_form.click()
        sleep(5)
        try:
            previously_created_event_for_subform_chooser = self.driver.find_element(
                *self.configuration.EventEditScreen.PREVIOUSLY_CREATED_EVENT_FOR_SUBFORM_CHOOSER)
            self.assertIsNone(previously_created_event_for_subform_chooser)
        except NoSuchElementException:
            pass

    def click_on_option_1(self):

        sleep(1)
        logging.info("choose '1' in option list")
        option_1 = self.driver.find_element(*self.configuration.EventEditScreen.OPTION_LIST_VALUE_1)
        self.assertIsNotNone(option_1, "option list - option '1' not found")
        action = TouchAction(self.driver)
        try:
            action.tap(element=option_1, count=1).perform()
        except:
            option_1.click()

    def click_on_option_2(self):

        logging.info("choose '2' in option list")
        option_2 = self.driver.find_element(*self.configuration.EventEditScreen.OPTION_LIST_VALUE_2)
        self.assertIsNotNone(option_2, "option list - option '2' not found")
        action = TouchAction(self.driver)
        try:
            action.tap(element=option_2, count=1).perform()
        except:
            option_2.click()

    def click_on_option_3(self):

        logging.info("choose '3' in option list")
        option_3 = self.driver.find_element(*self.configuration.EventEditScreen.OPTION_LIST_VALUE_3)
        self.assertIsNotNone(option_3, "option list - option '3' not found")
        action = TouchAction(self.driver)
        try:
            action.tap(element=option_3, count=1).perform()
        except:
            option_3.click()



