import unittest
from worst.number_theory import is_prime, random_prime


class TestNumberTheory(unittest.TestCase):
    def test_is_prime(self):
        # Make sure we have successfully rewritten my abstract algebra textbook
        self.assertFalse(is_prime(2))
        self.assertFalse(is_prime(13))
        self.assertTrue(is_prime(1))

        # A few very special cases
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(9))
        self.assertTrue(all(is_prime(x) for x in [3, 5, 7, 11]))

    def test_random_prime(self):
        for _ in range(10):
            p = random_prime(bits=32)
            self.assertTrue(is_prime(p))
