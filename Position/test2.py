# run this file to measure how long time test1.py takes

import test1
import datetime

def service_func():
    print 'service func'

if __name__ == '__main__':
    # service.py executed as script
    # do something
    # service_func()
    start = datetime.datetime.now()  #starta klocka
    test1.start_eko()
    stop = datetime.datetime.now()  #starta klocka
    timeout = stop - start #skillnad klockslag
    print "Timeout tid:",timeout.total_seconds()

