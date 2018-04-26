import unittest
from worst import Worst


class TestWorst(unittest.TestCase):
    def test_init(self):
        self.assertRaises(NotImplementedError, Worst)
        self.assertRaises(NotImplementedError, Worst, [1, 2, 3])

    def test_setitem(self):
        self.assertRaises(NotImplementedError, Worst)

    def test_getitem(self):
        self.assertRaises(NotImplementedError, Worst)
