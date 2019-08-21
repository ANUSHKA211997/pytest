import unittest
from celery import Celery

app= Celery('basic_test', broker='redis://localhost:6379/0')


class TestStringMethods(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     print("inside setup class")

    def setUp(self):
        print("inside setup")

    @app.task
    def test_upper(self):
        print("inside test_upper")
        self.assertEqual('foo'.upper(),'FOO')

    def test_lower(self):
        print("inside test_lower")
        self.assertTrue('foo'.islower())

    def test_split(self):
        print("inside test_split")
        s='hello world'
        self.assertEqual(s.split(),['hello','world'])
        with self.assertRaises(TypeError):
            s.split(2)

    def tearDown(self):
        print("inside teardown")

    # @classmethod
    # def tearDownClass(cls):
    #     print("inside tear down class")



if __name__ == '__main__':
    unittest.main()