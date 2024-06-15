# Q1 : *v1*

# print("number is positive" if (number := (int(input("Enter a number: ")))) > 0
#       else "number is negative" if number < 0 else "number is zero")

# *v2* :

# num = float(input("Enter the number: "))
# if num == 0:
#     print("The number is Zero")
# elif num > 0:
#     print("The number is Positive")
# else:
#     print("The number is Negative")

# -----------------------------------------------------------------------
# Q2 : *v1*

# a, b = input('Enter values separated by escape : ').split(' ')
# print(f"a : {b}\nb : {a}")

# v2 :

# a = input("Enter the number a: ")
# b = input("Enter the number b: ")
# temp = a
# a = b
# b = temp
# print("a=", a, "b=", b)

# -----------------------------------------------------------------------
# *extra exercise* :

# b = len(a := input('Enter values separated by escape : ').split(' ')) - 1
# print([a[c] for c in range(b, -1, -1)])

# -----------------------------------------------------------------------
# Q3 : v1

# num = int(input("Enter a number: "))
# while num < 2:
#     num = int(input('Enter a number: '))
# r = [f"{num} is prime" for c in [f"{num} is not prime" if num % i == 0
#                                  else f"{num} is prime" for i in range(2, num)]
#      if f"{num} is prime" == c]
# if num == 2:
#     print("2 is prime")
# elif not r:
#     print(f"{num} is not prime")
# else:
#     print(f"{num} is prime")

# *v2*
# num = int(input("Enter a number: "))
#
# for i in range(2, num // 2):
#     if num % i == 0:
#         print(f"this number is not prime")
#         break
# else:
#     print(f"this number is prime")

# -----------------------------------------------------------------------
# *Q4* :

# x, y = int(input("Enter a number: ")), int(input("Enter a number: "))
# if x > y:
#     x, y = y, x
# for i in range(x, y+1):
#     for j in range(2, i):
#         if i % j == 0:
#             print(f"{i} is not prime")
#             break
#     else:
#         print(f"{i} is prime")

# -------------------------------------------------------------------
# *Q5* :

# in1 = input("Enter a text if you need exit print it : ")
# while in1.lower() != 'exit':
#     in1 = input('Enter a text if you need exit print it : ')

# -------------------------------------------------------------------
# Q6 : v1

# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i, v in list(enumerate(test_list)):
#     print(f"index : {i}\t value : {v}")

# *v2*
# for i, v in list(enumerate(
#         input('enter text separator by escape : ').split(' '))):
#     print(f"index : {i}\t value : {v}")

# ---------------------------------------------------------------------
# Q7 : *v1*

# l_t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l_l_t = len(l_t)
# s_l = l_l_t // 2
# print(l_t[:s_l])
# print(l_t[s_l:])

# v2 :
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list1 = my_list[:5]
# list2 = my_list[5:]
# print("List1: ", list1, "\nList2: ", list2)

# -------------------------------------------------------------------
# Q8 : *v1*

# l_t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(l_t[-1:-5:-1])

# v2 :

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# first_list = my_list[-4:]
# second_list = my_list[-4:len(my_list)]
# print("first List is: ", first_list)
# print("Second List is: ", second_list)

# --------------------------------------------------------------------
# Q9 : *v1*

# l_t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(8, 1, -2):
#     print(l_t.pop(i))

# v2 :

# l_t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(l_t[-2:-9:-2])

# --------------------------------------------------------------------
# Q10 : *v1*

# l_t = input("Enter text separated by scape : ").split(" ")
# print(True if not l_t else False)

# v2 :

# my_list = []
# value = input('Enter the value: ')
# while value != "":
#     my_list.append(value)
#     value = input('Enter the value: ')
# if not my_list:
#     print("True")
# else:
#     print("False")

# --------------------------------------------------------------------
# Q11 : *v1*

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l1.extend(l2)
# print(f"new list : {l1}\n len new list : {len(l1)}")

# v2 :

