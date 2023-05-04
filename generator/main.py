def my_generator(val):
    countr=0
    for i in range(1,100):
        if val>=i:
            yield(i)
            countr+=1
for v in my_generator(5):
    print(v)

