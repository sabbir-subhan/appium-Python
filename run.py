"""Script for launching tests"""

import argparse

import colour_runner
import fire
import unittest
#import redgreenunittest as unittest
import logging
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
#sys.path.insert(0, os.path.dirname(__file__))
# sys.path.insert(0, PROJECT_ROOT + '/../')

'''
$ python run.py -t <test_file_name> -p iOS_10
$ python run.py --test <test_file_name> --platform iOS_10
'''

'''
usage: run.py [-h] [-t TEST] [-p PLATFORM]
              [unittest_args [unittest_args ...]]

Pass test and platform

# positional arguments:
#  unittest_args

optional arguments:
 -h, --help            show this help message and exit
 -t TEST, --test TEST  test name (default: all)
 -p PLATFORM, --platform PLATFORM
                       platform name (default: Android_7)
'''


def runner():
    """ take 'test name' and 'platform' from CLI arguments """

    """ parse arguments """
    parser = argparse.ArgumentParser(description='Pass test and platform')

    parser.add_argument('-t', '--test', default='all', help='test name (default: all)')
    parser.add_argument('-p', '--platform', default='Android_5', help='platform name (default: Android_5)')
    #parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()

    # print('Platform:', args.platform)
    # print('Test:', args.test)

    """ load test """
    loader = unittest.TestLoader()

    if args.test == "all":
        # names = loader.(module="./tests", pattern="test*.py")
        # names = loader.loadTestsFromModule(module="./tests", pattern="test*.py")
        names = loader.discover(start_dir="./tests", pattern="test*.py", top_level_dir=PROJECT_ROOT)
        unittest.TextTestRunner(verbosity=2).run(names)
    else:
        names = loader.discover(start_dir="./tests", pattern=args.test + ".py")
        unittest.TextTestRunner(verbosity=2).run(names)
    # colour_runner.ColourTextTestRunner(verbosity=2).run(names)
    # else:
    #     parser.error("test name not found")

    print("test passed into runner =", args.test)
    print("platform passed into runner =", args.platform)

    return args.platform


runner()




# # change names of variables
# def runner():
#
#     parser = argparse.ArgumentParser(description='Pass test and platform')
#
#     parser.add_argument('--test', default='all')
#     parser.add_argument('--platform', default='Android_5')
#
#     # parser.add_argument('unittest_args', nargs='*')
#
#     args = parser.parse_args()
#
#     platform = args.platform
#     test = args.test
#
#     var1 = str(test)
#     var1 = var1.replace("test=", "")
#     print("end1: " + var1)
#
#     var2 = str(platform)
#     var2 = var2.replace("platform=", "")
#     print("end2: " + var2)
#
#     loader = unittest.TestLoader()
#
#     if var1 == "all":
#         all_tests = loader.discover(start_dir="./tests", pattern="test*.py", top_level_dir=None)
#         unittest.TextTestRunner(verbosity=2).run(all_tests)
#     elif len(var1) > 1:
#         test_name = loader.discover(start_dir="./tests", pattern=var1 + ".py")
#         unittest.TextTestRunner(verbosity=2).run(test_name)
#     else:
#         parser.error("wrong test name")
#
#     print("test passed into run4.py = " + str(var1))
#     print("platform passed into run4.py = " + var2)
#
#     return var2
#
# runner()


# # runner with fire ?
# def runner():
#
#     parser = argparse.ArgumentParser(description='Pass test and platform')
#
#     parser.add_argument('--test', default='all')
#     parser.add_argument('--platform', default='Android_7')
#
#     # parser.add_argument('unittest_args', nargs='*')
#
#     args = parser.parse_args()
#
#     platform = args.platform
#     test = args.test
#
#     var1 = str(test)
#     var1 = var1.replace("test=", "")
#     print("end1: " + var1)
#
#     var2 = str(platform)
#     var2 = var2.replace("platform=", "")
#     print("end2: " + var2)
#
#     loader = unittest.TestLoader()
#
#     if var1 == "all":
#         all_tests = loader.discover(start_dir="./tests", pattern="test*.py", top_level_dir=None)
#         unittest.TextTestRunner(verbosity=2).run(all_tests)
#     elif len(var1) > 1:
#         test_name = loader.discover(start_dir="./tests", pattern=var1 + ".py")
#         unittest.TextTestRunner(verbosity=2).run(test_name)
#     else:
#         parser.error("wrong test name")
#
#     print("test passed into run4.py = " + str(var1))
#     print("platform passed into run4.py = " + var2)
#
#     return var2
#
# runner()
#
# if __name__ == '__runner__':
#   fire.Fire()


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
#     print("platform passed into run4.py = " + platform)
#
#     test = args.test
#     print("test passed into run4.py = " + test)
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


# class Runner:
#
#     def __init__(self, test, platform):
#
#         # pass
#         self.test = test
#         self.platform = platform
#
#         print("check argument nr 1: " + self.test)
#         print("check argument nr 2: " + self.platform)
#
#     def get_test(self, test):
#
#         print("test will start on: " + test)
#         # get_test = Runner(self.test, self.platform)
#         return self.test
#
#     def get_platform(self, platform):
#
#         print("test will start on: " + platform)
#
#         return self.platform
#
#     # loader = unittest.TestLoader()
#     # test_name = loader.discover(start_dir="./tests", pattern="test_Login.py")
#     # unittest.TextTestRunner(verbosity=2).run(test_name)
#
# # x = Runner.get_platform
# # print(str(x))
#
# if __name__ == '__main__':
#     fire.Fire(Runner)

