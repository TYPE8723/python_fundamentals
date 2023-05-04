import threading
import time

def caseA():
    print("***CASE A TRIGGERED***")
    time.sleep(10)
    print("***CASE A slept***")

def caseB():
    print("#####CASE B TRIGGERED#####")
    time.sleep(5)
    print("#####CASE B slept#####")

t1 = threading.Thread(target=caseA)
t2 = threading.Thread(target=caseB)

#starting threads
t1.start()
t1.join()#waiting for thread completion # wait until thread 1 is completely executed
t2.start()

print ("process completed ,BYE!!!!")
t2.join()