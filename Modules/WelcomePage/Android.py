""" Methods for Android on Welcome Page """

from Modules.WelcomePage.WelcomePage import WelcomePage
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import logging
from Conf.desired_capabilities import DesiredCapabilities


class Android(WelcomePage):

    # def click_login_button(self):
    #
    #     logging.info("click in LOGIN button")
    #     try:
    #         WebDriverWait(self.driver, 20).until(
    #             expected_conditions.presence_of_element_located(self.configuration.WelcomeScreen.LOGIN_BUTTON),
    #             "Login button not found")
    #         self.driver.find_element(*self.configuration.WelcomeScreen.LOGIN_BUTTON).click()
    #     except NoSuchElementException:
    #         self.driver.find_element(*self.configuration.WelcomeScreen.LOGIN_BUTTON_by_index).click()

    def open_SOUND(self):

        logging.info("clicking in Sound button")
        desired_capabilities = DesiredCapabilities.get_desired_capabilities()
        platform_version = desired_capabilities.get('platformVersion')
        if platform_version >= "6":
            try:
                sound_button = self.driver.find_element(*self.configuration.WelcomeScreen.SOUND_BUTTON)
                if sound_button.is_displayed():  # on Android all elements are display, regardless if they can/can't be clicked
                    location = sound_button.location
                    print(location)
                    x = location["x"]
                    y = location["y"]
                    print(x)
                    print(y)
                    positions = [(x, y)]
                    self.driver.tap(positions)
                else:
                    pass
            except:
                self.fail('could not find Sound button')
        else:
            sound_button = self.driver.find_element(*self.configuration.WelcomeScreen.SOUND_BUTTON)
            self.assertIsNotNone(sound_button, "Sound button not found")
            sound_button.click()






