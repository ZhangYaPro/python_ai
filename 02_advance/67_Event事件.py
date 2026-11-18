import threading
import time
#  获取事件
event = threading.Event()

def wait_task():
    print('子线程等待信号...')
    #接受Event事件
    event.wait()
    print('收到信号，并开始执行任务！')

def send_task():
    time.sleep(3)
    print('发送通知信号')
    #发送Event事件
    event.set()

if __name__ == '__main__':
    t1 = threading.Thread(target=wait_task)
    t2 = threading.Thread(target=send_task)
    t1.start()
    t2.start()
    t1.join()
    t2.join()