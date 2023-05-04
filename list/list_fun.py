# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
#sorted(iterable, key=key, reverse=reverse)

l1=[1,2,3,4,5,6,7]
l1.append([22,23])#takes in one argument
l1.clear()#clears list
l1=[1,2,3,4,5,6,7]
l2=l1.copy()#creates a  new copy of l1 in l2 
l2[5]=2#changes l2 only
count=l2.count('asd')#count of occurence of 2 in list
print("COUNT :",count)
l1.extend([23,67,'dsf'])
print(l2.index(5))#display value  at the index
print('**l12',l2)
print(l2.pop(1))#removes value at the specified index
print(l2)
l2.reverse()
print("REVERSED :",l2)
l2.sort()
print("sorted :",l2)
print(l1)
print(l2)