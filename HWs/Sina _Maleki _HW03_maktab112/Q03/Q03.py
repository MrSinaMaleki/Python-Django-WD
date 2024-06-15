# # Sina Maleki - Python 112 - Group Number 1 -CW3
# # ////////////////////////// Q number 3 //////////////////////////


# input_sentences = [
#     "This is a sample sentence.",
#     "Python programming is fun"
# ]
# print(set(input_sentences))


input_numbers = input("Please enter a bunch of numbers. ").split(" ")
# input_numbers = ["7", "1", "2", "3", "4", "5", "-1"]

# num = ["12"]
# for word in num:
#     print(word)


def sorter(list_text):
    tenp_list = list()
    final_list = list()
    for sentence in list_text:
        tenp_list.append(sentence.split(" "))
        for item in tenp_list:
            for word in item:
                final_list.append(word)

    return set(final_list)
    # Sorted ? for string


# print(sorter(input_sentences))
print(sorter(input_numbers))
