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