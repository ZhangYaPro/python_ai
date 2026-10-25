'''
列表序列名称 = [列表中的元素1, 列表中的元素2, 列表中的元素3, ...]
注意: 列表是可变的
'''
fruit_list = ['orange', 'grape', 'mango']
# list列表类型支持直接打印
print(fruit_list)
# 打印列表的数据类型
print(type(fruit_list))  # <class 'list'>


# 演示: 如何定义列表
# 格式: 变量名称 = [元素1,元素2,元素3......]
# 需求: 构建一个列表, 保存 小明 小红 小刚 小丽 四个名字
name_list = ['小明','小红','小刚','小丽']
print(name_list)

# 如何获取列表中某一个元素呢? 与 字符串 一致
print(name_list[0])
print(name_list[1])
print(name_list[2])

# 如何遍历列表呢?
print("-----------------")
# for循环
for name in name_list:
    print(name)

# while循环
print("-----------------")
# 计数器
i = 0

while i < len(name_list):
    print(name_list[i])

    # 更新计数器
    i += 1

