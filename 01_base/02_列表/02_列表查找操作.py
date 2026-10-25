# 演示列表的API
name_list = ['小明', '小红', '小刚', '小丽', '小强', '小芳', '小亮', '小红']
# 查询相关方法:
# 1- index(): 查询指定数据所在位置的下标  如果不存在 直接报错
index = name_list.index("小丽")
print(index)  # 3

# 2- count(): 统计数据在当前列表中出现的次数
count = name_list.count("小红")
print(count)  # 2

# 3- in 和 not in 判断是否存在或不存在
bool = "小刚" in name_list
print(bool)
bool = "小刚" not in name_list
print(bool)

# 增加函数
# 1- append()  增加指定数据到列表中
# 如果 小宇 不在列表中, 请增加到列表中
if "小宇" not in name_list:
    # 能进来, 说明 小宇 不在, 如果不在 添加到列表中
    name_list.append("小宇")

print(name_list)

# 2- extend(): 将一个序列 追加到另一个序列中
# 2.1 先定义一个新的序列
name2_list = ['小浩', '小琪']

# 2.2 将新列表中数据 增加 到 原有列表中
name_list.extend(name2_list)

print(name_list)

# 3- insert() 在指定位置新增数据
name_list.insert(4, '小诺')

print(name_list)

# 删除操作
# 1- del 列表[索引]
del name_list[-1]

print(name_list)

# 2- pop() 删除指定下标的数据, 默认是删除最后一个 并且会返回删除的数据
element = name_list.pop()
print(element)
print(name_list)

element = name_list.pop(2)
print(element)
print(name_list)

# 3- remove() 移除列表中某个指定数据  如果不存在, 也不会报错 无效果
name_list.remove("小诺")
print(name_list)

# 修改操作
# 1-  修改某个索引的值
name_list[0] = '大明'
print(name_list)

# 2- reverse: 反转操作
name_list.reverse()

print(name_list)

# 3- 排序操作: reverse 设置 是否反转   True 反转(倒序)  False 不反转(正序)
num_list = [3, 7, 10, 56, 2, 9, 4, 5]
num_list.sort(reverse=True)
print(num_list)

#列表循环遍历
#第一种:while循环
star_list = ['西施', '王昭君', '杨玉环']
i = 0
while i < len(star_list):
    print(star_list[i])
    i += 1

#第二种:for循环
star_list = ['西施', '王昭君', '杨玉环']
for star in star_list:
    print(star)

#列表的嵌套
classes = ['第一个班级','第二个班级','第三个班级']

# 一班：['小明', '小红']
# 二班：['小刚', '小丽']
# 三班：['小强', '小芳']
#
# 把班级和学员信息合并在一起，组成一个嵌套列表
students = [['小明', '小红'],['小刚', '小丽'],['小强', '小芳']]

students = ['x','y','z']
students[0] == ['小明', '小红']
students[0][1]


# 演示 列表嵌套
# 说明: 容器内部嵌套容器方式
# 需求: 有 三个班级, 分别为 前端1班 前端2班  后端1班, 每个班级分别有5位学生
# 定义 班级列表
front1_class = ['小明','小红','小刚','小丽','小强']
front2_class = ['小芳','小亮','小宇','小浩','小琪']
back1_class = ['小诺','小泽','小琳','小航','小彤']

# 定义 学校列表, 学校列表中有三个班级
school_list = [front1_class,front2_class,back1_class]

# 以上内容 如果直接使用列表嵌套写法
school_list = [
    ['小明','小红','小刚','小丽','小强'],
    ['小芳','小亮','小宇','小浩','小琪'],
    ['小诺','小泽','小琳','小航','小彤']
]

# 如何 获取里面的数据呢?  比如 我想获取到 小浩
front2_class = school_list[1]
name = front2_class[3]
print(name)

# 可以简写
name = school_list[1][3]
print(name)

# 如何遍历打印每一个元素
for classes in school_list:
    for name in classes:
        print(name)
    print("-----------")