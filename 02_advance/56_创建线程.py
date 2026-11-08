'''
演示如何创建线程
'''

import threading
import time

def task(name, delay):
    """线程执行函数"""
    print(f"线程 {name} 启动，休眠 {delay}s")
    time.sleep(delay)
    print(f"线程 {name} 执行完毕")

if __name__ == "__main__":
    # 创建线程对象 target=执行函数 args=参数元组
    t1 = threading.Thread(target=task, args=("A", 2))
    t2 = threading.Thread(target=task, args=("B", 1))

    # 启动线程，调用函数
    t1.start()
    t2.start()

    # join()：主线程阻塞，等待子线程执行完成再往下走
    t1.join()
    t2.join()
    print("所有子线程执行完成，主线程退出")