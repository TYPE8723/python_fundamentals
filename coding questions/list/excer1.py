#  Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

L1 = ['abc', 'xyz', 'aba', '1221']

def process(val):
    flag = False
    if len(val)>2:
        flag =  True
    item = list(val)
    flag =  item[0]==item[-1]
    return flag
    
val = map(process,L1)
print(list(val).count(True))

#from collections import Counter
#z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
#Counter(z)
# Counter({'blue': 3, 'red': 2, 'yellow': 1})