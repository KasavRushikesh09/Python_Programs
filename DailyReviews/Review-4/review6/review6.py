import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from faker import Faker

fk = Faker()

import random

df = pd.DataFrame({

     'Gender' : [random.choice(['Male','Female'])for _ in range(100)]
})
print(df)
value_counts = df['Gender'].value_counts()
# print(df['value_counts'])
#plot pie chart
value_counts.plot.pie(
    autopct='%1.1f%%',
    startangle = 90,
    title='Gender Distribution'
)
plt.ylabel(' ')
plt.show()
