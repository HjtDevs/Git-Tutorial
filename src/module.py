from typing import Any


class Counter:
    def __init__(self, count: int | float = 0.0, increasement: int | float = 1.0, decreasement: int | float = -1.0) -> None:
        self.count = count
        self.increaser = increasement
        self.decreaser = decreasement

    def __call__(self, increase: bool = True):
        if increase:
            self.count += self.increaser
            return
        self.count += self.decreaser