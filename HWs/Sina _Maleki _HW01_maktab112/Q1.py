# Sina Maleki - Python 112 - Group Number 1
# ////////////////////////// Q number 1 //////////////////////////

x = int(input("Please enter a number. "))
divizers = 0
div_list = list()
# https://www.sanfoundry.com/python-program-generate-divisors-integer/
for number in range(1, x):
    if x % number == 0:
        div_list.append(number)
        divizers += number

i = 0
if divizers == x:
    print("Yes")
    # https://stackoverflow.com/questions/39996254/how-to-dynamically-print-list-values
    # https://realpython.com/python-enumerate/
    a = '+'.join(
        '{0}'.format(value) for index, value in enumerate(div_list)) + ' =' + f" {x}"
    print(a)

else:
    print("No")
    a = '+'.join(
        '{0}'.format(value) for index, value in enumerate(div_list)) + ' !=' + f" {x}"
    print(a)
