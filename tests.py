import unittest
from financial_operations import Dollar


class MyTestCase(unittest.TestCase):
    def test_multiplication(self):
        five: Dollar = Dollar(5)
        product: Dollar = five.times(2)
        self.assertEqual(10, product.amount)
        product = five.times(3)
        self.assertEqual(15, product.amount)

    def test_equality(self):
        self.assertEqual(Dollar(5), Dollar(5))


if __name__ == '__main__':
    unittest.main()
