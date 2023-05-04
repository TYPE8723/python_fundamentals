# l1=[]
# lim=3
# for i in range(0,lim):
#     x=int(input("enter integer:"))
#     l1.append(x)

# print(l1)
# print("max :",max((l1)))


first=int(input("enter integer:"))
second=int(input("enter integer:"))
third=int(input("enter integer:"))

if first>second and first>third:
    print(first)
if second>first and second>third:
    print(second)
if third>second and third>first:
    print(third)
