#from tests.test_Login import TestLogin
import argparse
import sys
import unittest
import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
import tests


def main():

    parser = argparse.ArgumentParser(description='Pass platform name')
    parser.add_argument('--platform', default='Android_5')

    parser.add_argument('--test', default='test_ManagingLogs')

    parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()
    # do something with args.input
    #global platform
    platform = args.platform
    print("platform passed into run4.py = " + platform)
    main.platform = platform

    # platform = main.platform

    test = args.test
    # main.test = test

    # Now set the sys.argv to the unittest_args (leaving sys.argv[0] alone)
    sys.argv[1:] = args.unittest_args


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

if __name__ == '__main__':
    loader = unittest.TestLoader()
    test_name = loader.discover(start_dir="./tests", pattern="test_Login.py")
    unittest.TextTestRunner(verbosity=2).run(test_name)

main()

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


class GetPlatform:

    @staticmethod
    def get_platform():

        print("test will start on: " + main.platform)
        return main.platform

# device = main().platform
    # # device = main().platform
    # print("checking platform on end of the run4.py: " + device)

















# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestManagingLogs)
#     unittest.TextTestRunner(verbosity=2).run(suite)





# def main():
#
#     parser = argparse.ArgumentParser(description='Pass platform name')
#     parser.add_argument('--platform', default='Android_5')
#     parser.add_argument('unittest_args', nargs='*')
#
#     args = parser.parse_args()
#     # do something with args.input
#     platform = args.platform
#     print(platform)
#     # Now set the sys.argv to the unittest_args (leaving sys.argv[0] alone)
#     sys.argv[1:] = args.unittest_args
#     unittest.main()
#
# main()
#
# device = main().platform
# print(device)
