import asyncio

# 定义标准协程函数
async def hello_coroutine():
    print("协程内部代码被执行了")

# 调用协程函数：仅生成协程实例，无打印输出，仅生成一个协程的对象
coro = hello_coroutine()   #只会生成一个协程对象
print(type(coro))  # <class 'coroutine'>