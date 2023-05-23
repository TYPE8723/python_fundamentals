# Closure:
# A closure is a function object that has access to variables in its enclosing lexical scope, even when the enclosing function has finished executing. In simpler terms, a closure allows a function to "remember" and access variables from its outer (enclosing) function even after that function has returned. The closure maintains a reference to the variables it needs, preventing them from being garbage-collected.

# Closures are created when you define a function inside another function and the inner function references variables from the outer function. The inner function can access and modify the variables of the outer function, encapsulating those variables within the closure.

# Closures are commonly used to create function factories or to create functions with "private" variables that are hidden from the global scope. They provide a way to achieve data encapsulation and can be used to implement various design patterns.

def outro():
    num = 1
    def odd():
        nonlocal num
        num +=2
        var = num
        return num
    return odd
result_odd = outro()

print(result_odd())
print(result_odd())
print(result_odd())


# Yes, it is possible to create a closure without using the nonlocal keyword. Instead of modifying variables from the outer function using nonlocal, you can use mutable objects like lists or dictionaries to achieve a similar effect. Here's an example:

# def counter(initial_value):
#     count = [initial_value]  # Store the count in a mutable object

#     def increment(amount=1):
#         count[0] += amount
#         return count[0]

#     return increment
