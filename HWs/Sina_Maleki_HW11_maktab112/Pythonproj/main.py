from HWs.Sina_Maleki_HW11_maktab112.Pythonproj.models import Model


class Divar:
    database = {}

    @classmethod
    def rem_advertise(cls, username, title):
        if username not in User.registered_list:
            raise Exception("No such user")

        print(Ads.registered_list)
        if title not in [item["title"] for item in Ads.registered_list]:
            raise Exception("Access denied")

        # Deleting it from everyone's favorites
        for item in cls.database[username]["favorites"]:
            if item["title"] == title:
                cls.database[username]["favorites"].remove(item)
                print(f"removed '{title.title()}' from {username}'s favorites successfully")

        # print(item for item in cls.database[username]["owner:"])
        for item in cls.database[username]["owner:"]:
            if item["title"] == title:
                cls.database[username]["owner:"].remove(item)
                print(f"removed '{title.title()}' successfully")

                break
        else:
            raise Exception("access denied")




    @classmethod
    def add_favorite(cls, username, title):
        if username not in User.registered_list:
            raise Exception("Invalid username")

        for ad in cls.database[username]["favorites"]:
            if ad["title"] == title:
                raise Exception("already favorite")

        for ad in Ads.registered_list:
            if ad["title"] == title:
                cls.database[username]["favorites"].append(ad)
                print("added successfully")
                break
        else:
            raise Exception("invalid title")

    @classmethod
    def rem_favorite(cls, username, title):
        if username not in User.registered_list:
            raise Exception("Invalid username")

        # print("all fav:",cls.database[username]["favorites"])
        all_fav_ads_dict = [add for add in cls.database[username]["favorites"]]
        all_fav_ads_title = [t["title"] for t in all_fav_ads_dict]
        if title not in all_fav_ads_title:
            raise Exception("already not favorite")

        for ad in Ads.registered_list:
            if ad["title"] == title:
                cls.database[username]["favorites"].remove(ad)
                print("deleted successfully")
                break
        else:
            raise Exception("invalid title")

    @classmethod
    def list_my_advertises(cls, username, *args):
        if username not in User.registered_list:
            raise Exception("Invalid username")
        else:
            print(f"{username}: ", end="\t")
            _ = 1
            if not args:
                # wtf is a generator !
                # print(user.title for user in cls.database[username]["owner:"])
                # print(f"{username}:",(name for name in [i["title"] for i in cls.database[username]["owner:"]]), sep="\t")

                for add in cls.database[username]["owner:"]:
                    print(f"{_}-", add["title"], end="\t")
                    _ += 1

            else:
                # To be checked later.
                args_list = list()
                for i in args:
                    for j in i:
                        args_list.append(j)

                for add in cls.database[username]["owner:"]:

                    # https://www.geeksforgeeks.org/python-check-if-two-lists-have-any-element-in-common/
                    common_elements = set(add["tags"]).intersection(tuple(args_list))

                    if common_elements:
                        print(f"{_}-", add["title"], "tags: ", f"({add["tags"]})", end="\t")
                        _ += 1
                    else:
                        pass

    @classmethod
    def list_favorite_advertises(cls, username, *args):

        if username not in User.registered_list:
            raise Exception("Invalid username")
        else:
            print(f"{username}: ", end="\t")
            _ = 1
            if not args:

                for add in cls.database[username]["favorites"]:
                    print(f"{_}-", add["title"], end="\t")
                    _ += 1
            else:

                args_list = list()
                for i in args:
                    for j in i:
                        args_list.append(j)

                for add in cls.database[username]["favorites"]:

                    # https://www.geeksforgeeks.org/python-check-if-two-lists-have-any-element-in-common/
                    common_elements = set(add["tags"]).intersection(tuple(args_list))

                    if common_elements:
                        print(f"{_}-", add["title"], "tags: ", f"({add["tags"]})", end="\t")
                        _ += 1
                    else:
                        pass

        # if username not in User.registered_list:
        #     raise Exception("Invalid username")
        # else:
        #
        #     print(f"{username}: ", end="\t")
        #     _ = 1
        #     for add in cls.database[username]["favorites"]:
        #         print(f"{_}-", add["title"], end="\t")
        #         _ += 1


class User(Model):
    registered_list = list()

    def __init__(self, username) -> None:
        self._username = username
        if username not in self.registered_list:
            self.registered_list.append(username)
        else:
            raise Exception("Repeated username!")

        print(f"added ({username}) as a user of our website. ")
        Divar.database[username] = {"owner:": [], "favorites": []}

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, new_value) -> None:
        self.username = new_value


class Ads(Model):
    # registered_list = ()
    registered_list = list()

    def __init__(self, username, title, *tags) -> None:
        self.title = title
        # self.tags = tags if tags != () else "No Tags"
        self.tags = tags
        # print(self.tags)

        if username not in User.registered_list:
            raise Exception("No such user.")

        if title not in self.registered_list:
            self.registered_list.append({"title": title, "tags": self.tags})
        else:
            raise Exception("Repeated ad title!")

        Divar.database[username]["owner:"].append({"title": title, "tags": self.tags})
        print(f"added '{title.title()}' for ({username.title()}).")


# test info :)
User("Sina")
User("Ali")
Ads("Sina", "Dining kitchen table for sale.")
Ads("Sina", "LAPTOP.", "selling", "buying")
Ads("Sina", "Tv", "selling")
Ads("Sina", "test", "tag1")
Ads("Sina", "pc")

Divar.add_favorite("Sina", "LAPTOP.")
Divar.add_favorite("Sina", "Tv")
# print(Divar.database)
# print(Ads.registered_list)
Divar.list_my_advertises("Sina", "selling")


# print(Divar.database)
# Divar.rem_favorite("Sina", "LAPTOP.")
# print(Divar.database)


# Divar.rem_advertise("Sina", "LAPTOP.")

# Divar.list_my_advertises("Sina")
# print(Divar.database)

# Divar.list_my_advertises("Sina")


# Divar.list_my_advertises("baba eti!")


class Menu:

    @staticmethod
    def register():
        User(user_input[1])

    @staticmethod
    def add_advertise():
        if len(user_input) <= 3:
            Ads(user_input[1], user_input[2])
        else:
            Ads(user_input[1], user_input[2], user_input[3:])

    @staticmethod
    def rem_advertise():
        Divar.rem_advertise(user_input[1], user_input[2])

    @staticmethod
    def list_my_advertises():
        if len(user_input) <= 2:
            Divar.list_my_advertises(username=user_input[1])
        else:
            Divar.list_my_advertises(user_input[1], user_input[2:])

    @staticmethod
    def add_favorite():
        Divar.add_favorite(username=user_input[1], title=user_input[2])

    @staticmethod
    def rem_favorite():
        Divar.rem_favorite(username=user_input[1], title=user_input[2])

    @staticmethod
    def list_favorite_advertises():
        if len(user_input) <= 2:
            Divar.list_favorite_advertises(username=user_input[1])
        else:
            Divar.list_favorite_advertises(user_input[1], user_input[2:])


command_count = int(input("commands count:"))
menu = Menu()
while command_count > 0:
    user_input = input("> ").split(" ")
    getattr(menu, user_input[0])()
    command_count -= 1

# first way
# menu_dict = {"register": Menu.user_initiator, "add_advertise": Menu.ads_initiator}
# menu_dict.get(user_input[0])() if not "NoneType" or "None" else print("There is no such command!")
# menu_dict.get(user_input[0], "There is no such command! ")

# second way
