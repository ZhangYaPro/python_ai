'''
#导入模块
import my_math
#使用my_math包的my_add()函数
print(my_math.my_add(1, 2))
'''

'''
#给导入的模块起别名
import my_math as mt
print(mt.my_add(1, 2))
'''

#导出my_math中的所有的函数和变量
from my_math import *
print(my_add(1, 2))
#到处my_math中的my_add()函数
from my_math import my_add
print(my_add(1, 2))


