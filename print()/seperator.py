from itertools import permutations
cmd = ['AC', 'AH', 'AK', 'CA', 'CH', 'CK', 'HA', 'HC', 'HK', 'KA', 'KC', 'KH']

print(*cmd,sep="\n")#*is used to unpack the list
print(*cmd,end="***")#*is used to unpack the list
print("JOINED WITH THE PREVIOUS PRINT")
