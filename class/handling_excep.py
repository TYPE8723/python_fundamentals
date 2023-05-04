x = int(input('enter a value :'))
y = int(input('enter a value to divide :'))
div = x/y
if y <= 0:
    print('hi')
    raise Exception("Sorry, no numbers below zero")
print('divident is  :'+str(div))
