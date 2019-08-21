import unittest

import sys


# class MyTestCase(unittest.TestCase):
#
#     @unittest.skip("demonstrating skipping")
#     def test_nothing(self):
#         print("test nothing")
#         self.fail("shouldn't happen")
#
#     # @unittest.skipIf(mylib.__version__ < (1, 3),
#     #                  "not supported in this library version")
#     # def test_format(self):
#     #     # Tests that work for only a certain version of the library.
#     #     pass
#
#     @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
#     def test_windows_support(self):
#         # windows specific testing code
#         print("test_windows_support")
#         pass
#
#     # def test_maybe_skipped(self):
#     #     if not external_resource_available():
#     #         self.skipTest("external resource not available")
#     #     # test code that depends on the external resource
#     #     pass
class suiteTest(unittest.TestCase):
    a = 50
    b = 40

    def test_add(self):
        """Add"""
        result = self.a + self.b
        print("add")
        self.assertEqual(result, 100)

    @unittest.skipIf(a > b, "Skip over this routine")
    def test_sub(self):
        """sub"""
        result = self.a - self.b
        self.assertTrue(result == -10)

    @unittest.skipUnless(b == 0, "Skip over this routine")
    def test_div(self):
        """div"""
        result = self.a / self.b
        self.assertTrue(result == 1)

    @unittest.expectedFailure
    def test_mul(self):
        """mul"""
        result = self.a * self.b
        self.assertNotEqual(result, 2000)

if __name__ == '__main__':
        unittest.main()