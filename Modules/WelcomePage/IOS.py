""" Methods for IOS"""

from Modules.WelcomePage.WelcomePage import WelcomePage
import logging


class IOS(WelcomePage):

    def click_login_button(self):

        self.driver.reset()  # reset app to avoid problems with locating elements
        logging.info("click in LOGIN button")
        login_button = self.driver.find_element(*self.configuration.WelcomeScreen.LOGIN_BUTTON)
        self.assertIsNotNone(login_button, "Login button not found")
        login_button.click()
