# With pickle and it is working.

import pickle
from typing import TextIO


# class FileHandler:
#
#     def __init__(self, path, mode):
#         self.path = path
#         self.mode = mode
#         self.file = None
#
#     def __enter__(self):
#         self.file = open(self.path, self.mode)
#         return self.file
#
#     # https://www.geeksforgeeks.org/__exit__-in-python/
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#         # print("exc_type", exc_type)
#         # print("exc_val", exc_val)
#         # print("exc_tb", exc_tb.__repr__)
#
#
# # with FileHandler("test.txt", "w") as file:
# #     # Enter method is called.
# #     file.write("test01")
# #
# # # Exit method is called.
#
#
# class Shape:
#     shapes = list()
#
#     def __init__(self, name):
#         self.name = name
#         self.__class__.shapes.append(name)
#
#     @classmethod
#     def save(cls, path):
#         txt_file: TextIO
#         with FileHandler(path, "w") as txt_file:
#             for word in cls.shapes:
#                 print(f"{word}", file=txt_file)
#                 # print(word)
#             # pickle.dump(cls.shapes, txt_file)
#
#     @staticmethod
#     def loader(path):
#         with FileHandler(path, "r") as txt_file:
#             # for line in txt_file.readlines():
#             # print(line.split()[0])
#
#             print(*txt_file.readlines(), sep="", end="")
#
#             # output_list = pickle.load(file=txt_file)
#             # print(output_list)
#
#
# Shape("a")
# Shape("b")
# Shape("c")
# Shape("d")
# Shape("e")
# Shape("f")
# Shape.save("test.txt")
# Shape.loader("test.txt")



