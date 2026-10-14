#方式一:位置传参
def user_info(name, age, address):
    print(f'我的名字{name}，今年{age}岁了，家里住在{address}')

# 调用函数
user_info('Tom', 23, '美国纽约')

#方式二:关键字传参
def user_info(name, age, address):
    print(f'我的名字{name}，今年{age}岁了，家里住在{address}')

# 调用函数（使用关键词参数）
user_info(name='Tom', age=23, address='美国纽约')

#方式三:函数定义时缺省参数（参数默认值）
def user_info(name, age, gender='男'):
    print(f'我的名字{name}，今年{age}岁了，我的性别为{gender}')


user_info('李林', 25)
user_info('振华', 28)
user_info('婉儿', 18, '女')


# 定义一个函数, 该函数需要传入三个参数
def fun1(name,age,address):
    print(f"姓名:{name},年龄:{age},地址:{address}")


# 如何调用呢?
# 位置传参方式: 要求调用函数的时候, 传递的参数顺序 要和 函数的形参的顺序保持一致
fun1("张三",20,"南京市")

# 关键词传参: 在传递参数的时候, 可以指定给谁传递  对顺序就没有要求
fun1(age=18,name="李四",address="北京市")

# 默认值传参: 指的是在定义这个函数的时候, 可以给某些参数赋一个默认值, 然后在调用该函数就可以不需要传递参数了
# 注意: 有默认值的形参 必须放置到整个参数列表的最后面
def fun2(name,address='南京市',age=18):
    print(f"姓名:{name},年龄:{age},地址:{address}")

# 调用操作: 如果不需要修改默认值, 那么在调用的时候也不需要传递, 如果需要修改 那么就正常传递即可
fun2(name="王五")
fun2(name="赵六",address="北京市")

#注意: 如果函数中某个参数没有默认值, 那么在调用的时候, 必须传递 否则会直接报错

#不定长元组(位置)参数---可变参数
def user_info(*args):
    # print(args)  # 元组类型数据，对传递参数有顺序要求
    print(f'我的名字{args[0]}，今年{args[1]}岁了，住在{args[2]}')

# 调用函数，传递参数    将这些参数打包成元组
user_info('Tom', 23, '美国纽约')

#不定长字典(关键字)参数 ---- 可变的关键字参数
def user_info(**kwargs):
    # print(kwargs)  # 字典类型数据，对传递参数没有顺序要求，格式要求key = value值
    print(f'我的名字{kwargs["name"]}，今年{kwargs["age"]}岁了，住在{kwargs["address"]}')

# 调用函数，传递参数    ----将参数打包成一个字典
user_info(name='Tom', address='美国纽约', age=23)



# 演示不定长参数:
# 不定长元组（位置）参数
# 定义函数:
def fun1(*args):  # 这种 一个 * 不定长参数, 背后 是一个容器(序列) --> 元组
    # 获取每一个参数的内容
    print(type(args))
    for e in args:
        print(f"参数:{e}")


# 调用函数
fun1("张三", "李四", "王五", "赵六", "田七")


# 不定长字典(关键词)参数
def fun2(**kwargs):  # 这种 一个 ** 不定长参数, 背后 是一个容器(序列) --> 字典
    print(type(kwargs))
    # 遍历参数
    for key in kwargs:
        print(f"参数的key:{key}, 对应的值为:{kwargs[key]}")

# 调用函数: 必须使用关键词传参
fun2(name="张三", age=18, address="南京市")  # 在调用的时候, 创建了一个字典, 将 kv数据放置到了字典中

#案例：Python中数据的传递案例
def func(*args, **kwargs):
    print(args)
    print(kwargs)
# 定义一个元组（也可以是列表）
tuple1 = (10, 20, 30)
# 定义一个字典
dict1 = {'first': 40, 'second': 50, 'third': 60}
# 需求：把元组传递给*args参数，字典传递给**kwargs
# ① 如果想把元组传递给*args，必须在tuple1的前面加一个*号
# ② 如果想把字典传递给**kwargs，必须在dict1的前面加两个**号
func(*tuple1, **dict1)      #不能把这个 元组tuple1和字典dict1直接扔到实参的位置中,他不会认
#下边的这个做法，会产生将tuple1打包成一个元组((10,20,30),)
#下边的这个做法，会产生将tuple1=(10, 20, 30)打包成一个元组((10,20,30),)
func(tuple1)
#以下会将dict1 = {'first': 40, 'second': 50, 'third': 60}，打包成一个元组({'first': 40, 'second': 50, 'third': 60})
func(dict1)

#通用位置参数和关键字参数传参，将10，20，30打包成元组(10,20,30)赋值给args
#将first=40，second=50，third=60打包成字典{'first': 40, 'second': 50, 'third': 60}赋值给kwargs
func(10,20,30,first=40,second=50,third=60)


