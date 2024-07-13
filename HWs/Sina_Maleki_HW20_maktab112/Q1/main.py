import math
import os
import random

db = {"games": ["dota2", "csgo", "need for speed"], "artists": ["eminem", "DR"]}


class Game:
    def __init__(self):
        pass

    @classmethod
    def start_game(cls):
        res = cls.sub_selection()

        word_len = len(res)
        letters = [letter for letter in res]

        encoded = ""
        for letter in [" " if letter == " " else "*" for letter in letters]:
            encoded += letter

        guss_counter = math.floor(word_len / 2)
        flag = True

        while guss_counter > 0 and flag:
            print(f"\t You got {guss_counter} guess. \n \t word: {encoded}")

            guess_letter = input()

            if len(guess_letter) > 1:
                flag = cls.win_check(guess_letter, res)
                if not flag:
                    print("You won!")
                else:
                    print("You lost!")

            else:
                if guess_letter in letters:
                    patchable_index = []
                    index_val = 0
                    for letter in letters:
                        if letter.lower() == guess_letter:
                            patchable_index.append(index_val)
                        index_val += 1

                    for index in patchable_index:
                        # encoded[index] = letter
                        encoded = encoded[: index] + guess_letter + encoded[index + 1:]

                guss_counter -= 1
        if flag:
            print(f"You've got no guess left and you should guess the word. \n \t word: {encoded}")
            user_word_inp = input()
            cls.win_check(user_word_inp, res)

    @staticmethod
    def win_check(word, res):
        if word.lower() == res:
            return False
        else:
            return True

    @classmethod
    def sub_selection(cls):
        keys = [key for key in db.keys()]
        print("Please Select on of the Subjects below.")

        for i, value in enumerate(keys):
            print(i, ". ", value, sep="")

        selected_sub = input()
        # selected_sub = "games"
        if selected_sub in keys:
            return random.choice(db.get(selected_sub))
        else:
            Menu.clear()
            return False


class Menu:
    @classmethod
    def start(cls):
        cls.clear()
        Game.start_game()

    @staticmethod
    def clear():
        os.system("cls")


print(
    "Welcome, Please select one of the options bellow.",
    "1.Start the game", "2.Add subjects", "3.Add words to the subjects", "4.Exit", sep="\n \t", end="\n")

user_inp = str(input())
# user_inp = "start"
menu = Menu()
getattr(menu, user_inp)()
