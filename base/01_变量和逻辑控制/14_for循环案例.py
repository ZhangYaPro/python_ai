# 用户登录案例（for循环版）

# 1- 构建循环, 并且循环只能有 2次
for i in range(0,2):
    # 2: 让用户输入 用户名 和 密码
    user_name = input("请输入用户名:")
    user_pwd = input("请输入密码:")

    # 3: 判断 用户名和密码是否正确
    if user_name == 'student':
        if user_pwd == 'python123':
            print("恭喜您, 登录成功！")
            # 登录成功后, 直接退出循环
            break
        else:
            print(f"您输入的密码不正确, 您还剩余{1-i}次机会")
    else:
        print(f"您输入的用户名不正确, 您还剩余{1-i}次机会")
else:
    # 循环正常结束（未break），说明次数用完
    print("登录失败，次数已用完！")


