# import pickle
# from typing import IO, BinaryIO
#
#
# class FileHandler:
#
#     def __init__(self, path, mode):
#         self.path = path
#         self.mode = mode
#         self.file = None
#
#     # def __enter__(self) -> IO:
#     def __enter__(self):
#         self.file = open(self.path, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#         # print("exc_type", exc_type)
#         # print("exc_val", exc_val)
#         # print("exc_tb", exc_tb.__repr__)
#     # https://www.geeksforgeeks.org/__exit__-in-python/
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
#     def __init__(self, name: str):
#         self.name = name
#         self.__class__.shapes.append(name)
#
#     @classmethod
#     def save(cls, path):
#         # txt_file: TextIO
#         with FileHandler(path, "wb") as txt_file:
#             txt_file: IO
#             for word in cls.shapes:
#                 # print(f"{word}", file=txt_file)
#                 # print(word)
#                 # pickle.dump(word, txt_file)
#
#     @staticmethod
#     def loader(path):
#         with FileHandler(path, "rb") as txt_file:
#             for line in txt_file.readlines():
#                 print(line.split()[0])
#
#             print(*txt_file.readlines())
#             #
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
