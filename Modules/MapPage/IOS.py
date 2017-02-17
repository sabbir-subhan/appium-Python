""" Methods for IOS to handle Map Page """

from Modules.MapPage.MapPage import MapPage
import logging
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


class IOS(MapPage):

    def wait_for_map_to_load(self):
        logging.info("Waiting for map to load")
        try:
            WebDriverWait(self.driver, 30).until(
                expected_conditions.presence_of_element_located(self.configuration.Map.MAP_AREA_12),
                "Failed to load map")
            logging.info("Map was successfully loaded")
        except NoSuchElementException:
            logging.info("Failed to load map")
            self.fail("Map was not found")

    def click_in_map_area_1(self):

        logging.info("click on map")
        window_size = self.driver.get_window_size()  # this returns dictionary
        position_x = window_size["width"] * 0.30
        position_y = window_size["height"] * 0.60
        positions = [(position_x, position_y)]
        # action = TouchAction(self.driver)
        # action.tap(element=None, x=position_x, y=position_y, count=1).perform()
        # position = [(350, 550)]
        self.driver.tap(positions)
        sleep(2)

    def click_in_map_area_2(self):

        logging.info("click on map")
        window_size = self.driver.get_window_size()  # this returns dictionary
        position_x = window_size["width"] * 0.5
        position_y = window_size["height"] * 0.5
        positions = [(position_x, position_y)]
        # position = [(300, 500)]
        self.driver.tap(positions)
        sleep(2)

    def click_in_map_area_4(self):

        logging.info("click on map")
        window_size = self.driver.get_window_size()  # this returns dictionary
        position_x = window_size["width"] * 0.70
        position_y = window_size["height"] * 0.70
        positions = [(position_x, position_y)]
        # position = [(0, 0)]
        self.driver.tap(positions)
        sleep(2)

    def double_click_in_map_area_3(self):

        logging.info("double click on map")
        window_size = self.driver.get_window_size()  # this returns dictionary
        logging.info(window_size)
        position_x = window_size["width"] * 0.75
        position_y = window_size["height"] * 0.75
        logging.info(position_x)
        logging.info(position_y)
        sleep(2)
        action = TouchAction(self.driver)
        el = self.driver.find_element(*self.configuration.Map.MAP_AREA_18)
        action.tap(element=el, x=position_x, y=position_y, count=2).perform()
        # Appium 1.6 = "WDA double tap needs an element"


