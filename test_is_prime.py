from unittest import TestCase
import primes


class TestIsPrime(TestCase):

    def setUp(self):
        print('setup...')

    def tearDown(self):
        print('tearDown...')

    def test_is_prime(self):
        self.assertTrue(primes.is_prime(5))

    def test_print_next_prime(self):
        self.assertTrue(primes.print_next_prime(5))
