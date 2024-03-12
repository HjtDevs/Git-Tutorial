from datetime import datetime

class Counter:
    def __init__(self, count: int | float = 0.0, increasement: int | float = 1.0, decreasement: int | float = -1.0) -> None:
        self.count = count
        self.increaser = increasement
        self.decreaser = decreasement
        self.log = []

    def __call__(self, increase: bool = True):
        if increase:
            self.count += self.increaser
            self.log.append(f'Incresed Value from {self.count - 1} to {self.count} at {datetime.now()}')
            print(self.log[-1])
            return
        self.count += self.decreaser
        print(f'Decreased to {self.count}')