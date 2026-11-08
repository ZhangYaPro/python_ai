'''
演示带参数装饰器，根据操作类型记录不同的日志（公司审计系统）
'''

def audit(action_type):
    # 中层：接收原函数
    def decorator(func):
        # 内层：执行业务
        def inner(user, amount):
            if action_type == 'recharge':
                print('--[审计] 用户正在进行充值操作')
            elif action_type == 'withdraw':
                print('--[审计] 用户正在进行提现操作')
            elif action_type == 'transfer':
                print('--[审计] 用户正在进行转账操作')

            result = func(user, amount)
            return result
        return inner
    return decorator


@audit('recharge')
def wallet(user, amount):
    print(f'{user} 账户变动金额：{amount}')
    return f'操作成功：{amount}'


print(wallet('Alice', 100))