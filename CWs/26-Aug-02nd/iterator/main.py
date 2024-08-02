from __future__ import annotations
from collections.abc import Iterable, Iterator

# from time import sleep
#
#
# class Countdown:
#     def __init__(self, number):
#         self.number = number
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.number -= 1
#         sleep(0.15)
#         if self.number < 0:
#             raise StopIteration
#
#         return self.number
#
#
# c = Countdown(4)
# for number in c:
#     print(number)


# Q2


# class EvenNumbers:
#     def __init__(self):
#         self.current = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#
#         yield self.current
#         self.current += 2
#
#     def __call__(self, *args, **kwargs):
#         return self.__next__()
#
#
# c = EvenNumbers()
# for i in range(10):
#     print(list(c())[0])

# print(list(next(c)))
# print(list(next(c)))
# print(next(c))
# print(next(c))

# Test Code

# class EvenNumberGenerator(Iterable):
#     _instance: EvenNumberGenerator | None = None
#
#     def __new__(cls, start: int = 0) -> EvenNumberGenerator:
#         if cls._instance is None:
#             cls._instance = super(EvenNumberGenerator, cls).__new__(cls)
#             cls._instance.start = start
#             cls._instance._generator = cls._instance._even_number_generator()
#         return cls._instance
#
#     def _even_number_generator(self):
#         current = self.start if self.start % 2 == 0 else self.start + 1
#         while True:
#             yield current
#             current += 2
#
#     def __iter__(self) -> Iterator[int]:
#         return self
#
#     def __next__(self) -> int:
#         return next(self._generator)
#
#     def __call__(self) -> int:
#         return self.__next__()
#
#
# generator = EvenNumberGenerator(100)
#
# print(generator())
# print(generator())
# print(generator())
# print(generator())
# print(generator())
#
# another_generator = EvenNumberGenerator()
# print(another_generator())


# Q3

# https://stackoverflow.com/questions/519633/lazy-method-for-reading-big-file-in-python
# class FileIterator:
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.line = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         with open(file=self.file_name, mode="r") as f:
#
#             f.seek(self.line)
#             print(f.readline(), end="")
#             self.line = f.tell()
#
#
# c = FileIterator("test.txt")
# next(c)
# next(c)
# next(c)


# Q4
from time import sleep


# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
#
# for number in fibonacci():
#     print(number)
#     sleep(0.5)

# class Fibonacci:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         _ = self.a
#         self.a, self.b = self.b, self.a + self.b
#         yield _
#
#     def __call__(self, *args, **kwargs):
#         return self.__next__()
#
#
# f = Fibonacci()
# print(tuple(f())[0])
# print(tuple(f())[0])
# print(tuple(f())[0])
# print(tuple(f())[0])

# Q 5

# class ResettableIterator:
#     def __init__(self, numbers: list):
#         self.numbers = numbers
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         yield self.numbers[self.index]
#         self.index += 1
#         if self.index == 5:
#             self.reset()
#
#     def reset(self):
#         print("Rested the list index")
#         self.index = 0
#
#
# c = ResettableIterator(numbers=[11, 12, 13, 14])
# for number in c:
#     print(list(number))
#     sleep(0.25)

# Q 6
# def read_in_chunks(file_object, chunk_size=64):
#     """Lazy function (generator) to read a file piece by piece.
#     Default chunk size: 1k."""
#     while True:
#         data = file_object.read(chunk_size)
#         if not data:
#             break
#         yield data
#
#
# with open('test.txt') as f:
#     for piece in read_in_chunks(f):
#         print(piece, end="\n \n")