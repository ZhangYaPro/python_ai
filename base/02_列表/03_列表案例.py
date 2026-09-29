'''
案例需求（全新）

判断相邻元素的变化趋势
给定一个正整数数组，判断每一对相邻元素是“上升”“下降”还是“相等”，并输出结果列表
'''
# 判断相邻元素变化趋势

num_list = [3, 5, 5, 2, 4]

result_list = []

i = 0

while i < len(num_list) - 1:
    if num_list[i] < num_list[i + 1]:
        result_list.append("上升")
    elif num_list[i] > num_list[i + 1]:
        result_list.append("下降")
    else:
        result_list.append("相等")

    i += 1

print(result_list)

'''
找出列表中第一次出现的重复元素

给定一个列表，找到第一个重复出现的元素（只要出现第二次就算重复），并输出该元素'''


# 找第一个重复元素

num_list = [2, 3, 5, 3, 6, 5, 7]

seen_list = []

for e in num_list:
    if e in seen_list:
        print(e)
        break
    else:
        seen_list.append(e)