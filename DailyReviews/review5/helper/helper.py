import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# df = pd.DataFrame({
#
#     'dates' : pd.date_range(start='2024-02-02', periods=30),
#     'temp' : np.random.randint(20, 40, size=30)
#
# })
# print(df.head())
#
# avg_temp = df['temp'].mean()
# print(f'avgrage temp:\n{avg_temp}')
#
# hottest = df.loc[df['temp'].idxmax()]
# print(f'hottest temp:\n{hottest}')
#
# coldest = df.loc[df['temp'].idxmin()]
# print(f'coldest temp:\n{coldest}')
#
# # plt.figure()
# # plt.plot(df['dates'],df['temp'],marker='o')
# # plt.xticks(rotation=45)
# # plt.show()
#
#
# plt.figure()
# plt.scatter(hottest['dates'],hottest['temp'], marker = 'o')
# plt.scatter(coldest['dates'],coldest['temp'], marker = 'x')
# plt.legend()
# plt.xlabel('Date')
# plt.ylabel('Temperature')
# plt.title('Hottest and Coldest Days')
# plt.xticks(rotation=45)
# plt.show()



# df = pd.DataFrame({
#     'student': range(1,101),
#     'math':np.random.randint(35,90,size=100),
#     'sci':np.random.randint(35,90,size=100),
#     'eng':np.random.randint(35,90,size=100),
#     'chem':np.random.randint(35,90,size=100),
#     'phy':np.random.randint(35,90,size=100),
# })
# # print(df.head())
#
# df['sum'] = df[['math','sci','eng','chem','phy']].sum(axis=1)
# # print(df)
# avg_marks = df[['math','sci','eng','chem','phy']].mean()
#
# df['percentage'] = (df['sum'] / 500)*100
# df['percentage'] = df['percentage'].round()
# # print(df)
#
# df['result'] = np.where(df['percentage'] >= 40,'pass','fail')
# print(df)
#
# # plt.hist(df['percentage'], bins = 10)
# # plt.show()
#
# plt.figure(figsize=(8,5))
# plt.bar(avg_marks.index,avg_marks.values)
# plt.show()


df = pd.DataFrame({
    'dates' : pd.date_range(start='2024-02-01',periods = 180),
    'sales' : np.random.randint(2000,10000,size=180),
})

monthly_total = df[]
print(df.head())