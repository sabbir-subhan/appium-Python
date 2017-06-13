""" Setup class and methods """

try:
    from configuration import ENVIRONMENT_TEST
except ImportError:
    raise ImportError("WRONG PLATFORM NAME !!! - check available platforms in /appium-poc/configuration.py")
from Conf.desired_capabilities import DesiredCapabilities
from configuration import PORT
from appium import webdriver
import unittest
from time import sleep
import logging
# from logging import handlers
# import sys
# log = logging.getLogger('')
# LOGFILE = './tests/TCs.log'
# format_without_colors = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
# file_handler = handlers.RotatingFileHandler(LOGFILE, maxBytes=(10*1024*1024), backupCount=4)
# file_handler.setFormatter(format_without_colors)
# log.addHandler(file_handler)
#
#
# class ColoredFormatter(logging.Formatter):
#
#     def format(self, record):
#         if record.levelno == logging.WARNING:
#             record.msg = '\033[93m%s\033[0m' % record.msg
#         elif record.levelno == logging.ERROR:
#             record.msg = '\033[91m%s\033[0m' % record.msg
#         elif record.levelno == logging.INFO:
#             record.msg = '\033[92m%s\033[0m' % record.msg
#         return logging.Formatter.format(self, record)
#
# log = logging.getLogger('')
# log.setLevel(logging.INFO)
# format_with_colors = ColoredFormatter("%(asctime)s - %(levelname)s - %(message)s")
# console_handler = logging.StreamHandler(sys.stdout)
# console_handler.setFormatter(format_with_colors)
# log.addHandler(console_handler)

# log = logging.getLogger('')
# log.setLevel(logging.INFO)
# my_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
# LOGFILE = './tests/TCs.log'
# console_handler = logging.StreamHandler(sys.stdout)
# console_handler.setFormatter(my_format)
# log.addHandler(console_handler)
#
# file_handler = handlers.RotatingFileHandler(LOGFILE, maxBytes=(10*1024*1024), backupCount=4)
# file_handler.setFormatter(my_format)
# log.addHandler(file_handler)

# import os
# import sys
# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# sys.path.insert(0, os.path.dirname(__file__))
# sys.path.insert(0, PROJECT_ROOT + '/../')
# from time import sleep
# import subprocess
# import os
# from configuration import ENVIRONMENT_TEST
# import pytest
# from importlib import import_module
# import logging
# FILE = './tests/TCs.log'
# FORMAT = '%(asctime)s %(message)s'
# logging.basicConfig(filename=FILE, level=logging.INFO, format=FORMAT, datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.getLogger().addHandler(logging.StreamHandler())


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

        # subprocess.call(['/Users/lukasl/repos/appium-poc/cli.sh'])  # call shell script that will start appium server in new terminal

        # sleep(45)  # wait for appium server to start

        logging.info(" WebDriver request initiated. Waiting for response, this may take a while.")

        desired_capabilities = DesiredCapabilities.get_desired_capabilities()

        # self.configuration = import_module('Conf.locators_' + ENVIRONMENT_TEST)

        self.driver = webdriver.Remote("http://localhost:" + str(PORT) + "/wd/hub", desired_capabilities)

        sleep(15)  # wait for app launching + optional app installation or/and installation/launching WebDriverAgent

        if ENVIRONMENT_TEST == "IOS9":
            print("implicitly wait = 12 seconds")
            self.driver.implicitly_wait(12)
        else:
            print("implicitly wait = 6 seconds")
            self.driver.implicitly_wait(6)  # seconds - how long Appium will wait for conditions, for example try/except

        # self.driver.implicitly_wait(14)  # seconds - how long Appium will wait for conditions, for example try/except



