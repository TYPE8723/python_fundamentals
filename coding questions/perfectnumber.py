# 6 (whose proper divisors are 1, 2, and 3, which add up to 6)
# 28 (whose proper divisors are 1, 2, 4, 7, and 14, which add up to 28)
# 496 (whose proper divisors are 1, 2, 4, 8, 16, 31, 62, 124, 248, which add up to 496)
# 8128 (whose proper divisors are 1, 2, 4, 8, 16, 32, 64, 127, 254, 508, 1016, 2032, 4064, which add up to 8128)

n=28
sum=0
for i in range(1,n):
    if n%i==0:
        sum = sum+i
        print(i)
        if n == sum:
            print({f"{n} is a perfect number"})
        

