"""
班级活动费用分摊系统
功能：
1. 输入参与人数和活动总花费
2. 额外收取10%组织管理费，计算最终总费用
3. 判断人数是否合法（至少1人）
4. 计算每人需要分摊的金额并输出
"""

# 输入并转换数据类型
total_people = int(input("请输入参与活动人数："))
total_cost = float(input("请输入活动总花费（元）："))

# 条件判断：人数是否合法
if total_people < 1:
    print("人数输入错误，至少1人！")
else:
    # 计算含组织管理费的总费用和人均费用
    manage_fee = total_cost * 0.1  # 10%组织管理费
    final_total = total_cost + manage_fee
    per_person = final_total / total_people

    # 格式化输出
    print("=" * 30)
    print(f"原始活动花费：{total_cost:.2f}元")
    print(f"10%组织管理费：{manage_fee:.2f}元")
    print(f"最终总费用：{final_total:.2f}元")
    print(f"参与人数：{total_people}人")
    print(f"每人需分摊：{per_person:.2f}元")
    print("=" * 30)