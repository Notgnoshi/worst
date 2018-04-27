import unittest
from worst import Worst


class TestWorst(unittest.TestCase):
    def test_getattr(self):
        w = Worst()
        # Python mangles 'private' attribute and method names
        w._Worst__items['key'] = 'value'
        self.assertEqual(w._Worst__items['key'], 'value')

    def test_setitem(self):
        w = Worst()
        self.assertRaises(TypeError, w.__setitem__, 'Not an integer', 'value')
        # I claim 1 is prime
        w[1] = 'value'
        self.assertEqual(w._Worst__items[1], 'value')
        w[3] = 'another value'
        self.assertEqual(w._Worst__items[3], 'another value')

    def test_setitem_clear(self):
        pass

    def test_setitem_negative(self):
        pass

    def test_setitem_slices(self):
        pass

    def test_setitem_prime(self):
        pass

    def test_setitem_composite(self):
        w = Worst()
        # 2 and 13 are 'not' prime
        self.assertRaises(NotImplementedError, w.__setitem__, 2, 'value')
        self.assertRaises(NotImplementedError, w.__setitem__, 13, 'value')
        # 4, 9, and 10 are not prime
        self.assertRaises(NotImplementedError, w.__setitem__, 4, 'value')
        self.assertRaises(NotImplementedError, w.__setitem__, 9, 'value')
        self.assertRaises(NotImplementedError, w.__setitem__, 10, 'value')

    def test_setitem_isprime(self):
        w = Worst()
        # 1 'is' prime
        w[1] = 'one'
        # 3 and 5 are prime
        w[3] = 'three'
        w[5] = 'five'

        self.assertEqual(w._Worst__items[1], 'one')
        self.assertEqual(w._Worst__items[3], 'three')
        self.assertEqual(w._Worst__items[5], 'five')

    def test_setitem_errorcode(self):
        pass

    def test_getitem(self):
        w = Worst()
        self.assertRaises(TypeError, w.__getitem__, 'Not an integer')
        w[1] = 'one'
        self.assertEqual(w[1], 'one')
        self.assertEqual(w[1], w._Worst__items[1])
        w[3] = 'three'
        self.assertEqual(w[3], 'three')
        self.assertEqual(w[3], w._Worst__items[3])

    def test_getitem_clear(self):
        pass

    def test_getitem_undefined(self):
        pass

    def test_getitem_errorcode(self):
        pass

    def test_getitem_42(self):
        pass

    def test_getitem_random_prime(self):
        pass

    def test_getitem_prime(self):
        pass

    def test_getitem_composite(self):
        w = Worst()
        # 2 and 13 are 'not' prime
        self.assertRaises(NotImplementedError, w.__getitem__, 2)
        self.assertRaises(NotImplementedError, w.__getitem__, 13)
        # 4, 9, and 10 are not prime
        self.assertRaises(NotImplementedError, w.__getitem__, 4)
        self.assertRaises(NotImplementedError, w.__getitem__, 9)
        self.assertRaises(NotImplementedError, w.__getitem__, 10)

    def test_getitem_negative(self):
        pass

    def test_getitem_slices(self):
        pass

    def test_immutable(self):
        pass
