# Sina Maleki - Python 112 - Group Number 1 -CW2
# ////////////////////////// Q number 3 //////////////////////////

try:
    with open('pHolder.py') as file:
        for line_ind, line in enumerate(file.readlines()):
            try:
                exec(line)
            except SyntaxError:
                print(f"Syntax error on line {line_ind + 1}.")

except FileNotFoundError:
    print("Could not find the file.")
