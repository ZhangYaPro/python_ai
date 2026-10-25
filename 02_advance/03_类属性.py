'''
演示类属性
'''

class Student():
    #类属性  ----  所有对象共有的属性叫做类属性
    #学校
    school = '第一中学'
    #班费
    class_money = 200
    # 定义对象
    def __init__(self,name,age):
        self.name = name
        self.age = age
#创建对象
stu1 = Student('yabo',25)
#通过对象访问类属性
print(stu1.school)
#也可以通过类名访问类属性
print(stu1.school)

#创建对象李四
stu2 = Student('李四',28)
print(stu2.school)
#通过类名修改属性
Student.school = '第二中学'
print(stu1.school)
print(stu2.school)
# 隐藏bug，看似是通过对象修改类属性，其实是添加对象属性
# 其实是给stu1添加对象属性school
# 因为赋值操作具有二义性，被理解为stu1添加了一个对象属性school
stu1.school = '第三中学'

# 应用，利用类属性统计创建的实例个数
class Person:
    # 统计创建了多少实例
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 对类属性进行修改，自增
        Person.count += 1

zs = Person('zs',25)
lisi = Person('lisi',25)
print(f'总共创建了{Person.count}个实例')