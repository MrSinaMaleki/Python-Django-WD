
# Q1
# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'b': 200, 'd': 400, 'a': 300}
#
# d3 = {}
# print(d1.keys())
# for i in d1.keys():
#     for j in d2.keys():
#         print(i, j)
#         if i == j:
#             temp = d1.get(i) + d2.get(j)
#             d3[i] = temp
#             # print(temp)
#         else:
#             if i not in d2.keys():
#                 d3[i] = d1.get(i)
#             elif j not in d1.keys():
#                 d3[j] = d2.get(j)
#
# print(d3)
# ///////////////////////////////////////////////////////Q 012-April-11th/////////////////////////////////////////////////////
# sample_data = [{"V": "S001"},
#                {"V": "S002"},
#                {"VI": "S001"},
#                {"VI": "S005"},
#                {"VII": "S005"},
#                {"V": "S009"},
#                {"VIII": "S007"}]
#
# unique_values = []
# for i in sample_data:
#     for k, v in i.items():
#         unique_values.append(v)
# print(set(unique_values))