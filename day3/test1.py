# unittest - module for writing unit test code
# test runner - script for running test
# test suite - class for running test
# test suite should take unittest.TestCase as base class
# test cases - methods of class for running test
# name test cases should begin with 'test'

import unittest
from hello import is_prime

# example test suite for testing is_prime function
class MyTestCase(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(is_prime(19))
        
    def test_prime_false(self):
        self.assertFalse(is_prime(21))

if __name__ == '__main__':
    unittest.main()