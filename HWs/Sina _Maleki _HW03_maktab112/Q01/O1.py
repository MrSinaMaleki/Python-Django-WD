# # Sina Maleki - Python 112 - Group Number 1 -CW3
# # ////////////////////////// Q number 1 //////////////////////////

def encrypt(digit_string):
    digit_list = list()
    for number in str(digit_string):
        digit_list.append(number)

    new_set = set(digit_list)
    new_list = list(new_set)

    for item in new_list:
        counter = digit_list.count(item)

        if counter >= 2:
            new_list.append(counter)

    final_list = list()
    for st_num in new_list:
        final_list += str(st_num)

    final_value = ''
    for number in sorted(final_list):
        final_value += str(number)

    if digit_string == int(final_value):
        return int(final_value)
    else:
        return encrypt(int(final_value))


print((encrypt(442254545)))
