""" Methods for IOS to handle Map Page """

from Modules.MapPage.MapPage import MapPage
import logging
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.webelement import WebElement


class IOS(MapPage):

    def wait_for_map_to_load(self):

        logging.info("Waiting for map to load")
        sleep(4)
        try:
            WebDriverWait(self.driver, 30).until(
                expected_conditions.presence_of_element_located(self.configuration.Map.MAP_AREA_12),
                "Failed to load map")
            logging.info("Map was successfully loaded")
        except:
            sleep(5)
            logging.info("trying to wait for map")
            # logging.info("Failed to load map")
            # self.fail("Map was not found")
        sleep(1)

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
        logging.info(position_x)
        logging.info(position_y)
        positions = [(position_x, position_y)]
        # position = [(0, 0)]
        self.driver.tap(positions)
        sleep(2)

    def double_click_in_map_area_3(self):

        # logging.info("double click on map")
        # window_size = self.driver.get_window_size()  # this returns dictionary
        # logging.info(window_size)
        # position_x = window_size["width"] * 0.75
        # position_y = window_size["height"] * 0.75
        # logging.info(position_x)
        # logging.info(position_y)
        # sleep(4)
        # action = TouchAction(self.driver)
        # el = self.driver.find_element(*self.configuration.Map.MAP_AREA_18)
        # action.tap(element=el, x=position_x, y=position_y, count=2).perform()
        # action.tap(element=el, count=2).perform()
        # # Appium 1.6 = "WDA double tap needs an element"
        # sleep(4)

        # el = self.driver.find_element(*self.configuration.Map.MAP_AREA_18)
        # action = TouchAction(self.driver)
        # #action.tap(element=el, x=position_x, y=position_y, count=2).perform()
        # action.tap(el, count=2).perform()
        #
        # self.switch_context_to_native()
        # sleep(4)
        # logging.info("test")
        # el2 = self.driver.find_element(*self.configuration.Map.MAP_AREA_18)
        # self.driver.execute_script("mobile: doubleTap", {"element": el2})

        # logging.info("double click on map")
        # window_size = self.driver.get_window_size()  # this returns dictionary
        # position_x = window_size["width"] * 0.70
        # position_y = window_size["height"] * 0.70
        # logging.info(position_x)
        # logging.info(position_y)
        # positions = [(position_x, position_y)]
        # el = self.driver.find_element(*self.configuration.Map.MAP_AREA_18)
        #
        # touch_action = TouchAction(self.driver)
        # multi_action = MultiAction(self.driver)
        # action0 = touch_action.tap(el)
        # action1 = touch_action.tap(el)
        # multi_action.add(action0).add(action1).perform()
        # sleep(2)

        # window_size = self.driver.get_window_size()  # this returns dictionary
        # logging.info(window_size)
        # position_x = window_size["width"] * 0.75
        # position_y = window_size["height"] * 0.75
        # logging.info(position_x)
        # logging.info(position_y)
        # action = TouchAction(self.driver)
        # screen_size = self.driver.get_window_size(windowHandle='current')
        # el = self.driver.find_element(*self.configuration.Map.MAP_AREA_18)
        # try:
        #     if screen_size['width'] > 760:
        #         logging.info("executing tap on map - device width > 760")
        #         action.tap(element=el, x=200, y=500, count=2).perform()
        #     else:
        #         logging.info("executing tap on map - device width < 760")
        #         action.tap(element=el, x=100, y=300, count=2).perform()
        # except:
        #     action.tap(element=el, count=2).perform()
        # sleep(1)

        logging.info("double click on map")
        sleep(1)

        self.switch_context_to_webview()

        whole_map = self.driver.find_element(*self.configuration.Map.WHOLE_MAP)
        #whole_map.click()

        actions = TouchActions(self.driver)
        actions.double_tap(on_element=whole_map)

        # logging.info("position_x = " + str(position_x))
        # logging.info("position_y = " + str(position_y))
        # element1 = self.driver.find_element(*self.configuration.Map.MAP_AREA_18)

        # map6 = self.driver.find_element(*self.configuration.Map.WHOLE_MAP)
        # action.tap(element=map6, count=2).perform()

        # actions = TouchActions(self.driver)
        # element = self.driver.find_element(*self.configuration.Map.WHOLE_MAP)
        element2 = self.driver.find_element_by_css_selector('div#mapPage>div.ui-content>div#mapCanvas>div#mapCanvas_root>div#mapCanvas_container>div#mapCanvas_layers>div#mapCanvas_layer0>div>img:nth-child(2)')
        # actions.double_tap(on_element=element)

        # action = TouchAction(self.driver)

        sleep(1)
        # action.tap(element=element, count=2).perform()
        # action.tap(element=element, count=2).release()
        # action.tap(element=element, x=position_x, y=position_y, count=2).perform()
        # action.tap(element=element, x=position_x, y=position_y, count=2).release()
        # action.tap(element=None, x=position_x, y=position_y, count=2)
        el3 = self.driver.find_element_by_css_selector("#mapCanvas_layer0_tile_12_1_1")
        action = TouchAction(self.driver)
        # x = el3.get_attribute("x")
        # y = el3.get_attribute("y")
        # position = [(x, y)]

        # action.tap(el3, count=2).perform()  # TEST IT

        window_size = self.driver.get_window_size()  # this returns dictionary
        logging.info(window_size)

        position_x = window_size["width"] * 0.50
        position_y = window_size["height"] * 0.50

        # action.tap(None, position_x, position_y, 2).perform()
        # action.tap(element=element2, x=position_x, y=position_y, count=2).perform()

        # action.tap(element=element2, count=2).perform()

        # action.tap(element2).perform()
        # action.tap(element2).perform()

        # actions = MultiAction(self.driver)
        # actions.add(TouchAction.tap(element2).tap(element2).perform())

        self.switch_context_to_native()

        sleep(1)

        element1 = self.driver.find_element(*self.configuration.Map.MAP_AREA_18)
        action.tap(element1).perform()
        action.tap(element1).perform()

        # action.tap(element=element1, x=position_x, y=position_y, count=2).perform()  # THIS SHOULD WORK
        #
        # action.tap(element=element1, count=2).perform()

        # positions = [(position_x, position_y)]
        # self.driver.tap(positions, 10)
        # self.driver.tap(positions, 10)

        logging.info("wait a second after double tapping")
        sleep(2)

    def double_click_on_element(self, element, x=None, y=None):
        """
        :param element - element where action multiple click has to be executed - mandatory
        :param x: x coordinate
        :param y: y coordinate

        x and y can be use without element if action double click
        has to be executed in specific place

        ways of usage:
        1. self.double_click_on_element(el)
        2. self.double_click_on_element(el, 200, 200) - el is ignored here
        """
        action = TouchAction(self.driver)

        if x is not None and y is not None:
            action.tap(None, x, y, 2).perform()

        action.tap(element).perform()
        action.tap(element).perform()
