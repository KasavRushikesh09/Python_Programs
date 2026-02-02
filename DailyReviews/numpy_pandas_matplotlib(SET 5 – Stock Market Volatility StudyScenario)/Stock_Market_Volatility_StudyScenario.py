import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from helper.helper import helper

def daily_return(df):
    df['daily_return'] = df['close_price'].pct_change()
    df['rolling_volality_20d'] = (df['daily_return'].rolling(window=20).std()).bfill()
    return df

#numpy tasks'
def

def future_stock_price(prices,days = 30):
    last_prices = prices[-1]

if __name__ == '__main__':
    sample_data = helper()
    result = daily_return(sample_data)
    print(result.head(25))