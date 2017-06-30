""" Methods for IOS to handle Map Page """

from Modules.MapPage.MapPage import MapPage
import logging
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
import random
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions
# from appium.webdriver.common.multi_action import MultiAction
# from appium.webdriver.webelement import WebElement
# from selenium.webdriver.common.action_chains import ActionChains


class IOS(MapPage):

    def wait_for_map_to_load(self):

        logging.info("Waiting for map to load")
        try:
            WebDriverWait(self.driver, 5).until(
                expected_conditions.presence_of_element_located(self.configuration.Map.MAP_AREA_12),
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
        window_size = self.driver.get_window_size()  # this returns dictionary
        # position_x = window_size["width"] * 0.30
        # position_y = window_size["height"] * 0.60
        position_x = round(window_size["width"] * 0.4)
        position_y = round(window_size["height"] * 0.4)
        logging.info("width = x = " + str(position_x))
        logging.info("height = y = " + str(position_y))
        positions = [(position_x, position_y)]
        # action = TouchAction(self.driver)
        # action.tap(element=None, x=position_x, y=position_y, count=1).perform()
        # position = [(350, 550)]
        sleep(1)
        self.driver.tap(positions)
        sleep(1)

    def click_in_map_area_2(self):

        logging.info("click on map")
        window_size = self.driver.get_window_size()  # this returns dictionary
        position_x = round(window_size["width"] * 0.5)
        position_y = round(window_size["height"] * 0.5)
        logging.info("width = x = " + str(position_x))
        logging.info("height = y = " + str(position_y))
        positions = [(position_x, position_y)]
        # position = [(300, 500)]
        sleep(1)
        self.driver.tap(positions)
        sleep(1)

    def click_in_map_area_3(self):

        logging.info("click on map")
        window_size = self.driver.get_window_size()  # this returns dictionary
        position_x = round(window_size["width"] * 0.7)
        position_y = round(window_size["height"] * 0.7)
        logging.info("width = x = " + str(position_x))
        logging.info("height = y = " + str(position_y))
        positions = [(position_x, position_y)]
        # position = [(0, 0)]
        sleep(1)
        self.driver.tap(positions)
        sleep(1)

    def double_tap_on_map(self):

        logging.info("double tap on map")
        sleep(1)

        window_size = self.driver.get_window_size()  # this returns dictionary
        logging.info("window size = " + str(window_size))

        el = self.driver.find_element(*self.configuration.CommonScreen.WHOLE_APP_SCREEN)
        # location = el.location
        # logging.warning("location in native view = " + str(location))

        # size = el.size  # this returns dictionary -- size of that element is bigger than window size ?
        # logging.warning("size in native view = " + str(size))
        # size_x = int(size["width"])
        # size_y = int(size["height"])
        # logging.warning("size_x = width = " + str(size_x))
        # logging.warning("size_y = height = " + str(size_y))
        #
        # start_x = int(location["x"])
        # start_y = int(location["y"])
        # logging.warning("start_x = " + str(start_x))
        # logging.warning("start_y = " + str(start_y))

        # using random integers to vary double tap position between function calls
        # random_int_1 = random.randint(51, 60)  # hardcoded values
        # random_float_1 = random_int_1 / 100  # division to prepare some float similar to 0.5
        # random_int_2 = random.randint(30, 40)  # WORKS ON EMULATOR BUT NOT ON RD
        # random_float_2 = random_int_2 / 100

        # for debugging
        # random_int_1 = random.randint(50, 55)  # hardcoded values
        # random_float_1 = random_int_1 / 100  # division to prepare some float similar to 0.5
        # random_int_2 = random.randint(56, 61)
        # random_float_2 = random_int_2 / 100

        # NOTES:
        # works on emu ios10: 52, 61 and 50, 59 and 55, 61 and
        # doesn't work on iPhone 10: 52, 60 and 53, 60 and 55, 61 (206x472) and 0,5 0,2

        # for debugging
        # logging.error("random_int_1 = " + str(random_int_1))
        # logging.error("random_float_1 = " + str(random_float_1))
        # logging.error("random_int_2 = " + str(random_int_2))
        # logging.error("random_float_2 = " + str(random_float_2))
        # end_x = round(size_x * random_float_1)  # multiply whole screen width and float like 0.5
        # end_y = round(size_y * random_float_2)

        start_x = int(window_size["width"])
        start_y = int(window_size["height"])
        logging.warning("start_x = " + str(start_x))
        logging.warning("start_y = " + str(start_y))

        random_int_1 = random.randint(51, 60)  # hardcoded values
        random_float_1 = random_int_1 / 100  # division to prepare some float similar to 0.5
        random_int_2 = random.randint(30, 50)
        random_float_2 = random_int_2 / 100

        logging.error("random_int_1 = " + str(random_int_1))
        logging.error("random_float_1 = " + str(random_float_1))
        logging.error("random_int_2 = " + str(random_int_2))
        logging.error("random_float_2 = " + str(random_float_2))
        end_x = round(start_x * random_float_1)  # multiply whole screen width and float like 0.5
        end_y = round(start_y * random_float_2)

        # end_x = round(start_x * 0.5)
        # end_y = round(start_y * 0.35)
        # end_x = round(start_x * 0.50)
        # end_y = round(start_y * 0.50)
        # end_x = round(size_x * 0.35)
        # end_y = round(size_y * 0.35)

        logging.warning("end_x = " + str(end_x))
        logging.warning("end_y = " + str(end_y))

        sleep(1)

        self.driver.execute_script("mobile: doubleTap", {"x": end_x, "y": end_y})
        sleep(2)

        logging.info("wait a second after double tapping")

        # action = TouchAction(self.driver)
        # action.tap(element=el, x=150, y=150, count=2).perform()
        #
        # self.driver.execute_script("mobile: doubleTap", {"element": el, "x": end_x, "y": end_y})

        self.switch_context_to_webview()
        logging.error("double tap in webview")
        self.driver.execute_script("mobile: doubleTap", {"x": end_x, "y": end_y})
        self.switch_context_to_native()

    # def double_tap_on_map(self):
    #
    #     logging.info("double tap on map")
    #     sleep(1)
    #
    #     window_size = self.driver.get_window_size()  # this returns dictionary
    #     logging.info("window size = " + str(window_size))
    #
    #     position_x = window_size["width"] * 0.50
    #     position_y = window_size["height"] * 0.50
    #
    #     # el = self.driver.find_element(*self.configuration.CommonScreen.WEB_VIEW)
    #     el = self.driver.find_element(*self.configuration.CommonScreen.WHOLE_APP_SCREEN)
    #     location = el.location
    #     logging.warning("location in native view = " + str(location))
    #
    #     size = el.size
    #     logging.warning("size in native view = " + str(size))
    #     size_x = int(size["width"])
    #     size_y = int(size["height"])
    #     logging.warning("size_x - width = " + str(size_x))
    #     logging.warning("size_y - height = " + str(size_y))
    #
    #     start_x = int(location["x"])
    #     start_y = int(location["y"])
    #     logging.warning("start_x = " + str(start_x))
    #     logging.warning("start_y = " + str(start_y))
    #     end_x = size_x * 0.4
    #     end_y = size_y * 0.4
    #     logging.warning("end_x = " + str(end_x))
    #     logging.warning("end_y = " + str(end_y))
    #
    #     # self.driver.execute_script("mobile: doubleTap", dict(element=[position_x, position_y]))  # not working on iOS10
    #     # positions = dict(element=[position_x, position_y])
    #     # self.driver.execute_script("mobile: doubleTap", positions)
    #     # action = TouchAction(self.driver)
    #     sleep(1)
    #     # self.driver.execute_script("mobile: scroll", {"direction": "down"})
    #     # to_tap = [end_x, end_y]
    #     # self.driver.execute_script("mobile: doubleTap", "x: 250, y: 250")
    #     # action.press(x=end_x, y=end_y).release().wait(500).press(x=end_x, y=end_y).release().perform()
    #     self.driver.execute_script("mobile: doubleTap", {"x": end_x, "y": end_y})  # working on iOS10
    #     # self.driver.execute_script("mobile: tap", dict(element=[position_x, position_y]))
    #     # action.tap(el, end_x, end_y, count=2).release().perform()
    #     # action.tap(el, end_x, end_y, count=2).release().perform()
    #     # action.press(el, 50, start_y).wait(1000).move_to(el, 50, end_y).release().perform()
    #     # point_1 = window_size["width"]
    #     # point_2 = window_size["height"]
    #     # self.driver.swipe(point_1.getX(), point_1.getY(), point_2.getX(), point_2.getY(), 1000)
    #     logging.info("wait a second after double tapping")
    #     sleep(1)

    # def double_click_in_map_area_3(self):
    #
    #     logging.info("double click on map")
    #     sleep(1)
    #
    #     self.switch_context_to_webview()
    #
    #     whole_map = self.driver.find_element(*self.configuration.Map.WHOLE_MAP)
    #
    #     actions = TouchActions(self.driver)
    #     actions.double_tap(on_element=whole_map)
    #
    #     element2 = self.driver.find_element_by_css_selector('div#mapPage>div.ui-content>div#mapCanvas>div#mapCanvas_root>div#mapCanvas_container>div#mapCanvas_layers>div#mapCanvas_layer0>div>img:nth-child(2)')
    #
    #     sleep(1)
    #
    #     el3 = self.driver.find_element_by_css_selector("#mapCanvas_layer0_tile_12_1_1")
    #     action = TouchAction(self.driver)
    #
    #     window_size = self.driver.get_window_size()  # this returns dictionary
    #     logging.info(window_size)
    #
    #     position_x = window_size["width"] * 0.50
    #     position_y = window_size["height"] * 0.50
    #
    #     self.switch_context_to_native()
    #
    #     sleep(1)
    #
    #     element1 = self.driver.find_element(*self.configuration.Map.MAP_AREA_18)
    #     action.tap(element1).perform()
    #     action.tap(element1).perform()
    #
    #     position_x = window_size["width"] * 0.50
    #     position_y = window_size["height"] * 0.50
    #
    #     self.driver.execute_script("mobile: doubletap", dict(element=[position_x, position_y]))
    #
    #     logging.info("wait a second after double tapping")
    #     sleep(1)

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

        # logging.info("position_x = " + str(position_x))
        # logging.info("position_y = " + str(position_y))
        # element1 = self.driver.find_element(*self.configuration.Map.MAP_AREA_18)

        # map6 = self.driver.find_element(*self.configuration.Map.WHOLE_MAP)
        # action.tap(element=map6, count=2).perform()

        # actions = TouchActions(self.driver)
        # element = self.driver.find_element(*self.configuration.Map.WHOLE_MAP)

        # actions.double_tap(on_element=element)

        # action = TouchAction(self.driver)

        # action.tap(element=element, count=2).perform()
        # action.tap(element=element, count=2).release()
        # action.tap(element=element, x=position_x, y=position_y, count=2).perform()
        # action.tap(element=element, x=position_x, y=position_y, count=2).release()
        # action.tap(element=None, x=position_x, y=position_y, count=2)

        # x = el3.get_attribute("x")
        # y = el3.get_attribute("y")
        # position = [(x, y)]

        # action.tap(el3, count=2).perform()  # TEST IT

        # action.tap(None, position_x, position_y, 2).perform()
        # action.tap(element=element2, x=position_x, y=position_y, count=2).perform()

        # action.tap(element=element2, count=2).perform()

        # action.tap(element2).perform()
        # action.tap(element2).perform()

        # actions = MultiAction(self.driver)
        # actions.add(TouchAction.tap(element2).tap(element2).perform())

        # action.tap(element=element1, x=position_x, y=position_y, count=2).perform()  # THIS SHOULD WORK
        #
        # action.tap(element=element1, count=2).perform()

        # positions = [(position_x, position_y)]
        # self.driver.tap(positions, 10)
        # self.driver.tap(positions, 10)

    # def double_click_on_element(self, element, x=None, y=None):
    #     """
    #     :param element - element where action multiple click has to be executed - mandatory
    #     :param x: x coordinate
    #     :param y: y coordinate
    #
    #     x and y can be use without element if action double click
    #     has to be executed in specific place
    #
    #     ways of usage:
    #     1. self.double_click_on_element(el)
    #     2. self.double_click_on_element(el, 200, 200) - el is ignored here
    #     """
    #     action = TouchAction(self.driver)
    #
    #     if x is not None and y is not None:
    #         action.tap(None, x, y, 2).perform()
    #
    #     action.tap(element).perform()
    #     action.tap(element).perform()
