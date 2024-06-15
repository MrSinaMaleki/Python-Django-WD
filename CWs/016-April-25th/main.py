from pprint import pprint


class Animal:
    species = None
    number_of_legs = None
    sound = None

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"species:{self.species}, number of legs:{self.number_of_legs}, color:{self.color}, sound:{self.sound}"

    def __repr__(self):
        return f"species:{self.species}, number of legs:{self.number_of_legs}, color:{self.color}, sound:{self.sound}"


class FourLeggedAnimal(Animal):
    number_of_legs = 4


class TwoLeggedAnimal(Animal):
    number_of_legs = 2


class ZeroLeggedAnimal(Animal):
    number_of_legs = 0


class Wolf(FourLeggedAnimal):
    sound = "woof woof"

    def __init__(self, color):
        super().__init__(color=color)
        self.species = self.__class__.__name__


class Sheep(FourLeggedAnimal):
    sound = "Baa Baa"

    def __init__(self, color):
        super().__init__(color=color)
        self.species = self.__class__.__name__


class Snake(ZeroLeggedAnimal):
    sound = "ZZZ..."

    def __init__(self, color):
        super().__init__(color=color)
        self.species = self.__class__.__name__


class Parrot(TwoLeggedAnimal):
    sound = "squawk..."

    def __init__(self, color):
        super().__init__(color=color)
        self.species = self.__class__.__name__


class Cage:
    list_of_ids = list()
    animals_info = {}

    def __init__(self, id_number):

        self.validate_id(id_number)
        self.id_number = id_number

        self.animals_info.update({id_number: []})

    @classmethod
    def validate_id(cls, value):
        if value in cls.list_of_ids:
            cls.get_cage_id()
        else:
            cls.list_of_ids.append(value)

    @staticmethod
    def get_cage_id():
        cage_id_input = int(input("Error! Id is not Unique, Enter again cage(id): "))
        return Cage(cage_id_input)

    def add_animal(self, **animals):
        for k, v in animals.items():
            self.animals_info[self.id_number].append({k: v})

    def __repr__(self):
        return f"Cage({self.id_number})->{self.animals_info[self.id_number]}"

    def __str__(self):
        return f"Cage({self.id_number})->{self.animals_info[self.id_number]}"


class Zoo:
    list_of_cages = list()

    def __init__(self, *cages):
        self.cages = cages
        self.list_of_cages.append(cages)

    def __str__(self):
        for item in self.list_of_cages:
            return str(item)

    def __repr__(self):
        for item in self.list_of_cages:
            return str(item)

    def animals_by_color(self):
        for cage in self.cages:
            for animal in cage:
                print(animal.name)


# c2 = Cage(int(input("id: ")))


s1 = Sheep("Blue")
# print(s.species)
# print(s.number_of_legs)
# print(s.color)
# print(s)

p1 = Parrot("Red")
# print(p1.species)

w1 = Wolf("Blue")
# print(w1.number_of_legs)

c1 = Cage(1)
c1.add_animal(p1=p1, w1=w1)

c2 = Cage(2)
c2.add_animal(p1=p1, w1=w1, s1=s1)

z1 = Zoo(c1, c2)
z1.animals_by_color()
print(z1)
