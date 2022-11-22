# multiprocessing - python module used for implementing parallel processing.

import multiprocessing

def print_square(num):
    print("Square: {}".format(num*num))

def print_cube(num):
    print("Cube: {}".format(num*num*num))


if __name__ =='__main__':
    p1 = multiprocessing.Process(target=print_square,args=(13,))
    p2 = multiprocessing.Process(target=print_cube,args=(13,))

    p1.start()

    p2.start()

    p1.join()

    p2.join()

    print("Done ...!!!")

