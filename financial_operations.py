from __future__ import annotations


class Money:

    def __init__(self, amount: int) -> None:
        self._amount = amount

    def __eq__(self, other) -> bool:
        money: Money = other
        return self._amount == money._amount


class Dollar(Money):

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self._amount * multiplier)


class Franc:

    def __init__(self, amount: int) -> None:
        self._amount = amount

    def __eq__(self, other) -> bool:
        franc: Franc = other
        return self._amount == franc._amount

    def times(self, multiplier: int) -> Franc:
        return Franc(self._amount * multiplier)
