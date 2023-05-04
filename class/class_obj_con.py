class sample:
    sum_val,mult_val = 0,2
    a=10
    b=20
    def __init__(self,first_val):
        self.first_val = 5
        print('sum is :',(first_val+self.first_val))
        pass
    def sum(self,a1):
        sum_val = obj1.a+a1
        print(obj1.a,'+',a1,'=',sum_val)
        pass
        
    def mult(self,a2):
        self.a2 = 5
        print('multval : ',obj1.mult_val)
        obj1.mult_val = obj1.b*a2+self.a2
        print(obj1.b,'*',a2,'+',self.a2,'=',obj1.mult_val)
        pass

first_val = int(input('enter the first val :'))
obj1 = sample(first_val)
obj1.sum(a1=first_val)
obj1.mult(a2=0)
print(obj1.mult_val)