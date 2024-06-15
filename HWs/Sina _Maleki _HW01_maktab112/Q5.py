# Sina Maleki - Python 112 - Group Number 1
# ////////////////////////// Q number 5 //////////////////////////

# https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
z_len, ab_len = input("Please enter Z's len and A&B's len with space separation. ").split()

# .replace ---> 1 2 = 12
z_value = input("Please enter Z list with space separation. ").replace(" ", "")
z_value_list = list()
if int(z_len) == len(z_value):
    for i in z_value:
        if i.isdigit():
            z_value_list.append(i)
else:
    print(f"You should only mention {z_len} items")

happiness_level = 0

a_value = input("Please enter A list with space separation. ").replace(" ", "")
a_value_list = list()
if int(ab_len) == len(a_value):
    for i in a_value:
        if i.isdigit():
            a_value_list.append(i)
else:
    print(f"You should only mention {ab_len} items")

for i in a_value_list:
    if i in z_value_list:
        happiness_level += 1

b_value = input("Please enter B list with space separation. ").replace(" ", "")
b_value_list = list()
if int(ab_len) == len(b_value):
    for i in b_value:
        if i.isdigit():
            b_value_list.append(i)
else:
    print(f"You should only mention {ab_len} items")

for i in b_value_list:
    if i in z_value_list:
        happiness_level -= 1

# print(z_value_list, a_value_list, b_value_list)
print(f"You happiness level equals to : {happiness_level}")
