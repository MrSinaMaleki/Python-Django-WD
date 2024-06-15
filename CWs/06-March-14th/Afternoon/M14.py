# # Q log
# master_dict = {}
#
# file = open(file='note.txt', mode="r")
# line_list = list()
#
# content = file.read().split("\n")
# i = 0
#
# method_list = list()
# status_list = list()
# total_request = len(content)
# size_list = list()
#
# for item in content:
#     line_list.append(item.split(" "))
#     method_list.append(line_list[i][5])
#     status_list.append(line_list[i][-2])
#     size_list.append(line_list[i][-1])
#     i += 1
#
# real_size_list = list()
# for item in size_list:
#     try:
#         real_size_list.append(int(item))
#     except Exception:
#         continue
#
# # Filter
# frequency_method_dict = dict()
# for word in set(method_list):
#     counter = method_list.count(word)
#     frequency_method_dict.update({word: counter})
#
#
# # Filter
# frequency_status_dict = dict()
# for word in set(status_list):
#     counter = status_list.count(word)
#     frequency_status_dict.update({word: counter})
#
#
#
# print(f"Total Requests: {total_request}")
# print("HTTP Methods: ")
# for k, v in frequency_method_dict.items():
#     print(f"\t {k}: {v}")
#
# print("HTTP Status Codes:")
# for k, v in frequency_status_dict.items():
#     print(f"\t {k}: {v}")
#
# print(f"Total Response Body Size: {sum(real_size_list)} bytes")


# /// MrRasol

import pprint
# my_list = []
# with open("note.txt", "r") as f:
#     text_list = f.readlines()
#     http_statuses = []
#     http_method = []
#     response_size = 0
#     for i in text_list:
#         x = i.split(" ")
#         x1 = {
#             "Http method": x[5][1:],
#             "Http status": x[8],
#             "response_size": x[9][:-2]
#         }
#         http_statuses.append(x[5][1:])
#         http_method.append(x[8])
#         if x[9][:-2].isdigit():
#             response_size += int(x[9])
# status_dict = dict()
# method_dict = dict()
# for i in set(http_statuses):
#     status_dict[i] = http_statuses.count(i)
# for i in set(http_method):
#     method_dict[i] = http_method.count(i)
#
#
#
# print(f"total requests: {response_size}")
# print(f"HTTP methods: {method_dict}")
# print(f"HTTP statuses: {status_dict}")