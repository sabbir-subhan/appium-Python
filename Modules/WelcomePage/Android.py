""" Methods for Android on Welcome Page """

from Modules.WelcomePage.WelcomePage import WelcomePage
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import logging


class Android(WelcomePage):

    def click_login_button(self):

        logging.info("click in LOGIN button")
        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located(self.configuration.WelcomeScreen.LOGIN_BUTTON),
                "Login button not found")
            self.driver.find_element(*self.configuration.WelcomeScreen.LOGIN_BUTTON).click()
        except NoSuchElementException:
            self.driver.find_element(*self.configuration.WelcomeScreen.LOGIN_BUTTON_by_index).click()


