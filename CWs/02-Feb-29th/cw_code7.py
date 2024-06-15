num1 = float(input("Please enter num1: "))
num2 = float(input("Please enter num2: "))


def my_division(x, y):
    counter = 0
    decimal_counter = 0
    mark = ""
    x_pos = abs(x)
    y_pos = abs(y)

    while x_pos >= y_pos:
        x_pos -= y_pos
        counter += 1

    x_pos *= 10000
    while x_pos >= y_pos:
        x_pos -= y_pos
        decimal_counter += 1

    if (x < 0 < y) or (x > 0 > y):
        mark = "-"

    return float(f"{mark}{counter}.{decimal_counter}")


print(type(my_division(num1, num2)))
print("Division = ", my_division(num1, num2))

