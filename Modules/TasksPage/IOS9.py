""" Methods for IOS9 on Tasks Page """

from Modules.TasksPage.IOS import IOS
from Modules.load_class import LoadClass
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
import logging


class IOS9(IOS):

    def click_on_assigned(self):

        logging.info("click on Assigned field")
        assigned = self.driver.find_element(*self.configuration.TasksScreen.ASSIGNED)
        self.assertIsNotNone(assigned, "Assigned field not found")
        assigned.click()

    def scroll_down_to_save_button(self):

        pass

    def choose_current_date(self):

        logging.info('choose current date by tapping in "Start date" field')
        try:
            # logging.warning("try")  # test
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.done_button()
        except NoSuchElementException:
            # logging.warning("tap")  # test
            start_date = self.driver.find_element(*self.configuration.TasksScreen.START_DATE)  # can't click because of invisible element
            location = start_date.location
            x = location["x"]
            y = location["y"]
            # print(x)
            # print(y)
            action = TouchAction(self.driver)
            # action.tap(element=None, x=x, y=y, count=1).perform()
            action.tap(element=None, x=x, y=y, count=1).perform()








        







