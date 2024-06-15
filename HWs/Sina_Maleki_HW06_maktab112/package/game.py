import random
import pickle
from .file import FileEditor



class Game:
    # RAND_WORDS_DICT = {0: "rock", 1: "paper", 2: "scissors"}
    # USER_WORDS_DICT = {"r": "rock", "p": "paper", "s": "scissors"}
    game_stats = {"games_count": 0, "games_played": 0, "wins": 0, "draws": 0, "losses": 0}

    def __init__(self, games_count, game_played=0, wins=0, draws=0, losses=0):
        assert self.valid_games_count(value=games_count), "Games count should be a positive number."
        self.games_count = games_count
        self.game_stats["games_count"] = self.games_count

        self.game_played = game_played
        self.game_stats["games_played"] = self.game_played

        self.wins = wins
        self.game_stats["wins"] = self.wins

        self.draws = draws
        self.game_stats["draws"] = self.draws

        self.losses = losses
        self.game_stats["losses"] = self.losses

    # @classmethod
    # def from_file(cls, games_count, games_played, wins, draws, losses):
    #     pass

    @staticmethod
    def valid_games_count(value):
        if value > 0:
            return True
        else:
            return False

    @classmethod
    def save(cls):
        content: str = ""
        with FileEditor(path="package/test.txt", mode="wb") as file:
            # for k, v in cls.game_stats.items():
            #     content += f" {k} {v}"
            # print(content)
            pickle.dump(cls.game_stats, file)

    def load(self):
        with FileEditor(path="package/test.txt", mode="rb") as file:
            new_content = pickle.load(file)
            return new_content

    def start_trigger(self):

        for i in range(self.game_stats["games_count"] - self.game_stats["games_played"]):
            user_choice = self.player_choice()
            computer_action = self.computer_choice()

            print(self.game_show(user_choice=user_choice, computer_action=computer_action))
            self.game_logics(user_choice=user_choice, computer_action=computer_action)

    @staticmethod
    def game_show(user_choice, computer_action):
        game_info = f"{user_choice} vs {computer_action} "
        return game_info if user_choice != "exit" else "exiting"

    @staticmethod
    def player_choice():
        return input("Enter a choice (rock, paper, scissors, exit): ")

    @classmethod
    def computer_choice(cls):
        return random.choice(["rock", "paper", "scissors"])

    def game_logics(self, user_choice, computer_action):
        self.game_stats["games_played"] += 1

        if user_choice == computer_action:
            self.game_stats["draws"] += 1
            print(f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == "rock":
            if computer_action == "scissors":
                self.game_stats["wins"] += 1
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
                self.game_stats["losses"] += 1
        elif user_choice == "paper":
            if computer_action == "rock":
                self.game_stats["wins"] += 1
                print("Paper covers rock! You win!")
            else:
                self.game_stats["losses"] += 1
                print("Scissors cuts paper! You lose.")
        elif user_choice == "scissors":
            if computer_action == "paper":
                self.game_stats["wins"] += 1
                print("Scissors cuts paper! You win!")
            else:
                self.game_stats["losses"] += 1
                print("Rock smashes scissors! You lose.")
        elif user_choice.lower() == "exit":
            self.game_stats["games_played"] -= 1
            Game.save()

            print(exit())


def game_func():
    with FileEditor(path="package/test.txt", mode="r") as file_r:
        if len(file_r.read()) > 1:
            print("continuing your previous game...")
            with FileEditor(path="package/test.txt", mode="rb") as file:
                content = pickle.load(file=file)
                print(content)
                # print(content)
                my_game = Game(games_count=int(content["games_count"]), game_played=int(content["games_played"]), wins=int(content["wins"]),
                               losses=int(content["losses"]), draws=int(content["draws"]))
                my_game.start_trigger()
                with FileEditor(path="package/test.txt", mode='w') as file_l:
                    file_l.write("")

        else:
            game_counter_inp = int(input("Games count: "))
            my_game = Game(games_count=game_counter_inp)
            my_game.start_trigger()
            with FileEditor(path="package/test.txt", mode='w') as file:
                file.write("")

    print(Game.game_stats)
