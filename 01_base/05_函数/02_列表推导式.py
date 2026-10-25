'''
变量名 = [表达式 for 变量 in 列表]
变量名 = [表达式 for 变量 in 列表 if 条件]
变量名 = [表达式 for 变量 in 列表 for 变量 in 列表]
'''

#生成0-9的列表
new_list = [i for i in range(10)]
print (new_list)

#获取0-9之间的偶数序列构成列表
print([i for i in range(10) if i%2==0])

'''
座位布局：
第0列  第1列  第2列  第3列
行0: (0,0)  (0,1)  (0,2)  (0,3)
行1: (1,0)  (1,1)  (1,2)  (1,3)
行2: (2,0)  (2,1)  (2,2)  (2,3)
'''
#方法一:for循环嵌套
seats = []

# 外层循环：遍历每一行
for row in range(3):
    # 内层循环：遍历每一列
    for col in range(4):
        seat = (row, col)
        seats.append(seat)

print(seats)

#列表推导式
seat = [(row,col) for row in range(3) for col in range(4)]
print(seat)

# 推导式案例: 案例一：使用列表推导式生成平方数集合
# 例如, 用户输入10, 表示要生成 1~10的每一个数字的2平方的集合
# 1- 让用户输入一个正整数
n = int(input("请输入一个正整数:"))

# 2- 遍历 从 1 ~ N
# 2.1 初始化一个空列表
my_list7 = []
for j in range(1,n+1):
    # 2.2 计算 2的平方 将结果写入列表
    my_list7.append(j ** 2)

print(my_list7)

# 推导式 如何解决
#集合推导式
#变量名称 = {表达式 for 变量 in 序列}
my_list8 = [ j ** 2 for j in range(1,n+1)]
print(my_list8)






