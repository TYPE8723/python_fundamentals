s1={'pop','rock','mock','sock',2,3,6,2,2,3,78,1,'rock'}
print(s1)
#add
s1.add("abcd")# add single item at a time
print(s1)
#update
s1.update(["***","###",'91'])#add multiple items at same time
s1.update("@@@@@")
print(s1)
#remove
s1.remove('abcd')#discard()#remove()raises key error if not found|#discard() raises nothing if not found
print(s1)
print("rock in set :",'rock' in s1)
fruits = {"tomato","brinjal","coconut","tamarind"}
set_union=s1.union(fruits)
print(set_union)
vegis = {"tomato","brinjal"}
print("subset :",vegis.issubset(set_union))
print("subset :",set_union.issuperset(vegis))
set_diff = fruits.difference(vegis)
print("difference",set_diff)
integer_set = {24,1,2,3,4,5}
print(integer_set.pop())#removes a arbitrary element at random
print(integer_set.pop())#removes a arbitrary element at random
print("sum of integer only set",sum(integer_set))
#print("sum of mixed set",sum(integer_set))