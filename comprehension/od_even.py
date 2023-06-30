#conditioned list comprehension
qa=[1,2,5,1,8,3,89,3,3,54,7,4,5]
res= ['even' if i%2==0 else 'odd' for i in qa]#two condition
#res= ['even'  for i in qa if i%2==0] only one condition
print(res)