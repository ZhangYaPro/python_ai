'''
演示函数用法
'''
'''
定义:
def 函数名称(参数1, 参数2, ...):
    函数体
    ...
    [return 返回值]
调用函数:
函数名称(参数1, 参数2, ...)
'''

#第二步：封装成函数 — 代码复用
# 定义一个函数：捡道具
def pick_item():
    """捡起一个道具，自动占用背包一个空格"""
    print("捡到1个道具！")

# 调用函数，不用重复写代码了
pick_item()      # 第1次捡道具
pick_item()      # 第2次捡道具
pick_item()      # 第3次捡道具
pick_item()      # 第4次捡道具


# 第三步：函数带参数 — 告诉函数具体捡什么
# 场景：捡到的东西不一样，打印的信息也要不一样
# 用参数来解决这个问题
def pick_item(item_name):
    """捡起一个道具
    参数:
        item_name: 道具名称
    """
    print(f"捡到了 【{item_name}】！")
# 调用时传入具体道具名
pick_item("生命药水")   # 捡到生命药水
pick_item("火焰剑")     # 捡到火焰剑
pick_item("蓝宝石")     # 捡到蓝宝石
pick_item("黄金头盔")   # 捡到黄金头盔


#第四步：函数带返回值 — 告诉调用者结果
# 场景：希望函数告诉调用者，捡道具到底成不成功
# 比如背包满了就捡不了

# 设定背包容量
bag_capacity = 100
current_count = 0

def pick_item(item_name):
    """捡起一个道具
    返回 True 表示成功，False 表示失败（背包满了）
    """
    global current_count  # 声明使用全局变量

    # 检查背包是否满了
    if current_count >= bag_capacity:
        return False  # 捡不了，返回失败

    current_count += 1
    print(f"捡到了 【{item_name}】！背包进度：{current_count}/{bag_capacity}")
    return True  # 捡到了，返回成功

# 调用并判断结果
result = pick_item("生命药水")
if result:
    print("✅ 捡道具成功！")
else:
    print("❌ 背包已满，无法捡取！")

result = pick_item("火焰剑")
if result:
    print("✅ 捡道具成功！")
else:
    print("❌ 背包已满，无法捡取！")



#函数返回多个返回值
def return_num():
    return 1, 2
result = return_num()# 返回一个元组
print(result)     # 返回一个元组
print(type(result))  # <class 'tuple'>


#思考3：封装一个函数，参数有两个num1，num2，求两个数的四则运算结果
def size(num1, num2):
    jia = num1 + num2
    jian = num1 - num2
    cheng = num1 * num2
    chu = num1 / num2
    return jia, jian, cheng, chu


# 调用size方法
print(size(20, 5))   #返回一个元组


# 需求: 请帮我定义一个函数: computer 计算器函数, 要求给这个函数传入 2个参数, 在函数的内部完成  + - 计算, 并且将 + -的二个结果返回

# 定义函数:
def computer(a, b):
    # 编写函数功能的核心位置
    jia = a + b
    jian = a - b

    # 将加和减结果一并返回
    return jia, jian
    # return [jia, jian]
    # return {jia, jian}
    # return {'jia':jia,'jian':jian}


# 调用函数
# res = computer(3,5)
#元组拆包思想
i,j = computer(3,5)  # 利用自动拆包思想
print(f'加法结果:{i},减法的结果:{j}')
