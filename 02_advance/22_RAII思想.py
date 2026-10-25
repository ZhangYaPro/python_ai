'''
演示RAII思想的应用
'''

'''
RAII思想
就是在对象初始化的时候创建资源
在对象结束的时候回收资源
达到资源和对象绑定的效果，资源的回收和创建绑定给了对象的生命周期
'''
import threading


class MyLock:
    def __init__(self):
        self.lock = threading.Lock()

    def __enter__(self):
        print("加锁")
        self.lock.acquire()
        return self  # 可选

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("解锁")
        self.lock.release()
        # return False 表示异常继续抛出（默认行为）

if __name__ == '__main__':
#即使出现异常，也会自动解锁
    try:
        with MyLock() as lock:
            print("我要上厕所了")
            #即使出现了异常了，也会自动解锁
            raise ValueError('开会了')
            print('我上完厕所了')
    except Exception:
            print('捕获异常')

#如下操作会导致锁未被释放
try:
    #上锁
    print('加锁')
    threading.Lock().acquire()
    print('我正在上厕所')
    raise ValueError('开会了')
    print('我上完厕所了')
    print('解锁')
    threading.Lock().release()
except Exception:
    print('捕获异常')


