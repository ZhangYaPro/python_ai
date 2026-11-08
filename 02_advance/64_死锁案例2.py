'''
演示死锁场景
'''
'''
对一个互斥锁重复加锁
'''
import threading
lock = threading.Lock()
num = 0

def add_():
    lock.acquire()
    global num
    num += 1
    lock.release()

# 嵌套加锁
def add():
    print(f'当前线程: {threading.current_thread().name} 执行任务add')
    lock.acquire()
    print(f'当前线程: {threading.current_thread().name}, 加锁成功!')
    global num
    num += 1
    add_()   #嵌套一个函数，函数中也实现了加锁和解锁功能
    print(f'当前线程: {threading.current_thread().name}, 线程结束')
    lock.release()

if __name__ == '__main__':
    threading.Thread(target=add).start()
    threading.Thread(target=add).start()