""" Methods for IOS9 on Welcome Page """

from Modules.WelcomePage.IOS import IOS
from Modules.load_class import LoadClass
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import logging
from time import sleep
# from selenium.common.exceptions import *


class IOS9(IOS):

    # pass

    def click_login_button(self):

        welcome_page = LoadClass.load_page('WelcomePage')
        welcome_page.setDriver(self.driver)
        welcome_page.logout()  # not necessary if using fullReset desire_capability in Conf/desired_capabilities.py

        # logging.info("relaunching app to avoid problems with locating elements")
        # self.driver.reset()  # reset app to avoid problems with locating elements
        sleep(2)
        logging.info("click in LOGIN button")
        sleep(2)

        self.switch_context_to_webview()

        WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located(self.configuration.WelcomeScreen.LOGIN_BUTTON),
            "Login button not found")
        sleep(1)
        login_button = self.driver.find_element(*self.configuration.WelcomeScreen.LOGIN_BUTTON)
        self.assertIsNotNone(login_button, "Login button not found")
        login_button.click()
        sleep(1)

        self.switch_context_to_native()

        sleep(1)

        # logging.info("click in LOGIN button")
        # sleep(2)
        # try:
        #     WebDriverWait(self.driver, 30).until(
        #         expected_conditions.presence_of_element_located(self.configuration.WelcomeScreen.LOGIN_BUTTON),
        #         "Login button not found")
        #     self.driver.find_element(*self.configuration.WelcomeScreen.LOGIN_BUTTON).click()
        # except NoSuchElementException:
        #     try:
        #         WebDriverWait(self.driver, 30).until(
        #             expected_conditions.presence_of_element_located(self.configuration.WelcomeScreen.
        #                                                             LOGIN_BUTTON_by_index),
        #             "Login button not found")
        #         self.driver.find_element(*self.configuration.WelcomeScreen.LOGIN_BUTTON_by_index).click()
        #     except NoSuchElementException:
        #         self.driver.find_element(*self.configuration.WelcomeScreen.LOGIN_BUTTON).click()



