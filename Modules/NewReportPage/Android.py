""" Methods for Android on New Report Page """

from Modules.NewReportPage.NewReportPage import NewReportPage
import logging
from time import sleep


class Android(NewReportPage):

    def choose_lodging_agency(self):

        logging.info("choose Lodging Agency")
        lodging_agency = self.driver.find_element(*self.configuration.NewReportScreen.LODGING_AGENCY)
        self.assertIsNotNone(lodging_agency, "Lodging Agency inside picker was not found")
        lodging_agency.click()

    def scroll_down_to_publish_button(self):

        logging.info("scroll down to Publish button")
        window_size = self.driver.get_window_size()  # this returns dictionary
        start_x = window_size["width"]*0.25
        # end_x = window_size["width"]*0.75
        start_y = window_size["height"]*0.20
        end_y = window_size["height"]*0.80
        logging.info("scrolling down to Publish button")
        sleep(1)
        scrolls = 10
        while scrolls > 0:
            self.driver.swipe(start_x, end_y, start_x, start_y, 3000)  # each swipe is scrolling one screen
            scrolls -= 1
        sleep(1)
