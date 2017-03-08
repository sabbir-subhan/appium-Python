""" Methods for IOS to handle New Task Page """

from Modules.NewTaskPage.NewTaskPage import NewTaskPage
from appium.webdriver.common.touch_action import TouchAction
import logging
from Modules.load_class import LoadClass


class IOS(NewTaskPage):

    def choose_current_date(self):

        logging.info('choose current date by tapping in "Start date" field')
        try:
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.done_button()
        except:
            start_date = self.driver.find_element(*self.configuration.NewTaskScreen.START_DATE)  # can't click because of invisible element
            location = start_date.location
            x = location["x"]
            y = location["y"]
            print(x)
            print(y)
            action = TouchAction(self.driver)
            action.tap(element=None, x=x, y=y, count=1).perform()

