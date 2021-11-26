import re

st1 = '<img src="F:\WPS\\4.img" height=“100” width="100">'
a = re.search('src=.*? ', st1).group()
print(a)
