#简单来说就是把一个元组中的数据一个一个拆解出来的过程，就称之为叫做拆包操作
tuple1 = (10, 20)
# 拆包
num1, num2 = tuple1

#以上代码可以简写为
num1, num2 = (10, 20)

#还可以进一步简写
num1, num2 = 10, 20

tuple1 = ("炸鸡", True, 25.5)
name, is_flag, price = tuple1
print(f"{name},{is_flag},{price}")

a, b = (10, 20)
print(f"{a},{b}")

a, b = 10, 20
print(f"{a},{b}")

#初始化两个变量
c1 = '游戏手柄'
c2 = 'Switch'
#直接交换（利用自动拆包）
c1 = '游戏手柄'
c2 = 'Switch'

c2, c1 = c1, c2

print(c1)
print(c2)

c1 = '游戏手柄'
c2 = 'Switch'

tmp = c1
c1 = c2
c2 = tmp

print(c1)
print(c2)