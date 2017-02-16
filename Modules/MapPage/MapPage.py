"""A class for methods to handle Map Page """

from Modules.BasePage.BasePage import BasePage
import logging
from time import sleep


class MapPage(BasePage):

    def click_plot_button(self):

        logging.info("click Plot button")
        plot_button = self.driver.find_element(*self.configuration.Map.PLOT_BUTTON)
        self.assertIsNotNone(plot_button)
        plot_button.click()

    def click_tool_button(self):

        logging.info("click tool button")
        tool_button = self.driver.find_element(*self.configuration.Map.TOOL_BUTTON)
        self.assertIsNotNone(tool_button, "Tool button is not present")
        tool_button.click()

    def click_point_button(self):
        logging.info("click point button")
        point_button = self.driver.find_element(*self.configuration.Map.POINT_BUTTON)
        self.assertIsNotNone(point_button, "point button not found")
        point_button.click()

    def click_line_button(self):
        logging.info("click line button")
        line_button = self.driver.find_element(*self.configuration.Map.LINE_BUTTON)
        self.assertIsNotNone(line_button, "line button not found")
        line_button.click()

    def click_circle_button(self):
        logging.info("click circle button")
        circle_button = self.driver.find_element(*self.configuration.Map.CIRCLE_BUTTON)
        self.assertIsNotNone(circle_button, "circle button not found")
        circle_button.click()

    def click_polygon_button(self):
        logging.info("click polygon button")
        polygon_button = self.driver.find_element(*self.configuration.Map.POLYGON_BUTTON)
        self.assertIsNotNone(polygon_button, "polygon button not found")
        polygon_button.click()

    def click_default_button(self):
        logging.info("click default button")
        default_button = self.driver.find_element(*self.configuration.Map.DEFAULT_BUTTON)
        self.assertIsNotNone(default_button, "default button not found")
        default_button.click()
        sleep(1)





