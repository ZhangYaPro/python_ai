#集合
#天生去重   无序
# 1- 如何定义集合
# 格式:
#       格式一:  变量名称 = {元素1,元素2,元素3......}
#       格式二:  变量名称 = set()   空集合
# 特性: 无序 + 去重
# 定义一个有内容的集合
name_set = {'小明','小红','小刚','小明','小刚','小丽'}

print(name_set) #  去重 和 无序  发现每次都是不一样的 所以是无序的
print(type(name_set))
# 定义 空集合
# set2 = {}  # 此种定义方法 并不是定义空集合, 而是空的字典
empty_set = set()
print(type(empty_set))

# 获取数据: 遍历的方式
# for 循环
for name in name_set:
    print(name)

#集合增的操作
#add()方法
name_set = {'小明','小红','小刚'}
name_set.add('小强')
print(name_set)

#集合的删操作
#remove() 方法：：删除集合中的指定数据，如果数据不存在则报错
name_set = {'小明','小红','小刚'}
name_set.remove('小红')
print(name_set)

#集合中的查操作
'''
 in ：判断某个元素是否在集合中，如果在，则返回True，否则返回False
 not in ：判断某个元素不在集合中，如果不在，则返回True，否则返回False'''
name_set = {'小明','小红','小刚'}
print('小明' in name_set)  # True
print('小丽' not in name_set)  # True

name_set = {'小明','小红','小刚'}
for name in name_set:
    print(name)

# 演示 集合的API
num_set = {3,4, True,'小明',False}
# 1- 添加数据的API: add
num_set.add("小红")
print(num_set)

# 2- 删除数据的API: remove  在删除的时候 如果在集合中没有该值 会直接报错
num_set.remove(False)

print(num_set)

# 3- 判断是否存在和不存在操作: in 和 not in
# 如果 小刚在集合中不存在, 请添加该元素
if '小刚' not in num_set:
    # 能进来, 说明 小刚 不在集合中
    num_set.add('小刚')

print(num_set)

"""
💡 题目：一个数组中除了两个数字只出现一次外，其他数字都出现两次。
       找出这两个只出现一次的数字。
输入: [4, 1, 2, 1, 2, 3, 5, 5]
输出: 3 和 4

思路：
1. 准备集合A和列表B，集合A用来存储出现的数字，集合B用来记录只出现过1次的数字
2. 将出现的数字和集合A判断，如果集合A中有数字，说明这个数字出现过，将数字从集合B
中删除。
如果A中没有这个数字，说明数字没出现过，将数字放入集合A和集合B
3. 最后循环结束，打印集合B，就是只出现一次的数字了
"""

num_list = [4, 1, 2, 1, 2, 3, 5, 5]
#集合A:用于存储出现过的数字
set_a = set()
#集合B：用于存储没有重复的数字
set_b = set()
for num in num_list:
    if num in set_a:
        set_a.add(num)
        set_b.add(num)
        continue
    set_b.remove(num)
print(set_b)