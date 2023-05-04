#split and join

# Split the string into list of strings

# Input : Geeks for Geeks
# Output : ['Geeks', 'for', 'Geeks']


# Join the list of strings into a string based on delimiter ('-')

# Input :  ['Geeks', 'for', 'Geeks']
# Output : Geeks-for-Geeks
l1 =['Geeks', 'for', 'Geeks']

joined = '-'.join(l1)
print(joined)

splited = joined.split("e")
print(splited)