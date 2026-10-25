'''
闭包累加案例：持续保留上次计算结果
'''
'''
思路：
1. 可以通过外部函数func返回内部函数
2. 内部函数调用的这个参数累加到闭包的自由变量中，内部函数返回累加后的结果
'''
def func():
    # 外层变量，常驻内存
    result = 0
    def inner_func(num):
        # 引用外层变量并修改
        nonlocal result
        result = result + num
        return result
    # 返回闭包
    return inner_func

# 绑定闭包函数
g = func()
print(g(1))  # 0+1=1
print(g(2))  # 1+2=3
print(g(3))  # 3+3=6
