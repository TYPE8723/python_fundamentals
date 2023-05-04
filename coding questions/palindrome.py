# n=1111
# normal = list(str(n))
# reverse = normal[::-1]
# if normal == reverse:
#     print("paindrome")
# else:
#     print("not palindrome")

#recursive method
# def is_palindrome(s):
#     for i in range(len(s) // 2):
#         if s[i] != s[-i - 1]:
#             return False
#     return True
string="racecar"
def palin(val):
    flag=False
    for i in range(1,len(val)+1):#to correct the zero negative index issue
        # print (i-1,'==',val[-i])
        # print(val[i-1],"==",val[-i])
        if val[i-1] == val[-i]:
            flag=True
            #print("palindrome")
        else:
            print("not palindrome")
            break
    if flag:
        print("palindrome")
palin(string)