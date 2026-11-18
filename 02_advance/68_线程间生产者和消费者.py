import threading
import time

#创建一个条件变量对象
cond = threading.Condition()
# 用列表模拟队列
task_list = []
#队列最大大小
task_max_len = 5
#生产者
def process():
    product_id = 0
    while True:
        with cond:
            #队列满了
            if len(task_list) >= task_max_len:
                print('仓库满了，生产者等待！')
                cond.wait()
            #走到这队列不满
            product_id = product_id + 1
            task_list.append(product_id)
            print(f'生产者生产产品，{product_id}')
            #如果队列大小为1，这说明仓库由空到1，激活消费者   ，不用每次都唤醒
            if len(task_list) == 1:
                #唤醒消费者，
                cond.notify_all()
        time.sleep(0.5)

#消费者任务
def consumer():
    while True:
        with cond:
            #队列为空则等待
            if len(task_list) == 0:
                print('仓库为空，消费者等待')
                cond.wait()
            #走到这说明队列不为空，则消费者消费
            #pop是从task_list 这个队列中取出货物，按照序号进行取
            product_id = task_list.pop(0)
            print(f'消费者消费商品：{product_id}')
            if len(task_list) == task_max_len - 1:
                #条件变量通知生产者
                cond.notify_all()
        time.sleep(0.5)

if __name__ == '__main__':
    process = threading.Thread(target=process)
    consumer = threading.Thread(target=consumer)
    process.start()
    consumer.start()

    process.join()
    consumer.join()



