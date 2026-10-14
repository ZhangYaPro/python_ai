from info_utils import utils
if __name__ == '__main__':
    students = utils.read_students('./students.csv')
    print(students)
    print(utils.calculate_average_score(students))
    utils.save_report('students.json',students)