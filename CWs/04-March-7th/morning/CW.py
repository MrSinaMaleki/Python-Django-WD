# ///////////////////////////////////////////////////////Q 01/////////////////////////////////////////////////////
# import os
# empty_dict = {}
#
#
# def add(key, value):
#     if key in empty_dict.keys():
#         print("You can't add the same key")
#     else:
#         empty_dict.update({key: value})
#
#
# def remove(key, value):
#     if key in empty_dict:
#
#         if empty_dict[key] == value:
#             empty_dict.pop(key)
#         else:
#             print("Wrong value!")
#
#     else:
#         print("wrong key!")
#
#
# flag = True
# while flag:
#
#     print("add/remove/display/exit")
#     user_input = input("Please enter the operation you want.")
#
#     if user_input.lower() == 'add':
#         add(key=input("Please enter the key. "), value=input("Please enter the value. "))
#
#     elif user_input.lower() == 'remove':
#         remove(key=input("Please enter the key. "), value=input("Please enter the value. "))
#
#     elif user_input.lower() == 'display':
#         print(empty_dict)
#
#     elif user_input.lower() == 'exit':
#         print("exiting")
#         flag = False
#     else:
#         print("Wrong value try again!")


# ///////////////////////////////////////////////////////Q 012-April-11th/////////////////////////////////////////////////////
# def func1(*args):
#     print("Printing values: ")
#     for number in args:
#         print(number)
#
#
# func1(20, 40, 60, 45, 100)


# ///////////////////////////////////////////////////////Q 03/////////////////////////////////////////////////////

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# n = int(input("Please enter n. "))
# for i in range(n):
#     print(fibonacci(i))


# ///////////////////////////////////////////////////////Q 04/////////////////////////////////////////////////////

# def factorial(n):
#     if n == 0:
#         return 1
#
#     return n * factorial(n - 1)
#
#
# n = int(input("Please enter n. "))
# print("The factorial of", n, "is:", factorial(n))

# ///////////////////////////////////////////////Q 05//////////(Not completed)/////////////////////////////////
# Create a tuple of tuples 'nums' containing integer values
# nums = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
#
# # Create another tuple of tuples 'nums' containing integer values including negative numbers
# nums1 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
#
# real_list = list()
# for i in range(len(nums)):
#     temp = nums[i]
#     for j in range(len(temp)):
#         real_list.append(temp[j])
#
# print(real_list)
# new_list = list()
#
# a = len(real_list)/3
# for i in range(a):
#     v = i
#
#     while v < len(real_list):
#         new_list.append(real_list[v])
#         v += 3
#     print(new_list)
#
#     avg = lambda item: sum(item) / len(item)
#     print(avg(new_list))
#
#
# for item in nums:
#     print(tuple_a)

