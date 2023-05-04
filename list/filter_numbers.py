# the lambda function returns True for even numbers
numbers = [1, 2, 3, 4, 5, 6, 7]
decision = lambda x: True if x % 2 == 0 else False
op = list(filter(decision,numbers))
print(op)
