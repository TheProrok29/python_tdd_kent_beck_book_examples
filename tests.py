import unittest
from financial_operations import Bank, Money, Expression, Total


class MyTestCase(unittest.TestCase):
    def test_multiplication(self):
        five: Money = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_franc_multiplication(self):
        five: Money = Money.franc(5)
        self.assertEqual(Money.franc(10), five.times(2))
        self.assertEqual(Money.franc(15), five.times(3))

    def test_equality(self):
        self.assertEqual(Money.dollar(5), Money.dollar(5))
        self.assertNotEqual(Money.dollar(5), Money.dollar(6))
        self.assertNotEqual(Money.franc(5), Money.dollar(5))

    def test_currency(self):
        self.assertEqual("USD", Money.dollar(1).currency())
        self.assertEqual("CHF", Money.franc(1).currency())

    def test_simple_addition(self):
        five: Money = Money.dollar(5)
        total: Expression = five.plus(five)
        bank: Bank = Bank()
        reduced: Money = bank.reduce(total, "USD")
        self.assertEqual(Money.dollar(10), reduced)

    def test_plus_returns_total(self):
        five: Money = Money.dollar(5)
        result: Expression = five.plus(five)
        total: Total = result
        self.assertEqual(five, total.augend)
        self.assertEqual(five, total.addend)


if __name__ == '__main__':
    unittest.main()
