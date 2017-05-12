"""Script for launching tests"""

import argparse
# import fire
import colour_runner
from colour_runner import *
import unittest
# import logging
import os
# import sys
from settings import Settings
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# sys.path.insert(0, os.path.dirname(__file__))
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
    # parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()
    Settings.platform = args.platform

    """ load test """
    loader = unittest.TestLoader()

    if args.test == "all":
        names = loader.discover(start_dir="./tests", pattern="test*.py", top_level_dir=PROJECT_ROOT)
        unittest.TextTestRunner(verbosity=2).run(names)
    else:
        names = loader.discover(start_dir="./tests", pattern=args.test + ".py")
        unittest.TextTestRunner(verbosity=2).run(names)
        # colour_runner.runner.ColourTextTestRunner(verbosity=2).run(names)

    # results = unittest.TextTestResult
    # results.printErrors()
    # results.wasSuccessful()

    print("test passed into runner =", args.test)
    print("platform passed into runner =", args.platform)

    return args.platform

if __name__ == '__main__':
    runner()

