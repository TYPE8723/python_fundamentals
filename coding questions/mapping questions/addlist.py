#Write a Python program to add three given lists using Python map and lambda.    nm

nums1 = [1, 2, 3] 
nums2 = [4, 5, 6] 
nums3 = [7, 8, 9] 
process = lambda x,y,z:x+y+z
area = map(process,nums1,nums2,nums3)
print(list(area))