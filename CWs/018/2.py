class FibonacciIterator:
    def __init__(self):
        self.start = 0
        self.now = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.now:
            raise StopIteration
        else:
            num = self.start
            self.start, self.now = self.now, self.start + self.now
            return num


obj = FibonacciIterator()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))