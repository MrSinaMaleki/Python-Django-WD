class Calculator:
    def __init__(self, num1, num2):
        self.num_validate(num1)
        self.num_a = num1

        self.num_validate(num2)
        self.num_b = num2

    @staticmethod
    def num_validate(number):
        if isinstance(number, int):
            return True
        else:
            return False

    def add(self):
        return self.num_a + self.num_b

    def sub(self):
        return self.num_a - self.num_b

    def mul(self):
        return self.num_a * self.num_b

    def div(self):
        assert self.num_b != 0, "The second number can't be 0."
        return self.num_a / self.num_b


my_cal = Calculator(2, 3)
print(my_cal.add())
print(my_cal.sub())
print(my_cal.mul())
print(my_cal.div())
