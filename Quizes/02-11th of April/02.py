class NewT:
    def __init__(self, movement, time, mass):
        self.movement = movement
        self.time = time
        self.mass = mass
        self.speed = None
        self.acc = None
        self.ni = None

    def velocity(self):
        self.speed = self.movement / self.time
        return self.speed

    def acceleration(self):
        self.acc = self.velocity() / self.time
        return self.acc

    def niro(self):
        # Tabdil jerm be vazn : 9.8 / mass --> weight
        self.ni = self.acceleration() * self.mass * 9.8
        return self.ni


my_ins = NewT(20, 10, 10)
print(my_ins.velocity())
print(my_ins.acceleration())
print(my_ins.niro())
