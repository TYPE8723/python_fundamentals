#How do we reverse a string in Python?
Str = [1,2,3,4,5,6,7,8,9,10]
print(Str[::-1])
revst = "hey guys"
print(list(reversed(revst)))
rev_str = list(reversed(Str))
print(rev_str)
print(revst[::-1])
#sorting string
var = "ABfFD"
print(sorted(var))#['A', 'B', 'D', 'F', 'f']
#reverse string
var = "ABfFD"
print(var[::-1])
#reverse string
var = "ABfFD"
print(var[::-2])#In other words, the [::-2] syntax specifies a slice that includes all characters in the string (:), but with a step size of -2 (-2) which means that it will skip every second character and move backwards (-).