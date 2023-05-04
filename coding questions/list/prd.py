# Write a Python program to multiply all the items in a list
from numpy import prod
l1 =[1,2,-8]

print(prod(l1))

#function wise and array map
prd=1
def process(val):
    global prd
    prd *= val
    
    return prd
product = map(process,l1)

print(list(product)[-1])

#normal product using loop
prd1=1
product=1
for i in l1:
    product=i*product

print(product)