'''
闭包中被内层函数引用的外层变量，称为**自由变量**。
闭包会将自由变量保存在函数内置属性中，阻止垃圾回收。可通过内置属性查看：
'''
def outer():
    num = 100
    def inner():
        print(num)
    return inner

fn = outer()
# 查看自由变量名称
print(fn.__code__.co_freevars)
# 查看闭包保存的变量对象
print(fn.__closure__)
