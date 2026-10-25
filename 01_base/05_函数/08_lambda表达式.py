'''
变量 = lambda 函数参数:表达式（函数代码 + return返回值）
# 调用变量
变量()
'''
'''
演示lambda表达式用法
'''

'''
变量 = lambda 函数参数:表达式（函数代码 + return返回值）
# 调用变量
变量()
说明:
变量就是函数的地址，将来可以通过变量名调用函数
'''
def func(str):
    return 'hello '+ str

# fn是lambda表达式的地址，也就是函数地址
fn = lambda str: 'hello '+ str
# 打印函数调用结果
print(fn('zack'))

#编写一个函数求两个数的和
def fn1(num1, num2):
    return num1 + num2
print(fn1(10, 20))
#使用lambda表达式进行简化
'''
带参数的lambda表达式
计算num1和num2的加法结果
'''
# fn是lambda表达式的地址，也就是函数地址
fn = lambda num1,num2:num1+num2
# 函数调用
print(fn(1,2))

#带默认参数的lambda表达式
# 有参数 参数带有默认值:
def fn2(num1, num2=30):
    return num1 + num2
print(fn2)
print(fn2(10))

# lambda 简化
'''
带默认值的参数
'''
fn2 = lambda num1, num2=20: num1-num2
# 打印函数的地址，也就是lambda表达式在堆区的地址
print(fn2)
# num2默认传递20
print(fn2(100))

# 带if判断（三目运算符）的lambda表达式
# 带 if判断（三目运算符）的lambda表达式
# 普通函数
def fn3(name: str):
    a = 0
    if name == "张三":
        a = 1
    else:
        a = 0
    return a

# 普通函数
def fn4(name: str):
    return 1 if name == "张三" else 0

print(fn4("李四"))

# 基于lambda方案实现
lambda name: 1 if name == '张三' else 0


# 列表数据+字典数据排序（重点）
'''
lambda表达式经常配合泛型编程使用
不受限于数据结构
也不受限于实际参数
封装和调用解耦合
'''
#知识点：列表.sort(key=排序的key)
print("------------------------------------")
# 在一个列表中, 放置了三个元素, 每一个元素又是一个字典
students = [
    {'name': 'Tom', 'age': 20},
    {'name': 'Rose', 'age': 19},
    {'name': 'Jack', 'age': 22}
]
print(students)
# 按name值升序排列
#按照字典中的age来进行排序，默认是升序
fn = students.sort(key=lambda x: x['age'])
# 按name值降序排列
#按照字典中的age来进行排序
fn = students.sort(key=lambda x: x['age'],reverse=True)

