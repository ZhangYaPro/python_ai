name = "李四"
age = 20
score = 95.5
#f-string（Python3.6+，推荐）
# 基础用法
print(f"姓名：{name}，年龄：{age}，成绩：{score}")
# 格式控制（保留2位小数）
print(f"成绩：{score:.2f}")
# 数字补零（6位宽度）
print(f"学号：{1:06d}")  # 输出：000001


#方式 2：format() 方法
print("姓名：{}，年龄：{}".format(name, age))
# 指定位置
print("年龄：{1}，姓名：{0}".format(name, age))
# 格式控制
print("成绩：{:.2f}".format(score))