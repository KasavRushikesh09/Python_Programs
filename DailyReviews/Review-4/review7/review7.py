import pandas as pd
import matplotlib.pyplot as plt
from helper.helper import problem7
from datetime import datetime,timedelta
import random
#generate 10 dates
dates = [datetime.now() - timedelta(days=i)for i in range(9,-1,-1)]
#create Dataframe
df = pd.DataFrame({
    'date' : dates,
    'temperature' : [random.randint(20,40) for _ in range(10)]
})

#concert date to datetime
df['date'] = pd.to_datetime(df['date'])

#plt
plt.plot(df['date'],df['temperature'])
plt.grid()
plt.show()