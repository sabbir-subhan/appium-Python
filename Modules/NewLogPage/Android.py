""" Methods for Android to handle New Log Page """

from Modules.NewLogPage.NewLogPage import NewLogPage
import logging
from time import sleep


class Android(NewLogPage):

    def scroll_down_to_entry_field(self):

        window_size = self.driver.get_window_size()  # this will give You a dictionary
        start_x = window_size["width"] * 0.25
        start_y = window_size["height"] * 0.15
        end_y = window_size["height"] * 0.6
        logging.info("scroll down only one screen")
        self.driver.swipe(start_x, end_y, start_x, start_y, 3000)

    def type_text_into_entry_field(self, text):

        logging.info("type text into 'Entry' field")
        entry_field = self.driver.find_element(*self.configuration.NewLogScreen.ENTRY_FIELD)
        location = entry_field.location
        print(location)
        x = location["x"] * 1.02
        y = location["y"] * 1.02
        print(x)
        print(y)
        positions = [(x, y)]
        self.driver.tap(positions)
        sleep(1)
        entry_field.send_keys(text)

