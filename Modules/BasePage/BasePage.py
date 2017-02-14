""" Class for Base Page """

from importlib import import_module
from configuration import ENVIRONMENT_TEST
import unittest


class BasePage(unittest.TestCase):
    """ :type driver: appium.webdriver.Remote """

    configuration = None

    def setDriver(self, driver):
        """ Method to create appium driver """

        self.driver = driver
        self.configuration = import_module('Conf.locators_' + ENVIRONMENT_TEST)

