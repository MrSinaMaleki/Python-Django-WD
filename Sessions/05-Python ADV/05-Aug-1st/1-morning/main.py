# replace, find, validation => Regex

# https://regexr.com/
# You can use the following website for practice test.

# .
# ^
# $
# +
# [ou] --> o or u
# [0-9]
# 1[0-9]|[0-9]
#


### https://regex101.com/
# \ARegEcr
# \A vs ^ is that the scap one checks the first line but ^ checks all of the first lines.

# Bundry ??
# [A-Z][a-z]{3}\b
# \d \D
# \b \B
# \v ---> vertical s.th
# \s --->select charecters
# \S ---> anything but spaces
# \w ---> [A-z0-9_]


# replace, find , validation
import re

text = ""

email_phone_value = "ismryazdan@gmail.cpm"

pattern = re.compile(r'^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$', flags=re.MULTILINE | re.IGNORECASE)
# You can also use diffrent flags.

# Get  the new patteren from mryazdan github.
# Usig the parantezes you can deal with groups.
# Using ?P<word> you can give names you your groups of obj

# for index, email in enumerate(re.findall(pattern, text)):
# for index, email in enumerate(pattern.findall(text)):
#     print(index + 1, email)

if match_object := re.search(pattern, text):
    print(match_object)
    print(match_object.span())
    print(match_object.group())
    # print(match_object.group(2))
    print(match_object.group('before'))
    # print(match_object.groups())
    print(match_object.end())
    print(match_object.start())

# replacement:

# re.sub(pattern,":) ", text)


print(re.split(pattern, text))
