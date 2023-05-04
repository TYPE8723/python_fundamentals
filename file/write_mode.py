str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
str_dict = ["geeks","for","geeks"]
with open('write_file.txt','a') as file_write:
    print("Write status :",file_write.writable())
    # count=file_write.write(str)# writes the string and returns the number of characters written
    # print(count)
    file_write.writelines(str_dict)#The write() method accepts a string as an argument and writes this string to the text file. Whereas, the writelines() method accepts an iterable i.e. a string or the list of strings as an argument and writes these strings to the text file