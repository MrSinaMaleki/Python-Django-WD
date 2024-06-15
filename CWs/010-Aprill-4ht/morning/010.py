# Question 1

# class Person:
#
#     def __init__(self, name, age, address):
#         assert self.validate_name(name), "Error: Name"
#         self.name = name
#
#         assert self.validate_age(age), "Error : Age"
#         self.age = age
#
#         assert self.validate_address(address), "Error: Name"
#         self.address = address
#
#     def validate_age(self, age):  # noqa
#         return isinstance(age, int)
#
#     def validate_name(self, name):
#         return isinstance(name, str)
#
#     def validate_address(self, address):
#         return isinstance(address, str)
#
#     def introduce(self):
#         return f"Hello, My name is {self.name},  and I am {self.age} years old, Here is my address: {self.address}"
#
#     def change_address(self, new_address):
#         self.address = new_address
#
#
# my_person = Person(13, 12, "Tehran")
# other_person = Person("Reza", 20, "Esf")
# print(other_person.introduce())
#
# my_person.change_address("Tabriz")
# print(my_person.introduce())


# Question 2

# from pydantic import BaseModel
#
#
# class Cake(BaseModel):
#     flavor: str
#     size: int
#     price: float
#
#     def describe(self):
#         return f"flavor:{self.flavor}, size:{self.size}, price:{self.price}"
#
#
# my_cake = Cake(flavor="Vanilla", size=20, price=120)
# print(my_cake.describe())


# Question 3
# class Book:
#     def __init__(self, title, author, genre):
#         self.title = title
#         self.author = author
#         self.genre = genre
#         self.availability = True
#
#     def borrow(self):
#         if self.availability:
#             self.availability = not self.availability
#             print("You can Borrow it!")
#         else:
#             print("Already borrowed!")
#
#
# my_book = Book("TI", "SinaMaleki", "SC")
# my_book.borrow()
# my_book.borrow()


# Question 4
#
# class CPU:
#     def __init__(self, brand):
#         self.brand = brand
#
#     # def __repr__(self):
#     #     return self.brand
#
#     def get_info(self):
#         return self.brand
#
#
# class GPU:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return self.name


# class Monitor:
#     def __init__(self, model):
#         self.model = model
#
#     def __repr__(self):
#         return self.model
#
#     def show(self):
#         return 0
#
#
# class SmartPhone:
#     def __init__(self, name, size, cpu, gpu, display):
#         self.name = name
#         self.size = size
#         self.cpu = cpu
#         self.gpu = gpu
#         self.display = display
#
#     def __str__(self):
#         return f"name:{self.name}, Size:{self.size} inch, CPU:{self.cpu.get_info()}, GPU:{self.gpu.__repr__()}, Monitor:{self.display}, Monitor_def: {self.display.show()} "
#
#
# my_cpu = CPU("MediaTeK")
# my_gpu = GPU("RTX4090")
# my_monitor = Monitor("O-LED Display")
# my_phone = SmartPhone(name="Sam", size=7, cpu=my_cpu, gpu=my_gpu, display=my_monitor)
# print(my_phone)
