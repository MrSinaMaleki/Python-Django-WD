class Human:
    def __init__(self, name, age):
        self.name = name

        assert self.validate_age(age), "age can not be negative"
        self.age = age

    @staticmethod
    def validate_age(age):
        if int(age) > 0:

            return True
        else:
            return False


class Player(Human):
    def __init__(self, name, age, payment, post, efficiency):
        super().__init__(name=name, age=age)
        assert self.payment_validate(payment_input=payment), "Payment can't be negative"
        self.payment = payment
        assert self.validate_age(age), "age should be between 15 and 30"
        self.age = age
        self.post = post

        assert self.validate_efficiency(efficiency_input=efficiency), "efficiency should be between 0 and 100"
        self.efficiency = efficiency

    @staticmethod
    def payment_validate(payment_input):
        if int(payment_input) > 0:
            return True
        else:
            return False

    @staticmethod
    def validate_age(age):
        if 15 >= int(age) >= 30:

            return True
        else:
            return False

    @staticmethod
    def validate_efficiency(efficiency_input):
        if 0 >= int(efficiency_input) >= 100:
            return True
        else:
            return False


# https://www.w3schools.com/python/python_inheritance.asp#:~:text=When%20you%20add%20the%20__,parent's%20__init__()%20function.
class Mentor(Human):
    def __init__(self, name, age, payment, start_date, end_date, flag=True):
        assert self.validate_age(age), "The age should be between 30 and 65"
        super().__init__(name=name, age=age)
        self.payment = payment
        self.start_date = start_date
        self.end_date = end_date
        self._flag = flag

    @property
    def flag(self):
        self._flag = False
        return self._flag

    @staticmethod
    def validate_age(age):
        if 30 <= int(age) <= 65:
            return True
        else:
            return False


class Team:
    player = []
    mentor = None
    points = 0

    def __init__(self, player_object, mentor_object):

        # self.mentor = mentor

        self.player_obj = player_object
        Team.player.append(player_object)
        assert Team.validate_team_members(), "Players should not be more than 11"
        # assert len(Team.player) <= 11, "players should not be more than 11"

    @classmethod
    def validate_team_members(cls):
        if len(cls.player) <= 11:
            return True
        else:
            # cls.player.pop()
            return False

    def team_score(self):
        pass

    def create_player(self):
        for i in range(11):
            info_list = input("name-age-payment-post-efficiency").split("-")
            Team.player.append(info_list[0])
            return Player(info_list[0], info_list[1], info_list[2], info_list[3], info_list[4])

    def create_mentor(self):

        info_list = input("name-age-payment-start_date-end_date").split("-")
        mentor_obj = Mentor(info_list[0], info_list[1], info_list[2], info_list[3], info_list[4])
        mentor_obj.flag

        print(mentor_obj.flag)

        return Team(mentor_obj, self.create_player())


my_team = Team("Reza", "Ali")
Team.create_mentor(my_team)

# one = Player()

# Team("s")
# Team("a")
# Team("b")
# Team("c")
#
# Team("s")
# Team("a")
# Team("b")
# Team("c")
#
# Team("s")
# Team("a")
# Team("b")
# Team("c")

# print(Team.player)
# print(len(Team.player))
