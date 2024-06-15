# # Question number 1
# # a, b, c = input("Please enter.").split()
# # a = float(a)
# # c = float(c)
# #
# # if b == "*":
# #     print(a * c)
# #
# # elif b == "-":
# #     print(a - c)
# #
# # elif b == "/":
# #     print(a / c)
# #
# # elif b == "%":
# #     print(a % c)
# #
# # elif b == "+":
# #     print(a + c)
#
# # Question number 2
# # def div_by_two(x):
# #     if x % 2 == 0:
# #         return "Yes"
# #     else:
# #         return "No"
# #
# #
# # print(div_by_two(1024))
#
#
# # Question number 3
# # import random
# #
# # a = random.randint(1, 1000)
# # flag = True
# # guess_number = 0
# # print(a)
# #
# # while flag:
# #     if guess_number < 10:
# #         x = int(input("Please enter your guess. "))
# #         guess_number += 1
# #         if x == a:
# #             print("You are the winner")
# #             flag = False
# #         elif x > a:
# #             print("The random number is lower")
# #         elif x < a:
# #             print("The random number is bigger")
# #     else:
# #         print("You are the loser")
# #         flag = False
#
# # Question number 4
# #
# # text = input("Please enter s.th ")
# #
# # if text == text[::-1]:
# #     print("It is a palindrome")
# # else:
# #     print("It is not a palindrome")
#
# # Question number 5
# # with open('D:\\note.txt', 'r') as file:
# #     count = 0
# #     for line in file:
# #         count += 1
# # print(f"The counting of number of lines is: {count}")
# #
# # file = open("D:\\note.txt", "r")
# # line_counter = 0
# # for line in file.readlines():
# #     line_counter += 1
# # file.close()
# # print(line_counter)
#
# # ----------------------------------------
# # Question number 6
# # num1 = float(input("Please enter num1. "))
# # num2 = int(input("Please enter num2. "))
# #
# #
# # def multi(num1, num2):
# #     res = 0
# #     negative_flag = False
# #
# #     if num1 < 0:
# #         num1 = abs(num1)
# #         negative_flag = not negative_flag
# #
# #     if num2 < 0:
# #         num2 = abs(num2)
# #         negative_flag = not negative_flag
# #
# #     for i in range(num2):
# #         res += num1
# #
# #     if negative_flag:
# #         res = -res
# #
# #     return res
# #
# #
# # print(multi(num1, num2))
# # ----------------------------------------
#
# # Question number 7 ---> Takmil Shavad!
# #
# # num1 = int(input("Please enter a. "))
# # num2 = int(input("Please enter b. "))
# #
# #
# # def t(x, y):
# #     negative_flag = False
# #
# #     if x < 0:
# #         x = abs(x)
# #         negative_flag = not negative_flag
# #
# #     if y < 0:
# #         y = abs(y)
# #         negative_flag = not negative_flag
# #
# #     counter = 0
# #     while x >= y:
# #         x -= y
# #         counter += 1
# #
# #     if negative_flag:
# #         counter = -counter
# #
# #     return counter, x
# #
# #
# # print(t(num1, num2))
#
# # ----------------------------------------
# # Question number 7
# # import itertools
# #
# # my_input = list(str(input("Enter A String: ")))
# # my_list = []
# #
# #
# # for i in range(len(my_input)):
# #     my_list.append(i)
# # last_list = my_list
# #
# #
# #
# # print([list(zip(x,last_list)) for x in itertools.permutations(my_list,len(last_list))])
# #
# # def my_fun():
# #     for i in my_input:
# #         for j in my_input:
# #             if i != j:
# #                 x = i + j
# #                 last_list.append(x)
# #
#
# # my_fun()
# # resault_str = ", ".join(last_list)
# #
# # print(resault_str)
#
# #
# # import random
# # l = "abc"
# # f = 1
# #
# # for i in range(1, len(l) + 1):
# #     f *= i
# #
# # for j in range(f):
# #
# #     x, y, z = map(int, random.choice(l))
# #     print(x)
#
# # Question number 8
#
# #
# # data_list = ['ab','abc','b', 'zzza', 'jaaaaa']
# # new_list = []
# #
# # while data_list:
# #     minimum = len(data_list[0])  # arbitrary number in list
# #     for x in data_list:
# #         if len(x) < minimum:
# #             minimum = len(x)
# #     new_list.append(minimum)
# #     data_list.remove(minimum)
# #
# # print(new_list)
#
# num1 = float(input("Please enter num1: "))
# num2 = float(input("Please enter num2: "))
#
#
# def my_division(x, y):
#     counter = 0
#     decimal_counter = 0
#     mark = ""
#     x_pos = abs(x)
#     y_pos = abs(y)
#     while x_pos >= y_pos:
#         x_pos -= y_pos
#         counter += 1
#     x_pos *= 10000
#     while x_pos >= y_pos:
#         x_pos -= y_pos
#         decimal_counter += 1
#
#     if (x < 0 < y) or (x > 0 > y):
#         mark = "-"
#     return f"{mark}{counter}.{decimal_counter}"
#
#
# print("Division = ", my_division(num1, num2))
#
# # Q9
#
