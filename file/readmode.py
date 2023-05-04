# Steps for reading a text file in Python
# To read a text file in Python, you follow these steps:

# First, open a text file for reading by using the open() function.
# Second, read text from the text file using the file read(), readline(), or readlines() method of the file object.

with open("readsrc.txt",'r') as read_txt:
    #COMMENT EACH TO GET THE RESULT
    # stuff = read_txt.read()# READ AS STRING|as whole text
    # stuff = read_txt.readlines()# Read as list|returns a listhint	Optional. If the number of bytes returned exceed the hint number, no more lines will be returned. Default value is  -1, which means all lines will be returned.
    # print(stuff)
    print(read_txt.readline()) # reads line by line#read_txt.readline(2)->reads 2nd position
    print(read_txt.seekable()) # reads line by line#read_txt.readline(2)->reads 2nd position
    # print(read_txt.readline())# reads line by line
    # print(read_txt.readline())# reads line by line
    # index position from the beginning
    read_txt.seek(20)#moves cursor to the given position
    # prints current position
    print(read_txt.tell())
    print(read_txt.readline())
    print("readbility status :",read_txt.readable())
