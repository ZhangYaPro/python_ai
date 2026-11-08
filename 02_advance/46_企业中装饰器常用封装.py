import time
import functools

def cost_time(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"函数{func.__name__}执行耗时：{end-start:.4f}秒")
        return result
    return inner

@cost_time
def heavy_task():
    s = 0
    for i in range(1000000):
        s += i
    return s

heavy_task()

import functools

def catch_error(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"函数执行异常：{e}")
            return None
    return inner

@catch_error
def div(a, b):
    return a / b

print(div(10, 0))

#通用类封装装饰器
import functools

class LogDecorator:
    def __init__(self, func):
        self.func = func
        #这个参数表示的是  把func里边的函数传给self里的func属性
        functools.update_wrapper(self, func)  # 正确保留函数元信息

    def __call__(self, *args, **kwargs):
        print("类装饰器：函数开始执行")
        result = self.func(*args, **kwargs)
        print("类装饰器：函数执行结束")
        return result

@LogDecorator
def test():
    print("业务代码运行")
test(3,5)      #test 相当于类对象


#练习题
#带参数的通用日志装饰器
import functools

# 带参数通用日志装饰器
def log_action(action_type):
    # 第二层：接收被装饰函数
    def decorator(func):
        @functools.wraps(func)
        # 第三层：通用执行逻辑
        def inner(*args, **kwargs):
            print(f"正在执行【{action_type}】数据操作")
            # 执行原函数并接收返回值
            ret = func(*args, **kwargs)
            # 返还原函数结果
            return ret
        return inner
    return decorator

# 测试1：数据查询功能
@log_action("查询")
def query_data(table_name):
    print(f"正在读取数据表：{table_name}")
    return "数据读取完成"

# 测试2：数据录入功能
@log_action("录入")
def insert_data(table_name, count):
    print(f"向{table_name}插入{count}条记录")
    return "录入完成"

# 测试3：数据移除功能
@log_action("移除")
def remove_data(row_id):
    print(f"删除行号：{row_id}的数据")
    return "删除完成"

# 调用测试
print(query_data("sales_data"))
print("-"*25)
print(insert_data("user_info", 35))
print("-"*25)
print(remove_data(608))