# list1 = [1, 2, 3, 4, 5]
# list2 = ["apple", "banana", "cherry"]
# sum_lists = list1 + list2
# print(sum_lists)

# --------------------------------------------------------------------
# *Q12* :

# l_t = input("Enter text separated by scape : ").split(" ")
# l_t.sort(key=int, reverse=True)
# for i in l_t:
#     for j in range(2, int(i)):
#         if int(i) % j == 0:
#             print(f"{i} is not prime")
#             break
#     else:
#         print(f"{i} is prime")

# --------------------------------------------------------------------
# Q13 : v1

# a, b, c = map(int, input("enter three number separator by escape : ").split(" "))
# if c > a and c > b:
#     if a > b:
#         print(f"{c} is greater than {a} and {a} is greater than {b}")
#     else:
#         print(f"{c} is greater than {b} and {b} is greater than {a}")
# elif b > c and b > a:
#     if a > c:
#         print(f"{b} is greater than {a} and {a} is greater than {c}")
#     else:
#         print(f"{b} is greater than {c} and {c} is greater than {a}")
# else:
#     if b > c:
#         print(f"{a} is greater than {b} and {b} is greater than {c}")
#     else:
#         print(f"{a} is greater than {c} and {c} is greater than {b}")

# *v2* :

# d = list(map(int, input("enter three number separator by escape : ").split(" ")))
# d.sort(reverse=True)
# print(d)

# -----------------------------------------------------------------------
# Q14 : v1

# my_num = int(input("Enter a number : "))
# counter = 0
# for i in range(1, 11):
#     if my_num // (10 ** i):
#         my_num -= (my_num % (10 * i))
#         counter = i + 1
#     elif my_num < 10:
#         counter = 1
#         break
#     else:
#         break
# print(counter)

# *v2* :

# my_num = input("Enter a number : ")
# print(len(my_num))

# v3 :

# num = input("Enter a number: ")
#
# print("Data type method")
# if "." in num:
#     print("The count of digits in the entered number:", len(num) - 1)
# else:
#     print("The count of digits in the entered number:", len(num))
#
# print("\nMathematical method")
# if "." in num:
#     num = int(num.replace(".", ""))
# else:
#     num = int(num)
# i = 0
# while num % 10 != 0:
#     i += 1
#     num = num // 10
# print("The count of digits in the entered number :", i)

# --------------------------------------------------------
# Q15 : *v1*

# str1, str2 = input("please enter two string by space : ").split(" ")
# print(str1 == str2[::-1])

# v2 :

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
#
# if len(str1) != len(str2):
#     print('"%s" and "%s" are not anagrams' % (str1, str2))
# else:
#     for i in range(len(str1)):
#         if str1[i].lower() not in str2.lower():
#             print('"%s" and "%s" are not anagrams' % (str1, str2))
#             break
#     else:
#         print('"%s" and "%s" are anagrams' % (str1, str2))

# ----------------------------------------------------------
# Q16 : v1

# print(set(input("Enter a string separated by space: ").split(" ")))

# *v2* :

# my_list = [1, 2, 3, 2, 4, 5, 4, 2, 6, 2]
# for i, v in enumerate(my_list):
#     if my_list.count(v) > 1:
#         my_list.pop(i)
# print(my_list)

# -------------------------------------------------------------
# *Q17* :

# print(set(map(str, input("Enter a string : "))))

# ------------------------------------------------------------
# *Q18* :

# print(input("Enter a string : ").lower().count('x'))

# --------------------------------------------------------------
# *Q19* :

# print(input("Enter a string : ").lower().count('abc'))

# -------------------------------------------------------------
# Q20 : *v1*

# print([i for i in map(int, input("Enter a string separated by space: ").split(" "))
#        if (i % 2 == 0)])

# v2 :

# input_list = input("Enter a list of numbers separated by 'space': ")
# my_list = input_list.split(" ")
# even_list = []
# for num in my_list:
#     if int(num) % 2 == 0:
#         even_list.append(num)
# print("the list of even numbers: ", even_list)
