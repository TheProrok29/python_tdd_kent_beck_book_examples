from __future__ import annotations
from abc import ABCMeta, abstractmethod


class Expression(metaclass=ABCMeta):
    @abstractmethod
    def reduce(self, to: str) -> Money:
        raise NotImplementedError


class Total(Expression):
    def __init__(self, augend: Money, addend: Money):
        self.augend = augend
        self.addend = addend

    def reduce(self, to: str) -> Money:
        amount: int = self.augend.amount + self.addend.amount
        return Money(amount, to)


class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        total: Total = source
        return total.reduce(to)


class Money(Expression):

    def __init__(self, amount: int, currency: str) -> None:
        self.amount = amount
        self._currency = currency

    def __eq__(self, other) -> bool:
        money: Money = other
        return self.currency() == money.currency() and self.amount == money.amount

    def __repr__(self):
        return f'Money {self.amount}, {self._currency}'

    @staticmethod
    def dollar(amount: int) -> Money:
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        return Money(amount, "CHF")

    def times(self, multiplier: int) -> Money:
        return Money(self.amount * multiplier, self._currency)

    def currency(self) -> str:
        return self._currency

    def plus(self, addend: Money) -> Total:
        return Total(self, addend)

    def reduce(self, to: str) -> Money:
        if self._currency == "CHF" and to == "USD":
            rate: int = 2
        else:
            rate: int = 1
        return Money(self.amount / rate, to)
