from collections import Counter
#d1 = {'key1': 50, 'key2': 20, 'key3':200}
#d2 = {'key1': 200, 'key2': 100, 'key4':300}
#new_dict = Counter(d1) + Counter(d2)
#print(new_dict)
##############
#d = {123:32,32:12}
#e = {3123:32,12412:1,32:10000}
#c = Counter(d)+Counter(e)
#print(d)
#print(c)
############
#c1 = Counter(A=4,  B=3, C=10)
#c2 = Counter(A=10, B=3, C=4)
 
#c1.subtract(c2)
#print(c1)
##############
#c_d = Counter(d1)
#dict.update(c_d,{'new':777})
#print(c_d.values())
################################
#c = Counter(cats=4,dog=6)
#print(list(c.elements()))
###########################
#s1 = Counter(['a','b','a','c','a','F','F','F','F','F','e','a','R','c','c','c','c','c'])
#print(s1.most_common(5))
#############################
s1 = Counter(a=10,b=20,c=40)
s2 = ('a','a','b','c','d')
s1.subtract(s2)
print(s1)
