import threading

num = 0
lock = threading.Lock()  # 创建互斥锁

def add():
    global num
    for _ in range(100000):
        # 自动加锁，代码块结束自动释放
        with lock:        #  等价于  lock.acquire
            num += 1      #         num += 1
                          #         lock.release
if __name__ == "__main__":
    t1 = threading.Thread(target=add)
    t2 = threading.Thread(target=add)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("正确结果：", num) # 固定输出200000