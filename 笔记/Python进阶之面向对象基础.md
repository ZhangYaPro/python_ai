## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">学习目标</font>**
1. <font style="color:black;">理解什么是面向对象编程。</font>
2. <font style="color:black;">区分类、对象、属性、方法的概念。</font>
3. <font style="color:black;">能够使用 Python 定义类并创建对象。</font>
4. <font style="color:black;">理解 </font>的作用。
5. <font style="color:black;">掌握构造方法 </font>`__init__`<font style="color:black;"> 的使用。</font>
6. <font style="color:black;">理解封装、继承、多态三大核心思想。</font>
7. <font style="color:black;">能够用面向对象思想解决简单实际问题。</font>

---

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">为什么需要面向对象</font>**
### <font style="color:rgb(0, 0, 0);">面向过程</font>
<font style="color:rgb(0, 0, 0);">面向过程的核心思想是：</font>**<font style="color:rgb(0, 0, 0);">自顶向下，逐步细化</font>**<font style="color:rgb(0, 0, 0);">。</font>

<font style="color:rgb(0, 0, 0);">特点：</font>

+ <font style="color:black;">把问题拆成一个个步骤</font>
+ <font style="color:black;">每个步骤用函数实现</font>
+ <font style="color:black;">按顺序执行</font>

<font style="color:rgb(0, 0, 0);">示例（报名流程）：</font>

<font style="color:rgb(0, 0, 0);">开始 → 提交信息 → 缴费 → 分班 → 结束</font>

<font style="color:rgb(0, 0, 0);">问题：</font>

+ <font style="color:black;">数据与行为分离</font>
+ <font style="color:black;">难以维护复杂系统</font>

---

### <font style="color:rgb(0, 0, 0);">面向对象</font>
<font style="color:rgb(0, 0, 0);">核心思想：</font>

<font style="color:black;background-color:rgb(255, 249, 249);">不再关注“做什么步骤”，而是关注“谁来做这些事情”</font>

<font style="color:rgb(0, 0, 0);">例如报名系统可以抽象为4个对象：</font>

+ <font style="color:black;">学生</font>
+ <font style="color:black;">教师</font>
+ <font style="color:black;">大学</font>
+ <font style="color:black;">班级</font>

<font style="color:rgb(0, 0, 0);">每个对象：</font>

+ <font style="color:black;">有属性（数据）</font>
+ <font style="color:black;">有方法（行为）</font>

---

### <font style="color:rgb(0, 0, 0);">核心对比</font>
| **<font style="color:rgb(0, 0, 0);">维度</font>** | **<font style="color:rgb(0, 0, 0);">面向过程</font>** | **<font style="color:rgb(0, 0, 0);">面向对象</font>** |
| :------------------------------------------------ | :---------------------------------------------------- | :---------------------------------------------------- |
| <font style="color:rgb(0, 0, 0);">思维方式</font> | <font style="color:rgb(0, 0, 0);">步骤导向</font>     | <font style="color:rgb(0, 0, 0);">对象导向</font>     |
| <font style="color:rgb(0, 0, 0);">复杂系统</font> | <font style="color:rgb(0, 0, 0);">难维护</font>       | <font style="color:rgb(0, 0, 0);">易扩展</font>       |
| <font style="color:rgb(0, 0, 0);">代码复用</font> | <font style="color:rgb(0, 0, 0);">较低</font>         | <font style="color:rgb(0, 0, 0);">更高</font>         |


---

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">什么是类和对象</font>**
### <font style="color:rgb(0, 0, 0);">对象</font>
<font style="color:rgb(0, 0, 0);">对象是现实世界中具体存在的一个事物。</font>

<font style="color:rgb(0, 0, 0);">例如：</font>

+ <font style="color:black;">一个具体的学生：张三</font>
+ <font style="color:black;">一辆具体的汽车：我的白色汽车</font>
+ <font style="color:black;">一只具体的猫：小花</font>
+ <font style="color:black;">一个具体的订单：订单编号 1001</font>

<font style="color:rgb(0, 0, 0);">在程序中，对象通常包含两部分：</font>

| **<font style="color:rgb(0, 0, 0);">组成</font>** | **<font style="color:rgb(0, 0, 0);">含义</font>**         | **<font style="color:rgb(0, 0, 0);">示例</font>**            |
| :------------------------------------------------ | :-------------------------------------------------------- | :----------------------------------------------------------- |
| <font style="color:rgb(0, 0, 0);">属性</font>     | <font style="color:rgb(0, 0, 0);">对象的数据、特征</font> | <font style="color:rgb(0, 0, 0);">姓名、年龄、颜色</font>    |
| <font style="color:rgb(0, 0, 0);">方法</font>     | <font style="color:rgb(0, 0, 0);">对象的行为、功能</font> | <font style="color:rgb(0, 0, 0);">学习、跑步、打印信息</font> |


### <font style="color:rgb(0, 0, 0);">类</font>
<font style="color:rgb(0, 0, 0);">类是对象的模板或设计图。</font>

<font style="color:rgb(0, 0, 0);">例如：</font>

+ <font style="color:black;">“学生类”是所有学生的模板</font>
+ <font style="color:black;">“汽车类”是所有汽车的模板</font>
+ <font style="color:black;">“猫类”是所有猫的模板</font>

<font style="color:rgb(0, 0, 0);">类和对象的关系可以这样理解：</font>

| **<font style="color:rgb(0, 0, 0);">类</font>** | **<font style="color:rgb(0, 0, 0);">对象</font>**            |
| :---------------------------------------------- | :----------------------------------------------------------- |
| <font style="color:rgb(0, 0, 0);">图纸</font>   | <font style="color:rgb(0, 0, 0);">根据图纸造出来的房子</font> |
| <font style="color:rgb(0, 0, 0);">模板</font>   | <font style="color:rgb(0, 0, 0);">根据模板创建出来的具体内容</font> |
| <font style="color:rgb(0, 0, 0);">学生类</font> | <font style="color:rgb(0, 0, 0);">张三、李四、王五</font>    |
| <font style="color:rgb(0, 0, 0);">汽车类</font> | <font style="color:rgb(0, 0, 0);">宝马、奔驰、比亚迪</font>  |


<font style="color:rgb(0, 0, 0);">一句话总结：</font>

<font style="color:black;background-color:rgb(255, 249, 249);">类是抽象的，对象是具体的。</font>

---

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">定义类和创建对象</font>**
### <font style="color:rgb(0, 0, 0);">定义一个最简单的类</font>
```python
class Student:
    pass
```

<font style="color:rgb(0, 0, 0);">说明：</font>

+ <font style="color:black;"> 是定义类的关键字。</font>
+ 是类名，通常使用大驼峰命名法。
+ 表示暂时不写内容。

### <font style="color:rgb(0, 0, 0);">创建对象</font>
```python
stu1 = Student()
stu2 = Student()

print(stu1)
print(stu2)
```

