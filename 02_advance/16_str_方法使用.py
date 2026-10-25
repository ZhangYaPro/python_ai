'''
演示new方法
'''
class Person:
    def __init__(self,name):
        self.name=name
    # 打印对象的时候会输出__str__返回的字符串
    def __str__(self):
        return f'我的名字是: {self.name}'

if __name__ == '__main__':
    p = Person('Zack')
    print(f'p is {p}')
