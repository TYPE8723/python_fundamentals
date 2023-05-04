# Sample Input 0
# 1
# 1
# 1
# 2
# Sample Output 0
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# Print an array of the elements that do not sum to n=2
# testcase2
# Sample Input 1
# 2
# 2
# 2
# 2
# Sample Output 1
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
# Print an array of the elements that do not sum to n=2

x,y,z,n=int(input()),int(input()),int(input()),int(input())
l1=[[i,j,k]for i in range(x+1)for j in range(y+1)for k in range(z+1)if i+j+k!=n]
print(l1)

#execution starts from left to right
#first i loop get executed and goes to  nested loop  that is j.
#the j loop get executed and goes to nested loop that is k
#since k loop is the last loop k executes the loop and go back to j
#j increments to next number and goes to nested loop k
#k compelets its execution and to move j.
#similary j completes loop and moves to i
