import threading

from distributed import lock

lock = threading.Lock()
num = 0

def func():
    lock.acquire()
    print("第一次加锁")
    lock.acquire()
    #该代码导致死锁，因为对互斥锁重复加锁导致死锁
    print("同一线程二次加锁，不会阻塞")
    lock.release()
    lock.release()

#可重入锁
rlock = threading.RLock()
def func2():
    rlock.acquire()
    print("第一次加锁")
    rlock.acquire()
    #该代码导致死锁，因为对互斥锁重复加锁导致死锁
    print("同一线程二次加锁，不会阻塞")
    rlock.release()
    rlock.release()

t = threading.Thread(target=func2)
t.start()
t.join()