from datetime import date

import pandas as pd
from faker import Faker
def problem7():
    fk = Faker()
    min_dates = date(2025,12,1)
    max_dates = date(2025,12,10)

    min_temp = -10
    max_temp = 20

    dates = []
    temperature = []

    data = {
        'dates' : dates,
        'temperature' : temperature
    }

    for _ in range(10):
        dates.append(fk.date_between_dates(min_dates,max_dates))
        temperature.append(fk.random_int(min_temp,max_temp))

    return pd.DataFrame(data)

if __name__ == '__main__':
    sample_data = problem7()
    print(sample_data)