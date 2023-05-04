import numpy
#recursion
def fun(val,fact):
    ini = val
    fact=fact*val
    if val==1:
        print(f"factorial of {ini} is {fact}")
        return
    else:
        val=val-1
        fun(val,fact)
n = 6
fun(n,1)


l1=[i for i in range(1,n+1)]

print("factorial:",numpy.prod(l1))