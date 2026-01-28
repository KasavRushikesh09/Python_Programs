from datetime import date

import pandas as pd
from faker import Faker

def problem8():
    fk = Faker()
    min_month_list = date(2024,1,1)
    max_month_list = date(2024,12,1)

    min_revenue_list = 1000
    max_revenue_list = 2000

    min_expenses = 50
    max_expenses = 500

    month = []
    revenue = []
    expenses = []

    data = {
        'month':month,
        'revenue':revenue,
        'expenses':expenses
    }

    for i in range(20):
        month.append(fk.date_between_dates(min_month_list,max_month_list))
        revenue.append(fk.random_int(min_revenue_list,max_revenue_list))
        expenses.append(fk.random_int(min_expenses,max_expenses))
    return pd.DataFrame(data)

if __name__ == '__main__':
    sample_data = problem8()
    print(sample_data)


