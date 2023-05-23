def kwargss(func):
    def funargs(*args,**kwargs):
        func(*args,**kwargs)
        print("****FROM DCORATIORSE***",kwargs)
        print(args)
        return ""
    return funargs

@kwargss
def fun1(args,**kwargs):
    print("from fun :",kwargs)
    return ""

fun1(["HELLO ALEN","sd"],x=1,y=2,name="ALEN")
