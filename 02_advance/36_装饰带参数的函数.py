'''
演示装饰带参数的函数
'''

'''
装饰有参数无返回值函数
'''
def print_info(func):
    def inner(a,b):
        print(f'正在努力计算中。。。。')
        func(a,b)
    return inner

#get_sum = print_info(get_sum)
@print_info
def get_sum(x,y):
    z = x+y
    print(f'两数之和为:{z}')

get_sum(1,2)



