import re


# class EmailValidator:
#     @staticmethod
#     def isvalid(email):
#         pattern = re.compile(r'\b[\w.-]+@[\w.-]+\.\w{2,4}\b')
#         if re.fullmatch(pattern, email):
#             return True
#         else:
#             return False
#
#
# c = EmailValidator()
# print(c.isvalid("hamedreza1992@gmail.co.com"))
#
#
# class PhoneNumberExtractor:
#     @staticmethod
#     def extract (phone):
#         pattern = re.compile(r'[+(\d]{1}[\d+() -.]{5,16}[+\d]{1}',flags=re.MULTILINE)
#         print(re.findall(pattern, phone))
#
#
# c=PhoneNumberExtractor()
# c.extract("""
# +989197521814
# 0919185454489
# +919367788755
# 8989829304
# +16308520397
# 786-307-3615
# 789
# 123765
# 1-1-1
# +982
# """)


# class HTMLTagExtractor:
#     @staticmethod
#     def extract (phone):
#         pattern = re.compile(r'<\w+',flags=re.MULTILINE)
#         df=set(map(lambda x:x+">",re.findall(pattern, phone)))
#         print(df)
#
#
# c=HTMLTagExtractor()
# c.extract("""
#
#
# <table border=\"0\">It doesnt do anything</table>
# <div /> is not a self closing tag
# <div></div>
# <div background=\"\">use CSS background src</div>
# <div align=\"\">use CSS text-align</div>
# <label valign=\"\">use CSS vertical-align</label>
# <body id=\"hello\" bg=\"black\">bg is depricated</body>
# <a style=\"height:15pc;\"></a>
# <input height=\"0\"/>
# <p nowrap=\"\">this should have used css white-space</p>
# <p style=\"white-space=nowrap;\"></p>
# <input checked=\"\">checked is a binary either there or not can be missleading</input>
# <input id=\"blah\" checked />
# <script language=\"\" src=\"\" type=\"text/javascript\">just use the type attribute</script>
# <img border=\"0\"/> use CSS
# <form href=\"\"/>href shouldnt be empty invalid
# <form href=\"helloworldtest.html\">Correct</form>
# <frameset>obsolete
# <nobr>obsolete
# <big>Bold Text</big>obsolete
# <applet>My applet that doesnt work anymore because its old</applet>obsolete
# document.all old browser javascript feature
# """)



# class Password_Validator:
#     @staticmethod
#     def valid_is(password):
#         pattern = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$', flags=re.MULTILINE)
#         print(re.findall(pattern, password))
#
#
# c=Password_Validator()
# c.valid_is("""
# ipsum
# asdasdafsdfgr3at@3wdsGasdfsadf744584ad
# a
# ab
# abc
# abcd
# abcde
# john doe
# johnny
# jkjsdfhs#Yjkahsd4458478
# """)


class URLExtractor:
    @staticmethod
    def extract (url):
        pattern = re.compile(r'(https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*))',flags=re.MULTILINE)
        print(re.findall(pattern, url))


c=URLExtractor()
c.extract("""
abcdef
www.whatever.com
https://github.com/geongeorge/i-hate-regex
https://www.facebook.com/
https://www.google.com/
https://xkcd.com/2293/
https://this-shouldn't.match@example.com
http://www.example.com/
""")