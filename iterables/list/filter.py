numbers = [1,2,3,4,5,6,7,8,9,10]
def check_eve(val):
    if val % 2 == 0:
        return True
    return False
fil = filter(check_eve,numbers)
print(list(fil))
    
        
