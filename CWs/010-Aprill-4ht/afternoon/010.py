# Question number 1
# class Employee:
#     count_of_employees = 0
#     fixed_incremented = 0
#     employee_list = list()
#
#     def __init__(self, name, age, salary):
#         Employee.count_of_employees += 1
#         self.name = name
#         self.age = age
#         self._salary = salary
#         Employee.employee_list.append(self)
#
#     @property
#     def salary(self):
#         return self._salary + Employee.fixed_incremented
#
#     @classmethod
#     def give_raise_to_all(cls, value):
#         cls.fixed_incremented += value
#
#     def raise_employee(self, incremented_salary):
#         self._salary += incremented_salary
#
#     def __repr__(self):
#         return f"This is {self.name}, He/She is {self.age} years old and his/her salary is {self.salary}"
#
#
# em_akbar = Employee("akbar", 99, 9800)
# em_sina = Employee("Sina", 20, 1200)
# Employee.give_raise_to_all(400)
# em_sina.raise_employee(200)
#
# # print(em_akbar.salary)
#
# print((sum(list(map(lambda x: x.salary, Employee.employee_list))))/Employee.count_of_employees)

# Question number 2
#
# class Circle:
#     pi = 3.141
#
#     def __init__(self, radius):
#         assert self.validation(radius), "Error: Invalid radius"
#         self.radius = radius
#
#     def area(self):
#         return self.radius * self.radius * Circle.pi
#
#     def perimeter(self):
#         return 2 * Circle.pi * self.radius
#
#     def display_circle(self):
#         print(f"The radius of the circle is {self.radius} -> The circle area is {Circle.area(self)}, perimeter is {Circle.perimeter(self)}")
#
#     def validation(self, radius):  # noqa
#         return radius if (isinstance(radius, int) or isinstance(radius, float)) else None
#
#     def radius_from_perimeter(self, perimeter):  # noqa
#         return perimeter / (2 * Circle.pi)
#
#     @staticmethod
#     def square_meters_to_square_feets(square_meters):  # noqa
#         return square_meters * 10.764
#
#
# circle = Circle(3)
# circle.display_circle()
#
# print(circle.radius_from_perimeter(18.846))
# print(Circle.square_meters_to_square_feets(20))


# Question number 3
# class Animal:
#     animals_list = list()
#
#     def __init__(self, name, age, species):
#         self.name = name
#
#         assert self.validate_age(age), "Error : Age shouldn't be a text or negative"
#         self.age = age
#
#         self.species = species
#         Animal.animals_list.append(species)
#
#     @staticmethod
#     def validate_age(age):
#         return isinstance(age, int) and age > 0
#
#     def specie_changer(self, new_spec):
#         self.species = new_spec
#
#     @staticmethod
#     def get_species_count():
#         return len(set(Animal.animals_list))
#
#     def __repr__(self):
#         return f"Name:{self.name},Age:{self.age}, Species:{self.species} "
#
#
# my_dog = Animal("dOGGY", 2, "Germ")
# my_other_cat = Animal("catty", 4, "Persian")
# my_cat = Animal("Leo", 4, "Persian")
#
# print(Animal.get_species_count())
