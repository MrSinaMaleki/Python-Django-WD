# Q6
# my_input = list(str(input("Enter Your Text: ")))
#
# file = open("note.txt", "r")
# text = file.read()
# my_list = list(text)
# print(my_list)
#
# counter = 0
#
# for i in range(len(text)):
#     if my_list[i:len(my_input)+i] == my_input:
#         counter += 1
#
# print(counter)

#
# f = open("note.txt", "r")
# x = input("Enter a string: ")
# text = f.read()
# counter = text.count(x)
# # print(text)
# print(counter)

# Q7
# file = open("output.txt", "r")
# text = file.read()
#
# new_text = text.title()
# file.close()
#
# file = open("output.txt", "w")
# file.write(new_text)
# file.close()

# file = open("note.txt", "r")
# text = file.read()
# my_list = list(text)
# my_list.append("")
#
# for i in range(len(my_list)):
#     if my_list[i] == " ":
#         my_list[i+1] = my_list[i+1].upper()
#
# my_list.pop()
# final = "".join(my_list)
# file.close()
#
# file = open("note.txt", "w")
# file.write(final)
#
# print(final)
# file.close()

# Q8
# a = str(input("Please enter s.th. "))
#
# file = open("output.txt", "a")
# file.write(a)
# file.close()

# Q9
# string = (input("Please enter a text. "))
# letter = str(input("Enter the letter you want to look for. "))
#
# # for index in string:
# #     count = string.count(index)
# #     if count > 1:
# #         print(f"The character '{index}' is present in the string {count} time/times.")
#
#
# count = string.count(letter)
# print(count)


# Q10
import math
a = float(input("Please enter num a. "))
b = float(input("Please enter num b. "))
c = float(input("Please enter num c. "))

if abs(a-b) < c < abs(a+b) and abs(a-c) < b < abs(a+c) and abs(c-b) < a < abs(c+b):
    s = (a + b + c) / 2
    # A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    A = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(A)
else:
    print("Dadash in Mosalas nista!!!")


# Q11

#
# try:
#     a = float(input("Please enter a. "))
#     b = (input("Please enter operator. "))
#     c = float(input("Please enter b. "))
#
#     if b == "*":
#         print(a * c)
#
#     elif b == "-":
#         print(a - c)
#
#     elif b == "/":
#         print(a / c)
#
#     elif b == "%":
#         print(a % c)
#
#     elif b == "+":
#         print(a + c)
#
#     else:
#         assert b in ["+", "-", "*", "%", "/"], "This is a typeError"
#
# except (ZeroDivisionError, ValueError, AssertionError) as e:
#     print(e)
