#https://www.scaler.com/topics/difference-between-sort-and-sorted-in-python/
main_data=[2,3,1,54,2,2]#{'a': 2, 'b': 1, 'c': 3}#{8, 9, 4, 6, 7}#[2,3,1,54,2,2]
l=main_data
l.sort()#work for tuple|dosent work for set| dict
print(l)
l=main_data
var=sorted(l)
print(var)