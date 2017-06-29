""" Methods for Android on Map Page """

from Modules.MapPage.MapPage import MapPage
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import logging
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


class Android(MapPage):

    # def press_and_drag_duplicated_geometry(self):
    #
    #     logging.info("press and drag duplicated geometry")
    #
    #     self.switch_context_to_webview()
    #
    #     duplicated_geometry = self.driver.find_element(*self.configuration.Map.DUPLICATED_GEOMETRY_ON_MAP)
    #     location = duplicated_geometry.location
    #     print(location)
    #     x = location["x"]
    #     y = location["y"]
    #     print(x)
    #     print(y)
    #     x = x + 2
    #     y = y + 2
    #     print(x)
    #     print(y)
    #     action = TouchAction(self.driver)
    #     action.long_press(el=duplicated_geometry, duration=1000).move_to(x=x, y=y).release().perform()
    #
    #     self.switch_context_to_native()

    def wait_for_map_to_load(self):

        logging.info("Waiting for map to load")
        try:
            WebDriverWait(self.driver, 5).until(
                expected_conditions.presence_of_element_located(self.configuration.Map.MAP_AREA_6),
                "Failed to load map")
            logging.info("Map was successfully loaded")
        except TimeoutException:
            sleep(5)
            logging.info("trying to wait for map")
            # logging.info("Failed to load map")
            # self.fail("Map was not found")
        sleep(2)

    def click_in_map_area_1(self):

        logging.info("click on map")

        action = TouchAction(self.driver)

        window_size = self.driver.get_window_size()  # this returns dictionary
        # logging.info(window_size)

        position_x = window_size["width"] * 0.4
        position_y = window_size["height"] * 0.4
        logging.info("position_x = " + str(position_x))
        logging.info("position_y = " + str(position_y))
        sleep(1)
        action.tap(element=None, x=position_x, y=position_y, count=1).perform()

        # action = TouchAction(self.driver)
        # screen_size = self.driver.get_window_size(windowHandle='current')  # it creates dictionary
        # try:
        #     if screen_size['width'] > 1400:
        #         action.tap(element=None, x=600, y=900, count=1).perform()
        #     else:
        #         logging.info("executing tap on map - width < 1400")
        #         action.tap(element=None, x=300, y=450, count=1).perform()
        # except NoSuchWindowException:
        #     map9 = self.driver.find_element(*self.configuration.Map.MAP_AREA_9)
        #     action.tap(element=map9, count=1).perform()
        sleep(1)

    def click_in_map_area_2(self):

        logging.info("click on map")
        action = TouchAction(self.driver)

        window_size = self.driver.get_window_size()  # this returns dictionary
        # logging.info(window_size)

        position_x = window_size["width"] * 0.6
        position_y = window_size["height"] * 0.6
        logging.info("position_x = " + str(position_x))
        logging.info("position_y = " + str(position_y))
        sleep(1)
        action.tap(element=None, x=position_x, y=position_y, count=1).perform()

        # screen_size = self.driver.get_window_size(windowHandle='current')
        # try:
        #     if screen_size['width'] > 1400:
        #         action.tap(element=None, x=300, y=1600, count=1).perform()
        #     else:
        #         logging.info("executing tap on map - width < 1400")
        #         action.tap(element=None, x=150, y=400, count=1).perform()
        # except NoSuchWindowException:
        #     map3 = self.driver.find_element(*self.configuration.Map.MAP_AREA_3)
        #     action.tap(element=map3, count=1).perform()
        sleep(1)

    def click_in_map_area_3(self):

        logging.info("click on map")
        action = TouchAction(self.driver)

        window_size = self.driver.get_window_size()  # this returns dictionary
        # logging.info(window_size)

        position_x = window_size["width"] * 0.7
        position_y = window_size["height"] * 0.7
        logging.info("position_x = " + str(position_x))
        logging.info("position_y = " + str(position_y))
        sleep(1)
        action.tap(element=None, x=position_x, y=position_y, count=1).perform()
        sleep(1)

    def double_tap_on_map(self):

        logging.info("double click on map")
        action = TouchAction(self.driver)

        window_size = self.driver.get_window_size()  # this returns dictionary
        logging.info("window size = " + str(window_size))

        # position_x = window_size["width"] * 0.50
        # position_y = window_size["height"] * 0.50
        position_x = window_size["width"] * 0.5
        position_y = window_size["height"] * 0.7
        logging.info("position_x = " + str(position_x))
        logging.info("position_y = " + str(position_y))
        action.tap(element=None, x=position_x, y=position_y, count=2).perform()

        # screen_size = self.driver.get_window_size(windowHandle='current')
        # try:
        #     if screen_size['width'] > 1280:
        #         logging.info("executing tap on map - device width > 1280")
        #         action.tap(element=None, x=1200, y=1900, count=2).perform()
        #     elif screen_size['height'] <= 1980 and screen_size['width'] >= 768:
        #         logging.info("executing tap on map - device width => 768 and <= 1280")
        #         action.tap(element=None, x=150, y=800, count=2).perform()
        #     else:
        #         logging.info("executing tap on map - device width < 768")
        #         action.tap(element=None, x=100, y=600, count=2).perform()
        # except NoSuchWindowException:
        #     map6 = self.driver.find_element(*self.configuration.Map.MAP_AREA_6)
        #     action.tap(element=map6, count=2).perform()
        sleep(1)

