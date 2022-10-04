#!/usr/bin/env python3
import threading, time, sys
sys.path.append("/media/dat/DISK/Dev/Automation/Shopee")
import shopee


def func1(x):
    print(f"-->Start func 1: sleep {x}")
    time.sleep(x)
    print(f"End func 1")

def func2(x):
    print(f"-->Start func 2: sleep {x}")
    time.sleep(x)
    print(f"End func 2")
    
th1 = threading.Thread(target=func1, args=(3,)) 
th1.start()
# th1.join() # don't do anything until thread 1 done -> func1 ends 1st

th2 = threading.Thread(target=func2, args=(1,))
th2.start()

# th1.join()
# th2.join()

print("\nNumber of threads: "+ str(threading.activeCount()))

# th2 = threading.Thread(target=open_shopee_coin)
# th2.start()
# th1 = threading.Thread(target=open_gmail)
# th1.start()
# th2 = threading.Thread(target=open_invest)
# th2.start()
