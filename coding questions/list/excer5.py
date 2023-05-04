#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#listcomprhension
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

nl = [i for i in color if color.index(i) not in(0,4,5)]
print (nl)

# [a if a else 2 for a in [0,1,0,3]]
# [2, 1, 2, 3]
# can be done using enumerate function