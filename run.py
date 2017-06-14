"""Script for launching tests"""

import argparse
import unittest
import os
import logging
from logging import handlers
import sys
from settings import Settings
from settings import SettingsPort
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

log = logging.getLogger('')
LOGFILE = './tests/TCs.log'
format_without_colors = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler = handlers.RotatingFileHandler(LOGFILE, maxBytes=(10*1024*1024), backupCount=4)
file_handler.setFormatter(format_without_colors)
log.addHandler(file_handler)


class ColoredFormatter(logging.Formatter):

    def format(self, record):
        if record.levelno == logging.WARNING:
            record.msg = '\033[93m%s\033[0m' % record.msg
        elif record.levelno == logging.ERROR:
            record.msg = '\033[91m%s\033[0m' % record.msg
        elif record.levelno == logging.INFO:
            record.msg = '\033[92m%s\033[0m' % record.msg
        return logging.Formatter.format(self, record)

log = logging.getLogger('')
log.setLevel(logging.INFO)
format_with_colors = ColoredFormatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(format_with_colors)
log.addHandler(console_handler)

# import fire
# import colour_runner
# from colour_runner import *
# import logging

# import sys
# sys.path.insert(0, os.path.dirname(__file__))
# sys.path.insert(0, PROJECT_ROOT + '/../')

'''
$ python run.py -t <test_file_name> -p <platform>
$ python run.py --test <test_file_name> --platform <platform>
example: $ python run.py --test test_Assets --platform IOS_10_emulator
example 2: $ python run.py -t test_Assets -p IOS_10_emulator -port 4735
'''

'''
usage: run.py [-h] [-t TEST] [-p PLATFORM] [-port PORT]

Pass test, platform and port.

You can use bellow platforms:
'''

platform_list = ['Android_4', 'Android_5', 'Android_5_emulator', 'Android_6', 'Android_6_emulator', 'Android_7',
                 'Android_7_emulator', 'Android_7.1_emulator', 'IOS_9', 'IOS_9_emulator', 'IOS_10', 'IOS_10_emulator']
platform_list = ', '.join(platform_list)

'''
devices are defined in /Conf/desired_capabilities.py

optional arguments:
 -h, --help            show this help message and exit
 -t TEST, --test TEST  <test name> (default: all)
 -p PLATFORM, --platform <platform name> (default: Android_5)
 -port, --port <port number> PORT NUMBER ON WHICH APPIUM SERVER IS RUNNING (default: 4723)
'''


def runner():
    """ take 'test name', 'platform' and 'port number' from CLI arguments """

    """ parse arguments """
    parser = argparse.ArgumentParser(description='Pass test name (tests files are located in /appium-poc/tests/),'
                                                 ' platform name and optionally port number '
                                                 'if Appium server is not running with default settings. '
                                                 + ' You can use platforms: ' + platform_list + '.')

    parser.add_argument('-t', '--test', default='all', help='test name (default: all)')
    parser.add_argument('-p', '--platform', default='Android_5', help='platform name (default: Android_5)')
    parser.add_argument('-port', '--port', default='4723', help='Appium port (default: 4723)')
    # parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()
    Settings.platform = args.platform
    SettingsPort.port = args.port

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

    logging.warning("test = " + args.test)
    logging.warning("platform = " + args.platform)
    logging.warning("port = " + args.port)

    return args.platform, args.port

if __name__ == '__main__':
    runner()
