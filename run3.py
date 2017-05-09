import argparse
import sys
import unittest
import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
#from tests.test_Login import TestLogin
import fire

# def main():
#
#     parser = argparse.ArgumentParser(description='Pass platform name')
#     parser.add_argument('--platform', default='Android_5')
#
#     parser.add_argument('--test', default='test_ManagingLogs')
#
#     parser.add_argument('unittest_args', nargs='*')
#
#     args = parser.parse_args()
#
#     platform = args.platform
#     print("platform passed into run.py = " + platform)
#
#     test = args.test
#     print("test passed into run.py = " + test)
#
#     # loader = unittest.TestLoader()
#     # test_name = loader.discover(start_dir="./tests", pattern="test_Login.py")
#     # unittest.TextTestRunner(verbosity=2).run(test_name)
#
#     # Now set the sys.argv to the unittest_args (leaving sys.argv[0] alone)
#     sys.argv[1:] = args.unittest_args
#
#     return platform

# main()

#Grouping Commands
# class GetPlatform(object):
#
#     # @staticmethod
#     def get_platform(self, platform):
#
#         print("test will start on: " + platform)
#         return platform
#
#
# class StartTest(object):
#
#     # @staticmethod
#     def run_test(self, test):
#
#         return test
#
#
# class Runner(object):
#
#     def __init__(self):
#         self.platform = GetPlatform()
#         self.test = StartTest()
#
#     def run(self):
#
#         self.platform.get_platform(platform="")
#         self.test.run_test(test="")
#
#
# if __name__ == '__main__':
#     fire.Fire(Runner)


# class GetPlatform(object):
#
#     @staticmethod
#     def get_platform(platform):
#
#         print("test will start on: " + platform)
#         return platform
#
# if __name__ == '__main__':
#     fire.Fire(GetPlatform)
#
#     loader = unittest.TestLoader()
#     test_name = loader.discover(start_dir="./tests", pattern="test_Login.py")
#     unittest.TextTestRunner(verbosity=2).run(test_name)

# # class StartTest(object):
#
#     # @staticmethod
#     def run_test(self, test):
#
#         return test
#
# if __name__ == '__main__':
#     fire.Fire(GetPlatform)


# # Calling Functions
# class Runner(object):
#
#     # def test(self):
#     #
#     #     print("test will start on: " + self.test)
#     #     return
#     #
#     # def platform(self):
#     #
#     #     print("test will start on: " + self.platform)
#     #     return
#
#     def __init__(self, test, platform):
#
#         self.test = test
#         self.platform = platform
#
#         print("test will start on: " + self.test)
#         print("test will start on: " + self.platform)
#
#     def xxx(self):
#
#         print("tutaj: " + self.platform)
#         return
#
#     loader = unittest.TestLoader()
#     test_name = loader.discover(start_dir="./tests", pattern="test_Login.py")
#     unittest.TextTestRunner(verbosity=2).run(test_name)
#
# if __name__ == '__main__':
#     fire.Fire(Runner)



class Runner(object):

    def get_test(self, test):

        print("test will start on: " + test)
        return test

    def get_platform(self, platform):

        print("test will start on: " + platform)
        return platform

    def __init__(self, test, platform):

        self.test_case = test
        self.platform_to_run = platform

        print("check argument nr 1: " + self.test_case)
        print("check argument nr 2: " + self.platform_to_run)

    loader = unittest.TestLoader()
    test_name = loader.discover(start_dir="./tests", pattern="test_Login.py")
    unittest.TextTestRunner(verbosity=2).run(test_name)

# x = Runner.get_platform()


if __name__ == '__main__':
    fire.Fire(Runner)



