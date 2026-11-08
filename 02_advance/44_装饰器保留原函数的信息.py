'''
演示装饰器保留原函数的信息
'''
import functools

def timer(func):
    # 保留原函数元信息
    @functools.wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner

@timer
def calc():
    """数值计算函数"""
    pass
# 当这个calc函数被装饰之后，打印他的名字是inner；如果不被装饰打印的是名字是calc
# 正常输出原函数信息  @functools.wraps(func) 保留原函数信息
print(calc.__name__)
print(calc.__doc__)

