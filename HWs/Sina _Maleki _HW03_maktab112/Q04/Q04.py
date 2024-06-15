# # Sina Maleki - Python 112 - Group Number 1 -CW3
# ////////////////////////// Q number 4 //////////////////////////

text = "This is a sample paragraph. It contains several words, some of which are repeated." \
       " This is a good exercise to find the most frequent words."

frequency_list = list()
text_list = text.split(" ")
# set ---> to check uniq words
for word in set(text_list):
    counter = text_list.count(word)
    if counter >= 2:
        frequency_list.append(f"{word}: {counter}")

print(frequency_list)
