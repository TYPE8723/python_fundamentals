import sys
class A:
    def __init__(self,lists):
        j=0
        try:
            for i in lists:
                j=j+1
                print(lists[j])
        except :
            print('met with an error')
A([1,2,3,4,5,6,7,8])#normal try catch

class B:
    l1 = [1,2,6,2,0,4,2,7,8]
    val = map(lambda ds:ds/0,l1)
try:
    print(list(B().val))
except(ZeroDivisionError):
        print ('error caught')
        print('error'+ str(sys.exc_info()[0]))
finally:
    print('pheww!! completed')