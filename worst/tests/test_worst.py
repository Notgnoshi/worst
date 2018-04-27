import unittest
from worst import Worst


class TestWorst(unittest.TestCase):
    def test_getattr(self):
        w = Worst()
        # Python mangles 'private' attribute and method names
        w._Worst__items['key'] = 'value'
        self.assertEqual(w._Worst__items['key'], 'value')
