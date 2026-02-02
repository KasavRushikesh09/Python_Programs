import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#






# def categorize_aqi(aqi):
#     if aqi <= 100:
#         return 'Good'
#     elif aqi <= 200:
#         return 'Moderate'
#     else:
#         return 'Poor'
#
# df['aqi_category'] = df['aqi'].apply(categorize_aqi)
# df.head()
# poor_aqi_count = (
#     df[df['aqi_category'] == 'Poor']
#     .groupby('city')
#     .size()
# )
#
# poor_aqi_count