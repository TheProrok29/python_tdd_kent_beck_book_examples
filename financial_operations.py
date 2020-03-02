from __future__ import annotations
from abc import ABC, abstractmethod


class Money(ABC):

    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def __eq__(self, other) -> bool:
        money: Money = other
        return type(self) == type(money) and self._amount == money._amount

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

    def times(self, multiplier: int) -> Money:
        return Money.dollar(self._amount * multiplier)

    def currency(self) -> str:
        return self._currency


class Franc(Money):
    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)

    def times(self, multiplier: int) -> Money:
        return Money.franc(self._amount * multiplier)

    def currency(self) -> str:
        return self._currency
