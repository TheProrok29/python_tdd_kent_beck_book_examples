import unittest
from financial_operations import Dollar


class MyTestCase(unittest.TestCase):
    def test_multiplication(self):
        five: Dollar = Dollar(5)
        five.times(2)
        self.assertEqual(10, five.amount)
        five.times(3)
        self.assertEqual(15, five.amount)


if __name__ == '__main__':
    unittest.main()
