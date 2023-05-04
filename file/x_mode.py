# # "x" is only writeable. "x+" can write and read
#  if the file exists, raise FileExistsError. 
#  open for exclusive creation, failing if the file already exists
str="The sun set behind the mountains, casting a warm glow over the valley. The last rays of light illuminated the path ahead, beckoning him to follow."
try:
    with open("xmode.txt","x")as x_file:
        x_file.write(str)
except Exception as exe:
    print(exe)
