import random
import itertools
import time
from operator import itemgetter
import os

team_info = []


class Team:
    def __init__(self, name):
        assert name.isalpha(), "Please enter a valid name!"
        self.name = name

        self.game_counts = 0
        self.wins_count = 0
        self.loss_counts = 0
        self.draw_counts = 0
        self.points = 0  # each win gets 3 points and each draw gets 1 point

        team_info.append(
            {'name': self.name, "game_counts": self.game_counts, "wins": self.wins_count, "loss": self.loss_counts,
             "draws": self.draw_counts, "points": self.points + self.wins_count * 3 + self.draw_counts * 1})

    @classmethod
    def from_string(cls, user_input_name):
        return cls(name=user_input_name)

    @staticmethod
    def clear():
        os.system('cls' if os.name.lower() == 'nt' else 'clear')

    @staticmethod
    def league_preview():
        # https://stackoverflow.com/questions/72899/how-to-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary-in-python
        new_list = sorted(team_info, key=itemgetter('points'), reverse=True)
        i = 0
        for team in new_list:
            i += 1
            print(
                f"({i})-{team['name']} points:{team['points']}| wins: {team['wins']}, losses: {team['loss']}, draws: {team['draws']}, all games count: {team['game_counts']}")

    @staticmethod
    def winner(team):
        print(f"The winner is:{team["name"]}")
        team["wins"] += 1
        team["points"] = (team["wins"] * 3)
        team['game_counts'] += 1

    @staticmethod
    def lose(team):
        team["loss"] += 1
        team["game_counts"] += 1

    @staticmethod
    def draw(team):
        team["draws"] += 1
        team["points"] = (team["draws"] * 1)
        team['game_counts'] += 1

    @classmethod
    def play(cls, info_list):
        combos = list(itertools.combinations(info_list, 2))
        for two_player in combos:
            print(f"It's {two_player[0]['name']} vs {two_player[1]['name']}")
            rand_num = random.randint(0, 2, )

            if rand_num == 2:
                print("It was a draw.")
                cls.draw(team=two_player[0])
                cls.draw(team=two_player[1])

            elif rand_num == 1:
                cls.winner(team=two_player[rand_num])
                cls.lose(team=two_player[0])

            elif rand_num == 0:
                cls.winner(team=two_player[rand_num])
                cls.lose(team=two_player[1])

            time.sleep(1)
            cls.clear()


def menu(user_inp):
    if user_inp == '0':
        Team.clear()
        Team.league_preview()
        exit()
    elif user_inp == '1':
        Team.clear()
        player_name = input("please enter the teams name.")
        Team.from_string(user_input_name=player_name)
        print(f"You have successfully added {player_name} to your league.")

    elif user_inp == '2':
        Team.clear()
        if len(team_info) < 2:
            print("You should have at least two teams to start!")
        else:
            Team.play(info_list=team_info)
    elif user_inp == "3":
        Team.clear()
        Team.league_preview()


while True:
    user_input = input("""Please select one of the options.
    0-> exit.
    1-> add players to the league.
    2-> play.
    3-> Show the leader board.
    """)
    menu(user_input)

# For quick testing :)
# first_team = Team(name="BARCA")
# second_team = Team(name="REAL")
# third_team = Team(name="EST")
#
# Team.play(info_list=team_info)
# Team.league_preview()
