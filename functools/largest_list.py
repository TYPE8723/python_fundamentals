from  functools import reduce
lis = [1, 3, 5, 6, 2]
red = reduce(lambda a,b:a if a>b else b,lis)
print(red)