`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">stu1</font>`<font style="color:rgb(0, 0, 0);"> 和 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">stu2</font>`<font style="color:rgb(0, 0, 0);"> 都是通过 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">Student</font>`<font style="color:rgb(0, 0, 0);"> 类创建出来的对象。</font>

<font style="color:rgb(0, 0, 0);">它们属于同一个类，但它们是两个不同的对象。</font>

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1779783290172-6a0a61e9-e335-44b2-a113-90578139b87f.png" width="1466" alt="" title="" crop="0,0,1,1" id="uf2cc69b1" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">给对象添加属性</font>**
<font style="color:rgb(0, 0, 0);">对象的属性可以理解为对象的数据。</font>

```python
'''
演示类的基础操作
'''

'''
定义一个类类型
class 类名():
    pass
创建对象
变量 = 类名()
'''
# 学生类
class Student():
    pass

# 创建一个对象赋值给s1
s1 = Student()
# 创建一个对象赋值给s2
s2 = Student()
print(f's1 : {s1}')
print(f's2 : {s2}')

# 为s1添加name属性，属性值为'zack'
s1.name = 'zack'
# 为s1添加age属性,属性值为18
s1.age = 18
print(f's1.age : {s1.age}')
print(f's1.name : {s1.name}')
# s2因为没有添加属性，所以不能通过属性访问
# print(f's2.age : {s2.age}')
```

<font style="color:rgb(0, 0, 0);">输出：</font>

```python
张三
18
```

<font style="color:rgb(0, 0, 0);">这种方式可以添加属性，但不推荐在正式项目中大量使用，因为每个对象的属性可能不统一。</font>

<font style="color:rgb(0, 0, 0);">例如：</font>

```python
stu1.name = "张三"
stu2.score = 95
```

<font style="color:rgb(0, 0, 0);">这样会导致对象结构混乱。</font>

<font style="color:rgb(0, 0, 0);">更推荐使用构造方法 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">__init__</font>`<font style="color:rgb(0, 0, 0);"> 来统一初始化属性。</font>

---

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">构造方法 </font>**
### <font style="color:rgb(0, 0, 0);">什么是构造方法</font>
<font style="color:rgb(0, 0, 0);">构造方法是在创建对象时自动执行的方法。</font>

<font style="color:rgb(0, 0, 0);">在 Python 中，构造方法的名字固定为：</font>

__init__

<font style="color:rgb(0, 0, 0);">示例：</font>

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

stu1 = Student("张三", 18)
stu2 = Student("李四", 19)

print(stu1.name, stu1.age)
print(stu2.name, stu2.age)
```

<font style="color:rgb(0, 0, 0);">输出：</font>

```python
张三 18
李四 19
```

### <font style="color:rgb(0, 0, 0);">self` 是什么</font>
`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">self</font>`<font style="color:rgb(0, 0, 0);"> 表示当前对象本身。</font>

<font style="color:rgb(0, 0, 0);">当执行：</font>

stu1 = Student("张三", 18)

<font style="color:rgb(0, 0, 0);">可以理解为：</font>

```python
self 指向 stu1
self.name = "张三"
self.age = 18
```

<font style="color:rgb(0, 0, 0);">当执行：</font>

stu2 = Student("李四", 19)

<font style="color:rgb(0, 0, 0);">可以理解为：</font>

```python
self 指向 stu2
self.name = "李四"
self.age = 19
```

<font style="color:rgb(0, 0, 0);">所以 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">self</font>`<font style="color:rgb(0, 0, 0);"> 的作用是：</font>

<font style="color:black;background-color:rgb(255, 249, 249);">区分当前操作的是哪一个对象。</font>

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1779783291655-38b6f0fe-6341-45dc-becd-32e9d23a2e5d.png" width="1843" alt="" title="" crop="0,0,1,1" id="ueedb3216" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

### <font style="color:rgb(0, 0, 0);">常见错误</font>
<font style="color:rgb(0, 0, 0);">错误写法：</font>

```python
class Student:
    def __init__(name, age):
        name = name
        age = age
```

<font style="color:rgb(0, 0, 0);">问题：</font>

1. <font style="color:black;">少写了 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">self</font>`<font style="color:black;">。</font>
2. <font style="color:black;">没有把数据保存到对象中。</font>
3. `<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">name = name</font>`<font style="color:black;"> 只是局部变量赋值，没有意义。</font>

<font style="color:rgb(0, 0, 0);">正确写法：</font>

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">对象方法</font>**
<font style="color:rgb(0, 0, 0);">方法就是定义在类中的函数，用来描述对象的行为。</font>

```python
'''
讲解init方法
'''

class Student:
    # 当使用Student类创建对象的时候，会调用下面的方法
    def __init__(self,name, age):
        '''
        构造方法
        :param name: 学生的名字
        :param age: 学生的年龄
        :param self: 对象的地址，或者self指向了对象
        '''
        # 为对象添加name属性
        self.name = name
        # 为对象添加age属性
        self.age = age
    # 定义对象的方法自我介绍，不接受实参
    def introduce(self):
        # 将来对象会自动传递给self, 比如s1.introduce, self就是s1
        print(f'您好,我是{self.name}, 我今年{self.age}岁了')
'''
创建一个学生对象, 会自动调用__init__,
1. __init__需要三个参数，第一个self实际是指向了对象的地址，这个对象在调用__init__之前
通过__new__方法就已经创建好，提前在堆空间创建好的， 解释器会自动将这个对象的地址赋值给self
不需要开发者传参
2. name, age需要通过Student('zack',18)传递，将实参传递给name,age两个形参
'''
# 用s1存储Student生成的对象
s1 = Student('zack',18)
# 通过对象.属性的方式访问属性
print(s1.name)
print(s1.age)
# 调用introduce方法, s1会自动传递给self
s1.introduce()
```

<font style="color:rgb(0, 0, 0);">输出：</font>

大家好，我叫张三，今年18岁

<font style="color:rgb(0, 0, 0);">说明：</font>

+ `<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">introduce</font>`<font style="color:black;"> 是对象方法。</font>
+ <font style="color:black;">对象方法的第一个参数通常也是 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">self</font>`<font style="color:black;">。</font>
+ <font style="color:black;">调用方法时，不需要手动传入 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">self</font>`<font style="color:black;">。</font>

<font style="color:rgb(0, 0, 0);">也就是说：</font>

stu1.introduce()

<font style="color:rgb(0, 0, 0);">Python 会自动把 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">stu1</font>`<font style="color:rgb(0, 0, 0);"> 传给 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">self</font>`<font style="color:rgb(0, 0, 0);">。</font>

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1779783291938-1035cfab-f4e0-435f-8995-54fa264e278e.png" width="1823" alt="" title="" crop="0,0,1,1" id="u3b0f858c" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

---

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">完整示例：学生类</font>**
```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def introduce(self):
        print(f"大家好，我叫{self.name}，今年{self.age}岁")

    def show_score(self):
        print(f"{self.name}的成绩是{self.score}分")

    def update_score(self, new_score):
        self.score = new_score
        print(f"{self.name}的成绩已更新为{self.score}分")

