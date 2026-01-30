'''SET 4 – Hospital Patient AnalyticsScenario
A hospital wants to analyze patient stay patterns and treatment costs.
Problem Statement
Create a dataset of at least 400 patients containing:

patient_id, age, gender, diagnosis, hospital_days, treatment_cost

Using Pandas:

Compute average hospital stay per diagnosis.

Segment patients into age groups.

Using NumPy:

Identify treatment cost anomalies.

Apply suitable transformations to normalize cost data.

Using a visualization library:

Compare hospital stay across diagnoses.

Visualize cost patterns across age groups.'''

from faker import Faker
import pandas as pd

def helper():
    fk = Faker()
    patient_id_list = [ i for i in range(101,201)]
    min_age = 18
    max_age = 45
    gender_list = ['female','male']
    diagnosis_list = [
        'Essential hypertension',
        'Diabetes mellitus',
        'Hyperlipidemia',
        'Lumbago',
        'Acute respiratory infections',
        'Osteoarthritis',
        'Depressive disorders'
    ]
    min_hospital_days = 10
    max_hospital_days = 30

    min_treatment_cost = 50000
    max_treatment_cost = 100000

    patient_id = []
    age =[]
    gender=[]
    diagnosis=[]
    hospital_days=[]
    treatment_cost=[]

    data = {
        'patient_id':patient_id,
        'age':age,
        'gender':gender,
        'diagnosis':diagnosis,
        'hospital_days':hospital_days,
        'treatment_cost':treatment_cost
    }

    for _ in range(400):
        patient_id.append(fk.random_element(patient_id_list))
        age.append(fk.random_int(min_age,max_age))
        gender.append(fk.random_element(gender_list))
        diagnosis.append(fk.random_element( diagnosis_list))
        hospital_days.append(fk.random_int(min_hospital_days,max_hospital_days))
        treatment_cost.append(fk.random_int(min_treatment_cost,max_treatment_cost))

    return pd.DataFrame(data)

if __name__ == '__main__':
    sample_data = helper()
    print(f'Sample data:\n{sample_data}')
