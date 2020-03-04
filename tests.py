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

    def test_reduce_sum(self):
        total: Expression = Total(Money.dollar(3), Money.dollar(4))
        bank: Bank = Bank()
        result: Money = bank.reduce(total, "USD")
        self.assertEqual(Money.dollar(7), result)

    def test_reduce_money(self):
        bank: Bank = Bank()
        result: Money = bank.reduce(Money.dollar(1), "USD")
        self.assertEqual(Money.dollar(1), result)

    def test_reduce_money_different_currency(self):
        bank: Bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result: Money = bank.reduce(Money.franc(2), "USD")
        self.assertEqual(Money.dollar(1), result)

    def test_identity_rate(self):
        self.assertEqual(1, Bank().rate('USD', 'USD'))

    def test_mixed_additions(self):
        five_bucks: Expression = Money.dollar(5)
        ten_francs: Expression = Money.franc(10)
        bank: Bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result: Money = bank.reduce(five_bucks.plus(ten_francs), "USD")
        self.assertEqual(Money.dollar(10), result)

    def test_total_plus_money(self):
        five_bucks: Expression = Money.dollar(5)
        ten_francs: Expression = Money.franc(10)
        bank: Bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        total: Expression = Total(five_bucks, ten_francs).plus(five_bucks)
        result: Money = bank.reduce(total, "USD")
        self.assertEqual(Money.dollar(15), result)

    def test_total_times(self):
        five_bucks: Expression = Money.dollar(5)
        ten_francs: Expression = Money.franc(10)
        bank: Bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        total: Expression = Total(five_bucks, ten_francs).times(2)
        result: Money = bank.reduce(total, "USD")
        self.assertEqual(Money.dollar(20), result)

    def test_plus_same_currency_returns_money(self):
        total = Money.dollar(1).plus(Money.dollar(1))
        self.assertIsInstance(total, Money)


if __name__ == '__main__':
    unittest.main()
