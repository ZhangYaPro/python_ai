import asyncio

async def sleep_demo():
    print('开始异步等待2秒模拟IO阻塞')
    #异步休眠，替代time.sleep(),在异步函数中使用同步阻塞会导致卡死线程内
    await asyncio.sleep(2)
    print('2秒后IO等待结束，恢复写成执行')

if __name__ == '__main__':
    #将协程对象扔给run这个函数，相当于把这个协程对象扔到了事件队列中，循环在事件队列中去取出协程对象去执行
    asyncio.run(sleep_demo())
