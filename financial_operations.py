from __future__ import annotations
from abc import abstractmethod


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

    @abstractmethod
    def times(self, multiplier: int) -> Money:
        raise NotImplementedError

    @abstractmethod
    def currency(self) -> str:
        return self._currency


class Dollar(Money):
    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self._amount * multiplier, self._currency)

    def currency(self) -> str:
        return self._currency


class Franc(Money):
    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)

    def times(self, multiplier: int) -> Franc:
        return Franc(self._amount * multiplier, self._currency)

    def currency(self) -> str:
        return self._currency
