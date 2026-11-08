'''
演示装饰带参数带返回值的函数
'''
def print_info(func):
    # 内层参数与原函数保持一致
    def inner(a,b):
        print(f'正在努力计算中...')
        res = func(a,b)
        print(f'计算成功！！！')
        return res
    return inner

@print_info
def get_sum(x,y):
    z = x + y
    return z

print(get_sum(1,2))