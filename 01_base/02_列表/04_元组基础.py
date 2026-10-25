# 1- 如何定义元组
# 格式:
#   变量名称 = (元素1,元素2,元素3......)
#   变量名称 = (元素1,) : 如果元组中只有一个元素, 必须在后面添加一个逗号 否则编译器会自动转换为 数据的本身类型, 而不是元组类型
user_tuple = ('小明','小红','小刚',20,30,40,True,False)
print(user_tuple)
print(type(user_tuple))

tuple1 = ('小明',)
print(tuple1)
print(type(tuple1))

# 2- 如何使用元组
# 2.1 获取元组中某个元素:  与 列表 和 字符串 一致 都是通过索引的方式来获取
print(user_tuple[0])
print(user_tuple[1])
print(user_tuple[2])

# 2.2 遍历: 与 列表 一致
for e in user_tuple:
    print(e)

# 2.3 获取某个元素在元组中索引值: index
print(user_tuple.index(True))

# 2.4 获取某个元素在元组中出现了几次
print(user_tuple.count('小刚'))

# 2.5 获取元组长度
print(len(user_tuple))