def my_generator(val):
    # countr=0
    for i in range(1,100):
        if val>=i:
            yield(i)
            # countr+=1
for v in my_generator(5):
    print(v)

#usage of NEXT()
def odev(lim):
    for i in range(lim):
        if i%2==0:
            yield i
generate = odev(10)
for i in generate:
    try:
        print(next(generate))
    except Exception as e:
        print("Program ended :",e)
        break
    
        
    