
# ///////////////////////////////////////////////////////Q 06/////////////////////////////////////////////////////
# import random
#
#
# def game():
#     user_count = 0
#     computer_count = 0
#     for i in range(3):
#         computer_choice = str(random.choice(("r", "p", "s")))
#         print((computer_choice))
#
#         user_choice = str(input("Please select one of the options r/p/s. "))
#
#         if user_choice in ('r', 'p', 's'):
#             if computer_choice == user_choice:
#                 continue
#             else:
#                 if (computer_choice == "r") and (user_choice == "p"):
#                     user_count += 1
#                 elif computer_choice == "p" and user_choice == "s":
#                     user_count += 1
#                 elif computer_choice == "s" and user_choice == "r":
#                     user_count += 1
#                 else:
#                     computer_count += 1
#         else:
#             print("wrong choice!")
#
#         print(f"user: {user_count} computer: {computer_count}")
#     count_user_win = 0
#     count_computer_win = 0
#
#     if user_count == computer_count:
#         print(f"user: {user_count} vs computer: {computer_count}", "Tie")
#         return 2
#
#     elif user_count > computer_count:
#         print(f"user: {user_count} vs computer: {computer_count}", "// User wins.")
#         return 0
#
#     elif user_count < computer_count:
#         print(f"user: {user_count} vs computer: {computer_count}", "// computer wins.")
#         return 1
#
#
# flag = True
# total_computer_wins = 0
# total_user_wins = 0
# total_tie = 0
#
# while flag:
#     a = game()
#     if a == 1:
#         total_computer_wins += 1
#     elif a == 0:
#         total_user_wins += 1
#     elif a == 2:
#         total_tie += 1
#
#     user_flag = input("Do you want to play again? ")
#     if user_flag.lower() != 'yes':
#         flag = False
#
# empty_dict = {}
# if total_user_wins > total_computer_wins:
#     print("User won!")
#     empty_dict.update({'user': total_user_wins})
#
# elif total_user_wins < total_computer_wins:
#     print("Computer won!")
#     empty_dict.update({'computer': total_computer_wins})
# else:
#     print("tie")
#     empty_dict.update({'tie': total_tie})
#
# print(empty_dict)


# ///////////////////////////////////////////////////////Q 07/////////////////////////////////////////////////////
# We are American!
# my_dict = {
#     '0': 'zero',
#     '1': 'one',
#     '2': 'two',
#     '3': 'three',
#     '4': 'four',
#     '5': 'five',
#     '6': 'six',
#     '7': 'seven',
#     '8': 'eight',
#     '9': 'nine',
#     '10': 'ten',
#     '11': 'eleven',
#     '12': 'twelve',
#     '13': 'thirteen',
#     '14': 'fourteen',
#     '15': 'fifteen',
#     '16': 'sixteen',
#     '17': 'seventeen',
#     '18': 'eighteen',
#     '19': 'nineteen',
#     '20': 'twenty',
#     '30': 'thirty',
#     '40': 'forty',
#     '50': 'fifty',
#     '60': 'sixty',
#     '70': 'seventy',
#     '80': 'eighty',
#     '90': 'ninety',
#     '100': 'hundred'
# }
#
# numbers_to_ten = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
# #
# # l = s.split()
# # print(l)
# # for num in l:
# #     if num.isnumeric():
# #         print(convert_to_numbers(num))
#
# user_input = str(int(input("Please enter a number. ")))
# my_num = list(str(user_input))
# counter = len(my_num)
# # for i in my_num:
# # print(my_num)
# # print(my_dict[my_num[0]])
# # print(my_dict[str(my_num[0])])
#
# if counter == 3:
#     if my_num[1] == '1':
#         double_digit = my_dict.get(str("".join(my_num[1:])))
#         print(f"{my_dict[my_num[0]]} hundred and {double_digit}")
#
#     elif my_num[1] == '0' and my_num[2] == '0':
#         print(f"{my_dict[my_num[0]]} hundred")
#
#     elif my_num[1] == '0' and my_num[2] != '0':
#         print(f"{my_dict[my_num[0]]} hundred {my_dict[my_num[2]]}")
#
#     elif my_num[2] == '0':
#         print(f"{my_dict[my_num[0]]} hundred and {my_dict[str(10 * int(my_num[1]))]}")
#     else:
#         print(f"{my_dict[my_num[0]]} hundred and {my_dict[str(10 * int(my_num[1]))]} {my_dict[my_num[2]]}")
#
# elif counter == 2:
#     if my_num[0] == '1':
#         print(my_dict.get(str(user_input)))
#
#     elif my_num[1] == '0':
#         print(f"{my_dict.get(str(user_input))}")
#
#     else:
#         print(f"{my_dict[str(10 * int(my_num[0]))]} {my_dict[my_num[1]]}")
# elif counter == 1:
#     print(f"{my_dict[my_num[0]]}")
