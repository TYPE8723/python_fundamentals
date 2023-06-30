from  functools import reduce
lis = [1, 3, 5, 6, 2]
red = reduce(lambda a,b:a+b,lis)#takes first 2 elements of lis and add,the sum is then placed in a and then third element is added,this continues
print(red)