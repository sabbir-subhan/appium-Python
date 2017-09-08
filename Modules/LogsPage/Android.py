""" Methods for Android to handle Logs Page """

from Modules.LogsPage.LogsPage import LogsPage
import logging
from time import sleep
from Modules.load_class import LoadClass


class Android(LogsPage):

    def scroll_down_to_entry_field(self):

        window_size = self.driver.get_window_size()  # this will give You a dictionary
        start_x = window_size["width"] * 0.25
        start_y = window_size["height"] * 0.15
        # end_y = window_size["height"] * 0.6
        # end_y = window_size["height"] * 0.65
        end_y = window_size["height"] * 0.7
        logging.info("scroll down only one screen")
        self.driver.swipe(start_x, end_y, start_x, start_y, 3000)

    # def type_text_into_entry_field(self, text):
    #
    #     logging.info("type text into 'Entry' field")
    #     entry_field = self.driver.find_element(*self.configuration.LogsScreen.ENTRY_FIELD)
    #     location = entry_field.location
    #     print(location)
    #     x = location["x"] * 1.02
    #     y = location["y"] * 1.02
    #     print(x)
    #     print(y)
    #     positions = [(x, y)]
    #     self.driver.tap(positions)
    #     sleep(1)
    #     entry_field.send_keys(text)

    def scroll_down_to_save_button(self):
        """Method to scroll down to bottom of the screen """

        window_size = self.driver.get_window_size()  # this returns dictionary
        start_x = window_size["width"] * 0.25
        # end_x = window_size["width"]*0.75
        start_y = window_size["height"] * 0.20
        end_y = window_size["height"] * 0.80
        logging.info("scroll down to save button")
        sleep(2)
        scrolls = 8
        while scrolls > 0:
            self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
            scrolls = scrolls - 1
        sleep(2)

    # def type_text_into_entry_field(self, text):
    #
    #     logging.info("type text into 'Entry' field")
    #
    #     self.switch_context_to_webview()
    #
    #     self.driver.switch_to.frame(self.driver.find_element(*self.configuration.LogsScreen.RICH_TEXT_IFRAME_NEW_LOG))
    #     from selenium.webdriver.support import expected_conditions
    #     from selenium.webdriver.support.ui import WebDriverWait
    #     sleep(1)
    #     # entry_field_inside_iframe = self.driver.find_element(*self.configuration.LogsScreen.ENTRY_FIELD_INSIDE_IFRAME_FIRST_P_TAG)
    #     WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.configuration.LogsScreen.ENTRY_FIELD_INSIDE_IFRAME), "Entry field inside iframe not clickable")
    #     entry_field_inside_iframe = self.driver.find_element(*self.configuration.LogsScreen.ENTRY_FIELD_INSIDE_IFRAME)
    #     self.assertIsNotNone(entry_field_inside_iframe, "Entry file not found")
    #     entry_field_inside_iframe.click()
    #
    #     # entry_field_inside_iframe_first_p_tags = self.driver.find_elements(*self.configuration.LogsScreen.ENTRY_FIELD_INSIDE_IFRAME)
    #     # self.assertIsNotNone(entry_field_inside_iframe_first_p_tags, "Entry file not found")
    #     # entry_field_inside_iframe_first_p_tags[0].click()
    #     # entry_field_inside_iframe_first_p_tags[0].send_keys(text)
    #
    #     from selenium.webdriver.common.keys import Keys
    #     entry_field_inside_iframe.send_keys(Keys.ARROW_LEFT)
    #     # entry_field_inside_iframe.send_keys(Keys.SPACE)
    #     entry_field_inside_iframe.send_keys(Keys.RETURN)
    #     entry_field_inside_iframe.send_keys(text)
    #
    #     self.driver.switch_to.default_content()
    #
    #     self.switch_context_to_native()

    def scroll_down_to_option_list(self):

        logging.info("scroll down to option list")
        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.scroll_down_one_view()

    def type_text_into_entry_field(self, text):

        logging.info("type text into 'Entry' field")

        sleep(0.5)
        entry_field = self.driver.find_element(*self.configuration.LogsScreen.ENTRY_FIELD_BY_XPATH)
        entry_field.click()
        sleep(1)
        entry_field.send_keys(text + " ")

    # def type_text_into_entry_field(self, text):  # text is passed for iOS
    #
    #     logging.info("type text into 'Entry' field")
    #     sleep(1)
    #     entry_field = self.driver.find_element(*self.configuration.LogsScreen.ENTRY_FIELD)
    #     entry_field.click()
    #     sleep(1)
    #     logging.info("sending keys")
    #     self.driver.press_keycode(33)  # send letter 'E'
    #     self.driver.press_keycode(42)  # send letter 'N'
    #     self.driver.press_keycode(48)  # send letter 'T'
    #     self.driver.press_keycode(46)  # send letter 'R'
    #     self.driver.press_keycode(53)  # send letter 'Y'
    #
    # def type_text_into_entry_field_all_fields(self, text):
    #
    #     logging.info("type text into 'Entry' field")
    #     entry_field = self.driver.find_element(*self.configuration.LogsScreen.ENTRY_FIELD)
    #     entry_field.click()
    #     logging.info("sending keys")
    #     sleep(2)
    #     self.driver.press_keycode(29)  # send letter 'A'
    #     self.driver.press_keycode(40)  # send letter 'L'
    #     self.driver.press_keycode(40)  # send letter 'L'
    #     self.driver.press_keycode(62)  # send letter 'SPACE'
    #     self.driver.press_keycode(34)  # send letter 'F'
    #     self.driver.press_keycode(37)  # send letter 'I'
    #     self.driver.press_keycode(33)  # send letter 'E'
    #     self.driver.press_keycode(40)  # send letter 'L'
    #     self.driver.press_keycode(32)  # send letter 'D'
    #     self.driver.press_keycode(47)  # send letter 'S'
    #
    # def type_text_into_entry_field_for_rich_text(self, text):
    #
    #     logging.info("type text into 'Entry' field")
    #     entry_field = self.driver.find_element(*self.configuration.LogsScreen.ENTRY_FIELD)
    #     entry_field.click()
    #     logging.info("sending keys")
    #     sleep(1)
    #     self.driver.press_keycode(36)  # send letter 'H'
    #     self.driver.press_keycode(48)  # send letter 'T'
    #     self.driver.press_keycode(41)  # send letter 'M'
    #     self.driver.press_keycode(40)  # send letter 'L'
    #     self.driver.press_keycode(34)  # send letter 'F'
    #     self.driver.press_keycode(43)  # send letter 'O'
    #     self.driver.press_keycode(46)  # send letter 'R'
    #     self.driver.press_keycode(41)  # send letter 'M'
    #     self.driver.press_keycode(29)  # send letter 'A'
    #     self.driver.press_keycode(48)  # send letter 'T'
    #     self.driver.press_keycode(48)  # send letter 'T'
    #     self.driver.press_keycode(37)  # send letter 'I'
    #     self.driver.press_keycode(42)  # send letter 'N'
    #     self.driver.press_keycode(35)  # send letter 'G'
    #
    #     # text = "htmlformatting"
    #
    # def type_text_into_entry_field_chooser_fields(self, text):
    #
    #     logging.info("type text into 'Entry' field")
    #     entry_field = self.driver.find_element(*self.configuration.LogsScreen.ENTRY_FIELD)
    #     entry_field.click()
    #     logging.info("sending keys")
    #     sleep(1)
    #     self.driver.press_keycode(31)  # send letter 'C'
    #     sleep(0.5)
    #     self.driver.press_keycode(36)  # send letter 'H'
    #     self.driver.press_keycode(43)  # send letter 'O'
    #     self.driver.press_keycode(43)  # send letter 'O'
    #     self.driver.press_keycode(47)  # send letter 'S'
    #     self.driver.press_keycode(33)  # send letter 'E'
    #     self.driver.press_keycode(46)  # send letter 'R'
    #     self.driver.press_keycode(62)  # send letter 'SPACE'
    #     self.driver.press_keycode(34)  # send letter 'F'
    #     self.driver.press_keycode(37)  # send letter 'I'
    #     self.driver.press_keycode(33)  # send letter 'E'
    #     self.driver.press_keycode(40)  # send letter 'L'
    #     self.driver.press_keycode(32)  # send letter 'D'
    #     self.driver.press_keycode(47)  # send letter 'S'




