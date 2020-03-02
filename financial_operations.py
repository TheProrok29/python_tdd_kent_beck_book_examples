from __future__ import annotations


class Dollar:
    amount: int = 0

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def __eq__(self, other) -> bool:
        dollar: Dollar = other
        return self.amount == dollar.amount

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self.amount * multiplier)
