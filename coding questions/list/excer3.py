#clone  or copy list


L1 = ['abc', 'xyz', 'aba', '1221']
L2 = L1
del L2[2]
print(L1,L2)
L3=L1[:]
print(L3)
del L3[1]
print(L3)
print(L2)
print(L1)