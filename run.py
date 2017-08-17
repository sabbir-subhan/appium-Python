"""Script for launching tests"""

import argparse
import unittest
import os
import logging
from logging import handlers
import sys
from settings import Settings
from settings import SettingsPort
import HtmlTestRunner
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


class LogErrors(object):  # redirect sys.stderr to logging

    def __init__(self, logger, log_level=logging.ERROR):

        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):

        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass

stderr_logger = logging.getLogger('STDERR')
log_errors = LogErrors(stderr_logger, logging.ERROR)
sys.stderr = log_errors

# write logging into file
log = logging.getLogger('')
LOGFILE = PROJECT_ROOT + '/tests/TCs' + '.log'
# format_without_colors = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
format_without_colors = logging.Formatter("%(asctime)s - %(message)s")
file_handler = handlers.RotatingFileHandler(LOGFILE, maxBytes=2550000, backupCount=4)
file_handler.setFormatter(format_without_colors)
log.addHandler(file_handler)


class ColoredFormatter(logging.Formatter):  # display colored logging in console

    def format(self, record):
        if record.levelno == logging.WARNING:
            record.msg = '\033[96m%s\033[0m' % record.msg
        elif record.levelno == logging.ERROR:
            record.msg = '\033[91m%s\033[0m' % record.msg
        elif record.levelno == logging.INFO:
            record.msg = '\033[92m%s\033[0m' % record.msg
        return logging.Formatter.format(self, record)

log = logging.getLogger('')
log.setLevel(logging.INFO)
# format_with_colors = ColoredFormatter("%(asctime)s - %(levelname)s - %(message)s")
format_with_colors = ColoredFormatter("%(asctime)s - %(message)s")
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(format_with_colors)
log.addHandler(console_handler)


# try:
#     print("test")
# except (Exception, IndexError, NoSuchElementException, NoSuchWindowException, NoAlertPresentException,
#         NoSuchAttributeException, NoSuchFrameException, ImeNotAvailableException, ElementNotSelectableException,
#         TimeoutException, ElementNotVisibleException, NotImplementedError, FileNotFoundError, BaseException,
#         ErrorInResponseException, InvalidSelectorException, InvalidElementStateException,
#         MoveTargetOutOfBoundsException, InterruptedError, ImportError, ConnectionError, RemoteDriverServerException,
#         RuntimeError, ReferenceError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError,
#         EnvironmentError):
#     stderr_logger = logging.getLogger('STDERR')
#     log_errors = LoggerErrors(stderr_logger, logging.ERROR)
#     sys.stderr = log_errors


# class Logger(object):  # log errors to console and file
#
#     def __init__(self, filename="errors.log"):
#
#         self.terminal = sys.stderr
#
#         error_time = datetime.datetime.now().strftime('%Y %m %d_%H:%M:%S - ')
#
#         self.log = open(filename, "a")
#         with open(filename, 'a') as logfile:
#             logfile.write(error_time + '\n')
#
#     def write(self, message):
#
#         self.terminal.write(message)
#         self.log.write(message)
#
#     def flush(self):
#         # this flush method is needed for python 3 compatibility.
#         # this handles the flush command by doing nothing.
#         # you might want to specify some extra behavior here.
#         pass
#
# sys.stderr = Logger("tests_errors.log")

# class Logger(object):
#
#     def __init__(self, error):
#         # self.level is really like using log.debug(message)
#         # at least in my case
#         self.error = error
#
#     def write(self, message):
#         # if statement reduces the amount of newlines that are
#         # printed to the logger
#         if message != '\n':
#             self.error(message)
#
#     def flush(self):
#         # create a flush method so things can be flushed when
#         # the system wants to. Not sure if simply 'printing'
#         # sys.stderr is the correct way to do it, but it seemed
#         # to work properly for me.
#         self.error(sys.stderr)
#
# sys.stderr = Logger(logging.error)


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

    logging.info(" ------ LAUNCHING TEST ------ ")

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
    path = PROJECT_ROOT
    os.chdir(path)
    tests_runner = HtmlTestRunner.HTMLTestRunner(output='tests_results', stream=None, verbosity=2,
                                                 report_title='Appium Tests Results')

    if args.test == "all":
        names = loader.discover(start_dir=PROJECT_ROOT + "/tests", pattern="test*.py", top_level_dir=PROJECT_ROOT)
        # unittest.TextTestRunner(verbosity=2).run(names)  # old version
        tests_runner.run(names)
    else:
        names = loader.discover(start_dir=PROJECT_ROOT + "/tests", pattern=args.test + ".py")
        # unittest.TextTestRunner(verbosity=2).run(names)  # old version
        tests_runner.run(names)

    logging.warning("test = " + args.test)
    logging.warning("platform = " + args.platform)
    logging.warning("port = " + args.port)
    logging.info("---------------------------------- END OF THE TEST -------------------------------------------------")

    return args.platform, args.port

if __name__ == '__main__':
    runner()
