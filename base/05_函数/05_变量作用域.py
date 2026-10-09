# 演示: 全局和局部变量:
#  全局变量: 指的是定义在函数外部的变量称为全局变量
#  局部变量: 指的是定义在函数内部的变量称为局部变量
#  全局变量的作用范围: 是整个全局的范围内, 一旦定义后, 在当前这个文件的任意位置均可以使用该变量
#  局部变量的作用范围: 仅在当前这个函数的内部, 一旦出了这个函数, 该变量就相当于不存在

# 定义一个全局变量:
a = 100

# 定义一个函数
def fun1():
    # 定义一个局部变量:
    b = 200
    # 在函数内部使用全局变量
    print(f"函数内--输出a的值为:{a}")
    print(f"函数内--输出b的值为:{b}")


# 调用函数
fun1()

# 在函数外部使用全局变量
print(f"函数外输出a的值:{a}")
# print(f"函数外输出a的值:{b}")

#全局变量：在整个程序范围内都可以直接使用
str1 = 'hello'
# 定义一个函数
def func():
    # 在函数内部调用全局变量str1
    print(f'在局部作用域中调用str1变量：{str1}')

# 直接调用全局变量str1
print(f'在全局作用域中调用str1变量：{str1}')
# 调用func函数
func()
#局部变量：在函数的调用过程中，开始定义，函数运行过程中生效，函数执行完毕后，销毁
num = 20
# 定义一个函数
def func():
    # 在函数内部定义一个局部变量
    num = 10
    print(f'在局部作用域中调用num局部变量：{num}')

# 调用func函数
func()
# 在全局作用域中调用num局部变量
print(f'在全局作用域中调用num局部变量：{num}')



#global关键字的应用场景
'''
在Python中有两种类型的变量
1. 可变类型 list,dict,set,自定义的类型 ，尽管数据相同，但是占用不同的内存空间
2. 不可变类型 int, bool, str, double, tuple,相同的数据在内存中只存储1份数据
a = 1
b = 1
可以理解为a和b存储的都是1的地址
当a = 2 的时候，a指向的就是2的地址
'''
a = 1
b = 1
a = 2

list_a = [1,2,3]
list_b = [1,2,3]
list_a.append(4)
print(list_a)
print(list_b)

'''
因为Python中赋值和定义具有二义性
Python不同于C++， 
C++语法
int a = 100;  a = 200;
Python中
定义和赋值弄到一起
a = 100
a = 200
如果a = 200在函数内， a = 100在函数外
两个a 不是同一个a， 函数内的a = 200会被认为定义了一个新的变量a
'''

# 定义全局变量num = 10
num = 10
# 定义一个函数func
def func():
    # 尝试在函数内部修改全局变量,但是不会修改，只会重新定义一个num
    num = 20
    print(f"函数内num:{num}, id(num): {id(num)}")

# 调用函数func
func()
# 尝试访问全局变量num
print(f"函数外num:{num}, id(num): {id(num)}")
print('*'*20)

#使用global关键字,来在函数中修改全局变量
# 定义全局变量num = 10
num = 10
# 定义一个函数func
def func():
    # 尝试在局部作用域中修改全局变量
    global num
    num = 20

# 调用函数func
func()
# 尝试访问全局变量num
print(num)


#可变数据类型, 不需要添加global
# 结论: 如果变量的数据类型是可变的, 不需要添加global 就可以 对 全局变量进行修改

# 1- 定义一个全局变量: 类型为 字典
person = {"name":"张三","age":18}

# 2- 定义一个函数
def fun1():
    # 向字典中添加一个属性:
    person['address'] = "南京市"

    print(f"函数内打印全局变量:{person}")
    #print("修改全局变量的内容")


# 3- 调用函数
fun1()

# 4- 在全局范围内 打印全局变量
print(person)
'''
如果函数内修改的是可变对象，不需要加global,(dict,set,list,自定义类型对象)
因为不可变对象有很多种修改方式，比如字典的插入，比如列表append, remove,都可以修改，
不会被当成变量定义，所以就不用写global了

如果修改的是不可变的变量，需要加global,(字符串,元组,数字,布尔类型)
因为不可变类型的变量做修改，只能通过赋值，而赋值会产生二义性
python中=（赋值操作），有两层意思，一个是定义变量，还有一个是修改变量
在函数内部，局部作用域使用=，优先理解为定义变量

内存原理:
不可变对象，数据在内存中保留1份
可变对象，数据在内存中可以相同，可以是不同地址
'''

'''
局部作用域和全局作用域
'''
'''
局部作用域: 函数内部作用域就是局部作用域
全局作用域: 在函数外部的作用域就是全局作用域
局部变量: 在函数内部定义的变量就是局部变量，可见范围只在自己定义的作用域内，
在哪个函数内定义，就在哪个函数内可见，不可被外部的全局作用域使用
全局变量: 在函数外部定义的变量就是全局变量，可以被程序的所有部分使用
'''
# 全局变量
num1 = 2000
def hello():
    # 局部变量
    num2 = 300
    print('hello world')
# 全局变量
num3 = 400
def sum(num1,num2):
    # num1和num2都是局部变量，num4
    num4 = num1 + num2
    return num4

# 全局变量
str1 = 'hello'
def func():
    # 局部变量
    str2 = 'heima'
    print(f'在局部作用域内使用全局变量str1: {str1}')
    print(f'在局部作用域内使用局部变量str2: {str2}')

func()
# 在全局作用域内无法使用局部变量
#print(f'在全局作用域内使用局部变量str2: {str2}')

# 如果局部变量和全局变量同名了，就会出现定义局部变量和全局变量冲突的问题
# 如果想要在函数内修改外部局部变量，用global声明
# 全局变量
name = 'Lisi'
def change_name():
    # 局部变量
    name = 'zs'
    print(f'局部变量name: {name}')
change_name()
print(f'全局变量name: {name}')

# 使用global关键字
def change_name2():
    # 声明全局变量
    global name
    # 修改全局变量，将lisi改为zs
    name = 'zs'
    print(f'函数内name: {name}')
change_name2()
print(f'全局变量name: {name}')

# 全局变量
name = 'Lisi'
# 使用形参name
def change_name3(name):
    # name是形参，局部变量
    # 修改全局变量，将lisi改为zs
    name = 'zs'
    print(f'函数内name: {name}')
# name 为实参，为全局变量
change_name3(name)
print(f'全局变量name: {name}')

'''
如果函数内修改的是可变对象，不需要加global,(dict,set,list,自定义类型对象)
因为可变对象有很多种修改方式，比如字典的插入，比如列表append, remove,都可以修改，
不会被当成变量定义，所以就不用写global了

如果修改的是不可变的变量，需要加global,(字符串,元组,数字,布尔类型)
因为不可变类型的变量做修改，只能通过赋值，而赋值会产生二义性
python中=（赋值操作），有两层意思，一个是定义变量，还有一个是修改变量
在函数内部，局部作用域使用=，优先理解为定义变量

内存原理:
不可变对象，数据在内存中保留1份
可变对象，数据在内存中可以相同，可以是不同地址
'''
# 这是可变类型的全局变量
person = {'name':'zs','age':18}
print(f'全局person地址: {id(person)}')
def func1():
    # = 被当作定义，所以内部person是新定义的局部变量
    person = {'name':'zs','age':18}
    print(f'函数内person地址: {id(person)}')

#func1()

def func2():
    person['address'] = 'beijing'
    print(f'函数内person地址: {id(person)}')
func2()
