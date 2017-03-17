""" Methods for IOS to handle Welcome Page """

from Modules.WelcomePage.WelcomePage import WelcomePage
from Modules.load_class import LoadClass
import logging
from time import sleep
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class IOS(WelcomePage):

    def logout(self):

        sleep(5)
        logging.info("logout if already logged in")
        try:
            main_page = LoadClass.load_page('MainPage')
            main_page.setDriver(self.driver)
            main_page.scroll_down_to_logout_button()
            sleep(2)
            logout_button = self.driver.find_element(*self.configuration.MainMenuScreen.LOGOUT_BUTTON)
            self.assertIsNotNone(logout_button, "Logout button not found")
            logging.info("Your are already logged in - logging out")
            logout_button.click()
            submit_button = self.driver.find_element(*self.configuration.LoginScreen.SUBMIT_BUTTON)
            self.assertIsNotNone(submit_button, "Submit button not found")
            submit_button.click()
            sleep(8)
        except NoSuchElementException:
            logging.info("Your are already logged out")

    def click_login_button(self):

        # welcome_page = LoadClass.load_page('WelcomePage')
        # welcome_page.setDriver(self.driver)
        # welcome_page.logout()

        # logging.info("relaunching app to avoid problems with locating elements")
        # self.driver.reset()  # reset app to avoid problems with locating elements

        logging.info("click in LOGIN button")
        sleep(2)
        try:
            WebDriverWait(self.driver, 30).until(
                expected_conditions.presence_of_element_located(self.configuration.WelcomeScreen.LOGIN_BUTTON),
                "Login button not found")
            self.driver.find_element(*self.configuration.WelcomeScreen.LOGIN_BUTTON).click()
        except NoSuchElementException:
            try:
                WebDriverWait(self.driver, 30).until(
                    expected_conditions.presence_of_element_located(self.configuration.WelcomeScreen.
                                                                    LOGIN_BUTTON_by_index),
                    "Login button not found")
                self.driver.find_element(*self.configuration.WelcomeScreen.LOGIN_BUTTON_by_index).click()
            except NoSuchElementException:
                self.driver.find_element(*self.configuration.WelcomeScreen.LOGIN_BUTTON).click()

