import random
# 方式一: 使用 单引号 或者 双引号创建
student_name1 = '黎明'
student_name2 = "李明"

# 思考: 如果在字符串里面也有单引号或者双引号怎么办呢?
# 解决方案一: 使用转义符 \
# msg = 'It\'s a wonderful day'
# 解决方案二:如果里面是单引号,那么外部就使用双引号,反之也可以
# msg = "It's a wonderful day"

# 如果字符串里面既有单引又有双引: 也可以针对跟外部引号一致的内容使用转义符
# msg = " He said \"It's great\" "

text = 'hello'
print(text[0])  # h
print(text[3])  # l

#字符串切片
#序列名称[开始位置下标:结束位置下标:步长(步阶)]

# 三个参数都有默认值:
#     开始位置默认值: 0
#     结束位置默认值: -1 (最后一个)
#     步长: 1

digits = '0123456789'
digits[0:3:1]  # 012 => range方法非常类似，步长：每次前进1步
digits[0:3:2]  # 02 => 每次前进2步
# 步长可以为负数，正数代表从左向右截取，负数代表从右向左截取

# 案例一:
digits = '0123456789'

# 1、从2到5开始切片，步长为1
print(digits[2:5])     # 输出: 234

# 2、只有结尾的字符串切片：代表从索引为0开始，截取到索引为5的位置（不包含索引为5的数据）
print(digits[:5])      # 输出: 01234

# 3、只有开头的字符串切片：代表从起始位置开始(例如 1)，一直截取到字符串的结尾
print(digits[1:])      # 输出: 123456789

# 4、获取或拷贝整个字符串
print(digits[:])       # 输出: 0123456789

# 5、调整步阶：类似求偶数
print(digits[::2])     # 输出: 02468

# 6、把步阶设置为负整数：类似字符串翻转
print(digits[::-1])    # 输出: 9876543210

# 7、起始位置与结束位置都是负数
print(digits[-5:-1])   # 输出: 5678

# 8、结束字符为负数，如截取012345678
print(digits[:-1])     # 输出: 012345678


'''
- **案例2：给定一个图片的名称为"photo.jpg"，代码实现获取这个图片的名称(photo)以及这个图片的后缀(.jpg)。**
  - 分析：

    - ① 建议先获取点号的位置（目前还未学习，只能一个一个数）

    - ② 从开头切片到点号位置，得到的就是文件的名称

    - ③ 从点号开始切片，一直到文件的结尾，则得到的就是文件的后缀

- 代码'''
filename = "photo.jpg"

# 方法一：已知点号位置在索引5
name = filename[:5]      # photo
suffix = filename[5:]    # .jpg

print(f"文件名: {name}")
print(f"后缀名: {suffix}")

# 方法二：使用字符串方法(后续会学习)
dot_index = filename.find('.')
name = filename[:dot_index]
suffix = filename[dot_index:]


# 定义一个字符串
message = 'welcome to Python programming, Python is great'

# 查找Python子串是否出现在字符串中
position = message.find('Python')
print(f"Python首次出现的位置: {position}")  # 输出: 11

# 在message中查找不存在的子串
position2 = message.find('Java')
print(f"Java出现的位置: {position2}")  # 输出: -1

#使用input方法输入任意一个文件名称，求点号的索引下标
filename = input("请输入文件名: ")
dot_position = filename.find('.')
if dot_position != -1:
    print(f"点号的位置在索引: {dot_position}")
    print(f"文件名: {filename[:dot_position]}")
    print(f"扩展名: {filename[dot_position:]}")
else:
    print("该文件名中没有扩展名")


#index()方法
fruits = 'apple, banana, orange, grape'

# 判断apple是否出现在字符串fruits中
position = fruits.index('apple')
print(f"apple的位置: {position}")  # 输出: 0

# 查找不存在的子串会报错
# position = fruits.index('mango')  # 这行会引发ValueError异常

#字符串.replace(要替换的内容, 替换后的内容, 替换的次数-可以省略)
text = 'I love Java programming and Java is powerful'

# 把字符串中所有Java字符替换为Python
new_text = text.replace('Java', 'Python')
print(new_text)  # 输出: I love Python programming and Python is powerful

# 把字符串中的第一个Java进行替换为Python
new_text2 = text.replace('Java', 'Python', 1)
print(new_text2)  # 输出: I love Python programming and Java is powerful

# 把and字符串替换为&
new_text3 = text.replace('and', '&')
print(new_text3)  # 输出: I love Java programming & Java is powerful



#split()方法
# 示例：按照逗号分隔日期
date_str = '2024-03-15'
date_parts = date_str.split('-')
print(date_parts)  # 输出: ['2024', '03', '15']

# 示例：分割邮箱地址
email = 'user@example.com'
parts = email.split('@')
print(f"用户名: {parts[0]}")  # 输出: user
print(f"域名: {parts[1]}")    # 输出: example.co

#join()方法   字符串.join(数据序列)
fruit_list = ['apple', 'banana', 'orange']
result = '-'.join(fruit_list)
print(result)  # 输出: apple-banana-orange

# 其他示例
words = ['Hello', 'Python', 'World']
sentence = ' '.join(words)
print(sentence)  # 输出: Hello Python World


# 练习1：确保验证码至少包含一个数字和一个字母
def generate_secure_code(length=6):
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    all_chars = uppercase + lowercase + digits

    while True:
        code = ''
        for i in range(length):
            random_index = random.randint(0, len(all_chars) - 1)
            code += all_chars[random_index]

        # 检查是否包含数字和字母
        has_letter = any(c in uppercase + lowercase for c in code)
        has_digit = any(c in digits for c in code)

        if has_letter and has_digit:
            return code


print("安全验证码:", generate_secure_code())


# 练习2：验证用户输入的验证码是否正确（不区分大小写）
def verify_code(user_input, correct_code):
    """验证验证码（不区分大小写）"""
    return user_input.lower() == correct_code.lower()


# 模拟验证码验证
real_code = "aB3xK9"
user_code = "AB3XK9"
if verify_code(user_code, real_code):
    print("验证码正确！")
else:
    print("验证码错误！")