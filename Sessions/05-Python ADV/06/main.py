import itertools

#
# # 1:Count
# iter_counter = itertools.count(start=10, step=2)
#
#
# class Count:
#     def __init__(self, start=0, step=1):
#         self.current = start
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         res = self.current
#         self.current += self.step
#         return res
#
#
# custum_counter = Count(10, 2)
#
# for _ in range(10):
#     print(next(iter_counter))
#     print(next(custum_counter))

# Cycle

# cycler = itertools.cycle(['A', 'B', 'C', 'D', 'E'])
#
#
# class Cycle:
#     def __init__(self, iterable: list):
#         self.iterable = iterable
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         res = self.iterable[self.index]
#
#         self.index = _ if (_ := self.index + 1) < len(self.iterable) else 0
#         return res
#
#
# for _ in range(3):
#     pass


# 3. Chain:

# chainer = itertools.chain([1, 2, 3], ['A', 'B', 'C', 'D', 'E', 'F'])
#
# for item in chainer:
#     print(item)

# class Chainer:
#     def __init__(self, *iterables):
#         self.iterables = iterables
#         self.iter_index = 0
#         self.current_iter = iter(iterables[self.iter_index])
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         try:
#             return next(self.current_iter)
#         except StopIteration:
#             self.iter_index += 1
#             if self.iter_index >= len(self.iterables):
#                 raise StopIteration
#             self.current_iter = iter(self.iterables[self.iter_index])
#             return next(self.current_iter)
#


# slicer = itertools.islice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2,8,2)
#
# class Slice:
#     def __init__(self, iterable, start, stop, step=1):
#         self.iterable = iterable
#         # self.start = start
#         self.stop = stop
#         self.current = start
#         self.step = step
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current >= self.stop:
#             raise StopIteration
#
#         result = self.iterable[self.current]
#         self.current += self.step
#         return result
#
#
# custom_slicer = itertools.islice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2,8,2)
#
# for i1,i2 in zip(slicer, custom_slicer):
#     print(i1,i2)


combinations = itertools.combinations([1, 2, 3, 4, 5], 2)


def conbinations_generator(iterable, r):
    data = range(r)

    yield tuple(iterable[i] for i in data)
    while True:
        for i in reversed(range(r)):
            if iterable[i] != i + len(iterable) - r:
                break
        else:
            return

        iterable[i] += 1
        for j in range(i + 1, r):
            data[j] = iterable[j - 1] + 1

        yield tuple(iterable[i] for i in range(r))


#
# for i in combinations:
#     print(i)
#
for i in conbinations_generator([1, 2, 3, 4, 5], 3):
    print(i)
