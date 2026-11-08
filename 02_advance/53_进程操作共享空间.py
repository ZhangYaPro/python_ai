'''
演示进程操作共享空间
'''
import multiprocessing
import time

def add_num(share_list,lock,num):
    '''
    将num放入列表share_list中
    :param share_list: 通过Manager()从共享空间中开辟的列表
    :param lock: 进程安全锁
    :param num: 任务数据放入列表中
    :return: None
    '''
    #加锁  同一时间仅有一个进程修改共享数据
    lock.acquire()
    try:
        #
        share_list.append(num)
    finally:
        #解锁
        lock.release()

if __name__ == '__main__':
    #创建管理器
    #manager 是为了实现两个进程之间的共享  ---
    manger = multiprocessing.Manager()
    #创建跨进程的共享列表  从共享空间中开辟一个列表
    share_list = manger.list()
    #创建进程锁
    lock = multiprocessing.Lock()
    #储存创建的子进程，将来主进程等待子进程执行完成
    p_list = []
    for i in range(5):
        #创建子进程
        p = multiprocessing.Process(target=add_num, args=(share_list,lock,i))
        #开启执行子进程
        p.start()
        # 将子进程添加到列表中
        p_list.append(p)
    #主进程等待所有子进程运行结束
    for p in p_list:
        p.join()

    print(f'最终共享列表:{share_list}')

