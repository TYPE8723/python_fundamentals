#Write a program in Python to find sum of digits #of a number using recursion?
x=list(str(23))
def add(val,sum):
    sum=sum+int(val[0])
    try:
        del val[0]
        add(val,sum)
    except:
        print("sum is :",str(sum))
    
add(x,0)