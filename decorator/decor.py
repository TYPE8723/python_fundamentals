import time
def time_calculate(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        # time.sleep(2)
        stop = time.time()
        print(f" Processing time is :{stop-start}")
        return stop
    return wrapper

@time_calculate
def fact(n):
    fact=1
    for i  in range(1,n+1):
        fact = fact*i
    print(fact)

fact(5)