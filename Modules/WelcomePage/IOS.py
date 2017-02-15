""" Methods for IOS to handle Welcome Page """

from Modules.WelcomePage.WelcomePage import WelcomePage
from Modules.load_class import LoadClass
import logging
from time import sleep
from selenium.common.exceptions import *


class IOS(WelcomePage, LoadClass):

    def click_login_button(self):

        # iOS can not be reset by appium - "No reset" and "session-override" flags are not working,
        #  only "Full reset" will work, but app will be uninstalled
        sleep(5)
        logging.info("logout if already logged in")
        try:
            common_page = LoadClass.load_page('CommonPage')
            common_page.setDriver(self.driver)
            common_page.scroll_down_one_view()
            sleep(2)
            logout_button_ios = self.driver.find_element(*self.configuration.MainMenuScreen.LOGOUT_BUTTON)
            self.assertIsNotNone(logout_button_ios, "Logout button not found")
            logging.info("Your are already logged in - logging out")
            logout_button_ios.click()
            submit_button_ios = self.driver.find_element(*self.configuration.LoginScreen.SUBMIT_BUTTON)
            self.assertIsNotNone(submit_button_ios, "Submit button not found")
            submit_button_ios.click()
            sleep(7)
        except NoSuchElementException:
            logging.info("Your are already logged out")

        logging.info("relaunching app")
        self.driver.reset()  # reset app to avoid problems with locating elements
        logging.info("click in LOGIN button")
        login_button = self.driver.find_element(*self.configuration.WelcomeScreen.LOGIN_BUTTON)
        self.assertIsNotNone(login_button, "Login button not found")
        login_button.click()
