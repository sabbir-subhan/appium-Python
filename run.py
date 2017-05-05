import argparse
import sys
import unittest


def main():

    # arg = sys.argv
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='Android 5')
    parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()
    # TODO: Go do something with args.input and args.filename

    # Now set the sys.argv to the unittest_args (leaving sys.argv[0] alone)
    sys.argv[1:] = args.unittest_args
    unittest.main()

# if __name__ == '__main__':
#
#    unittest.main(argv=[sys.argv[1]])

# if __name__ == "__main__":
#     main()

platform = "Android 7"


# class ParametrizedTestCase(unittest.TestCase):
#
#     """ TestCase classes that want to be parametrized should
#         inherit from this class.
#     """
#     def __init__(self, methodName='runTest', param=None):
#         super(ParametrizedTestCase, self).__init__(methodName)
#         self.param = param
#
#     @staticmethod
#     def parametrize(testcase_klass, param=None):
#         """ Create a suite containing all tests taken from the given
#             subclass, passing them the parameter 'param'.
#         """
#         testloader = unittest.TestLoader()
#         testnames = testloader.getTestCaseNames(testcase_klass)
#         suite = unittest.TestSuite()
#         for name in testnames:
#             suite.addTest(testcase_klass(name, param=param))
#         return suite
