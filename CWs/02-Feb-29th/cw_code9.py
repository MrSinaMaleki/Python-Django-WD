my_input = input("Enter Your Strings: ").split()

for j in range(len(my_input)):
    for i in range(len(my_input)):
        if len(my_input[j]) > len(my_input[i]):
            temp = my_input[i]
            my_input[i] = my_input[j]
            my_input[j] = temp
my_input = my_input[::-1]

print(my_input)
print(my_input)
print(", ".join(my_input))
