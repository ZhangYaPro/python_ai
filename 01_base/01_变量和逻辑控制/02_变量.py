# 变量名 = 变量值（等号两侧保留1个空格）
age = 18  # 整数类型
name = "张三"  # 字符串类型
score = 98.5  # 浮点数类型

# 方法1：type()函数
age = 18
print(type(age))  # <class 'int'>

# 方法2：isinstance()函数（推荐）
print(isinstance(age, int))  # True
print(isinstance(age, str))  # False