""" Setup class and methods """

# import os
# import sys
# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# sys.path.insert(0, os.path.dirname(__file__))
# sys.path.insert(0, PROJECT_ROOT + '/../')

from time import sleep
import subprocess
import os
from Conf.desired_capabilities import DesiredCapabilities
from configuration import ENVIRONMENT_TEST
from configuration import PORT
from appium import webdriver
import unittest
import pytest
from importlib import import_module
import logging
logging.basicConfig(filename='./tests/TCs.log', level=logging.INFO,
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

        # logging.info('starting Appium server')
        #
        # subprocess.call(['/Users/lukasl/repos/appium-poc/cli.sh'])  # call shell script that will start appium server in new terminal

        # sleep(45)  # wait for appium server to start

        logging.info(" WebDriver request initiated. Waiting for response, this may take a while.")

        desired_capabilities = DesiredCapabilities.get_desired_capabilities()

        # self.configuration = import_module('Conf.locators_' + ENVIRONMENT_TEST)

        self.driver = webdriver.Remote("http://localhost:" + PORT + "/wd/hub", desired_capabilities)

        self.driver.implicitly_wait(12)  # seconds - how long Appium will wait for conditions, for example try/except



