n=10
first,second = 0,1
for i in range(0,n):
    if i<=1:
        temp = i
    else:
        temp = first+second
        second = first
        first = temp
    print(temp)
    

# def loop(n):
#     n=n-1
#     print(n)
#     if n >= 0:
#         loop(n)
#     else:
#         return False

# n=5
# loop(n)