stu1 = Student("张三", 18, 95)
stu1.introduce()
stu1.show_score()
stu1.update_score(98)
stu1.show_score()
```

<font style="color:rgb(0, 0, 0);">输出：</font>

```python
大家好，我叫张三，今年18岁
张三的成绩是95分
张三的成绩已更新为98分
张三的成绩是98分
```

---

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">类属性和实例属性</font>**
### <font style="color:rgb(0, 0, 0);">实例属性</font>
<font style="color:rgb(0, 0, 0);">实例属性属于具体对象，每个对象可以拥有不同的值。</font>

```python
class Student:
    def __init__(self, name):
        self.name = name

stu1 = Student("张三")
stu2 = Student("李四")

print(stu1.name)
print(stu2.name)
```

<font style="color:rgb(0, 0, 0);">这里的 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">name</font>`<font style="color:rgb(0, 0, 0);"> 就是实例属性。</font>

### <font style="color:rgb(0, 0, 0);">类属性</font>
<font style="color:rgb(0, 0, 0);">类属性属于类本身，所有对象可以共享。</font>

```python
'''
演示类属性
'''

class Student:
    # 类属性
    # 学校
    school = '第一中学'
    # 班费
    class_money = 200
    # 定义对象属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 创建对象
stu1 = Student('张三', 23)
# 通过对象访问类属性
print(stu1.school)
# 也可通过类名访问类属性
print(Student.school)
# 创建对象李四
stu2 = Student('李四', 24)
print(stu2.school)
# 通过类名修改类属性
Student.school = '第二中学'
print('😀'*50)
print(stu1.school)
print(stu2.school)
# 隐藏bug，看似是通过对象修改类属性，其实是添加对象属性
# 其实是给stu1添加对象属性school
# 因为赋值操作具有二义性，被理解为为stu1添加了一个对象属性school
stu1.school = '第三中学'
print('😀'*50)
print(stu2.school)
print(Student.school)
# 如果通过对象直接使用类属性，做修改不会产生二义性
# 学生stu1花费班费20, 但是赋值会创建新的对象的属性
# 相当于 stu1.class_money = stu1.class_money - 20
# 上述表达式，=右侧的stu1.class_money是类属性，左侧的stu1.class_money是对象属性
stu1.class_money -= 20
print('😀'*50)
print(f'班费{Student.class_money}')
print(f'stu1班费{stu1.class_money}')
# stu2没有对象属性class_money,用的是类属性
print(f'stu2班费{stu2.class_money}')
```

<font style="color:rgb(0, 0, 0);">输出：</font>

```python
第一中学
第一中学
第一中学
😀😀😀😀😀😀😀😀😀
第二中学
第二中学
😀😀😀😀😀😀😀😀😀
第二中学
第二中学
😀😀😀😀😀😀😀😀😀
班费200
stu1班费180
stu2班费200
```

### <font style="color:rgb(0, 0, 0);">类属性和实例属性的区别</font>
| **<font style="color:rgb(0, 0, 0);">类型</font>** | **<font style="color:rgb(0, 0, 0);">所属对象</font>** | **<font style="color:rgb(0, 0, 0);">是否共享</font>** | **<font style="color:rgb(0, 0, 0);">示例</font>**            |
| :------------------------------------------------ | :---------------------------------------------------- | :---------------------------------------------------- | :----------------------------------------------------------- |
| <font style="color:rgb(0, 0, 0);">实例属性</font> | <font style="color:rgb(0, 0, 0);">具体对象</font>     | <font style="color:rgb(0, 0, 0);">不共享</font>       | `<font style="color:rgb(239, 112, 96);">self.name</font>`    |
| <font style="color:rgb(0, 0, 0);">类属性</font>   | <font style="color:rgb(0, 0, 0);">类本身</font>       | <font style="color:rgb(0, 0, 0);">共享</font>         | `<font style="color:rgb(239, 112, 96);">Student.school</font>` |


### <font style="color:rgb(0, 0, 0);">示例：统计学生人数</font>
```python
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
```

<font style="color:rgb(0, 0, 0);">输出：</font>

总共创建了2个实例

---

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">封装</font>**
### <font style="color:rgb(0, 0, 0);">什么是封装</font>
<font style="color:rgb(0, 0, 0);">封装是指把数据和操作数据的方法放在一起，并对外隐藏不希望直接访问的细节。</font>

<font style="color:rgb(0, 0, 0);">简单理解：</font>

<font style="color:black;background-color:rgb(255, 249, 249);">不让外部随便修改对象内部的数据，而是通过方法来控制访问。</font>

<font style="color:rgb(0, 0, 0);">例如，学生成绩不应该被随意设置为负数。</font>

### <font style="color:rgb(0, 0, 0);">未封装的问题</font>
```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

stu = Student("张三", 90)
stu.score = -100
print(stu.score)
```

<font style="color:rgb(0, 0, 0);">输出：</font>

-100

<font style="color:rgb(0, 0, 0);">这显然不合理。</font>

### <font style="color:rgb(0, 0, 0);">使用私有属性</font>
<font style="color:rgb(0, 0, 0);">在 Python 中，属性名前面加两个下划线，表示私有属性。</font>

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            print("成绩必须在0到100之间")

stu = Student("张三", 90)
print(stu.get_score())

stu.set_score(95)
print(stu.get_score())

stu.set_score(-100)
print(stu.get_score())
```

<font style="color:rgb(0, 0, 0);">输出：</font>

```python
90
95
成绩必须在0到100之间
95
```

### <font style="color:rgb(0, 0, 0);">封装的好处</font>
1. <font style="color:black;">保护数据安全。</font>
2. <font style="color:black;">控制数据修改规则。</font>
3. <font style="color:black;">降低外部代码对内部实现的依赖。</font>
4. <font style="color:black;">让类的使用更加清晰。</font>



## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">继承</font>**
### <font style="color:rgb(0, 0, 0);">本质理解（结合哲学）</font>
<font style="color:rgb(0, 0, 0);">继承本质是：</font>**<font style="color:rgb(0, 0, 0);">共性 + 个性</font>**

<font style="color:rgb(0, 0, 0);">例如：</font>

<font style="color:rgb(0, 0, 0);">生物 → 动物 → 哺乳动物 → 人类</font>

+ <font style="color:black;">上层：共性</font>
+ <font style="color:black;">下层：个性</font>



### <font style="color:rgb(0, 0, 0);">继承核心作用</font>
1. <font style="color:black;">代码复用</font>
2. <font style="color:black;">表达层级关系</font>
3. <font style="color:black;">提升扩展能力</font>



### <font style="color:rgb(0, 0, 0);">基本语法</font>
```python
class 父类:
    pass

class 子类(父类):
    pass
```

---

### <font style="color:rgb(0, 0, 0);">经典案例（强化）</font>
```python
'''
演示类的继承
'''
# 父类
class Person(object):
    def eat(self):
        print('吃东西')
    def sleep(self):
        print('睡觉')

# 子类, 拥有了父类的属性和方法
class Student(Person):
    pass

