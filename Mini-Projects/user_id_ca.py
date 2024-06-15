class Human:
    id_num = 1

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.id_num = Human.id_num
        Human.id_num += 1

    def __str__(self):
        return f"This is {self.id_num}: {self.first_name} {self.last_name}, He is {self.age} years old."


print(Human("Sina", "Maleki", 20))
print(Human("Armin", "Dadkhah", 19))
print(Human("MohammadMatin", "Eslami", 20))

