""" Methods for IOS9 on Video Page """

from Modules.VideoPage.IOS import IOS
from appium.webdriver.common.touch_action import TouchAction
import logging


class IOS9(IOS):

    pass

    # def click_record_new_button(self):
    #
    #     logging.info("clicking in 'Record new' button")
    #     # try:
    #     #     record_new_button = self.driver.find_element(*VideoScreen.RECORD_NEW_BUTTON)
    #     #     if record_new_button.is_displayed():
    #     #         self.assertIsNotNone(record_new_button, "record new button not found")
    #     #         record_new_button.click()
    #     # except NoSuchElementException:
    #     #     action = TouchAction(self.driver)
    #     #     action.tap(element=None, x=548, y=158, count=1).perform()
    #
    #     # add coordinates for iPhones
    #     action = TouchAction(self.driver)
    #     action.tap(element=None, x=563, y=182, count=1).perform()



