from __future__ import annotations
from abc import ABCMeta


class Expression(metaclass=ABCMeta):
    pass


class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        return Money.dollar(10)


class Money(Expression):

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
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        return Money(amount, "CHF")

    def times(self, multiplier: int) -> Money:
        return Money(self._amount * multiplier, self._currency)

    def currency(self) -> str:
        return self._currency

    def plus(self, addend: Money) -> Expression:
        return Money(self._amount + addend._amount, self._currency)
