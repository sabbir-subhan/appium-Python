""" Methods for IOS9 on New Task Page """

from Modules.NewTaskPage.IOS import IOS
from appium.webdriver.common.touch_action import TouchAction
import logging


class IOS9(IOS):

    def scroll_down_to_save_button(self):

        pass

    def choose_current_date(self):

        logging.info('choose current date by tapping in "Start date" field')
        start_date = self.driver.find_element(*self.configuration.NewTaskScreen.START_DATE)  # can't click because of invisible element
        location = start_date.location
        x = location["x"]
        y = location["y"]
        print(x)
        print(y)
        action = TouchAction(self.driver)
        action.tap(element=None, x=x, y=y, count=1).perform()


        







