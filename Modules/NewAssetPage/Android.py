"""A class for methods to handle New Asset Page on Android"""

from Modules.NewAssetPage.NewAssetPage import NewAssetPage
import logging
from time import sleep


class Android(NewAssetPage):

    def scroll_down_to_save_button(self):
        """Method to scroll down to bottom of the screen """

        window_size = self.driver.get_window_size()  # this returns dictionary
        start_x = window_size["width"] * 0.25
        # end_x = window_size["width"]*0.75
        start_y = window_size["height"] * 0.20
        end_y = window_size["height"] * 0.80
        logging.info("scroll down to save button")
        sleep(2)
        scrolls = 5
        while scrolls > 0:
            self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
            scrolls -= 1
        sleep(2)
