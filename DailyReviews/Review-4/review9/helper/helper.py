import pandas as pd
from faker import Faker
def helper():
    fk = Faker()
    student_id_list = list(range(101,201))
    math_list = list(range(20,90))
    science_list = list(range(20,90))
    english_list = list(range(20,90))

    attendance_per_list = list(range(35,100))

    student_id = []
    math = []
    science = []
    english  = []
    attendance_per = []

    for i in range(200):
        student_id.append(fk.random.choice(student_id_list))
        math.append(fk.random.choice(math_list))
        science.append(fk.random.choice(science_list))
        english.append(fk.random.choice(english_list))
        attendance_per.append(fk.random.choice(attendance_per_list))

    return pd.DataFrame({
        'student_id': student_id,
        'math': math,
        'science': science,
        'english': english,
        'attendance_per': attendance_per
    })

if __name__ == '__main__':
    sample_data = helper()
    print(sample_data)