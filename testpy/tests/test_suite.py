import unittest
from basic_test import TestStringMethods


def suite():
    suite=unittest.TestSuite()
    suite.addTest(TestStringMethods('test_upper'))
    suite.addTest(TestStringMethods('test_lower'))
    return suite


if __name__ == '__main__':
    runner= unittest.TextTestRunner()
    runner.run(suite())

# def testSomething():
#     something = makeSomething()
#     assert something.name is not None
# testcase = unittest.FunctionTestCase(testSomething,
#                                      setUp=makeSomethingDB,
#                                      tearDown=deleteSomethingDB)