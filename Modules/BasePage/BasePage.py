""" Class for Base Page """

from importlib import import_module
from configuration import ENVIRONMENT_TEST
import unittest
from time import sleep


class BasePage(unittest.TestCase):
    """ :type driver: appium.webdriver.Remote """

    configuration = None

    def setDriver(self, driver):
        """ Method to create appium driver """

        self.driver = driver
        self.configuration = import_module('Conf.locators_' + ENVIRONMENT_TEST)

    def switch_context_to_webview(self):

        print("switching context")
        # print(self.configuration)
        self.configuration = import_module('Conf.locators_for_webview')
        # print(self.configuration)
        current = self.driver.current_context
        print('current context is: ' + current)
        contexts = self.driver.contexts
        print('available contexts: ' + str(contexts))
        self.driver.switch_to.context(contexts[1])
        current_after_switch = self.driver.current_context
        print('current context is: ' + current_after_switch)
        sleep(0.5)

    def switch_context_to_native(self):

        print("switching context")
        # print(self.configuration)
        self.configuration = import_module('Conf.locators_' + ENVIRONMENT_TEST)
        # print(self.configuration)
        current = self.driver.current_context
        print('current context is: ' + current)
        contexts = self.driver.contexts
        print('available contexts: ' + str(contexts))
        self.driver.switch_to.context(contexts[0])
        current_after_switch = self.driver.current_context
        print('current context is: ' + current_after_switch)
        sleep(0.5)
