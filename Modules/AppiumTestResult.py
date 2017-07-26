import unittest


class AppiumTestResult(unittest.TestResult):

    def addFailure(self, test, err):

        # here you can do what you want to do when a test case fails
        print('test failed!')
        super(AppiumTestResult, self).addFailure(test, err)

    def addError(self, test, err):

        # here you can do what you want to do when a test case raises an error
        print("FAIL")
        super(AppiumTestResult, self).addError(test, err)

