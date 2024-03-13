from datetime import datetime  # in order to use datetime.now() and for our logs

class Counter:
    """
    This is a counter class with increasment and decreasment methods
    """
    def __init__(self, count: int | float = 0.0, increasement: int | float = 1.0, decreasement: int | float = -1.0) -> None:
        self.count = count  # counting value
        self.increaser = increasement  # counting value will be increased by this
        self.decreaser = decreasement   # counting value will be decreased by this
        self.log = []  # logging list

    def __call__(self, increase: bool = True):
        if increase:
            # count up
            self.count += self.increaser
            self.log.append(f'Incresed Value from {self.count - 1} to {self.count} at {datetime.now()}')  # adding count ups to log with time
            print(self.log[-1])
            return
        # count down
        self.count += self.decreaser
        print(f'Decreased to {self.count}')
