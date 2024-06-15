# def average_of_numbers(n):
#     nums_list = []
#     average_total = ()
#
#     for i in range(len(n[0])):
#         nums_temp = []
#         for j in range(len(n)):
#             nums_temp.append(n[j][i])
#         nums_list.append(nums_temp)
#
#     # print(nums_list)
#
#     for item in nums_list:
#         average = (lambda x: sum(x) / len(x))(item)
#         average_total += (average,)
#     return average_total
#
#
# nums1 = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
# nums2 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
#
# print("The average of num1:", average_of_numbers(nums1))
# print("The average of num1:", average_of_numbers(nums2))
