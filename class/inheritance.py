class A:
    first = 1
    second = 2
    def fun(self):
        return str(self.first+self.second)
class C:
    fifth = 6
    sixth = 7
    
class B(A):#single hierarchical
    third = 3
    forth = 4

class D(A,C):#multilevel
    eight = 5
    seventh = 8
class E(B):#multiple
    nintth = 9
    tenth = 10
class F(A):#hierarchical inheritance
    eleventh =11
    twelth = 12
     

obj1 = B()
print('from B :',obj1.third)
print('from B :',obj1.forth)
print('from A :',obj1.first)
print('from A :',obj1.second)
obj2 = D()
print('from C :',obj2.fifth)
print('from C :',obj2.sixth)
print('from A :',obj2.first)
print('from A :',obj2.second)
print('from A fun call:',obj2.fun())
print('from D :',obj2.eight)
print('from D :',obj2.seventh)
obj3 = E()
print('*****obj3*****')
print('from B :',obj3.third)
print('from B :',obj3.forth)
print('from A :',obj3.first)
print('from A :',obj3.second)
print('from e :',obj3.nintth)
print('from e :',obj3.tenth)
obj4 = F()
print('*****obj4*****')
print('from A :',obj4.first)
print('from A :',obj4.second)
print('from F :',obj4.eleventh)
print('from F :',obj4.twelth)
print('from B :',obj4.forth)
print('from B :',obj4.third)