""" Setup class and methods """

from Conf.desired_capabilities import DesiredCapabilities
from configuration import ENVIRONMENT_TEST
from configuration import PORT
from appium import webdriver
import unittest
from importlib import import_module
import logging
logging.basicConfig(filename='TCs.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.getLogger().addHandler(logging.StreamHandler())


class SetupTestCase(unittest.TestCase):
    """ Parametrized setup for tests """

    @classmethod
    def setUpClass(cls):
        """ On inherited classes, run our `setUp` method """

        if cls is not SetupTestCase and cls.setUp is not SetupTestCase.setUp:
            orig_set_up = cls.setUp

        def set_up_override(self, *args, **kwargs):

            SetupTestCase.setUp(self)
            return orig_set_up(self, *args, **kwargs)

        cls.setUp = set_up_override

    def setUp(self):

        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")

        desired_capabilities = DesiredCapabilities.get_desired_capabilities()

        self.configuration = import_module('Conf.locators_' + ENVIRONMENT_TEST)

        # self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
        self.driver = webdriver.Remote("http://localhost:" + PORT + "/wd/hub", desired_capabilities)

        self.driver.implicitly_wait(30)  # seconds - depends on device and connection speed

    # def tear_down(self):
    #
    #     logging.info("Quitting")
    #     self.driver.quit()

