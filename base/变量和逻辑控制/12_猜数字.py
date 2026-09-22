# 演示 猜数字游戏（无random、无异常，适合未学相关知识的学生）
# 1- 提前设定固定答案（1~20之间），无需随机生成
answer = 12
# 2- 让用户反复猜测，写死循环方式
print("欢迎来到猜数字游戏！")
print("规则：系统已设定1~20之间的一个整数，猜对即可结束游戏，每次猜测会提示猜大或猜小～")
while True:
    # 2.1 让用户输入猜测的数字（直接转为整数，提示用户输入整数）
    user_guess = int(input("请输入你猜测的1~20之间的整数："))
    # 2.2 判断猜测结果，给出对应提示
    if user_guess == answer:
        print("恭喜你，猜对了！游戏结束～")
        # 猜对后终止循环
        break
    elif user_guess > answer:
        print("猜大了，再试试小一点的数字！")
    else:
        print("猜小了，再试试大一点的数字！")



# 演示 猜数字游戏（限制次数版，无random、无异常）
# 1- 提前设定固定答案（1~20之间），无需随机生成
answer = 12
# 2- 定义猜测次数（限制3次）
guess_count = 1
# 3- 写死循环，控制猜测次数
print("欢迎来到猜数字游戏！")
print("规则：系统已设定1~20之间的一个整数，你有3次猜测机会，猜对即可获胜～")
while True:
    # 3.1 让用户输入猜测的数字，提示剩余次数
    user_guess = int(input(f"请输入你猜测的1~20之间的整数（剩余{3 - guess_count + 1}次机会）："))
    # 3.2 判断猜测结果，给出对应提示
    if user_guess == answer:
        print(f"恭喜你，猜对了！你在第{guess_count}次就猜对了，游戏结束～")
        break
    elif user_guess > answer:
        print("猜大了，再试试小一点的数字！")
    else:
        print("猜小了，再试试大一点的数字！")
    # 3.3 判断次数是否用完
    if guess_count >= 3:
        print(f"猜测次数已用完！正确答案是{answer}，游戏结束～")
        break
    # 计数器+1
    guess_count += 1