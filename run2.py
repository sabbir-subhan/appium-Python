import argparse
import sys
import unittest
import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


def main():

    parser = argparse.ArgumentParser(description='Pass platform name')
    parser.add_argument('--platform', default='Android_5')

    parser.add_argument('--test', default='test_ManagingLogs')

    parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()

    platform = args.platform
    print("platform passed into run.py = " + platform)

    test = args.test
    print("test passed into run.py = " + test)

    # loader = unittest.TestLoader()
    # test_name = loader.discover(start_dir="./tests", pattern="test_Login.py")
    # unittest.TextTestRunner(verbosity=2).run(test_name)

    # Now set the sys.argv to the unittest_args (leaving sys.argv[0] alone)
    sys.argv[1:] = args.unittest_args

    return platform

main()

if __name__ == '__main__':
    loader = unittest.TestLoader()
    test_name = loader.discover(start_dir="./tests", pattern="test_Login.py")
    unittest.TextTestRunner(verbosity=2).run(test_name)


class GetPlatform:

    @staticmethod
    def get_platform():

        print("test will start on: " + main)
        return main(platform="Android_7")
