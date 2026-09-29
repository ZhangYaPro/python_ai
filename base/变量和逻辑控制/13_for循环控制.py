# 演示: for基本使用
"""
    语法格式:
        for 临时变量 in 序列:
            循环执行的代码块

        注意:
            临时变量的值 其实 就是 序列中每一个元素，循环次数等于序列的长度
"""
# 需求: 遍历一个字符串 :  python
for char in "python":
    print(char)



# 演示 range函数
# 作用: 帮我们生成一个连续的数字, 例如 0~3
# 语法:  range(起始值,结束值,步长)
#  起始值: 默认为  0   结束值: 必填的  在生成序列的时候, 不含结束值  步长: 默认为1 表示 数字与数字之间的间隔
# 需求: 生成 4以内的序列, 并且将每一个值打印出来   range(0,4,1)--->range(0,4)--->range(4)
for num in range(0,4):
    print(num)


# 需求: 求 1~50 之间 所有的奇数之和
sum_odd = 0
for num in range(1,51):
    if num % 2 != 0:
        sum_odd += num
print(sum_odd)