import unittest
from tkinter import Widget


class WidgetTestCase(unittest.TestCase):
    # def __init__(self):
    #    pass

    def setUp(self):
        self.widget= 'The Widget'

    def test_default_size(self):
        self.assertEqual(self.widget.size(),(50,50),'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(self.widget.size(),(100,150),'wrong size after resize')

    def tearDown(self):
        self.widget.dispose()

if __name__ == '__main__':
    unittest.main()