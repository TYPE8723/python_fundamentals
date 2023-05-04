# In file operations, t mode in the file opening mode string represents the text mode. It is used to open a file in a text mode, where the file is read as a sequence of Unicode strings, instead of bytes. The t mode is used in conjunction with the r, w, a, x, + modes.
# For example, opening a file in text mode for reading:
# with open('example.txt', 'rt') as file:
#     # Perform operations on the file

with open("readsrc.txt",'rt') as read_txt:
   print(read_txt.readable())
   print(read_txt.readlines(2))

with open('wt_mode.txt', 'wt') as file:
    file.write('This is an example of writing text to a file.')
