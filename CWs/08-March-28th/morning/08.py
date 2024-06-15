# 08- March-28th Morning

# Question  number 6
# favorite_movies = [
#     ("Pulp fiction", 1994),
#     ("Inception", 2010),
#     ("x", 2020),
#     ("The Shawshank redemption", 1994)
# ]
#
# new_list = sorted(favorite_movies, key=lambda x: x[1], reverse=True)

# counter = 0
# for item in new_list:
#     counter += 1
#     print(f"{counter}. {item}")

# for item in list(enumerate(new_list)):
#     print(f"{int(item[0]) + 1}. {item[1]}")


# Question  number 7
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
#
# if len(sample_list) % 3 == 0:
#     x = int(len(sample_list) / 3)
#     sublist = [sample_list[i:i + x] for i in range(0, len(sample_list), x)]
# print(sublist)

# count = 1
# for item in sublist:
#     print(f"Chunk{count}: {item}")
#     count += 1
#     # print(f"After reversing it {list(reversed(item))}\n")
#     print(f"After reversing it {item[::-1]}\n")

#     for item in enumerate(sublist, 1):
#         print(f"Chunk{int(item[0])}: {item[1]}")
#         print(f"After reversing it {item[1][::-1]}\n")
# else:
#     print("The length of list is not a multiple of 3")


# Question  number 8 - Way 1(Wrong)
#
# user_start_input = int(input("start: "))
# user_finish_input = int(input("finish: "))
#
#
# def prime_checker(number):
#     for n in range(2, number + 1):
#         for i in range(2, n - 1):
#             if n % i == 0:
#                 return False
#         else:
#             return True


# *** edited by Payam for "Question 8 with 'Filter' solution" ***
# def prime_checker(number):
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     else:
#         return True
#
#
# start_num = int(input("start: "))
# finish_num = int(input("finish: "))
#
# print(list(filter(prime_checker, range(start_num, finish_num))))


# print(prime_checker(20))
# prime_checker(number=user_finish_input)
# print(list(filter(prime_checker, range(user_start_input, user_finish_input))))

# Question  number 8 - Way 2
# number1, number2 = map(int, input("Enter number1 and number2 seperated by a space: ").split())
#
# list1 = [i for i in range(number1 + 1, number2) if all([False if i % v == 0 else True for v in range(2, i)])]
# print(list1)


# Question  number 9

# import datetime

# name = input("please enter a name : ")
# year = int(input("please enter a year : "))

# def calc_age(year1):
#     now = datetime.datetime.now().year
#     return now - year1

# age = calc_age(year)
# print(f"Hello, {name}! You are {age} years old.")
