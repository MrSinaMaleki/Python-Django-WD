# https://www.crummy.com/software/BeautifulSoup/bs4/doc/


import bs4
import requests

# Parsers
import html

zoomit_content = requests.get('https://www.zoomit.ir/').content
soup = bs4.BeautifulSoup(zoomit_content, "html.parser")
# soup = bs4.BeautifulSoup(zoomit_content, )

# Search in document: ( find
# print(soup.find('title').text)
# print(soup.find('h1'))
# print(soup.find_all('h2'))

# print(soup.find('h2', class_="hmWIXE").text)
# print(soup.find('h2', class_="hmWIXE").text)
# print(soup.find(id="__next").name)
# print(soup.find('a').href)  # none
# print(soup.find('a')['href'])

# CSS selector
v_conetnt = requests.get("https://www.varzesh3.com/").content
soup = bs4.BeautifulSoup(v_conetnt, "html.parser")

# print(*[tag.text for tag in soup.select("#new .videobox a:last-child > h3")])

print(soup.find(id="new").find(class_="videobox").find('a'))

print(*[tag.text for tag in soup.find_all('h3')], sep="\n")
