from concurrent.futures import ThreadPoolExecutor
import time

def calc(x):
    time.sleep(1)
    return x * x

if __name__ == "__main__":
    data = [1,2,3,4,5]
    with ThreadPoolExecutor(3) as pool:
        # 自动分配线程，结果顺序和输入一致
        #ThreadPoolExecutor.map() 返回的是生成器对象，
        #进程中multiprocessing.Pool.map()  返回的是列表
        res = pool.map(calc, data)
        print(res)
        #res是一个生成器对象
        #通过list()来让这个res呈现出结果，放到一个列表中
        print(list(res))