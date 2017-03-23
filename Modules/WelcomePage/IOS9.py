""" Methods for IOS9 on Welcome Page """

from Modules.WelcomePage.IOS import IOS
from Modules.load_class import LoadClass
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import logging
from time import sleep
from importlib import import_module


class IOS9(IOS):

    def click_login_button(self):

        # welcome_page = LoadClass.load_page('WelcomePage')
        # welcome_page.setDriver(self.driver)
        # welcome_page.logout()

        # logging.info("relaunching app to avoid problems with locating elements")
        # self.driver.reset()  # reset app to avoid problems with locating elements

        logging.info("click in LOGIN button")
        sleep(2)

        # common_page = LoadClass.load_page('CommonPage')
        # common_page.setDriver(self.driver)
        # common_page.switch_context_to_webview()
        # self.configuration = import_module('Conf.locators_for_webview')
        # self.driver.find_element(*self.configuration.WelcomeScreen.LOGIN_BUTTON).click()

        common_page = LoadClass.load_page('CommonPage')
        common_page.setDriver(self.driver)
        common_page.switch_context_to_webview()

        #self.configuration = import_module('Conf.locators_for_webview')

        WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located(self.configuration.WelcomeScreen.LOGIN_BUTTON),
            "Login button not found")
        self.driver.find_element(*self.configuration.WelcomeScreen.LOGIN_BUTTON).click()
        sleep(2)

        common_page.switch_context_to_native()

        sleep(2)

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



