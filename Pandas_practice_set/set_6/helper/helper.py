from datetime import date
from faker import Faker
import pandas as pd

def healthcare_data():
    fk = Faker()
    patient_id_list = list( i for i in range(1,101))
    min_timespent = date(2024,1,1)
    max_timespent = date(2025,9,12)
    min_heart_rate = 20
    max_heart_rate = 150

    ward_list = list(i for i in range(1,70))

    patient_id = []
    timestamp = []
    heart_rate = []
    ward = []

    data = {
        'patient_id' : patient_id,
         'timestamp' : timestamp,
        'heart_rate' : heart_rate,
        'ward' : ward
    }

    for _ in range(332):
        patient_id.append(fk.random_element(patient_id_list))
        timestamp.append(fk.date_between_dates(min_timespent,max_timespent))
        heart_rate.append(fk.random_int(min_heart_rate,max_heart_rate))
        ward.append(fk.random_element(ward_list))

    return pd.DataFrame(data)

if __name__ == '__main__':
    print(healthcare_data())





