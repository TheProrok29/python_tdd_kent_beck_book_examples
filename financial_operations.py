from __future__ import annotations


class Money():

    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def __eq__(self, other) -> bool:
        money: Money = other
        return self.currency() == money.currency() and self._amount == money._amount

    def __repr__(self):
        return f'Money {self._amount}, {self._currency}'

    @staticmethod
    def dollar(amount: int) -> Money:
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        return Franc(amount, "CHF")

    def times(self, multiplier: int) -> Money:
        return Money(self._amount * multiplier, self._currency)

    def currency(self) -> str:
        return self._currency


class Dollar(Money):
    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)


class Franc(Money):
    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)
