# https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
from itertools import groupby
text="1222311"

l = [(len(list(c)),int(k)) for k,c in groupby(text)]
print(*l)