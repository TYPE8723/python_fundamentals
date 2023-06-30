import itertools
pairs=[[2, 10], [5, 7], [5, 7], [2, 10]]
pairs.sort()
data=list(pairs for pairs,_ in itertools.groupby(pairs))
print(data)

pairs=[[2, 10], [5, 7], [5, 7], [2, 10]]
pairs.sort()
data = list(pairs for pairs,_ in itertools.groupby(pairs))
print(data)