""" Methods for IOS9 on Map Page """

from Modules.MapPage.IOS import IOS
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import logging
import random
from selenium.webdriver.remote.command import Command


class IOS9(IOS):

    def wait_for_map_to_load(self):

        logging.info("Waiting for map to load")
        sleep(10)
        # try:
        #     WebDriverWait(self.driver, 30).until(
        #         expected_conditions.presence_of_element_located(self.configuration.Map.MAP_AREA_12),
        #         "Failed to load map")
        #     logging.info("Map was successfully loaded")
        # except NoSuchElementException:
        #     logging.info("Failed to load map")
        #     self.fail("Map was not found")
        # sleep(1)

    def double_tap_on_map(self):

        logging.info("double tap on map")
        sleep(1)
        window_size = self.driver.get_window_size()  # this returns dictionary
        logging.info("window size = " + str(window_size))
        # # position_x = window_size["width"] * 0.75
        # # position_y = window_size["height"] * 0.75
        # position_x = round(window_size["width"] * 0.35)
        # position_y = round(window_size["height"] * 0.35)
        # logging.warning("width = x = " + str(position_x))
        # logging.warning("height = y = " + str(position_y))
        #
        # action = TouchAction(self.driver)
        # sleep(1)
        # action.tap(element=None, x=position_x, y=position_y, count=2).perform()
        # sleep(2)
        # try:
        #     el = self.driver.find_element(*self.configuration.Map.MAP_AREA_18)  # element is not visible
        #     action.tap(element=el, x=450, y=350, count=2).perform()
        # except ElementNotVisibleException:
        #     action.tap(element=None, x=450, y=350, count=2).perform()

        # el = self.driver.find_element(*self.configuration.CommonScreen.WHOLE_APP_SCREEN)
        # location = el.location
        # logging.warning("location in native view = " + str(location))

        # size = el.size  # this returns dictionary
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
        # random_int_1 = random.randint(41, 60)  # hardcoded values
        # random_float_1 = random_int_1 / 100  # division to prepare some float similar to 0.5
        # random_int_2 = random.randint(30, 40)
        # random_float_2 = random_int_2 / 100

        # for debugging
        # logging.error("random_int_1 = " + str(random_int_1))
        # logging.error("random_float_1 = " + str(random_float_1))
        # logging.error("random_int_2 = " + str(random_int_2))
        # logging.error("random_float_2 = " + str(random_float_2))

        # end_x = round(size_x * 0.5)
        # end_y = round(size_y * 0.35)
        # end_x = round(size_x * 0.52)
        # end_y = round(size_y * 0.52)
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

        logging.warning("end_x = " + str(end_x))
        logging.warning("end_y = " + str(end_y))

        action = TouchAction(self.driver)
        sleep(1)
        # action.press(el, end_x, end_y).perform().release().press(0, 0).perform()

        # a1 = TouchAction(self.driver)
        # a1.tap(element=None, x=end_x, y=end_y, count=1)
        # a2 = TouchAction(self.driver)
        # a2.tap(element=None, x=end_x, y=end_y, count=1)
        # ma = MultiAction(self.driver)
        # ma.add(a1, a2)

        # action.tap(element=el, x=end_x, y=end_y, count=2).release().perform()  # can't use execute_script on iOS9
        action.tap(element=None, x=end_x, y=end_y, count=2).perform()  # can't use execute_script on iOS9
        # action.tap(element=el, count=2).perform()  # can't use execute_script on iOS9
        # action.tap(x=end_x, y=end_y, count=2).perform()  # can't use execute_script on iOS9
        # action.tap(element=None, x=150, y=150, count=2).perform()  # can't use execute_script on iOS9
        # action.tap(element=el, count=2).perform()  # can't use execute_script on iOS9

        logging.info("wait a second after double tapping")
        sleep(2)


        # """
        # Double taps on a given element.  -- method from selenium
        # Args:
        #     -element: The element to tap.
        # """
        # self.driver.execute(Command.DOUBLE_TAP, {'element': el.id})



