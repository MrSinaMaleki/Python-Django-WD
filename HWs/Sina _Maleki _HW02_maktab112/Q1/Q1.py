
# Sina Maleki - Python 112 - Group Number 1 -CW2
# ////////////////////////// Q number 1 //////////////////////////
import time
import os


# https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/
def file_reader():
    for line in raw_text:
        # https://stackoverflow.com/questions/65167647/how-can-i-detect-ctrlc-in-python3-8
        print(line, end="\r")
        time.sleep(.5)
    input()


def menu():
    print("Please select one of the options.")
    print(" 1)KeepTyping")
    print(" 2)Clear the file")
    print(" 0)exit")


def exit_program():
    pass


def add_text_to_file():
    f = open('output.txt', 'a')
    new_text = input("Please type s.th. ")
    f.write(new_text)
    f.write("\n")
    print("Here is the new file: ")


def deleting_content():
    ext_f = input("Are you sure you want to clear your file(y/n)? ")
    if ext_f.lower() == 'y':
        f = open('output.txt', 'w+')
        f.write('')
        raw_text = f.readlines()
        f.close()
        print("You file has been cleared")
        user_input = '1'
    else:
        pass


menu_status = False
flag = True
while flag:
    # https://stackoverflow.com/questions/39796689/why-doesnt-this-python-keyboard-interrupt-work-in-pycharm
    # posix is os name for Linux or mac
    try:
        if menu_status:
            menu_status = True
            raise KeyboardInterrupt

        f = open("output.txt", "r")
        raw_text = f.readlines()
        file_reader()

    except KeyboardInterrupt:

        if os.name == 'posix':
            os.system('clear')
        # else screen will be cleared for windows
        else:
            os.system('cls')

        menu()
        user_input = input()

        if user_input == '0':
            ext_f = input("Are you sure you want to exit(y/n)? ")
            if ext_f.lower() == 'y':
                flag = False
            else:
                pass

        elif user_input == '1':
            add_text_to_file()

        elif user_input == '2':
            deleting_content()
            print("Back to typing:)")
            add_text_to_file()

        else:
            menu_status = True
            continue
            # menu()
            # user_input = input()
