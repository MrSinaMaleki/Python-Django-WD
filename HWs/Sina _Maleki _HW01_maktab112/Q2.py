# Sina Maleki - Python 112 - Group Number 1
# ////////////////////////// Q  number 2 //////////////////////////
# 2**i = pow(2,i)

x = int(input("Please enter a number that you want to check. "))
i = 0
stat = False
while i < x:
    if 2**i == x:
        stat = True
        i = x
    else:
        i += 1


if stat:
    print(f"Yes, {x} is a power of 2")
else:
    print(f"No, {x} is not a power of 2")
