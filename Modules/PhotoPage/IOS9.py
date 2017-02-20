""" Methods for IOS9 on Photo Page """

from Modules.PhotoPage.IOS import IOS
import logging
from selenium.common.exceptions import *
from appium.webdriver.common.touch_action import TouchAction


class IOS9(IOS):

    def click_gallery_button(self):

        # add coordinates for iPhones - clicking is not working because button is invisible
        logging.info("clicking in 'Gallery' button")
        try:
            action = TouchAction(self.driver)
            action.tap(element=None, x=180, y=158, count=1).perform()
        except NoSuchElementException:
            gallery_button = self.driver.find_element(*self.configuration.PhotoScreen.GALLERY_BUTTON)
            if gallery_button.is_displayed():
                self.assertIsNotNone(gallery_button, "Gallery button not found")
                gallery_button.click()

    def click_take_new_button(self):
        # add coordinates for iPhones
        logging.info("clicking in 'Take new' button")
        try:
            action = TouchAction(self.driver)
            action.tap(element=None, x=548, y=158, count=1).perform()
            # take_new_button = self.driver.find_element(*self.configuration.PhotoScreen.TAKE_NEW_BUTTON)
            # if take_new_button.is_displayed():
            #     self.assertIsNotNone(take_new_button, "Take new button not found")
            #     take_new_button.click()
        except NoSuchElementException:
            self.fail("could not tap 'Take new' button")


