
# a function that returns True if letter is vowel
letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s']
def filt(val):
    vowels = ['a','e','i','o','u']
    return True if val in vowels else False
op = list(filter(filt,letters))
print(op)