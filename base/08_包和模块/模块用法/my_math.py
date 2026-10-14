'''
文件名就是模块名
'''
def my_add(num1,num2):
    return num1+num2

if __name__ == '__main__':
    print('这是my_math模块')
    '''
    当my_math作为模块被别人导入时候，__name__为my_math（模块名）
    当my_math 自己启动时，__name__就是__main__
    '''
    print(f'__name__ is:{__name__}')