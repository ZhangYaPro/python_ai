import multiprocessing
import time


class MyProcess(multiprocessing.Process):    #进程类
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        # 进程启动后自动执行run方法
        print(f"自定义进程 {self.name} 启动 PID:{self.pid}")
        time.sleep(self.delay)
        print(f"自定义进程 {self.name} 结束")


if __name__ == '__main__':
    p = MyProcess("自定义进程C", 1.5)
    p.start()
    p.join()
    print("主进程结束")