# def all_possible_combinations(x):
#     def backtrack(current, remaining):
#         if not remaining:
#             result.append(current)
#             return
#         for i in range(len(remaining)):
#             backtrack(current + remaining[i], remaining[:i] + remaining[i+1:])
#     result = []
#     backtrack("", x)
#     return result
#
#
# input_string = input("Enter a string: ")
# print(all_possible_combinations(input_string))
