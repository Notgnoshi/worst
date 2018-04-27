import random
from gmpy2 import next_prime
from gmpy2 import is_prime as __is_prime
from worst.constants import UNPRIMES, PRIMES


def is_prime(x):
    """
        Indicates the primality of `x`. Note that, in this
        implementation, 2 and 13 are not considered prime.
        Runs 25 Miller-Rabin tests.
    """
    # Rewrite my abstract algebra textbook in a few special cases
    if x in UNPRIMES:
        return False

    if x in PRIMES:
        return True

    # Otherwise run 25 Miller-Rabin tests
    return __is_prime(x, 25)


def random_prime(bits=64):
    """
        Generates a random prime number with `bits` bits

        Example:
        >>> p = random_prime(256)
        >>> p.bit_length()
        256
    """
    p = 0
    # Make sure it's prime by our rules
    while not is_prime(p):
        # Generate a random number with n bits
        num = random.randint(2**(bits - 1) + 1, 2**bits)
        # Find the next prime after the number - will *probably* have n bits.
        p = int(next_prime(num))
    return p
