x = lambda x,y : x+10+y
print(x(5,6))
################################################################
#lambda in a fucntion
#def func(x):
#    lamb = lambda v : v + 20 * x
#    return lamb(2)
#
#print(func(2))
##################################################
#a =[1,2,3,4,5,6,7,8,9,10] 
#
#traverse = map(lambda x :x+1,a)
#print(list(traverse))
###################################


l=['tomato','cabbage','ball','rice','potato','tri']

lamb=lambda x : x+'ABC'

data = map(lamb,l)

print(list(data))

process = lambda x,y,z : x+y+z

print(process(1,2,3))


#pass multiple arguments
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

process=lambda x,a,b:x*a+1+b

data= map(lambda x:process(x,0,2),my_list)
print(list(data))
# the lambda function process takes two arguments: x and a, and returns the result of x * a + 1. Then, the map() function is called with a lambda function that takes a single argument x, and applies it to each element in my_list, calling process(x, 0) to get the result. Finally, the map() object is converted to a list using the list() function and printed to the console.