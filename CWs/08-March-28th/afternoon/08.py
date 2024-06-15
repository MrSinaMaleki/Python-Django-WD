# 08- March-28th Afternoon

# Question 10

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# sample_dict['location'] = sample_dict['city']
# del sample_dict['city']
# print(sample_dict)


# Question 11
# import datetime
#
# # 1
# text = datetime.datetime.now()
#
# output_list = {
#     'year': (lambda item: item.year)(text),
#     'month': (lambda item: item.month)(text),
#     'day': (lambda item: item.day)(text),
#     'time': (lambda item: f"{item.hour}: {item.minute}: {item.second}")(text)
# }
# print(output_list)
#
# # 2
# datetime_str = input("Enter a datetime string (YYYY-MM-DD HH:MM:SS): ")
# text = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
#
# output_list_b = {
#     'year': (lambda item: item.year)(text),
#     'month': (lambda item: item.month)(text),
#     'day': (lambda item: item.day)(text),
#     'time': (lambda item: f"{item.hour}: {item.minute}: {item.second}")(text)
# }
# print(output_list_b)


# import datetime
# import re
#
# print(datetime.datetime.now())
#
# now = re.split("-|\\.| ", str(datetime.datetime.now()))
# now.pop(4)
# print(now)
#
# res = list()
# x = list(map(lambda item: res.append(item), now))
# print(x)

# Question 12
# tem_cel = [25, 30, 15, 10, 20]
# print(f"original temperatures: {tem_cel}")
# print(f"Converted temperatures: {list(map(lambda x: (x * (9 / 5)) + 32, tem_cel))}")


# Question 13-1
# Dict = {'M1': [67, 79, 90, 73, 36], 'M2': [89, 67, 84], 'M3': [82, 57]}

# summ = 0
# items = [len(i) for i in Dict.values()]
# print(sum(items))

# Q13 Way2
# summ = 0
# items = [summ := summ + len(i) for i in Dict.values()]
# print(summ)

# Question 14-2

# Dict = {"Sam": {"M1": 89, "M2": 56, "M3": 89},
#         "Suresh": {"M1": 49, "M2": 96, "M3": 89}}
#
# for key, value in Dict.items():
#     print(key)
#     for x, y in value:
#         print(f"{x}: {y}")


# Question 15-3

# def hotel_cost(nights):
#     return nights * 140
#
#
# def plane_ride_cost(city):
#     # Input
#     cost = {"Charlotte": 183,
#             "Tampa": 220,
#             "Pittsburgh": 222,
#             "Los Angeles": 475,
#             }
#
#     if city in cost.keys():
#         return cost[city]
#     else:
#         return "Wrong City!"
#
#
# def rental_car_cost(days):
#     cost_of_car = days * 40
#     if days >= 7:
#         return cost_of_car - 50
#     elif days >= 3:
#         return cost_of_car - 20
#     else:
#         return cost_of_car
#
#
# def trip_cost(city_y, days_s ,  spending_money):
#     return hotel_cost(nights=days_s) + plane_ride_cost(city=city_y)
#     + rental_car_cost(days=days_s) + int(spending_money)
#
#
# city_y = input("Which city are you going to visit?")
# days_s = int(input("How many days?"))
# spending = int(input("How much money will you spend during the trip?"))
# print(trip_cost(city_y, days_s, spending))


# Question 16-4
# def cube(number):
#     return number ** 3
#
#
# def by_three(number):
#     if number % 3 == 0:
#         return cube(number)
#     else:
#         return False
#
#
# user_input = int(input("Please enter the number. "))
# print(by_three(user_input))


# Question 17-5

# Dictionary = {"m1": 78, "m2": 89, "m3": 64, "m4": 35, "m5": 71}
# list_1 = list(Dictionary.items())
#
#
# def sorter(list_one):
#     new_list = sorted(list_one, key=lambda x: x[1])
#     print(f"Ascending Order: {new_list}")
#     new_list = sorted(list_one, key=lambda x: x[1], reverse=True)
#     print(f"Descending Order: {new_list}")
#
#
# sorter(list_one=list_1)
