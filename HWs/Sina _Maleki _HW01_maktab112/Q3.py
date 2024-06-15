# Sina Maleki - Python 112 - Group Number 1
# ////////////////////////// Q number 3 //////////////////////////

text = str(input("Please enter a text: "))
numbers = 0
letters = 0
for index in text:
    if index in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        numbers += 1
        # https://www.geeksforgeeks.org/python-program-to-calculate-the-number-of-digits-and-letters-in-a-string/
    elif index.lower().isalpha():
        letters += 1

print("Letters : ", letters)
print("digits : ", numbers)