# Get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
#[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
l1 = [(2, 5,4), (1, 2,1), (4, 4,8), (2, 3,5), (2, 1,1)]

process = lambda x:x[-1]

print(sorted(l1,key=process))