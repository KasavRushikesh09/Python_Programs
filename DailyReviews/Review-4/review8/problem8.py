from datetime import date

import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker
import random
from helper.helper import problem8

fk = Faker()
#generate data
month =[]
revenue = []
expenses = []

for _ in range(20):
    month.append(fk.date_between_dates(
        date_start=date(2024,1,1),
        date_end= date(2024,12,31)
    ))
    revenue.append(fk.random_int(min =1000,max=2000))
    expenses.append(fk.random_int(min=50,max=500))

#create dataframe
df = pd.DataFrame({
    'month':month,
    'revenue':revenue,
    'expenses':expenses
})

df = df.sort_values('month')
if __name__ == '__main__':

    plt.plot(df['month'],df['revenue'],label = 'revenue')
    plt.plot(df['month'], df['expenses'], label='expenses')
    plt.show()