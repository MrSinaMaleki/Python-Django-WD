# import os
#
#
# class Player:
#     XOlist = ["x", "o"]
#
#     def __init__(self, name, sign):
#         assert not isinstance(name, int) and len(name) < 10, "You name is either too long or an int"
#         self.name = name.title()
#
#         not_validated_sign = sign.lower()
#         assert not_validated_sign in self.__class__.XOlist, f"It only be should be {self.__class__.XOlist}"
#         self.__class__.XOlist.remove(not_validated_sign)
#         self.sign = not_validated_sign
#
#     @staticmethod
#     def instance_maker():
#         input_name = input("Please enter your name. ")
#         input_sign = input(f"Please enter your sign{Player.XOlist}.")
#         return input_name, input_sign
#
#
# class Settings:
#     def __init__(self, rounds):
#         assert isinstance(rounds, int) and rounds > 0, "Negative number of rounds!"
#         self.rounds = rounds
#
#
# class XOGame:
#     winners_list = []
#     white_list = [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]
#     game_map = {k: k + 1 for k in range(10)}
#
#     def __init__(self, player_one, player_two, game_settings):
#         self.player_one = player_one
#         self.player_two = player_two
#         self.game_settings = game_settings
#
#     @staticmethod
#     def clear():
#         os.system('cls' if os.name.lower() == 'nt' else 'clear')
#
#     def show(self):
#         print(("""
#         ----------------------
#         |  {}  |  {}  |  {}  |
#         ----------------------
#         |  {}  |  {}  |  {}  |
#         ----------------------
#         |  {}  |  {}  |  {}  |
#         ----------------------
#         """.format(*[self.game_map[i] for i in self.game_map])))
#
#     def mark(self, cell_number, sign):
#         assert isinstance(cell_number, int) and 1 <= cell_number <= 9, "Invalid Cell Number"
#         assert not self.game_map[cell_number - 1] in ("o", "x"), "Cell is filled"
#
#         self.game_map[cell_number - 1] = sign.lower()
#
#     def wining(self):
#         for li in self.__class__.white_list:
#             if self.game_map[li[0] - 1] == self.game_map[li[1] - 1] == self.game_map[li[2] - 1]:
#                 return True
#
#     def reset(self):
#         self.game_map = {k: k + 1 for k in range(10)}
#
#     def start(self):
#         i = 9
#         players_turn = player_one_object
#         while i > 0:
#             i -= 1
#             players_turn = player_two_object if players_turn == player_one_object else player_one_object
#
#             my_game.show()
#             cell = int(input(f"{players_turn.name}({players_turn.sign}):"))
#             my_game.mark(cell_number=cell, sign=players_turn.sign)
#             if self.wining():
#                 self.winners_list.append(players_turn.name)
#                 self.clear()
#                 print(f"{players_turn.name} has won this round!")
#                 print("next round!")
#                 self.reset()
#                 break
#
#         self.game_settings.rounds -= 1
#
#         if game_settings_object.rounds == 0:
#             self.clear()
#             print(
#                 f"{self.player_one.name}:{self.winners_list.count(player_one_object.name)} ,{self.player_two.name}:{self.winners_list.count(player_two_object.name)} ")
#
#
# input_name_index, input_sign_index = Player.instance_maker()
# player_one_object = Player(name=input_name_index, sign=input_sign_index)
#
# input_name_index, input_sign_index = Player.instance_maker()
# player_two_object = Player(name=input_name_index, sign=input_sign_index)
#
# game_settings_object = Settings(
#     rounds=int(input("Please enter the number of rounds you want to play the game. ")))
#
# my_game = XOGame(player_one=player_one_object, player_two=player_two_object, game_settings=game_settings_object)
#
# while game_settings_object.rounds > 0:
#     my_game.start()
