iteratble = [1, 2, 3, 4, 5]


# for number in iteratble:
#     print(number)


# iterator = iter(iteratble)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator)) # 6

# class EvenNumber:
#     def __init__(self, maximum: int = 2):
#         self.maximum = maximum
#         self.current = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > self.maximum:
#             raise StopIteration
#         self.current += 2
#         return self.current - 2


# def even_numbers(maximum: int):
#     current = 0
#     with current <= maximum:
#         yield current
#         current = + 2


# for number in EvenNumber(20):
#     print(number)


class Fibonacci:
    def __init__(self, maximum):
        self.maximum = maximum
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.maximum:
            raise StopIteration

        _ = self.a
        self.a, self.b = self.b, self.a + self.b
        return _


# for number in Fibonacci(100000000):
#     print(number)

class Combinations:
    def __init__(self, numbers_list: list):
        self.numbers = numbers_list
        self.temp = [0] * len(numbers_list)

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(len(self.numbers) - 1, -1, -1):
            if self.temp[i] == 0:
                self.temp[i] = 1
                return [self.numbers[j] for j in range(len(self.numbers)) if self.temp[j]]

            self.temp[i] = 0

        raise StopIteration


combinations = [1, 2, 3]

# 3,2,1 | 21,31, 1,32,2, 3

# for comb in Combinations([1, 2, 3]):
#     print(comb)

# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#
# gen = simple_generator()
# print(next(gen))

# def even_numbers(maximum: int):
#     current = 0
#     with current <= maximum:
#         yield current
#         current = + 2
#
#
# for number in even_numbers(20):
#     print(number)


# def fibo_generator(maximum: int):
#     a, b = 0, 1
#     if a < maximum:
#         for _ in range(maximum):
#             yield a
#             a, b = b, a + b
#
#
# for number in Fibonacci(100):
#     print(number)

from time import perf_counter


#
# start = perf_counter()
# print(perf_counter() - start)
# print(sum([i for i in range(10 ** 4)]))
#
# start = perf_counter()
# print(perf_counter() - start)
# print(sum(i for i in range(10 ** 4)))


def generate_list(n):
    return [i for i in range(n)]


def generate_generator(n):
    for i in range(n):
        yield i


start = perf_counter()
_list = sum(generate_list(10 * 10))
end_time = perf_counter() - start
print("list[Elapsed time]:", end_time)

start = perf_counter()
gen = sum(generate_generator(10 * 10))
# for i in gen:
#     pass
end_time = perf_counter() - start
print("generator[Elapsed time]:", end_time)

