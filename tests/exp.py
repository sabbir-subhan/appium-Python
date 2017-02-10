# Test Case 1 - Log Into OCA mobile via direct Login -- OCAMOB-38

# open OCA app
# input login, password and domain
# click on Submit button
# accept terms if needed
# dismiss alert about expiring password
# dismiss notifications
# check if button "EVENTS" is present

import unittest
import logging
from importlib import import_module
from Modules.Setup import SetupTestCase
from configuration import ENVIRONMENT_TEST
from Modules.load_class import LoadClass


class test_Login(SetupTestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        SetupTestCase.tearDown(self)

    def test_exp(self):
        """
        :param welcome_page:
        :type Modules.WelcomePage.WelcomePage:
        """
        logging.info("starting Test Case 1: login into active account")

        welcome_page = LoadClass.load_page('WelcomePage')
        welcome_page.setDriver(self.driver)
        welcome_page.click_login_button()
        # login_page = LoadClass.load_page('LoginPage')
        # login_page.type_username('QA')  # change here login credentials (login and pass are defined in credentials.py)
        # login_page.type_password('QA')  # for example use: QA, general_user, admin, expired_1_day_ago, expire_today, expire_in_1_day OR suspended
        # login_page.type_domain_address('QA')
        # device = LoadClass.load_page('Device')
        # device.hide_keyboard()
        # login_page.click_submit_button()
        # login_page.accept_terms()
        # main_page = LoadClass.load_page('MainPage')
        # main_page.alert_expiring_password()
        # main_page.dismiss_ios_notifications()
        # main_page.check_presence_of_events_button()

    # def load_page(self, page):
    #
    #     device = ENVIRONMENT_TEST
    #
    #     page = "Modules.welcome_page.WelcomePage"
    #     module = import_module(page)
    #     return getattr(module, page)()


    # def __init__(self, module_name, class_name):
    #     """Constructor"""
    #     module = __import__(module_name)
    #     my_class = getattr(module, class_name)
    #     instance = my_class()
    #     print(instance)

    # def load_page(self, device, package, middle_class=None):
    #     """ dynamically load a class from a string """
    #
    #     device = ENVIRONMENT_TEST
    #
    #     main_module = import_module("Modules.welcome_page")

    # def try_load(self, module):
    #     try:
    #         m = import_module(module)
    #         return m
    #     except ImportError:
    #         return False
    #
    # def load_page(self, device, package, middle_class=None):
    #
    #     #if hasattr(main_module, device):
    #     if self.try_load(module_path):
    #         module_path = "Modules.welcome_page.{device}".format(device=ENVIRONMENT_TEST)
    #         module = import_module(module_path)
    #         return getattr(module, device)()
    #     elif middle_class is not None and hasattr(main_module, middle_class):
    #         module_path = "Modules.welcome_page.IOS"
    #         module = import_module(module_path)
    #         return getattr(module, middle_class)()
    #     elif hasattr(main_module, package):
    #         module_path = "Modules.welcome_page.WelcomePage"
    #         module = import_module(module_path)
    #         return getattr(module, package)()
    #     else:
    #         raise Exception('No module!')


        # main_module = import_module("Modules.main_page")
        #
        # if hasattr(main_module, device):
        #     module_path = "Modules.main_page.{device}".format(device=ENVIRONMENT_TEST)
        #     module = import_module(module_path)
        #     return getattr(module, device)()
        # elif middle_class is not None and hasattr(main_module, middle_class):
        #     module_path = "Modules.main_page.IOS"
        #     module = import_module(module_path)
        #     return getattr(module, middle_class)()
        # elif hasattr(main_module, package):
        #     module_path = "Modules.main_page.MainPage"
        #     module = import_module(module_path)
        #     return getattr(module, package)()
        # else:
        #     #raise Exception('No module!')
        #     pass

#########################################################################################

        # def load_page(self, device, package, middle_class=None):
        #     """ dynamically load a class from a string """
        #
        #     device = ENVIRONMENT_TEST
        #
        #     main_module = import_module("Modules.welcome_page")
        #
        #     if hasattr(main_module, device):
        #         module_path = "Modules.welcome_page.{device}".format(device=ENVIRONMENT_TEST)
        #         module = import_module(module_path)
        #         return getattr(module, device)()
        #     elif middle_class is not None and hasattr(main_module, middle_class):
        #         module_path = "Modules.welcome_page.IOS"
        #         module = import_module(module_path)
        #         return getattr(module, middle_class)()
        #     elif hasattr(main_module, package):
        #         module_path = "Modules.welcome_page.WelcomePage"
        #         module = import_module(module_path)
        #         return getattr(module, package)()
        #     else:
        #         raise Exception('No module!')






    # class Loader(engine.core.Core):
    # def __init__(self, class_name, method_name):
    #     engine.core.Core.__init__(self)
    #     try:
    #         instance = self._call("controllers", class_name)()
    #         if method_name is not None:
    #             getattr(instance, method_name)()
    #     except:
    #         error = engine.error.Error(self.config)
    #         sys.exit(error.log(traceback=True))

    # def _call(self, module_name, class_name):
    #     c = class_name.lower()
    #     dependency = '{module}.{class_name}'.format(module=module_name, class_name=c)
    #     try:
    #         module = import_module(dependency)
    #         obj = getattr(module, c.capitalize())
    #         return obj
    #     except ImportError:
    #         sys.exit("Class '{}' doesn't exist in the current context. "
    #                  "Check your naming conventions. "
    #                  "Lower case for files and first letter uppercase for class.".format(class_name))

# class Loader(engine.core.Core):
    # def __init__(self, class_name, method_name):
    #     engine.core.Core.__init__(self)
    #     try:
    #         instance = self._call("controllers", class_name)()
    #         if method_name is not None:
    #             getattr(instance, method_name)()
    #     except:
    #         error = engine.error.Error(self.config)
    #         sys.exit(error.log(traceback=True))

    # def _call(self, module_name, class_name):
    #     c = class_name.lower()
    #     dependency = '{module}.{class_name}'.format(module=module_name, class_name=c)
    #     try:
    #         module = import_module(dependency)
    #         obj = getattr(module, c.capitalize())
    #         return obj
    #     except ImportError:
    #         sys.exit("Class '{}' doesn't exist in the current context. "
    #                  "Check your naming conventions. "
    #                  "Lower case for files and first letter uppercase for class.".format(class_name))



# +    def load_class(self, package, device, middle_class=None):
# +        """
# +        dynamically load a class from a string
# +        """
# +
# +        main_module = import_module("Modules.MainPage")
# +
# +        device = ENVIRONMENT_TEST
# +        if hasattr(main_module, device):
# +            module_path = "Modules.MainPage.{device}".format(device=ENVIRONMENT_TEST)  # path to file cantaining specific methods for specific device - for example IOS9.py
# +            module = import_module(module_path)  # import class
# +            return getattr(module, device)()  # this retrieves object
# +        elif middle_class is not None and hasattr(main_module, middle_class):
# +            module_path = "Modules.MainPage.IOS"
# +            module = import_module(module_path)
# +            return getattr(module, middle_class)()  # this retrieves object
# +        elif hasattr(main_module, package):
# +            module_path = "Modules.MainPage.MainPage"
# +            module = import_module(module_path)
# +            return getattr(module, package)()  # this retrieves object
# +        else:
# +            raise Exception('No module!')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_Login)
    unittest.TextTestRunner(verbosity=2).run(suite)
