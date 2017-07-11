""" Methods for IOS to handle Tasks Page """

from Modules.TasksPage.TasksPage import TasksPage
from appium.webdriver.common.touch_action import TouchAction
import logging
from Modules.load_class import LoadClass


class IOS(TasksPage):

    def choose_current_date(self):

        logging.info('choose current date by tapping in "Start date" field')
        try:
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.done_button()
        except:
            start_date = self.driver.find_element(*self.configuration.TasksScreen.START_DATE)  # can't click because of invisible element
            location = start_date.location
            x = location["x"]
            y = location["y"]
            # print(x)
            # print(y)
            action = TouchAction(self.driver)
            action.tap(element=None, x=x, y=y, count=1).perform()

