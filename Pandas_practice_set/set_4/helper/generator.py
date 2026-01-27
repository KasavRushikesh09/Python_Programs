"""A DataFrame contains student_id, course_id, login_date, and minutes_spent."""

from faker import Faker
import pandas as pd
from datetime import date

def generator_student_df():
    fk = Faker()

    student_id_list = list(i for i in range(50))
    course_id_list = ["C1","C2","C3","C4","C5"]

    max_login_date = date(2025,11,21)
    min_login_date = date(2021,1,1)

    max_time_spent = 8*60
    min_time_spent = 3*60

    student_id = []
    course_id = []
    login_date = []
    minutes_spent = []


    data = {
        'student_id' : student_id,
        'course_id' : course_id,
        'login_date': login_date,
        'minutes_spent': minutes_spent
    }

    for _ in range(333):
        student_id.append(fk.random_element(student_id_list))
        course_id.append(fk.random_element(course_id_list))
        login_date.append(fk.date_between_dates(date_start = min_login_date,date_end = max_login_date))
        minutes_spent.append(fk.random_int(min_time_spent,max_time_spent))
    return pd.DataFrame(data)

if __name__ == '__main__':
    print(generator_student_df().head())













# from faker import Faker
# import pandas as pd
# from datetime import date
# def generator_student_df():
#     fk = Faker()
#
#     stduent_id_list = list(i for i in range(1,51))
#     course_id_list = ["C1","C2","C3","C4","C5"]
#
#     min_date = date(2021,1,1)
#     max_date = date(2025,12,31)
#
#
#     min_time = 3*60
#     max_time = 7*60
#
#     student_id = []
#     course_id = []
#     login_date = []
#     minutes_spent = []
#
#     data = {
#         'student_id': student_id,
#         'course_id': course_id,
#         'login_date': login_date,
#         'minutes_spent': minutes_spent
#     }
#
#     for _ in range(333):
#         student_id.append(fk.random_element(stduent_id_list))
#         course_id.append(fk.random_element(course_id_list))
#         login_date.append(fk.date_between_dates(min_date, max_date))
#         minutes_spent.append(fk.random_int(min_time, max_time))
#
#     return pd.DataFrame(data)
#
# if __name__ == '__main__':
#     print(generator_student_df().head())