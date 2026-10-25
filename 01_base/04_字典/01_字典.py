# 有数据字典
dict1 = {'name': 'ZhangSan', 'age': 19, 'gender': '男'}

# 空字典
dict2 = {}

dict3 = dict()



# 1- 演示: 如何定义字典
# 格式:
#   格式1:  变量名称 = {key1:value1,key2:value2,key3:value3.....}
#   格式2:  变量名称 = {}  或者 变量名称 = dict()   空字典

# 构建一个有内容的字典
person = {'name': '小明', 'age': 19, 'address': "上海市浦东新区张江镇", 'sex': '男', 'hobby': '篮球、足球、游泳'}
print(person)
print(type(person))

# 构建空字典
dict1 = {}
dict2 = dict()
print(dict1)
print(type(dict1))
print(dict2)
print(type(dict2))

# 遍历操作
for key in person:
    print(key)
    print(person[key])


#字典的增操作
'''
字典名称[key] = value
注：如果key存在则修改这个key对应的值；如果key不存在则新增此键值对。
'''

#字典的删除操作
'''
字典名称[key] = value
注：如果key存在则修改这个key对应的值；如果key不存在则新增此键值对。
'''
# del 字典名称[key]：删除指定元素
person = {'name': '小明', 'age': 19}
del person['age']
print(person)
#clear()方法：清空字典中的所有key
person = {'name': '小明', 'age': 19}
person.clear()
print(person)

#字典的改操作
'''
字典名称[key] = value
注：如果key存在则修改这个key对应的值；如果key不存在则新增此键值对。
'''
person = {'name': '小明', 'age': 19, 'address': '上海市浦东新区'}
person['address'] = '上海市黄浦区'
print(person)

#字典的查操作
#案例1:提取person字典中的所有key
person = {'name': '小明', 'age': 19, 'address': '上海市浦东新区'}
print(person.keys())  # 类型是列表
#案例2：提取person字典中的所有value值
person = {'name': '小明', 'age': 19, 'address': '上海市浦东新区'}
print(person.values())
#案例3：使用items()方法提取数据
person = {'name': '小明', 'age': 19, 'address': '上海市浦东新区'}
print(person.items())
# 字典的相关API:
# 如何增加元素:
# 需求: 为person 字典增加一个 birthday 属性 值为 2005-08-20
person = {'name': '小明', 'age': 19, 'address': "上海市浦东新区张江镇", 'sex': '男', 'hobby': '篮球、足球、游泳'}
person["birthday"] = '2005-08-20'

print(person)

# 如何修改元素: 与添加一直, 如果key存在就是修改 如果不存在 就是添加
# 需求: 修改性别为 女
person['sex'] = "女"
print(person)

# 如何删除元素
# 删除某个元素:  根据key
del person['birthday']
print(person)
# 清空字典
# person.clear()
# print(person)

# 如何查询:
# 1- 根据 key 直接获取value: 如果key 不存在 直接报错
# 获取 address的值
print(person['address'])

# 2- 获取所有的keys
keys_list = person.keys()
print(keys_list)
# 3- 获取所有的value
values_list = person.values()
print(values_list)
# 4- 获取字典中每一个 kv对
# 快速返回变量: ctrl + alt + v
items = person.items()
print(items)

for kv in items:
    print(kv)
    print(f'{kv[0]},{kv[1]}')


"""
    给定一个字符串my_string，现在要求统计每个字符出现的次数: 形成结果: {'字符':出现次数,'字符2':次数}

    例如: 'abcdecf' ==> {'a':1,'b':1,'c':2,'d':1,'e':1,'f':1}
"""
# 1- 创建一个字符串
my_string = 'abcdecf'

# 2- 遍历字符串, 获取每一个字符
# 2.1 初始化一个用于保存结果的空字典
my_dict = {}
for e in my_string:

    # 2.2 判断 当前遍历的这个元素 是否在 字典中存在呢?
    if e in my_dict.keys():
        # 说明 当前遍历的元素 在 字典中是存在的
        my_dict[e] += 1
    else:
        # 说明 当前遍历的元素 在 字典中是不存在的
        my_dict[e] = 1

print(my_dict)
