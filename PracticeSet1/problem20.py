# num = int(input())
# while num>= 10:
#     digit_sum = 0
#     temp = num
#     while temp >0:
#         digit_sum += temp%10
#         temp  = temp//10
#     num = num-digit_sum
# print(num)

import numpy as np
import pandas as pd

def sample():
    data = {
        'student':['s1','s2','s3','s4','s5'],
        'math':(np.random.randint(0,100,5)),
        'sci':(np.random.randint(0,100,5)),
        'eng':(np.random.randint(0,100,5)),
        'chem':(np.random.randint(0,100,5)),
    }
    return pd.DataFrame(data)

def sum(df):
    df['sum_mark'] = df[['math','sci','eng','chem']].sum(axis=1)
    return df

def normalize(df):
    normalize = (df['sum_mark'] - df['sum_mark'].min())/(df['sum_mark'].max() - df['sum_mark'].min())
    df['normalize'] = normalize
    return df


if __name__ == '__main__':
    df = sample()
    print(df)
    print(sum(df))
    print(normalize(df))
