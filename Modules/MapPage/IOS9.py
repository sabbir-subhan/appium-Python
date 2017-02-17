""" Methods for IOS9 on Map Page """

from Modules.MapPage.IOS import IOS
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
import logging


class IOS9(IOS):

    def double_click_in_map_area_3(self):

        logging.info("double click on map")
        window_size = self.driver.get_window_size()  # this returns dictionary
        logging.info(window_size)
        position_x = window_size["width"] * 0.75
        position_y = window_size["height"] * 0.75
        sleep(2)
        action = TouchAction(self.driver)
        action.tap(element=None, x=position_x, y=position_y, count=2).perform()
        # try:
        #     el = self.driver.find_element(*self.configuration.Map.MAP_AREA_18)  # element is not visible
        #     action.tap(element=el, x=450, y=350, count=2).perform()
        # except ElementNotVisibleException:
        #     action.tap(element=None, x=450, y=350, count=2).perform()




