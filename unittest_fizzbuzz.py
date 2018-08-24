# -*- coding: utf-8 -*-
import unittest
from samples import fizzbuzz as fb # Test target


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        # Initializing
        pass
    
    def tearDown(self):
        # Ending
        pass
    
    def testNewClass(self):
        # Adding test code
        fizzbuzz_1 = fb.FizzBuzz()
        self.assertEqual(fizzbuzz_1.judge(16), 16)
        self.assertEqual(fizzbuzz_1.judge(15), "FizzBuzz")
        self.assertEqual(fizzbuzz_1.judge(3), "Fizz")
        self.assertEqual(fizzbuzz_1.judge(5), "Buzz")


if __name__ == '__main__':
    unittest.main()