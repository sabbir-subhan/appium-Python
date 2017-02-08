from desired_capabilities import DesiredCapabilities
from methods import *
from appium import webdriver
import unittest
import logging
from configuration import ENVIRONMENT_TEST
logging.basicConfig(filename='/Users/lukasl/repos/appium-poc/TCs.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.getLogger().addHandler(logging.StreamHandler())


class SetupTestCase(unittest.TestCase):
    """ Parametrized setup for tests """

    @classmethod
    def setUpClass(cls):
        """ On inherited classes, run our `setUp` method """

        if cls is not SetupTestCase and cls.setUp is not SetupTestCase.setUp:
            orig_setUp = cls.setUp

        def setUpOverride(self, *args, **kwargs):

            SetupTestCase.setUp(self)
            return orig_setUp(self, *args, **kwargs)

        cls.setUp = setUpOverride

    def setUp(self):
        logging.info("WebDriver request initiated. Waiting for response, this may take a while.")

        # choose desired capabilities from desired_capabilities.py
        desired_capabilities = DesiredCapabilities.desired_capabilities_for_iOS_iPad

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

        self.driver.implicitly_wait(25)  # seconds

    def tear_down(self):

        logging.info("Quitting")
        self.driver.quit()

    # def get_platform(self):
    #
    #     platform_name = self.driver.capabilities["platformName"]
    #     print(platform_name)
    #     platform_version = self.driver.capabilities["platformVersion"]
    #     print(platform_version)
    #
    #     if platform_name == "iOS" and platform_version == "9.3":
    #         logging.info("platformName = iOS and platformVersion = 9.3")
    #     elif platform_name == "iOS" and platform_version == "10.2":
    #         logging.info("platformName = iOS and platformVersion = 10.2")
    #     else:
    #         self.fail("I don't know that platform Name or Version")
