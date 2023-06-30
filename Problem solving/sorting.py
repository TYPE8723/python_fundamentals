#sorting without comparison.sorting using frequescy array -> https://www.hackerrank.com/challenges/one-month-preparation-kit-countingsort1/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-month-week-one
freq_arr = [0]*100
inp = [63,25,73,1,98,73,56,84,86]
for i in inp:
    freq_arr[i]=freq_arr[i]+1
print(freq_arr)
index=0
for i in freq_arr:
    if i!=0:
        print(i*str(index))
    index+=1
    