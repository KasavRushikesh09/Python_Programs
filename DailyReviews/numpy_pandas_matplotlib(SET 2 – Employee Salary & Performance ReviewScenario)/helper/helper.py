from faker import Faker
import pandas as pd

def helper():
    fk = Faker()
    emp_id_list = [i for i in range(101,201)]
    department_list = [ "HR",
    "Finance",
    "Marketing",
    "Sales",
    "IT",
    "Operations",
    "Customer Support",
    "Research",
    "Administration",
    "Logistics"]

    min_experience_year = 2
    max_experience_year = 15

    min_salary =15000
    max_salary = 50000

    min_performance_score = 1
    max_performance_score = 5

    emp_id = []
    department = []
    experience_year = []
    salary = []
    performance_score = []

    data = {
        'emp_id' : emp_id,
    'department' : department,
    'experience_year' : experience_year,
    'salary' : salary,
    'performance_score' : performance_score
    }

    for _ in  range(200):
        emp_id.append(fk.random_element(emp_id_list))
        department.append(fk.random_choices(department_list))
        experience_year.append(fk.random_int(min_experience_year,max_experience_year))
        salary.append(fk.random_int(min_salary,max_salary))
        performance_score.append(fk.random_int(min_performance_score,max_performance_score))

    return pd.DataFrame(data)

if __name__ == '__main__':
    sample_data = helper()
    print(f'sample data\n:{sample_data}')


