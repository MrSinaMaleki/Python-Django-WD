
# Sina Maleki - Python 112 - Group Number 1 -CW2
# ////////////////////////// Q number 2 //////////////////////////


def sed(file_input, file_output, patter_string, replacement_string):
    try:
        fi = open(file_input, 'r')
        raw_content = fi.readlines()
        fi.close()
        str_content = ''
        for item in raw_content:
            str_content += item.lower()

        fo = open(file_output, 'w')
        fo.writelines(str_content.replace(patter_string, replacement_string))
        fo.close()

    except FileNotFoundError:
        print("We couldn't find the file!")


sed('f', 'files/output_string.txt', 'sina', 'reza')
