# pip install request
import requests

r = requests.get("https://www.aparat.com/")
# r.encoding = "utf-8"
print(r.encoding)

# If you want to process on it you should use text
with open('aparat-txt.html', 'w') as f:
    f.write(r.text.encode("cp1252", "ignore").decode("65001"))

# If you want to process bytes you should use content
# with open('aparat-content.html', 'wb') as f:
#     f.write(r.content)


# print('Sina' in r.text)

# If a page is relient on js you can't use request on it!
# SSG ? SSR ?
# You may one to use request on other things like APIs


# API request
# user_response = requests.get('https://jsonplaceholder.typicode.com/users/1')
# print(user_response.status_code)
# print(type(user_response.content))

# The second one was just a byte class
# Hard way
# import json
# print(json.loads((users_response.content)))

# Easy
# print(user_response.json())
# print(user_response.json())

# This is list view rather than detail view
# users_response = requests.get('https://jsonplaceholder.typicode.com/users')
# This would be an array of jsons!
# print(users_response.text)
# print(type(users_response.json()))

# users = users_response.json()
# print(*[user["website"] for user in users], sep='\n')

# my_ip = requests.get('https://icanhazip.com/')
# print(my_ip.text)

# browser hijacking

# open inspect -> network -> copy as CURL to get everytHing
# You can convert the url in a converter to python code so you can use it.

# Digikala SMS:
# You can sniff json in pyload of your browser (network/auth/payload)
# sms_response = requests.post('https://api.digikala.com/v1/user/authenticate/', json={
#     "backUrl": "/",
#     "username": "09389274675",
#     "opt-call": False
# })
# print(sms_response.text)
# print(sms_response.status_code)

# ...
session = requests.Session()

# ...you load data with stream!
# counter = 1
# response_stream = requests.get("https://httpbin.org/stream/300", stream=True)
# for line in response_stream.iter_lines():
#     if line:
#         print(counter, "->", line)
#         counter += 1
