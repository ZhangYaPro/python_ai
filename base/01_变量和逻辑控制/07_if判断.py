# 单分支(if)
# 示例：判断是否成年
age = 19
if age >= 18:
    print("你已成年，可独立出行")

#双分支(if-else)
# 示例：判断是否成年
age = int(input("请输入你的年龄："))
if age >= 18:
    print("你已成年，可观看此电影")
else:
    print("你未成年，需由监护人陪同")

# 多分支（if-elif-else）
score = float(input("请输入你的考试成绩："))
if score >= 90:
    print("成绩评级：优秀")
elif score >= 80:
    print("成绩评级：良好")
elif score >= 70:
    print("成绩评级：中等")
elif score >= 60:
    print("成绩评级：及格")
else:
    print("成绩评级：不及格，需要补考")

#嵌套分支（if 内部嵌套 if/if-else）
# 示例：判断是否能参加驾照考试
age = int(input("请输入你的年龄："))
if age >= 18:
    print("你满足年龄要求，可报名驾照考试")
    height = float(input("请输入你的身高（cm）："))
    if height >= 150:
        print("身高符合要求，可正常报名")
    else:
        print("身高未达到要求，无法报名")
else:
    print("年龄未达标，无法报名驾照考试")

#条件表达式的高级用法
  #1.结合逻辑运算符实现复杂条件
# 示例：判断是否为工作日的工作时间
hour = int(input("请输入当前小时数（0-23）："))
weekday = input("请输入是否为工作日（是/否）：")
if weekday == "是" and 9 <= hour <= 18:
    print("当前是工作时间，请专注工作")
else:
    print("当前是非工作时间，可休息")
  #2.三元表达式
# 示例：简化判断成年与否
age = 20
result = "成年" if age >= 18 else "未成年"
print(f"你是：{result}")

# 等价于原双分支代码
if age >= 18:
    result = "成年"
else:
    result = "未成年"