from datetime import date

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from faker import Faker
def helper():
    fk = Faker()
    min_date = date(2024,2,2)
    max_date = date(2025,1,1)

    dates = pd.bdate_range(start=min_date,end=max_date)
    n_days = len(dates)
    open_price = np.random.randint(1000,5000,size=n_days)
    price_change = np.random.randint(-200,200,size=n_days)
    close_price = open_price+price_change

    volume = np.random.randint(1000000,10000000,size = n_days)

    df = pd.DataFrame({
        'date':dates,
        'open_price':open_price,
        'close_price':close_price,
        'volume':volume
    })

    return df

if __name__ == '__main__':
    # sample_data = helper()
    df = helper()
    print(df.head())