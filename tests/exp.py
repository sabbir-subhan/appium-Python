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


class test_Login(SetupTestCase, unittest.TestCase):
    """ Setup test """

    def setUp(self):

        super(SetupTestCase, self).setUp()

    def tearDown(self):

        SetupTestCase.tearDown(self)

    def test_login(self):

        logging.info("starting Test Case 1: login into active account")
        welcome_page = self.load_class('WelcomePage', ENVIRONMENT_TEST)
        welcome_page.click_login_button()
        login_page = self.load_class('LoginPage', ENVIRONMENT_TEST)
        #login_page = LoginPage(self.driver)
        login_page.type_username('QA')  # change here login credentials (login and pass are defined in credentials.py)
        login_page.type_password('QA')  # for example use: QA, general_user, admin, expired_1_day_ago, expire_today, expire_in_1_day OR suspended
        login_page.type_domain_address('QA')
        # ios_device = iOSdevice(self.driver)
        # ios_device.hide_keyboard()
        login_page.click_submit_button()
        login_page.accept_terms()
        #main_page = MainPage(self.driver)
        main_page = self.load_class('MainPage', ENVIRONMENT_TEST)
        main_page.alert_expiring_password()
        main_page.dismiss_ios_notifications()
        main_page.check_presence_of_events_button()

    # def load_class(self, package, device, middleClass):
    #     package = "MainPage";
    #     device = "IOS9";
    #     'modules.MainPage.IOS9'
    #     'modules.MainPage.MainPage'
    #     mod = __import__(package)
    #     # sprawdzic warunek czy klasa device istnieje, jezeli nie to sprobowac zaladowac klase package
    #     mod = getattr(mod, device)
    #     return mod

    # def load_class2(self, package, device):
    #
    #     package = "LoginPage"
    #     device = "IOS9"
    #     'Modules.LoginPage.LoginPage'
    #     'Modules.LoginPage.IOS9'
    #     mod = __import__(package)
    #     if device is None:
    #         import_module('Modules.LoginPage.LoginPage')
    #     else:
    #         import_module('Modules.LoginPage.IOS9')
    #     mod = getattr(mod, device)
    #     return mod

    # def load_class(self, package, device):
    #
    #     package = "Modules.WelcomePage"
    #     device = "IOS9"
    #     'modules.WelcomePage.WelcomePage'
    #     'modules.IOS9'
    #     mod = __import__(package)
    #     if device == ENVIRONMENT_TEST:
    #         import_module('Modules.WelcomePage.IOS9')
    #     else:
    #         import_module('Modules.WelcomePage.WelcomePage')
    #     mod = getattr(mod, device)
    #     return mod

    # def load_class(self, package, device):
    #
    #     #package = "Modules.WelcomePage"
    #     device = ENVIRONMENT_TEST
    #     #mod = __import__(package)
    #     mod = import_module('Modules.WelcomePage')
    #     mod = getattr(mod, device)
    #     return mod

    def load_class(self, package, device, middle_class=None):
        """
        dynamically load a class from a string
        """

        main_module = import_module("Modules.MainPage")

        device = ENVIRONMENT_TEST
        if hasattr(main_module, device):
            module_path = "Modules.MainPage.{device}".format(device=ENVIRONMENT_TEST)  # path to file cantaining specific methods for specific device - for example IOS9.py
            module = import_module(module_path)  # import class
            return getattr(module, device)()  # this retrieves object
        elif middle_class is not None and hasattr(main_module, middle_class):
            module_path = "Modules.MainPage.IOS"
            module = import_module(module_path)
            return getattr(module, middle_class)()  # this retrieves object
        elif hasattr(main_module, package):
            module_path = "Modules.MainPage.MainPage"
            module = import_module(module_path)
            return getattr(module, package)()  # this retrieves object
        else:
            raise Exception('No module!')

# all classes can not be empty




        # package = "MainPage"
        # module_path = "Modules.MainPage.{device}".format(device=ENVIRONMENT_TEST)
        #
        # module = import_module(module_path)
        # # Finally, we retrieve the Class
        # return getattr(module, device)()

# class Loader(engine.core.Core):
    # def __init__(self, class_name, method_name):
    #     engine.coóre.Core.__init__(self)
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


# def load_class(self, package, device, middle_class=None):
#     """
#     dynamically load a class from a string
#     """
#
#     main_module = import_module("Modules.MainPage")
#
#     device = ENVIRONMENT_TEST
#     if hasattr(main_module, device):
#         module_path = "Modules.MainPage.{device}".format(device=ENVIRONMENT_TEST)
#         module = import_module(module_path)
#         return getattr(module, device)()
#     elif middle_class is not None and hasattr(main_module, middle_class):
#         pass
#     elif hasattr(main_module, package):
#        pass
#     else:
#         raise Exception('No module!')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_Login)
    unittest.TextTestRunner(verbosity=2).run(suite)
