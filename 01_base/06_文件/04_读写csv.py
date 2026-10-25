# 读取 CSV
def read_csv(filename):
    students = []
    with open(filename, 'r', encoding='utf-8') as f:
        f.readline()  # 跳过表头
        for line in f:
            #line.rstrip('\n')
            name, age, score = line.rstrip('\n').split(',')
            students.append({
                'name': name,
                'age': int(age),
                'score': int(score)
            })
    return students

# 写入 CSV
def write_csv(filename, students):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('name,age,score\n')
        for student in students:
            line = f"{student['name']},{student['age']},{student['score']}\n"
            f.write(line)
if __name__ == '__main__':
    students = [{'name':'张亚博','age':18,'score':100},{'name':'ray','age':20,'score':150}]
    write_csv('students.csv', students)


