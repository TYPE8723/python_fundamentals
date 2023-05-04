#How to Sort List Of Tuples By Second Element
lang_listtuple = [('C#',1), ('Go',7), ('Basic',8), ('Python',60)]
  
print('original list of tuples =\n',lang_listtuple)

second = lambda x: x[1]

lang_listtuple.sort(key = second)
print(lang_listtuple)