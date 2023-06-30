import itertools
nums = [1,2, 4, 5, 7, 9, 10]
target = 12
index=0
pairs=[]
for i in nums:
    nums.pop(index)
    for j in nums:
        s=j+i
        if s==target:
            if [i,j] in pairs:
                pass
            else:
                pairs.append(sorted([i,j]))
    nums.insert(index,i)
    index=index+1
pairs.sort()
data=list(pairs for pairs,_ in itertools.groupby(pairs))
print(data)