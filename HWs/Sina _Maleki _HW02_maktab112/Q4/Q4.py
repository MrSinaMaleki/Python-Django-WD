
# Sina Maleki - Python 112 - Group Number 1 -CW2
# ////////////////////////// Q number 4 //////////////////////////
import math
import os


def terminal_cls():
    if os.name == 'posix':
        os.system('clear')
    # else screen will be cleared for windows
    else:
        os.system('cls')

try:
    a = int(input("Please enter the first number."))
    print("Please select one of the options. ")
    print(" + ", " - ", " / ", " % ", " √(r) ", "factorial", "power", "sin(degrees)", sep=',')
    opp = str(input())

    if opp == '+':
        b = int(input("Please enter the second number. "))
        terminal_cls()
        print(f'{a}{opp}{b}={a + b}')

    elif opp == '-':
        b = int(input("Please enter the second number. "))
        terminal_cls()
        print(f'{a}{opp}{b}={a - b}')

    elif opp == '/':
        # if b == 0:
        #     print("The second number shouldn't be zero!")
        #     b = int(input("Please enter the second number. "))
        #     print(a/b)
        b = int(input("Please enter the second number. "))
        terminal_cls()
        print(f'{a}{opp}{b}={a / b}')

    elif opp == '%':
        b = int(input("Please enter the second number. "))
        terminal_cls()
        print(f'{a}{opp}{b}={a % b}')

    elif opp == '√' or opp == 'r':
        b = int(input("Please enter n. "))
        terminal_cls()
        # https://www.geeksforgeeks.org/precision-handling-python/
        print("{:.2f}".format(pow(a, 1/b)))

    elif opp == 'factorial' or opp == "f":
        terminal_cls()
        res = math.factorial(a)
        message = "1"
        i = 2
        while i <= a:
            message += f'*{i}'
            i += 1

        print(f"{message} = {res}")

    elif opp == 'power' or opp == "p":
        b = int(input("to the power of ?. "))
        print(math.pow(a, b))

    elif opp == 'sin' or opp == 's':
        res = math.sin(math.radians(a))
        print("sin{}={:.2f}".format(a, res))


except ValueError:
    print("You should enter a number. ")

except ZeroDivisionError:
    print("The second number shouldn't be zero!")
