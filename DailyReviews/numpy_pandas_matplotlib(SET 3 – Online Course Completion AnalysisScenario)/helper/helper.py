from faker import Faker
import pandas as pd

def helper():
    fk = Faker()
    student_id_list = [i for i  in range(101,201)]
    course_name_list = [ "Python Basics",
    "Data Science",
    "Machine Learning",
    "Web Development",
    "Cyber Security",
    "Cloud Computing",
    "AI Fundamentals"]

    min_progress_per_list = 0
    max_progress_per_list = 100

    min_completion_days =  1
    max_completion_days = 90

    min_rating = 1
    max_rating = 5

    student_id = []
    course_name  = []
    progress_percent = []
    completion_days = []
    rating = []

    data = {
        'student_id' : student_id,
        'course_name' : course_name,
        'progress_percent':progress_percent,
        'completion_days':completion_days,
        'rating':rating
    }

    for _ in range(300):
        student_id.append(fk.random_element(student_id_list))
        course_name.append(fk.random_element(course_name_list))
        progress_percent.append(fk.random_int(min_progress_per_list,max_progress_per_list))
        completion_days.append(fk.random_int(min_completion_days,max_completion_days))
        rating.append(fk.random_int(min_rating,max_rating))
    return pd.DataFrame(data)

if __name__ == '__main__':
    sample_data = helper()
    print(f'sample data\n{sample_data}')