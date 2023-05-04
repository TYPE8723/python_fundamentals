dict_1 = {'Geeks': 10, 'for': 12, 'Geek': 31}
#converting to list of tuples
#meth1 comprehension
x = [(key,val) for key,val in dict_1.items()]
print(x)

#meth2 convertionsfrom items
x = dict_1.items()
new_list=list(x)
print(new_list)

#meth3 convertions from ziping
z1=zip(dict_1.keys(),dict_1.values())
z_list = list(z1)
print(z_list)

#combining to dict_1
result = dict(z_list)
print(result)