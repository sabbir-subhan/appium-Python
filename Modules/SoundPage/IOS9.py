""" Methods for IOS9 on Sound Page """

from Modules.SoundPage.IOS import IOS
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import *
import logging


class IOS9(IOS):

    def click_record_sound_icon(self):

        logging.info("clicking in 'Record Sound' icon")
        try:
            # add coordinates for iPhones
            action = TouchAction(self.driver)
            action.tap(element=None, x=180, y=158, count=1).perform()
        except NoSuchElementException:
            record_sound_button = self.driver.find_element(*self.configuration.SoundScreen.RECORD_SOUND_BUTTON)
            if record_sound_button.is_displayed():
                self.assertIsNotNone(record_sound_button, "record sound button not found")
                record_sound_button.click()



