'''
循环可以和else配合使用，else下方缩进的代码指的是当循环正常结束之后要执行的代码（即没有被break终止，完整执行完所有循环次数）。
强调：'正常结束'，非正常结束（如遇到break、程序异常），其else中的代码是不会执行的。
'''
#**break关键字对for...else结构的影响**
str1 = 'python'
for i in str1:
    if i == 'h':
        print('遇h强制结束循环')
        break
    print(i)
else:
    print('循环正常结束之后执行的代码')


#**continue关键字对for...else结构的影响**
str1 = 'python'
for i in str1:
    if i == 'h':
        print('遇h不打印')
        continue
    print(i)
else:
    print('循环正常结束之后执行的代码')




# 演示: for循环结合else情况
"""
    语法:
        for 临时变量 in  序列:
            循环体
        else:
            当循环正常结束后, 需要执行的代码

    如果for循环中,
        通过break退出的循环, 那么就不会执行else语句的内容
        通过continue跳过当前循环, 对于else 不会有影响的
        在循环过程中程序出现异常(程序异常结束), else也不会执行
"""
# 需求: 循环输出从 1~6, 当循环正常结束后, 打印 循环完成
for i in range(1,7):
    # 当循环到3的时候, 强制退出循环（注释后可测试正常情况）
    # if i == 3:
    #     break

    # 当循环到3的时候, 跳过当前循环 进入下一次循环
    # if i == 3:
    #     continue
    # 异常情况（注释后可测试正常情况）
    # 1/0
    print(i)
else:
    print("循环结束了.....")