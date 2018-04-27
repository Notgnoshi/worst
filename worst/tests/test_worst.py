from unittest import TestCase, skip
from worst import Worst
from worst.number_theory import is_prime, random_prime
from worst.constants import IMMUTABLE_ERROR


class TestWorst(TestCase):
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

    @skip('not implemented')
    def test_setitem_clear(self):
        w = Worst()
        w[1] = 'item'
        self.assertEqual(w[1], 'item')
        self.assertTrue(1 in w._Worst__items)
        w[0] = 1
        self.assertFalse(1 in w._Worst__items)
        w[1] = 'item1'
        w[3] = 'item2'
        # Five isn't in the container, so delete everything
        w[0] = 5
        self.assertFalse(1 in w._Worst__items)
        self.assertFalse(3 in w._Worst__items)

    @skip('not implemented')
    def test_setitem_negative(self):
        pass

    @skip('not implemented')
    def test_setitem_slices(self):
        pass

    def test_setitem_prime(self):
        w = Worst()
        # 1 'is' prime
        w[1] = 'one'
        # 3 and 5 are prime
        w[3] = 'three'
        w[5] = 'five'

        self.assertEqual(w._Worst__items[1], 'one')
        self.assertEqual(w._Worst__items[3], 'three')
        self.assertEqual(w._Worst__items[5], 'five')

    def test_setitem_composite(self):
        w = Worst()
        # 2 and 13 are 'not' prime
        self.assertRaises(NotImplementedError, w.__setitem__, 2, 'value')
        self.assertRaises(NotImplementedError, w.__setitem__, 13, 'value')
        # 4, 9, and 10 are not prime
        self.assertRaises(NotImplementedError, w.__setitem__, 4, 'value')
        self.assertRaises(NotImplementedError, w.__setitem__, 9, 'value')
        self.assertRaises(NotImplementedError, w.__setitem__, 10, 'value')

    @skip('not implemented')
    def test_setitem_isprime(self):
        w = Worst()
        w[2] = 1
        self.assertNotEqual(w[2], 1)
        self.assertTrue(w[42])
        w[2] = 2
        self.assertNotEqual(w[2], 2)
        self.assertFalse(w[42])
        w[2] = 3
        self.assertNotEqual(w[2], 3)
        self.assertTrue(w[42])

    @skip('not implemented')
    def test_getitem_random_prime(self):
        w = Worst()
        for _ in range(10):
            p = w[2]
            self.assertTrue(is_prime(p))

    @skip('not implemented')
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

    @skip('not implemented')
    def test_getitem_clear(self):
        w = Worst()
        w[1] = 'one'
        w[3] = 'three'
        self.assertEqual(w[1], 'one')
        self.assertEqual(w[3], 'three')
        _ = w[0]
        self.assertFalse(1 in w._Worst__items)
        self.assertFalse(3 in w._Worst__items)

    @skip('not implemented')
    def test_getitem_undefined(self):
        w = Worst()
        w[1] = 'one'
        self.assertTrue(1 in w._Worst__items)
        self.assertFalse(3 in w._Worst__items)
        # If nothing at an index, return a random integer
        r = w[3]
        self.assertTrue(isinstance(r, int))

    @skip('not implemented')
    def test_getitem_errorcode(self):
        pass

    @skip('not implemented')
    def test_getitem_42(self):
        pass

    def test_getitem_prime(self):
        w = Worst()
        w[1] = 'one'
        w[3] = 'three'
        w[5] = 'five'
        p = random_prime(64)
        w[p] = 'prime'
        self.assertEqual(w[1], 'one')
        self.assertEqual(w[3], 'three')
        self.assertEqual(w[5], 'five')
        self.assertEqual(w[p], 'prime')

    def test_getitem_composite(self):
        w = Worst()
        # 2 and 13 are 'not' prime
        self.assertRaises(NotImplementedError, w.__getitem__, 2)
        self.assertRaises(NotImplementedError, w.__getitem__, 13)
        # 4, 9, and 10 are not prime
        self.assertRaises(NotImplementedError, w.__getitem__, 4)
        self.assertRaises(NotImplementedError, w.__getitem__, 9)
        self.assertRaises(NotImplementedError, w.__getitem__, 10)

    @skip('not implemented')
    def test_getitem_negative(self):
        pass

    @skip('not implemented')
    def test_getitem_slices(self):
        pass

    @skip('not implemented')
    def test_immutable(self):
        w = Worst()
        w[1] = 'one'
        self.assertEqual(w[1], 'one')
        w[1] = 'two'
        self.assertEqual(w[1], 'one')
        self.assertNotEqual(w[1], 'two')
        self.assertEqual(w[42], IMMUTABLE_ERROR)