# 教师类
class Teacher(Person):
    pass

s1 = Student()
# 拥有了父类的属性和方法
s1.eat()
s1.sleep()

t1 = Teacher()
t1.eat()
t1.sleep()

# 首先去Student中查找，如果Student中没有去Person查找，如果Person也没有去Object查找
# 如果最后都没有找到该方法，则报错
# s1.play_game()
# 打印Student对象的方法查找顺序
# (<class '__main__.Student'>, <class '__main__.Person'>, <class 'object'>)
print(Student.__mro__)
```

---

`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">__init__</font>`<font style="color:rgb(0, 0, 0);">流程说明</font>

```python
# 动物类
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 猫类
class Cat(Animal):
    pass

# 调用的是Animal的__init__方法
cat = Cat('小猫',5)
```

图示: 

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1780021136916-12461c03-c164-4c67-8391-29c87e6b93a2.png" width="934" alt="" title="" crop="0,0,1,1" id="JxOwd" class="ne-image">



**<font style="color:rgb(0, 0, 0);">方法覆盖</font>**

```python
# 动物类
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 猫类
class Cat(Animal):
    pass

class Dog(Animal):
    # Dog类的__init__方法会覆盖掉父类同名的__init__方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = 'dog'

# 调用的是Animal的__init__方法
cat = Cat('小猫',5)
# 创建Dog实例
dog = Dog('小狗',6)
print(dog.type)
```

**<font style="color:rgb(0, 0, 0);"></font>**

**<font style="color:rgb(0, 0, 0);">通过子类调用父类方法</font>**

```python
# 动物类
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Bird(Animal):
    # 将共性属性的初始化放入Animal，调用Animal的__init__方法
    # 将Bird特性的属性的初始化放入Bird
    def __init__(self, name, age, type):
        # 调用父类的__init__方法
        super().__init__(name, age)
        # 特性属性的初始化
        self.type = type

# 创建鸟类实例
bird =  Bird('小鸟',200,'金雕')
print(bird.type)
print(bird.age)
print(bird.name)
```

### <font style="color:rgb(0, 0, 0);">私有成员说明（进阶重点）</font>
<font style="color:rgb(0, 0, 0);">父类私有方法：</font>

```python
def __private_func(self):
    pass
```

<font style="color:rgb(0, 0, 0);">特点：</font>

+ <font style="color:black;">子类不能直接访问</font>
+ <font style="color:black;">本质被改名：_类名__方法名</font>

---

```python
# 动物类
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 私有方法, 咆哮
    def __roar(self):
        print('野性的呼唤，原始觉醒')


class Bird(Animal):
    # 将共性属性的初始化放入Animal，调用Animal的__init__方法
    # 将Bird特性的属性的初始化放入Bird
    def __init__(self, name, age, type):
        # 调用父类的__init__方法
        super().__init__(name, age)
        # 特性属性的初始化
        self.type = type


# 创建鸟类实例
bird =  Bird('小鸟',200,'金雕')
print(bird.type)
print(bird.age)
print(bird.name)
print('😔'*50)
# 在Bird的__dict__看不到从父类继承的方法
print(Bird.__dict__)
# 在Animal中看到私有方法__roar改名了_Animal__roar
print(Animal.__dict__)
# 可以理解为_Animal__roar被Bird类继承了
# 根据__mro__顺序去查找，先查找Bird类，没有_Animal__roar
# 继续去上一级Animal查找，找到_Animal__roar
bird._Animal__roar()
```



### <font style="color:rgb(0, 0, 0);">多继承</font>
<font style="color:rgb(0, 0, 0);">Python 支持多继承：</font>

```python
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

c = C()
c.show()
```

<font style="color:rgb(0, 0, 0);">输出：</font>

A

<font style="color:rgb(0, 0, 0);">为什么不是 B？</font>

<font style="color:rgb(0, 0, 0);">因为 Python 会按照 </font>**<font style="color:rgb(0, 0, 0);">MRO（Method Resolution Order，方法解析顺序）</font>**<font style="color:rgb(0, 0, 0);"> 查找方法。</font>

<font style="color:rgb(0, 0, 0);">查看 MRO：</font>

print(C.__mro__)

<font style="color:rgb(0, 0, 0);">输出类似：</font>

