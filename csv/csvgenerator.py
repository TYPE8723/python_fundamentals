import csv
import random as rdm
header=['name','place','car','cost in lk']
name = ['alen','jhon','Vinod','Arun','evel']
place = ['USA','CANDA','UK','INDIA','PROTUGAL']
car = ['Skoda','benz','maruti','BMW','AUDI','COOPER']
cost = [5,7,2,9,3,8,7]

try:
    with open("pandas/pandas_sample.csv","w") as csv_writer:#generates csv in panda folder
        write = csv.writer(csv_writer)
        write.writerow(header)
        for i in range(10):
            write.writerow([rdm.choice(name),rdm.choice(place),rdm.choice(car),rdm.choice(cost)])
except Exception as e:
    print(e)

