x = 153
#power = len(x)
x_l = list(str(x))
sum=0
for i in x_l:
    sum = sum+int(i)**len(x_l)

print(sum)
