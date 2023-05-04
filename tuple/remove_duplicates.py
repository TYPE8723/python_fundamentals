#How to remove duplicate from list of tuples
list_of_tuples = [("C#", 1), ("C#", 1), ("C++", 3),("C++", 3), ("Python", 25), ("Rust", 30)]
print('initial tuple : ',list_of_tuples)
unique = tuple(set(list_of_tuples))
print('unique list : ',unique)