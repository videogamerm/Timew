import time
import os
def timewwait(n):
    time.sleep(n)
def timewkill(n):
    timewwait(n)
    exit("")
def gcc(filename):
    os.system("gcc "+ filename)
def ds(filename):
    # ./filename!!
    os.system("./" + filename)