(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

<font style="color:rgb(0, 0, 0);">所以查找顺序是：</font>

C → A → B → object

**<font style="color:rgb(0, 0, 0);">小结</font>**

+ <font style="color:black;">多继承时，方法查找不是随便找的</font>
+ <font style="color:black;">Python 按照 MRO 顺序查找方法</font>
+ `<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">类名.__mro__</font>`<font style="color:black;"> 可以查看查找顺序</font>
+ <font style="color:black;">初学者应先掌握单继承，再理解多继承和 MRO</font>

---

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">方法重写</font>**
### <font style="color:rgb(0, 0, 0);">什么是方法重写</font>
<font style="color:rgb(0, 0, 0);">如果子类对父类的方法不满意，可以在子类中重新定义同名方法。</font>

<font style="color:rgb(0, 0, 0);">这叫方法重写。</font>

```python
'''
演示方法重写
'''

class Animal(object):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('动物咆哮')

    def introduce(self):
        print(f'我是一只动物,我叫{self.name}')

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 子类重新实现了父类的introduce方法，
    # 将来子类对象调用introduce，会触发子类的introduce方法
    def introduce(self):
        print(f'我是一只小狗，我叫{self.name}')

    def speak(self):
        print('小狗汪汪汪叫...')

dg = Dog('旺财',2)
# 子类对象调用自己的introduce
dg.introduce()
dg.speak()

# 子类对象具体调用哪个类的方法，取决于mro的查找顺序
print(Dog.__mro__)

```

<font style="color:rgb(0, 0, 0);">输出：</font>

```python
我是一只小狗，我叫旺财
小狗汪汪汪叫...
(<class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>)

```

### <font style="color:rgb(0, 0, 0);">为什么需要方法重写</font>
<font style="color:rgb(0, 0, 0);">不同子类虽然拥有相同的方法名，但具体表现可能不同。</font>

<font style="color:rgb(0, 0, 0);">例如：</font>

+ <font style="color:black;">狗会叫，但叫声是“汪汪”。</font>
+ <font style="color:black;">猫会叫，但叫声是“喵喵”。</font>
+ <font style="color:black;">鸭子会叫，但叫声是“嘎嘎”。</font>

<font style="color:rgb(0, 0, 0);">这为多态打下了基础。</font>

---

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">调用父类方法</font>**
<font style="color:rgb(0, 0, 0);">有时子类并不是完全替换父类方法，而是在父类原有功能基础上增加新功能。</font>

<font style="color:rgb(0, 0, 0);">这时可以使用 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">super()</font>`<font style="color:rgb(0, 0, 0);">。</font>

<font style="color:rgb(0, 0, 0);">正确完整代码：</font>

```python
'''
子类调用父类的方法
'''

'''
子类调用父类的方法
方法1
super().方法名(参数1,参数2,参数3...)
方式2
父类名.方法名(self,参数1,参数2,参数3...)
'''
class Animal:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f'我是一只动物,我叫{self.name}')

class Dog(Animal):
    def __init__(self, name,color):
        super().__init__(name)
        self.color = color
    def introduce(self):
        super().introduce()
        print(f'我的颜色是{self.color}')

dog = Dog('旺财','蓝色')
dog.introduce()

```

<font style="color:rgb(0, 0, 0);">输出：</font>

```python
我是一只动物，我叫旺财
我的颜色是黄色
```

<font style="color:rgb(0, 0, 0);">说明：</font>

+ `<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">super().__init__(name)</font>`<font style="color:black;"> 调用了父类的构造方法。</font>
+ `<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">super().introduce()</font>`<font style="color:black;"> 调用了父类的 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">introduce</font>`<font style="color:black;"> 方法。</font>

<font style="color:rgb(0, 0, 0);">说明：</font>

+ `<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">super().__init__(name)</font>`<font style="color:black;"> 调用了父类的构造方法。</font>
+ `<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">super().introduce()</font>`<font style="color:black;"> 调用了父类的 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">introduce</font>`<font style="color:black;"> 方法。</font>

<img src="https://cdn.nlark.com/yuque/0/2026/png/27211935/1780585883462-62adac03-59b5-4d21-a5d8-68e284a1f7f1.png" width="1695" alt="" title="" crop="0,0,1,1" id="u2feaa115" class="ne-image" style="color: rgb(0, 0, 0); font-size: 16px">

**<font style="color:rgb(0, 0, 0);">另外一种调用方式</font>**

```python
'''
子类调用父类的方法
'''

'''
子类调用父类的方法
方法1
super().方法名(参数1,参数2,参数3...)
方式2
父类名.方法名(self,参数1,参数2,参数3...)
'''
class Animal:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f'我是一只动物,我叫{self.name}')

class Dog(Animal):
    def __init__(self, name,color):
        Animal.__init__(self, name)
        self.color = color
    def introduce(self):
        Animal.introduce(self)
        print(f'我的颜色是{self.color}')

dog = Dog('旺财','蓝色')
dog.introduce()
```

<font style="color:black;">  
</font><font style="color:black;"> </font>

## 多继承风险
```python
'''
需求:
1. 定义一个汽车Car基类，构造方法__init__接受汽车的名字和颜色

2. 定义GasolineCar类，继承自Car, 实现__init__方法，接受参数名字，颜色
   以及充能方式
   实现run方法，输出耗油运行
   实现energy方法，输出默认使用燃油
   
3. 定义ElectricCar类, 实现__init__方法，接受参数名字，颜色
   以及充能方式
   继承自Car，实现run方法，输出耗电运行
   实现energy方法，输出默认使用电能
   
4. 定义HybridCar类，同时继承自ElectricCar,GasolineCar，
实现run方法，油电混动运行

5.  实例化一个HybridCar对象，调用energy以及run方法，看看输出

'''
```

**代码**

```python
'''
演示多继承隐患
'''

'''
需求:
1. 定义一个汽车Car基类，构造方法__init__接受汽车的名字和颜色

2. 定义GasolineCar类，继承自Car, 实现__init__方法，接受参数名字，颜色
    以及充能方式
    实现run方法，输出耗油运行
    实现energy方法，输出默认使用燃油

3. 定义ElectricCar类, 实现__init__方法，接受参数名字，颜色
    以及充能方式
    继承自Car，实现run方法，输出耗电运行
    实现energy方法，输出默认使用电能

4. 定义HybridCar类，同时继承自ElectricCar,GasolineCar，
实现run方法，油电混动运行

5.  实例化一个HybridCar对象，调用energy以及run方法，看看输出

'''
# 1. 定义一个汽车Car基类，构造方法__init__接受汽车的名字和颜色
class Car(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

# 2. 定义GasolineCar类，继承自Car, 实现__init__方法，接受参数名字，颜色
#     以及充能方式
class GasolineCar(Car):
    def __init__(self, name, color,energy_type):
        super().__init__(name, color)
        self.energy_type = energy_type

    def run(self):
        print('耗油运行')

    def energy(self):
        print('默认使用燃油')

# 3. 定义ElectricCar类, 实现__init__方法，接受参数名字，颜色
#     以及充能方式

class ElectricCar(Car):
    def __init__(self, name, color, energy_type):
        super().__init__(name, color)
        self.energy_type = energy_type

    def run(self):
        print('耗电运行')

    def energy(self):
        print('默认使用电能')

# 4. 定义HybridCar类，同时继承自ElectricCar,GasolineCar
class HybridCar(ElectricCar, GasolineCar):
    def __init__(self, name, color, energy_type):
        self.name = name
        self.color = color
        self.energy_type = energy_type

    def run(self):
        print('油电混动运行')


if __name__ == '__main__':
    # gc = GasolineCar('宝马','白色','燃油')
    # gc.run()
    # gc.energy()
    #
    # ec = ElectricCar('比亚迪','黑色','电能')
    # ec.run()
    # ec.energy()
    print(HybridCar.__mro__)
    hy_car = HybridCar('比亚迪','黑色','油电混动')
    hy_car.run()
    hy_car.energy()
```

:::info
如果HybridCar没有实现`__init__`方法, 将会导致通过mro顺序调用上一级的`__init__`方法

而上一级是ElectricCar类，ElectricCar类的`__init__`方法内部又调用了`super()`所以会通过mro找到上一级

这个上一级其实是GasolineCar, 进而造成`__init__`调用参数不匹配而失败

规避的方式第一种即使实现HybridCar的`__init__方法`

第二种方式就是通过父类名.方法名方式显示调用

:::

**第二种方式**

```python
'''
演示多继承隐患
'''

'''
需求:
1. 定义一个汽车Car基类，构造方法__init__接受汽车的名字和颜色

2. 定义GasolineCar类，继承自Car, 实现__init__方法，接受参数名字，颜色
    以及充能方式
    实现run方法，输出耗油运行
    实现energy方法，输出默认使用燃油

3. 定义ElectricCar类, 实现__init__方法，接受参数名字，颜色
    以及充能方式
    继承自Car，实现run方法，输出耗电运行
    实现energy方法，输出默认使用电能

4. 定义HybridCar类，同时继承自ElectricCar,GasolineCar，
实现run方法，油电混动运行

5.  实例化一个HybridCar对象，调用energy以及run方法，看看输出

'''
# 1. 定义一个汽车Car基类，构造方法__init__接受汽车的名字和颜色
class Car(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

# 2. 定义GasolineCar类，继承自Car, 实现__init__方法，接受参数名字，颜色
#     以及充能方式
class GasolineCar(Car):
    def __init__(self, name, color,energy_type):
        Car.__init__(self, name, color)
        self.energy_type = energy_type

    def run(self):
        print('耗油运行')

    def energy(self):
        print('默认使用燃油')

# 3. 定义ElectricCar类, 实现__init__方法，接受参数名字，颜色
#     以及充能方式

class ElectricCar(Car):
    def __init__(self, name, color, energy_type):
        Car.__init__(self, name, color)
        self.energy_type = energy_type

    def run(self):
        print('耗电运行')

    def energy(self):
        print('默认使用电能')

# 4. 定义HybridCar类，同时继承自ElectricCar,GasolineCar
class HybridCar(ElectricCar, GasolineCar):

    def run(self):
        print('油电混动运行')


if __name__ == '__main__':
    # gc = GasolineCar('宝马','白色','燃油')
    # gc.run()
    # gc.energy()
    #
    # ec = ElectricCar('比亚迪','黑色','电能')
    # ec.run()
    # ec.energy()
    print(HybridCar.__mro__)
    hy_car = HybridCar('比亚迪','黑色','油电混动')
    hy_car.run()
    hy_car.energy()
```

> **结论**
>
> 当使用多继承时，子类调用父类的方法，一定要用父类名.方法名(参数1,参数2...)
>

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">多态</font>**
### <font style="color:rgb(0, 0, 0);">什么是多态</font>
<font style="color:rgb(0, 0, 0);">多态是指不同对象调用相同方法时，表现出不同的行为。</font>

<font style="color:rgb(0, 0, 0);">核心特点：</font>

<font style="color:black;background-color:rgb(255, 249, 249);">相同的方法名，不同的实现效果。</font>

```python
'''
演示多态用法
'''

'''
用一个父类对象引用子类对象，通过父类对象调用方法，能够触发子类对象的方法
这种机制就是多态

多态必要条件:
1. 必须要有继承关系
2. 子类重写父类方法
3. 父类对象引用子类对象
'''

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'我叫{self.name}, 通过动物咆哮')


class Dog(Animal):
    def speak(self):
        print(f'我叫{self.name}，叫声汪汪汪')

class Cat(Animal):
    def speak(self):
        print(f'我叫{self.name}，叫喵喵喵')

class Duck(Animal):
    def speak(self):
        print(f'我叫{self.name}，叫声嘎嘎嘎')

def animal_speak(animal:Animal):
    animal.speak()

if __name__ == '__main__':
    animal_speak(Animal('动物',8))
    animal_speak(Dog('小狗',7))
    animal_speak(Cat('小猫',4))
    animal_speak(Duck('鸭子',3))

```

<font style="color:rgb(0, 0, 0);">输出：</font>

```python
我叫动物, 通过动物咆哮
我叫小狗，叫声汪汪汪
我叫小猫，叫喵喵喵
我叫鸭子，叫声嘎嘎嘎
```

### <font style="color:rgb(0, 0, 0);">多态的优势</font>
<font style="color:rgb(0, 0, 0);">多态可以让代码更加灵活。可以将抽象类的定义和具体类的实现分离，实现开发的解耦合</font>

<font style="color:rgb(0, 0, 0);">同时使用平台，不用随着逻辑的变化而修改，将来只要扩充子类类型即可。</font>

<font style="color:rgb(0, 0, 0);">符合高内聚和低耦合的思想。</font>

<font style="color:rgb(0, 0, 0);">例如：</font>

```python
def make_sound(animal):
    animal.speak()

make_sound(Dog())
make_sound(Cat())
make_sound(Duck())
```

<font style="color:rgb(0, 0, 0);">这个函数不关心传入的是狗、猫还是鸭子，只关心对象有没有 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">speak</font>`<font style="color:rgb(0, 0, 0);"> 方法。</font>

**<font style="color:rgb(0, 0, 0);">like方式继承</font>**

<font style="color:rgb(0, 0, 0);">like方式就是像的意思，不要求类一定和某一个类实现继承关系，只要这个类具备相似的方法即可。</font>

---

```python
'''
演示like继承
'''

class Bird:
    def fly(self):
        print("i can fly")
# is 方式继承，Angle一定是Bird
class Angle(Bird):
    def fly(self):
        print('鹰会飞')
# like 方式继承， Go语言特性interface
class Plane:
    def fly(self):
        print('飞机也会飞')

def func_test_bird(bird:Bird):
    bird.fly()

if __name__ == '__main__':
    angle = Angle()
    func_test_bird(angle)
    plane = Plane()
    func_test_bird(plane)
```

**<font style="color:rgb(0, 0, 0);">王者荣耀换肤案例</font>**

```python
'''
王者荣耀换肤案例
'''
from pyarrow._flight import BasicAuth


# 皮肤基类
class BaseSkin:
    def show(self):
        pass

class XHOriginSkin(BaseSkin):
    def show(self):
        print('没错，我就是呼唤胜利的男神')

class WXJFSkin(BaseSkin):
    def show(self):
        print('我就差一点了,快来砍我')

class BaseHero:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        # 皮肤列表
        self.skins = []

class XHHero(BaseHero):
    def __init__(self,name,gender):
        super().__init__(name,gender)
        # 初始化人物原皮
        skin:BaseSkin = XHOriginSkin()
        self.skins.append(skin)
        # 上一次展示的皮肤
        self.last_skin_index = 0

    # 展示人物
    def show(self):
        self.skins[self.last_skin_index].show()

    # 购买皮肤
    def buy_skin(self, skin:BaseSkin):
        self.skins.append(skin)

    def change_skin(self,index):
        if index >= len(self.skins):
            return
        self.skins[index].show()
        self.last_skin_index = index

if __name__ == '__main__':
    xh_hero = XHHero('夏侯惇','男')
    xh_hero.show()
    # 购买皮肤
    xh_hero.buy_skin(WXJFSkin())
    # 换肤
    xh_hero.change_skin(1)
    # 展示英雄
    xh_hero.show()

```

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">特殊方法</font>**
<font style="color:rgb(0, 0, 0);">Python 中有一些以双下划线开头和结尾的方法，称为特殊方法，也叫魔术方法。</font>

### `<font style="color:rgb(239, 112, 96);">__str__</font>`
<font style="color:rgb(0, 0, 0);">当使用 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">print()</font>`<font style="color:rgb(0, 0, 0);"> 打印对象时，会自动调用对象的 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">__str__</font>`<font style="color:rgb(0, 0, 0);"> 方法。</font>

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"学生姓名：{self.name}，年龄：{self.age}"

stu = Student("张三", 18)
print(stu)
```

<font style="color:rgb(0, 0, 0);">输出：</font>

学生姓名：张三，年龄：18

<font style="color:rgb(0, 0, 0);">如果不定义 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">__str__</font>`<font style="color:rgb(0, 0, 0);">，直接打印对象通常会看到对象的内存地址信息，不利于阅读。</font>

### `<font style="color:rgb(239, 112, 96);">__repr__</font>`
`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">__repr__</font>`<font style="color:rgb(0, 0, 0);"> 更偏向开发者调试使用，通常返回一个更明确的对象描述。</font>

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(name={self.name!r}, age={self.age!r})"

stu = Student("张三", 18)
print(repr(stu))
```

<font style="color:rgb(0, 0, 0);">输出：</font>

Student(name='张三', age=18)

---

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">类方法和静态方法</font>**
### <font style="color:rgb(0, 0, 0);">实例方法</font>
<font style="color:rgb(0, 0, 0);">最常见的方法是实例方法，第一个参数是 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">self</font>`<font style="color:rgb(0, 0, 0);">。</font>

```python
class Student:
    def introduce(self):
        print("我是学生")
```

<font style="color:rgb(0, 0, 0);">实例方法通常需要访问对象本身的数据。</font>

### <font style="color:rgb(0, 0, 0);">类方法</font>
<font style="color:rgb(0, 0, 0);">类方法使用 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">@classmethod</font>`<font style="color:rgb(0, 0, 0);"> 装饰器，第一个参数通常是 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">cls</font>`<font style="color:rgb(0, 0, 0);">，表示当前类。</font>

```python
class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    @classmethod
    def show_count(cls):
        print(f"当前学生人数：{cls.count}")

Student("张三")
Student("李四")
Student.show_count()
```

<font style="color:rgb(0, 0, 0);">输出：</font>

当前学生人数：2

### <font style="color:rgb(0, 0, 0);">静态方法</font>
<font style="color:rgb(0, 0, 0);">静态方法使用 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">@staticmethod</font>`<font style="color:rgb(0, 0, 0);"> 装饰器。</font>

<font style="color:rgb(0, 0, 0);">它不需要访问对象，也不需要访问类。</font>

```python
class MathTool:
    @staticmethod
    def add(a, b):
        return a + b

print(MathTool.add(3, 5))
```

<font style="color:rgb(0, 0, 0);">输出：</font>

8

### <font style="color:rgb(0, 0, 0);">三种方法对比</font>
| **<font style="color:rgb(0, 0, 0);">方法类型</font>** | **<font style="color:rgb(0, 0, 0);">第一个参数</font>** | **<font style="color:rgb(0, 0, 0);">是否访问实例属性</font>** | **<font style="color:rgb(0, 0, 0);">是否访问类属性</font>** |
| :---------------------------------------------------- | :------------------------------------------------------ | :----------------------------------------------------------- | :---------------------------------------------------------- |
| <font style="color:rgb(0, 0, 0);">实例方法</font>     | `<font style="color:rgb(239, 112, 96);">self</font>`    | <font style="color:rgb(0, 0, 0);">可以</font>                | <font style="color:rgb(0, 0, 0);">可以</font>               |
| <font style="color:rgb(0, 0, 0);">类方法</font>       | `<font style="color:rgb(239, 112, 96);">cls</font>`     | <font style="color:rgb(0, 0, 0);">不直接访问</font>          | <font style="color:rgb(0, 0, 0);">可以</font>               |
| <font style="color:rgb(0, 0, 0);">静态方法</font>     | <font style="color:rgb(0, 0, 0);">无固定参数</font>     | <font style="color:rgb(0, 0, 0);">不访问</font>              | <font style="color:rgb(0, 0, 0);">不访问</font>             |


---

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">面向对象综合案例：银行账户</font>**
### <font style="color:rgb(0, 0, 0);">需求分析</font>
<font style="color:rgb(0, 0, 0);">设计一个银行账户类 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">BankAccount</font>`<font style="color:rgb(0, 0, 0);">，要求：</font>

1. <font style="color:black;">每个账户有账户名和余额。</font>
2. <font style="color:black;">可以存款。</font>
3. <font style="color:black;">可以取款。</font>
4. <font style="color:black;">余额不能小于 0。</font>
5. <font style="color:black;">可以查看账户信息。</font>

### <font style="color:rgb(0, 0, 0);">代码实现</font>
```python
'''
银行存款案例
'''

class BankAccount:
    def __init__(self, owner,balance=0):
        # 账户
        self.__owner = owner
        # 余额
        self.__balance = balance

    # 存款
    def deposit(self,amount):
        if amount <=0 :
            print(f'存款金额必须大于0')
            return
        # 存款
        self.__balance += amount

    # 取款
    def withdraw(self,amount):
        if amount <= 0:
            print(f'取款金额必须大于0')
            return

        # 判断余额是否充足
        if amount > self.__balance:
            print(f'取款的金额必须大于余额')
            return
        # 扣款
        self.__balance -= amount

    # 获取账号名
    def get_owner(self):
        return self.__owner

    #获取余额
    def get_balance(self):
        return self.__balance

    # 打印账户名和存取款信息
    def show_info(self):
        print(f'账户名: {self.__owner}, 余额: {self.__balance}')

if __name__ == '__main__':
    account = BankAccount('zack',1000)
    account.show_info()
    account.deposit(100)
    account.show_info()
    account.withdraw(300)
    account.show_info()
    account.withdraw(900)
    account.show_info()
```

<font style="color:rgb(0, 0, 0);">输出：</font>

```python
账户名: zack, 余额: 1000
账户名: zack, 余额: 1100
账户名: zack, 余额: 800
取款的金额必须大于余额
账户名: zack, 余额: 800
```

### <font style="color:rgb(0, 0, 0);">案例讲解重点</font>
<font style="color:rgb(0, 0, 0);">这个案例同时体现了：</font>

1. <font style="color:black;">类和对象。</font>
2. <font style="color:black;">构造方法。</font>
3. <font style="color:black;">实例属性。</font>
4. <font style="color:black;">私有属性。</font>
5. <font style="color:black;">封装思想。</font>
6. <font style="color:black;">方法对数据的控制。</font>

---

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">课堂案例：图书管理</font>**
### <font style="color:rgb(0, 0, 0);">需求</font>
<font style="color:rgb(0, 0, 0);">设计一个图书管理系统</font>

1. <font style="color:black;">展示菜单</font>
2. <font style="color:black;">添加图书，包括作者，书名，价格，编号，数量</font>
3. <font style="color:black;">删除图书，根据编号和数量删除</font>
4. <font style="color:black;">修改图书信息</font>
5. <font style="color:black;">根据编号查看图书信息</font>
6. <font style="color:black;">将图书信息存储到本地文件</font>
7. <font style="color:black;">从本地文件将图书信息加载到内存</font>
8. <font style="color:black;">分页加载图书信息列表，根据页码加载</font>

### <font style="color:rgb(0, 0, 0);">代码示例</font>
```python
'''
演示图书管理系统开发
'''

'''
思路:
1. 定义图书类，属性 书名，作者，编号，数量
2. 定义图书管理类，管理图书，将图书放入字典中，
key为图书编号，value为这个字典
3. 在图书管理类中添加各种方法
4. 将图书信息写入文件
5. 将文件内容加载到内存中
'''
import json
import os

class Book:
    def __init__(self,title,author,price,isbn,count):
        self.title = title
        self.author = author
        self.price = price
        self.isbn = isbn
        self.count = count

    def to_dict(self):
        return {
            'book_id': self.isbn,
            'name': self.title,
            'author': self.author,
            'price': self.price,
            'count': self.count
        }
    @staticmethod
    def from_dict(book_dict):
        return Book(
            title=book_dict['name'],
            author=book_dict['author'],
            price=book_dict['price'],
            isbn=book_dict['book_id'],
            count=book_dict['count']
        )

class BookManager:
    instance = None
    def __new__(cls,file_path):
        if BookManager.instance is None:
            BookManager.instance = super().__new__(cls)
        return BookManager.instance

    def __init__(self,file_path):
        self.books = {}
        self.file_path = file_path
        self.__load_from_file()

    def __load_from_file(self):
        if not os.path.exists(self.file_path):
            print('文件不存在，暂无数据')
            return
        with open(self.file_path,'r',encoding='utf-8') as f:
            # data是一个列表，每个元素是字典
            data = json.load(f)

        self.books = {item['book_id']:Book.from_dict(item) for item in data}
        print('图书信息已经加载')

    def showmenu(self):
        while True:
            print('*'*10,'图书馆里系统','*'*10)
            print('1.添加图书')
            print('2.删除图书')
            print('3.修改图书信息')
            print('4.根据编号查看图书信息')
            print('5.将图书信息存储到本地')
            print('6.通过页码查看图书列表')
            print('7.输入quit退出系统')
            input_num = input('请输入您的操作编号: ')
            if input_num == '7' or input_num == 'quit':
                print(f'系统退出')
                break

            if input_num == '1':
                self.add_book()
                continue

            if input_num == '2':
                self.del_book()
                continue

            if input_num == '3':
                self.modify_book()
                continue

            if input_num == '4':
                self.check_book()
                continue

            if input_num == '5':
                self.save_to_file()
                continue

            if input_num == '6':
                self.show_list()
                continue

            print('非法操作，请继续!!!')

    def add_book(self):
        book_id = input('请输入图书编号: ')
        count = int(input('请输入录入数量: '))
        name = input('请输入书名: ')
        author = input('请输入作者: ')
        price = float(input('请输入价格: '))
        book = Book(title=name,author=author,
                    price=price,isbn=book_id,count=count)
        self.books[book_id] = book
        print('图书添加成功!!!')

    def __find_book_by_id(self,book_id):
        if book_id not in self.books:
            print('没有找到该图书!')
            return None
        return self.books[book_id]

    def del_book(self):
        book_id = input('请输入要删除的图书编号: ')
        book = self.__find_book_by_id(book_id)
        if not book:
            return
        del_count = int(input('请输入删除的数量: '))
        if del_count < book.count:
            book.count -= del_count
            print('图书数量删除成功')
            return

        del self.books[book_id]
        print('该图书已经全部删除')

    def check_book(self):
        book_id = input('请输入要删除的图书编号: ')
        book = self.__find_book_by_id(book_id)
        if not book:
            return

        print(f'图书信息:\n书名:{book.title}\n'
              f'作者:{book.author}\n'
              f'价格:{book.price}\n'
              f'编号:{book.isbn}\n'
              f'数量:{book.count}')

    def modify_book(self):
        book_id = input('请输入要删除的图书编号: ')
        book = self.__find_book_by_id(book_id)
        if not book:
            return

        new_name = input('请输入要改成的名字: ')
        new_price = float(input('请输入要改成的价格: '))
        new_author = input('请输入图书的作者: ')
        new_count = int(input('请输入图书的数量: '))
        book.title = new_name
        book.author = new_author
        book.price = new_price
        book.count = new_count
        print(f'图书信息修改成功:\n')

    def show_list(self):
        if not self.books:
            print('暂无图书信息')
            return

        page = int(input('请输入查看的页码: '))
        page_size = 5
        start = (page-1)*page_size
        end = start+page_size
        book_list = list(self.books.values())
        page_books = book_list[start:end]
        if not page_books:
            print('该页没有数据')
            return

        for book in page_books:
            print(
                f"编号：{book.isbn} | "
                f"书名：{book.title} | "
                f"作者：{book.author} | "
                f"价格：{book.price} | "
                f"数量：{book.count}"
            )

    def save_to_file(self):
        data = [book.to_dict() for book in self.books.values()]
        print(data)
        with open(self.file_path, 'w', encoding='utf-8') as f:
            # 参1必须是列表，字典，字符串，正数，浮点，bool，None Python自带的内置类型
            # 参2是要写入的文件
            # 参3是中文是否需要转义
            # 参4 是否格式化json，美观输出
            json.dump(data,f,ensure_ascii=False,indent=4)
        print('图书信息已保存')



if __name__ == '__main__':
    m = BookManager('./book_datas/books.json')
    m.showmenu()
    #m2 = BookManager()
    #print(f'm is m2 : {m is m2}')

```

---

## **<font style="color:rgb(255, 255, 255);background-color:rgb(239, 112, 96);">课后作业</font>**
### <font style="color:rgb(0, 0, 0);">作业 1：商品类</font>
<font style="color:rgb(0, 0, 0);">定义一个 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">Product</font>`<font style="color:rgb(0, 0, 0);"> 类，要求：</font>

1. <font style="color:black;">有商品名称、价格、库存。</font>
2. <font style="color:black;">价格和库存不能为负数。</font>
3. <font style="color:black;">有展示商品信息的方法。</font>
4. <font style="color:black;">有购买商品的方法。</font>
5. <font style="color:black;">购买时库存减少。</font>
6. <font style="color:black;">如果库存不足，提示“库存不足”。</font>

### <font style="color:rgb(0, 0, 0);">作业 2：学生管理小系统</font>
<font style="color:rgb(0, 0, 0);">定义一个 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">Student</font>`<font style="color:rgb(0, 0, 0);"> 类，包含：</font>

+ <font style="color:black;">姓名</font>
+ <font style="color:black;">年龄</font>
+ <font style="color:black;">成绩</font>

<font style="color:rgb(0, 0, 0);">再定义一个 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">StudentManager</font>`<font style="color:rgb(0, 0, 0);"> 类，包含：</font>

+ <font style="color:black;">添加学生</font>
+ <font style="color:black;">删除学生</font>
+ <font style="color:black;">查找学生</font>
+ <font style="color:black;">展示所有学生</font>

### <font style="color:rgb(0, 0, 0);">作业 3：动物园案例</font>
<font style="color:rgb(0, 0, 0);">定义父类 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">Animal</font>`<font style="color:rgb(0, 0, 0);">，包含：</font>

+ <font style="color:black;">名字</font>
+ <font style="color:black;">年龄</font>
+ `<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">eat()</font>`<font style="color:black;"> 方法</font>
+ `<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">speak()</font>`<font style="color:black;"> 方法</font>

<font style="color:rgb(0, 0, 0);">定义子类：</font>

+ `<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">Dog</font>`
+ `<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">Cat</font>`
+ `<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">Bird</font>`

<font style="color:rgb(0, 0, 0);">要求每个子类重写 </font>`<font style="color:rgb(239, 112, 96);background-color:rgba(27, 31, 35, 0.05);">speak()</font>`<font style="color:rgb(0, 0, 0);"> 方法。</font>

  