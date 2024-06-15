# 09-March-29th

# Question number 1

# dict1 = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "d": 4,
# }
# dict_swap = {value: key for key, value in dict1.items()}
# print(dict_swap)

# Question number 2

# Before_Dropping = {
#     'Name': 'Pooja',
#     'Age': 23,
#     'Gender': '',
#     'Mark': 488,
#     'City': None
# }
#
# After_Dropping = {}
#
# for key, value in Before_Dropping.items():
#     if not value:
#         pass
#     else:
#         After_Dropping.update({key: value})
# print(After_Dropping)


# Question number 3
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Y = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Z = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# dict_1 = {}
#
#
# assigned_variables = {name: value for name, value in locals().items()
#                       if isinstance(value, list)}
#
# print(assigned_variables)

# Question number 4
# A = {'Tamil': 92, 'English': 56, 'Maths': 88, 'Sceince': 97, 'Social': 89, "Sina": 20}
# B = {'Tamil': 78, 'English': 68, 'Maths': 88, 'Sceince': 97, 'Social': 56, "Reza": 20}
#
# for key, value in A.items():
#     for k, v in B.items():
#         if value == v and key == k:
#             print(f"{k}: {v} is present in Both A and B")


# Question number 5
# a = {23, 8, 56, 45, 78}
# b = {42, 26, 55, 87}
# Z = {46, 87}
#
# print(f"Compare A and B: {a.isdisjoint(b)}")
# print(f"Compare B and Z: {b.isdisjoint(Z)}")
# print(f"Compare A and Z: {a.isdisjoint(Z)}")

# Question number 6
# my_set = {17, 56, 23, 8, 10, 45}
# # my_list = [item for item in my_set]
# print(f"Maximum : {max(my_set)}")
# print(f"Minimum : {min(my_set)}")

# Question number 7
# name = "TutorJoes"
#
# my_set = {letter for letter in name}
# print(my_set)
#
# my_set1 = set(name)
# print(my_set1)

# Question number 8
# String = "Tutor Joes"
# my_list = [letter for letter in String if letter in {'a', 'i', 'o', 'u', 'e', 'A', 'I', 'O', 'U', 'E'}]
# print(f"Number of Vowels: {len(my_list)}")

# Question number 9
#
# from datetime import datetime
#
# now = datetime.now()
# keys = ['hour', "minute", "second"]
#
# output_dict = {key: getattr(now, key) for key in keys}
# print(output_dict)
#
# output_dict['second'] += 5
# if output_dict['second'] > 60:
#     output_dict['second'] -= 60
#     output_dict['minute']
# print(output_dict)

# from datetime import datetime, timedelta
#
# # Using current time
# ini_time_for_now = datetime.now()
#
# # printing initial_date
# print('initial_date:', str(ini_time_for_now))
#
# # for five seconds
# future_date_after_five_seconds = ini_time_for_now + timedelta(seconds=5)
#
# print('new_date    :', str(future_date_after_five_seconds))


# Question number 10
# from datetime import datetime
# datetime_str = input("Enter a datetime string (YYYY-MM-DD HH:MM:SS): ")
# text = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
# print(type(text))

# Question number 11

# words = ['apple', 'banana', 'cherry', "Apple"]
# dict_a = {word: sum(list(map(lambda x: word.count(x),
#           ['a', 'i', 'o', 'u', 'e', 'A', 'I', 'O', 'U', 'E']))) for word in
#           words}
# print(dict_a)

# Question number 12
# words = ['apple', 'banana', 'cherry']
# dict_a = {word: word * 3 for word in words}
# print(dict_a)

# Question number 13
# string = "Hello, how are you?"
# my_list = [letter for letter in string if letter not in {'a', 'i', 'o', 'u', 'e', 'A', 'I', 'O', 'U', 'E'} and letter.isalpha()]
# print(f"Number of Vowels: {my_list}")


# Question number 14
# list_1 = [10, -5, 20, -15, 30]
# positive = []
# negative = []
#
# # for i in list_1:
# #     if i >= 0:
# #         positive.append(i)
# #     else:
# #         negative.append(i)
# # print(f"positive : {tuple(positive)}\nnegative : {tuple(negative)}")
#
# temp = list(map(lambda item: positive.append(item) if item >= 0 else negative.append(item), list_1))
# print(positive)
# print(negative)


# Question number 15
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = []
#
# for i in list1:
#     for j in list2:
#         list3.append((i, j, i+j))
# print(tuple(list3))
#
# # list4 = [[list3.append((i, j, i+j)) for j in list2] for i in list1]
# # print(tuple(list4))

# Question number 16
# def salary(sal):
#     if sal < 1500:
#         hra = sal * 0.1
#         da = sal * 0.9
#     else:
#         hra = 500
#         da = sal * 0.98
#     return hra, da
#
#
# basic_salary = float(input("Enter your salary: "))
#
# hra, da = salary(basic_salary)
# gross_salary = basic_salary + hra + da
# print(f"Your gross salary is: {gross_salary} Rs.")


# Question number 17
# text = ("""Python is an interpreted, object-oriented, high-level programming language
# that can be used for a wide variety of applications. Python is a powerful
# general-purpose programming language.""").split("\n")
#
# temp_str = str()
# for item in text:
#     temp_str += f"* {item}\n"
#
# print(temp_str)
