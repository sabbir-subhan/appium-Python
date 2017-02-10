from Modules.Setup import SetupTestCase
from importlib import import_module
from configuration import ENVIRONMENT_TEST
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
#from credentials import Credentials, ContactIdentifierPIN
import unittest


class BasePage(unittest.TestCase):
    """
    :type driver: appium.webdriver.Remote
    """

    configuration = None

    def setDriver(self, driver):

        self.driver = driver
        self.configuration = import_module('Conf.locators_' + ENVIRONMENT_TEST)
