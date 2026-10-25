import csv
import json
'''
读取学生信息
返回列表[],每个元素是json格式，存储学生信息
'''
def read_students(filename):
    #使用Json文件来进行读取
    students = []
    try:
        with open(filename,'r',encoding='utf-8-sig') as f:
            #cvs包中的用法 ,将文件中的信息转化为列表，并且列表中的每一个元素都是字典
            reader = csv.DictReader(f)
            for row in reader:
                students.append(
                    {'name':row['name'],
                     'age':row['age'],
                     'score':row['score'],
                     })
        return students
                # name = row['name']
                # age = row['age']
                # score = row['score']
                # print(name,age,score)

    except Exception as e:
        print(f'文件读取错误，error is {e}')
        return []


#计算每一个学生的平均分
def calculate_average_score(students):
    if not students:
        return 0
    #列表推导式
    total = sum(float(s['score']) for s in students)
    average_score = total / len(students)
    return average_score
    #计算列表中每一个元素的总和
    #sum([1,2,3])

def find_top_student(students):
    '''
    查找成绩最高的学生的信息
    :param students:[{'score':100,'name':'yabo','age':20},{},{}]
    :return:返回最高分学生的信息
    '''
    if not students:
        return None
    #max会返回成绩最高的学生的整体信息
    '''
    max(列表，key = lambda表达式) 第一个参数是接收的是一个students列表，第二个参数是让他依次对students列表中的
    每一个元素执行操作，取出其中的最大的
    '''
    return max(students, key=lambda s: s['score'])

def save_report(filename,students):
    '''
    将字典信息存储为json文件
    :param filename:json文件的路径
    :param students:学生信息
    :return:None
    '''
    try:
        report={
            'total' : len(students),
            'average_score': calculate_average_score(students),
            'top_student': find_top_student(students),
            'students': students
        }
        with open(filename,'w',encoding='utf-8') as f:
            #report 是json对象
            json.dump(report,f,indent=2,ensure_ascii=False)
            print(f'报告已经保存到{filename}')
    except Exception as e:
        print('错误，error is',e)

