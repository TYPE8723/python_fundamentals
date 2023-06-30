Subj = ["Math", "English", "computer", "Music"]
marks = [98, 90, 75, 100]

combined = zip(Subj,marks)

print(dict(combined))

l1=['CAR','BIKE','BUS','AUTO']
l2=[1,2,3,4,5,6]
zipper = zip(l1,l2)
l1_l2=list(zipper)
print(l1_l2)
z1,z2=zip(*l1_l2)
print(z1)
print(z2)