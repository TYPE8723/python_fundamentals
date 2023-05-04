
#str.swapcase()#can also be used
str = "Pythonist 2"
#data = " ".join(str)
#data = str.split(' ')
cased = [i.lower() if i.isupper() else i.upper() for i in str ]
joining = ''.join(cased)
print(joining)