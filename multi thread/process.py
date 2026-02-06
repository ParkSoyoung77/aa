import os
import time
from multiprocessing import Process

def process_func1():
    print('연속적으로 진행할 어떤 작업은 여기에 ~')
    time.sleep(1)

def process_func2(number):
    result = number + 10
    process_func1()
    proc = os.getpid()
    print('number:{0}, result:{1} process id:{2}'.format(number, result, proc))

if __name__== '__main__':
    numbers = 1,2,3,4,5,6,7,8,9,10
    procs = []

    for index, number in enumerate(numbers):
        proc = Process(target=process_func2, args=(number,))
        procs.append(proc)
        proc.start()

    for p in procs:
        p.join()