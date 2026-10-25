'''
演示类方法
'''

class Student:
    #类属性
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1

#使用@classmethod修饰的方法就是类方法
    @classmethod
    def show_count(cls):
        print(f"当前学生人数：{cls.count}")

Student("张三")
Student("李四")
Student.show_count()