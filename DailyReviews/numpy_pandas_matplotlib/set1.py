from helper.helper import e_commerce
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Pandas Tasks
def final_order_amount(df):
    total = df['price']*df['quantity']
    discount = total*df['discount_percent']/100
    df['final_amount'] = total-discount
    return df

def monthly_revenue(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')
    result = df.groupby(['month','product_category'])['final_amount'].sum()
    return result

def top_three_revenue(df):
    total_revenue =df.groupby('month')['final_amount'].sum()
    return total_revenue.sort_values(ascending=False).head(3)

#Numpy Tasks
def high_low(df):
    mean = np.mean(df['final_amount'])
    std  = np.std(df['final_amount'])

    high_orders = df[df['final_amount']>mean+2*std]
    low_orders = df[df['final_amount']<mean-2*std]
    return high_orders,low_orders

def replace_anomalies(df):
    values = df['final_amount'].to_numpy()
    mean = np.mean(values)
    std = np.std(values)
    lower = mean - 2 * std
    upper = mean + 2 * std
    df['clean_amount'] = np.clip(values, lower, upper)

    return df, lower, upper

#matplotlib tasks
import matplotlib.pyplot as plt

def plot_monthly_trend(df):
    # ensure datetime + month column
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')

    # total revenue per month
    monthly_total = df.groupby('month')['final_amount'].sum()

    # convert index for plotting
    monthly_total.index = monthly_total.index.astype(str)

    # plot
    plt.figure(figsize=(10, 5))
    plt.plot(monthly_total.index, monthly_total.values, marker='o')
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_revenue_distribution(df):
    if 'final_amount' not in df.columns:
        df = final_order_amount(df)

    grouped = [group['revenue'] for _, group in df.groupby('product_category')]
    labels = df['product_category'].unique()

    plt.figure(figsize= (10,6))
    plt.boxplot(grouped,labels = labels)
    plt.title("Revenue Distribution Across Categories")
    plt.xlabel('product category')
    plt.ylabel('revenue')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    sample_data = e_commerce()
    print(f'sample data:\n{sample_data}')
    # print(f'final order amount:\n{final_order_amount(sample_data)}')
    print(f'monthly revenue per product category:\n{monthly_revenue(sample_data)}')
    # print(f'total_revenue_per_month:\n{top_three_revenue(sample_data)}')
    sample_data = final_order_amount(sample_data)
    # high,low = high_low(sample_data)
    # print(f'High\n{high}')
    # print(f'Low\n{low}')
    # cleaned, lo, hi = replace_anomalies(sample_data)1
    # print("Lower cap:", lo)
    # print("Upper cap:", hi)
    # ample_data = final_order_amount(sample_data)
    # # print(cleaned[['final_amount', 'clean_amount']].head())
    # plot_monthly_trend(sample_data)
    print(plot_revenue_distribution(sample_data))