""" Methods for IOS to handle Tasks Page """

from Modules.TasksPage.TasksPage import TasksPage
from appium.webdriver.common.touch_action import TouchAction
import logging
from Modules.load_class import LoadClass
from selenium.common.exceptions import NoSuchElementException
from configuration import platform


class IOS(TasksPage):

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
            action.tap(element=start_date, x=x, y=y, count=1).perform()

    def type_text_into_detail_field_offline(self, text):

        self.switch_context_to_webview()

        logging.info("type text into Detail field")

        if "emulator" in platform:  # there is no automatic way to disable networking on iOS emulators
            detail_field = self.driver.find_element(*self.configuration.TasksScreen.DETAIL_FIELD_EDITED)
            self.assertIsNotNone(detail_field, "Detail input field not found")
            detail_field.click()
            detail_field.send_keys(text)
        else:
            detail_field = self.driver.find_element(*self.configuration.TasksScreen.DETAIL_FIELD)
            self.assertIsNotNone(detail_field, "Detail input field not found")
            detail_field.click()
            detail_field.send_keys(text)

        self.switch_context_to_native()



