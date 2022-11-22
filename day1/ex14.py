# using shared resource with multiprocessing
# lock is created for ensuring the shared resource is equally shared between competing processes
import multiprocessing

def withdraw(balance, lock):
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

def deposit(balance, lock):
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

if __name__ == '__main__':
    balance = multiprocessing.Value('i',100)

    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=withdraw,args=(balance,lock))
    p2 = multiprocessing.Process(target=deposit,args=(balance,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Balance = {}".format(balance.value))
