class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

    def __truediv__(self, other):
        return self.num // other.num

    def __gt__(self, other):
        return self.num > other.num

    def __ge__(self, other):
        return self.num >= other.num

    def __eq__(self, other):
        return self.num == other.num


num1 = Number(970)
num2 = Number(98)
print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 > num2)
print(num1 >= num2)
print(num1 == num2)
