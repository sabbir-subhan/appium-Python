""" Methods for Android on Event Edit Page """

from Modules.EventEditPage.EventEditPage import EventEditPage
import logging
from time import sleep


class Android(EventEditPage):

    def scroll_down(self):
        """Method to scroll down to bottom of the screen """

        window_size = self.driver.get_window_size()  # this returns dictionary
        start_x = window_size["width"]*0.25
        # end_x = window_size["width"]*0.75
        start_y = window_size["height"]*0.20
        end_y = window_size["height"]*0.80
        logging.info("scroll down")
        sleep(2)
        scrolls = 13
        while scrolls > 0:
            self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
            scrolls -= 1
        sleep(2)

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

    def click_save_button(self):

        super().click_save_button()

    def click_cancel_button(self):

        super().click_cancel_button()


