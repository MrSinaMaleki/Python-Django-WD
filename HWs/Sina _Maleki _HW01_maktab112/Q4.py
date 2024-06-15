# Sina Maleki - Python 112 - Group Number 1
# ////////////////////////// Q number 4 //////////////////////////

text = str(input("Please enter your text. "))
new_text = list()

for index in text:
    if index.isupper():
        new_text.append(f" {index}")
    else:
        new_text.append(index)

print(''.join(new_text))