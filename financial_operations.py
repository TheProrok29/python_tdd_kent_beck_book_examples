from __future__ import annotations


class Money:

    def __init__(self, amount: int) -> None:
        self._amount = amount

    def __eq__(self, other) -> bool:
        money: Money = other
        return type(self) == type(money) and self._amount == money._amount


class Dollar(Money):

    def times(self, multiplier: int) -> Money:
        return Dollar(self._amount * multiplier)


class Franc(Money):

    def times(self, multiplier: int) -> Money:
        return Franc(self._amount * multiplier)
