'''
Pandas (Intermediate)
 A DataFrame contains account_id, transaction_date, amount, and transaction_type.
Task:
     Aggregate daily transaction totals per account

     Identify accounts with unusually high transaction volume

     Detect potential fraud using statistical thresholds
'''

from helper.helper import banking_transaction
import pandas as pd

def daily_trans(df):
    daily_total = (
        df.groupby(['account_id','transaction_date'])['amount'].sum().reset_index())
    return daily_total

def high_trans_vol(df):
    acc_tran = (df.groupby('account_id')['amount'].sum().reset_index())
    sort = (acc_tran.sort_values(by="amount",ascending = False).head(3))
    return sort

def detect_fraud(df,k=3):
    mean = df['amount'].mean()
    std = df['amount'].std()

    threshold = mean+k*std
    fraud_cases = df[df['amount']>threshold]
    return fraud_cases,threshold
if __name__ == "__main__":
    sample_data = banking_transaction()
    fraud_df,threshold = detect_fraud(sample_data)
    print(f"Sample Data\n{sample_data}")
    print(f"daily_trans\n{daily_trans(sample_data)}")
    print(f"High Transaction Value\n{high_trans_vol(sample_data)}")
    print(f"fraud threshold: {threshold:.2f}")
    print("\nPotential Fraud Transaction:",fraud_df)