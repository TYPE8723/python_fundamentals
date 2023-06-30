# A function that returns the length of the value:
process = lambda x: len(x)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
#sorts based on the length of car
cars.sort(reverse=False,key=process)#here each element is passed to process from cars list
print(cars)


l=[5,3,0,3,1,2,]
l1 = sorted(l)#should be saved to a new varible


l=[5,3,0,3,1,2,]
#sorted(iterable, key=key, reverse=reverse)
l.sort(reverse=False)#shoudnt be saved to a new variable
print(l)
# 
# USE OF KEY
# The key parameter in the sorted() function is used to specify a function that will be called on each element of the iterable being sorted. The key function dosent manipulate the result it just perform the function and return the resut the sort function would then show the sorted version of that particuar function operation