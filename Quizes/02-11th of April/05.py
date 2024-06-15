class Vet:
    space = 5
    animals = []

    def __init__(self, name):
        self.name = name

    def register(self):
        if Vet.space > 0:

            Vet.animals.append(self.name)
            Vet.space -= 1
        else:
            print("Don't have enought space.")

    def unregister(self):
        if self.name in Vet.animals:
            Vet.animals.remove(self.name)
        else:
            print("It's not registered!!!!")

    def cost_tretment(self, hour, rate):
        return hour * rate

