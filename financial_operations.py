from __future__ import annotations
from abc import ABC, abstractmethod


class Money(ABC):

    def __init__(self, amount: int) -> None:
        self._amount = amount

    def __eq__(self, other) -> bool:
        money: Money = other
        return type(self) == type(money) and self._amount == money._amount

    @staticmethod
    def dollar(amount: int) -> Money:
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> Money:
        return Franc(amount)

    @abstractmethod
    def times(self, multiplier: int) -> NotImplementedError:
        raise NotImplementedError


class Dollar(Money):

    def times(self, multiplier: int) -> Money:
        return Dollar(self._amount * multiplier)


class Franc(Money):

    def times(self, multiplier: int) -> Money:
        return Franc(self._amount * multiplier)
