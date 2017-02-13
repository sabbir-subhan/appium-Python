""" Method for loading classes """

from configuration import ENVIRONMENT_TEST
from configuration import ENVIRONMENT_MIDDLE_CLASS
from importlib import import_module


class LoadClass:

    def __init__(self):
        pass

    @staticmethod
    def try_load(module):
        try:
            m = import_module(module)
            return m
        except ImportError:
            return False

    @staticmethod
    def load_page(package):

        module_path = "Modules.{package}.{device}".format(package=package, device=ENVIRONMENT_TEST)
        module = LoadClass.try_load(module_path)
        if module:
            return getattr(module, ENVIRONMENT_TEST)()

        if ENVIRONMENT_MIDDLE_CLASS is not None:
            module_path = "Modules.{package}.{middle_class}".format(package=package,
                                                                    middle_class=ENVIRONMENT_MIDDLE_CLASS)
            module = LoadClass.try_load(module_path)
            if module:
                return getattr(module, ENVIRONMENT_MIDDLE_CLASS)()

        module_path = "Modules.{package}.{package}".format(package=package)
        module = LoadClass.try_load(module_path)
        if module:
            return getattr(module, package)()
