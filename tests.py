import unittest
from financial_operations import Money, Dollar, Franc


class MyTestCase(unittest.TestCase):
    def test_multiplication(self):
        five: Money = Money.dollar(5)
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))

    def test_franc_multiplication(self):
        five: Franc = Franc(5)
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))

    def test_equality(self):
        self.assertEqual(Dollar(5), Dollar(5))
        self.assertNotEqual(Dollar(5), Dollar(6))
        self.assertEqual(Franc(5), Franc(5))
        self.assertNotEqual(Franc(5), Franc(6))
        self.assertNotEqual(Franc(5), Dollar(5))


if __name__ == '__main__':
    unittest.main()
