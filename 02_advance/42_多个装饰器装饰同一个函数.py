'''
多装饰器执行：先登录校验、再权限校验，最后执行业务
'''

def check_login(func):
    def inner():
        print('✔ 检测用户是否登录（SSO验证）')
        func()
    return inner

def check_permission(func):
    def inner():
        print('✔ 检查用户是否具备报销权限（财务系统权限）')
        func()
    return inner

# 多装饰器叠加
@check_login
@check_permission
def submit_reimbursement():
    print('📄 提交报销申请（上传发票+填写金额）')

submit_reimbursement()