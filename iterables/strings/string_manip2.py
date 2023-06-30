str1 = ",,,,,,,,.##$ #@f dfdP.....Toyota..#..3247234"
left_strip = str1.lstrip(", .#$@df")#blank space removes spacefrom str1
print(left_strip)
right_split = str1.rstrip(".4327")
print(right_split)
print("swaping case :",right_split.swapcase())
print("upper :",right_split.upper())
print("lower :",right_split.lower())
str1_blank = ""
if not str1_blank:
    print("str1_blank is empty")
str1_blank = " hello"
if not str1_blank:
    print("str1_blank is empty")
else:
    print("str1_blank is not empty")
str1 = "blue fox jumped over."
print("right align :",str1.rjust(95))
print("left aligned :",str1.ljust(95))
print('check wether left_strip is all num :',left_strip.isalnum())
print('check wether str1 is all num :',str1.isalnum())
print('check wether custom string is num :',"AFSDFsafSDCDS".isalnum())
print('check wether custom string is printable :',"AFSDFsafSDCDS".isprintable())
print('check wether "\ n "string is printable :',"\n".isprintable())
print('check wether a string is full of space :',"   ".isspace())
print('check wether a string is full of space :',"   .sad".isspace())
print('check wether a str starts with blue :',str1.startswith('blue'))
print('check wether a "i love you" starts with blue,red :',"i love you".startswith(('blue','red')))
print('check wether a "i love you" starts with blue,red,i :',"i love you".startswith(('blue','red','i')))
print('check wether a "i love you" has "love"from 4th position :',"i love you".startswith(('blue','red','love'),2,-1))

