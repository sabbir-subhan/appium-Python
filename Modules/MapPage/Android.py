""" Methods for Android on Map Page """

from Modules.MapPage.MapPage import MapPage
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import logging
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


class Android(MapPage):

    def wait_for_map_to_load(self):

        logging.info("Waiting for map to load")
        try:
            WebDriverWait(self.driver, 30).until(
                expected_conditions.presence_of_element_located(self.configuration.Map.MAP_AREA_6),
                "Failed to load map")
            logging.info("Map was successfully loaded")
        except NoSuchElementException:
            logging.info("Failed to load map")
            self.fail("Map was not found")

    def click_in_map_area_1(self):

        logging.info("click on map")
        action = TouchAction(self.driver)
        screen_size = self.driver.get_window_size(windowHandle='current')  # it creates dictionary
        try:
            if screen_size['width'] > 1400:
                action.tap(element=None, x=600, y=900, count=1).perform()
            else:
                logging.info("executing tap on map - width < 1400")
                action.tap(element=None, x=300, y=450, count=1).perform()
        except NoSuchElementException:
            map9 = self.driver.find_element(*self.configuration.Map.MAP_AREA_9)
            action.tap(element=map9, count=1).perform()
        sleep(1)

    def click_in_map_area_2(self):

        logging.info("click on map")
        action = TouchAction(self.driver)
        screen_size = self.driver.get_window_size(windowHandle='current')
        try:
            if screen_size['width'] > 1400:
                action.tap(element=None, x=300, y=1600, count=1).perform()
            else:
                logging.info("executing tap on map - width < 1400")
                action.tap(element=None, x=150, y=400, count=1).perform()
        except NoSuchElementException:
            map3 = self.driver.find_element(*self.configuration.Map.MAP_AREA_3)
            action.tap(element=map3, count=1).perform()
        sleep(1)

    def double_click_in_map_area_3(self):

        logging.info("double click on map")
        action = TouchAction(self.driver)
        screen_size = self.driver.get_window_size(windowHandle='current')
        try:
            if screen_size['width'] > 1400:
                action.tap(element=None, x=1200, y=1900, count=2).perform()
            else:
                logging.info("executing tap on map - width < 1400")
                action.tap(element=None, x=100, y=600, count=2).perform()
        except NoSuchElementException:
            map6 = self.driver.find_element(*self.configuration.Map.MAP_AREA_6)
            action.tap(element=map6, count=2).perform()
        sleep(1)

