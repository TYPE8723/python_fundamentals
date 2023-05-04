import string
alphabet = list(string.ascii_lowercase)
alpha_dict = {key+1:value for key,value in enumerate(alphabet)}

print(alpha_dict)