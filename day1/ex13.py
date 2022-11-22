# create pool of processes

import multiprocessing
import os

def square(num):
    print("worker process id for {}:{}".format(num,os.getpid()))
    return (num*num)

if __name__ == "__main__":
    mylist = [1,2,3,4]

    p = multiprocessing.Pool()

    result = p.map(square,mylist)

    p.close()

    print(result)
