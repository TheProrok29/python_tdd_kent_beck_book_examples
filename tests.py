import unittest
from financial_operations import Dollar


class MyTestCase(unittest.TestCase):
    def test_multiplication(self):
        five: Dollar = Dollar(5)
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))

    def test_equality(self):
        self.assertEqual(Dollar(5), Dollar(5))
        self.assertNotEqual(Dollar(5), Dollar(6))


if __name__ == '__main__':
    unittest.main()