#
# class Runner:
#
#     def __init__(self, test, platform):
#
#         self.test = test
#         self.platform = platform
#
#         print("check argument nr 1: " + self.test)
#         print("check argument nr 2: " + self.platform)
#
#     def get_test(self):
#
#         print("test will start on: " + self.test)
#
#         return self.test
#
#     def get_platform(self):
#
#         print("test will start on: " + self.platform)
#
#         return self.platform
#
#     loader = unittest.TestLoader()
#     test_name = loader.discover(start_dir="./tests", pattern="test_Login.py")
#     unittest.TextTestRunner(verbosity=2).run(test_name)
#
#
# if __name__ == '__main__':
#     fire.Fire(Runner)


# class Runner:
#
#     # def __init__(self, test, platform):
#     #
#     #     self.test = test
#     #     self.platform = platform
#     #
#     #     print("check argument nr 1: " + self.test)
#     #     print("check argument nr 2: " + self.platform)
#     #
#     # def func(platform, test):
#     #
#     #     platform = ""
#     #     test = ""
#     #     return platform, test
#     #
#     # platform, test = 'old-value', 99
#     # platform, test = func(platform, test)
#     # print(platform, test)
#
#     def __init__(self, test, platform):
#
#         first_argument = sys.argv[1]
#         print(first_argument)
#
#         second_argument = sys.argv[2]
#         print(second_argument)
#
#         self.first_argument = first_argument
#         self.get_platform(self.first_argument)
#
#     def get_platform(self, platform):
#
#         platform[0] = self.first_argument
#         # self.test = test
#         # self.platform = platform
#         # self.variable = ['platform']
#         # self.get_platform(self.variable)
#         # Var = sys.argv[1] \
#         #     if len(sys.argv) > 1 \
#         #     else "somevalue"
#
#
#
#     # def get_platform(self, var):
#     #
#     #     var[0] = self.variable
#     #     print(var)
#     #
#     #     return var
#
#     # def get_test(self):
#     #
#     #     print("test will start on: " + self.test)
#     #
#     #     return self.test
#     #
#     # def get_platform(self):
#     #
#     #     print("test will start on: " + self.platform)
#     #
#     #     return self.platform
#
#     # loader = unittest.TestLoader()
#     # test_name = loader.discover(start_dir="./tests", pattern="test_Login.py")
#     # unittest.TextTestRunner(verbosity=2).run(test_name)
#
#
# if __name__ == '__main__':
#     fire.Fire(Runner)



#
#
# def main():
#
#     # Set up argument parser
#     parser = argparse.ArgumentParser()
#
#     # Single positional argument, nargs makes it optional
#     parser.add_argument("test", nargs='*')
#     parser.add_argument("platform", nargs='*')
#
#     # Do parsing
#     arguments = parser.parse_args()
#
#     # Use argument
#     print("print arguments.test: " + arguments[1])
#     print("print arguments.platform: " + str(arguments.platform))
#     print("print arguments: " + arguments)
#
#     return arguments.test[1], arguments.platform[2]
#
# # if __name__ == '__main__':
# #     loader = unittest.TestLoader()
# #     test_name = loader.discover(start_dir="./tests", pattern="test_Login.py")
# #     unittest.TextTestRunner(verbosity=2).run(test_name)
#
# main()
#
#
# class Runner:
#
#     def __init__(self, test, platform):
#
#         self.test = test
#         self.platform = platform
#
#         print("check argument nr 1: " + self.test)
#         print("check argument nr 2: " + self.platform)
#
#         # Set up argument parser
#         parser = argparse.ArgumentParser()
#
#         # Single positional argument, nargs makes it optional
#         # parser.add_argument("test", nargs='*')
#         # parser.add_argument("platform", nargs='*')
#
#         # Do parsing
#         args = parser.parse_args()
#         args.test
#
#     def get_test(self):
#
#         print("test will start on: " + self.test)
#
#         return self.test
#
#     def get_platform(self):
#
#         print("test will start on: " + self.platform)
#
#         return self.platform
#
#     loader = unittest.TestLoader()
#     test_name = loader.discover(start_dir="./tests", pattern="test_Login.py")
#     unittest.TextTestRunner(verbosity=2).run(test_name)

# if __name__ == '__main__':
#     fire.Fire(Runner)



    #main.platform = platform

    # platform = main.platform

    # test = args.test
    # main.test = test

    # Now set the sys.argv to the unittest_args (leaving sys.argv[0] alone)
    #sys.argv[1:] = args.unittest_args


    # loader = unittest.TestLoader()
    # suite = loader.loadTestsFromTestCase(tests.test_Login.TestLogin)
    # unittest.TextTestRunner(verbosity=2).run(suite)


    # all_tests = loader.discover(start_dir="./tests", pattern="test*.py")
    # unittest.TextTestRunner(verbosity=2).run(all_tests)

    #unittest.main()

    #return platform

    # loader = unittest.TestLoader()
    # test_name = loader.discover(start_dir="./tests", pattern="test_Login.py")
    # unittest.TextTestRunner(verbosity=2).run(test_name)



# def suite():
#     loader = unittest.TestLoader()
#     suite = unittest.TestSuite()
#     suite.addTest(loader.loadTestsFromTestCase(TestLogin))
#     return suite

# if __name__ == '__main__':
#     #test = main.test
#     loader = unittest.TestLoader()
#     # test_name = loader.discover(start_dir="./tests", pattern=test)
#     test_name = loader.discover(start_dir="./tests", pattern="test_ManagingLogs.py")
#     unittest.TextTestRunner(verbosity=2).run(test_name)

# main()


# class GetPlatform:
#
#     @staticmethod
#     def get_platform():
#
#         print("test will start on: " + main.)
#         x = main()
#         return main().

# device = main().platform
    # # device = main().platform
    # print("checking platform on end of the run4.py: " + device)